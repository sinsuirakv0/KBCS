# v15.7.4 → v16.0.0 · 最優先の変更候補 (67)

[一覧の目次](README.md)

<a id="compare-9cd7f7a17d1c7bc6b562290b7619fa80"></a>

### [`00b5e964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e964.md) → [`00bcde64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcde64.md) _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c00.md) · 呼出先 7件 [`00b603b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b603b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)
- 新版 呼出元 1件 [`00c5d800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d800.md) · 呼出先 7件 [`00bcf8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.86% / 新版 75.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e998"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e9ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5e9b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5e998",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5e9e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0b60"
      ]
    ],
    [
      "00bcdef0",
      "READ",
      [
        "storage",
        "00c1bbb8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bcde98",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bcdee8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5d760"
      ]
    ],
    [
      "00bcdef0",
      "READ",
      [
        "storage",
        "00c9b5e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e964.md#insn-00b5e998) · [`00b5e9ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e964.md#insn-00b5e9ac) · [`00b5e9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e964.md#insn-00b5e9b8)

~~~diff
- 00b5e998 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b5e998 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5e998 bytes e80f00f9
- 00b5e9ac ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b5e9ac ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b5e9ac ["INT_ADD", "register:4040:8", ["register:4040:8", "const:38:8"]]
- 00b5e9ac ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00b5e9ac bytes 1f8d03f8
- 00b5e9b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b5e9b8 ["INT_ADD", "register:40b8:8", ["register:40b8:8", "const:30:8"]]
- 00b5e9b8 ["STORE", null, ["const:1b1:8", "register:40b8:8", "tmp:0:8"]]
- 00b5e9b8 bytes e80e03f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea9f495f397cdf341b7ce001427dff43"></a>

### [`00b5eab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5eab0.md) → [`00bcdfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcdfb0.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0cd0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bc0.md)
- 新版 呼出元 1件 [`00c5d8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8d0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7c0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.85% / 新版 78.85%

CFGの説明率　旧版 33.33% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5eab4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5eab4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5eab8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5eab4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5eab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5eabc",
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
      "00bcdfb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bcdfb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bcdfbc",
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

- 旧版 [`00b5eab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5eab0.md#insn-00b5eab4) · [`00b5eab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5eab0.md#insn-00b5eab8) · [`00b5eabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5eab0.md#insn-00b5eabc)

~~~diff
- 00b5eab4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5eab4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5eab4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5eab4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5eab4 bytes f65704a9
- 00b5eab8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b5eab8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b5eab8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b5eab8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5eab8 bytes f44f05a9
- 00b5eabc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b5eabc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b5eabc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b5eabc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5eabc bytes fd7b06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0623df3e8fee2a4101f539a26fd18c2f"></a>

### [`00b5ebb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ebb4.md) → [`00bce0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce0b4.md) _ZN8firebase4auth4Auth20SignInWithCredentialERKNS0_10CredentialE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b607e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b607e4.md) [`00b65314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b65/00b65314.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcfce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfce4.md) [`00bd4814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4814.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 16.13% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ecc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ecc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bce1c0"
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
      "unmatched:00b5ec4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ],
    [
      "00bce15c",
      "READ",
      [
        "storage",
        "010a1498",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5ecbc",
      "READ",
      [
        "storage",
        "00c1bbf8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bce14c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ],
    [
      "00bce15c",
      "READ",
      [
        "storage",
        "011263a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bce1bc",
      "READ",
      [
        "storage",
        "00c9b628",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ebfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ebb4.md#insn-00b5ebfc) · [`00b5ec34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ebb4.md#insn-00b5ec34) · [`00b5ec44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ebb4.md#insn-00b5ec44)
- 新版 `00bce0fc`（命令位置の公開資料なし） · `00bce144`（命令位置の公開資料なし）

~~~diff
- 00b5ebfc ["INT_ADD", "register:40f0:8", ["const:b5ebfc:8", "const:4:8"]]
- 00b5ebfc ["CALL", null, ["callee:00c5d810:8"]]
+ 00bce0fc ["INT_ADD", "register:40f0:8", ["const:bce0fc:8", "const:4:8"]]
+ 00bce0fc ["CALL", null, ["callee:00c5d810:8"]]
- 00b5ebfc bytes 05080294
+ 00bce0fc bytes c53d0294
- 00b5ec34 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b5ec34 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b5ec34 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b5ec34 ["COPY", "register:4018:8", ["tmp:0:8"]]
- 00b5ec34 bytes 4301899a
- 00b5ec44 ["INT_ADD", "register:40f0:8", ["const:b5ec44:8", "const:4:8"]]
- 00b5ec44 ["CALL", null, ["callee:00c5d7e0:8"]]
+ 00bce144 ["INT_ADD", "register:40f0:8", ["const:bce144:8", "const:4:8"]]
+ 00bce144 ["CALL", null, ["callee:00c5d7e0:8"]]
- 00b5ec44 bytes e7070294
+ 00bce144 bytes a73d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d645377c760c1a35a64f05186c8e4ab2"></a>

### [`00b5eda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5eda0.md) → [`00bce2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce2a0.md) _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth4UserEEENS_16SafeFutureHandleIT_EEi

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c10.md) · 呼出先 7件 [`00b606c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b606c8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)
- 新版 呼出元 1件 [`00c5d810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d810.md) · 呼出先 7件 [`00bcfbc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfbc8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bce2dc",
      "value": [
        "leaf",
        "ram:c5d760:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5eddc",
      "value": [
        "leaf",
        "ram:be0b60:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bce2e4",
      "incomplete_value": true,
      "site": "00bce2f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ede4",
      "incomplete_value": true,
      "site": "00b5edf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 2,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bce30c",
      "value": [
        "leaf",
        "ram:c5a690:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5ee0c",
      "value": [
        "leaf",
        "ram:bddc40:8"
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
      "00bce2dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0b60"
      ]
    ],
    [
      "00bce2e4",
      "READ",
      [
        "storage",
        "00c1bbc8",
        null,
        "pointer"
      ]
    ],
    [
      "00bce2e4",
      "PARAM",
      [
        "storage",
        "00b606c8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4UserEEEvPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bce2dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5d760"
      ]
    ],
    [
      "00bce2e4",
      "READ",
      [
        "storage",
        "00c9b5f8",
        null,
        "pointer"
      ]
    ],
    [
      "00bce2e4",
      "PARAM",
      [
        "storage",
        "00bcfbc8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth4UserEEEvPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5eddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5eda0.md#insn-00b5eddc) · [`00b5edf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5eda0.md#insn-00b5edf8) · [`00b5ee0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5eda0.md#insn-00b5ee0c)
- 新版 `00bce2dc`（命令位置の公開資料なし） · `00bce2f8`（命令位置の公開資料なし） · `00bce30c`（命令位置の公開資料なし）

~~~diff
- 00b5eddc ["INT_ADD", "register:40f0:8", ["const:b5eddc:8", "const:4:8"]]
- 00b5eddc ["CALL", null, ["ram:be0b60:8"]]
+ 00bce2dc ["INT_ADD", "register:40f0:8", ["const:bce2dc:8", "const:4:8"]]
+ 00bce2dc ["CALL", null, ["ram:c5d760:8"]]
- 00b5eddc bytes 61070294
+ 00bce2dc bytes 213d0294
- 00b5edf8 ["INT_ADD", "register:40f0:8", ["const:b5edf8:8", "const:4:8"]]
- 00b5edf8 ["CALL", null, ["callee:00c5aa40:8"]]
+ 00bce2f8 ["INT_ADD", "register:40f0:8", ["const:bce2f8:8", "const:4:8"]]
+ 00bce2f8 ["CALL", null, ["callee:00c5aa40:8"]]
- 00b5edf8 bytes 72fc0194
+ 00bce2f8 bytes d2310294
- 00b5ee0c ["INT_ADD", "register:40f0:8", ["const:b5ee0c:8", "const:4:8"]]
- 00b5ee0c ["CALL", null, ["ram:bddc40:8"]]
+ 00bce30c ["INT_ADD", "register:40f0:8", ["const:bce30c:8", "const:4:8"]]
+ 00bce30c ["CALL", null, ["ram:c5a690:8"]]
- 00b5ee0c bytes 8dfb0194
+ 00bce30c bytes e1300294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6bbfc3960d10d417ce25e869420425e"></a>

### [`00b5ee64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ee64.md) → [`00bce364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce364.md) _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4UserEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0cf0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0be0.md)
- 新版 呼出元 1件 [`00c5d8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d8f0.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7e0.md)

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
      "site": "00bce3e0",
      "value": [
        "leaf",
        "ram:c5a690:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5eee0",
      "value": [
        "leaf",
        "ram:bddc40:8"
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
      "00bce3e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ]
  ],
  "added": [
    [
      "00bce3e0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5eee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ee64.md#insn-00b5eee0) · [`00b5ee98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ee64.md#insn-00b5ee98) · [`00b5eeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ee64.md#insn-00b5eeac)
- 新版 `00bce3e0`（命令位置の公開資料なし） · `00bce398`（命令位置の公開資料なし） · `00bce3ac`（命令位置の公開資料なし）

~~~diff
- 00b5eee0 ["INT_ADD", "register:40f0:8", ["const:b5eee0:8", "const:4:8"]]
- 00b5eee0 ["CALL", null, ["ram:bddc40:8"]]
+ 00bce3e0 ["INT_ADD", "register:40f0:8", ["const:bce3e0:8", "const:4:8"]]
+ 00bce3e0 ["CALL", null, ["ram:c5a690:8"]]
- 00b5eee0 bytes 58fb0194
+ 00bce3e0 bytes ac300294
- 00b5ee98 ["INT_ADD", "register:40f0:8", ["const:b5ee98:8", "const:4:8"]]
- 00b5ee98 ["CALL", null, ["callee:00c5d910:8"]]
+ 00bce398 ["INT_ADD", "register:40f0:8", ["const:bce398:8", "const:4:8"]]
+ 00bce398 ["CALL", null, ["callee:00c5d910:8"]]
- 00b5ee98 bytes 9e070294
+ 00bce398 bytes 5e3d0294
- 00b5eeac ["INT_ADD", "register:40f0:8", ["const:b5eeac:8", "const:4:8"]]
- 00b5eeac ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bce3ac ["INT_ADD", "register:40f0:8", ["const:bce3ac:8", "const:4:8"]]
+ 00bce3ac ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5eeac bytes 35fc0194
+ 00bce3ac bytes 95310294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6320b095459419ba3ac0bae2ce8a063"></a>

### [`00b5ef68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ef68.md) → [`00bce468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce468.md) _ZN8firebase4auth4Auth35SignInAndRetrieveDataWithCredentialERKNS0_10CredentialE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb90.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b6041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b6041c.md) [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00c5a5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5e0.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 96.19% / 新版 96.19%

CFGの説明率　旧版 50.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bce574",
      "incomplete_value": true,
      "site": "00bce574",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:620:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f074",
      "incomplete_value": true,
      "site": "00b5f074",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf0:8"
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
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bce500",
      "value": [
        "leaf",
        "ram:c5a690:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b5f000",
      "value": [
        "leaf",
        "ram:bddc40:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bce510",
      "incomplete_value": true,
      "site": "00bce520",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f010",
      "incomplete_value": true,
      "site": "00b5f020",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:498:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bce500",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ],
    [
      "00bce510",
      "READ",
      [
        "storage",
        "010a1498",
        null,
        "undefined8"
      ]
    ],
    [
      "00bce570",
      "READ",
      [
        "storage",
        "00c1bbf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bce500",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ],
    [
      "00bce510",
      "READ",
      [
        "storage",
        "011263a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bce570",
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ef68.md#insn-00b5f000) · [`00b5f020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ef68.md#insn-00b5f020) · [`00b5f0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ef68.md#insn-00b5f0a4)
- 新版 `00bce500`（命令位置の公開資料なし） · `00bce520`（命令位置の公開資料なし） · `00bce5a4`（命令位置の公開資料なし）

~~~diff
- 00b5f000 ["INT_ADD", "register:40f0:8", ["const:b5f000:8", "const:4:8"]]
- 00b5f000 ["CALL", null, ["ram:bddc40:8"]]
+ 00bce500 ["INT_ADD", "register:40f0:8", ["const:bce500:8", "const:4:8"]]
+ 00bce500 ["CALL", null, ["ram:c5a690:8"]]
- 00b5f000 bytes 10fb0194
+ 00bce500 bytes 64300294
- 00b5f020 ["INT_ADD", "register:40f0:8", ["const:b5f020:8", "const:4:8"]]
- 00b5f020 ["CALL", null, ["callee:004977f4:8"]]
+ 00bce520 ["INT_ADD", "register:40f0:8", ["const:bce520:8", "const:4:8"]]
+ 00bce520 ["CALL", null, ["callee:004977f4:8"]]
- 00b5f020 bytes 4f56e497
+ 00bce520 bytes b524e397
- 00b5f0a4 ["INT_ADD", "register:40f0:8", ["const:b5f0a4:8", "const:4:8"]]
- 00b5f0a4 ["CALL", null, ["callee:00c5ab40:8"]]
+ 00bce5a4 ["INT_ADD", "register:40f0:8", ["const:bce5a4:8", "const:4:8"]]
+ 00bce5a4 ["CALL", null, ["callee:00c5ab40:8"]]
- 00b5f0a4 bytes 07fc0194
+ 00bce5a4 bytes 67310294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebfa2ab04a9cb866c13eae19a1584c61"></a>

### [`00b5f154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f154.md) → [`00bce654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce654.md) _ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd30.md) · 呼出先 3件 [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5a790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a790.md) · 呼出先 3件 [`00c5a7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7e0.md) [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 50.00% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f194"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f1a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b5f1a4",
      "incomplete_value": true,
      "site": "00b5f1b4",
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
            "const:30:8"
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
      "unmatched:00b5f190",
      "PARAM",
      [
        "storage",
        "002a5154",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b5f194",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ],
    [
      "unmatched:00b5f1a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ]
  ],
  "added": [
    [
      "00bce690",
      "PARAM",
      [
        "storage",
        "002b5b82",
        null,
        "string"
      ]
    ],
    [
      "00bce694",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ac00"
      ]
    ],
    [
      "00bce6a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f154.md#insn-00b5f194) · [`00b5f1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f154.md#insn-00b5f1a0) · [`00b5f1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f154.md#insn-00b5f1b4)
- 新版 `00bce6b4`（命令位置の公開資料なし）

~~~diff
- 00b5f194 ["INT_ADD", "register:40f0:8", ["const:b5f194:8", "const:4:8"]]
- 00b5f194 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b5f194 bytes fbfb0194
- 00b5f1a0 ["INT_ADD", "register:40f0:8", ["const:b5f1a0:8", "const:4:8"]]
- 00b5f1a0 ["CALL", null, ["ram:bdde10:8"]]
- 00b5f1a0 bytes 1cfb0194
- 00b5f1b4 ["INT_ADD", "register:40f0:8", ["const:b5f1b4:8", "const:4:8"]]
- 00b5f1b4 ["CALL", null, ["callee:00c5a7e0:8"]]
+ 00bce6b4 ["INT_ADD", "register:40f0:8", ["const:bce6b4:8", "const:4:8"]]
+ 00bce6b4 ["CALL", null, ["callee:00c5a7e0:8"]]
- 00b5f1b4 bytes f3fa0194
+ 00bce6b4 bytes 4b300294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f385bd1e99e306d7f99f08ce556e5947"></a>

### [`00b5f1d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f1d8.md) → [`00bce6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce6d8.md) _ZN8firebase4auth4Auth17SignInAnonymouslyEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b6041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b6041c.md) [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 12件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 16.67% / 新版 5.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f1dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f1dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f1e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5f1dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f1e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f1e4",
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
      "00bce6dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bce6e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bce6e4",
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

- 旧版 [`00b5f1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f1d8.md#insn-00b5f1dc) · [`00b5f1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f1d8.md#insn-00b5f1e0) · [`00b5f1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f1d8.md#insn-00b5f1e4)

~~~diff
- 00b5f1dc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b5f1dc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b5f1dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b5f1dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f1dc bytes fa6703a9
- 00b5f1e0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5f1e0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5f1e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5f1e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f1e0 bytes f85f04a9
- 00b5f1e4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5f1e4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5f1e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b5f1e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f1e4 bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc90ee09d04b057f55dee4960bd299a4"></a>

### [`00b5f364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f364.md) → [`00bce864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce864.md) _ZN8firebase4auth4Auth26SignInWithEmailAndPasswordEPKcS3_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b6041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b6041c.md) [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.25% / 新版 92.25%

CFGの説明率　旧版 11.76% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f398"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bce9a8",
      "incomplete_value": true,
      "site": "00bce9a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:620:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f4a8",
      "incomplete_value": true,
      "site": "00b5f4a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf0:8"
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
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bce898"
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
      "unmatched:00b5f398",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bce914",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bce9a4",
      "READ",
      [
        "storage",
        "00c1bbf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bce898",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bce914",
      "READ",
      [
        "storage",
        "011263b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bce9a4",
      "READ",
      [
        "storage",
        "00c9b620",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f364.md#insn-00b5f398) · [`00b5f42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f364.md#insn-00b5f42c) · [`00b5f478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f364.md#insn-00b5f478)
- 新版 `00bce92c`（命令位置の公開資料なし） · `00bce978`（命令位置の公開資料なし）

~~~diff
- 00b5f398 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b5f398 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5f398 bytes e81f00f9
- 00b5f42c ["INT_ADD", "register:40f0:8", ["const:b5f42c:8", "const:4:8"]]
- 00b5f42c ["CALL", null, ["callee:004977f4:8"]]
+ 00bce92c ["INT_ADD", "register:40f0:8", ["const:bce92c:8", "const:4:8"]]
+ 00bce92c ["CALL", null, ["callee:004977f4:8"]]
- 00b5f42c bytes 4c55e497
+ 00bce92c bytes b223e397
- 00b5f478 ["INT_ADD", "register:40f0:8", ["const:b5f478:8", "const:4:8"]]
- 00b5f478 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bce978 ["INT_ADD", "register:40f0:8", ["const:bce978:8", "const:4:8"]]
+ 00bce978 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b5f478 bytes c2fa0194
+ 00bce978 bytes 22300294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30e6b3df9c54cccb8ae9d27e56d4d7e0"></a>

### [`00b5f5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f5f0.md) → [`00bceaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceaf0.md) _ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b6041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b6041c.md) [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 14件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bcf91c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf91c.md) [`00bd4404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd4/00bd4404.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.03% / 新版 88.03%

CFGの説明率　旧版 40.74% / 新版 44.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f5f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f5f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5f5f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5f5f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f5f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5f5fc",
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
      "00bceaf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bceaf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bceafc",
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

- 旧版 [`00b5f5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f5f0.md#insn-00b5f5f4) · [`00b5f5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f5f0.md#insn-00b5f5f8) · [`00b5f5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f5f0.md#insn-00b5f5fc)

~~~diff
- 00b5f5f4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b5f5f4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b5f5f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b5f5f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f5f4 bytes fa6704a9
- 00b5f5f8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b5f5f8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b5f5f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b5f5f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f5f8 bytes f85f05a9
- 00b5f5fc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b5f5fc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b5f5fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b5f5fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b5f5fc bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aedef29598991fbb4a88fc44cbe09a41"></a>

### [`00b5f974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f974.md) → [`00bcee74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bcee74.md) _ZNK8firebase4auth4Auth13language_codeEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde510.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md) [`00c5af90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5af90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 42.86% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bceea4",
      "incomplete_value": true,
      "site": "00bceeb0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:348:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f9a4",
      "incomplete_value": true,
      "site": "00b5f9b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:440:8"
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
      "00bceea4",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bceea4",
      "READ",
      [
        "storage",
        "01126348",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f974.md#insn-00b5f9b0) · [`00b5f98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f974.md#insn-00b5f98c) · [`00b5f998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f974.md#insn-00b5f998)
- 新版 `00bceeb0`（命令位置の公開資料なし） · `00bcee8c`（命令位置の公開資料なし） · `00bcee98`（命令位置の公開資料なし）

~~~diff
- 00b5f9b0 ["INT_ADD", "register:40f0:8", ["const:b5f9b0:8", "const:4:8"]]
- 00b5f9b0 ["CALL", null, ["callee:004977f4:8"]]
+ 00bceeb0 ["INT_ADD", "register:40f0:8", ["const:bceeb0:8", "const:4:8"]]
+ 00bceeb0 ["CALL", null, ["callee:004977f4:8"]]
- 00b5f9b0 bytes eb53e497
+ 00bceeb0 bytes 5122e397
- 00b5f98c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b5f98c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bcee8c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00bcee8c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b5f98c bytes c90200b4
+ 00bcee8c bytes c90200b4
- 00b5f998 ["INT_ADD", "register:40f0:8", ["const:b5f998:8", "const:4:8"]]
- 00b5f998 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bcee98 ["INT_ADD", "register:40f0:8", ["const:bcee98:8", "const:4:8"]]
+ 00bcee98 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b5f998 bytes 1afa0194
+ 00bcee98 bytes 7a2f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4686213eb7a61ab76b00497d6cae27c"></a>

### [`00b5f9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f9fc.md) → [`00bceefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bceefc.md) _ZN8firebase4auth4Auth17set_language_codeEPKc

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 37.50% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcef18",
      "incomplete_value": true,
      "site": "00bcef20",
      "value": [
        "LOAD",
        "8",
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
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcef4c",
      "incomplete_value": true,
      "site": "00bcef5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "definition_site": "00b5fa4c",
      "incomplete_value": true,
      "site": "00b5fa5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:448:8"
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
      "00bcef4c",
      "READ",
      [
        "storage",
        "010a1448",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcef4c",
      "READ",
      [
        "storage",
        "01126350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5fa20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f9fc.md#insn-00b5fa20) · [`00b5fa5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f9fc.md#insn-00b5fa5c) · [`00b5fa10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f9fc.md#insn-00b5fa10)
- 新版 `00bcef20`（命令位置の公開資料なし） · `00bcef5c`（命令位置の公開資料なし） · `00bcef10`（命令位置の公開資料なし）

~~~diff
- 00b5fa20 ["INT_ADD", "register:40f0:8", ["const:b5fa20:8", "const:4:8"]]
- 00b5fa20 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bcef20 ["INT_ADD", "register:40f0:8", ["const:bcef20:8", "const:4:8"]]
+ 00bcef20 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b5fa20 bytes f8f90194
+ 00bcef20 bytes 582f0294
- 00b5fa5c ["INT_ADD", "register:40f0:8", ["const:b5fa5c:8", "const:4:8"]]
- 00b5fa5c ["CALL", null, ["callee:00574cac:8"]]
+ 00bcef5c ["INT_ADD", "register:40f0:8", ["const:bcef5c:8", "const:4:8"]]
+ 00bcef5c ["CALL", null, ["callee:00574cac:8"]]
- 00b5fa5c bytes eec8e797
+ 00bcef5c bytes 5497e697
- 00b5fa10 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5fa10 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bcef10 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcef10 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b5fa10 bytes e80300b4
+ 00bcef10 bytes e80300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f11c7eb64d4c25042d9c286d07daaa5"></a>

### [`00b5fa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fa9c.md) → [`00bcef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bcef9c.md) _ZN8firebase4auth4Auth14UseAppLanguageEv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcefc4",
      "incomplete_value": true,
      "site": "00bcefd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:358:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5fac4",
      "incomplete_value": true,
      "site": "00b5fad0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:450:8"
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
      "00bcefc4",
      "READ",
      [
        "storage",
        "010a1450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcefc4",
      "READ",
      [
        "storage",
        "01126358",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5fad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fa9c.md#insn-00b5fad0) · [`00b5faac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fa9c.md#insn-00b5faac) · [`00b5fab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fa9c.md#insn-00b5fab8)
- 新版 `00bcefd0`（命令位置の公開資料なし） · `00bcefac`（命令位置の公開資料なし） · `00bcefb8`（命令位置の公開資料なし）

~~~diff
- 00b5fad0 ["INT_ADD", "register:40f0:8", ["const:b5fad0:8", "const:4:8"]]
- 00b5fad0 ["CALL", null, ["callee:00574cac:8"]]
+ 00bcefd0 ["INT_ADD", "register:40f0:8", ["const:bcefd0:8", "const:4:8"]]
+ 00bcefd0 ["CALL", null, ["callee:00574cac:8"]]
- 00b5fad0 bytes d1c8e797
+ 00bcefd0 bytes 3797e697
- 00b5faac ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b5faac ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bcefac ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bcefac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b5faac bytes c80100b4
+ 00bcefac bytes c80100b4
- 00b5fab8 ["INT_ADD", "register:40f0:8", ["const:b5fab8:8", "const:4:8"]]
- 00b5fab8 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bcefb8 ["INT_ADD", "register:40f0:8", ["const:bcefb8:8", "const:4:8"]]
+ 00bcefb8 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b5fab8 bytes d2f90194
+ 00bcefb8 bytes 322f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47076ad15d0f29ea50ec286b721d9805"></a>

### [`00b5fb88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fb88.md) → [`00bcf088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf088.md) _ZN8firebase4auth4Auth22SendPasswordResetEmailEPKc

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b60b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60b98.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 0件  · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00bd0098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.26% / 新版 82.26%

CFGの説明率　旧版 23.81% / 新版 29.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fbbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcf0bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5fd54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b5fbbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b5fbec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ],
    [
      "00bcf128",
      "READ",
      [
        "storage",
        "010a14b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bcf0bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00bcf0ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ],
    [
      "00bcf128",
      "READ",
      [
        "storage",
        "011263c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5fbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fb88.md#insn-00b5fbbc) · [`00b5fbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fb88.md#insn-00b5fbec) · [`00b5fc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fb88.md#insn-00b5fc08)
- 新版 `00bcf108`（命令位置の公開資料なし）

~~~diff
- 00b5fbbc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00b5fbbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b5fbbc bytes e82700f9
- 00b5fbec ["INT_ADD", "register:40f0:8", ["const:b5fbec:8", "const:4:8"]]
- 00b5fbec ["CALL", null, ["ram:bddc40:8"]]
- 00b5fbec bytes 15f80194
- 00b5fc08 ["INT_ADD", "register:40f0:8", ["const:b5fc08:8", "const:4:8"]]
- 00b5fc08 ["CALL", null, ["callee:00c5ac80:8"]]
+ 00bcf108 ["INT_ADD", "register:40f0:8", ["const:bcf108:8", "const:4:8"]]
+ 00bcf108 ["CALL", null, ["callee:00c5ac80:8"]]
- 00b5fc08 bytes 7ef90194
+ 00bcf108 bytes de2e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-404ed3a8b8c7d329becb29b2d9df8845"></a>

### [`00b5fed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fed8.md) → [`00bcf3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf3d8.md) _ZN8firebase4auth4Auth11UseEmulatorENSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEj

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ac80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf428",
      "incomplete_value": true,
      "site": "00bcf43c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:388:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ff28",
      "incomplete_value": true,
      "site": "00b5ff3c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
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
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b5ff50"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bcf450"
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
      "unmatched:00b5ff28",
      "READ",
      [
        "storage",
        "010a1480",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b5ff50",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcf428",
      "READ",
      [
        "storage",
        "01126388",
        null,
        "undefined8"
      ]
    ],
    [
      "00bcf450",
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

- 旧版 [`00b5ff3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fed8.md#insn-00b5ff3c) · [`00b5ff50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fed8.md#insn-00b5ff50)
- 新版 `00bcf43c`（命令位置の公開資料なし） · `00bcf450`（命令位置の公開資料なし）

~~~diff
- 00b5ff3c ["INT_ADD", "register:40f0:8", ["const:b5ff3c:8", "const:4:8"]]
- 00b5ff3c ["CALL", null, ["callee:00574cac:8"]]
+ 00bcf43c ["INT_ADD", "register:40f0:8", ["const:bcf43c:8", "const:4:8"]]
+ 00bcf43c ["CALL", null, ["callee:00574cac:8"]]
- 00b5ff3c bytes b6c7e797
+ 00bcf43c bytes 1c96e697
- 00b5ff50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5ff50 ["INT_ADD", "register:40f0:8", ["const:b5ff50:8", "const:4:8"]]
- 00b5ff50 ["CALLIND", null, ["register:0:8"]]
- 00b5ff50 bytes 00013fd6
+ 00bcf450 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcf450 ["INT_ADD", "register:40f0:8", ["const:bcf450:8", "const:4:8"]]
+ 00bcf450 ["CALLIND", null, ["register:0:8"]]
+ 00bcf450 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab1da60d8e74a3c5dec76e9d0fc43a86"></a>

### [`00b5fffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fffc.md) → [`00bcf4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf4fc.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHand

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bd0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7d0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 28.57% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf560",
      "incomplete_value": false,
      "site": "00bcf564",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60060",
      "incomplete_value": false,
      "site": "00b60064",
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
            "const:467:8"
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
    "new": null,
    "old": {
      "definition_site": "00b60068",
      "incomplete_value": true,
      "site": "00b60078",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6006c",
      "incomplete_value": true,
      "site": "00b60078",
      "value": [
        "live",
        "register:40b0:8"
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
      "unmatched:00b60060",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcf560",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fffc.md#insn-00b60064) · [`00b60078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fffc.md#insn-00b60078) · [`00b60084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fffc.md#insn-00b60084)
- 新版 `00bcf564`（命令位置の公開資料なし） · `00bcf578`（命令位置の公開資料なし） · `00bcf584`（命令位置の公開資料なし）

~~~diff
- 00b60064 ["INT_ADD", "register:40f0:8", ["const:b60064:8", "const:4:8"]]
- 00b60064 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bcf564 ["INT_ADD", "register:40f0:8", ["const:bcf564:8", "const:4:8"]]
+ 00bcf564 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b60064 bytes 47f80194
+ 00bcf564 bytes a72d0294
- 00b60078 ["INT_ADD", "register:40f0:8", ["const:b60078:8", "const:4:8"]]
- 00b60078 ["CALL", null, ["callee:00c5aa70:8"]]
+ 00bcf578 ["INT_ADD", "register:40f0:8", ["const:bcf578:8", "const:4:8"]]
+ 00bcf578 ["CALL", null, ["callee:00c5aa70:8"]]
- 00b60078 bytes def70194
+ 00bcf578 bytes 3e2d0294
- 00b60084 ["INT_ADD", "register:40f0:8", ["const:b60084:8", "const:4:8"]]
- 00b60084 ["CALL", null, ["callee:00c5aa30:8"]]
+ 00bcf584 ["INT_ADD", "register:40f0:8", ["const:bcf584:8", "const:4:8"]]
+ 00bcf584 ["CALL", null, ["callee:00c5aa30:8"]]
- 00b60084 bytes cbf70194
+ 00bcf584 bytes 2b2d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c219bcb5e4afa3e6256de465259e0802"></a>

### [`00b601d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b601d8.md) → [`00bcf6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf6d8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4Auth20FetchProvidersResultEZNS2_14FutureCallbackIS4_EEvP7_JNIEnvP8_jobje

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ba0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7a0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcf744",
      "incomplete_value": false,
      "site": "00bcf748",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60244",
      "incomplete_value": false,
      "site": "00b60248",
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
            "const:467:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcf744",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcf744",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b601d8.md#insn-00b60248) · [`00b6020c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b601d8.md#insn-00b6020c) · [`00b60218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b601d8.md#insn-00b60218)
- 新版 `00bcf748`（命令位置の公開資料なし） · `00bcf70c`（命令位置の公開資料なし） · `00bcf718`（命令位置の公開資料なし）

~~~diff
- 00b60248 ["INT_ADD", "register:40f0:8", ["const:b60248:8", "const:4:8"]]
- 00b60248 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bcf748 ["INT_ADD", "register:40f0:8", ["const:bcf748:8", "const:4:8"]]
+ 00bcf748 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b60248 bytes cef70194
+ 00bcf748 bytes 2e2d0294
- 00b6020c ["INT_ADD", "register:40f0:8", ["const:b6020c:8", "const:4:8"]]
- 00b6020c ["CALL", null, ["callee:00c5a600:8"]]
+ 00bcf70c ["INT_ADD", "register:40f0:8", ["const:bcf70c:8", "const:4:8"]]
+ 00bcf70c ["CALL", null, ["callee:00c5a600:8"]]
- 00b6020c bytes 85f60194
+ 00bcf70c bytes bd2b0294
- 00b60218 ["INT_ADD", "register:40f0:8", ["const:b60218:8", "const:4:8"]]
- 00b60218 ["CALL", null, ["callee:00c5aa80:8"]]
+ 00bcf718 ["INT_ADD", "register:40f0:8", ["const:bcf718:8", "const:4:8"]]
+ 00bcf718 ["CALL", null, ["callee:00c5aa80:8"]]
- 00b60218 bytes 7af70194
+ 00bcf718 bytes da2c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b10d7015ee713249d561601544ee963"></a>

### [`00b60310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60310.md) → [`00bcf810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf810.md) _ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0d40.md) · 呼出先 3件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf70.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md)
- 新版 呼出元 1件 [`00c5d940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d940.md) · 呼出先 3件 [`00c5a870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a870.md) [`00c5a9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a9f0.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

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
      "site": "00bcf830",
      "value": [
        "leaf",
        "ram:c5a870:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b60330",
      "value": [
        "leaf",
        "ram:bdde10:8"
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
      "00bcf830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdde10"
      ]
    ]
  ],
  "added": [
    [
      "00bcf830",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a870"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60310.md#insn-00b60330) · [`00b60344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60310.md#insn-00b60344) · [`00b60358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60310.md#insn-00b60358)
- 新版 `00bcf830`（命令位置の公開資料なし） · `00bcf844`（命令位置の公開資料なし） · `00bcf858`（命令位置の公開資料なし）

~~~diff
- 00b60330 ["INT_ADD", "register:40f0:8", ["const:b60330:8", "const:4:8"]]
- 00b60330 ["CALL", null, ["ram:bdde10:8"]]
+ 00bcf830 ["INT_ADD", "register:40f0:8", ["const:bcf830:8", "const:4:8"]]
+ 00bcf830 ["CALL", null, ["ram:c5a870:8"]]
- 00b60330 bytes b8f60194
+ 00bcf830 bytes 102c0294
- 00b60344 ["INT_ADD", "register:40f0:8", ["const:b60344:8", "const:4:8"]]
- 00b60344 ["CALL", null, ["callee:00c5aa00:8"]]
+ 00bcf844 ["INT_ADD", "register:40f0:8", ["const:bcf844:8", "const:4:8"]]
+ 00bcf844 ["CALL", null, ["callee:00c5aa00:8"]]
- 00b60344 bytes 0ff70194
+ 00bcf844 bytes 6f2c0294
- 00b60358 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60358 ["INT_ADD", "register:40f0:8", ["const:b60358:8", "const:4:8"]]
- 00b60358 ["CALLIND", null, ["register:0:8"]]
+ 00bcf858 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcf858 ["INT_ADD", "register:40f0:8", ["const:bcf858:8", "const:4:8"]]
+ 00bcf858 ["CALLIND", null, ["register:0:8"]]
- 00b60358 bytes 00013fd6
+ 00bcf858 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1490a268def5dc0f482b81dcbee4fca0"></a>

### [`00b603b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b603b0.md) → [`00bcf8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md) _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b5e964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e964.md) [`00b6c244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6c/00b6c244.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddba0.md) [`00bddbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbe0.md) [`00bdef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef70.md)
- 新版 呼出元 2件 [`00bcde64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcde64.md) [`00bdb744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdb/00bdb744.md) · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a5f0.md) [`00c5a650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a650.md) [`00c5ba20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba20.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bcf8c8",
      "value": [
        "leaf",
        "ram:c5a650:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b603c8",
      "value": [
        "leaf",
        "ram:bddbe0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bcf8d0",
      "value": [
        "leaf",
        "ram:c5a5f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b603d0",
      "value": [
        "leaf",
        "ram:bddba0:8"
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
      "site": "00bcf8d8",
      "value": [
        "leaf",
        "ram:c5a5f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b603d8",
      "value": [
        "leaf",
        "ram:bddba0:8"
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
      "00bcf8c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddbe0"
      ]
    ],
    [
      "00bcf8d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddba0"
      ]
    ],
    [
      "00bcf8d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddba0"
      ]
    ]
  ],
  "added": [
    [
      "00bcf8c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a650"
      ]
    ],
    [
      "00bcf8d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a5f0"
      ]
    ],
    [
      "00bcf8d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a5f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b603c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b603b0.md#insn-00b603c8) · [`00b603d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b603b0.md#insn-00b603d0) · [`00b603d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b603b0.md#insn-00b603d8)
- 新版 `00bcf8c8`（命令位置の公開資料なし） · `00bcf8d0`（命令位置の公開資料なし） · `00bcf8d8`（命令位置の公開資料なし）

~~~diff
- 00b603c8 ["INT_ADD", "register:40f0:8", ["const:b603c8:8", "const:4:8"]]
- 00b603c8 ["CALL", null, ["ram:bddbe0:8"]]
+ 00bcf8c8 ["INT_ADD", "register:40f0:8", ["const:bcf8c8:8", "const:4:8"]]
+ 00bcf8c8 ["CALL", null, ["ram:c5a650:8"]]
- 00b603c8 bytes 06f60194
+ 00bcf8c8 bytes 622b0294
- 00b603d0 ["INT_ADD", "register:40f0:8", ["const:b603d0:8", "const:4:8"]]
- 00b603d0 ["CALL", null, ["ram:bddba0:8"]]
+ 00bcf8d0 ["INT_ADD", "register:40f0:8", ["const:bcf8d0:8", "const:4:8"]]
+ 00bcf8d0 ["CALL", null, ["ram:c5a5f0:8"]]
- 00b603d0 bytes f4f50194
+ 00bcf8d0 bytes 482b0294
- 00b603d8 ["INT_ADD", "register:40f0:8", ["const:b603d8:8", "const:4:8"]]
- 00b603d8 ["CALL", null, ["ram:bddba0:8"]]
+ 00bcf8d8 ["INT_ADD", "register:40f0:8", ["const:bcf8d8:8", "const:4:8"]]
+ 00bcf8d8 ["CALL", null, ["ram:c5a5f0:8"]]
- 00b603d8 bytes f2f50194
+ 00bcf8d8 bytes 462b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60c8bd0cbb9d1fe6d7af0bb919c59f12"></a>

### [`00b604f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b604f0.md) → [`00bcf9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf9f0.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12Fut

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00be0b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b90.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d790.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 60.00% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcfa5c",
      "incomplete_value": false,
      "site": "00bcfa60",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6055c",
      "incomplete_value": false,
      "site": "00b60560",
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
            "const:467:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcfa5c",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcfa5c",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b604f0.md#insn-00b60560) · [`00b60524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b604f0.md#insn-00b60524) · [`00b60530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b604f0.md#insn-00b60530)
- 新版 `00bcfa60`（命令位置の公開資料なし） · `00bcfa24`（命令位置の公開資料なし） · `00bcfa30`（命令位置の公開資料なし）

~~~diff
- 00b60560 ["INT_ADD", "register:40f0:8", ["const:b60560:8", "const:4:8"]]
- 00b60560 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bcfa60 ["INT_ADD", "register:40f0:8", ["const:bcfa60:8", "const:4:8"]]
+ 00bcfa60 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b60560 bytes 08f70194
+ 00bcfa60 bytes 682c0294
- 00b60524 ["INT_ADD", "register:40f0:8", ["const:b60524:8", "const:4:8"]]
- 00b60524 ["CALL", null, ["callee:00c5a600:8"]]
+ 00bcfa24 ["INT_ADD", "register:40f0:8", ["const:bcfa24:8", "const:4:8"]]
+ 00bcfa24 ["CALL", null, ["callee:00c5a600:8"]]
- 00b60524 bytes bff50194
+ 00bcfa24 bytes f72a0294
- 00b60530 ["INT_ADD", "register:40f0:8", ["const:b60530:8", "const:4:8"]]
- 00b60530 ["CALL", null, ["callee:00c5aa80:8"]]
+ 00bcfa30 ["INT_ADD", "register:40f0:8", ["const:bcfa30:8", "const:4:8"]]
+ 00bcfa30 ["CALL", null, ["callee:00c5aa80:8"]]
- 00b60530 bytes b4f60194
+ 00bcfa30 bytes 142c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe352a951291394805d7293b5518527a"></a>

### [`00b606dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b606dc.md) → [`00bcfbdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfbdc.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4UserEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0be0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7e0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.42% / 新版 92.42%

CFGの説明率　旧版 85.71% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcfc40",
      "incomplete_value": false,
      "site": "00bcfc44",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60740",
      "incomplete_value": false,
      "site": "00b60744",
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
            "const:467:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcfc40",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b607ac",
      "READ",
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
      "00bcfc40",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "00bcfcac",
      "READ",
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

- 旧版 [`00b60744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b606dc.md#insn-00b60744) · [`00b60708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b606dc.md#insn-00b60708) · [`00b60714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b606dc.md#insn-00b60714)
- 新版 `00bcfc44`（命令位置の公開資料なし） · `00bcfc08`（命令位置の公開資料なし） · `00bcfc14`（命令位置の公開資料なし）

~~~diff
- 00b60744 ["INT_ADD", "register:40f0:8", ["const:b60744:8", "const:4:8"]]
- 00b60744 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bcfc44 ["INT_ADD", "register:40f0:8", ["const:bcfc44:8", "const:4:8"]]
+ 00bcfc44 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b60744 bytes 8ff60194
+ 00bcfc44 bytes ef2b0294
- 00b60708 ["INT_ADD", "register:40f0:8", ["const:b60708:8", "const:4:8"]]
- 00b60708 ["CALL", null, ["callee:00c5a600:8"]]
+ 00bcfc08 ["INT_ADD", "register:40f0:8", ["const:bcfc08:8", "const:4:8"]]
+ 00bcfc08 ["CALL", null, ["callee:00c5a600:8"]]
- 00b60708 bytes 46f50194
+ 00bcfc08 bytes 7e2a0294
- 00b60714 ["INT_ADD", "register:40f0:8", ["const:b60714:8", "const:4:8"]]
- 00b60714 ["CALL", null, ["callee:00c5aa80:8"]]
+ 00bcfc14 ["INT_ADD", "register:40f0:8", ["const:bcfc14:8", "const:4:8"]]
+ 00bcfc14 ["CALL", null, ["callee:00c5aa80:8"]]
- 00b60714 bytes 3bf60194
+ 00bcfc14 bytes 9b2b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-753e75d7c46c857b3c5b8bcfea2a2e73"></a>

### [`00b607e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b607e4.md) → [`00bcfce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfce4.md) _ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b5ebb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5ebb4.md) [`00b708dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b708dc.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bb0.md)
- 新版 呼出元 2件 [`00bce0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bce/00bce0b4.md) [`00bdfddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdfddc.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7b0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60814"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60818"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bcfd14"
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
      "unmatched:00b60814",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60818",
      "WRITE",
      [
        "storage",
        "Stack[-0x4c]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60864",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bddc40"
      ]
    ]
  ],
  "added": [
    [
      "00bcfd14",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00bcfd18",
      "WRITE",
      [
        "storage",
        "Stack[-0x4c]",
        null,
        null
      ]
    ],
    [
      "00bcfd64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a690"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b607e4.md#insn-00b60814) · [`00b60818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b607e4.md#insn-00b60818) · [`00b6081c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b607e4.md#insn-00b6081c)
- 新版 `00bcfd1c`（命令位置の公開資料なし）

~~~diff
- 00b60814 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b60814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b60814 bytes e81f00f9
- 00b60818 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b60818 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b60818 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:34:8"]]
- 00b60818 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b60818 bytes ffd30039
- 00b6081c ["INT_ADD", "register:40f0:8", ["const:b6081c:8", "const:4:8"]]
- 00b6081c ["CALL", null, ["callee:00c5d920:8"]]
+ 00bcfd1c ["INT_ADD", "register:40f0:8", ["const:bcfd1c:8", "const:4:8"]]
+ 00bcfd1c ["CALL", null, ["callee:00c5d920:8"]]
- 00b6081c bytes 41010294
+ 00bcfd1c bytes 01370294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-131df35565691c664c0fc2f5d4371694"></a>

### [`00b608b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b608b8.md) → [`00bcfdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcfdb8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4UserEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResu

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bb0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7b0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 58.33% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcfe24",
      "incomplete_value": false,
      "site": "00bcfe28",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60924",
      "incomplete_value": false,
      "site": "00b60928",
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
            "const:467:8"
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
      "definition_site": "00bcfe5c",
      "incomplete_value": true,
      "site": "00bcfe64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:40a8:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bcfe60",
      "incomplete_value": true,
      "site": "00bcfe64",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "1",
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
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bcfe24",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bcfe24",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b608b8.md#insn-00b60928) · [`00b60964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b608b8.md#insn-00b60964) · [`00b608ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b608b8.md#insn-00b608ec)
- 新版 `00bcfe28`（命令位置の公開資料なし） · `00bcfe64`（命令位置の公開資料なし） · `00bcfdec`（命令位置の公開資料なし）

~~~diff
- 00b60928 ["INT_ADD", "register:40f0:8", ["const:b60928:8", "const:4:8"]]
- 00b60928 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bcfe28 ["INT_ADD", "register:40f0:8", ["const:bcfe28:8", "const:4:8"]]
+ 00bcfe28 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b60928 bytes 16f60194
+ 00bcfe28 bytes 762b0294
- 00b60964 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60964 ["INT_ADD", "register:40f0:8", ["const:b60964:8", "const:4:8"]]
- 00b60964 ["CALLIND", null, ["register:0:8"]]
+ 00bcfe64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bcfe64 ["INT_ADD", "register:40f0:8", ["const:bcfe64:8", "const:4:8"]]
+ 00bcfe64 ["CALLIND", null, ["register:0:8"]]
- 00b60964 bytes 00013fd6
+ 00bcfe64 bytes 00013fd6
- 00b608ec ["INT_ADD", "register:40f0:8", ["const:b608ec:8", "const:4:8"]]
- 00b608ec ["CALL", null, ["callee:00c5a600:8"]]
+ 00bcfdec ["INT_ADD", "register:40f0:8", ["const:bcfdec:8", "const:4:8"]]
+ 00bcfdec ["CALL", null, ["callee:00c5a600:8"]]
- 00b608ec bytes cdf40194
+ 00bcfdec bytes 052a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5d996ceb2279a2cea075858a88148c2"></a>

### [`00b60a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60a90.md) → [`00bcff90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcff90.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10AuthResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_E

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bc0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7c0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 89.39% / 新版 89.39%

CFGの説明率　旧版 20.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60aec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bcffec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b60ac4",
      "incomplete_value": true,
      "site": "00b60ac8",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:00b60aec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcfffc"
      ]
    ],
    [
      "unmatched:00b60af4",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b60ae4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bcffec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bcfffc"
      ]
    ],
    [
      "00bcfff4",
      "PARAM",
      [
        "storage",
        "002a7008",
        null,
        "string"
      ]
    ],
    [
      "00bcffe4",
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

- 旧版 [`00b60ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60a90.md#insn-00b60ac8) · [`00b60ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60a90.md#insn-00b60ae4) · [`00b60aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60a90.md#insn-00b60aec)
- 新版 `00bcffc8`（命令位置の公開資料なし）

~~~diff
- 00b60ac8 ["INT_ADD", "register:40f0:8", ["const:b60ac8:8", "const:4:8"]]
- 00b60ac8 ["CALL", null, ["callee:00c5aa80:8"]]
+ 00bcffc8 ["INT_ADD", "register:40f0:8", ["const:bcffc8:8", "const:4:8"]]
+ 00bcffc8 ["CALL", null, ["callee:00c5aa80:8"]]
- 00b60ac8 bytes 4ef50194
+ 00bcffc8 bytes ae2a0294
- 00b60ae4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60ae4 ["INT_ADD", "register:40f0:8", ["const:b60ae4:8", "const:4:8"]]
- 00b60ae4 ["CALLIND", null, ["register:0:8"]]
- 00b60ae4 bytes 00013fd6
- 00b60aec ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b60aec bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-393e1d999e3c60166f73653f22c79090"></a>

### [`00b60b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60b98.md) → [`00bd0098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0098.md) _ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`00b5fb88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fb88.md) [`00b6fe28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6fe28.md) [`00b70050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70050.md) [`00b70b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70b28.md) [`00b70d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b70/00b70d18.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00be0bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bf0.md)
- 新版 呼出元 8件 [`00bcf088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf088.md) [`00bdf328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf328.md) [`00bdf550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf550.md) [`00be0028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0028.md) [`00be0218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be0/00be0218.md) · 呼出先 6件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5aa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa00.md) [`00c5d7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.58% / 新版 64.58%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60b9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60b9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60ba0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b60b9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60ba0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60ba4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd009c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bd00a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd00a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60b98.md#insn-00b60b9c) · [`00b60ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60b98.md#insn-00b60ba0) · [`00b60ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60b98.md#insn-00b60ba4)

~~~diff
- 00b60b9c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b60b9c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b60b9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b60b9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60b9c bytes f85f04a9
- 00b60ba0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b60ba0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b60ba0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b60ba0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60ba0 bytes f65705a9
- 00b60ba4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b60ba4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b60ba4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b60ba4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60ba4 bytes f44f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b17011046eb6312054c7c4c8a154de2e"></a>

### [`00b60c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60c6c.md) → [`00bd016c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd016c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS_4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUl

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bf0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00c5d7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d7f0.md) · 呼出先 10件 [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa30.md) [`00c5aa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa50.md) [`00c5aa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aa60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.03% / 新版 91.03%

CFGの説明率　旧版 60.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60c6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60c70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60c70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b60c6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60c70",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60c74",
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
      "00bd016c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bd0170",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bd0174",
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

- 旧版 [`00b60c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60c6c.md#insn-00b60c6c) · [`00b60c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60c6c.md#insn-00b60c70) · [`00b60c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60c6c.md#insn-00b60c74)

~~~diff
- 00b60c6c ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b60c6c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b60c6c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b60c6c bytes f90f1bf8
- 00b60c70 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b60c70 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b60c70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b60c70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60c70 bytes f85f01a9
- 00b60c74 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b60c74 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b60c74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b60c74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60c74 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6202f713fcca6ebce6075ee50b2c993"></a>

### [`00b60da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60da4.md) → [`00bd02a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd02a4.md) _ZN8firebase4auth10authresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

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
      "site": "00b60dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd02d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd02b8",
      "incomplete_value": true,
      "site": "00bd02b8",
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
      "definition_site": "00b60db8",
      "incomplete_value": true,
      "site": "00b60db8",
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
      "00bd02b4",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b60dc4",
      "PARAM",
      [
        "storage",
        "002a2055",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b60dc8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bd02b4",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd02c4",
      "PARAM",
      [
        "storage",
        "002b2716",
        null,
        "string"
      ]
    ],
    [
      "00bd02c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60da4.md#insn-00b60db8) · [`00b60dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60da4.md#insn-00b60dc8) · [`00b60dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60da4.md#insn-00b60dd0)
- 新版 `00bd02b8`（命令位置の公開資料なし）

~~~diff
- 00b60db8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b60db8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd02b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd02b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b60db8 bytes e80000b5
+ 00bd02b8 bytes e80000b5
- 00b60dc8 ["INT_ADD", "register:40f0:8", ["const:b60dc8:8", "const:4:8"]]
- 00b60dc8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b60dc8 bytes b2f40194
- 00b60dd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
- 00b60dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60dd0 bytes 60a202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-332f41956abf7b9682d57c073a7ef089"></a>

### [`00b60de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60de4.md) → [`00bd02e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd02e4.md) _ZN8firebase4auth10authresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00b60e10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0310"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd02f8",
      "incomplete_value": true,
      "site": "00bd02f8",
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
      "definition_site": "00b60df8",
      "incomplete_value": true,
      "site": "00b60df8",
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
      "00bd02f4",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd02f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b60e14"
      ]
    ],
    [
      "unmatched:00b60e00",
      "PARAM",
      [
        "storage",
        "002a2055",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd02f4",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd02f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0314"
      ]
    ],
    [
      "00bd0300",
      "PARAM",
      [
        "storage",
        "002b2716",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60de4.md#insn-00b60e08) · [`00b60e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60de4.md#insn-00b60e10) · [`00b60e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60de4.md#insn-00b60e20)

~~~diff
- 00b60e08 ["INT_ADD", "register:40f0:8", ["const:b60e08:8", "const:4:8"]]
- 00b60e08 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b60e08 bytes a2f40194
- 00b60e10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
- 00b60e10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60e10 bytes 60a202f9
- 00b60e20 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b60e20 ["RETURN", null, ["register:0:8"]]
- 00b60e20 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6882bfedfb4e3e7420135a4a8a75ce49"></a>

### [`00b60e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60e24.md) → [`00bd0324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0324.md) _ZN8firebase4auth10authresult10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b60e54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0354"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd0338",
      "incomplete_value": true,
      "site": "00bd0338",
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
      "definition_site": "00b60e38",
      "incomplete_value": true,
      "site": "00b60e38",
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
      "00bd0334",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b60e44",
      "PARAM",
      [
        "storage",
        "002a2055",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b60e4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bd0334",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0344",
      "PARAM",
      [
        "storage",
        "002b2716",
        null,
        "string"
      ]
    ],
    [
      "00bd034c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60e24.md#insn-00b60e38) · [`00b60e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60e24.md#insn-00b60e4c) · [`00b60e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60e24.md#insn-00b60e54)
- 新版 `00bd0338`（命令位置の公開資料なし）

~~~diff
- 00b60e38 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b60e38 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd0338 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd0338 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b60e38 bytes 080100b5
+ 00bd0338 bytes 080100b5
- 00b60e4c ["INT_ADD", "register:40f0:8", ["const:b60e4c:8", "const:4:8"]]
- 00b60e4c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b60e4c bytes 91f40194
- 00b60e54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
- 00b60e54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60e54 bytes 60a202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f482ebb6d44e733f73506416c3ac961"></a>

### [`00b60e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60e68.md) → [`00bd0368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0368.md) _ZN8firebase4auth10authresult10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b60e98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0398"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd037c",
      "incomplete_value": true,
      "site": "00bd037c",
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
      "definition_site": "00b60e7c",
      "incomplete_value": true,
      "site": "00b60e7c",
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
      "00bd0378",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd037c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b60e9c"
      ]
    ],
    [
      "unmatched:00b60e84",
      "PARAM",
      [
        "storage",
        "002a2055",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd0378",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd037c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd039c"
      ]
    ],
    [
      "00bd0384",
      "PARAM",
      [
        "storage",
        "002b2716",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60e68.md#insn-00b60e90) · [`00b60e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60e68.md#insn-00b60e98) · [`00b60ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60e68.md#insn-00b60ea8)
- 新版 `00bd0390`（命令位置の公開資料なし）

~~~diff
- 00b60e90 ["INT_ADD", "register:40f0:8", ["const:b60e90:8", "const:4:8"]]
- 00b60e90 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0390 ["INT_ADD", "register:40f0:8", ["const:bd0390:8", "const:4:8"]]
+ 00bd0390 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b60e90 bytes 80f40194
+ 00bd0390 bytes e0290294
- 00b60e98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
- 00b60e98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60e98 bytes 60a202f9
- 00b60ea8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b60ea8 ["RETURN", null, ["register:0:8"]]
- 00b60ea8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-722c708597a4e8f989037cb7499185a2"></a>

### [`00b60eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60eb8.md) → [`00bd03b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd03b8.md) _ZN8firebase4auth10authresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd0410",
      "incomplete_value": true,
      "site": "00bd0410",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60f10",
      "incomplete_value": true,
      "site": "00b60f10",
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
            "const:548:8"
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
      "definition_site": "00bd03ec",
      "incomplete_value": true,
      "site": "00bd03f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:448:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60eec",
      "incomplete_value": true,
      "site": "00b60ef8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
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
      "unmatched:00b60ecc",
      "READ",
      [
        "storage",
        "010a1548",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd03ec",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0410",
      "WRITE",
      [
        "storage",
        "010a1548",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd03cc",
      "READ",
      [
        "storage",
        "01126450",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd03ec",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0410",
      "WRITE",
      [
        "storage",
        "01126450",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60eb8.md#insn-00b60ef8) · [`00b60f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60eb8.md#insn-00b60f10) · [`00b60ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60eb8.md#insn-00b60ec8)
- 新版 `00bd03f8`（命令位置の公開資料なし） · `00bd0410`（命令位置の公開資料なし） · `00bd03c8`（命令位置の公開資料なし）

~~~diff
- 00b60ef8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60ef8 ["INT_ADD", "register:40f0:8", ["const:b60ef8:8", "const:4:8"]]
- 00b60ef8 ["CALLIND", null, ["register:0:8"]]
+ 00bd03f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd03f8 ["INT_ADD", "register:40f0:8", ["const:bd03f8:8", "const:4:8"]]
+ 00bd03f8 ["CALLIND", null, ["register:0:8"]]
- 00b60ef8 bytes 00013fd6
+ 00bd03f8 bytes 00013fd6
- 00b60f10 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b60f10 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:548:8"]]
- 00b60f10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd0410 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd0410 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:450:8"]]
+ 00bd0410 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b60f10 bytes a0221539
+ 00bd0410 bytes a0421139
- 00b60ec8 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd03c8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b60ec8 bytes 152a00b0
+ 00bd03c8 bytes b52a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a736a30a6a9e5c50cc8a4881f0f49c1e"></a>

### [`00b60f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60f24.md) → [`00bd0424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0424.md) _ZN8firebase4auth10authresult12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.43% / 新版 46.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60f28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60f28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b60f24",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60f28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60f2c",
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
      "00bd0424",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd0428",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd042c",
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

- 旧版 [`00b60f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60f24.md#insn-00b60f24) · [`00b60f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60f24.md#insn-00b60f28) · [`00b60f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60f24.md#insn-00b60f2c)

~~~diff
- 00b60f24 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b60f24 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b60f24 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b60f24 bytes f50f1df8
- 00b60f28 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b60f28 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b60f28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b60f28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60f28 bytes f44f01a9
- 00b60f2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b60f2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b60f2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b60f2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60f2c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77e88e526ff6ee5004ea1d58964fc9b9"></a>

### [`00b60f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60f94.md) → [`00bd0494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0494.md) _ZN8firebase4auth10authresult14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60f94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60f94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b60f98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b60f94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60f98",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b60fa8",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0494",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd0498",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd04a8",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60f94.md#insn-00b60f94) · [`00b60f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60f94.md#insn-00b60f98) · [`00b60fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60f94.md#insn-00b60fb0)

~~~diff
- 00b60f94 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b60f94 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b60f94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b60f94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b60f94 bytes f44fbea9
- 00b60f98 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b60f98 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b60f98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b60f98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b60f98 bytes fd7b01a9
- 00b60fb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b60fb0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b60fb0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73babbd8df44ff51d5aed50127d7cd62"></a>

### [`00b61004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61004.md) → [`00bd0504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0504.md) _ZN8firebase4auth10authresult11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bd0520",
      "incomplete_value": false,
      "site": "00bd0524",
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
    "old": {
      "definition_site": "00b61020",
      "incomplete_value": false,
      "site": "00b61024",
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
            "const:547:8"
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
      "definition_site": "00bd0530",
      "incomplete_value": true,
      "site": "00bd053c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61030",
      "incomplete_value": true,
      "site": "00b6103c",
      "value": [
        "LOAD",
        "8",
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
      "00bd0520",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd0530",
      "DATA",
      [
        "storage",
        "010a1550",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0520",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd0530",
      "DATA",
      [
        "storage",
        "01126458",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61004.md#insn-00b61024) · [`00b6101c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61004.md#insn-00b6101c) · [`00b61020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61004.md#insn-00b61020)
- 新版 `00bd0524`（命令位置の公開資料なし） · `00bd051c`（命令位置の公開資料なし） · `00bd0520`（命令位置の公開資料なし）

~~~diff
- 00b61024 ["INT_ADD", "register:40f0:8", ["const:b61024:8", "const:4:8"]]
- 00b61024 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd0524 ["INT_ADD", "register:40f0:8", ["const:bd0524:8", "const:4:8"]]
+ 00bd0524 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b61024 bytes 57f40194
+ 00bd0524 bytes b7290294
- 00b6101c ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd051c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b6101c bytes a0b9fff0
+ 00bd051c bytes c0b6ff90
- 00b61020 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b61020 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61020 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61020 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd0520 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd0520 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0520 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0520 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61020 bytes 001c1591
+ 00bd0520 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d8d5932db205638b231d3bd16ac9b4a"></a>

### [`00b61040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61040.md) → [`00bd0540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0540.md) _ZN8firebase4auth10authresult13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61044"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61040",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61044",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61054",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0540",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd0544",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd0554",
      "READ",
      [
        "storage",
        "01126448",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61040.md#insn-00b61040) · [`00b61044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61040.md#insn-00b61044) · [`00b6105c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61040.md#insn-00b6105c)

~~~diff
- 00b61040 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b61040 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b61040 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b61040 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b61040 bytes f44fbea9
- 00b61044 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b61044 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b61044 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b61044 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61044 bytes fd7b01a9
- 00b6105c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6105c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6105c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a98bdd085124c26f1d67c538f57c0912"></a>

### [`00b610ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b610ec.md) → [`00bd05ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd05ec.md) _ZN8firebase4auth20additional_user_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocato

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b61118"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0618"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd0600",
      "incomplete_value": true,
      "site": "00bd0600",
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
      "definition_site": "00b61100",
      "incomplete_value": true,
      "site": "00b61100",
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
      "00bd05fc",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0600",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6111c"
      ]
    ],
    [
      "unmatched:00b6110c",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd05fc",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0600",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd061c"
      ]
    ],
    [
      "00bd060c",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b610ec.md#insn-00b61110) · [`00b61118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b610ec.md#insn-00b61118) · [`00b61128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b610ec.md#insn-00b61128)

~~~diff
- 00b61110 ["INT_ADD", "register:40f0:8", ["const:b61110:8", "const:4:8"]]
- 00b61110 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61110 bytes e0f30194
- 00b61118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00b61118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61118 bytes 60ba02f9
- 00b61128 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b61128 ["RETURN", null, ["register:0:8"]]
- 00b61128 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6e601b1151d4a689a8a9f9cfe13f078"></a>

### [`00b6112c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6112c.md) → [`00bd062c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd062c.md) _ZN8firebase4auth20additional_user_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocato

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

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
      "site": "00b61158"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0658"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd0640",
      "incomplete_value": true,
      "site": "00bd0640",
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
      "definition_site": "00b61140",
      "incomplete_value": true,
      "site": "00b61140",
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
      "00bd063c",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61148",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b61150",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bd063c",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0648",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ],
    [
      "00bd0650",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6112c.md#insn-00b61140) · [`00b61150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6112c.md#insn-00b61150) · [`00b61158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6112c.md#insn-00b61158)
- 新版 `00bd0640`（命令位置の公開資料なし）

~~~diff
- 00b61140 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b61140 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd0640 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd0640 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b61140 bytes e80000b5
+ 00bd0640 bytes e80000b5
- 00b61150 ["INT_ADD", "register:40f0:8", ["const:b61150:8", "const:4:8"]]
- 00b61150 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61150 bytes d0f30194
- 00b61158 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00b61158 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61158 bytes 60ba02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06142fb23cf03773cda7b2cd7e074ceb"></a>

### [`00b6116c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6116c.md) → [`00bd066c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd066c.md) _ZN8firebase4auth20additional_user_info10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd069c",
      "incomplete_value": true,
      "site": "00bd069c",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6119c",
      "incomplete_value": true,
      "site": "00b6119c",
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
            "const:570:8"
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
      "definition_site": "00bd0680",
      "incomplete_value": true,
      "site": "00bd0680",
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
      "definition_site": "00b61180",
      "incomplete_value": true,
      "site": "00b61180",
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
      "definition_site": "00bd068c",
      "incomplete_value": false,
      "site": "00bd0694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6118c",
      "incomplete_value": false,
      "site": "00b61194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:74:8"
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
      "00bd067c",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd068c",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ],
    [
      "00bd069c",
      "WRITE",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd067c",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd068c",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ],
    [
      "00bd069c",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6116c.md#insn-00b61194) · [`00b6119c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6116c.md#insn-00b6119c) · [`00b61178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6116c.md#insn-00b61178)
- 新版 `00bd0694`（命令位置の公開資料なし） · `00bd069c`（命令位置の公開資料なし） · `00bd0678`（命令位置の公開資料なし）

~~~diff
- 00b61194 ["INT_ADD", "register:40f0:8", ["const:b61194:8", "const:4:8"]]
- 00b61194 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0694 ["INT_ADD", "register:40f0:8", ["const:bd0694:8", "const:4:8"]]
+ 00bd0694 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61194 bytes bff30194
+ 00bd0694 bytes 1f290294
- 00b6119c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00b6119c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd069c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:478:8"]]
+ 00bd069c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6119c bytes 60ba02f9
+ 00bd069c bytes 603e02f9
- 00b61178 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd0678 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b61178 bytes 132a0090
+ 00bd0678 bytes b32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e37549b61c2c5ce5cf7019eae184c5a1"></a>

### [`00b611b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b611b0.md) → [`00bd06b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd06b0.md) _ZN8firebase4auth20additional_user_info10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b611e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd06e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd06c4",
      "incomplete_value": true,
      "site": "00bd06c4",
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
      "definition_site": "00b611c4",
      "incomplete_value": true,
      "site": "00b611c4",
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
      "00bd06c0",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd06c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b611e4"
      ]
    ],
    [
      "unmatched:00b611cc",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd06c0",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd06c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd06e4"
      ]
    ],
    [
      "00bd06cc",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b611c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b611b0.md#insn-00b611c4) · [`00b611d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b611b0.md#insn-00b611d8) · [`00b611e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b611b0.md#insn-00b611e0)
- 新版 `00bd06c4`（命令位置の公開資料なし） · `00bd06d8`（命令位置の公開資料なし）

~~~diff
- 00b611c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b611c4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd06c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd06c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b611c4 bytes 080100b5
+ 00bd06c4 bytes 080100b5
- 00b611d8 ["INT_ADD", "register:40f0:8", ["const:b611d8:8", "const:4:8"]]
- 00b611d8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd06d8 ["INT_ADD", "register:40f0:8", ["const:bd06d8:8", "const:4:8"]]
+ 00bd06d8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b611d8 bytes aef30194
+ 00bd06d8 bytes 0e290294
- 00b611e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
- 00b611e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b611e0 bytes 60ba02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8df6f472d0291b6fd0207287314abcee"></a>

### [`00b6126c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6126c.md) → [`00bd076c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd076c.md) _ZN8firebase4auth20additional_user_info12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 35.71% / 新版 35.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6126c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61270"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61270"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6126c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61270",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61274",
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
      "00bd076c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd0770",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd0774",
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

- 旧版 [`00b6126c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6126c.md#insn-00b6126c) · [`00b61270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6126c.md#insn-00b61270) · [`00b61274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6126c.md#insn-00b61274)

~~~diff
- 00b6126c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b6126c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b6126c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6126c bytes f50f1df8
- 00b61270 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b61270 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b61270 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b61270 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61270 bytes f44f01a9
- 00b61274 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b61274 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b61274 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b61274 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61274 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90dfd393aa32120e9ad1aa961757e6db"></a>

### [`00b612dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b612dc.md) → [`00bd07dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd07dc.md) _ZN8firebase4auth20additional_user_info14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "definition_site": "00bd081c",
      "incomplete_value": true,
      "site": "00bd081c",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6131c",
      "incomplete_value": true,
      "site": "00b6131c",
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
            "const:570:8"
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
      "definition_site": "00bd07f8",
      "incomplete_value": true,
      "site": "00bd07f8",
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
      "definition_site": "00b612f8",
      "incomplete_value": true,
      "site": "00b612f8",
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
      "definition_site": "00bd0800",
      "incomplete_value": false,
      "site": "00bd0814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61300",
      "incomplete_value": false,
      "site": "00b61314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:74:8"
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
      "00bd07f0",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0800",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ],
    [
      "00bd081c",
      "WRITE",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd07f0",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0800",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ],
    [
      "00bd081c",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b612dc.md#insn-00b61314) · [`00b6131c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b612dc.md#insn-00b6131c) · [`00b612e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b612dc.md#insn-00b612e8)
- 新版 `00bd0814`（命令位置の公開資料なし） · `00bd081c`（命令位置の公開資料なし） · `00bd07e8`（命令位置の公開資料なし）

~~~diff
- 00b61314 ["INT_ADD", "register:40f0:8", ["const:b61314:8", "const:4:8"]]
- 00b61314 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0814 ["INT_ADD", "register:40f0:8", ["const:bd0814:8", "const:4:8"]]
+ 00bd0814 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61314 bytes 5ff30194
+ 00bd0814 bytes bf280294
- 00b6131c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
- 00b6131c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd081c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:478:8"]]
+ 00bd081c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6131c bytes 80ba02f9
+ 00bd081c bytes 803e02f9
- 00b612e8 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd07e8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b612e8 bytes 142a0090
+ 00bd07e8 bytes b42a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b48199f8eae2b5c5b13302d32060cde3"></a>

### [`00b6134c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6134c.md) → [`00bd084c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd084c.md) _ZN8firebase4auth20additional_user_info11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bd0868",
      "incomplete_value": false,
      "site": "00bd086c",
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
    "old": {
      "definition_site": "00b61368",
      "incomplete_value": false,
      "site": "00b6136c",
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
            "const:547:8"
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
      "definition_site": "00bd0878",
      "incomplete_value": true,
      "site": "00bd0884",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61378",
      "incomplete_value": true,
      "site": "00b61384",
      "value": [
        "LOAD",
        "8",
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
      "00bd0868",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd0878",
      "DATA",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0868",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd0878",
      "DATA",
      [
        "storage",
        "01126488",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6136c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6134c.md#insn-00b6136c) · [`00b61364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6134c.md#insn-00b61364) · [`00b61368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6134c.md#insn-00b61368)
- 新版 `00bd086c`（命令位置の公開資料なし） · `00bd0864`（命令位置の公開資料なし） · `00bd0868`（命令位置の公開資料なし）

~~~diff
- 00b6136c ["INT_ADD", "register:40f0:8", ["const:b6136c:8", "const:4:8"]]
- 00b6136c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd086c ["INT_ADD", "register:40f0:8", ["const:bd086c:8", "const:4:8"]]
+ 00bd086c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6136c bytes 85f30194
+ 00bd086c bytes e5280294
- 00b61364 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd0864 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b61364 bytes a0b9fff0
+ 00bd0864 bytes c0b6ff90
- 00b61368 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b61368 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61368 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61368 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd0868 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd0868 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0868 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0868 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61368 bytes 001c1591
+ 00bd0868 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28d0673aab095a253487ef395546be61"></a>

### [`00b61388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61388.md) → [`00bd0888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0888.md) _ZN8firebase4auth20additional_user_info13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd08c8",
      "incomplete_value": true,
      "site": "00bd08c8",
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
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b613c8",
      "incomplete_value": true,
      "site": "00b613c8",
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
            "const:570:8"
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
      "definition_site": "00bd08a4",
      "incomplete_value": true,
      "site": "00bd08a4",
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
      "definition_site": "00b613a4",
      "incomplete_value": true,
      "site": "00b613a4",
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
      "definition_site": "00bd08ac",
      "incomplete_value": false,
      "site": "00bd08c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:29a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b613ac",
      "incomplete_value": false,
      "site": "00b613c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:74:8"
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
      "00bd089c",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd08ac",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ],
    [
      "00bd08c8",
      "WRITE",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd089c",
      "READ",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd08ac",
      "PARAM",
      [
        "storage",
        "002ac29a",
        null,
        "string"
      ]
    ],
    [
      "00bd08c8",
      "WRITE",
      [
        "storage",
        "01126478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b613c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61388.md#insn-00b613c0) · [`00b613c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61388.md#insn-00b613c8) · [`00b61394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61388.md#insn-00b61394)
- 新版 `00bd08c0`（命令位置の公開資料なし） · `00bd08c8`（命令位置の公開資料なし） · `00bd0894`（命令位置の公開資料なし）

~~~diff
- 00b613c0 ["INT_ADD", "register:40f0:8", ["const:b613c0:8", "const:4:8"]]
- 00b613c0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd08c0 ["INT_ADD", "register:40f0:8", ["const:bd08c0:8", "const:4:8"]]
+ 00bd08c0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b613c0 bytes 34f30194
+ 00bd08c0 bytes 94280294
- 00b613c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
- 00b613c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd08c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:478:8"]]
+ 00bd08c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b613c8 bytes 80ba02f9
+ 00bd08c8 bytes 803e02f9
- 00b61394 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd0894 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b61394 bytes 142a0090
+ 00bd0894 bytes b42a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9060e48f469d72af37c1b71e63bf391b"></a>

### [`00b613f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b613f8.md) → [`00bd08f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd08f8.md) _ZN8firebase4auth20additional_user_info10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bd0914",
      "incomplete_value": false,
      "site": "00bd0918",
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
    "old": {
      "definition_site": "00b61414",
      "incomplete_value": false,
      "site": "00b61418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
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
      "definition_site": "00bd0924",
      "incomplete_value": true,
      "site": "00bd0930",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61424",
      "incomplete_value": true,
      "site": "00b61430",
      "value": [
        "LOAD",
        "8",
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
      "00bd0914",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd0924",
      "DATA",
      [
        "storage",
        "010a1598",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd0914",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd0924",
      "DATA",
      [
        "storage",
        "011264a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b613f8.md#insn-00b61418) · [`00b61410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b613f8.md#insn-00b61410) · [`00b61414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b613f8.md#insn-00b61414)
- 新版 `00bd0918`（命令位置の公開資料なし） · `00bd0910`（命令位置の公開資料なし） · `00bd0914`（命令位置の公開資料なし）

~~~diff
- 00b61418 ["INT_ADD", "register:40f0:8", ["const:b61418:8", "const:4:8"]]
- 00b61418 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd0918 ["INT_ADD", "register:40f0:8", ["const:bd0918:8", "const:4:8"]]
+ 00bd0918 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b61418 bytes 5af30194
+ 00bd0918 bytes ba280294
- 00b61410 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd0910 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b61410 bytes c0b9ff90
+ 00bd0910 bytes c0b6ffb0
- 00b61414 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b61414 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61414 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61414 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd0914 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd0914 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0914 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0914 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61414 bytes 00c81791
+ 00bd0914 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c1366dd2ec5dc543c975bed0b7d33a7"></a>

### [`00b61434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61434.md) → [`00bd0934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0934.md) _ZN8firebase4auth27api_not_available_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd0960",
      "incomplete_value": true,
      "site": "00bd0960",
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
    "old": {
      "definition_site": "00b61460",
      "incomplete_value": true,
      "site": "00b61460",
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
            "const:5a0:8"
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
      "definition_site": "00bd0948",
      "incomplete_value": true,
      "site": "00bd0948",
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
      "definition_site": "00b61448",
      "incomplete_value": true,
      "site": "00b61448",
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
      "definition_site": "00bd0954",
      "incomplete_value": false,
      "site": "00bd0958",
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
            "const:374:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61454",
      "incomplete_value": false,
      "site": "00b61458",
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
            "const:739:8"
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
      "00bd0944",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0954",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00bd0960",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0944",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0954",
      "PARAM",
      [
        "storage",
        "002a7374",
        null,
        "string"
      ]
    ],
    [
      "00bd0960",
      "WRITE",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61434.md#insn-00b61458) · [`00b61460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61434.md#insn-00b61460) · [`00b61440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61434.md#insn-00b61440)
- 新版 `00bd0958`（命令位置の公開資料なし） · `00bd0960`（命令位置の公開資料なし） · `00bd0940`（命令位置の公開資料なし）

~~~diff
- 00b61458 ["INT_ADD", "register:40f0:8", ["const:b61458:8", "const:4:8"]]
- 00b61458 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0958 ["INT_ADD", "register:40f0:8", ["const:bd0958:8", "const:4:8"]]
+ 00bd0958 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61458 bytes 0ef30194
+ 00bd0958 bytes 6e280294
- 00b61460 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b61460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd0960 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00bd0960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61460 bytes 60d202f9
+ 00bd0960 bytes 605602f9
- 00b61440 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd0940 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b61440 bytes 132a0090
+ 00bd0940 bytes b32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af9fdc884e239b3f9d02ff0da6ee0dc0"></a>

### [`00b61474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61474.md) → [`00bd0974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0974.md) _ZN8firebase4auth27api_not_available_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd09a0",
      "incomplete_value": true,
      "site": "00bd09a0",
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
    "old": {
      "definition_site": "00b614a0",
      "incomplete_value": true,
      "site": "00b614a0",
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
            "const:5a0:8"
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
      "definition_site": "00bd0988",
      "incomplete_value": true,
      "site": "00bd0988",
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
      "definition_site": "00b61488",
      "incomplete_value": true,
      "site": "00b61488",
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
      "definition_site": "00bd0990",
      "incomplete_value": false,
      "site": "00bd0998",
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
            "const:374:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61490",
      "incomplete_value": false,
      "site": "00b61498",
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
            "const:739:8"
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
      "00bd0984",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0990",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00bd09a0",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0984",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0990",
      "PARAM",
      [
        "storage",
        "002a7374",
        null,
        "string"
      ]
    ],
    [
      "00bd09a0",
      "WRITE",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61474.md#insn-00b61498) · [`00b614a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61474.md#insn-00b614a0) · [`00b61480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61474.md#insn-00b61480)
- 新版 `00bd0998`（命令位置の公開資料なし） · `00bd09a0`（命令位置の公開資料なし） · `00bd0980`（命令位置の公開資料なし）

~~~diff
- 00b61498 ["INT_ADD", "register:40f0:8", ["const:b61498:8", "const:4:8"]]
- 00b61498 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0998 ["INT_ADD", "register:40f0:8", ["const:bd0998:8", "const:4:8"]]
+ 00bd0998 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61498 bytes fef20194
+ 00bd0998 bytes 5e280294
- 00b614a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b614a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd09a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00bd09a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b614a0 bytes 60d202f9
+ 00bd09a0 bytes 605602f9
- 00b61480 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd0980 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b61480 bytes 132a0090
+ 00bd0980 bytes b32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1468cca4cfe62635b80c98d3f5ad153"></a>

### [`00b614f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b614f8.md) → [`00bd09f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd09f8.md) _ZN8firebase4auth27api_not_available_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd0a28",
      "incomplete_value": true,
      "site": "00bd0a28",
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
    "old": {
      "definition_site": "00b61528",
      "incomplete_value": true,
      "site": "00b61528",
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
            "const:5a0:8"
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
      "definition_site": "00bd0a0c",
      "incomplete_value": true,
      "site": "00bd0a0c",
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
      "definition_site": "00b6150c",
      "incomplete_value": true,
      "site": "00b6150c",
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
      "definition_site": "00bd0a14",
      "incomplete_value": false,
      "site": "00bd0a20",
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
            "const:374:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61514",
      "incomplete_value": false,
      "site": "00b61520",
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
            "const:739:8"
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
      "00bd0a08",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0a14",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00bd0a28",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0a08",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0a14",
      "PARAM",
      [
        "storage",
        "002a7374",
        null,
        "string"
      ]
    ],
    [
      "00bd0a28",
      "WRITE",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b614f8.md#insn-00b61520) · [`00b61528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b614f8.md#insn-00b61528) · [`00b61504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b614f8.md#insn-00b61504)
- 新版 `00bd0a20`（命令位置の公開資料なし） · `00bd0a28`（命令位置の公開資料なし） · `00bd0a04`（命令位置の公開資料なし）

~~~diff
- 00b61520 ["INT_ADD", "register:40f0:8", ["const:b61520:8", "const:4:8"]]
- 00b61520 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0a20 ["INT_ADD", "register:40f0:8", ["const:bd0a20:8", "const:4:8"]]
+ 00bd0a20 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61520 bytes dcf20194
+ 00bd0a20 bytes 3c280294
- 00b61528 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
- 00b61528 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd0a28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
+ 00bd0a28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61528 bytes 60d202f9
+ 00bd0a28 bytes 605602f9
- 00b61504 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd0a04 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b61504 bytes 132a0090
+ 00bd0a04 bytes b32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-127ea79d2f3d6b1930c2cafd81d2fe77"></a>

### [`00b61548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61548.md) → [`00bd0a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0a48.md) _ZN8firebase4auth27api_not_available_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd0aa0",
      "incomplete_value": true,
      "site": "00bd0aa0",
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
    "old": {
      "definition_site": "00b615a0",
      "incomplete_value": true,
      "site": "00b615a0",
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
            "const:5a8:8"
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
      "definition_site": "00bd0a7c",
      "incomplete_value": true,
      "site": "00bd0a88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:4a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6157c",
      "incomplete_value": true,
      "site": "00b61588",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:5a0:8"
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
      "00bd0a5c",
      "READ",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd0a7c",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0aa0",
      "WRITE",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd0a5c",
      "READ",
      [
        "storage",
        "011264b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd0a7c",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0aa0",
      "WRITE",
      [
        "storage",
        "011264b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61548.md#insn-00b61588) · [`00b615a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61548.md#insn-00b615a0) · [`00b61558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61548.md#insn-00b61558)
- 新版 `00bd0a88`（命令位置の公開資料なし） · `00bd0aa0`（命令位置の公開資料なし） · `00bd0a58`（命令位置の公開資料なし）

~~~diff
- 00b61588 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61588 ["INT_ADD", "register:40f0:8", ["const:b61588:8", "const:4:8"]]
- 00b61588 ["CALLIND", null, ["register:0:8"]]
+ 00bd0a88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0a88 ["INT_ADD", "register:40f0:8", ["const:bd0a88:8", "const:4:8"]]
+ 00bd0a88 ["CALLIND", null, ["register:0:8"]]
- 00b61588 bytes 00013fd6
+ 00bd0a88 bytes 00013fd6
- 00b615a0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b615a0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5a8:8"]]
- 00b615a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd0aa0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd0aa0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4b0:8"]]
+ 00bd0aa0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b615a0 bytes a0a21639
+ 00bd0aa0 bytes a0c21239
- 00b61558 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd0a58 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b61558 bytes 152a0090
+ 00bd0a58 bytes b52a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc4738ce2a348339acae9e1a14379a3f"></a>

### [`00b615b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b615b4.md) → [`00bd0ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0ab4.md) _ZN8firebase4auth27api_not_available_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

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
      "definition_site": "00bd0af0",
      "incomplete_value": true,
      "site": "00bd0af0",
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
    "old": {
      "definition_site": "00b615f0",
      "incomplete_value": true,
      "site": "00b615f0",
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
            "const:5a8:8"
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
      "definition_site": "00bd0b10",
      "incomplete_value": true,
      "site": "00bd0b10",
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
    "old": {
      "definition_site": "00b61610",
      "incomplete_value": true,
      "site": "00b61610",
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
            "const:5a0:8"
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
      "definition_site": "00bd0acc",
      "incomplete_value": true,
      "site": "00bd0acc",
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
      "definition_site": "00b615cc",
      "incomplete_value": true,
      "site": "00b615cc",
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
      "00bd0ac8",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0ad4",
      "READ",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd0af0",
      "WRITE",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd0ac8",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0ad4",
      "READ",
      [
        "storage",
        "011264b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd0af0",
      "WRITE",
      [
        "storage",
        "011264b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b615f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b615b4.md#insn-00b615f0) · [`00b6160c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b615b4.md#insn-00b6160c) · [`00b61610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b615b4.md#insn-00b61610)
- 新版 `00bd0af0`（命令位置の公開資料なし） · `00bd0b0c`（命令位置の公開資料なし） · `00bd0b10`（命令位置の公開資料なし）

~~~diff
- 00b615f0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b615f0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b615f0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5a8:8"]]
- 00b615f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd0af0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd0af0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd0af0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4b0:8"]]
+ 00bd0af0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b615f0 bytes bfa21639
+ 00bd0af0 bytes bfc21239
- 00b6160c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6160c ["INT_ADD", "register:40f0:8", ["const:b6160c:8", "const:4:8"]]
- 00b6160c ["CALLIND", null, ["register:0:8"]]
+ 00bd0b0c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0b0c ["INT_ADD", "register:40f0:8", ["const:bd0b0c:8", "const:4:8"]]
+ 00bd0b0c ["CALLIND", null, ["register:0:8"]]
- 00b6160c bytes 00013fd6
+ 00bd0b0c bytes 00013fd6
- 00b61610 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b61610 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b61610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd0b10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
+ 00bd0b10 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd0b10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b61610 bytes 9fd202f9
+ 00bd0b10 bytes 9f5602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36b9b3a24ceda89a4e359bdef0632100"></a>

### [`00b61624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61624.md) → [`00bd0b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0b24.md) _ZN8firebase4auth27api_not_available_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00b61664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0b64"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61640"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61638",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61640",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0b68"
      ]
    ],
    [
      "unmatched:00b61648",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd0b38",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0b40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0b68"
      ]
    ],
    [
      "00bd0b48",
      "PARAM",
      [
        "storage",
        "002a7374",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61624.md#insn-00b61640) · [`00b6165c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61624.md#insn-00b6165c) · [`00b61664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61624.md#insn-00b61664)
- 新版 `00bd0b5c`（命令位置の公開資料なし）

~~~diff
- 00b61640 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61640 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b61640 bytes 410100b5
- 00b6165c ["INT_ADD", "register:40f0:8", ["const:b6165c:8", "const:4:8"]]
- 00b6165c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0b5c ["INT_ADD", "register:40f0:8", ["const:bd0b5c:8", "const:4:8"]]
+ 00bd0b5c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6165c bytes 8df20194
+ 00bd0b5c bytes ed270294
- 00b61664 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b61664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61664 bytes 80d202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e4ab13d82a5878a6a462a0afbc3c384"></a>

### [`00b61694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61694.md) → [`00bd0b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0b94.md) _ZN8firebase4auth27api_not_available_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bd0bb0",
      "incomplete_value": false,
      "site": "00bd0bb4",
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
    "old": {
      "definition_site": "00b616b0",
      "incomplete_value": false,
      "site": "00b616b4",
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
            "const:547:8"
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
      "definition_site": "00bd0bc0",
      "incomplete_value": true,
      "site": "00bd0bcc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b616c0",
      "incomplete_value": true,
      "site": "00b616cc",
      "value": [
        "LOAD",
        "8",
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
      "00bd0bb0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd0bc0",
      "DATA",
      [
        "storage",
        "010a15b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd0bb0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd0bc0",
      "DATA",
      [
        "storage",
        "011264b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b616b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61694.md#insn-00b616b4) · [`00b616ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61694.md#insn-00b616ac) · [`00b616b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61694.md#insn-00b616b0)
- 新版 `00bd0bb4`（命令位置の公開資料なし） · `00bd0bac`（命令位置の公開資料なし） · `00bd0bb0`（命令位置の公開資料なし）

~~~diff
- 00b616b4 ["INT_ADD", "register:40f0:8", ["const:b616b4:8", "const:4:8"]]
- 00b616b4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd0bb4 ["INT_ADD", "register:40f0:8", ["const:bd0bb4:8", "const:4:8"]]
+ 00bd0bb4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b616b4 bytes b3f20194
+ 00bd0bb4 bytes 13280294
- 00b616ac ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd0bac ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b616ac bytes a0b9fff0
+ 00bd0bac bytes c0b6ff90
- 00b616b0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b616b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b616b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b616b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd0bb0 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd0bb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0bb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd0bb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b616b0 bytes 001c1591
+ 00bd0bb0 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e00d8cb6fa230ef321c47d80f4c1c317"></a>

### [`00b616d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b616d0.md) → [`00bd0bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0bd0.md) _ZN8firebase4auth27api_not_available_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd0c10",
      "incomplete_value": true,
      "site": "00bd0c10",
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
    "old": {
      "definition_site": "00b61710",
      "incomplete_value": true,
      "site": "00b61710",
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
            "const:5a0:8"
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
      "definition_site": "00bd0bec",
      "incomplete_value": true,
      "site": "00bd0bec",
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
      "definition_site": "00b616ec",
      "incomplete_value": true,
      "site": "00b616ec",
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
      "definition_site": "00bd0bf4",
      "incomplete_value": false,
      "site": "00bd0c08",
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
            "const:374:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b616f4",
      "incomplete_value": false,
      "site": "00b61708",
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
            "const:739:8"
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
      "00bd0be4",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0bf4",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00bd0c10",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0be4",
      "READ",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0bf4",
      "PARAM",
      [
        "storage",
        "002a7374",
        null,
        "string"
      ]
    ],
    [
      "00bd0c10",
      "WRITE",
      [
        "storage",
        "011264a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b616d0.md#insn-00b61708) · [`00b61710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b616d0.md#insn-00b61710) · [`00b616dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b616d0.md#insn-00b616dc)
- 新版 `00bd0c08`（命令位置の公開資料なし） · `00bd0c10`（命令位置の公開資料なし） · `00bd0bdc`（命令位置の公開資料なし）

~~~diff
- 00b61708 ["INT_ADD", "register:40f0:8", ["const:b61708:8", "const:4:8"]]
- 00b61708 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0c08 ["INT_ADD", "register:40f0:8", ["const:bd0c08:8", "const:4:8"]]
+ 00bd0c08 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61708 bytes 62f20194
+ 00bd0c08 bytes c2270294
- 00b61710 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
- 00b61710 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd0c10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
+ 00bd0c10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61710 bytes 80d202f9
+ 00bd0c10 bytes 805602f9
- 00b616dc ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd0bdc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b616dc bytes 142a0090
+ 00bd0bdc bytes b42a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-159ebc81a9a11a08715f33d317a2e803"></a>

### [`00b6177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6177c.md) → [`00bd0c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0c7c.md) _ZN8firebase4auth21action_code_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 20.00% / 新版 25.00%

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
      "site": "00b617a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0ca8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd0c90",
      "incomplete_value": true,
      "site": "00bd0c90",
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
      "definition_site": "00b61790",
      "incomplete_value": true,
      "site": "00b61790",
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
      "00bd0c8c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6179c",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b617a0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bd0c8c",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0c9c",
      "PARAM",
      [
        "storage",
        "002a4f33",
        null,
        "string"
      ]
    ],
    [
      "00bd0ca0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6177c.md#insn-00b61790) · [`00b617a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6177c.md#insn-00b617a0) · [`00b617a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6177c.md#insn-00b617a8)
- 新版 `00bd0c90`（命令位置の公開資料なし）

~~~diff
- 00b61790 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b61790 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd0c90 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd0c90 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b61790 bytes e80000b5
+ 00bd0c90 bytes e80000b5
- 00b617a0 ["INT_ADD", "register:40f0:8", ["const:b617a0:8", "const:4:8"]]
- 00b617a0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b617a0 bytes 3cf20194
- 00b617a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b617a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b617a8 bytes 60e202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-138fd988dfb840238909e573682c23b2"></a>

### [`00b617fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b617fc.md) → [`00bd0cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0cfc.md) _ZN8firebase4auth21action_code_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd0d2c",
      "incomplete_value": true,
      "site": "00bd0d2c",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6182c",
      "incomplete_value": true,
      "site": "00b6182c",
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
            "const:5c0:8"
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
      "definition_site": "00bd0d10",
      "incomplete_value": true,
      "site": "00bd0d10",
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
      "definition_site": "00b61810",
      "incomplete_value": true,
      "site": "00b61810",
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
      "definition_site": "00bd0d1c",
      "incomplete_value": false,
      "site": "00bd0d24",
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
            "const:f33:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6181c",
      "incomplete_value": false,
      "site": "00b61824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:4fa:8"
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
      "00bd0d0c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0d1c",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "00bd0d2c",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0d0c",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0d1c",
      "PARAM",
      [
        "storage",
        "002a4f33",
        null,
        "string"
      ]
    ],
    [
      "00bd0d2c",
      "WRITE",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b617fc.md#insn-00b61824) · [`00b6182c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b617fc.md#insn-00b6182c) · [`00b61808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b617fc.md#insn-00b61808)
- 新版 `00bd0d24`（命令位置の公開資料なし） · `00bd0d2c`（命令位置の公開資料なし） · `00bd0d08`（命令位置の公開資料なし）

~~~diff
- 00b61824 ["INT_ADD", "register:40f0:8", ["const:b61824:8", "const:4:8"]]
- 00b61824 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0d24 ["INT_ADD", "register:40f0:8", ["const:bd0d24:8", "const:4:8"]]
+ 00bd0d24 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61824 bytes 1bf20194
+ 00bd0d24 bytes 7b270294
- 00b6182c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b6182c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd0d2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00bd0d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6182c bytes 60e202f9
+ 00bd0d2c bytes 606602f9
- 00b61808 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd0d08 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b61808 bytes 132a0090
+ 00bd0d08 bytes b32a00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0afe05bbccb12b9e2b27942f27d9baf"></a>

### [`00b61840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61840.md) → [`00bd0d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0d40.md) _ZN8firebase4auth21action_code_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b61870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0d70"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd0d54",
      "incomplete_value": true,
      "site": "00bd0d54",
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
      "definition_site": "00b61854",
      "incomplete_value": true,
      "site": "00b61854",
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
      "00bd0d50",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0d54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b61874"
      ]
    ],
    [
      "unmatched:00b6185c",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd0d50",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0d54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0d74"
      ]
    ],
    [
      "00bd0d5c",
      "PARAM",
      [
        "storage",
        "002a4f33",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61840.md#insn-00b61868) · [`00b61870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61840.md#insn-00b61870) · [`00b61880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61840.md#insn-00b61880)
- 新版 `00bd0d68`（命令位置の公開資料なし）

~~~diff
- 00b61868 ["INT_ADD", "register:40f0:8", ["const:b61868:8", "const:4:8"]]
- 00b61868 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0d68 ["INT_ADD", "register:40f0:8", ["const:bd0d68:8", "const:4:8"]]
+ 00bd0d68 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61868 bytes 0af20194
+ 00bd0d68 bytes 6a270294
- 00b61870 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
- 00b61870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61870 bytes 60e202f9
- 00b61880 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b61880 ["RETURN", null, ["register:0:8"]]
- 00b61880 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d186a4ed111742326e69471b46a03c3"></a>

### [`00b61890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61890.md) → [`00bd0d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0d90.md) _ZN8firebase4auth21action_code_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 16.67% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b618e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0de8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bd0dc4",
      "incomplete_value": true,
      "site": "00bd0dd0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b618c4",
      "incomplete_value": true,
      "site": "00b618d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:5c0:8"
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
      "00bd0da4",
      "READ",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd0db0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b618ec"
      ]
    ],
    [
      "unmatched:00b618c4",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd0da4",
      "READ",
      [
        "storage",
        "011264d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd0db0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0dec"
      ]
    ],
    [
      "00bd0dc4",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b618d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61890.md#insn-00b618d0) · [`00b618e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61890.md#insn-00b618e8) · [`00b618f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61890.md#insn-00b618f8)
- 新版 `00bd0dd0`（命令位置の公開資料なし）

~~~diff
- 00b618d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b618d0 ["INT_ADD", "register:40f0:8", ["const:b618d0:8", "const:4:8"]]
- 00b618d0 ["CALLIND", null, ["register:0:8"]]
+ 00bd0dd0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd0dd0 ["INT_ADD", "register:40f0:8", ["const:bd0dd0:8", "const:4:8"]]
+ 00bd0dd0 ["CALLIND", null, ["register:0:8"]]
- 00b618d0 bytes 00013fd6
+ 00bd0dd0 bytes 00013fd6
- 00b618e8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b618e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5c8:8"]]
- 00b618e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b618e8 bytes a0221739
- 00b618f8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b618f8 ["RETURN", null, ["register:0:8"]]
- 00b618f8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2bd39e546884b0c57c571d52fa58873"></a>

### [`00b618fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b618fc.md) → [`00bd0dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0dfc.md) _ZN8firebase4auth21action_code_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b618fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61900"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61900"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b618fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61900",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61904",
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
      "00bd0dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bd0e00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd0e04",
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

- 旧版 [`00b618fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b618fc.md#insn-00b618fc) · [`00b61900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b618fc.md#insn-00b61900) · [`00b61904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b618fc.md#insn-00b61904)

~~~diff
- 00b618fc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b618fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b618fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b618fc bytes f50f1df8
- 00b61900 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b61900 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b61900 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b61900 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61900 bytes f44f01a9
- 00b61904 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b61904 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b61904 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b61904 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61904 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6eed1752edd1e8fba31085299f669d9"></a>

### [`00b6196c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6196c.md) → [`00bd0e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0e6c.md) _ZN8firebase4auth21action_code_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b619ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0eac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61988"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61980",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61988",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0eb0"
      ]
    ],
    [
      "unmatched:00b61990",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd0e80",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0e88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0eb0"
      ]
    ],
    [
      "00bd0e90",
      "PARAM",
      [
        "storage",
        "002a4f33",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6196c.md#insn-00b61988) · [`00b619a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6196c.md#insn-00b619a4) · [`00b619ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6196c.md#insn-00b619ac)
- 新版 `00bd0ea4`（命令位置の公開資料なし）

~~~diff
- 00b61988 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61988 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b61988 bytes 410100b5
- 00b619a4 ["INT_ADD", "register:40f0:8", ["const:b619a4:8", "const:4:8"]]
- 00b619a4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0ea4 ["INT_ADD", "register:40f0:8", ["const:bd0ea4:8", "const:4:8"]]
+ 00bd0ea4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b619a4 bytes bbf10194
+ 00bd0ea4 bytes 1b270294
- 00b619ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b619ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b619ac bytes 80e202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84ed609b78423dd714231e680eb9fb7f"></a>

### [`00b61a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61a18.md) → [`00bd0f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0f18.md) _ZN8firebase4auth21action_code_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b61a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0f58"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61a34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61a2c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61a34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0f5c"
      ]
    ],
    [
      "unmatched:00b61a3c",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd0f2c",
      "READ",
      [
        "storage",
        "011264c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0f34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd0f5c"
      ]
    ],
    [
      "00bd0f3c",
      "PARAM",
      [
        "storage",
        "002a4f33",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61a18.md#insn-00b61a34) · [`00b61a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61a18.md#insn-00b61a50) · [`00b61a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61a18.md#insn-00b61a58)
- 新版 `00bd0f50`（命令位置の公開資料なし）

~~~diff
- 00b61a34 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61a34 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b61a34 bytes 410100b5
- 00b61a50 ["INT_ADD", "register:40f0:8", ["const:b61a50:8", "const:4:8"]]
- 00b61a50 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd0f50 ["INT_ADD", "register:40f0:8", ["const:bd0f50:8", "const:4:8"]]
+ 00bd0f50 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61a50 bytes 90f10194
+ 00bd0f50 bytes f0260294
- 00b61a58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
- 00b61a58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61a58 bytes 80e202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d842ef3028c0b56d5d53ef795b0d06d"></a>

### [`00b61ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ac4.md) → [`00bd0fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0fc4.md) _ZN8firebase4auth15email_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00b61af0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd0ff0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd0fd8",
      "incomplete_value": true,
      "site": "00bd0fd8",
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
      "definition_site": "00b61ad8",
      "incomplete_value": true,
      "site": "00b61ad8",
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
      "00bd0fd4",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61ae4",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b61ae8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bd0fd4",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd0fe4",
      "PARAM",
      [
        "storage",
        "002a1bb7",
        null,
        "string"
      ]
    ],
    [
      "00bd0fe8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ac4.md#insn-00b61ad8) · [`00b61ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ac4.md#insn-00b61ae8) · [`00b61af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ac4.md#insn-00b61af0)
- 新版 `00bd0fd8`（命令位置の公開資料なし）

~~~diff
- 00b61ad8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b61ad8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd0fd8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd0fd8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b61ad8 bytes e80000b5
+ 00bd0fd8 bytes e80000b5
- 00b61ae8 ["INT_ADD", "register:40f0:8", ["const:b61ae8:8", "const:4:8"]]
- 00b61ae8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61ae8 bytes 6af10194
- 00b61af0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b61af0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61af0 bytes 60f202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-280edeb5404b55ff21ad6b8e449cf5bf"></a>

### [`00b61b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b44.md) → [`00bd1044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1044.md) _ZN8firebase4auth15email_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b61b74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1074"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd1058",
      "incomplete_value": true,
      "site": "00bd1058",
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
      "definition_site": "00b61b58",
      "incomplete_value": true,
      "site": "00b61b58",
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
      "00bd1054",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1058",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b61b78"
      ]
    ],
    [
      "unmatched:00b61b64",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd1054",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1058",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1078"
      ]
    ],
    [
      "00bd1064",
      "PARAM",
      [
        "storage",
        "002a1bb7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b44.md#insn-00b61b6c) · [`00b61b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b44.md#insn-00b61b74) · [`00b61b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b44.md#insn-00b61b84)

~~~diff
- 00b61b6c ["INT_ADD", "register:40f0:8", ["const:b61b6c:8", "const:4:8"]]
- 00b61b6c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61b6c bytes 49f10194
- 00b61b74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b61b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61b74 bytes 60f202f9
- 00b61b84 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b61b84 ["RETURN", null, ["register:0:8"]]
- 00b61b84 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6adcd429b6372164459790f57b4b7e18"></a>

### [`00b61b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b88.md) → [`00bd1088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1088.md) _ZN8firebase4auth15email_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61bb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd10b8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd109c",
      "incomplete_value": true,
      "site": "00bd109c",
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
      "definition_site": "00b61b9c",
      "incomplete_value": true,
      "site": "00b61b9c",
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
      "00bd1098",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61ba4",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b61bb8",
      "WRITE",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1098",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd10a4",
      "PARAM",
      [
        "storage",
        "002a1bb7",
        null,
        "string"
      ]
    ],
    [
      "00bd10b8",
      "WRITE",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b88.md#insn-00b61b9c) · [`00b61bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b88.md#insn-00b61bb0) · [`00b61bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61b88.md#insn-00b61bb8)
- 新版 `00bd109c`（命令位置の公開資料なし） · `00bd10b0`（命令位置の公開資料なし）

~~~diff
- 00b61b9c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b61b9c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd109c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd109c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b61b9c bytes 080100b5
+ 00bd109c bytes 080100b5
- 00b61bb0 ["INT_ADD", "register:40f0:8", ["const:b61bb0:8", "const:4:8"]]
- 00b61bb0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd10b0 ["INT_ADD", "register:40f0:8", ["const:bd10b0:8", "const:4:8"]]
+ 00bd10b0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61bb0 bytes 38f10194
+ 00bd10b0 bytes 98260294
- 00b61bb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e0:8"]]
- 00b61bb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61bb8 bytes 60f202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9e1069c489feaf912f98466512c5cfb"></a>

### [`00b61bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61bd8.md) → [`00bd10d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd10d8.md) _ZN8firebase4auth15email_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd1130",
      "incomplete_value": true,
      "site": "00bd1130",
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
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61c30",
      "incomplete_value": true,
      "site": "00b61c30",
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
            "const:5e8:8"
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
      "definition_site": "00bd110c",
      "incomplete_value": true,
      "site": "00bd1118",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:4e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61c0c",
      "incomplete_value": true,
      "site": "00b61c18",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:5e0:8"
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
      "00bd10ec",
      "READ",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd110c",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1130",
      "WRITE",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd10ec",
      "READ",
      [
        "storage",
        "011264f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd110c",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1130",
      "WRITE",
      [
        "storage",
        "011264f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61bd8.md#insn-00b61c18) · [`00b61c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61bd8.md#insn-00b61c30) · [`00b61be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61bd8.md#insn-00b61be8)
- 新版 `00bd1118`（命令位置の公開資料なし） · `00bd1130`（命令位置の公開資料なし） · `00bd10e8`（命令位置の公開資料なし）

~~~diff
- 00b61c18 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61c18 ["INT_ADD", "register:40f0:8", ["const:b61c18:8", "const:4:8"]]
- 00b61c18 ["CALLIND", null, ["register:0:8"]]
+ 00bd1118 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1118 ["INT_ADD", "register:40f0:8", ["const:bd1118:8", "const:4:8"]]
+ 00bd1118 ["CALLIND", null, ["register:0:8"]]
- 00b61c18 bytes 00013fd6
+ 00bd1118 bytes 00013fd6
- 00b61c30 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b61c30 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5e8:8"]]
- 00b61c30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd1130 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd1130 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4f0:8"]]
+ 00bd1130 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b61c30 bytes a0a21739
+ 00bd1130 bytes a0c21339
- 00b61be8 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd10e8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b61be8 bytes 152a0090
+ 00bd10e8 bytes b52a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3feab13a0edb65bd671bdabb88375ec4"></a>

### [`00b61c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61c44.md) → [`00bd1144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1144.md) _ZN8firebase4auth15email_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61c80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61ca0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1180"
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
      "00bd1158",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd115c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b61ca4"
      ]
    ],
    [
      "00bd1164",
      "READ",
      [
        "storage",
        "010a15e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1158",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd115c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd11a4"
      ]
    ],
    [
      "00bd1164",
      "READ",
      [
        "storage",
        "011264f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61c44.md#insn-00b61c5c) · [`00b61c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61c44.md#insn-00b61c80) · [`00b61c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61c44.md#insn-00b61c88)
- 新版 `00bd115c`（命令位置の公開資料なし）

~~~diff
- 00b61c5c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61c5c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd115c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd115c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b61c5c bytes 410200b4
+ 00bd115c bytes 410200b4
- 00b61c80 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b61c80 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b61c80 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5e8:8"]]
- 00b61c80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b61c80 bytes bfa21739
- 00b61c88 ["INT_ADD", "register:40f0:8", ["const:b61c88:8", "const:4:8"]]
- 00b61c88 ["CALL", null, ["callee:00c5ab60:8"]]
- 00b61c88 bytes 16f10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b1eb020b74caf65e4b8074e26bf5585"></a>

### [`00b61cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61cb4.md) → [`00bd11b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd11b4.md) _ZN8firebase4auth15email_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61cb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61cb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61cb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61cb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61cb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b61cc8",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd11b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd11b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd11c8",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61cb4.md#insn-00b61cb4) · [`00b61cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61cb4.md#insn-00b61cb8) · [`00b61cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61cb4.md#insn-00b61cd0)

~~~diff
- 00b61cb4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b61cb4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b61cb4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b61cb4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b61cb4 bytes f44fbea9
- 00b61cb8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b61cb8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b61cb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b61cb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b61cb8 bytes fd7b01a9
- 00b61cd0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61cd0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b61cd0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39c3cf1ca37c18e9cd40376b1c639408"></a>

### [`00b61d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d60.md) → [`00bd1260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1260.md) _ZN8firebase4auth15email_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00b61da0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd12a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61d7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b61d74",
      "READ",
      [
        "storage",
        "010a15e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b61d7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd12a4"
      ]
    ],
    [
      "unmatched:00b61d84",
      "PARAM",
      [
        "storage",
        "002924a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd1274",
      "READ",
      [
        "storage",
        "011264e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd127c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd12a4"
      ]
    ],
    [
      "00bd1284",
      "PARAM",
      [
        "storage",
        "002a1bb7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d60.md#insn-00b61d7c) · [`00b61d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d60.md#insn-00b61d98) · [`00b61da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61d60.md#insn-00b61da0)
- 新版 `00bd1298`（命令位置の公開資料なし）

~~~diff
- 00b61d7c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61d7c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b61d7c bytes 410100b5
- 00b61d98 ["INT_ADD", "register:40f0:8", ["const:b61d98:8", "const:4:8"]]
- 00b61d98 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1298 ["INT_ADD", "register:40f0:8", ["const:bd1298:8", "const:4:8"]]
+ 00bd1298 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61d98 bytes bef00194
+ 00bd1298 bytes 1e260294
- 00b61da0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e0:8"]]
- 00b61da0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61da0 bytes 80f202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f7ade9d1eb94e51b170c3428169d7a8"></a>

### [`00b61e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e0c.md) → [`00bd130c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd130c.md) _ZN8firebase4auth23weak_password_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd1338",
      "incomplete_value": true,
      "site": "00bd1338",
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
    "old": {
      "definition_site": "00b61e38",
      "incomplete_value": true,
      "site": "00b61e38",
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
            "const:600:8"
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
      "definition_site": "00bd1320",
      "incomplete_value": true,
      "site": "00bd1320",
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
      "definition_site": "00b61e20",
      "incomplete_value": true,
      "site": "00b61e20",
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
      "definition_site": "00bd132c",
      "incomplete_value": false,
      "site": "00bd1330",
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
            "const:52a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61e2c",
      "incomplete_value": false,
      "site": "00b61e30",
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
            "const:117:8"
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
      "00bd131c",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd132c",
      "PARAM",
      [
        "storage",
        "0029f117",
        null,
        "string"
      ]
    ],
    [
      "00bd1338",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd131c",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd132c",
      "PARAM",
      [
        "storage",
        "002af52a",
        null,
        "string"
      ]
    ],
    [
      "00bd1338",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e0c.md#insn-00b61e30) · [`00b61e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e0c.md#insn-00b61e38) · [`00b61e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e0c.md#insn-00b61e18)
- 新版 `00bd1330`（命令位置の公開資料なし） · `00bd1338`（命令位置の公開資料なし） · `00bd1318`（命令位置の公開資料なし）

~~~diff
- 00b61e30 ["INT_ADD", "register:40f0:8", ["const:b61e30:8", "const:4:8"]]
- 00b61e30 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1330 ["INT_ADD", "register:40f0:8", ["const:bd1330:8", "const:4:8"]]
+ 00bd1330 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61e30 bytes 98f00194
+ 00bd1330 bytes f8250294
- 00b61e38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b61e38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1338 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00bd1338 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61e38 bytes 600203f9
+ 00bd1338 bytes 608602f9
- 00b61e18 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd1318 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b61e18 bytes 132a0090
+ 00bd1318 bytes b32a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfcce5fd09348a440cd44bccf0205afa"></a>

### [`00b61e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e4c.md) → [`00bd134c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd134c.md) _ZN8firebase4auth23weak_password_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd1378",
      "incomplete_value": true,
      "site": "00bd1378",
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
    "old": {
      "definition_site": "00b61e78",
      "incomplete_value": true,
      "site": "00b61e78",
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
            "const:600:8"
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
      "definition_site": "00bd1360",
      "incomplete_value": true,
      "site": "00bd1360",
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
      "definition_site": "00b61e60",
      "incomplete_value": true,
      "site": "00b61e60",
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
      "definition_site": "00bd1368",
      "incomplete_value": false,
      "site": "00bd1370",
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
            "const:52a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61e68",
      "incomplete_value": false,
      "site": "00b61e70",
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
            "const:117:8"
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
      "00bd135c",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1368",
      "PARAM",
      [
        "storage",
        "0029f117",
        null,
        "string"
      ]
    ],
    [
      "00bd1378",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd135c",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1368",
      "PARAM",
      [
        "storage",
        "002af52a",
        null,
        "string"
      ]
    ],
    [
      "00bd1378",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e4c.md#insn-00b61e70) · [`00b61e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e4c.md#insn-00b61e78) · [`00b61e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61e4c.md#insn-00b61e58)
- 新版 `00bd1370`（命令位置の公開資料なし） · `00bd1378`（命令位置の公開資料なし） · `00bd1358`（命令位置の公開資料なし）

~~~diff
- 00b61e70 ["INT_ADD", "register:40f0:8", ["const:b61e70:8", "const:4:8"]]
- 00b61e70 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1370 ["INT_ADD", "register:40f0:8", ["const:bd1370:8", "const:4:8"]]
+ 00bd1370 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61e70 bytes 88f00194
+ 00bd1370 bytes e8250294
- 00b61e78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b61e78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00bd1378 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61e78 bytes 600203f9
+ 00bd1378 bytes 608602f9
- 00b61e58 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd1358 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b61e58 bytes 132a0090
+ 00bd1358 bytes b32a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55ce27c6d28eb6e38a09622f9e119572"></a>

### [`00b61ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ed0.md) → [`00bd13d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd13d0.md) _ZN8firebase4auth23weak_password_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd1400",
      "incomplete_value": true,
      "site": "00bd1400",
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
    "old": {
      "definition_site": "00b61f00",
      "incomplete_value": true,
      "site": "00b61f00",
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
            "const:600:8"
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
      "definition_site": "00bd13e4",
      "incomplete_value": true,
      "site": "00bd13e4",
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
      "definition_site": "00b61ee4",
      "incomplete_value": true,
      "site": "00b61ee4",
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
      "definition_site": "00bd13ec",
      "incomplete_value": false,
      "site": "00bd13f8",
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
            "const:52a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61eec",
      "incomplete_value": false,
      "site": "00b61ef8",
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
            "const:117:8"
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
      "00bd13e0",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd13ec",
      "PARAM",
      [
        "storage",
        "0029f117",
        null,
        "string"
      ]
    ],
    [
      "00bd1400",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd13e0",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd13ec",
      "PARAM",
      [
        "storage",
        "002af52a",
        null,
        "string"
      ]
    ],
    [
      "00bd1400",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ed0.md#insn-00b61ef8) · [`00b61f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ed0.md#insn-00b61f00) · [`00b61edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ed0.md#insn-00b61edc)
- 新版 `00bd13f8`（命令位置の公開資料なし） · `00bd1400`（命令位置の公開資料なし） · `00bd13dc`（命令位置の公開資料なし）

~~~diff
- 00b61ef8 ["INT_ADD", "register:40f0:8", ["const:b61ef8:8", "const:4:8"]]
- 00b61ef8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd13f8 ["INT_ADD", "register:40f0:8", ["const:bd13f8:8", "const:4:8"]]
+ 00bd13f8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b61ef8 bytes 66f00194
+ 00bd13f8 bytes c6250294
- 00b61f00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b61f00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1400 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00bd1400 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61f00 bytes 600203f9
+ 00bd1400 bytes 608602f9
- 00b61edc ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd13dc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b61edc bytes 132a0090
+ 00bd13dc bytes b32a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d41dcaa632e7dd8a0dceebd2207f5fe5"></a>

### [`00b61f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f20.md) → [`00bd1420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1420.md) _ZN8firebase4auth23weak_password_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd1478",
      "incomplete_value": true,
      "site": "00bd1478",
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
    "old": {
      "definition_site": "00b61f78",
      "incomplete_value": true,
      "site": "00b61f78",
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
            "const:608:8"
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
      "definition_site": "00bd1454",
      "incomplete_value": true,
      "site": "00bd1460",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "old": {
      "definition_site": "00b61f54",
      "incomplete_value": true,
      "site": "00b61f60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:600:8"
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
      "00bd1434",
      "READ",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1454",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1478",
      "WRITE",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1434",
      "READ",
      [
        "storage",
        "01126510",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1454",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1478",
      "WRITE",
      [
        "storage",
        "01126510",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f20.md#insn-00b61f60) · [`00b61f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f20.md#insn-00b61f78) · [`00b61f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f20.md#insn-00b61f30)
- 新版 `00bd1460`（命令位置の公開資料なし） · `00bd1478`（命令位置の公開資料なし） · `00bd1430`（命令位置の公開資料なし）

~~~diff
- 00b61f60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61f60 ["INT_ADD", "register:40f0:8", ["const:b61f60:8", "const:4:8"]]
- 00b61f60 ["CALLIND", null, ["register:0:8"]]
+ 00bd1460 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1460 ["INT_ADD", "register:40f0:8", ["const:bd1460:8", "const:4:8"]]
+ 00bd1460 ["CALLIND", null, ["register:0:8"]]
- 00b61f60 bytes 00013fd6
+ 00bd1460 bytes 00013fd6
- 00b61f78 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b61f78 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:608:8"]]
- 00b61f78 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd1478 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd1478 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:510:8"]]
+ 00bd1478 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b61f78 bytes a0221839
+ 00bd1478 bytes a0421439
- 00b61f30 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd1430 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b61f30 bytes 152a0090
+ 00bd1430 bytes b52a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fccba14d17cb9c9733307085d19ad1b"></a>

### [`00b61f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f8c.md) → [`00bd148c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd148c.md) _ZN8firebase4auth23weak_password_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 28.57% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61fc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b61fe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd14c8"
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
      "00bd14a0",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd14ac",
      "READ",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd14b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b61fcc"
      ]
    ]
  ],
  "added": [
    [
      "00bd14a0",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd14ac",
      "READ",
      [
        "storage",
        "01126510",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd14b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd14cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f8c.md#insn-00b61fa4) · [`00b61fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f8c.md#insn-00b61fc8) · [`00b61fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61f8c.md#insn-00b61fd0)
- 新版 `00bd14a4`（命令位置の公開資料なし）

~~~diff
- 00b61fa4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b61fa4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00bd14a4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00bd14a4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b61fa4 bytes 410200b4
+ 00bd14a4 bytes 410200b4
- 00b61fc8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b61fc8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b61fc8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:608:8"]]
- 00b61fc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b61fc8 bytes bf221839
- 00b61fd0 ["INT_ADD", "register:40f0:8", ["const:b61fd0:8", "const:4:8"]]
- 00b61fd0 ["CALL", null, ["callee:00c5ab60:8"]]
- 00b61fd0 bytes 44f00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-800f0d6d63683a07e03c3541d48eece8"></a>

### [`00b61ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ffc.md) → [`00bd14fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd14fc.md) _ZN8firebase4auth23weak_password_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "definition_site": "00bd153c",
      "incomplete_value": true,
      "site": "00bd153c",
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
    "old": {
      "definition_site": "00b6203c",
      "incomplete_value": true,
      "site": "00b6203c",
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
            "const:600:8"
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
      "definition_site": "00bd1518",
      "incomplete_value": true,
      "site": "00bd1518",
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
      "definition_site": "00b62018",
      "incomplete_value": true,
      "site": "00b62018",
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
      "definition_site": "00bd1520",
      "incomplete_value": false,
      "site": "00bd1534",
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
            "const:52a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62020",
      "incomplete_value": false,
      "site": "00b62034",
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
            "const:117:8"
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
      "00bd1510",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1520",
      "PARAM",
      [
        "storage",
        "0029f117",
        null,
        "string"
      ]
    ],
    [
      "00bd153c",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1510",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1520",
      "PARAM",
      [
        "storage",
        "002af52a",
        null,
        "string"
      ]
    ],
    [
      "00bd153c",
      "WRITE",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ffc.md#insn-00b62034) · [`00b6203c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ffc.md#insn-00b6203c) · [`00b62008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61ffc.md#insn-00b62008)
- 新版 `00bd1534`（命令位置の公開資料なし） · `00bd153c`（命令位置の公開資料なし） · `00bd1508`（命令位置の公開資料なし）

~~~diff
- 00b62034 ["INT_ADD", "register:40f0:8", ["const:b62034:8", "const:4:8"]]
- 00b62034 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1534 ["INT_ADD", "register:40f0:8", ["const:bd1534:8", "const:4:8"]]
+ 00bd1534 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62034 bytes 17f00194
+ 00bd1534 bytes 77250294
- 00b6203c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b6203c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd153c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00bd153c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6203c bytes 800203f9
+ 00bd153c bytes 808602f9
- 00b62008 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd1508 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b62008 bytes f42900f0
+ 00bd1508 bytes b42a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8a695505e639bf8055793f9c3f094ea"></a>

### [`00b6206c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6206c.md) → [`00bd156c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd156c.md) _ZN8firebase4auth23weak_password_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bd1588",
      "incomplete_value": false,
      "site": "00bd158c",
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
    "old": {
      "definition_site": "00b62088",
      "incomplete_value": false,
      "site": "00b6208c",
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
            "const:547:8"
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
      "definition_site": "00bd1598",
      "incomplete_value": true,
      "site": "00bd15a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62098",
      "incomplete_value": true,
      "site": "00b620a4",
      "value": [
        "LOAD",
        "8",
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
      "00bd1588",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd1598",
      "DATA",
      [
        "storage",
        "010a1610",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd1588",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd1598",
      "DATA",
      [
        "storage",
        "01126518",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6208c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6206c.md#insn-00b6208c) · [`00b62084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6206c.md#insn-00b62084) · [`00b62088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6206c.md#insn-00b62088)
- 新版 `00bd158c`（命令位置の公開資料なし） · `00bd1584`（命令位置の公開資料なし） · `00bd1588`（命令位置の公開資料なし）

~~~diff
- 00b6208c ["INT_ADD", "register:40f0:8", ["const:b6208c:8", "const:4:8"]]
- 00b6208c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd158c ["INT_ADD", "register:40f0:8", ["const:bd158c:8", "const:4:8"]]
+ 00bd158c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6208c bytes 3df00194
+ 00bd158c bytes 9d250294
- 00b62084 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd1584 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b62084 bytes a0b9ffd0
+ 00bd1584 bytes a0b6fff0
- 00b62088 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b62088 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62088 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62088 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd1588 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd1588 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1588 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1588 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62088 bytes 001c1591
+ 00bd1588 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d96ceaff8b329d62173c271876dada56"></a>

### [`00b620a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b620a8.md) → [`00bd15a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd15a8.md) _ZN8firebase4auth23weak_password_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b620e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd15e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b620c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b620bc",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b620c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd15ec"
      ]
    ],
    [
      "unmatched:00b620cc",
      "PARAM",
      [
        "storage",
        "0029f117",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd15bc",
      "READ",
      [
        "storage",
        "01126508",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd15c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd15ec"
      ]
    ],
    [
      "00bd15cc",
      "PARAM",
      [
        "storage",
        "002af52a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b620c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b620a8.md#insn-00b620c4) · [`00b620e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b620a8.md#insn-00b620e0) · [`00b620e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b620a8.md#insn-00b620e8)
- 新版 `00bd15e0`（命令位置の公開資料なし）

~~~diff
- 00b620c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b620c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b620c4 bytes 410100b5
- 00b620e0 ["INT_ADD", "register:40f0:8", ["const:b620e0:8", "const:4:8"]]
- 00b620e0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd15e0 ["INT_ADD", "register:40f0:8", ["const:bd15e0:8", "const:4:8"]]
+ 00bd15e0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b620e0 bytes ecef0194
+ 00bd15e0 bytes 4c250294
- 00b620e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b620e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b620e8 bytes 800203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee0f1d30dfed09cf9af6d52512c30d88"></a>

### [`00b62154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62154.md) → [`00bd1654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1654.md) _ZN8firebase4auth29invalid_credentials_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

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
      "site": "00b62180"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1680"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd1668",
      "incomplete_value": true,
      "site": "00bd1668",
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
      "definition_site": "00b62168",
      "incomplete_value": true,
      "site": "00b62168",
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
      "00bd1664",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62174",
      "PARAM",
      [
        "storage",
        "002a8fb7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b62178",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bd1664",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1674",
      "PARAM",
      [
        "storage",
        "002b9c4e",
        null,
        "string"
      ]
    ],
    [
      "00bd1678",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62154.md#insn-00b62168) · [`00b62178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62154.md#insn-00b62178) · [`00b62180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62154.md#insn-00b62180)
- 新版 `00bd1668`（命令位置の公開資料なし）

~~~diff
- 00b62168 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b62168 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00bd1668 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd1668 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b62168 bytes e80000b5
+ 00bd1668 bytes e80000b5
- 00b62178 ["INT_ADD", "register:40f0:8", ["const:b62178:8", "const:4:8"]]
- 00b62178 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62178 bytes c6ef0194
- 00b62180 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b62180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62180 bytes 601203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a61b54814f6175b6bfd5e4d458064e32"></a>

### [`00b62194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62194.md) → [`00bd1694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1694.md) _ZN8firebase4auth29invalid_credentials_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b62194"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62198"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62194",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b62198",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd16a4",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1694",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd1698",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd16a4",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62194.md#insn-00b62194) · [`00b62198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62194.md#insn-00b62198) · [`00b621a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62194.md#insn-00b621a8)
- 新版 `00bd16a8`（命令位置の公開資料なし）

~~~diff
- 00b62194 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b62194 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b62194 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b62194 bytes f30f1ef8
- 00b62198 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b62198 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b62198 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b62198 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b62198 bytes fd7b01a9
- 00b621a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b621a8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00bd16a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd16a8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b621a8 bytes e80000b5
+ 00bd16a8 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6c83e02840bfb91b24f8490a3b1bfdc"></a>

### [`00b621d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b621d4.md) → [`00bd16d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd16d4.md) _ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b62204"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1704"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd16e8",
      "incomplete_value": true,
      "site": "00bd16e8",
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
      "definition_site": "00b621e8",
      "incomplete_value": true,
      "site": "00b621e8",
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
      "00bd16e4",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b621f4",
      "PARAM",
      [
        "storage",
        "002a8fb7",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b621fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00bd16e4",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd16f4",
      "PARAM",
      [
        "storage",
        "002b9c4e",
        null,
        "string"
      ]
    ],
    [
      "00bd16fc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b621e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b621d4.md#insn-00b621e8) · [`00b621fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b621d4.md#insn-00b621fc) · [`00b62204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b621d4.md#insn-00b62204)
- 新版 `00bd16e8`（命令位置の公開資料なし）

~~~diff
- 00b621e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b621e8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00bd16e8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bd16e8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b621e8 bytes 080100b5
+ 00bd16e8 bytes 080100b5
- 00b621fc ["INT_ADD", "register:40f0:8", ["const:b621fc:8", "const:4:8"]]
- 00b621fc ["CALL", null, ["callee:00c5ab10:8"]]
- 00b621fc bytes a5ef0194
- 00b62204 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b62204 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62204 bytes 601203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-684774d73a71b4630781c0cf480a807a"></a>

### [`00b62218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62218.md) → [`00bd1718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1718.md) _ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd1748",
      "incomplete_value": true,
      "site": "00bd1748",
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
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62248",
      "incomplete_value": true,
      "site": "00b62248",
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
            "const:620:8"
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
      "definition_site": "00bd172c",
      "incomplete_value": true,
      "site": "00bd172c",
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
      "definition_site": "00b6222c",
      "incomplete_value": true,
      "site": "00b6222c",
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
      "definition_site": "00bd1734",
      "incomplete_value": false,
      "site": "00bd1740",
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
            "const:c4e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62234",
      "incomplete_value": false,
      "site": "00b62240",
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
            "const:fb7:8"
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
      "00bd1728",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1734",
      "PARAM",
      [
        "storage",
        "002a8fb7",
        null,
        "string"
      ]
    ],
    [
      "00bd1748",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1728",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1734",
      "PARAM",
      [
        "storage",
        "002b9c4e",
        null,
        "string"
      ]
    ],
    [
      "00bd1748",
      "WRITE",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62218.md#insn-00b62240) · [`00b62248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62218.md#insn-00b62248) · [`00b62224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62218.md#insn-00b62224)
- 新版 `00bd1740`（命令位置の公開資料なし） · `00bd1748`（命令位置の公開資料なし） · `00bd1724`（命令位置の公開資料なし）

~~~diff
- 00b62240 ["INT_ADD", "register:40f0:8", ["const:b62240:8", "const:4:8"]]
- 00b62240 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1740 ["INT_ADD", "register:40f0:8", ["const:bd1740:8", "const:4:8"]]
+ 00bd1740 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62240 bytes 94ef0194
+ 00bd1740 bytes f4240294
- 00b62248 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b62248 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1748 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:528:8"]]
+ 00bd1748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62248 bytes 601203f9
+ 00bd1748 bytes 609602f9
- 00b62224 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd1724 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b62224 bytes f32900f0
+ 00bd1724 bytes b32a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6181a55f70d6551e0eaf016017432f87"></a>

### [`00b62344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62344.md) → [`00bd1844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1844.md) _ZN8firebase4auth29invalid_credentials_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62384"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1884"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62360"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62358",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62360",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1888"
      ]
    ],
    [
      "unmatched:00b62368",
      "PARAM",
      [
        "storage",
        "002a8fb7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd1858",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1860",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1888"
      ]
    ],
    [
      "00bd1868",
      "PARAM",
      [
        "storage",
        "002b9c4e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62344.md#insn-00b62360) · [`00b6237c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62344.md#insn-00b6237c) · [`00b62384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62344.md#insn-00b62384)
- 新版 `00bd187c`（命令位置の公開資料なし）

~~~diff
- 00b62360 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b62360 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b62360 bytes 410100b5
- 00b6237c ["INT_ADD", "register:40f0:8", ["const:b6237c:8", "const:4:8"]]
- 00b6237c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd187c ["INT_ADD", "register:40f0:8", ["const:bd187c:8", "const:4:8"]]
+ 00bd187c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6237c bytes 45ef0194
+ 00bd187c bytes a5240294
- 00b62384 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
- 00b62384 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62384 bytes 801203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eafbd7356ac15adf53672b15e1507a8b"></a>

### [`00b623b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623b4.md) → [`00bd18b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd18b4.md) _ZN8firebase4auth29invalid_credentials_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bd18d0",
      "incomplete_value": false,
      "site": "00bd18d4",
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
    "old": {
      "definition_site": "00b623d0",
      "incomplete_value": false,
      "site": "00b623d4",
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
            "const:547:8"
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
      "definition_site": "00bd18e0",
      "incomplete_value": true,
      "site": "00bd18ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b623e0",
      "incomplete_value": true,
      "site": "00b623ec",
      "value": [
        "LOAD",
        "8",
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
      "00bd18d0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd18e0",
      "DATA",
      [
        "storage",
        "010a1630",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd18d0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd18e0",
      "DATA",
      [
        "storage",
        "01126538",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b623d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623b4.md#insn-00b623d4) · [`00b623cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623b4.md#insn-00b623cc) · [`00b623d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623b4.md#insn-00b623d0)
- 新版 `00bd18d4`（命令位置の公開資料なし） · `00bd18cc`（命令位置の公開資料なし） · `00bd18d0`（命令位置の公開資料なし）

~~~diff
- 00b623d4 ["INT_ADD", "register:40f0:8", ["const:b623d4:8", "const:4:8"]]
- 00b623d4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd18d4 ["INT_ADD", "register:40f0:8", ["const:bd18d4:8", "const:4:8"]]
+ 00bd18d4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b623d4 bytes 6bef0194
+ 00bd18d4 bytes cb240294
- 00b623cc ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd18cc ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b623cc bytes a0b9ffd0
+ 00bd18cc bytes a0b6fff0
- 00b623d0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b623d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b623d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b623d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd18d0 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd18d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd18d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd18d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b623d0 bytes 001c1591
+ 00bd18d0 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc1540c75fb2465294795b3294b7ea75"></a>

### [`00b623f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623f0.md) → [`00bd18f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd18f0.md) _ZN8firebase4auth29invalid_credentials_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b62430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1930"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6240c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b62404",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6240c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1934"
      ]
    ],
    [
      "unmatched:00b62414",
      "PARAM",
      [
        "storage",
        "002a8fb7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd1904",
      "READ",
      [
        "storage",
        "01126528",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd190c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1934"
      ]
    ],
    [
      "00bd1914",
      "PARAM",
      [
        "storage",
        "002b9c4e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6240c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623f0.md#insn-00b6240c) · [`00b62428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623f0.md#insn-00b62428) · [`00b62430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b623f0.md#insn-00b62430)
- 新版 `00bd1928`（命令位置の公開資料なし）

~~~diff
- 00b6240c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6240c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6240c bytes 410100b5
- 00b62428 ["INT_ADD", "register:40f0:8", ["const:b62428:8", "const:4:8"]]
- 00b62428 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1928 ["INT_ADD", "register:40f0:8", ["const:bd1928:8", "const:4:8"]]
+ 00bd1928 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62428 bytes 1aef0194
+ 00bd1928 bytes 7a240294
- 00b62430 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
- 00b62430 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62430 bytes 801203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e60ada889bb7cdb22b3575de062581a"></a>

### [`00b6249c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6249c.md) → [`00bd199c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd199c.md) _ZN8firebase4auth22invalid_user_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd19c8",
      "incomplete_value": true,
      "site": "00bd19c8",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b624c8",
      "incomplete_value": true,
      "site": "00b624c8",
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
            "const:640:8"
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
      "definition_site": "00bd19b0",
      "incomplete_value": true,
      "site": "00bd19b0",
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
      "definition_site": "00b624b0",
      "incomplete_value": true,
      "site": "00b624b0",
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
      "definition_site": "00bd19bc",
      "incomplete_value": false,
      "site": "00bd19c0",
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
            "const:bef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b624bc",
      "incomplete_value": false,
      "site": "00b624c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:4df:8"
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
      "00bd19ac",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd19bc",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ],
    [
      "00bd19c8",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd19ac",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd19bc",
      "PARAM",
      [
        "storage",
        "002a1bef",
        null,
        "string"
      ]
    ],
    [
      "00bd19c8",
      "WRITE",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b624c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6249c.md#insn-00b624c0) · [`00b624c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6249c.md#insn-00b624c8) · [`00b624a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6249c.md#insn-00b624a8)
- 新版 `00bd19c0`（命令位置の公開資料なし） · `00bd19c8`（命令位置の公開資料なし） · `00bd19a8`（命令位置の公開資料なし）

~~~diff
- 00b624c0 ["INT_ADD", "register:40f0:8", ["const:b624c0:8", "const:4:8"]]
- 00b624c0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd19c0 ["INT_ADD", "register:40f0:8", ["const:bd19c0:8", "const:4:8"]]
+ 00bd19c0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b624c0 bytes f4ee0194
+ 00bd19c0 bytes 54240294
- 00b624c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b624c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd19c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
+ 00bd19c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b624c8 bytes 602203f9
+ 00bd19c8 bytes 60a602f9
- 00b624a8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd19a8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b624a8 bytes f32900f0
+ 00bd19a8 bytes b32a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a84d0c37854feef9e3cc88e7a6f88a22"></a>

### [`00b624dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b624dc.md) → [`00bd19dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd19dc.md) _ZN8firebase4auth22invalid_user_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd1a08",
      "incomplete_value": true,
      "site": "00bd1a08",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62508",
      "incomplete_value": true,
      "site": "00b62508",
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
            "const:640:8"
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
      "definition_site": "00bd19f0",
      "incomplete_value": true,
      "site": "00bd19f0",
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
      "definition_site": "00b624f0",
      "incomplete_value": true,
      "site": "00b624f0",
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
      "definition_site": "00bd19f8",
      "incomplete_value": false,
      "site": "00bd1a00",
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
            "const:bef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b624f8",
      "incomplete_value": false,
      "site": "00b62500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:4df:8"
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
      "00bd19ec",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd19f8",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ],
    [
      "00bd1a08",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd19ec",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd19f8",
      "PARAM",
      [
        "storage",
        "002a1bef",
        null,
        "string"
      ]
    ],
    [
      "00bd1a08",
      "WRITE",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b624dc.md#insn-00b62500) · [`00b62508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b624dc.md#insn-00b62508) · [`00b624e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b624dc.md#insn-00b624e8)
- 新版 `00bd1a00`（命令位置の公開資料なし） · `00bd1a08`（命令位置の公開資料なし） · `00bd19e8`（命令位置の公開資料なし）

~~~diff
- 00b62500 ["INT_ADD", "register:40f0:8", ["const:b62500:8", "const:4:8"]]
- 00b62500 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1a00 ["INT_ADD", "register:40f0:8", ["const:bd1a00:8", "const:4:8"]]
+ 00bd1a00 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62500 bytes e4ee0194
+ 00bd1a00 bytes 44240294
- 00b62508 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b62508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1a08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:548:8"]]
+ 00bd1a08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62508 bytes 602203f9
+ 00bd1a08 bytes 60a602f9
- 00b624e8 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd19e8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b624e8 bytes f32900f0
+ 00bd19e8 bytes b32a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4423c1492130b39f4d3d752c3db754f2"></a>

### [`00b62560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62560.md) → [`00bd1a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1a60.md) _ZN8firebase4auth22invalid_user_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

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
      "site": "00b62590"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1a90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62574"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bd1a70",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62574",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1a94"
      ]
    ],
    [
      "unmatched:00b6257c",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd1a70",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1a74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1a94"
      ]
    ],
    [
      "00bd1a7c",
      "PARAM",
      [
        "storage",
        "002a1bef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62560.md#insn-00b62574) · [`00b62588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62560.md#insn-00b62588) · [`00b62590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62560.md#insn-00b62590)
- 新版 `00bd1a88`（命令位置の公開資料なし）

~~~diff
- 00b62574 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b62574 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b62574 bytes 080100b5
- 00b62588 ["INT_ADD", "register:40f0:8", ["const:b62588:8", "const:4:8"]]
- 00b62588 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1a88 ["INT_ADD", "register:40f0:8", ["const:bd1a88:8", "const:4:8"]]
+ 00bd1a88 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62588 bytes c2ee0194
+ 00bd1a88 bytes 22240294
- 00b62590 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b62590 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62590 bytes 602203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12e8e93535b5bac2f710070995297f1b"></a>

### [`00b625b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b625b0.md) → [`00bd1ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ab0.md) _ZN8firebase4auth22invalid_user_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd1b08",
      "incomplete_value": true,
      "site": "00bd1b08",
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
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62608",
      "incomplete_value": true,
      "site": "00b62608",
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
            "const:648:8"
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
      "definition_site": "00bd1ae4",
      "incomplete_value": true,
      "site": "00bd1af0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:548:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b625e4",
      "incomplete_value": true,
      "site": "00b625f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:640:8"
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
      "00bd1ac4",
      "READ",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1ae4",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1b08",
      "WRITE",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1ac4",
      "READ",
      [
        "storage",
        "01126550",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1ae4",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1b08",
      "WRITE",
      [
        "storage",
        "01126550",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b625f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b625b0.md#insn-00b625f0) · [`00b62608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b625b0.md#insn-00b62608) · [`00b625c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b625b0.md#insn-00b625c0)
- 新版 `00bd1af0`（命令位置の公開資料なし） · `00bd1b08`（命令位置の公開資料なし） · `00bd1ac0`（命令位置の公開資料なし）

~~~diff
- 00b625f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b625f0 ["INT_ADD", "register:40f0:8", ["const:b625f0:8", "const:4:8"]]
- 00b625f0 ["CALLIND", null, ["register:0:8"]]
+ 00bd1af0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1af0 ["INT_ADD", "register:40f0:8", ["const:bd1af0:8", "const:4:8"]]
+ 00bd1af0 ["CALLIND", null, ["register:0:8"]]
- 00b625f0 bytes 00013fd6
+ 00bd1af0 bytes 00013fd6
- 00b62608 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b62608 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:648:8"]]
- 00b62608 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd1b08 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd1b08 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:550:8"]]
+ 00bd1b08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b62608 bytes a0221939
+ 00bd1b08 bytes a0421539
- 00b625c0 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd1ac0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b625c0 bytes f52900f0
+ 00bd1ac0 bytes b52a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-912bea852c38b13da62dceba063f1856"></a>

### [`00b6261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6261c.md) → [`00bd1b1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1b1c.md) _ZN8firebase4auth22invalid_user_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

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
      "definition_site": "00bd1b58",
      "incomplete_value": true,
      "site": "00bd1b58",
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
            "const:550:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62658",
      "incomplete_value": true,
      "site": "00b62658",
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
            "const:648:8"
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
      "definition_site": "00bd1b78",
      "incomplete_value": true,
      "site": "00bd1b78",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62678",
      "incomplete_value": true,
      "site": "00b62678",
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
            "const:640:8"
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
      "definition_site": "00bd1b34",
      "incomplete_value": true,
      "site": "00bd1b34",
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
      "definition_site": "00b62634",
      "incomplete_value": true,
      "site": "00b62634",
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
      "00bd1b30",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1b3c",
      "READ",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1b58",
      "WRITE",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1b30",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1b3c",
      "READ",
      [
        "storage",
        "01126550",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1b58",
      "WRITE",
      [
        "storage",
        "01126550",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6261c.md#insn-00b62658) · [`00b62674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6261c.md#insn-00b62674) · [`00b62678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6261c.md#insn-00b62678)
- 新版 `00bd1b58`（命令位置の公開資料なし） · `00bd1b74`（命令位置の公開資料なし） · `00bd1b78`（命令位置の公開資料なし）

~~~diff
- 00b62658 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b62658 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b62658 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:648:8"]]
- 00b62658 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd1b58 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd1b58 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd1b58 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:550:8"]]
+ 00bd1b58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b62658 bytes bf221939
+ 00bd1b58 bytes bf421539
- 00b62674 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62674 ["INT_ADD", "register:40f0:8", ["const:b62674:8", "const:4:8"]]
- 00b62674 ["CALLIND", null, ["register:0:8"]]
+ 00bd1b74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1b74 ["INT_ADD", "register:40f0:8", ["const:bd1b74:8", "const:4:8"]]
+ 00bd1b74 ["CALLIND", null, ["register:0:8"]]
- 00b62674 bytes 00013fd6
+ 00bd1b74 bytes 00013fd6
- 00b62678 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b62678 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b62678 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd1b78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:548:8"]]
+ 00bd1b78 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd1b78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b62678 bytes 9f2203f9
+ 00bd1b78 bytes 9fa602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81d16cd79910b8aebb7009728b2420d4"></a>

### [`00b6268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6268c.md) → [`00bd1b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1b8c.md) _ZN8firebase4auth22invalid_user_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6268c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6268c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62690"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6268c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b62690",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b626a0",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1b8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bd1b90",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bd1ba0",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6268c.md#insn-00b6268c) · [`00b62690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6268c.md#insn-00b62690) · [`00b626a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b6268c.md#insn-00b626a8)

~~~diff
- 00b6268c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6268c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6268c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6268c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6268c bytes f44fbea9
- 00b62690 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b62690 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b62690 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b62690 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b62690 bytes fd7b01a9
- 00b626a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b626a8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b626a8 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ab8dcbfb29b977af491d5ea1b8dca8d"></a>

### [`00b626fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b626fc.md) → [`00bd1bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1bfc.md) _ZN8firebase4auth22invalid_user_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bd1c18",
      "incomplete_value": false,
      "site": "00bd1c1c",
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
    "old": {
      "definition_site": "00b62718",
      "incomplete_value": false,
      "site": "00b6271c",
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
            "const:547:8"
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
      "definition_site": "00bd1c28",
      "incomplete_value": true,
      "site": "00bd1c34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62728",
      "incomplete_value": true,
      "site": "00b62734",
      "value": [
        "LOAD",
        "8",
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
      "00bd1c18",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd1c28",
      "DATA",
      [
        "storage",
        "010a1650",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd1c18",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd1c28",
      "DATA",
      [
        "storage",
        "01126558",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6271c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b626fc.md#insn-00b6271c) · [`00b62714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b626fc.md#insn-00b62714) · [`00b62718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b626fc.md#insn-00b62718)
- 新版 `00bd1c1c`（命令位置の公開資料なし） · `00bd1c14`（命令位置の公開資料なし） · `00bd1c18`（命令位置の公開資料なし）

~~~diff
- 00b6271c ["INT_ADD", "register:40f0:8", ["const:b6271c:8", "const:4:8"]]
- 00b6271c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd1c1c ["INT_ADD", "register:40f0:8", ["const:bd1c1c:8", "const:4:8"]]
+ 00bd1c1c ["CALL", null, ["callee:00c5ac00:8"]]
- 00b6271c bytes 99ee0194
+ 00bd1c1c bytes f9230294
- 00b62714 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd1c14 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b62714 bytes a0b9ffd0
+ 00bd1c14 bytes a0b6fff0
- 00b62718 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b62718 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62718 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62718 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd1c18 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd1c18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1c18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1c18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62718 bytes 001c1591
+ 00bd1c18 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c52afe1009364af39a8bea14f6fcef0"></a>

### [`00b62738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62738.md) → [`00bd1c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1c38.md) _ZN8firebase4auth22invalid_user_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b62778"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1c78"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62754"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6274c",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62754",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1c7c"
      ]
    ],
    [
      "unmatched:00b6275c",
      "PARAM",
      [
        "storage",
        "002924df",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd1c4c",
      "READ",
      [
        "storage",
        "01126548",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1c54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1c7c"
      ]
    ],
    [
      "00bd1c5c",
      "PARAM",
      [
        "storage",
        "002a1bef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62738.md#insn-00b62754) · [`00b62770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62738.md#insn-00b62770) · [`00b62778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62738.md#insn-00b62778)
- 新版 `00bd1c70`（命令位置の公開資料なし）

~~~diff
- 00b62754 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b62754 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b62754 bytes 410100b5
- 00b62770 ["INT_ADD", "register:40f0:8", ["const:b62770:8", "const:4:8"]]
- 00b62770 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1c70 ["INT_ADD", "register:40f0:8", ["const:bd1c70:8", "const:4:8"]]
+ 00bd1c70 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62770 bytes 48ee0194
+ 00bd1c70 bytes a8230294
- 00b62778 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b62778 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62778 bytes 802203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b19d5b89482cb424f10625ec2ec84829"></a>

### [`00b627e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627e4.md) → [`00bd1ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ce4.md) _ZN8firebase4auth31recent_login_required_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "site": "00b62810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bd1d10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bd1cf8",
      "incomplete_value": true,
      "site": "00bd1cf8",
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
      "definition_site": "00b627f8",
      "incomplete_value": true,
      "site": "00b627f8",
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
      "00bd1cf4",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1cf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b62814"
      ]
    ],
    [
      "unmatched:00b62804",
      "PARAM",
      [
        "storage",
        "002ab1dd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd1cf4",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1cf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1d14"
      ]
    ],
    [
      "00bd1d04",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627e4.md#insn-00b62808) · [`00b62810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627e4.md#insn-00b62810) · [`00b62820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b627e4.md#insn-00b62820)

~~~diff
- 00b62808 ["INT_ADD", "register:40f0:8", ["const:b62808:8", "const:4:8"]]
- 00b62808 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62808 bytes 22ee0194
- 00b62810 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b62810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62810 bytes 603203f9
- 00b62820 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b62820 ["RETURN", null, ["register:0:8"]]
- 00b62820 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edb5f47d9b525b531b80a8d5b66c7138"></a>

### [`00b62824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62824.md) → [`00bd1d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1d24.md) _ZN8firebase4auth31recent_login_required_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd1d50",
      "incomplete_value": true,
      "site": "00bd1d50",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62850",
      "incomplete_value": true,
      "site": "00b62850",
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
            "const:660:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b62838"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bd1d38"
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
      "unmatched:00b62834",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b62838",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1d54"
      ]
    ],
    [
      "00bd1d40",
      "PARAM",
      [
        "storage",
        "002ab1dd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bd1d34",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1d38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bd1d54"
      ]
    ],
    [
      "00bd1d40",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62824.md#insn-00b62838) · [`00b62848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62824.md#insn-00b62848) · [`00b62850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62824.md#insn-00b62850)
- 新版 `00bd1d48`（命令位置の公開資料なし） · `00bd1d50`（命令位置の公開資料なし）

~~~diff
- 00b62838 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b62838 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b62838 bytes e80000b5
- 00b62848 ["INT_ADD", "register:40f0:8", ["const:b62848:8", "const:4:8"]]
- 00b62848 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1d48 ["INT_ADD", "register:40f0:8", ["const:bd1d48:8", "const:4:8"]]
+ 00bd1d48 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62848 bytes 12ee0194
+ 00bd1d48 bytes 72230294
- 00b62850 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b62850 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1d50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
+ 00bd1d50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62850 bytes 603203f9
+ 00bd1d50 bytes 60b602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7193493435d93b8c54c955554b1f0e8e"></a>

### [`00b62864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62864.md) → [`00bd1d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1d64.md) _ZN8firebase4auth31recent_login_required_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd1d94",
      "incomplete_value": true,
      "site": "00bd1d94",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62894",
      "incomplete_value": true,
      "site": "00b62894",
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
            "const:660:8"
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
      "definition_site": "00bd1d78",
      "incomplete_value": true,
      "site": "00bd1d78",
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
      "definition_site": "00b62878",
      "incomplete_value": true,
      "site": "00b62878",
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
      "definition_site": "00bd1d84",
      "incomplete_value": false,
      "site": "00bd1d8c",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62884",
      "incomplete_value": false,
      "site": "00b6288c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:1dd:8"
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
      "00bd1d74",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1d84",
      "PARAM",
      [
        "storage",
        "002ab1dd",
        null,
        "string"
      ]
    ],
    [
      "00bd1d94",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1d74",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1d84",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ],
    [
      "00bd1d94",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6288c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62864.md#insn-00b6288c) · [`00b62894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62864.md#insn-00b62894) · [`00b62870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62864.md#insn-00b62870)
- 新版 `00bd1d8c`（命令位置の公開資料なし） · `00bd1d94`（命令位置の公開資料なし） · `00bd1d70`（命令位置の公開資料なし）

~~~diff
- 00b6288c ["INT_ADD", "register:40f0:8", ["const:b6288c:8", "const:4:8"]]
- 00b6288c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1d8c ["INT_ADD", "register:40f0:8", ["const:bd1d8c:8", "const:4:8"]]
+ 00bd1d8c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b6288c bytes 01ee0194
+ 00bd1d8c bytes 61230294
- 00b62894 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b62894 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1d94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
+ 00bd1d94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62894 bytes 603203f9
+ 00bd1d94 bytes 60b602f9
- 00b62870 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd1d70 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b62870 bytes f32900f0
+ 00bd1d70 bytes b32a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f37ed3cba0bf87d3462a162fe1ea4c2"></a>

### [`00b628a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628a8.md) → [`00bd1da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1da8.md) _ZN8firebase4auth31recent_login_required_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd1dd8",
      "incomplete_value": true,
      "site": "00bd1dd8",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b628d8",
      "incomplete_value": true,
      "site": "00b628d8",
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
            "const:660:8"
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
      "definition_site": "00bd1dbc",
      "incomplete_value": true,
      "site": "00bd1dbc",
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
      "definition_site": "00b628bc",
      "incomplete_value": true,
      "site": "00b628bc",
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
      "definition_site": "00bd1dc4",
      "incomplete_value": false,
      "site": "00bd1dd0",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b628c4",
      "incomplete_value": false,
      "site": "00b628d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:1dd:8"
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
      "00bd1db8",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1dc4",
      "PARAM",
      [
        "storage",
        "002ab1dd",
        null,
        "string"
      ]
    ],
    [
      "00bd1dd8",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1db8",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1dc4",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ],
    [
      "00bd1dd8",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b628d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628a8.md#insn-00b628d0) · [`00b628d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628a8.md#insn-00b628d8) · [`00b628b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628a8.md#insn-00b628b4)
- 新版 `00bd1dd0`（命令位置の公開資料なし） · `00bd1dd8`（命令位置の公開資料なし） · `00bd1db4`（命令位置の公開資料なし）

~~~diff
- 00b628d0 ["INT_ADD", "register:40f0:8", ["const:b628d0:8", "const:4:8"]]
- 00b628d0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1dd0 ["INT_ADD", "register:40f0:8", ["const:bd1dd0:8", "const:4:8"]]
+ 00bd1dd0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b628d0 bytes f0ed0194
+ 00bd1dd0 bytes 50230294
- 00b628d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b628d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1dd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:568:8"]]
+ 00bd1dd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b628d8 bytes 603203f9
+ 00bd1dd8 bytes 60b602f9
- 00b628b4 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd1db4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b628b4 bytes f32900f0
+ 00bd1db4 bytes b32a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b495a0339583b07d5b5dbddd651b6169"></a>

### [`00b628f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628f8.md) → [`00bd1df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1df8.md) _ZN8firebase4auth31recent_login_required_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bd1e50",
      "incomplete_value": true,
      "site": "00bd1e50",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62950",
      "incomplete_value": true,
      "site": "00b62950",
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
            "const:668:8"
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
      "definition_site": "00bd1e2c",
      "incomplete_value": true,
      "site": "00bd1e38",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
    "old": {
      "definition_site": "00b6292c",
      "incomplete_value": true,
      "site": "00b62938",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:660:8"
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
      "00bd1e0c",
      "READ",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1e2c",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1e50",
      "WRITE",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1e0c",
      "READ",
      [
        "storage",
        "01126570",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1e2c",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1e50",
      "WRITE",
      [
        "storage",
        "01126570",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628f8.md#insn-00b62938) · [`00b62950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628f8.md#insn-00b62950) · [`00b62908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b628f8.md#insn-00b62908)
- 新版 `00bd1e38`（命令位置の公開資料なし） · `00bd1e50`（命令位置の公開資料なし） · `00bd1e08`（命令位置の公開資料なし）

~~~diff
- 00b62938 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b62938 ["INT_ADD", "register:40f0:8", ["const:b62938:8", "const:4:8"]]
- 00b62938 ["CALLIND", null, ["register:0:8"]]
+ 00bd1e38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1e38 ["INT_ADD", "register:40f0:8", ["const:bd1e38:8", "const:4:8"]]
+ 00bd1e38 ["CALLIND", null, ["register:0:8"]]
- 00b62938 bytes 00013fd6
+ 00bd1e38 bytes 00013fd6
- 00b62950 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b62950 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:668:8"]]
- 00b62950 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bd1e50 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00bd1e50 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:570:8"]]
+ 00bd1e50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b62950 bytes a0a21939
+ 00bd1e50 bytes a0c21539
- 00b62908 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
+ 00bd1e08 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b62908 bytes f52900f0
+ 00bd1e08 bytes b52a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aba59a252803239648976513aa59bcf6"></a>

### [`00b62964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62964.md) → [`00bd1e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1e64.md) _ZN8firebase4auth31recent_login_required_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

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
      "definition_site": "00bd1ea0",
      "incomplete_value": true,
      "site": "00bd1ea0",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b629a0",
      "incomplete_value": true,
      "site": "00b629a0",
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
            "const:668:8"
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
      "definition_site": "00bd1ec0",
      "incomplete_value": true,
      "site": "00bd1ec0",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b629c0",
      "incomplete_value": true,
      "site": "00b629c0",
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
            "const:660:8"
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
      "definition_site": "00bd1e7c",
      "incomplete_value": true,
      "site": "00bd1e7c",
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
      "definition_site": "00b6297c",
      "incomplete_value": true,
      "site": "00b6297c",
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
      "00bd1e78",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1e84",
      "READ",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1ea0",
      "WRITE",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bd1e78",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1e84",
      "READ",
      [
        "storage",
        "01126570",
        null,
        "undefined1"
      ]
    ],
    [
      "00bd1ea0",
      "WRITE",
      [
        "storage",
        "01126570",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b629a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62964.md#insn-00b629a0) · [`00b629bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62964.md#insn-00b629bc) · [`00b629c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62964.md#insn-00b629c0)
- 新版 `00bd1ea0`（命令位置の公開資料なし） · `00bd1ebc`（命令位置の公開資料なし） · `00bd1ec0`（命令位置の公開資料なし）

~~~diff
- 00b629a0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b629a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b629a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:668:8"]]
- 00b629a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00bd1ea0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00bd1ea0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00bd1ea0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:570:8"]]
+ 00bd1ea0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b629a0 bytes bfa21939
+ 00bd1ea0 bytes bfc21539
- 00b629bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b629bc ["INT_ADD", "register:40f0:8", ["const:b629bc:8", "const:4:8"]]
- 00b629bc ["CALLIND", null, ["register:0:8"]]
+ 00bd1ebc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bd1ebc ["INT_ADD", "register:40f0:8", ["const:bd1ebc:8", "const:4:8"]]
+ 00bd1ebc ["CALLIND", null, ["register:0:8"]]
- 00b629bc bytes 00013fd6
+ 00bd1ebc bytes 00013fd6
- 00b629c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b629c0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b629c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00bd1ec0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:568:8"]]
+ 00bd1ec0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00bd1ec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b629c0 bytes 9f3203f9
+ 00bd1ec0 bytes 9fb602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9287232757cb741c408fa6db3a149c9"></a>

### [`00b629d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b629d4.md) → [`00bd1ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ed4.md) _ZN8firebase4auth31recent_login_required_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "definition_site": "00bd1f14",
      "incomplete_value": true,
      "site": "00bd1f14",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62a14",
      "incomplete_value": true,
      "site": "00b62a14",
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
            "const:660:8"
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
      "definition_site": "00bd1ef0",
      "incomplete_value": true,
      "site": "00bd1ef0",
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
      "definition_site": "00b629f0",
      "incomplete_value": true,
      "site": "00b629f0",
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
      "definition_site": "00bd1ef8",
      "incomplete_value": false,
      "site": "00bd1f0c",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b629f8",
      "incomplete_value": false,
      "site": "00b62a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:1dd:8"
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
      "00bd1ee8",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1ef8",
      "PARAM",
      [
        "storage",
        "002ab1dd",
        null,
        "string"
      ]
    ],
    [
      "00bd1f14",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1ee8",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1ef8",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ],
    [
      "00bd1f14",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b629d4.md#insn-00b62a0c) · [`00b62a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b629d4.md#insn-00b62a14) · [`00b629e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b629d4.md#insn-00b629e0)
- 新版 `00bd1f0c`（命令位置の公開資料なし） · `00bd1f14`（命令位置の公開資料なし） · `00bd1ee0`（命令位置の公開資料なし）

~~~diff
- 00b62a0c ["INT_ADD", "register:40f0:8", ["const:b62a0c:8", "const:4:8"]]
- 00b62a0c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1f0c ["INT_ADD", "register:40f0:8", ["const:bd1f0c:8", "const:4:8"]]
+ 00bd1f0c ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62a0c bytes a1ed0194
+ 00bd1f0c bytes 01230294
- 00b62a14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b62a14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1f14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:568:8"]]
+ 00bd1f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62a14 bytes 803203f9
+ 00bd1f14 bytes 80b602f9
- 00b629e0 ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd1ee0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b629e0 bytes f42900f0
+ 00bd1ee0 bytes b42a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c101b1a2c37f78fae5d4f11a9ee2f099"></a>

### [`00b62a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a44.md) → [`00bd1f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1f44.md) _ZN8firebase4auth31recent_login_required_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bd1f60",
      "incomplete_value": false,
      "site": "00bd1f64",
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
    "old": {
      "definition_site": "00b62a60",
      "incomplete_value": false,
      "site": "00b62a64",
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
            "const:547:8"
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
      "definition_site": "00bd1f70",
      "incomplete_value": true,
      "site": "00bd1f7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62a70",
      "incomplete_value": true,
      "site": "00b62a7c",
      "value": [
        "LOAD",
        "8",
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
      "00bd1f60",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00bd1f70",
      "DATA",
      [
        "storage",
        "010a1670",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd1f60",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00bd1f70",
      "DATA",
      [
        "storage",
        "01126578",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a44.md#insn-00b62a64) · [`00b62a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a44.md#insn-00b62a5c) · [`00b62a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a44.md#insn-00b62a60)
- 新版 `00bd1f64`（命令位置の公開資料なし） · `00bd1f5c`（命令位置の公開資料なし） · `00bd1f60`（命令位置の公開資料なし）

~~~diff
- 00b62a64 ["INT_ADD", "register:40f0:8", ["const:b62a64:8", "const:4:8"]]
- 00b62a64 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd1f64 ["INT_ADD", "register:40f0:8", ["const:bd1f64:8", "const:4:8"]]
+ 00bd1f64 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b62a64 bytes c7ed0194
+ 00bd1f64 bytes 27230294
- 00b62a5c ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00bd1f5c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00b62a5c bytes a0b9ffd0
+ 00bd1f5c bytes a0b6fff0
- 00b62a60 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b62a60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62a60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62a60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd1f60 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00bd1f60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1f60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd1f60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62a60 bytes 001c1591
+ 00bd1f60 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a08a5f1c0660eb482104cdc73a41f931"></a>

### [`00b62a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a80.md) → [`00bd1f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1f80.md) _ZN8firebase4auth31recent_login_required_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5aaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5aaf0.md) [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd1fc0",
      "incomplete_value": true,
      "site": "00bd1fc0",
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
            "const:568:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62ac0",
      "incomplete_value": true,
      "site": "00b62ac0",
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
            "const:660:8"
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
      "definition_site": "00bd1f9c",
      "incomplete_value": true,
      "site": "00bd1f9c",
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
      "definition_site": "00b62a9c",
      "incomplete_value": true,
      "site": "00b62a9c",
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
      "definition_site": "00bd1fa4",
      "incomplete_value": false,
      "site": "00bd1fb8",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62aa4",
      "incomplete_value": false,
      "site": "00b62ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ab000:8"
          ],
          [
            "leaf",
            "const:1dd:8"
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
      "00bd1f94",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1fa4",
      "PARAM",
      [
        "storage",
        "002ab1dd",
        null,
        "string"
      ]
    ],
    [
      "00bd1fc0",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd1f94",
      "READ",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd1fa4",
      "PARAM",
      [
        "storage",
        "002bc100",
        null,
        "string"
      ]
    ],
    [
      "00bd1fc0",
      "WRITE",
      [
        "storage",
        "01126568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a80.md#insn-00b62ab8) · [`00b62ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a80.md#insn-00b62ac0) · [`00b62a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62a80.md#insn-00b62a8c)
- 新版 `00bd1fb8`（命令位置の公開資料なし） · `00bd1fc0`（命令位置の公開資料なし） · `00bd1f8c`（命令位置の公開資料なし）

~~~diff
- 00b62ab8 ["INT_ADD", "register:40f0:8", ["const:b62ab8:8", "const:4:8"]]
- 00b62ab8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd1fb8 ["INT_ADD", "register:40f0:8", ["const:bd1fb8:8", "const:4:8"]]
+ 00bd1fb8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62ab8 bytes 76ed0194
+ 00bd1fb8 bytes d6220294
- 00b62ac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b62ac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd1fc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:568:8"]]
+ 00bd1fc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62ac0 bytes 803203f9
+ 00bd1fc0 bytes 80b602f9
- 00b62a8c ["COPY", "register:40a0:8", ["const:10a1000:8"]]
+ 00bd1f8c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b62a8c bytes f42900f0
+ 00bd1f8c bytes b42a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbe6746e38c97354648a38c450af45ec"></a>

### [`00b62af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62af0.md) → [`00bd1ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd1ff0.md) _ZN8firebase4auth31recent_login_required_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00bd200c",
      "incomplete_value": false,
      "site": "00bd2010",
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
    "old": {
      "definition_site": "00b62b0c",
      "incomplete_value": false,
      "site": "00b62b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:5f2:8"
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
      "definition_site": "00bd201c",
      "incomplete_value": true,
      "site": "00bd2028",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b62b1c",
      "incomplete_value": true,
      "site": "00b62b28",
      "value": [
        "LOAD",
        "8",
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
      "00bd200c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00bd201c",
      "DATA",
      [
        "storage",
        "010a1678",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bd200c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00bd201c",
      "DATA",
      [
        "storage",
        "01126580",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62af0.md#insn-00b62b10) · [`00b62b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62af0.md#insn-00b62b08) · [`00b62b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62af0.md#insn-00b62b0c)
- 新版 `00bd2010`（命令位置の公開資料なし） · `00bd2008`（命令位置の公開資料なし） · `00bd200c`（命令位置の公開資料なし）

~~~diff
- 00b62b10 ["INT_ADD", "register:40f0:8", ["const:b62b10:8", "const:4:8"]]
- 00b62b10 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00bd2010 ["INT_ADD", "register:40f0:8", ["const:bd2010:8", "const:4:8"]]
+ 00bd2010 ["CALL", null, ["callee:00c5ac00:8"]]
- 00b62b10 bytes 9ced0194
+ 00bd2010 bytes fc220294
- 00b62b08 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00bd2008 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00b62b08 bytes a0b9fff0
+ 00bd2008 bytes a0b6fff0
- 00b62b0c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b62b0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b62b0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b62b0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bd200c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00bd200c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd200c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bd200c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b62b0c bytes 00c81791
+ 00bd200c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8322282a3e2b18bed356c5dcf3a6d36e"></a>

### [`00b62b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b2c.md) → [`00bd202c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd2/00bd202c.md) _ZN8firebase4auth24user_collision_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allo

採用 · 移動量 `+0x6f500` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

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
      "definition_site": "00bd2058",
      "incomplete_value": true,
      "site": "00bd2058",
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
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62b58",
      "incomplete_value": true,
      "site": "00b62b58",
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
            "const:680:8"
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
      "definition_site": "00bd2040",
      "incomplete_value": true,
      "site": "00bd2040",
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
      "definition_site": "00b62b40",
      "incomplete_value": true,
      "site": "00b62b40",
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
      "definition_site": "00bd204c",
      "incomplete_value": false,
      "site": "00bd2050",
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
            "const:c2a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b62b4c",
      "incomplete_value": false,
      "site": "00b62b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:443:8"
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
      "00bd203c",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd204c",
      "PARAM",
      [
        "storage",
        "00293443",
        null,
        "string"
      ]
    ],
    [
      "00bd2058",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bd203c",
      "READ",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ],
    [
      "00bd204c",
      "PARAM",
      [
        "storage",
        "002a2c2a",
        null,
        "string"
      ]
    ],
    [
      "00bd2058",
      "WRITE",
      [
        "storage",
        "01126588",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b62b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b2c.md#insn-00b62b50) · [`00b62b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b2c.md#insn-00b62b58) · [`00b62b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b62/00b62b2c.md#insn-00b62b38)
- 新版 `00bd2050`（命令位置の公開資料なし） · `00bd2058`（命令位置の公開資料なし） · `00bd2038`（命令位置の公開資料なし）

~~~diff
- 00b62b50 ["INT_ADD", "register:40f0:8", ["const:b62b50:8", "const:4:8"]]
- 00b62b50 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00bd2050 ["INT_ADD", "register:40f0:8", ["const:bd2050:8", "const:4:8"]]
+ 00bd2050 ["CALL", null, ["callee:00c5ab10:8"]]
- 00b62b50 bytes 50ed0194
+ 00bd2050 bytes b0220294
- 00b62b58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b62b58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bd2058 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:588:8"]]
+ 00bd2058 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b62b58 bytes 604203f9
+ 00bd2058 bytes 60c602f9
- 00b62b38 ["COPY", "register:4098:8", ["const:10a1000:8"]]
+ 00bd2038 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b62b38 bytes f32900f0
+ 00bd2038 bytes b32a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

