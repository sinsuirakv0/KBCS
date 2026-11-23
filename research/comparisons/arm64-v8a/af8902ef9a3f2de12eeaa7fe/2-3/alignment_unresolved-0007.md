# v16.0.0 → v16.0.1 · 命令位置の検査未完了 (7)

[一覧の目次](README.md)

<a id="compare-22c454129fb5b820dd0b4ff366de1223"></a>

### [`00afc6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc6b8.md) → [`00afcae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcae0.md) FUN_00afcae0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc6f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afcb20"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc708"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc6fc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc700",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc704",
      "DATA",
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
      "00afcb24",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afcb28",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afcb2c",
      "DATA",
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

- 旧版 [`00afc6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc6b8.md#insn-00afc6f8) · [`00afc708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc6b8.md#insn-00afc708)
- 新版 `00afcb20`（命令位置の公開資料なし）

~~~diff
- 00afc6f8 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00afc6f8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00afc6f8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00afc6f8 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00afc6f8 bytes 0a6929b8
- 00afc708 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afc708 ["RETURN", null, ["register:0:8"]]
- 00afc708 bytes c0035fd6
+ 00afcb20 ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 00afcb20 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00afcb20 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00afcb20 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00afcb20 bytes 0a6929b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b531c92a87eac3a58cafeedd713186a"></a>

### [`00afc74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc74c.md) → [`00afcb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcb74.md) FUN_00afcb74

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.89% / 新版 57.89%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc784"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afcbac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc794"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc788",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc78c",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc790",
      "DATA",
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
      "00afcbb0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afcbb4",
      "READ",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afcbb8",
      "DATA",
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

- 旧版 [`00afc784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc74c.md#insn-00afc784) · [`00afc794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc74c.md#insn-00afc794)
- 新版 `00afcbac`（命令位置の公開資料なし）

~~~diff
- 00afc784 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00afc784 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00afc784 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00afc784 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00afc784 bytes 136929b8
- 00afc794 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afc794 ["RETURN", null, ["register:0:8"]]
- 00afc794 bytes c0035fd6
+ 00afcbac ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00afcbac ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00afcbac ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00afcbac ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00afcbac bytes 136929b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8acf62e109fe63ce3b8625a7e7f514e"></a>

### [`00afc798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc798.md) → [`00afcbc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcbc0.md) FUN_00afcbc0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc7e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00afcc10"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afc7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc798.md#insn-00afc7e8) · [`00afc7b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc798.md#insn-00afc7b4)
- 新版 `00afcc10`（命令位置の公開資料なし） · `00afcbdc`（命令位置の公開資料なし）

~~~diff
- 00afc7e8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afc7e8 ["RETURN", null, ["register:0:8"]]
- 00afc7e8 bytes c0035fd6
+ 00afcc10 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00afcc10 ["RETURN", null, ["register:0:8"]]
+ 00afcc10 bytes c0035fd6
- 00afc7b4 ["INT_ADD", "register:40f0:8", ["const:afc7b4:8", "const:4:8"]]
- 00afc7b4 ["CALL", null, ["callee:008514f8:8"]]
+ 00afcbdc ["INT_ADD", "register:40f0:8", ["const:afcbdc:8", "const:4:8"]]
+ 00afcbdc ["CALL", null, ["callee:008514f8:8"]]
- 00afc7b4 bytes 4153f597
+ 00afcbdc bytes 4752f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c4572596ae1ec846f516cbc944ae2ac"></a>

### [`00afc7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc7ec.md) → [`00afcc14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcc14.md) FUN_00afcc14

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005f2d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2d28.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`005f2d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2d68.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc828"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00afcc50"
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
      "unmatched:00afc820",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc824",
      "DATA",
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
      "00afcc48",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afcc4c",
      "DATA",
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

- 旧版 [`00afc828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc7ec.md#insn-00afc828) · [`00afc800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc7ec.md#insn-00afc800)
- 新版 `00afcc50`（命令位置の公開資料なし） · `00afcc28`（命令位置の公開資料なし）

~~~diff
- 00afc828 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afc828 ["RETURN", null, ["register:0:8"]]
- 00afc828 bytes c0035fd6
+ 00afcc50 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00afcc50 ["RETURN", null, ["register:0:8"]]
+ 00afcc50 bytes c0035fd6
- 00afc800 ["INT_ADD", "register:40f0:8", ["const:afc800:8", "const:4:8"]]
- 00afc800 ["CALL", null, ["callee:008514f8:8"]]
+ 00afcc28 ["INT_ADD", "register:40f0:8", ["const:afcc28:8", "const:4:8"]]
+ 00afcc28 ["CALL", null, ["callee:008514f8:8"]]
- 00afc800 bytes 2e53f597
+ 00afcc28 bytes 3452f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9109e99acee867b39313e130df521c08"></a>

### [`00afc82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc82c.md) → [`00afcc54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcc54.md) FUN_00afcc54

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 36.84% / 新版 36.84%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc82c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc82c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc830"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afc82c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc830",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afc834",
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
      "00afcc54",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afcc58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afcc5c",
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

- 旧版 [`00afc82c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc82c.md#insn-00afc82c) · [`00afc830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc82c.md#insn-00afc830) · [`00afc834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc82c.md#insn-00afc834)

~~~diff
- 00afc82c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afc82c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afc82c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afc82c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afc82c bytes fd7bbda9
- 00afc830 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00afc830 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afc830 bytes f50b00f9
- 00afc834 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afc834 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afc834 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afc834 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afc834 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e28121241c599fda57140b7cf20b127"></a>

### [`00afc8cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc8cc.md) → [`00afccf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afccf4.md) FUN_00afccf4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afc8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc8cc.md#insn-00afc8e0) · [`00afc8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc8cc.md#insn-00afc8fc)
- 新版 `00afcd08`（命令位置の公開資料なし） · `00afcd24`（命令位置の公開資料なし）

~~~diff
- 00afc8e0 ["INT_ADD", "register:40f0:8", ["const:afc8e0:8", "const:4:8"]]
- 00afc8e0 ["CALL", null, ["callee:008514f8:8"]]
+ 00afcd08 ["INT_ADD", "register:40f0:8", ["const:afcd08:8", "const:4:8"]]
+ 00afcd08 ["CALL", null, ["callee:008514f8:8"]]
- 00afc8e0 bytes f652f597
+ 00afcd08 bytes fc51f597
- 00afc8fc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00afc8fc ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00afc8fc ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:0:8"]]
- 00afc8fc ["INT_ADD", "tmp:2:8", ["register:4040:8", "tmp:1:8"]]
- 00afc8fc bytes 086969b8
+ 00afcd24 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00afcd24 ["COPY", "tmp:1:8", ["tmp:0:8"]]
+ 00afcd24 ["INT_LEFT", "tmp:1:8", ["tmp:1:8", "const:0:8"]]
+ 00afcd24 ["INT_ADD", "tmp:2:8", ["register:4040:8", "tmp:1:8"]]
+ 00afcd24 bytes 086969b8
~~~


<a id="compare-53a9ddabe780d387bd9505b3e981c629"></a>

### [`00afc9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc9a0.md) → [`00afcdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcdc8.md) FUN_00afcdc8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`007119b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00711/007119b0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`007119f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00711/007119f0.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afc9d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afce00"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afc9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc9a0.md#insn-00afc9d8) · [`00afc9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc9a0.md#insn-00afc9bc)
- 新版 `00afce00`（命令位置の公開資料なし） · `00afcde4`（命令位置の公開資料なし）

~~~diff
- 00afc9d8 ["COPY", "tmp:0:4", ["register:4098:4"]]
- 00afc9d8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00afc9d8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00afc9d8 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00afc9d8 bytes 136929b8
+ 00afce00 ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 00afce00 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00afce00 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00afce00 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00afce00 bytes 136929b8
- 00afc9bc ["INT_ADD", "register:40f0:8", ["const:afc9bc:8", "const:4:8"]]
- 00afc9bc ["CALL", null, ["callee:008514f8:8"]]
+ 00afcde4 ["INT_ADD", "register:40f0:8", ["const:afcde4:8", "const:4:8"]]
+ 00afcde4 ["CALL", null, ["callee:008514f8:8"]]
- 00afc9bc bytes bf52f597
+ 00afcde4 bytes c551f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e649cb623343cd4e862e8cadb916e9b4"></a>

### [`00afc9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc9ec.md) → [`00afce14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afce14.md) FUN_00afce14

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005f2d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2d28.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`005f2d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f2/005f2d68.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afce54"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afca2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc9ec.md#insn-00afca2c) · [`00afca08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afc9ec.md#insn-00afca08)
- 新版 `00afce54`（命令位置の公開資料なし） · `00afce30`（命令位置の公開資料なし）

~~~diff
- 00afca2c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00afca2c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00afca2c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00afca2c ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00afca2c bytes 0a6929b8
+ 00afce54 ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 00afce54 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00afce54 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00afce54 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00afce54 bytes 0a6929b8
- 00afca08 ["INT_ADD", "register:40f0:8", ["const:afca08:8", "const:4:8"]]
- 00afca08 ["CALL", null, ["callee:008514f8:8"]]
+ 00afce30 ["INT_ADD", "register:40f0:8", ["const:afce30:8", "const:4:8"]]
+ 00afce30 ["CALL", null, ["callee:008514f8:8"]]
- 00afca08 bytes ac52f597
+ 00afce30 bytes b251f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b426d08b098dc5c10f29fdcbfed98e7"></a>

### [`00afca40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afca40.md) → [`00afce68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afce68.md) FUN_00afce68

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afca44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afca40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afca44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afca74",
      "READ",
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
      "00afce68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afce6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00afce9c",
      "READ",
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

- 旧版 [`00afca40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afca40.md#insn-00afca40) · [`00afca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afca40.md#insn-00afca44) · [`00afca7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afca40.md#insn-00afca7c)

~~~diff
- 00afca40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afca40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afca40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00afca40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afca40 bytes fd7bbea9
- 00afca44 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afca44 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afca44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00afca44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afca44 bytes f44f01a9
- 00afca7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00afca7c ["RETURN", null, ["register:0:8"]]
- 00afca7c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d01af399dc933960bf12a86d02f61192"></a>

### [`00afcacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcacc.md) → [`00afcef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afcef4.md) FUN_00afcef4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00710298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00710/00710298.md) · 呼出先 1件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`007102d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00710/007102d8.md) · 呼出先 1件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcb0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afcf34"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afcb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcacc.md#insn-00afcb0c) · [`00afcae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcacc.md#insn-00afcae8)
- 新版 `00afcf34`（命令位置の公開資料なし） · `00afcf10`（命令位置の公開資料なし）

~~~diff
- 00afcb0c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00afcb0c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00afcb0c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00afcb0c ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00afcb0c bytes 0a6929b8
+ 00afcf34 ["COPY", "tmp:0:4", ["register:4050:4"]]
+ 00afcf34 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00afcf34 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00afcf34 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00afcf34 bytes 0a6929b8
- 00afcae8 ["INT_ADD", "register:40f0:8", ["const:afcae8:8", "const:4:8"]]
- 00afcae8 ["CALL", null, ["callee:008514f8:8"]]
+ 00afcf10 ["INT_ADD", "register:40f0:8", ["const:afcf10:8", "const:4:8"]]
+ 00afcf10 ["CALL", null, ["callee:008514f8:8"]]
- 00afcae8 bytes 7452f597
+ 00afcf10 bytes 7a51f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b53e914e35123b6c2d08840ceeff901"></a>

### [`00afcbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcbf4.md) → [`00afd01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afd01c.md) FUN_00afd01c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcc94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00afd0bc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00afcc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcbf4.md#insn-00afcc94) · [`00afcc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcbf4.md#insn-00afcc10)
- 新版 `00afd0bc`（命令位置の公開資料なし） · `00afd038`（命令位置の公開資料なし）

~~~diff
- 00afcc94 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 00afcc94 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00afcc94 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00afcc94 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00afcc94 bytes 146929b8
+ 00afd0bc ["COPY", "tmp:0:4", ["register:40a0:4"]]
+ 00afd0bc ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00afd0bc ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00afd0bc ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00afd0bc bytes 146929b8
- 00afcc10 ["INT_ADD", "register:40f0:8", ["const:afcc10:8", "const:4:8"]]
- 00afcc10 ["CALL", null, ["callee:008514f8:8"]]
+ 00afd038 ["INT_ADD", "register:40f0:8", ["const:afd038:8", "const:4:8"]]
+ 00afd038 ["CALL", null, ["callee:008514f8:8"]]
- 00afcc10 bytes 2a52f597
+ 00afd038 bytes 3051f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-755227afb26d76985ce6ed3e387de39f"></a>

### [`00afcca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcca8.md) → [`00afd0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afd0d0.md) FUN_00afd0d0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00716d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00716/00716d90.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00afccbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcca8.md#insn-00afccbc) · [`00afccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcca8.md#insn-00afccd0) · [`00afccd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcca8.md#insn-00afccd4)
- 新版 `00afd0e4`（命令位置の公開資料なし） · `00afd0f8`（命令位置の公開資料なし） · `00afd0fc`（命令位置の公開資料なし）

~~~diff
- 00afccbc ["INT_ADD", "register:40f0:8", ["const:afccbc:8", "const:4:8"]]
- 00afccbc ["CALL", null, ["callee:008514f8:8"]]
+ 00afd0e4 ["INT_ADD", "register:40f0:8", ["const:afd0e4:8", "const:4:8"]]
+ 00afd0e4 ["CALL", null, ["callee:008514f8:8"]]
- 00afccbc bytes ff51f597
+ 00afd0e4 bytes 0551f597
- 00afccd0 ["INT_ADD", "register:40f0:8", ["const:afccd0:8", "const:4:8"]]
- 00afccd0 ["CALL", null, ["callee:005e7420:8"]]
+ 00afd0f8 ["INT_ADD", "register:40f0:8", ["const:afd0f8:8", "const:4:8"]]
+ 00afd0f8 ["CALL", null, ["callee:005e7420:8"]]
- 00afccd0 bytes c4a9eb97
+ 00afd0f8 bytes caa8eb97
- 00afccd4 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00afccd4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00afccd4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00afccd4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00afd0fc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00afd0fc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00afd0fc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00afd0fc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00afccd4 bytes 60010037
+ 00afd0fc bytes 60010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eebf06ad9b6d5802bafe2b6fb4416f14"></a>

### [`00afcf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcf78.md) → [`00afd3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afd/00afd3a0.md) FUN_00afd3a0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcf78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcf78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00afcf7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00afcf78",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afcf7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00afcf80",
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
      "00afd3a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00afd3a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00afd3a8",
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

- 旧版 [`00afcf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcf78.md#insn-00afcf78) · [`00afcf7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcf78.md#insn-00afcf7c) · [`00afcf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afc/00afcf78.md#insn-00afcf80)

~~~diff
- 00afcf78 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00afcf78 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00afcf78 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00afcf78 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00afcf78 bytes fd7bbda9
- 00afcf7c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00afcf7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00afcf7c bytes f50b00f9
- 00afcf80 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00afcf80 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00afcf80 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00afcf80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00afcf80 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-071d2778273f6aee54375ebaa1015a10"></a>

### [`00b000b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b000b0.md) → [`00b004d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b004d8.md) FUN_00b004d8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00120"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b00548"
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
      "unmatched:00b00124",
      "DATA",
      [
        "storage",
        "0023d2b0",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b0054c",
      "DATA",
      [
        "storage",
        "0023d2b0",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b000b0.md#insn-00b00120) · [`00b000cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b000b0.md#insn-00b000cc)
- 新版 `00b00548`（命令位置の公開資料なし） · `00b004f4`（命令位置の公開資料なし）

~~~diff
- 00b00120 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b00120 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b00120 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b00120 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b00120 bytes 0801899a
+ 00b00548 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b00548 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b00548 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b00548 ["COPY", "register:4040:8", ["tmp:0:8"]]
+ 00b00548 bytes 0801899a
- 00b000cc ["INT_ADD", "register:40f0:8", ["const:b000cc:8", "const:4:8"]]
- 00b000cc ["CALL", null, ["callee:008514f8:8"]]
+ 00b004f4 ["INT_ADD", "register:40f0:8", ["const:b004f4:8", "const:4:8"]]
+ 00b004f4 ["CALL", null, ["callee:008514f8:8"]]
- 00b000cc bytes fb44f597
+ 00b004f4 bytes 0144f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bec7df19782e8af54335d6987d754b6b"></a>

### [`00b00248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00248.md) → [`00b00670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00670.md) FUN_00b00670

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b002b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b006e0"
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
      "unmatched:00b002bc",
      "DATA",
      [
        "storage",
        "0023d360",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b006e4",
      "DATA",
      [
        "storage",
        "0023d360",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b002b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00248.md#insn-00b002b8) · [`00b00264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00248.md#insn-00b00264)
- 新版 `00b006e0`（命令位置の公開資料なし） · `00b0068c`（命令位置の公開資料なし）

~~~diff
- 00b002b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b002b8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b002b8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b002b8 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b002b8 bytes 0801899a
+ 00b006e0 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b006e0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b006e0 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b006e0 ["COPY", "register:4040:8", ["tmp:0:8"]]
+ 00b006e0 bytes 0801899a
- 00b00264 ["INT_ADD", "register:40f0:8", ["const:b00264:8", "const:4:8"]]
- 00b00264 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0068c ["INT_ADD", "register:40f0:8", ["const:b0068c:8", "const:4:8"]]
+ 00b0068c ["CALL", null, ["callee:008514f8:8"]]
- 00b00264 bytes 9544f597
+ 00b0068c bytes 9b43f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a9f9071cda7911f376b10781851668b"></a>

### [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) → [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) FUN_00b009dc

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) · 呼出先 67件 [`00afeea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afeea4.md) [`00b00b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00b10.md) [`00b00bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00bb8.md) [`00b00ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00ce8.md) [`00b00d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00d90.md)
- 新版 呼出元 1件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) · 呼出先 67件 [`00aff2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00aff2cc.md) [`00b00f38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00f38.md) [`00b00fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00fe0.md) [`00b01110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b01110.md) [`00b011b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b011b8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 94.17% / 新版 94.17%

CFGの説明率　旧版 88.34% / 新版 87.80%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00658"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b00758"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b008e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b00a04",
      "DATA",
      [
        "storage",
        "0030a384",
        "switchD_00b005e4::switchdataD_0030a384",
        "ushort"
      ]
    ],
    [
      "unmatched:00b00654",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b03444"
      ]
    ],
    [
      "unmatched:00b00658",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b00eec"
      ]
    ]
  ],
  "added": [
    [
      "00b00a04",
      "DATA",
      [
        "storage",
        "0030a3c4",
        "switchD_00b00a0c::switchdataD_0030a3c4",
        "ushort"
      ]
    ],
    [
      "00b00a7c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b03444"
      ]
    ],
    [
      "00b00a80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b00eec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md#insn-00b00654) · [`00b00658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md#insn-00b00658) · [`00b00754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md#insn-00b00754)

~~~diff
- 00b00654 ["INT_ADD", "register:40f0:8", ["const:b00654:8", "const:4:8"]]
- 00b00654 ["CALL", null, ["callee:00b03444:8"]]
- 00b00654 bytes 720a0094
- 00b00658 ["INT_EQUAL", "tmp:0:1", ["register:4000:4", "const:0:4"]]
- 00b00658 ["CBRANCH", null, ["local:b102:8", "tmp:0:1"]]
- 00b00658 bytes 60230034
- 00b00754 ["INT_ADD", "register:40f0:8", ["const:b00754:8", "const:4:8"]]
- 00b00754 ["CALL", null, ["callee:00b03444:8"]]
- 00b00754 bytes 320a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb30deb50fac141aff24ca7b89f61a94"></a>

### [`00b01074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01074.md) → [`00b0149c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b0149c.md) FUN_00b0149c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 50.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b01090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01074.md#insn-00b01090) · [`00b010a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01074.md#insn-00b010a4) · [`00b010b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01074.md#insn-00b010b0)
- 新版 `00b014b8`（命令位置の公開資料なし） · `00b014cc`（命令位置の公開資料なし） · `00b014d8`（命令位置の公開資料なし）

~~~diff
- 00b01090 ["INT_ADD", "register:40f0:8", ["const:b01090:8", "const:4:8"]]
- 00b01090 ["CALL", null, ["callee:008514f8:8"]]
+ 00b014b8 ["INT_ADD", "register:40f0:8", ["const:b014b8:8", "const:4:8"]]
+ 00b014b8 ["CALL", null, ["callee:008514f8:8"]]
- 00b01090 bytes 0a41f597
+ 00b014b8 bytes 1040f597
- 00b010a4 ["INT_ADD", "register:40f0:8", ["const:b010a4:8", "const:4:8"]]
- 00b010a4 ["CALL", null, ["callee:005e7420:8"]]
+ 00b014cc ["INT_ADD", "register:40f0:8", ["const:b014cc:8", "const:4:8"]]
+ 00b014cc ["CALL", null, ["callee:005e7420:8"]]
- 00b010a4 bytes cf98eb97
+ 00b014cc bytes d597eb97
- 00b010b0 ["BRANCH", null, ["local:b4:8"]]
+ 00b014d8 ["BRANCH", null, ["local:b5:8"]]
- 00b010b0 bytes 0b000014
+ 00b014d8 bytes 0b000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ee6a8e35136b6358b40e02014fc4d8e"></a>

### [`00b012d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b012d4.md) → [`00b016fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b016fc.md) FUN_00b016fc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 4件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 28.57% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01348"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b01770"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b01348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b012d4.md#insn-00b01348) · [`00b012f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b012d4.md#insn-00b012f0)
- 新版 `00b01770`（命令位置の公開資料なし） · `00b01718`（命令位置の公開資料なし）

~~~diff
- 00b01348 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b01348 ["RETURN", null, ["register:0:8"]]
- 00b01348 bytes c0035fd6
+ 00b01770 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b01770 ["RETURN", null, ["register:0:8"]]
+ 00b01770 bytes c0035fd6
- 00b012f0 ["INT_ADD", "register:40f0:8", ["const:b012f0:8", "const:4:8"]]
- 00b012f0 ["CALL", null, ["callee:008514f8:8"]]
+ 00b01718 ["INT_ADD", "register:40f0:8", ["const:b01718:8", "const:4:8"]]
+ 00b01718 ["CALL", null, ["callee:008514f8:8"]]
- 00b012f0 bytes 7240f597
+ 00b01718 bytes 783ff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-376d0c9324b8fa36661f26331eaca37e"></a>

### [`00b0136c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0136c.md) → [`00b01794`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b01794.md) FUN_00b01794

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0136c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0136c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01370"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0136c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01370",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01374",
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
      "00b01794",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b01798",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b0179c",
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

- 旧版 [`00b0136c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0136c.md#insn-00b0136c) · [`00b01370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0136c.md#insn-00b01370) · [`00b01374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0136c.md#insn-00b01374)

~~~diff
- 00b0136c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0136c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0136c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b0136c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b0136c bytes fd7bbda9
- 00b01370 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b01370 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b01370 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b01370 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01370 bytes f65701a9
- 00b01374 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b01374 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b01374 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b01374 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01374 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca955e97d23820e69e613f8f458a4200"></a>

### [`00b01630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01630.md) → [`00b01a58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b01a58.md) FUN_00b01a58

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b016a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b01ac8"
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
      "unmatched:00b016a4",
      "DATA",
      [
        "storage",
        "0023d2cc",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b01acc",
      "DATA",
      [
        "storage",
        "0023d2cc",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b016a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01630.md#insn-00b016a0) · [`00b0164c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01630.md#insn-00b0164c)
- 新版 `00b01ac8`（命令位置の公開資料なし） · `00b01a74`（命令位置の公開資料なし）

~~~diff
- 00b016a0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b016a0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b016a0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b016a0 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b016a0 bytes 0801899a
+ 00b01ac8 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b01ac8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b01ac8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b01ac8 ["COPY", "register:4040:8", ["tmp:0:8"]]
+ 00b01ac8 bytes 0801899a
- 00b0164c ["INT_ADD", "register:40f0:8", ["const:b0164c:8", "const:4:8"]]
- 00b0164c ["CALL", null, ["callee:008514f8:8"]]
+ 00b01a74 ["INT_ADD", "register:40f0:8", ["const:b01a74:8", "const:4:8"]]
+ 00b01a74 ["CALL", null, ["callee:008514f8:8"]]
- 00b0164c bytes 9b3ff597
+ 00b01a74 bytes a13ef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2d8e128ec4ace34e56e327b4cd52e27"></a>

### [`00b0177c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0177c.md) → [`00b01ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b01ba4.md) FUN_00b01ba4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 58.33% / 新版 58.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0177c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0177c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01780"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0177c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01780",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01784",
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
      "00b01ba4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b01ba8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b01bac",
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

- 旧版 [`00b0177c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0177c.md#insn-00b0177c) · [`00b01780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0177c.md#insn-00b01780) · [`00b01784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0177c.md#insn-00b01784)

~~~diff
- 00b0177c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0177c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0177c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b0177c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b0177c bytes fd7bbda9
- 00b01780 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b01780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b01780 bytes f50b00f9
- 00b01784 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b01784 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b01784 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b01784 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01784 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30a187eebe2a8a2a3f5d4e68faa1a62e"></a>

### [`00b01e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01e14.md) → [`00b0223c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0223c.md) FUN_00b0223c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b01e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01e14.md#insn-00b01e30) · [`00b01e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01e14.md#insn-00b01e44) · [`00b01e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01e14.md#insn-00b01e50)
- 新版 `00b02258`（命令位置の公開資料なし） · `00b0226c`（命令位置の公開資料なし） · `00b02278`（命令位置の公開資料なし）

~~~diff
- 00b01e30 ["INT_ADD", "register:40f0:8", ["const:b01e30:8", "const:4:8"]]
- 00b01e30 ["CALL", null, ["callee:008514f8:8"]]
+ 00b02258 ["INT_ADD", "register:40f0:8", ["const:b02258:8", "const:4:8"]]
+ 00b02258 ["CALL", null, ["callee:008514f8:8"]]
- 00b01e30 bytes a23df597
+ 00b02258 bytes a83cf597
- 00b01e44 ["INT_ADD", "register:40f0:8", ["const:b01e44:8", "const:4:8"]]
- 00b01e44 ["CALL", null, ["callee:005e7420:8"]]
+ 00b0226c ["INT_ADD", "register:40f0:8", ["const:b0226c:8", "const:4:8"]]
+ 00b0226c ["CALL", null, ["callee:005e7420:8"]]
- 00b01e44 bytes 6795eb97
+ 00b0226c bytes 6d94eb97
- 00b01e50 ["BRANCH", null, ["local:b4:8"]]
+ 00b02278 ["BRANCH", null, ["local:b3:8"]]
- 00b01e50 bytes 0b000014
+ 00b02278 bytes 0b000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1ec27163a9b017bab20ba547075419c"></a>

### [`00b01f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01f24.md) → [`00b0234c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0234c.md) FUN_00b0234c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 61.70% / 新版 61.70%

CFGの説明率　旧版 5.88% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01f24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01f28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b01f24",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01f28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01f2c",
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
      "00b0234c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b02350",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b02354",
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

- 旧版 [`00b01f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01f24.md#insn-00b01f24) · [`00b01f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01f24.md#insn-00b01f28) · [`00b01f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01f24.md#insn-00b01f2c)

~~~diff
- 00b01f24 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b01f24 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b01f24 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b01f24 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b01f24 bytes fd7bbda9
- 00b01f28 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b01f28 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b01f28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b01f28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01f28 bytes f65701a9
- 00b01f2c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b01f2c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b01f2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b01f2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01f2c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02292b7236e690c571455011d2805d7e"></a>

### [`00b0271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0271c.md) → [`00b02b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02b44.md) FUN_00b02b44

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0271c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0271c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02720"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0271c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b02720",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b02724",
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
      "00b02b44",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b02b48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b02b4c",
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

- 旧版 [`00b0271c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0271c.md#insn-00b0271c) · [`00b02720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0271c.md#insn-00b02720) · [`00b02724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0271c.md#insn-00b02724)

~~~diff
- 00b0271c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0271c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0271c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b0271c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b0271c bytes fd7bbda9
- 00b02720 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b02720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b02720 bytes f50b00f9
- 00b02724 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b02724 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b02724 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b02724 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b02724 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-044db706b4b216da4cc85881f8746111"></a>

### [`00b027b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b027b4.md) → [`00b02bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02bdc.md) FUN_00b02bdc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 10.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b027b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b027b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b027b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b027b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b027b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b027bc",
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
      "00b02bdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b02be0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b02be4",
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

- 旧版 [`00b027b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b027b4.md#insn-00b027b4) · [`00b027b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b027b4.md#insn-00b027b8) · [`00b027bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b027b4.md#insn-00b027bc)

~~~diff
- 00b027b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b027b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b027b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b027b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b027b4 bytes fd7bbda9
- 00b027b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b027b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b027b8 bytes f50b00f9
- 00b027bc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b027bc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b027bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b027bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b027bc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f251b97a5e8dc42e4429d847b9462f1"></a>

### [`00b03190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03190.md) → [`00b035b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b035b8.md) FUN_00b035b8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 42.86% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b031ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03190.md#insn-00b031ac) · [`00b031c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03190.md#insn-00b031c0) · [`00b031cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03190.md#insn-00b031cc)
- 新版 `00b035d4`（命令位置の公開資料なし） · `00b035e8`（命令位置の公開資料なし） · `00b035f4`（命令位置の公開資料なし）

~~~diff
- 00b031ac ["INT_ADD", "register:40f0:8", ["const:b031ac:8", "const:4:8"]]
- 00b031ac ["CALL", null, ["callee:008514f8:8"]]
+ 00b035d4 ["INT_ADD", "register:40f0:8", ["const:b035d4:8", "const:4:8"]]
+ 00b035d4 ["CALL", null, ["callee:008514f8:8"]]
- 00b031ac bytes c338f597
+ 00b035d4 bytes c937f597
- 00b031c0 ["INT_ADD", "register:40f0:8", ["const:b031c0:8", "const:4:8"]]
- 00b031c0 ["CALL", null, ["callee:005e7420:8"]]
+ 00b035e8 ["INT_ADD", "register:40f0:8", ["const:b035e8:8", "const:4:8"]]
+ 00b035e8 ["CALL", null, ["callee:005e7420:8"]]
- 00b031c0 bytes 8890eb97
+ 00b035e8 bytes 8e8feb97
- 00b031cc ["BRANCH", null, ["local:b5:8"]]
+ 00b035f4 ["BRANCH", null, ["local:b4:8"]]
- 00b031cc bytes 0b000014
+ 00b035f4 bytes 0b000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bbd2540b6783ae9b1e53a62bc5a8e4f"></a>

### [`00b03418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03418.md) → [`00b03840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03840.md) FUN_00b03840

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md)
- 新版 呼出元 5件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b03478",
      "DATA",
      [
        "storage",
        "0023d404",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b038a0",
      "DATA",
      [
        "storage",
        "0023d404",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03418.md#insn-00b0343c) · [`00b03450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03418.md#insn-00b03450) · [`00b03458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03418.md#insn-00b03458)
- 新版 `00b03864`（命令位置の公開資料なし） · `00b03878`（命令位置の公開資料なし） · `00b03880`（命令位置の公開資料なし）

~~~diff
- 00b0343c ["INT_ADD", "register:40f0:8", ["const:b0343c:8", "const:4:8"]]
- 00b0343c ["CALL", null, ["callee:008514f8:8"]]
+ 00b03864 ["INT_ADD", "register:40f0:8", ["const:b03864:8", "const:4:8"]]
+ 00b03864 ["CALL", null, ["callee:008514f8:8"]]
- 00b0343c bytes 1f38f597
+ 00b03864 bytes 2537f597
- 00b03450 ["INT_ADD", "register:40f0:8", ["const:b03450:8", "const:4:8"]]
- 00b03450 ["CALL", null, ["callee:005e7420:8"]]
+ 00b03878 ["INT_ADD", "register:40f0:8", ["const:b03878:8", "const:4:8"]]
+ 00b03878 ["CALL", null, ["callee:005e7420:8"]]
- 00b03450 bytes e48feb97
+ 00b03878 bytes ea8eeb97
- 00b03458 ["INT_ADD", "register:40f0:8", ["const:b03458:8", "const:4:8"]]
- 00b03458 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03880 ["INT_ADD", "register:40f0:8", ["const:b03880:8", "const:4:8"]]
+ 00b03880 ["CALL", null, ["callee:008514f8:8"]]
- 00b03458 bytes 1838f597
+ 00b03880 bytes 1e37f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baf07891baa002060b73b8d04cdc1551"></a>

### [`00b03c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03c30.md) → [`00b04058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04058.md) FUN_00b04058

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`00b045f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b045f8.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md)
- 新版 呼出元 2件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) [`00b04a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04a20.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 92.65% / 新版 92.65%

CFGの説明率　旧版 84.55% / 新版 83.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03db0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b040f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0418c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b04080",
      "DATA",
      [
        "storage",
        "0030a42a",
        "switchD_00b03c6c::switchdataD_0030a42a",
        "byte"
      ]
    ],
    [
      "unmatched:00b03cc0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005e7420"
      ]
    ],
    [
      "unmatched:00b03cc8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ],
  "added": [
    [
      "00b04080",
      "DATA",
      [
        "storage",
        "0030a46a",
        "switchD_00b04094::switchdataD_0030a46a",
        "byte"
      ]
    ],
    [
      "00b040e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005e7420"
      ]
    ],
    [
      "00b040f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b03cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03c30.md#insn-00b03cc0) · [`00b03cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03c30.md#insn-00b03cc8) · [`00b03d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03c30.md#insn-00b03d98)

~~~diff
- 00b03cc0 ["INT_ADD", "register:40f0:8", ["const:b03cc0:8", "const:4:8"]]
- 00b03cc0 ["CALL", null, ["callee:005e7420:8"]]
- 00b03cc0 bytes c88deb97
- 00b03cc8 ["INT_ADD", "register:40f0:8", ["const:b03cc8:8", "const:4:8"]]
- 00b03cc8 ["CALL", null, ["callee:008514f8:8"]]
- 00b03cc8 bytes fc35f597
- 00b03d98 ["INT_ADD", "register:40f0:8", ["const:b03d98:8", "const:4:8"]]
- 00b03d98 ["CALL", null, ["callee:005e7420:8"]]
- 00b03d98 bytes 928deb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b939e730400970ec185c944143516ff"></a>

### [`00b29a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29a58.md) → [`00b29e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e80.md) FUN_00b29e80

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b12ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b12/00b12ed4.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00b29be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29be8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a010.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.00% / 新版 93.00%

CFGの説明率　旧版 77.78% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b29ad8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b29ae0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b29f00"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b29ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29a58.md#insn-00b29ad8) · [`00b29ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b29/00b29a58.md#insn-00b29ae0)
- 新版 `00b29f00`（命令位置の公開資料なし）

~~~diff
- 00b29ad8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b29ad8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b29ad8 ["COPY", "tmp:2:8", ["register:4058:8"]]
- 00b29ad8 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00b29ad8 bytes 6a818a9a
- 00b29ae0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b29ae0 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b29ae0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b29ae0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b29ae0 bytes 5731899a
+ 00b29f00 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b29f00 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b29f00 ["COPY", "tmp:2:8", ["register:4058:8"]]
+ 00b29f00 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
+ 00b29f00 bytes 6a818a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-910adf50087e31224b0fec54c39c045d"></a>

### [`00b2a3ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a3ac.md) → [`00b2a7d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a7d4.md) FUN_00b2a7d4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2a3c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2a7ec"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2a3cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2a3c4",
      "DATA",
      [
        "storage",
        "00c8ede8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00b2a3c8",
      "DATA",
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
      "00b2a7ec",
      "DATA",
      [
        "storage",
        "00c8f1e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00b2a7f0",
      "DATA",
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

- 旧版 [`00b2a3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a3ac.md#insn-00b2a3c4) · [`00b2a3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a3ac.md#insn-00b2a3cc)
- 新版 `00b2a7ec`（命令位置の公開資料なし）

~~~diff
- 00b2a3c4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b2a3c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b2a3c4 bytes 080000f9
- 00b2a3cc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b2a3cc ["RETURN", null, ["register:0:8"]]
- 00b2a3cc bytes c0035fd6
+ 00b2a7ec ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b2a7ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b2a7ec bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7f3c9f3a515f0e5e3baba1ab36fac29"></a>

### [`00b2a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a3d0.md) → [`00b2a7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a7f8.md) FUN_00b2a7f8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2a3d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2a800"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2a3dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2a3d8",
      "DATA",
      [
        "storage",
        "00c8ede8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2a800",
      "DATA",
      [
        "storage",
        "00c8f1e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a3d0.md#insn-00b2a3d8) · [`00b2a3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a3d0.md#insn-00b2a3dc)
- 新版 `00b2a800`（命令位置の公開資料なし）

~~~diff
- 00b2a3d8 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00b2a3d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b2a3d8 bytes 280000f9
- 00b2a3dc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b2a3dc ["RETURN", null, ["register:0:8"]]
- 00b2a3dc bytes c0035fd6
+ 00b2a800 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00b2a800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b2a800 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d55b5a4463afbf029dd7b014ec210e1"></a>

### [`00b2a5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a5e8.md) → [`00b2aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aa10.md) FUN_00b2aa10

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 89.47% / 新版 94.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2a5e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2a5e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2a5ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2a5e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2a5ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2a5f0",
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
      "00b2aa10",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b2aa14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b2aa18",
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

- 旧版 [`00b2a5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a5e8.md#insn-00b2a5e8) · [`00b2a5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a5e8.md#insn-00b2a5ec) · [`00b2a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2a/00b2a5e8.md#insn-00b2a5f0)

~~~diff
- 00b2a5e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b2a5e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b2a5e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b2a5e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b2a5e8 bytes fd7bbda9
- 00b2a5ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b2a5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b2a5ec bytes f50b00f9
- 00b2a5f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b2a5f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b2a5f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b2a5f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b2a5f0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dd3a799e3f626b81fe941f5760aa175"></a>

### [`00b2bb0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bb0c.md) → [`00b2bf34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bf34.md) FUN_00b2bf34

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md) · 呼出先 8件 [`00576278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576278.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) · 呼出先 8件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.67% / 新版 82.67%

CFGの説明率　旧版 88.24% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2bb10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2bb10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2bb14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2bb10",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2bb14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2bb18",
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
      "00b2bf38",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b2bf3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b2bf40",
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

- 旧版 [`00b2bb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bb0c.md#insn-00b2bb10) · [`00b2bb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bb0c.md#insn-00b2bb14) · [`00b2bb18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2bb0c.md#insn-00b2bb18)

~~~diff
- 00b2bb10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b2bb10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b2bb10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b2bb10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b2bb10 bytes fd7b04a9
- 00b2bb14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00b2bb14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b2bb14 bytes f52b00f9
- 00b2bb18 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b2bb18 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b2bb18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b2bb18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b2bb18 bytes f44f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c28e64939c39d58892f328d12dfd69b"></a>

### [`00b2cfd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cfd4.md) → [`00b2d3fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d3fc.md) FUN_00b2d3fc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2cfdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2d404"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2cfe0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2cfdc",
      "DATA",
      [
        "storage",
        "00c8ee68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2d404",
      "DATA",
      [
        "storage",
        "00c8f268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2cfdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cfd4.md#insn-00b2cfdc) · [`00b2cfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2cfd4.md#insn-00b2cfe0)
- 新版 `00b2d404`（命令位置の公開資料なし）

~~~diff
- 00b2cfdc ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00b2cfdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b2cfdc bytes 280000f9
- 00b2cfe0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b2cfe0 ["RETURN", null, ["register:0:8"]]
- 00b2cfe0 bytes c0035fd6
+ 00b2d404 ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00b2d404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b2d404 bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fd87cd131f34031c722589b412419be"></a>

### [`00b2d2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d2cc.md) → [`00b2d6f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d6f4.md) FUN_00b2d6f4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d2d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2d700"
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
      "unmatched:00b2d2d8",
      "DATA",
      [
        "storage",
        "00c8ef68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2d700",
      "DATA",
      [
        "storage",
        "00c8f368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d2d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d2cc.md#insn-00b2d2d8) · [`00b2d2cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d2cc.md#insn-00b2d2cc)
- 新版 `00b2d700`（命令位置の公開資料なし）

~~~diff
- 00b2d2d8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b2d2d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b2d2d8 bytes 090000f9
+ 00b2d700 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b2d700 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00b2d700 bytes 090000f9
- 00b2d2cc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00b2d2cc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b2d2cc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b2d2cc bytes 08404039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7303a1134a460b71e9590c1f2cdef3e2"></a>

### [`00b2d2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d2ec.md) → [`00b2d714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d714.md) FUN_00b2d714

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d2f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2d720"
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
      "unmatched:00b2d2f8",
      "DATA",
      [
        "storage",
        "00c8ef68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2d720",
      "DATA",
      [
        "storage",
        "00c8f368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d2ec.md#insn-00b2d2f8) · [`00b2d2ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d2ec.md#insn-00b2d2ec)
- 新版 `00b2d720`（命令位置の公開資料なし）

~~~diff
- 00b2d2f8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b2d2f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b2d2f8 bytes 090000f9
+ 00b2d720 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b2d720 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00b2d720 bytes 090000f9
- 00b2d2ec ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00b2d2ec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b2d2ec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b2d2ec bytes 08404039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7eb644ecbbe978d9b4f1e4ede78865be"></a>

### [`00b2d468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d468.md) → [`00b2d890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d890.md) _INIT_260

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.19% / 新版 70.19%

CFGの説明率　旧版 62.16% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d498"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d4ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d4b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2d498",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2d4a4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b2d4ac",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b2d8c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b2d8cc",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b2d8d4",
      "WRITE",
      [
        "storage",
        "Stack[-0xff]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d468.md#insn-00b2d498) · [`00b2d4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d468.md#insn-00b2d4ac) · [`00b2d4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d468.md#insn-00b2d4b0)

~~~diff
- 00b2d498 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b2d498 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b2d498 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b2d498 bytes a9831ff8
- 00b2d4ac ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b2d4ac ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00b2d4ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b2d4ac bytes ea130278
- 00b2d4b0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b2d4b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b2d4b0 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7331c08830b72e56ce53472d496d1278"></a>

### [`00b2f320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f320.md) → [`00b2f748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f748.md) FUN_00b2f748

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) [`00a955d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a95/00a955d0.md) · 呼出先 1件 [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md)
- 新版 呼出元 2件 [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) [`00a957c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a95/00a957c8.md) · 呼出先 1件 [`00b3be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f35c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2f784"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f364"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2f35c",
      "WRITE",
      [
        "storage",
        "00ca3a9c",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b2f360",
      "DATA",
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
      "00b2f784",
      "WRITE",
      [
        "storage",
        "00ca3e9c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b2f788",
      "DATA",
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

- 旧版 [`00b2f35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f320.md#insn-00b2f35c) · [`00b2f364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f320.md#insn-00b2f364)
- 新版 `00b2f784`（命令位置の公開資料なし）

~~~diff
- 00b2f35c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b2f35c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:a9c:8"]]
- 00b2f35c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b2f35c bytes 09712a39
- 00b2f364 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b2f364 ["RETURN", null, ["register:0:8"]]
- 00b2f364 bytes c0035fd6
+ 00b2f784 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00b2f784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:e9c:8"]]
+ 00b2f784 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b2f784 bytes 09713a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-143160199267134b8e3cece30383b8b5"></a>

### [`00b2f3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3c8.md) → [`00b2f7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f7f0.md) FUN_00b2f7f0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 18件 [`0060a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0060a/0060a860.md) [`00664af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664af0.md) [`00664b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664b8c.md) [`00664cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664cdc.md) [`0070d378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070d378.md) · 呼出先 1件 [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)
- 新版 呼出元 18件 [`0060a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0060a/0060a8a0.md) [`00664b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664b30.md) [`00664bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664bcc.md) [`00664d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664d1c.md) [`0070d3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070d/0070d3b8.md) · 呼出先 1件 [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f3e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b2f808"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f3e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2f3e4",
      "DATA",
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
      "00b2f80c",
      "DATA",
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

- 旧版 [`00b2f3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3c8.md#insn-00b2f3e0) · [`00b2f3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3c8.md#insn-00b2f3e8)
- 新版 `00b2f808`（命令位置の公開資料なし）

~~~diff
- 00b2f3e0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b2f3e0 ["COPY", "tmp:1:4", ["register:4048:4"]]
- 00b2f3e0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b2f3e0 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b2f3e0 bytes 2031881a
- 00b2f3e8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b2f3e8 ["RETURN", null, ["register:0:8"]]
- 00b2f3e8 bytes c0035fd6
+ 00b2f808 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b2f808 ["COPY", "tmp:1:4", ["register:4048:4"]]
+ 00b2f808 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b2f808 ["COPY", "tmp:1:4", ["register:4040:4"]]
+ 00b2f808 bytes 2031881a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5733b16f74f96f3b50837275233f008"></a>

### [`00b2f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3ec.md) → [`00b2f814`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f814.md) FUN_00b2f814

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0075d548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d548.md) · 呼出先 2件 [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)
- 新版 呼出元 1件 [`0075d588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075d/0075d588.md) · 呼出先 2件 [`00b3be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2f870"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f434"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2f448",
      "WRITE",
      [
        "storage",
        "00ca3a9c",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b2f44c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2f450",
      "DATA",
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
      "00b2f870",
      "WRITE",
      [
        "storage",
        "00ca3e9c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b2f874",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b2f878",
      "DATA",
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

- 旧版 [`00b2f434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3ec.md#insn-00b2f434) · [`00b2f448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3ec.md#insn-00b2f448) · [`00b2f454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f3ec.md#insn-00b2f454)

~~~diff
- 00b2f434 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b2f434 ["COPY", "tmp:1:4", ["register:4058:4"]]
- 00b2f434 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b2f434 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b2f434 bytes 6831881a
- 00b2f448 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b2f448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:a9c:8"]]
- 00b2f448 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b2f448 bytes 09712a39
- 00b2f454 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b2f454 ["RETURN", null, ["register:0:8"]]
- 00b2f454 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8305dc9ced721c775d736f9f8d2f1ec"></a>

### [`00b2f480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f480.md) → [`00b2f8a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f8a8.md) FUN_00b2f8a8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`007591f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/007591f4.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) [`00996a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996a80.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 2件 [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)
- 新版 呼出元 4件 [`00759234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/00759234.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) [`00996c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00996/00996c1c.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 2件 [`00b3be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f4f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2f918"
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
      "unmatched:00b2f4f0",
      "WRITE",
      [
        "storage",
        "00ca3a9c",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b2f918",
      "WRITE",
      [
        "storage",
        "00ca3e9c",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2f4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f480.md#insn-00b2f4f0) · [`00b2f498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f480.md#insn-00b2f498)
- 新版 `00b2f918`（命令位置の公開資料なし） · `00b2f8c0`（命令位置の公開資料なし）

~~~diff
- 00b2f4f0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b2f4f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:a9c:8"]]
- 00b2f4f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b2f4f0 bytes 09712a39
+ 00b2f918 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00b2f918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:e9c:8"]]
+ 00b2f918 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b2f918 bytes 09713a39
- 00b2f498 ["INT_ADD", "register:40f0:8", ["const:b2f498:8", "const:4:8"]]
- 00b2f498 ["CALL", null, ["callee:00b3be94:8"]]
+ 00b2f8c0 ["INT_ADD", "register:40f0:8", ["const:b2f8c0:8", "const:4:8"]]
+ 00b2f8c0 ["CALL", null, ["callee:00b3be94:8"]]
- 00b2f498 bytes 75310094
+ 00b2f8c0 bytes 75310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0d92eb2836a1e24a9fbe951de74f967"></a>

### [`00b2f504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f504.md) → [`00b2f92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2f/00b2f92c.md) FUN_00b2f92c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`0070d378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070d378.md) [`007591f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/007591f4.md) [`00961604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00961/00961604.md) [`00962d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00962/00962d80.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 2件 [`00b3ba38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba38.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)
- 新版 呼出元 6件 [`0070d3b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0070d/0070d3b8.md) [`00759234`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/00759234.md) [`009617a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00961/009617a0.md) [`00962f1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00962/00962f1c.md) [`00a06d9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a06/00a06d9c.md) · 呼出先 2件 [`00b3be60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be60.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f504"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f504"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2f508"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2f504",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2f508",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b2f50c",
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
      "00b2f92c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b2f930",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b2f934",
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

- 旧版 [`00b2f504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f504.md#insn-00b2f504) · [`00b2f508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f504.md#insn-00b2f508) · [`00b2f50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f504.md#insn-00b2f50c)

~~~diff
- 00b2f504 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b2f504 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b2f504 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b2f504 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b2f504 bytes fd7bbda9
- 00b2f508 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b2f508 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b2f508 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b2f508 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b2f508 bytes f65701a9
- 00b2f50c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b2f50c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b2f50c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b2f50c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b2f50c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fda50682b28438ff7e250ca1f4212769"></a>

### [`00b35eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35eec.md) → [`00b36314`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36314.md) _INIT_269

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35f04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35f04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35f08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b35ef4",
      "PARAM",
      [
        "storage",
        "01124be8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b35ef8",
      "READ",
      [
        "storage",
        "00c9a7f8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b35ef8",
      "PARAM",
      [
        "storage",
        "00bc43c8",
        "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b3631c",
      "PARAM",
      [
        "storage",
        "01124fe8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b36320",
      "READ",
      [
        "storage",
        "00c9abf8",
        null,
        "pointer"
      ]
    ],
    [
      "00b36320",
      "PARAM",
      [
        "storage",
        "00bc47f0",
        "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b35f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35eec.md#insn-00b35f04) · [`00b35f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35eec.md#insn-00b35f08)
- 新版 `00b3632c`（命令位置の公開資料なし）

~~~diff
- 00b35f04 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b35f04 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b35f04 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b35f04 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b35f04 bytes 3f7c00a9
- 00b35f08 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 00b35f08 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b35f08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b35f08 bytes 3f0800f9
+ 00b3632c ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00b3632c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b3632c ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00b3632c ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 00b3632c bytes 3f7c00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64a419d25bf6149f90cfe4ab25b1a12c"></a>

### [`00b35f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35f10.md) → [`00b36338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b36338.md) FUN_00b36338

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0087e6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6d0.md) · 呼出先 13件 [`004977f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/004977f4.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`0087e710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087e/0087e710.md) · 呼出先 13件 [`00497834`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497834.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.18% / 新版 88.18%

CFGの説明率　旧版 75.00% / 新版 72.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35f30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35f50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b35f60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b35f30",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b35f4c",
      "READ",
      [
        "storage",
        "002b044a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b35f50",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b36358",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b36374",
      "READ",
      [
        "storage",
        "002b048a",
        null,
        "string"
      ]
    ],
    [
      "00b36378",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b35f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35f10.md#insn-00b35f30) · [`00b35f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35f10.md#insn-00b35f50) · [`00b35f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b35/00b35f10.md#insn-00b35f60)

~~~diff
- 00b35f30 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b35f30 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b35f30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b35f30 bytes a8831ff8
- 00b35f50 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b35f50 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
- 00b35f50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b35f50 bytes e8630039
- 00b35f60 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b35f60 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b35f60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:27:8"]]
- 00b35f60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b35f60 bytes ff9f0039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5e24483438fa4fa65f080fd9305666"></a>

### [`00b364ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b364ac.md) → [`00b368d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b36/00b368d4.md) FUN_00b368d4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b14d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b14d4.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`005b1514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005b1/005b1514.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.68% / 新版 73.68%

CFGの説明率　旧版 84.62% / 新版 73.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b364c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b364d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b364e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b364c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b364d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b364e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x3f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b368f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b368fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b36908",
      "WRITE",
      [
        "storage",
        "Stack[-0x3f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b364c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b364ac.md#insn-00b364c8) · [`00b364d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b364ac.md#insn-00b364d4) · [`00b364e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b36/00b364ac.md#insn-00b364e0)

~~~diff
- 00b364c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b364c8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b364c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b364c8 bytes a8831ff8
- 00b364d4 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b364d4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
- 00b364d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b364d4 bytes e9630039
- 00b364e0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b364e0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00b364e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00b364e0 bytes e81302b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6963b1b5c27fd47faa251f2ff985ab4"></a>

### [`00b375f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b375f0.md) → [`00b37a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b37/00b37a18.md) FUN_00b37a18

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0088826c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/0088826c.md) [`0088bbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088b/0088bbac.md) · 呼出先 8件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 2件 [`008882ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/008882ac.md) [`0088bbec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0088b/0088bbec.md) · 呼出先 8件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.92% / 新版 77.92%

CFGの説明率　旧版 64.71% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b375f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b375f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b375f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b375f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b375f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b375fc",
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
      "00b37a1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b37a20",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b37a24",
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

- 旧版 [`00b375f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b375f0.md#insn-00b375f4) · [`00b375f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b375f0.md#insn-00b375f8) · [`00b375fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b37/00b375f0.md#insn-00b375fc)

~~~diff
- 00b375f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b375f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b375f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b375f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b375f4 bytes fd7b04a9
- 00b375f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 00b375f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b375f8 bytes f52b00f9
- 00b375fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b375fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b375fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b375fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b375fc bytes f44f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f636c6e8037df6c8c85251c93144232b"></a>

### [`00b38098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38098.md) → [`00b384c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b384c0.md) FUN_00b384c0

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00888d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00888/00888d88.md) · 呼出先 15件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md)
- 新版 呼出元 1件 [`00888dc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00888/00888dc8.md) · 呼出先 15件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.17% / 新版 80.17%

CFGの説明率　旧版 55.56% / 新版 64.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b380bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b380f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b380f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b380bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b380e8",
      "READ",
      [
        "storage",
        "002b14db",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b380ec",
      "READ",
      [
        "storage",
        "002b14ea",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b384e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b38510",
      "READ",
      [
        "storage",
        "002b151b",
        null,
        "string"
      ]
    ],
    [
      "00b38514",
      "READ",
      [
        "storage",
        "002b152a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b380bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38098.md#insn-00b380bc) · [`00b380f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38098.md#insn-00b380f4) · [`00b380f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38098.md#insn-00b380f8)

~~~diff
- 00b380bc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b380bc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b380bc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b380bc bytes a8831ff8
- 00b380f4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b380f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b380f4 bytes e00b00f9
- 00b380f8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b380f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b380f8 bytes 0000803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ef66de2747b84a9675125357a1afdca"></a>

### [`00b382e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b382e0.md) → [`00b38708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b38708.md) Java_jp_co_ponos_battlecats_IronSourceImplementation_onInitializationComplete

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b382e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b38710"
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
      "unmatched:00b382e4",
      "READ",
      [
        "storage",
        "01124cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b382e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b38720"
      ]
    ]
  ],
  "added": [
    [
      "00b3870c",
      "READ",
      [
        "storage",
        "011250b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b38710",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b38720"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b382e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b382e0.md#insn-00b382e8) · [`00b382e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b382e0.md#insn-00b382e0)
- 新版 `00b38710`（命令位置の公開資料なし）

~~~diff
- 00b382e8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b382e8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b382e8 bytes 800000b4
+ 00b38710 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00b38710 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b38710 bytes 800000b4
- 00b382e0 ["COPY", "register:4040:8", ["const:1124000:8"]]
- 00b382e0 bytes 682f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e330cadc99d17a2e6f135907fa8f660c"></a>

### [`00b390b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b390b8.md) → [`00b394e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b39/00b394e0.md) FUN_00b394e0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a9abdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9a/00a9abdc.md) · 呼出先 8件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`00a9add8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a9a/00a9add8.md) · 呼出先 8件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.71% / 新版 88.71%

CFGの説明率　旧版 53.85% / 新版 41.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b390f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3911c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3951c"
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
      "unmatched:00b390f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b39100",
      "READ",
      [
        "storage",
        "002ae041",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b3911c",
      "WRITE",
      [
        "storage",
        "Stack[-0x57]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b3951c",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b39528",
      "READ",
      [
        "storage",
        "002ae081",
        null,
        "string"
      ]
    ],
    [
      "00b39544",
      "WRITE",
      [
        "storage",
        "Stack[-0x57]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b390f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b390b8.md#insn-00b390f4) · [`00b3911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b390b8.md#insn-00b3911c) · [`00b391a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b390b8.md#insn-00b391a8)

~~~diff
- 00b390f4 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b390f4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:18:8"]]
- 00b390f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b390f4 bytes e8630039
- 00b3911c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:19:8"]]
- 00b3911c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b3911c bytes e093813c
- 00b391a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b391a8 ["RETURN", null, ["register:0:8"]]
- 00b391a8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb8e9c4e35ae2d4019033742f36db220"></a>

### [`00b391ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b391ec.md) → [`00b39614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b39/00b39614.md) FUN_00b39614

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00893108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00893/00893108.md) · 呼出先 12件 [`00497a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00497/00497a08.md) [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`00589104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589104.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`005892e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005892e0.md)
- 新版 呼出元 1件 [`0089314c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00893/0089314c.md) · 呼出先 12件 [`00497a48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00497/00497a48.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.00% / 新版 79.00%

CFGの説明率　旧版 63.64% / 新版 73.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3920c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b39244"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b39248"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3920c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b39238",
      "READ",
      [
        "storage",
        "002a6f7d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b3923c",
      "READ",
      [
        "storage",
        "002a6f87",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b39634",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b39660",
      "READ",
      [
        "storage",
        "002a7059",
        null,
        "string"
      ]
    ],
    [
      "00b39664",
      "READ",
      [
        "storage",
        "002a7063",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3920c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b391ec.md#insn-00b3920c) · [`00b39244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b391ec.md#insn-00b39244) · [`00b39248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b391ec.md#insn-00b39248)

~~~diff
- 00b3920c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b3920c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b3920c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b3920c bytes a8831ff8
- 00b39244 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b39244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b39244 bytes e00b00f9
- 00b39248 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b39248 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b39248 bytes 0000803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fb87053bfa89354650f984f20e99295"></a>

### [`00b3a6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a6e4.md) → [`00b3ab0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3ab0c.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementRequestSuccess

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00b3b3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b3f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00b3b820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b820.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 75.68% / 新版 75.68%

CFGの説明率　旧版 60.00% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3a728"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3a730"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b3ab50"
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
      "unmatched:00b3a710",
      "PARAM",
      [
        "storage",
        "01124df8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b3a718",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b3b820"
      ]
    ],
    [
      "unmatched:00b3a728",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3ab6c"
      ]
    ]
  ],
  "added": [
    [
      "00b3ab38",
      "PARAM",
      [
        "storage",
        "011251f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3ab40",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b3b820"
      ]
    ],
    [
      "00b3ab50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3ab6c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3a718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a6e4.md#insn-00b3a718) · [`00b3a728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a6e4.md#insn-00b3a728) · [`00b3a730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a6e4.md#insn-00b3a730)

~~~diff
- 00b3a718 ["INT_ADD", "register:40f0:8", ["const:b3a718:8", "const:4:8"]]
- 00b3a718 ["CALL", null, ["callee:00b3b820:8"]]
- 00b3a718 bytes 38030094
- 00b3a728 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00b3a728 bytes e0000054
- 00b3a730 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b3a730 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b3a730 bytes a00000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-465db68793dc3d3f01d2ef71f0c700b1"></a>

### [`00b3aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aa30.md) → [`00b3ae58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3ae58.md) Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyPlacementDismissed

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00589914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589914.md) [`00b3b4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b4fc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00589954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589954.md) [`00b3b924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b924.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 78.38% / 新版 78.38%

CFGの説明率　旧版 54.55% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3aa74"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b3ae9c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3aa64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3aa5c",
      "PARAM",
      [
        "storage",
        "01124e10",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b3aa64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b3b924"
      ]
    ],
    [
      "unmatched:00b3aa74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3aeb8"
      ]
    ]
  ],
  "added": [
    [
      "00b3ae84",
      "PARAM",
      [
        "storage",
        "01125210",
        null,
        "undefined8"
      ]
    ],
    [
      "00b3ae8c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00b3b924"
      ]
    ],
    [
      "00b3ae9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3aeb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3aa64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aa30.md#insn-00b3aa64) · [`00b3aa74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aa30.md#insn-00b3aa74) · [`00b3aa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aa30.md#insn-00b3aa8c)

~~~diff
- 00b3aa64 ["INT_ADD", "register:40f0:8", ["const:b3aa64:8", "const:4:8"]]
- 00b3aa64 ["CALL", null, ["callee:00b3b924:8"]]
- 00b3aa64 bytes a6020094
- 00b3aa74 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b3aa74 bytes e0000054
- 00b3aa8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3aa8c ["INT_ADD", "register:40f0:8", ["const:b3aa8c:8", "const:4:8"]]
- 00b3aa8c ["CALLIND", null, ["register:0:8"]]
- 00b3aa8c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a075ce90678282a74b7d9738cd906bb"></a>

### [`00b3aaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aaf4.md) → [`00b3af1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3af1c.md) FUN_00b3af1c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b38ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38ae0.md) [`00b3aaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aaf4.md) · 呼出先 2件 [`00b3aaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aaf4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00b38f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b38f08.md) [`00b3af1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3af1c.md) · 呼出先 2件 [`00b3af1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3af1c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 38.46% / 新版 34.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ab64"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ab68"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ab90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3ab64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3af9c"
      ]
    ],
    [
      "unmatched:00b3ab68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3afb0"
      ]
    ],
    [
      "unmatched:00b3ab90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3afc8"
      ]
    ]
  ],
  "added": [
    [
      "00b3af8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3af9c"
      ]
    ],
    [
      "00b3af90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3afb0"
      ]
    ],
    [
      "00b3afb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3afc8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3ab64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aaf4.md#insn-00b3ab64) · [`00b3ab68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aaf4.md#insn-00b3ab68) · [`00b3ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aaf4.md#insn-00b3ab90)

~~~diff
- 00b3ab64 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00b3ab64 bytes 80000054
- 00b3ab68 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b3ab68 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00b3ab68 bytes 000100b4
- 00b3ab90 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 00b3ab90 bytes 80000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09acd760a7a8fe178e3d1eccfcd3bb98"></a>

### [`00b3abd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md) → [`00b3affc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3affc.md) FUN_00b3affc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b38ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b38/00b38ae8.md) [`00b3abd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md) · 呼出先 2件 [`00b3abd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00b38f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b38/00b38f10.md) [`00b3affc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3affc.md) · 呼出先 2件 [`00b3affc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3affc.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 47.37% / 新版 36.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ac10"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b3b038"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ac60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3ac10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3b04c"
      ]
    ],
    [
      "unmatched:00b3ac60",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b3b038",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3b04c"
      ]
    ],
    [
      "00b3b088",
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

- 旧版 [`00b3ac10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md#insn-00b3ac10) · [`00b3ac60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md#insn-00b3ac60)
- 新版 `00b3b038`（命令位置の公開資料なし）

~~~diff
- 00b3ac10 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 00b3ac10 bytes a0000054
- 00b3ac60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3ac60 ["INT_ADD", "register:40f0:8", ["const:b3ac60:8", "const:4:8"]]
- 00b3ac60 ["CALLIND", null, ["register:0:8"]]
- 00b3ac60 bytes 00013fd6
+ 00b3b038 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
+ 00b3b038 bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0f95ee9bb0dab7105cf8ae6db53a0ee"></a>

### [`00b3adc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3adc8.md) → [`00b3b1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b1f0.md) FUN_00b3b1f0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b3ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3ac84.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00b3b0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b0ac.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 4.17% / 新版 5.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3adc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3adc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3adcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3adc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3adcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3add0",
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
      "00b3b1f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b3b1f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b3b1f8",
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

- 旧版 [`00b3adc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3adc8.md#insn-00b3adc8) · [`00b3adcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3adc8.md#insn-00b3adcc) · [`00b3add0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3adc8.md#insn-00b3add0)

~~~diff
- 00b3adc8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b3adc8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b3adc8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b3adc8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b3adc8 bytes fd7bbba9
- 00b3adcc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b3adcc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b3adcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b3adcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3adcc bytes fa6701a9
- 00b3add0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b3add0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b3add0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b3add0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3add0 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a1f96db9cf73e9f9a066810f8146d93"></a>

### [`00b3aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aecc.md) → [`00b3b2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b2f4.md) FUN_00b3b2f4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.09% / 新版 89.09%

CFGの説明率　旧版 40.00% / 新版 41.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3af38"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3af3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b3b360"
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
      "unmatched:00b3af38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3b370"
      ]
    ],
    [
      "unmatched:00b3af3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3b384"
      ]
    ],
    [
      "00b3b36c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b3af50"
      ]
    ]
  ],
  "added": [
    [
      "00b3b360",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3b370"
      ]
    ],
    [
      "00b3b364",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3b384"
      ]
    ],
    [
      "00b3b36c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3b378"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3af38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aecc.md#insn-00b3af38) · [`00b3af3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aecc.md#insn-00b3af3c) · [`00b3af58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aecc.md#insn-00b3af58)

~~~diff
- 00b3af38 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00b3af38 bytes 80000054
- 00b3af3c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b3af3c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b3af3c bytes 000100b4
- 00b3af58 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3af58 ["INT_ADD", "register:40f0:8", ["const:b3af58:8", "const:4:8"]]
- 00b3af58 ["CALLIND", null, ["register:0:8"]]
- 00b3af58 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-224cb3be593b8d55f2eb9ca47f200cd1"></a>

### [`00b3b290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b290.md) → [`00b3b6b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b6b8.md) FUN_00b3b6b8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b39fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b39/00b39fc8.md) [`00b3a190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a190.md) · 呼出先 1件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 2件 [`00b3a3f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3a3f0.md) [`00b3a5b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3a5b8.md) · 呼出先 1件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.65% / 新版 78.65%

CFGの説明率　旧版 70.59% / 新版 48.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3b3a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3b3a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3b7c8"
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
      "unmatched:00b3b39c",
      "READ",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3b3b8",
      "READ",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3b360",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b3b7c4",
      "READ",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b3b7e0",
      "READ",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b3b788",
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

- 旧版 [`00b3b360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b290.md#insn-00b3b360) · [`00b3b370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b290.md#insn-00b3b370) · [`00b3b398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b290.md#insn-00b3b398)

~~~diff
- 00b3b360 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b360 ["INT_ADD", "register:40f0:8", ["const:b3b360:8", "const:4:8"]]
- 00b3b360 ["CALLIND", null, ["register:0:8"]]
- 00b3b360 bytes 00013fd6
- 00b3b370 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b370 ["INT_ADD", "register:40f0:8", ["const:b3b370:8", "const:4:8"]]
- 00b3b370 ["CALLIND", null, ["register:0:8"]]
- 00b3b370 bytes 00013fd6
- 00b3b398 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3b398 ["INT_ADD", "register:40f0:8", ["const:b3b398:8", "const:4:8"]]
- 00b3b398 ["CALLIND", null, ["register:0:8"]]
- 00b3b398 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e2e7f892b46a564328cbe7d4e7439d1"></a>

### [`00b3b4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b4fc.md) → [`00b3b924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3b924.md) FUN_00b3b924

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b3a970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3a970.md) [`00b3aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3aa30.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`00b3ad98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3ad98.md) [`00b3ae58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3a/00b3ae58.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 70.77% / 新版 70.77%

CFGの説明率　旧版 6.25% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3b554"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3b5b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3b5b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3b5c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58050"
      ]
    ]
  ],
  "added": [
    [
      "00b3b9ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58050"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3b554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b4fc.md#insn-00b3b554) · [`00b3b5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b4fc.md#insn-00b3b5b4) · [`00b3b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3b4fc.md#insn-00b3b5b8)

~~~diff
- 00b3b554 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3b554 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3b554 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b3b554 ["COPY", "register:40c8:8", ["tmp:0:8"]]
- 00b3b554 bytes 39018a9a
- 00b3b5b4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b3b5b4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3b5b4 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b3b5b4 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00b3b5b4 bytes 01018b9a
- 00b3b5b8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b3b5b8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3b5b8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3b5b8 ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00b3b5b8 bytes 5701899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8fa5454ba0767233a58eae423cc7d56"></a>

### [`00b3bee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bee4.md) → [`00b3c30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3c30c.md) FUN_00b3c30c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`00767f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767f54.md) [`00768564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768564.md) [`007687b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007687b0.md) [`00768ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768ba8.md) · 呼出先 5件 [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) [`00b3c040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c040.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)
- 新版 呼出元 10件 [`00764ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00764/00764ee0.md) [`00767f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00767/00767f94.md) [`007685a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007685a4.md) [`007687f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/007687f0.md) [`00768be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00768/00768be8.md) · 呼出先 5件 [`004499b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00449/004499b8.md) [`00b3c468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3c/00b3c468.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.75% / 新版 92.75%

CFGの説明率　旧版 41.18% / 新版 41.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3bf6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3c394"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3bf1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3bf1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3c378"
      ]
    ],
    [
      "unmatched:00b3bf74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3c3c8"
      ]
    ]
  ],
  "added": [
    [
      "00b3c344",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3c378"
      ]
    ],
    [
      "00b3c39c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3c3c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3bf1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bee4.md#insn-00b3bf1c) · [`00b3bf6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bee4.md#insn-00b3bf6c) · [`00b3bf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3bee4.md#insn-00b3bf70)

~~~diff
- 00b3bf1c ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b3bf1c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b3bf1c bytes b50100b4
- 00b3bf6c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:10:8"]]
- 00b3bf6c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b3bf6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b3bf6c bytes bf0a00f9
- 00b3bf70 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b3bf70 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b3bf70 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3bf70 ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00b3bf70 bytes 5701899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2e55b2f23f8d53028c9919fc6fd5757"></a>

### [`00b3dfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3dfe8.md) → [`00b3e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3e/00b3e410.md) FUN_00b3e410

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 40件 [`005cc6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc6a4.md) [`00606494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606494.md) [`006766ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/006766ec.md) [`006794f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00679/006794f4.md) [`006d1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 40件 [`005cc6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005cc/005cc6e4.md) [`006064d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00606/006064d4.md) [`0067672c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067672c.md) [`00679534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00679/00679534.md) [`006d1fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d1fe4.md) · 呼出先 3件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.67% / 新版 82.67%

CFGの説明率　旧版 25.00% / 新版 24.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3dfe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3dfe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3dfec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3dfe8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3dfec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3dff0",
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
      "00b3e410",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b3e414",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b3e418",
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

- 旧版 [`00b3dfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3dfe8.md#insn-00b3dfe8) · [`00b3dfec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3dfe8.md#insn-00b3dfec) · [`00b3dff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3dfe8.md#insn-00b3dff0)

~~~diff
- 00b3dfe8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b3dfe8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b3dfe8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b3dfe8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b3dfe8 bytes fd7bbca9
- 00b3dfec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b3dfec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b3dfec bytes f70b00f9
- 00b3dff0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b3dff0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b3dff0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b3dff0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3dff0 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-135515caa03cc0ecefc08996607e5f2b"></a>

### [`00b3f2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f2fc.md) → [`00b3f724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3f724.md) FUN_00b3f724

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`006d8cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8cc0.md) [`0075a3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075a/0075a3d8.md) [`009850f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/009850f8.md) [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 1件 [`00b3dfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3dfe8.md)
- 新版 呼出元 6件 [`006d8d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d8/006d8d00.md) [`0075a418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0075a/0075a418.md) [`00985294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985294.md) [`00985418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00985/00985418.md) [`0098dc08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0098d/0098dc08.md) · 呼出先 1件 [`00b3e410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3e/00b3e410.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 68.00% / 新版 70.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f374"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b3f79c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b3f374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f2fc.md#insn-00b3f374) · [`00b3f31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f2fc.md#insn-00b3f31c)
- 新版 `00b3f79c`（命令位置の公開資料なし） · `00b3f744`（命令位置の公開資料なし）

~~~diff
- 00b3f374 ["COPY", "tmp:0:1", ["register:101:1"]]
- 00b3f374 ["COPY", "tmp:1:1", ["const:0:1"]]
- 00b3f374 ["INT_AND", "tmp:2:1", ["tmp:1:1", "const:8:1"]]
- 00b3f374 ["INT_EQUAL", "register:100:1", ["tmp:2:1", "const:8:1"]]
- 00b3f374 bytes 0009407a
+ 00b3f79c ["COPY", "tmp:0:1", ["register:101:1"]]
+ 00b3f79c ["COPY", "tmp:1:1", ["const:0:1"]]
+ 00b3f79c ["INT_AND", "tmp:2:1", ["tmp:1:1", "const:8:1"]]
+ 00b3f79c ["INT_EQUAL", "register:100:1", ["tmp:2:1", "const:8:1"]]
+ 00b3f79c bytes 0009407a
- 00b3f31c ["INT_ADD", "register:40f0:8", ["const:b3f31c:8", "const:4:8"]]
- 00b3f31c ["CALL", null, ["callee:00b3e410:8"]]
+ 00b3f744 ["INT_ADD", "register:40f0:8", ["const:b3f744:8", "const:4:8"]]
+ 00b3f744 ["CALL", null, ["callee:00b3e410:8"]]
- 00b3f31c bytes 33fbff97
+ 00b3f744 bytes 33fbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d72ed8e38e4a63aeedfec585dc98330"></a>

### [`00b3f560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f560.md) → [`00b3f988`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3f988.md) FUN_00b3f988

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f584"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f584"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3f9ac"
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
      "unmatched:00b3f584",
      "DATA",
      [
        "storage",
        "00c8f168",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00b3f588",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b3f58c",
      "DATA",
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
      "00b3f9ac",
      "DATA",
      [
        "storage",
        "00c8f568",
        null,
        "undefined *"
      ]
    ],
    [
      "00b3f9b0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b3f9b4",
      "DATA",
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

- 旧版 [`00b3f584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f560.md#insn-00b3f584) · [`00b3f590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f560.md#insn-00b3f590)
- 新版 `00b3f9ac`（命令位置の公開資料なし）

~~~diff
- 00b3f584 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b3f584 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b3f584 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00b3f584 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3f584 bytes 082400a9
- 00b3f590 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b3f590 ["RETURN", null, ["register:0:8"]]
- 00b3f590 bytes c0035fd6
+ 00b3f9ac ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b3f9ac ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00b3f9ac ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00b3f9ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b3f9ac bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a962e162c5ca57133a129661ca4e6bb9"></a>

### [`00b3f594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f594.md) → [`00b3f9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3f9bc.md) FUN_00b3f9bc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f5a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3f5a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b3f9c8"
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
      "unmatched:00b3f5a0",
      "DATA",
      [
        "storage",
        "00c8f168",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b3f9c8",
      "DATA",
      [
        "storage",
        "00c8f568",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3f5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f594.md#insn-00b3f5a0) · [`00b3f5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3f594.md#insn-00b3f5a4)
- 新版 `00b3f9c8`（命令位置の公開資料なし）

~~~diff
- 00b3f5a0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b3f5a0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b3f5a0 ["COPY", "tmp:2:8", ["register:4008:8"]]
- 00b3f5a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3f5a0 bytes 292000a9
- 00b3f5a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b3f5a4 ["RETURN", null, ["register:0:8"]]
- 00b3f5a4 bytes c0035fd6
+ 00b3f9c8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b3f9c8 ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00b3f9c8 ["COPY", "tmp:2:8", ["register:4008:8"]]
+ 00b3f9c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b3f9c8 bytes 292000a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c4bf8a14b8ff1ad33acbbd9718550f8"></a>

### [`00b3fa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa48.md) → [`00b3fe70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3fe70.md) FUN_00b3fe70

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b3ff84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md) · 呼出先 2件 [`00c5a560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a560.md) [`00c5a860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a860.md)
- 新版 呼出元 1件 [`00b403ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b403ac.md) · 呼出先 2件 [`00c5a960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a960.md) [`00c5ac60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3fa60"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b3fe88"
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
      "unmatched:00b3fa60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3fe94"
      ]
    ]
  ],
  "added": [
    [
      "00b3fe88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b3fe94"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3fa60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa48.md#insn-00b3fa60) · [`00b3fa58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa48.md#insn-00b3fa58)
- 新版 `00b3fe88`（命令位置の公開資料なし） · `00b3fe80`（命令位置の公開資料なし）

~~~diff
- 00b3fa60 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b3fa60 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b3fa60 bytes 61000054
+ 00b3fe88 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b3fe88 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b3fe88 bytes 61000054
- 00b3fa58 ["INT_ADD", "register:40f0:8", ["const:b3fa58:8", "const:4:8"]]
- 00b3fa58 ["CALL", null, ["callee:00c5ac60:8"]]
+ 00b3fe80 ["INT_ADD", "register:40f0:8", ["const:b3fe80:8", "const:4:8"]]
+ 00b3fe80 ["CALL", null, ["callee:00c5ac60:8"]]
- 00b3fa58 bytes 826b0494
+ 00b3fe80 bytes 786b0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbe7d1009ce535a9cf91869b0ff55040"></a>

### [`00b3fb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fb3c.md) → [`00b3ff64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3ff64.md) _ZN8firebase9analytics8internal10FutureData3GetEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8b0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5acb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5acb0.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3fb48"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b3ff70"
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
      "unmatched:00b3fb40",
      "READ",
      [
        "storage",
        "00c9b2a0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b3fb44",
      "READ",
      [
        "storage",
        "01124f28",
        "_ZN8firebase9analytics8internal10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b3ff68",
      "READ",
      [
        "storage",
        "00c9b6a0",
        null,
        "pointer"
      ]
    ],
    [
      "00b3ff6c",
      "READ",
      [
        "storage",
        "01125328",
        "_ZN8firebase9analytics8internal10FutureData14s_future_data_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3fb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fb3c.md#insn-00b3fb48) · [`00b3fb3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fb3c.md#insn-00b3fb3c)
- 新版 `00b3ff70`（命令位置の公開資料なし）

~~~diff
- 00b3fb48 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b3fb48 ["RETURN", null, ["register:0:8"]]
- 00b3fb48 bytes c0035fd6
+ 00b3ff70 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b3ff70 ["RETURN", null, ["register:0:8"]]
+ 00b3ff70 bytes c0035fd6
- 00b3fb3c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b3fb3c bytes e80a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cbfea13cb3a93c6fdb61b43207accc8"></a>

### [`00b3fd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fd98.md) → [`00b401c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b401c0.md) _ZNSt6__ndk113__vector_baseIN8firebase10FutureBaseENS_9allocatorIS2_EEED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a920.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a600.md) [`00c5a610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a610.md) [`00c5a690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a690.md) [`00c5a6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6a0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa90.md) [`00c5aaa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaa0.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 38.46% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3fdac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3fdbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b401d4"
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
      "unmatched:00b3fdac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40250"
      ]
    ],
    [
      "unmatched:00b3fdbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40260"
      ]
    ],
    [
      "unmatched:00b3fdf4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b401d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40250"
      ]
    ],
    [
      "00b401e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40260"
      ]
    ],
    [
      "00b4021c",
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

- 旧版 [`00b3fdac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fd98.md#insn-00b3fdac) · [`00b3fdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fd98.md#insn-00b3fdbc) · [`00b3fdf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fd98.md#insn-00b3fdf4)

~~~diff
- 00b3fdac ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b3fdac ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b3fdac bytes f50300b4
- 00b3fdbc ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00b3fdbc bytes e0030054
- 00b3fdf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b3fdf4 ["INT_ADD", "register:40f0:8", ["const:b3fdf4:8", "const:4:8"]]
- 00b3fdf4 ["CALLIND", null, ["register:0:8"]]
- 00b3fdf4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50caa8c44cd3ff6974b5ea035f44cd48"></a>

### [`00b3fe98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md) → [`00b402c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402c0.md) FUN_00b402c0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 11件 [`00b3fe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe84.md) [`00bb7f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7f60.md) [`00bb8174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb8174.md) [`00bb82b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb82b4.md) [`00bb83f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb83f4.md) · 呼出先 4件 [`00b3fee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fee8.md) [`00c378a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378a4.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 11件 [`00b402ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b402ac.md) [`00bb8388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8388.md) [`00bb859c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb859c.md) [`00bb86dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb86dc.md) [`00bb881c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb881c.md) · 呼出先 4件 [`00b40310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40310.md) [`00c37ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ccc.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3fed0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b402f8"
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
      "unmatched:00b3fec4",
      "READ",
      [
        "storage",
        "00c9a790",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b3fec4",
      "PARAM",
      [
        "storage",
        "00c963d8",
        "_ZTISt12length_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00b3fec8",
      "READ",
      [
        "storage",
        "00c9a798",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b402ec",
      "READ",
      [
        "storage",
        "00c9ab90",
        null,
        "pointer"
      ]
    ],
    [
      "00b402ec",
      "PARAM",
      [
        "storage",
        "00c967d8",
        "_ZTISt12length_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00b402f0",
      "READ",
      [
        "storage",
        "00c9ab98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3fed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md#insn-00b3fed0) · [`00b3feac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fe98.md#insn-00b3feac)
- 新版 `00b402f8`（命令位置の公開資料なし） · `00b402d4`（命令位置の公開資料なし）

~~~diff
- 00b3fed0 ["INT_ADD", "register:40f0:8", ["const:b3fed0:8", "const:4:8"]]
- 00b3fed0 ["CALL", null, ["callee:00c57f10:8"]]
- 00b3fed0 bytes 105f0494
+ 00b402f8 ["INT_ADD", "register:40f0:8", ["const:b402f8:8", "const:4:8"]]
+ 00b402f8 ["CALL", null, ["callee:00c57f10:8"]]
+ 00b402f8 bytes 065f0494
- 00b3feac ["INT_ADD", "register:40f0:8", ["const:b3feac:8", "const:4:8"]]
- 00b3feac ["CALL", null, ["callee:00c57ef0:8"]]
+ 00b402d4 ["INT_ADD", "register:40f0:8", ["const:b402d4:8", "const:4:8"]]
+ 00b402d4 ["CALL", null, ["callee:00c57ef0:8"]]
- 00b3feac bytes 115f0494
+ 00b402d4 bytes 075f0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb89051f8725610a9194ef110c56764b"></a>

### [`00b3ff84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md) → [`00b403ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b403ac.md) _INIT_277

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b3fa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa48.md) [`00b3fa7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3fa7c.md) [`00c5a7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a7c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b3fe70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3fe70.md) [`00b3fea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3f/00b3fea4.md) [`00c5abc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5abc0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ffa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ffa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ffa8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3ff94",
      "PARAM",
      [
        "storage",
        "01124f08",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b3ffa4",
      "WRITE",
      [
        "storage",
        "01124f08",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b3ffa4",
      "DATA",
      [
        "storage",
        "002a8290",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b403bc",
      "PARAM",
      [
        "storage",
        "01125308",
        null,
        "undefined8"
      ]
    ],
    [
      "00b403cc",
      "WRITE",
      [
        "storage",
        "01125308",
        null,
        "undefined8"
      ]
    ],
    [
      "00b403cc",
      "DATA",
      [
        "storage",
        "002a835d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3ffa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md#insn-00b3ffa4) · [`00b3ffa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md#insn-00b3ffa8) · [`00b3ffac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ff84.md#insn-00b3ffac)

~~~diff
- 00b3ffa4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b3ffa4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b3ffa4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00b3ffa4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b3ffa4 bytes 082400a9
- 00b3ffa8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00b3ffa8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b3ffa8 bytes 0a0800f9
- 00b3ffac ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b3ffac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b3ffac ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:18:8"]]
- 00b3ffac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b3ffac bytes 1f600039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c56d5ce008f62ebce38122b17c1a861"></a>

### [`00b3ffb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ffb4.md) → [`00b403dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b403dc.md) _ZN8firebase9analytics9analytics19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ffe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40408"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b3ffc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b3ffc4",
      "READ",
      [
        "storage",
        "01124f30",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b3ffc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4040c"
      ]
    ],
    [
      "unmatched:00b3ffd4",
      "PARAM",
      [
        "storage",
        "002a6fd3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b403ec",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b403f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4040c"
      ]
    ],
    [
      "00b403fc",
      "PARAM",
      [
        "storage",
        "002a70af",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3ffc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ffb4.md#insn-00b3ffc8) · [`00b3ffd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ffb4.md#insn-00b3ffd8) · [`00b3ffe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3f/00b3ffb4.md#insn-00b3ffe0)

~~~diff
- 00b3ffc8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b3ffc8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b3ffc8 bytes e80000b5
- 00b3ffd8 ["INT_ADD", "register:40f0:8", ["const:b3ffd8:8", "const:4:8"]]
- 00b3ffd8 ["CALL", null, ["callee:00c5af10:8"]]
- 00b3ffd8 bytes ce6a0494
- 00b3ffe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f30:8"]]
- 00b3ffe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b3ffe0 bytes 609a07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b7907e1104d62a10f634ddc9aa664e8"></a>

### [`00b400c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b400c8.md) → [`00b404f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b404f0.md) _ZN8firebase9analytics9analytics15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40120"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40548"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40108"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b40504",
      "READ",
      [
        "storage",
        "01124f38",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b400fc",
      "READ",
      [
        "storage",
        "01124f30",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b40120",
      "WRITE",
      [
        "storage",
        "01124f38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b40504",
      "READ",
      [
        "storage",
        "01125338",
        null,
        "undefined1"
      ]
    ],
    [
      "00b40524",
      "READ",
      [
        "storage",
        "01125330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40548",
      "WRITE",
      [
        "storage",
        "01125338",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b400c8.md#insn-00b40108) · [`00b40120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b400c8.md#insn-00b40120)
- 新版 `00b40530`（命令位置の公開資料なし）

~~~diff
- 00b40108 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b40108 ["INT_ADD", "register:40f0:8", ["const:b40108:8", "const:4:8"]]
- 00b40108 ["CALLIND", null, ["register:0:8"]]
- 00b40108 bytes 00013fd6
- 00b40120 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b40120 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:f38:8"]]
- 00b40120 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b40120 bytes a0e23c39
+ 00b40530 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b40530 ["INT_ADD", "register:40f0:8", ["const:b40530:8", "const:4:8"]]
+ 00b40530 ["CALLIND", null, ["register:0:8"]]
+ 00b40530 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08eb6f15aea1f62a1db5d3986f1a5978"></a>

### [`00b402c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b402c0.md) → [`00b406e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b406e8.md) _ZN8firebase9analytics9analytics10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b402c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b402c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b402c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b402c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b402c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b406fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b402e4"
      ]
    ]
  ],
  "added": [
    [
      "00b406e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b406ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b406fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4070c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b402c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b402c0.md#insn-00b402c0) · [`00b402c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b402c0.md#insn-00b402c4) · [`00b402e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b402c0.md#insn-00b402e0)

~~~diff
- 00b402c0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b402c0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b402c0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b402c0 bytes f30f1ef8
- 00b402c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b402c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b402c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b402c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b402c4 bytes fd7b01a9
- 00b402e0 ["INT_ADD", "register:40f0:8", ["const:b402e0:8", "const:4:8"]]
- 00b402e0 ["CALL", null, ["callee:00c5b000:8"]]
- 00b402e0 bytes 486a0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99be8881540a15e82046cd9aeb6a6db0"></a>

### [`00b4055c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4055c.md) → [`00b40984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40984.md) _ZN8firebase9analytics22analytics_consent_type11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4055c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40560"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40560"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4055c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b40560",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40998",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b40580"
      ]
    ]
  ],
  "added": [
    [
      "00b40984",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b40988",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40998",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b409a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4055c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4055c.md#insn-00b4055c) · [`00b40560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4055c.md#insn-00b40560) · [`00b4057c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b4055c.md#insn-00b4057c)

~~~diff
- 00b4055c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b4055c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b4055c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4055c bytes f30f1ef8
- 00b40560 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b40560 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b40560 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b40560 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b40560 bytes fd7b01a9
- 00b4057c ["INT_ADD", "register:40f0:8", ["const:b4057c:8", "const:4:8"]]
- 00b4057c ["CALL", null, ["callee:00c5b000:8"]]
- 00b4057c bytes a1690494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec57c994731150fe3e829370030f8087"></a>

### [`00b40608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40608.md) → [`00b40a30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40a30.md) _ZN8firebase9analytics22analytics_consent_type10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4060c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4060c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b40608",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4060c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40a44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4062c"
      ]
    ]
  ],
  "added": [
    [
      "00b40a30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b40a34",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40a44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40a54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40608.md#insn-00b40608) · [`00b4060c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40608.md#insn-00b4060c) · [`00b40628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40608.md#insn-00b40628)

~~~diff
- 00b40608 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b40608 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b40608 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b40608 bytes f30f1ef8
- 00b4060c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b4060c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b4060c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4060c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4060c bytes fd7b01a9
- 00b40628 ["INT_ADD", "register:40f0:8", ["const:b40628:8", "const:4:8"]]
- 00b40628 ["CALL", null, ["callee:00c5b000:8"]]
- 00b40628 bytes 76690494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a60d928744d0333848b747aaa7dabff"></a>

### [`00b40644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40644.md) → [`00b40a6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40a6c.md) _ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40648"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40648"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b40644",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b40648",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b40654",
      "READ",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40a6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b40a70",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40a7c",
      "READ",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40644.md#insn-00b40644) · [`00b40648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40644.md#insn-00b40648) · [`00b40658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40644.md#insn-00b40658)

~~~diff
- 00b40644 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b40644 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b40644 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b40644 bytes f30f1ef8
- 00b40648 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b40648 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b40648 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b40648 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b40648 bytes fd7b01a9
- 00b40658 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b40658 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b40658 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-826fe33930c7e8b6c8b48ef898b48991"></a>

### [`00b40684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40684.md) → [`00b40aac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40aac.md) _ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40684"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40688"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b40684",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b40688",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b40694",
      "READ",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b40aac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b40ab0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40abc",
      "READ",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40684.md#insn-00b40684) · [`00b40688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40684.md#insn-00b40688) · [`00b40698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40684.md#insn-00b40698)

~~~diff
- 00b40684 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b40684 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b40684 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b40684 bytes f30f1ef8
- 00b40688 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b40688 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b40688 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b40688 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b40688 bytes fd7b01a9
- 00b40698 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b40698 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b40698 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c982bff87ed6e2f92ae3e63925da26a3"></a>

### [`00b40758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40758.md) → [`00b40b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40b80.md) _ZN8firebase9analytics24analytics_consent_status15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 10.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b407b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40bd8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40798"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b40b94",
      "READ",
      [
        "storage",
        "01124fe0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b4078c",
      "READ",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b407b0",
      "WRITE",
      [
        "storage",
        "01124fe0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b40b94",
      "READ",
      [
        "storage",
        "011253e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b40bb4",
      "READ",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40bd8",
      "WRITE",
      [
        "storage",
        "011253e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40758.md#insn-00b40798) · [`00b407b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40758.md#insn-00b407b0)
- 新版 `00b40bc0`（命令位置の公開資料なし）

~~~diff
- 00b40798 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b40798 ["INT_ADD", "register:40f0:8", ["const:b40798:8", "const:4:8"]]
- 00b40798 ["CALLIND", null, ["register:0:8"]]
- 00b40798 bytes 00013fd6
- 00b407b0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b407b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:fe0:8"]]
- 00b407b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b407b0 bytes a0823f39
+ 00b40bc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b40bc0 ["INT_ADD", "register:40f0:8", ["const:b40bc0:8", "const:4:8"]]
+ 00b40bc0 ["CALLIND", null, ["register:0:8"]]
+ 00b40bc0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f7b3f866965b0d2d6ef8b651c92938f"></a>

### [`00b407c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b407c4.md) → [`00b40bec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40bec.md) _ZN8firebase9analytics24analytics_consent_status12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 35.71% / 新版 35.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40820"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b40c28"
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
      "00b40c00",
      "READ",
      [
        "storage",
        "01124fd8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b407dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b40824"
      ]
    ],
    [
      "unmatched:00b407e4",
      "READ",
      [
        "storage",
        "01124fe0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b40c00",
      "READ",
      [
        "storage",
        "011253d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b40c04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40c4c"
      ]
    ],
    [
      "00b40c0c",
      "READ",
      [
        "storage",
        "011253e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b407dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b407c4.md#insn-00b407dc) · [`00b407fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b407c4.md#insn-00b407fc) · [`00b40800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b407c4.md#insn-00b40800)

~~~diff
- 00b407dc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b407dc ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b407dc bytes 410200b4
- 00b407fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b407fc ["INT_ADD", "register:40f0:8", ["const:b407fc:8", "const:4:8"]]
- 00b407fc ["CALLIND", null, ["register:0:8"]]
- 00b407fc bytes 00013fd6
- 00b40800 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b40800 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b40800 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:fe0:8"]]
- 00b40800 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b40800 bytes bf823f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0141ff73fe952a2421d01018ce407450"></a>

### [`00b408a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b408a4.md) → [`00b40ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b40/00b40ccc.md) _ZN8firebase9analytics24analytics_consent_status11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b408a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b408a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b408a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b408a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b408a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40ce0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b408c8"
      ]
    ]
  ],
  "added": [
    [
      "00b40ccc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b40cd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b40ce0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b40cf0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b408a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b408a4.md#insn-00b408a4) · [`00b408a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b408a4.md#insn-00b408a8) · [`00b408c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b408a4.md#insn-00b408c4)

~~~diff
- 00b408a4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b408a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b408a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b408a4 bytes f30f1ef8
- 00b408a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b408a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b408a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b408a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b408a8 bytes fd7b01a9
- 00b408c4 ["INT_ADD", "register:40f0:8", ["const:b408c4:8", "const:4:8"]]
- 00b408c4 ["CALL", null, ["callee:00c5b000:8"]]
- 00b408c4 bytes cf680494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f049db5845b81817b7c31f339ac5c28"></a>

### [`00b40d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40d1c.md) → [`00b41144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41144.md) _ZN8firebase9analytics8internal13IsInitializedEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5a8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8e0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5ace0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ace0.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b40d2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b41154"
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
      "unmatched:00b40d20",
      "READ",
      [
        "storage",
        "01125000",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b41148",
      "READ",
      [
        "storage",
        "01125400",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b40d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40d1c.md#insn-00b40d2c) · [`00b40d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b40/00b40d1c.md#insn-00b40d1c)
- 新版 `00b41154`（命令位置の公開資料なし）

~~~diff
- 00b40d2c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b40d2c ["RETURN", null, ["register:0:8"]]
- 00b40d2c bytes c0035fd6
+ 00b41154 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b41154 ["RETURN", null, ["register:0:8"]]
+ 00b41154 bytes c0035fd6
- 00b40d1c ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00b40d1c bytes 282f00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77d85a88573bddd9d4d0e55f5e160353"></a>

### [`00b412ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b412ac.md) → [`00b416d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b416d4.md) _ZN8firebase9analytics11AddToBundleEP7_JNIEnvP8_jobjectPKcS6_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.49% / 新版 80.49%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b412ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b412ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b412b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b412ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b412b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b412b4",
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
      "00b416d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b416d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b416dc",
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

- 旧版 [`00b412ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b412ac.md#insn-00b412ac) · [`00b412b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b412ac.md#insn-00b412b0) · [`00b412b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b412ac.md#insn-00b412b4)

~~~diff
- 00b412ac ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b412ac ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b412ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b412ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b412ac bytes f657bda9
- 00b412b0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b412b0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b412b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b412b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b412b0 bytes f44f01a9
- 00b412b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b412b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b412b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b412b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b412b4 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f98c10770920e55e626dfacec962bf7d"></a>

### [`00b41448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41448.md) → [`00b41870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41870.md) _ZN8firebase9analytics20AddArrayListToBundleEP7_JNIEnvP8_jobjectPKcS4_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.67% / 新版 76.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41448"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4144c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b41448",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b4144c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b41450",
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
      "00b41870",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b41874",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b41878",
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

- 旧版 [`00b41448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41448.md#insn-00b41448) · [`00b4144c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41448.md#insn-00b4144c) · [`00b41450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b41448.md#insn-00b41450)

~~~diff
- 00b41448 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b41448 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b41448 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b41448 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b41448 bytes f657bda9
- 00b4144c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b4144c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b4144c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b4144c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b4144c bytes f44f01a9
- 00b41450 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b41450 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b41450 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b41450 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b41450 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5422572c26d3ac43c713f030c01a88a"></a>

### [`00b414c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b414c0.md) → [`00b418e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b418e8.md) _ZN8firebase9analytics17AddBundleToBundleEP7_JNIEnvP8_jobjectPKcS4_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00574cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574cac.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00574cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00574/00574cec.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b414e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b41910"
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
      "unmatched:00b414e8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b41910",
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

- 旧版 [`00b414e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b414c0.md#insn-00b414e8) · [`00b414e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b414c0.md#insn-00b414e0)
- 新版 `00b41910`（命令位置の公開資料なし）

~~~diff
- 00b414e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b414e8 ["INT_ADD", "register:40f0:8", ["const:b414e8:8", "const:4:8"]]
- 00b414e8 ["CALLIND", null, ["register:0:8"]]
- 00b414e8 bytes 00013fd6
+ 00b41910 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b41910 ["INT_ADD", "register:40f0:8", ["const:b41910:8", "const:4:8"]]
+ 00b41910 ["CALLIND", null, ["register:0:8"]]
+ 00b41910 bytes 00013fd6
- 00b414e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:538:8"]]
- 00b414e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b414e0 bytes 089d42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cd2c7ffba5c2815c085ba87fd9edb29"></a>

### [`00b4163c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b4163c.md) → [`00b41a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b41/00b41a64.md) _ZN8firebase9analytics11MapToBundleEP7_JNIEnvRKNSt6__ndk13mapINS_7VariantES5_NS3_4lessIS5_EENS3_9allocatorINS3_4pairIKS5_S5_EEEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ac10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac10.md) · 呼出先 8件 [`005896b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/005896b4.md) [`00c5a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a720.md) [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) [`00c5ab90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab90.md)
- 新版 呼出元 1件 [`00c5b010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b010.md) · 呼出先 8件 [`005896f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/005896f4.md) [`00c5ab20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ab20.md) [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) [`00c5af90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 80.18% / 新版 80.18%

CFGの説明率　旧版 36.96% / 新版 38.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b416ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b41700"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4174c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b41b08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b416f8"
      ]
    ],
    [
      "unmatched:00b416ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41b34"
      ]
    ],
    [
      "unmatched:00b416f4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41b38"
      ]
    ]
  ],
  "added": [
    [
      "00b41b08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41b20"
      ]
    ],
    [
      "00b41b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41b34"
      ]
    ],
    [
      "00b41b1c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b41b38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b416ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b4163c.md#insn-00b416ec) · [`00b41700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b4163c.md#insn-00b41700) · [`00b4174c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b41/00b4163c.md#insn-00b4174c)

~~~diff
- 00b416ec ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b416ec ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b416ec ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b416ec ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b416ec bytes 09010037
- 00b41700 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b41700 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00b41700 bytes 81000054
- 00b4174c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b4174c ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b4174c bytes c1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a02f23e9418eb936981585b4390b17b4"></a>

### [`00b43e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43e4c.md) → [`00b44274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44274.md) _ZN8firebase11LogGetLevelEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43e58"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b44280"
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
      "unmatched:00b43e50",
      "READ",
      [
        "storage",
        "00c9b2d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b43e54",
      "READ",
      [
        "storage",
        "00ca4240",
        "_ZN8firebase11g_log_levelE",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b44278",
      "READ",
      [
        "storage",
        "00c9b6d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b4427c",
      "READ",
      [
        "storage",
        "00ca4640",
        "_ZN8firebase11g_log_levelE",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43e4c.md#insn-00b43e58) · [`00b43e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43e4c.md#insn-00b43e4c)
- 新版 `00b44280`（命令位置の公開資料なし）

~~~diff
- 00b43e58 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b43e58 ["RETURN", null, ["register:0:8"]]
- 00b43e58 bytes c0035fd6
+ 00b44280 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b44280 ["RETURN", null, ["register:0:8"]]
+ 00b44280 bytes c0035fd6
- 00b43e4c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b43e4c bytes c80a0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e27eded8a71c8574761c2d6df8df1af1"></a>

### [`00b43f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43f00.md) → [`00b44328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44328.md) _ZN8firebase7LogInfoEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5abe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abe0.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)
- 新版 呼出元 1件 [`00c5afe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5afe0.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 51.22% / 新版 51.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 2件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43f1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43f20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b43f20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b43f1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43f20",
      "WRITE",
      [
        "storage",
        "Stack[-0x130]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b43f24",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b44344",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00b44348",
      "WRITE",
      [
        "storage",
        "Stack[-0x130]",
        null,
        null
      ]
    ],
    [
      "00b4434c",
      "WRITE",
      [
        "storage",
        "Stack[-0x110]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b43f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43f00.md#insn-00b43f1c) · [`00b43f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43f00.md#insn-00b43f20) · [`00b43f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43f00.md#insn-00b43f24)

~~~diff
- 00b43f1c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:b8:8"]]
- 00b43f1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4038:8"]]
- 00b43f1c bytes e75f00f9
- 00b43f20 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b43f20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b43f20 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b43f20 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b43f20 bytes e00700ad
- 00b43f24 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b43f24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00b43f24 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b43f24 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5060:16"]]
- 00b43f24 bytes e20f01ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27c4d632a555877099fb619b0719ddc5"></a>

### [`00b44190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44190.md) → [`00b445b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b445b8.md) _ZN8firebase10LogMessageENS_8LogLevelEPKcz

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5acc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5acc0.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5ad20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad20.md)
- 新版 呼出元 1件 [`00c5b0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0c0.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b120.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 32.43% / 新版 32.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b441ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b441ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b441b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b441ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x120]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b441b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b441b4",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b445d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x120]",
        null,
        null
      ]
    ],
    [
      "00b445d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ],
    [
      "00b445dc",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b441ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44190.md#insn-00b441ac) · [`00b441b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44190.md#insn-00b441b0) · [`00b441b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44190.md#insn-00b441b4)

~~~diff
- 00b441ac ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b441ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b441ac ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b441ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b441ac bytes e00700ad
- 00b441b0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b441b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5040:16"]]
- 00b441b0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b441b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5060:16"]]
- 00b441b0 bytes e20f01ad
- 00b441b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b441b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
- 00b441b4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b441b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50a0:16"]]
- 00b441b4 bytes e41702ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3905f94d923ff10031d9b973537dc09"></a>

### [`00b44224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44224.md) → [`00b4464c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b4464c.md) _ZN8firebase14LogSetCallbackEPFvNS_8LogLevelEPKcPvES3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b43cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b43/00b43cf8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b44120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44120.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 36.36% / 新版 36.36%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44244"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44248"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4466c"
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
      "unmatched:00b4422c",
      "READ",
      [
        "storage",
        "00c9b2e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b44230",
      "READ",
      [
        "storage",
        "00c9b2e8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b44244",
      "WRITE",
      [
        "storage",
        "00ca4248",
        "_ZN8firebase14g_log_callbackE",
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b44654",
      "READ",
      [
        "storage",
        "00c9b6e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b44658",
      "READ",
      [
        "storage",
        "00c9b6e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b4466c",
      "WRITE",
      [
        "storage",
        "00ca4648",
        "_ZN8firebase14g_log_callbackE",
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44224.md#insn-00b44244) · [`00b44248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44224.md#insn-00b44248) · [`00b4424c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44224.md#insn-00b4424c)

~~~diff
- 00b44244 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b44244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b44244 bytes 280100f9
- 00b44248 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b44248 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00b44248 bytes 410100f9
- 00b4424c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b4424c ["RETURN", null, ["register:0:8"]]
- 00b4424c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83a5b77a54e3236d9d18d9a7ce210680"></a>

### [`00b443cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b443cc.md) → [`00b447f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b447f4.md) _ZN8firebase11LogMessageVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ace0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ace0.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5adf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5adf0.md)
- 新版 呼出元 1件 [`00c5b0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0e0.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5b1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b1f0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.46% / 新版 78.46%

CFGの説明率　旧版 13.04% / 新版 15.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b443e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b44810"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b443ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b443e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b443ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b448d4"
      ]
    ],
    [
      "00b44828",
      "DATA",
      [
        "storage",
        "0030b5b4",
        "switchD_00b4440c::switchdataD_0030b5b4",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b44810",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00b44814",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b448d4"
      ]
    ],
    [
      "00b44828",
      "DATA",
      [
        "storage",
        "0030b5f4",
        "switchD_00b44834::switchdataD_0030b5f4",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b443e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b443cc.md#insn-00b443e8) · [`00b443ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b443cc.md#insn-00b443ec) · [`00b444c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b443cc.md#insn-00b444c8)

~~~diff
- 00b443e8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b443e8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00b443e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b443e8 bytes a9831ef8
- 00b443ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b443ec ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b443ec ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 00b443ec bytes 08060054
- 00b444c8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b444c8 ["RETURN", null, ["register:0:8"]]
- 00b444c8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15454f44d662e3fcbbb3ff5fb543928c"></a>

### [`00b447b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b447b0.md) → [`00b44bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b44/00b44bd8.md) _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b447e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b44c08"
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
      "unmatched:00b447e0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b44c08",
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

- 旧版 [`00b447e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b447b0.md#insn-00b447e0) · [`00b447c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b447b0.md#insn-00b447c8)
- 新版 `00b44c08`（命令位置の公開資料なし） · `00b44bf0`（命令位置の公開資料なし）

~~~diff
- 00b447e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b447e0 ["INT_ADD", "register:40f0:8", ["const:b447e0:8", "const:4:8"]]
- 00b447e0 ["CALLIND", null, ["register:0:8"]]
- 00b447e0 bytes 00013fd6
+ 00b44c08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b44c08 ["INT_ADD", "register:40f0:8", ["const:b44c08:8", "const:4:8"]]
+ 00b44c08 ["CALLIND", null, ["register:0:8"]]
+ 00b44c08 bytes 00013fd6
- 00b447c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b447c8 ["INT_ADD", "register:40f0:8", ["const:b447c8:8", "const:4:8"]]
- 00b447c8 ["CALLIND", null, ["register:0:8"]]
+ 00b44bf0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b44bf0 ["INT_ADD", "register:40f0:8", ["const:b44bf0:8", "const:4:8"]]
+ 00b44bf0 ["CALLIND", null, ["register:0:8"]]
- 00b447c8 bytes 00013fd6
+ 00b44bf0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea67d1b4ca7c1118e0cf363c796809c2"></a>

### [`00b44ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44ea0.md) → [`00b452c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b452c8.md) _ZN8firebase4util12class_loader10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 26.67% / 新版 26.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44ea0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44ea4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b44ea4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b44ea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b44ea4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b452dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b44ec4"
      ]
    ]
  ],
  "added": [
    [
      "00b452c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b452cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b452dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b452ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b44ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44ea0.md#insn-00b44ea0) · [`00b44ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44ea0.md#insn-00b44ea4) · [`00b44ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44ea0.md#insn-00b44ec0)

~~~diff
- 00b44ea0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b44ea0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b44ea0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b44ea0 bytes f30f1ef8
- 00b44ea4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b44ea4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b44ea4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b44ea4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b44ea4 bytes fd7b01a9
- 00b44ec0 ["INT_ADD", "register:40f0:8", ["const:b44ec0:8", "const:4:8"]]
- 00b44ec0 ["CALL", null, ["callee:00c5b000:8"]]
- 00b44ec0 bytes 50570494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a87b80cd8a277c2347ea88f5d7766b1e"></a>

### [`00b44ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44ff0.md) → [`00b45418`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45418.md) _ZN8firebase4util17jniresultcallback15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.79% / 新版 71.79%

CFGの説明率　旧版 10.00% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45078"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b454a0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45030"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4542c",
      "READ",
      [
        "storage",
        "01125258",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45438",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4507c"
      ]
    ],
    [
      "unmatched:00b45024",
      "READ",
      [
        "storage",
        "01125250",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4542c",
      "READ",
      [
        "storage",
        "01125658",
        null,
        "undefined1"
      ]
    ],
    [
      "00b45438",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b454a4"
      ]
    ],
    [
      "00b4544c",
      "READ",
      [
        "storage",
        "01125650",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44ff0.md#insn-00b45030) · [`00b45044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44ff0.md#insn-00b45044) · [`00b4505c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b44/00b44ff0.md#insn-00b4505c)

~~~diff
- 00b45030 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45030 ["INT_ADD", "register:40f0:8", ["const:b45030:8", "const:4:8"]]
- 00b45030 ["CALLIND", null, ["register:0:8"]]
- 00b45030 bytes 00013fd6
- 00b45044 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45044 ["INT_ADD", "register:40f0:8", ["const:b45044:8", "const:4:8"]]
- 00b45044 ["CALLIND", null, ["register:0:8"]]
- 00b45044 bytes 00013fd6
- 00b4505c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4505c ["INT_ADD", "register:40f0:8", ["const:b4505c:8", "const:4:8"]]
- 00b4505c ["CALLIND", null, ["register:0:8"]]
- 00b4505c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a47174c2380379c27f285ba73330a3ab"></a>

### [`00b4508c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4508c.md) → [`00b454b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b454b4.md) _ZN8firebase4util17jniresultcallback12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 40.00% / 新版 40.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4508c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45090"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45090"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4508c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45090",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45094",
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
      "00b454b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b454b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b454bc",
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

- 旧版 [`00b4508c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4508c.md#insn-00b4508c) · [`00b45090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4508c.md#insn-00b45090) · [`00b45094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4508c.md#insn-00b45094)

~~~diff
- 00b4508c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b4508c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b4508c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b4508c bytes f50f1df8
- 00b45090 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b45090 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b45090 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45090 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45090 bytes f44f01a9
- 00b45094 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45094 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45094 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b45094 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45094 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-598f67dabe25e3369f9609d9da39837b"></a>

### [`00b45248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45248.md) → [`00b45670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45670.md) _ZN8firebase4util17jniresultcallback10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 33.33% / 新版 33.33%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b4525c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b45684"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45268"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4525c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b4526c"
      ]
    ],
    [
      "unmatched:00b45264",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b45268",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b45684",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45694"
      ]
    ],
    [
      "00b4568c",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b45690",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4525c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45248.md#insn-00b4525c) · [`00b45268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45248.md#insn-00b45268) · [`00b45280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45248.md#insn-00b45280)

~~~diff
- 00b4525c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b4525c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b4525c bytes 8b000054
- 00b45268 ["INT_ADD", "register:40f0:8", ["const:b45268:8", "const:4:8"]]
- 00b45268 ["CALL", null, ["callee:00c5b000:8"]]
- 00b45268 bytes 66560494
- 00b45280 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b45280 ["RETURN", null, ["register:0:8"]]
- 00b45280 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-054b379ca1f16d8ed7a86dda41314bf9"></a>

### [`00b45284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45284.md) → [`00b456ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b456ac.md) _ZN8firebase4util26cppthreaddispatchercontext19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45288"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45284",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45288",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b45294",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b456ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b456b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b456bc",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45284.md#insn-00b45284) · [`00b45288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45284.md#insn-00b45288) · [`00b45298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45284.md#insn-00b45298)

~~~diff
- 00b45284 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b45284 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b45284 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b45284 bytes f30f1ef8
- 00b45288 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b45288 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b45288 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b45288 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b45288 bytes fd7b01a9
- 00b45298 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45298 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b45298 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fe39343b8603c7552d5c40d3867eafc"></a>

### [`00b45304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45304.md) → [`00b4572c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4572c.md) _ZN8firebase4util26cppthreaddispatchercontext10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4575c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45318"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b45314",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45318",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45760"
      ]
    ],
    [
      "unmatched:00b45324",
      "PARAM",
      [
        "storage",
        "002be54b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4573c",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45740",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45760"
      ]
    ],
    [
      "00b4574c",
      "PARAM",
      [
        "storage",
        "002be58b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45304.md#insn-00b45318) · [`00b4532c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45304.md#insn-00b4532c) · [`00b45334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45304.md#insn-00b45334)

~~~diff
- 00b45318 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45318 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b45318 bytes 080100b5
- 00b4532c ["INT_ADD", "register:40f0:8", ["const:b4532c:8", "const:4:8"]]
- 00b4532c ["CALL", null, ["callee:00c5af10:8"]]
- 00b4532c bytes f9550494
- 00b45334 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:278:8"]]
- 00b45334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45334 bytes 603e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf221c7c259aa7a39658b4dc113faa64"></a>

### [`00b4538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4538c.md) → [`00b457b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b457b4.md) _ZN8firebase4util26cppthreaddispatchercontext8GetClassEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45394"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b457bc"
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
      "unmatched:00b45390",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b457b8",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4538c.md#insn-00b45394) · [`00b4538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4538c.md#insn-00b4538c)
- 新版 `00b457bc`（命令位置の公開資料なし）

~~~diff
- 00b45394 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b45394 ["RETURN", null, ["register:0:8"]]
- 00b45394 bytes c0035fd6
+ 00b457bc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b457bc ["RETURN", null, ["register:0:8"]]
+ 00b457bc bytes c0035fd6
- 00b4538c ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00b4538c bytes 082f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bfb88d9f7bd0c448115d952dfa1429d"></a>

### [`00b45398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45398.md) → [`00b457c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b457c0.md) _ZN8firebase4util26cppthreaddispatchercontext15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 14.29% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45420"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45848"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b453f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b457d4",
      "READ",
      [
        "storage",
        "01125280",
        null,
        "undefined1"
      ]
    ],
    [
      "00b457e0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45424"
      ]
    ],
    [
      "unmatched:00b453cc",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b457d4",
      "READ",
      [
        "storage",
        "01125680",
        null,
        "undefined1"
      ]
    ],
    [
      "00b457e0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4584c"
      ]
    ],
    [
      "00b457f4",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b453d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45398.md#insn-00b453d8) · [`00b453f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45398.md#insn-00b453f4) · [`00b45414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45398.md#insn-00b45414)

~~~diff
- 00b453d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b453d8 ["INT_ADD", "register:40f0:8", ["const:b453d8:8", "const:4:8"]]
- 00b453d8 ["CALLIND", null, ["register:0:8"]]
- 00b453d8 bytes 00013fd6
- 00b453f4 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b453f4 bytes 20010054
- 00b45414 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b45414 ["INT_ADD", "register:40f0:8", ["const:b45414:8", "const:4:8"]]
- 00b45414 ["CALLIND", null, ["register:0:8"]]
- 00b45414 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9778e72d9f92400c56278a2be8441203"></a>

### [`00b45434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45434.md) → [`00b4585c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b4585c.md) _ZN8firebase4util26cppthreaddispatchercontext12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 35.00% / 新版 35.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45470"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b454c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45898"
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
      "unmatched:00b45448",
      "READ",
      [
        "storage",
        "01125278",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b4544c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b454c4"
      ]
    ],
    [
      "unmatched:00b45454",
      "READ",
      [
        "storage",
        "01125280",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b45870",
      "READ",
      [
        "storage",
        "01125678",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45874",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b458ec"
      ]
    ],
    [
      "00b4587c",
      "READ",
      [
        "storage",
        "01125680",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4544c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45434.md#insn-00b4544c) · [`00b4546c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45434.md#insn-00b4546c) · [`00b45470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b45434.md#insn-00b45470)

~~~diff
- 00b4544c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b4544c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b4544c bytes c10300b4
- 00b4546c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4546c ["INT_ADD", "register:40f0:8", ["const:b4546c:8", "const:4:8"]]
- 00b4546c ["CALLIND", null, ["register:0:8"]]
- 00b4546c bytes 00013fd6
- 00b45470 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b45470 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b45470 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:280:8"]]
- 00b45470 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b45470 bytes bf020a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da4c4eec22e86ced8b2e9c70b7aeef74"></a>

### [`00b455f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b455f0.md) → [`00b45a18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45a18.md) _ZN8firebase4util26cppthreaddispatchercontext10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 46.67% / 新版 46.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45610"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b45a38"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45628"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b45a2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b45614"
      ]
    ],
    [
      "unmatched:00b4560c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b45610",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b45a2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45a3c"
      ]
    ],
    [
      "00b45a34",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b45a38",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b455f0.md#insn-00b45610) · [`00b45628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b455f0.md#insn-00b45628)
- 新版 `00b45a38`（命令位置の公開資料なし）

~~~diff
- 00b45610 ["INT_ADD", "register:40f0:8", ["const:b45610:8", "const:4:8"]]
- 00b45610 ["CALL", null, ["callee:00c5b000:8"]]
- 00b45610 bytes 7c550494
- 00b45628 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b45628 ["RETURN", null, ["register:0:8"]]
- 00b45628 bytes c0035fd6
+ 00b45a38 ["INT_ADD", "register:40f0:8", ["const:b45a38:8", "const:4:8"]]
+ 00b45a38 ["CALL", null, ["callee:00c5b000:8"]]
+ 00b45a38 bytes 72550494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-309e2a93be4ffe353caf2f63ca5ff99d"></a>

### [`00b4562c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4562c.md) → [`00b45a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b45/00b45a54.md) _ZN8firebase4util19cppthreaddispatcher19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocator

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45658"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b45a80"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b45640"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b4563c",
      "READ",
      [
        "storage",
        "011252b0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b45640",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45a84"
      ]
    ],
    [
      "unmatched:00b4564c",
      "PARAM",
      [
        "storage",
        "002bad63",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b45a64",
      "READ",
      [
        "storage",
        "011256b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b45a68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b45a84"
      ]
    ],
    [
      "00b45a74",
      "PARAM",
      [
        "storage",
        "002bada3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b45640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4562c.md#insn-00b45640) · [`00b45650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4562c.md#insn-00b45650) · [`00b45658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b45/00b4562c.md#insn-00b45658)

~~~diff
- 00b45640 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b45640 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b45640 bytes e80000b5
- 00b45650 ["INT_ADD", "register:40f0:8", ["const:b45650:8", "const:4:8"]]
- 00b45650 ["CALL", null, ["callee:00c5af10:8"]]
- 00b45650 bytes 30550494
- 00b45658 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b0:8"]]
- 00b45658 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b45658 bytes 605a01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

