# v16.0.0 → v16.0.1 · 最優先の変更候補 (67)

[一覧の目次](README.md)

<a id="compare-698a72fc8d955278f614fa206d9346b1"></a>

### [`00b00f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00f9c.md) → [`00b013c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b013c4.md) FUN_00b013c4

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 4件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008c2ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2ce0.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 4件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008c2d24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c2d24.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b00fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00f9c.md#insn-00b00fb8) · [`00b00fcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00f9c.md#insn-00b00fcc) · [`00b00fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00f9c.md#insn-00b00fd4)
- 新版 `00b013e0`（命令位置の公開資料なし） · `00b013f4`（命令位置の公開資料なし） · `00b013fc`（命令位置の公開資料なし）

~~~diff
- 00b00fb8 ["INT_ADD", "register:40f0:8", ["const:b00fb8:8", "const:4:8"]]
- 00b00fb8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b013e0 ["INT_ADD", "register:40f0:8", ["const:b013e0:8", "const:4:8"]]
+ 00b013e0 ["CALL", null, ["callee:008514f8:8"]]
- 00b00fb8 bytes 4041f597
+ 00b013e0 bytes 4640f597
- 00b00fcc ["INT_ADD", "register:40f0:8", ["const:b00fcc:8", "const:4:8"]]
- 00b00fcc ["CALL", null, ["callee:005e7420:8"]]
+ 00b013f4 ["INT_ADD", "register:40f0:8", ["const:b013f4:8", "const:4:8"]]
+ 00b013f4 ["CALL", null, ["callee:005e7420:8"]]
- 00b00fcc bytes 0599eb97
+ 00b013f4 bytes 0b98eb97
- 00b00fd4 ["INT_ADD", "register:40f0:8", ["const:b00fd4:8", "const:4:8"]]
- 00b00fd4 ["CALL", null, ["callee:008514f8:8"]]
+ 00b013fc ["INT_ADD", "register:40f0:8", ["const:b013fc:8", "const:4:8"]]
+ 00b013fc ["CALL", null, ["callee:008514f8:8"]]
- 00b00fd4 bytes 3941f597
+ 00b013fc bytes 3f40f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8c6365fb52a7787c397bd49a896c78e"></a>

### [`00b01414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01414.md) → [`00b0183c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b0183c.md) FUN_00b0183c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.68% / 新版 94.68%

CFGの説明率　旧版 38.89% / 新版 31.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0187c",
      "incomplete_value": true,
      "site": "00b01880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01454",
      "incomplete_value": true,
      "site": "00b01458",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
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
      "unmatched:00b01518",
      "DATA",
      [
        "storage",
        "0023d2fc",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b01940",
      "DATA",
      [
        "storage",
        "0023d2fc",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01414.md#insn-00b01458) · [`00b01438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01414.md#insn-00b01438) · [`00b01440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01414.md#insn-00b01440)
- 新版 `00b01880`（命令位置の公開資料なし） · `00b01860`（命令位置の公開資料なし） · `00b01868`（命令位置の公開資料なし）

~~~diff
- 00b01458 ["INT_ADD", "register:40f0:8", ["const:b01458:8", "const:4:8"]]
- 00b01458 ["CALL", null, ["callee:005e7420:8"]]
+ 00b01880 ["INT_ADD", "register:40f0:8", ["const:b01880:8", "const:4:8"]]
+ 00b01880 ["CALL", null, ["callee:005e7420:8"]]
- 00b01458 bytes e297eb97
+ 00b01880 bytes e896eb97
- 00b01438 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00b01860 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b01438 bytes 00020054
+ 00b01860 bytes 00020054
- 00b01440 ["INT_ADD", "register:40f0:8", ["const:b01440:8", "const:4:8"]]
- 00b01440 ["CALL", null, ["callee:008514f8:8"]]
+ 00b01868 ["INT_ADD", "register:40f0:8", ["const:b01868:8", "const:4:8"]]
+ 00b01868 ["CALL", null, ["callee:008514f8:8"]]
- 00b01440 bytes 1e40f597
+ 00b01868 bytes 243ff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc720217dc5e743246eb9c65c9d26d58"></a>

### [`00b0158c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0158c.md) → [`00b019b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b019b4.md) FUN_00b019b4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 45.45% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b015a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0158c.md#insn-00b015a8) · [`00b015bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0158c.md#insn-00b015bc) · [`00b015c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0158c.md#insn-00b015c0)
- 新版 `00b019d0`（命令位置の公開資料なし） · `00b019e4`（命令位置の公開資料なし） · `00b019e8`（命令位置の公開資料なし）

~~~diff
- 00b015a8 ["INT_ADD", "register:40f0:8", ["const:b015a8:8", "const:4:8"]]
- 00b015a8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b019d0 ["INT_ADD", "register:40f0:8", ["const:b019d0:8", "const:4:8"]]
+ 00b019d0 ["CALL", null, ["callee:008514f8:8"]]
- 00b015a8 bytes c43ff597
+ 00b019d0 bytes ca3ef597
- 00b015bc ["INT_ADD", "register:40f0:8", ["const:b015bc:8", "const:4:8"]]
- 00b015bc ["CALL", null, ["callee:005e7420:8"]]
+ 00b019e4 ["INT_ADD", "register:40f0:8", ["const:b019e4:8", "const:4:8"]]
+ 00b019e4 ["CALL", null, ["callee:005e7420:8"]]
- 00b015bc bytes 8997eb97
+ 00b019e4 bytes 8f96eb97
- 00b015c0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b015c0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b015c0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b015c0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b019e8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b019e8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b019e8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b019e8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b015c0 bytes e0000037
+ 00b019e8 bytes e0000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97fb07b515f9b75f000f11a7e4aacd3b"></a>

### [`00b0180c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0180c.md) → [`00b01c34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b01c34.md) FUN_00b01c34

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b01868",
      "DATA",
      [
        "storage",
        "0030a490",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01894",
      "DATA",
      [
        "storage",
        "0030a484",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b01c90",
      "DATA",
      [
        "storage",
        "0030a4d0",
        null,
        null
      ]
    ],
    [
      "00b01cbc",
      "DATA",
      [
        "storage",
        "0030a4c4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0182c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0180c.md#insn-00b0182c) · [`00b01840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0180c.md#insn-00b01840) · [`00b01848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b0180c.md#insn-00b01848)
- 新版 `00b01c54`（命令位置の公開資料なし） · `00b01c68`（命令位置の公開資料なし） · `00b01c70`（命令位置の公開資料なし）

~~~diff
- 00b0182c ["INT_ADD", "register:40f0:8", ["const:b0182c:8", "const:4:8"]]
- 00b0182c ["CALL", null, ["callee:008514f8:8"]]
+ 00b01c54 ["INT_ADD", "register:40f0:8", ["const:b01c54:8", "const:4:8"]]
+ 00b01c54 ["CALL", null, ["callee:008514f8:8"]]
- 00b0182c bytes 233ff597
+ 00b01c54 bytes 293ef597
- 00b01840 ["INT_ADD", "register:40f0:8", ["const:b01840:8", "const:4:8"]]
- 00b01840 ["CALL", null, ["callee:005e7420:8"]]
+ 00b01c68 ["INT_ADD", "register:40f0:8", ["const:b01c68:8", "const:4:8"]]
+ 00b01c68 ["CALL", null, ["callee:005e7420:8"]]
- 00b01840 bytes e896eb97
+ 00b01c68 bytes ee95eb97
- 00b01848 ["INT_ADD", "register:40f0:8", ["const:b01848:8", "const:4:8"]]
- 00b01848 ["CALL", null, ["callee:008514f8:8"]]
+ 00b01c70 ["INT_ADD", "register:40f0:8", ["const:b01c70:8", "const:4:8"]]
+ 00b01c70 ["CALL", null, ["callee:008514f8:8"]]
- 00b01848 bytes 1c3ff597
+ 00b01c70 bytes 223ef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cf85a0954c2574232e2750ac99c413e"></a>

### [`00b018c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b018c0.md) → [`00b01ce8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b01ce8.md) FUN_00b01ce8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 50.33% / 新版 50.33%

CFGの説明率　旧版 13.04% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b019e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b019f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01a9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b019b0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005e7420"
      ]
    ],
    [
      "unmatched:00b019b8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "unmatched:00b019ec",
      "DATA",
      [
        "storage",
        "0023d410",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b01dd8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005e7420"
      ]
    ],
    [
      "00b01de0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514f8"
      ]
    ],
    [
      "00b01e14",
      "DATA",
      [
        "storage",
        "0023d410",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b019b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b018c0.md#insn-00b019b0) · [`00b019b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b018c0.md#insn-00b019b8) · [`00b019e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b018c0.md#insn-00b019e8)

~~~diff
- 00b019b0 ["INT_ADD", "register:40f0:8", ["const:b019b0:8", "const:4:8"]]
- 00b019b0 ["CALL", null, ["callee:005e7420:8"]]
- 00b019b0 bytes 8c96eb97
- 00b019b8 ["INT_ADD", "register:40f0:8", ["const:b019b8:8", "const:4:8"]]
- 00b019b8 ["CALL", null, ["callee:008514f8:8"]]
- 00b019b8 bytes c03ef597
- 00b019e8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b019e8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b019e8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b019e8 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b019e8 bytes 2801889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16d002884af060cac1ece67dffee6013"></a>

### [`00b01b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01b24.md) → [`00b01f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b01f4c.md) FUN_00b01f4c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 42.86% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01b24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01b24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01b28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b01b24",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01b28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01b2c",
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
      "00b01f4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b01f50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b01f54",
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

- 旧版 [`00b01b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01b24.md#insn-00b01b24) · [`00b01b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01b24.md#insn-00b01b28) · [`00b01b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01b24.md#insn-00b01b2c)

~~~diff
- 00b01b24 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b01b24 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b01b24 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b01b24 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b01b24 bytes fd7bbda9
- 00b01b28 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b01b28 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b01b28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b01b28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01b28 bytes f65701a9
- 00b01b2c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b01b2c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b01b2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b01b2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01b2c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-851001259c8336373b7d14edfa28630f"></a>

### [`00b01be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01be0.md) → [`00b02008`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02008.md) FUN_00b02008

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 33.33% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b01bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01be0.md#insn-00b01bfc) · [`00b01c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01be0.md#insn-00b01c10) · [`00b01c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01be0.md#insn-00b01c18)
- 新版 `00b02024`（命令位置の公開資料なし） · `00b02038`（命令位置の公開資料なし） · `00b02040`（命令位置の公開資料なし）

~~~diff
- 00b01bfc ["INT_ADD", "register:40f0:8", ["const:b01bfc:8", "const:4:8"]]
- 00b01bfc ["CALL", null, ["callee:008514f8:8"]]
+ 00b02024 ["INT_ADD", "register:40f0:8", ["const:b02024:8", "const:4:8"]]
+ 00b02024 ["CALL", null, ["callee:008514f8:8"]]
- 00b01bfc bytes 2f3ef597
+ 00b02024 bytes 353df597
- 00b01c10 ["INT_ADD", "register:40f0:8", ["const:b01c10:8", "const:4:8"]]
- 00b01c10 ["CALL", null, ["callee:005e7420:8"]]
+ 00b02038 ["INT_ADD", "register:40f0:8", ["const:b02038:8", "const:4:8"]]
+ 00b02038 ["CALL", null, ["callee:005e7420:8"]]
- 00b01c10 bytes f495eb97
+ 00b02038 bytes fa94eb97
- 00b01c18 ["INT_ADD", "register:40f0:8", ["const:b01c18:8", "const:4:8"]]
- 00b01c18 ["CALL", null, ["callee:008514f8:8"]]
+ 00b02040 ["INT_ADD", "register:40f0:8", ["const:b02040:8", "const:4:8"]]
+ 00b02040 ["CALL", null, ["callee:008514f8:8"]]
- 00b01c18 bytes 283ef597
+ 00b02040 bytes 2e3df597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44fc4195acaaf81c631bed0b1bae4a59"></a>

### [`00b01c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01c9c.md) → [`00b020c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b020c4.md) FUN_00b020c4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.21% / 新版 70.21%

CFGの説明率　旧版 16.67% / 新版 6.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01c9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01c9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01ca0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b01c9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01ca0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01ca4",
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
      "00b020c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b020c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b020cc",
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

- 旧版 [`00b01c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01c9c.md#insn-00b01c9c) · [`00b01ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01c9c.md#insn-00b01ca0) · [`00b01ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01c9c.md#insn-00b01ca4)

~~~diff
- 00b01c9c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b01c9c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b01c9c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b01c9c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b01c9c bytes fd7bbda9
- 00b01ca0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b01ca0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b01ca0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b01ca0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01ca0 bytes f65701a9
- 00b01ca4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b01ca4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b01ca4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b01ca4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01ca4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c192b5dfb0787a9be88449ba2596019"></a>

### [`00b01d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01d58.md) → [`00b02180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02180.md) FUN_00b02180

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.72% / 新版 78.72%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01d58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01d58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b01d5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b01d58",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01d5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b01d60",
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
      "00b02180",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b02184",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b02188",
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

- 旧版 [`00b01d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01d58.md#insn-00b01d58) · [`00b01d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01d58.md#insn-00b01d5c) · [`00b01d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01d58.md#insn-00b01d60)

~~~diff
- 00b01d58 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b01d58 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b01d58 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b01d58 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b01d58 bytes fd7bbda9
- 00b01d5c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b01d5c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b01d5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b01d5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01d5c bytes f65701a9
- 00b01d60 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b01d60 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b01d60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b01d60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b01d60 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d2eaa97aa7d3e7b8cb7fb28b4d09fb5"></a>

### [`00b01e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01e8c.md) → [`00b022b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b022b4.md) FUN_00b022b4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b01ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01e8c.md#insn-00b01ea8) · [`00b01ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01e8c.md#insn-00b01ebc) · [`00b01ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01e8c.md#insn-00b01ec0)
- 新版 `00b022d0`（命令位置の公開資料なし） · `00b022e4`（命令位置の公開資料なし） · `00b022e8`（命令位置の公開資料なし）

~~~diff
- 00b01ea8 ["INT_ADD", "register:40f0:8", ["const:b01ea8:8", "const:4:8"]]
- 00b01ea8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b022d0 ["INT_ADD", "register:40f0:8", ["const:b022d0:8", "const:4:8"]]
+ 00b022d0 ["CALL", null, ["callee:008514f8:8"]]
- 00b01ea8 bytes 843df597
+ 00b022d0 bytes 8a3cf597
- 00b01ebc ["INT_ADD", "register:40f0:8", ["const:b01ebc:8", "const:4:8"]]
- 00b01ebc ["CALL", null, ["callee:005e7420:8"]]
+ 00b022e4 ["INT_ADD", "register:40f0:8", ["const:b022e4:8", "const:4:8"]]
+ 00b022e4 ["CALL", null, ["callee:005e7420:8"]]
- 00b01ebc bytes 4995eb97
+ 00b022e4 bytes 4f94eb97
- 00b01ec0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b01ec0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b01ec0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b01ec0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b022e8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b022e8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b022e8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b022e8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b01ec0 bytes 60000037
+ 00b022e8 bytes 60000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a50c02fc11a823dfa41e00f545a2ac8"></a>

### [`00b01fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01fe0.md) → [`00b02408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02408.md) FUN_00b02408

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 9.09% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b02434",
      "incomplete_value": true,
      "site": "00b02438",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0245c",
      "incomplete_value": true,
      "site": "00b0247c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b02454",
      "incomplete_value": true,
      "site": "00b0247c",
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
    "old": null,
    "ordinal": 3,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b02010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01fe0.md#insn-00b02010) · [`00b02054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01fe0.md#insn-00b02054) · [`00b01ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b01/00b01fe0.md#insn-00b01ffc)
- 新版 `00b02438`（命令位置の公開資料なし） · `00b0247c`（命令位置の公開資料なし） · `00b02424`（命令位置の公開資料なし）

~~~diff
- 00b02010 ["INT_ADD", "register:40f0:8", ["const:b02010:8", "const:4:8"]]
- 00b02010 ["CALL", null, ["callee:005e7420:8"]]
+ 00b02438 ["INT_ADD", "register:40f0:8", ["const:b02438:8", "const:4:8"]]
+ 00b02438 ["CALL", null, ["callee:005e7420:8"]]
- 00b02010 bytes f494eb97
+ 00b02438 bytes fa93eb97
- 00b02054 ["INT_ADD", "register:40f0:8", ["const:b02054:8", "const:4:8"]]
- 00b02054 ["CALL", null, ["callee:00afeae8:8"]]
+ 00b0247c ["INT_ADD", "register:40f0:8", ["const:b0247c:8", "const:4:8"]]
+ 00b0247c ["CALL", null, ["callee:00afeae8:8"]]
- 00b02054 bytes 9bf1ff97
+ 00b0247c bytes 9bf1ff97
- 00b01ffc ["INT_ADD", "register:40f0:8", ["const:b01ffc:8", "const:4:8"]]
- 00b01ffc ["CALL", null, ["callee:008514f8:8"]]
+ 00b02424 ["INT_ADD", "register:40f0:8", ["const:b02424:8", "const:4:8"]]
+ 00b02424 ["CALL", null, ["callee:008514f8:8"]]
- 00b01ffc bytes 2f3df597
+ 00b02424 bytes 353cf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8768e29ed58ba40d3089017ce8a11ae"></a>

### [`00b0206c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0206c.md) → [`00b02494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02494.md) FUN_00b02494

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0206c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0206c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02070"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0206c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b02070",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b02074",
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
      "00b02494",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b02498",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b0249c",
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

- 旧版 [`00b0206c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0206c.md#insn-00b0206c) · [`00b02070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0206c.md#insn-00b02070) · [`00b02074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0206c.md#insn-00b02074)

~~~diff
- 00b0206c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0206c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0206c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b0206c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b0206c bytes fd7bbda9
- 00b02070 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b02070 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b02070 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b02070 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b02070 bytes f65701a9
- 00b02074 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b02074 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b02074 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b02074 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b02074 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c06416d6f6acce6114bf5d6f6c52288"></a>

### [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md) → [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md) FUN_00b0272c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 31件 [`00af8fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af8/00af8fa4.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) [`00b00bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00bb8.md) [`00b00ee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b00ee0.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00853c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c30.md) [`00903da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903da8.md) [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md)
- 新版 呼出元 31件 [`00af93cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af9/00af93cc.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) [`00b00fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b00fe0.md) [`00b01308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b01/00b01308.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00853c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c70.md) [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.95% / 新版 96.95%

CFGの説明率　旧版 57.43% / 新版 52.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02598"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02674"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b029c0"
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
      "unmatched:00b0249c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b028e8"
      ]
    ],
    [
      "unmatched:00b024b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b02944"
      ]
    ],
    [
      "unmatched:00b02674",
      "DATA",
      [
        "storage",
        "0023d240",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b028c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b028e8"
      ]
    ],
    [
      "00b028d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b02944"
      ]
    ],
    [
      "00b02a9c",
      "DATA",
      [
        "storage",
        "0023d240",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0249c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md#insn-00b0249c) · [`00b024b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md#insn-00b024b0) · [`00b02598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md#insn-00b02598)

~~~diff
- 00b0249c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b0249c ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 00b0249c bytes 280100b4
- 00b024b0 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b024b0 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
- 00b024b0 bytes 6a030054
- 00b02598 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:28:8"]]
- 00b02598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b02598 bytes 081400f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eae56ae25c488d72a716c7ec175600a6"></a>

### [`00b0284c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0284c.md) → [`00b02c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02c74.md) FUN_00b02c74

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md)
- 新版 呼出元 5件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 30.00% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0284c.md#insn-00b02870) · [`00b02884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0284c.md#insn-00b02884) · [`00b0288c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0284c.md#insn-00b0288c)
- 新版 `00b02c98`（命令位置の公開資料なし） · `00b02cac`（命令位置の公開資料なし） · `00b02cb4`（命令位置の公開資料なし）

~~~diff
- 00b02870 ["INT_ADD", "register:40f0:8", ["const:b02870:8", "const:4:8"]]
- 00b02870 ["CALL", null, ["callee:008514f8:8"]]
+ 00b02c98 ["INT_ADD", "register:40f0:8", ["const:b02c98:8", "const:4:8"]]
+ 00b02c98 ["CALL", null, ["callee:008514f8:8"]]
- 00b02870 bytes 123bf597
+ 00b02c98 bytes 183af597
- 00b02884 ["INT_ADD", "register:40f0:8", ["const:b02884:8", "const:4:8"]]
- 00b02884 ["CALL", null, ["callee:005e7420:8"]]
+ 00b02cac ["INT_ADD", "register:40f0:8", ["const:b02cac:8", "const:4:8"]]
+ 00b02cac ["CALL", null, ["callee:005e7420:8"]]
- 00b02884 bytes d792eb97
+ 00b02cac bytes dd91eb97
- 00b0288c ["INT_ADD", "register:40f0:8", ["const:b0288c:8", "const:4:8"]]
- 00b0288c ["CALL", null, ["callee:008514f8:8"]]
+ 00b02cb4 ["INT_ADD", "register:40f0:8", ["const:b02cb4:8", "const:4:8"]]
+ 00b02cb4 ["CALL", null, ["callee:008514f8:8"]]
- 00b0288c bytes 0b3bf597
+ 00b02cb4 bytes 113af597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6033e317509fde835a04840f589180b8"></a>

### [`00b029ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b029ec.md) → [`00b02e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02e14.md) FUN_00b02e14

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 5件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md)
- 新版 呼出元 5件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 75.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b029ec.md#insn-00b02a10) · [`00b02a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b029ec.md#insn-00b02a24) · [`00b02a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b029ec.md#insn-00b02a2c)
- 新版 `00b02e38`（命令位置の公開資料なし） · `00b02e4c`（命令位置の公開資料なし） · `00b02e54`（命令位置の公開資料なし）

~~~diff
- 00b02a10 ["INT_ADD", "register:40f0:8", ["const:b02a10:8", "const:4:8"]]
- 00b02a10 ["CALL", null, ["callee:008514f8:8"]]
+ 00b02e38 ["INT_ADD", "register:40f0:8", ["const:b02e38:8", "const:4:8"]]
+ 00b02e38 ["CALL", null, ["callee:008514f8:8"]]
- 00b02a10 bytes aa3af597
+ 00b02e38 bytes b039f597
- 00b02a24 ["INT_ADD", "register:40f0:8", ["const:b02a24:8", "const:4:8"]]
- 00b02a24 ["CALL", null, ["callee:005e7420:8"]]
+ 00b02e4c ["INT_ADD", "register:40f0:8", ["const:b02e4c:8", "const:4:8"]]
+ 00b02e4c ["CALL", null, ["callee:005e7420:8"]]
- 00b02a24 bytes 6f92eb97
+ 00b02e4c bytes 7591eb97
- 00b02a2c ["INT_ADD", "register:40f0:8", ["const:b02a2c:8", "const:4:8"]]
- 00b02a2c ["CALL", null, ["callee:008514f8:8"]]
+ 00b02e54 ["INT_ADD", "register:40f0:8", ["const:b02e54:8", "const:4:8"]]
+ 00b02e54 ["CALL", null, ["callee:008514f8:8"]]
- 00b02a2c bytes a33af597
+ 00b02e54 bytes a939f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fa865d7b318ec4d29cda6fb12bd8123"></a>

### [`00b02abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02abc.md) → [`00b02ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02ee4.md) FUN_00b02ee4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 5件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md)
- 新版 呼出元 5件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.71% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02abc.md#insn-00b02ae0) · [`00b02af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02abc.md#insn-00b02af4) · [`00b02afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02abc.md#insn-00b02afc)
- 新版 `00b02f08`（命令位置の公開資料なし） · `00b02f1c`（命令位置の公開資料なし） · `00b02f24`（命令位置の公開資料なし）

~~~diff
- 00b02ae0 ["INT_ADD", "register:40f0:8", ["const:b02ae0:8", "const:4:8"]]
- 00b02ae0 ["CALL", null, ["callee:008514f8:8"]]
+ 00b02f08 ["INT_ADD", "register:40f0:8", ["const:b02f08:8", "const:4:8"]]
+ 00b02f08 ["CALL", null, ["callee:008514f8:8"]]
- 00b02ae0 bytes 763af597
+ 00b02f08 bytes 7c39f597
- 00b02af4 ["INT_ADD", "register:40f0:8", ["const:b02af4:8", "const:4:8"]]
- 00b02af4 ["CALL", null, ["callee:005e7420:8"]]
+ 00b02f1c ["INT_ADD", "register:40f0:8", ["const:b02f1c:8", "const:4:8"]]
+ 00b02f1c ["CALL", null, ["callee:005e7420:8"]]
- 00b02af4 bytes 3b92eb97
+ 00b02f1c bytes 4191eb97
- 00b02afc ["INT_ADD", "register:40f0:8", ["const:b02afc:8", "const:4:8"]]
- 00b02afc ["CALL", null, ["callee:008514f8:8"]]
+ 00b02f24 ["INT_ADD", "register:40f0:8", ["const:b02f24:8", "const:4:8"]]
+ 00b02f24 ["CALL", null, ["callee:008514f8:8"]]
- 00b02afc bytes 6f3af597
+ 00b02f24 bytes 7539f597
~~~


<a id="compare-b170483b246ded78a15387f9da71a343"></a>

### [`00b02b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02b8c.md) → [`00b02fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02fb4.md) FUN_00b02fb4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md)
- 新版 呼出元 5件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 28.57% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02c08"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b03030"
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
      "unmatched:00b02bf8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b02bfc",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b02c00",
      "READ",
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
      "00b03020",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b03024",
      "READ",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b03028",
      "READ",
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

- 旧版 [`00b02c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02b8c.md#insn-00b02c08) · [`00b02bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02b8c.md#insn-00b02bb0)
- 新版 `00b03030`（命令位置の公開資料なし） · `00b02fd8`（命令位置の公開資料なし）

~~~diff
- 00b02c08 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b02c08 ["RETURN", null, ["register:0:8"]]
- 00b02c08 bytes c0035fd6
+ 00b03030 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b03030 ["RETURN", null, ["register:0:8"]]
+ 00b03030 bytes c0035fd6
- 00b02bb0 ["INT_ADD", "register:40f0:8", ["const:b02bb0:8", "const:4:8"]]
- 00b02bb0 ["CALL", null, ["callee:008514f8:8"]]
+ 00b02fd8 ["INT_ADD", "register:40f0:8", ["const:b02fd8:8", "const:4:8"]]
+ 00b02fd8 ["CALL", null, ["callee:008514f8:8"]]
- 00b02bb0 bytes 423af597
+ 00b02fd8 bytes 4839f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a9186db76cb428adc275305e43d9ce2"></a>

### [`00b02c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02c5c.md) → [`00b03084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03084.md) FUN_00b03084

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`005e1b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1b78.md) [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md)
- 新版 呼出元 6件 [`005e1bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1bb8.md) [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 80.77% / 新版 80.77%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b030b8",
      "incomplete_value": true,
      "site": "00b030bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b02c90",
      "incomplete_value": true,
      "site": "00b02c94",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b02cd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b03100"
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
      "00b030d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b02cdc"
      ]
    ],
    [
      "unmatched:00b02cd4",
      "DATA",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b030d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b03104"
      ]
    ],
    [
      "00b030fc",
      "DATA",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02c5c.md#insn-00b02c94) · [`00b02cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02c5c.md#insn-00b02cd8)
- 新版 `00b030bc`（命令位置の公開資料なし） · `00b03100`（命令位置の公開資料なし）

~~~diff
- 00b02c94 ["INT_ADD", "register:40f0:8", ["const:b02c94:8", "const:4:8"]]
- 00b02c94 ["CALL", null, ["callee:005e7420:8"]]
+ 00b030bc ["INT_ADD", "register:40f0:8", ["const:b030bc:8", "const:4:8"]]
+ 00b030bc ["CALL", null, ["callee:005e7420:8"]]
- 00b02c94 bytes d391eb97
+ 00b030bc bytes d990eb97
- 00b02cd8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b02cd8 ["RETURN", null, ["register:0:8"]]
- 00b02cd8 bytes c0035fd6
+ 00b03100 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b03100 ["RETURN", null, ["register:0:8"]]
+ 00b03100 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ae03ef4e707f805934918535ecbf8a6"></a>

### [`00b02d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02d2c.md) → [`00b03154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03154.md) FUN_00b03154

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md)
- 新版 呼出元 5件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b02d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02d2c.md#insn-00b02d50) · [`00b02d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02d2c.md#insn-00b02d64) · [`00b02d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02d2c.md#insn-00b02d6c)
- 新版 `00b03178`（命令位置の公開資料なし） · `00b0318c`（命令位置の公開資料なし） · `00b03194`（命令位置の公開資料なし）

~~~diff
- 00b02d50 ["INT_ADD", "register:40f0:8", ["const:b02d50:8", "const:4:8"]]
- 00b02d50 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03178 ["INT_ADD", "register:40f0:8", ["const:b03178:8", "const:4:8"]]
+ 00b03178 ["CALL", null, ["callee:008514f8:8"]]
- 00b02d50 bytes da39f597
+ 00b03178 bytes e038f597
- 00b02d64 ["INT_ADD", "register:40f0:8", ["const:b02d64:8", "const:4:8"]]
- 00b02d64 ["CALL", null, ["callee:005e7420:8"]]
+ 00b0318c ["INT_ADD", "register:40f0:8", ["const:b0318c:8", "const:4:8"]]
+ 00b0318c ["CALL", null, ["callee:005e7420:8"]]
- 00b02d64 bytes 9f91eb97
+ 00b0318c bytes a590eb97
- 00b02d6c ["INT_ADD", "register:40f0:8", ["const:b02d6c:8", "const:4:8"]]
- 00b02d6c ["CALL", null, ["callee:008514f8:8"]]
+ 00b03194 ["INT_ADD", "register:40f0:8", ["const:b03194:8", "const:4:8"]]
+ 00b03194 ["CALL", null, ["callee:008514f8:8"]]
- 00b02d6c bytes d339f597
+ 00b03194 bytes d938f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31128c3d86189ffbcf154aaa0015ca7b"></a>

### [`00b02dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02dfc.md) → [`00b03224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03224.md) FUN_00b03224

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md)
- 新版 呼出元 5件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 14.29% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b03258",
      "incomplete_value": true,
      "site": "00b0325c",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b02e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02dfc.md#insn-00b02e34) · [`00b02e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02dfc.md#insn-00b02e0c) · [`00b02e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02dfc.md#insn-00b02e20)
- 新版 `00b0325c`（命令位置の公開資料なし） · `00b03248`（命令位置の公開資料なし）

~~~diff
- 00b02e34 ["INT_ADD", "register:40f0:8", ["const:b02e34:8", "const:4:8"]]
- 00b02e34 ["CALL", null, ["callee:005e7420:8"]]
+ 00b0325c ["INT_ADD", "register:40f0:8", ["const:b0325c:8", "const:4:8"]]
+ 00b0325c ["CALL", null, ["callee:005e7420:8"]]
- 00b02e34 bytes 6b91eb97
+ 00b0325c bytes 7190eb97
- 00b02e0c ["COPY", "register:40e8:8", ["register:8:8"]]
- 00b02e0c bytes fd030091
- 00b02e20 ["INT_ADD", "register:40f0:8", ["const:b02e20:8", "const:4:8"]]
- 00b02e20 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03248 ["INT_ADD", "register:40f0:8", ["const:b03248:8", "const:4:8"]]
+ 00b03248 ["CALL", null, ["callee:008514f8:8"]]
- 00b02e20 bytes a639f597
+ 00b03248 bytes ac38f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35d9c570ab99ede2740290a7ea2de3e4"></a>

### [`00b02ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02ecc.md) → [`00b032f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b032f4.md) FUN_00b032f4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b02f40",
      "incomplete_value": true,
      "site": "00b02f5c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
      "definition_site": "00b02f30",
      "incomplete_value": true,
      "site": "00b02f5c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b02f34",
      "incomplete_value": true,
      "site": "00b02f5c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b02f24",
      "DATA",
      [
        "storage",
        "0023d3bc",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b0334c",
      "DATA",
      [
        "storage",
        "0023d3bc",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02ecc.md#insn-00b02f5c) · [`00b02f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02ecc.md#insn-00b02f70)
- 新版 `00b03384`（命令位置の公開資料なし） · `00b03398`（命令位置の公開資料なし）

~~~diff
- 00b02f5c ["INT_ADD", "register:40f0:8", ["const:b02f5c:8", "const:4:8"]]
- 00b02f5c ["CALL", null, ["callee:00afeae8:8"]]
+ 00b03384 ["INT_ADD", "register:40f0:8", ["const:b03384:8", "const:4:8"]]
+ 00b03384 ["CALL", null, ["callee:00afeae8:8"]]
- 00b02f5c bytes d9edff97
+ 00b03384 bytes d9edff97
- 00b02f70 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b02f70 ["RETURN", null, ["register:0:8"]]
- 00b02f70 bytes c0035fd6
+ 00b03398 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b03398 ["RETURN", null, ["register:0:8"]]
+ 00b03398 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76678c1d24d1680c08ff0d2fe37fa907"></a>

### [`00b02f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02f74.md) → [`00b0339c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b0339c.md) FUN_00b0339c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b02fe8",
      "incomplete_value": true,
      "site": "00b03004",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
      "definition_site": "00b02fdc",
      "incomplete_value": true,
      "site": "00b03004",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b02fec",
      "incomplete_value": false,
      "site": "00b03004",
      "value": [
        "leaf",
        "const:33:8"
      ]
    },
    "ordinal": 3,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b02fcc",
      "DATA",
      [
        "storage",
        "0023d3c4",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b033f4",
      "DATA",
      [
        "storage",
        "0023d3c4",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b03004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02f74.md#insn-00b03004) · [`00b02f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02f74.md#insn-00b02f90) · [`00b02fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02f74.md#insn-00b02fa4)
- 新版 `00b0342c`（命令位置の公開資料なし） · `00b033b8`（命令位置の公開資料なし） · `00b033cc`（命令位置の公開資料なし）

~~~diff
- 00b03004 ["INT_ADD", "register:40f0:8", ["const:b03004:8", "const:4:8"]]
- 00b03004 ["CALL", null, ["callee:00afeae8:8"]]
+ 00b0342c ["INT_ADD", "register:40f0:8", ["const:b0342c:8", "const:4:8"]]
+ 00b0342c ["CALL", null, ["callee:00afeae8:8"]]
- 00b03004 bytes afedff97
+ 00b0342c bytes afedff97
- 00b02f90 ["INT_ADD", "register:40f0:8", ["const:b02f90:8", "const:4:8"]]
- 00b02f90 ["CALL", null, ["callee:008514f8:8"]]
+ 00b033b8 ["INT_ADD", "register:40f0:8", ["const:b033b8:8", "const:4:8"]]
+ 00b033b8 ["CALL", null, ["callee:008514f8:8"]]
- 00b02f90 bytes 4a39f597
+ 00b033b8 bytes 5038f597
- 00b02fa4 ["INT_ADD", "register:40f0:8", ["const:b02fa4:8", "const:4:8"]]
- 00b02fa4 ["CALL", null, ["callee:005e7420:8"]]
+ 00b033cc ["INT_ADD", "register:40f0:8", ["const:b033cc:8", "const:4:8"]]
+ 00b033cc ["CALL", null, ["callee:005e7420:8"]]
- 00b02fa4 bytes 0f91eb97
+ 00b033cc bytes 1590eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f84c303ac4d60146165b6896db820303"></a>

### [`00b0301c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0301c.md) → [`00b03444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03444.md) FUN_00b03444

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 14.29% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b03474",
      "incomplete_value": true,
      "site": "00b03478",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00b03078",
      "DATA",
      [
        "storage",
        "0023d3d4",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b034a0",
      "DATA",
      [
        "storage",
        "0023d3d4",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b03050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0301c.md#insn-00b03050) · [`00b0303c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0301c.md#insn-00b0303c) · [`00b03058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0301c.md#insn-00b03058)
- 新版 `00b03478`（命令位置の公開資料なし） · `00b03464`（命令位置の公開資料なし） · `00b03480`（命令位置の公開資料なし）

~~~diff
- 00b03050 ["INT_ADD", "register:40f0:8", ["const:b03050:8", "const:4:8"]]
- 00b03050 ["CALL", null, ["callee:005e7420:8"]]
+ 00b03478 ["INT_ADD", "register:40f0:8", ["const:b03478:8", "const:4:8"]]
+ 00b03478 ["CALL", null, ["callee:005e7420:8"]]
- 00b03050 bytes e490eb97
+ 00b03478 bytes ea8feb97
- 00b0303c ["INT_ADD", "register:40f0:8", ["const:b0303c:8", "const:4:8"]]
- 00b0303c ["CALL", null, ["callee:008514f8:8"]]
+ 00b03464 ["INT_ADD", "register:40f0:8", ["const:b03464:8", "const:4:8"]]
+ 00b03464 ["CALL", null, ["callee:008514f8:8"]]
- 00b0303c bytes 1f39f597
+ 00b03464 bytes 2538f597
- 00b03058 ["INT_ADD", "register:40f0:8", ["const:b03058:8", "const:4:8"]]
- 00b03058 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03480 ["INT_ADD", "register:40f0:8", ["const:b03480:8", "const:4:8"]]
+ 00b03480 ["CALL", null, ["callee:008514f8:8"]]
- 00b03058 bytes 1839f597
+ 00b03480 bytes 1e38f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a4704c0bad84972556c08401f28a13f"></a>

### [`00b030ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b030ec.md) → [`00b03514`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03514.md) FUN_00b03514

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 12.50% / 新版 6.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b03118",
      "incomplete_value": true,
      "site": "00b0311c",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b0313c",
      "incomplete_value": true,
      "site": "00b03150",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
      "definition_site": "00b03140",
      "incomplete_value": true,
      "site": "00b03150",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b0311c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b030ec.md#insn-00b0311c) · [`00b03150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b030ec.md#insn-00b03150) · [`00b03108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b030ec.md#insn-00b03108)
- 新版 `00b03544`（命令位置の公開資料なし） · `00b03578`（命令位置の公開資料なし） · `00b03530`（命令位置の公開資料なし）

~~~diff
- 00b0311c ["INT_ADD", "register:40f0:8", ["const:b0311c:8", "const:4:8"]]
- 00b0311c ["CALL", null, ["callee:005e7420:8"]]
+ 00b03544 ["INT_ADD", "register:40f0:8", ["const:b03544:8", "const:4:8"]]
+ 00b03544 ["CALL", null, ["callee:005e7420:8"]]
- 00b0311c bytes b190eb97
+ 00b03544 bytes b78feb97
- 00b03150 ["INT_ADD", "register:40f0:8", ["const:b03150:8", "const:4:8"]]
- 00b03150 ["CALL", null, ["callee:00afeae8:8"]]
+ 00b03578 ["INT_ADD", "register:40f0:8", ["const:b03578:8", "const:4:8"]]
+ 00b03578 ["CALL", null, ["callee:00afeae8:8"]]
- 00b03150 bytes 5cedff97
+ 00b03578 bytes 5cedff97
- 00b03108 ["INT_ADD", "register:40f0:8", ["const:b03108:8", "const:4:8"]]
- 00b03108 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03530 ["INT_ADD", "register:40f0:8", ["const:b03530:8", "const:4:8"]]
+ 00b03530 ["CALL", null, ["callee:008514f8:8"]]
- 00b03108 bytes ec38f597
+ 00b03530 bytes f237f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-726301dd5fa505825e9ce9febef1d785"></a>

### [`00b03228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03228.md) → [`00b03650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03650.md) FUN_00b03650

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 14.29% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0322c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b03228",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0322c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b03230",
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
      "00b03650",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b03654",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b03658",
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

- 旧版 [`00b03228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03228.md#insn-00b03228) · [`00b0322c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03228.md#insn-00b0322c) · [`00b03230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03228.md#insn-00b03230)

~~~diff
- 00b03228 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b03228 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b03228 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b03228 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b03228 bytes fd7bbda9
- 00b0322c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b0322c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b0322c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b0322c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0322c bytes f65701a9
- 00b03230 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b03230 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b03230 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b03230 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b03230 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3082410a6e1ed1f70fde92a0388391b"></a>

### [`00b032d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b032d0.md) → [`00b036f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b036f8.md) FUN_00b036f8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 4件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b032ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b032d0.md#insn-00b032ec) · [`00b03300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b032d0.md#insn-00b03300) · [`00b03308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b032d0.md#insn-00b03308)
- 新版 `00b03714`（命令位置の公開資料なし） · `00b03728`（命令位置の公開資料なし） · `00b03730`（命令位置の公開資料なし）

~~~diff
- 00b032ec ["INT_ADD", "register:40f0:8", ["const:b032ec:8", "const:4:8"]]
- 00b032ec ["CALL", null, ["callee:008514f8:8"]]
+ 00b03714 ["INT_ADD", "register:40f0:8", ["const:b03714:8", "const:4:8"]]
+ 00b03714 ["CALL", null, ["callee:008514f8:8"]]
- 00b032ec bytes 7338f597
+ 00b03714 bytes 7937f597
- 00b03300 ["INT_ADD", "register:40f0:8", ["const:b03300:8", "const:4:8"]]
- 00b03300 ["CALL", null, ["callee:005e7420:8"]]
+ 00b03728 ["INT_ADD", "register:40f0:8", ["const:b03728:8", "const:4:8"]]
+ 00b03728 ["CALL", null, ["callee:005e7420:8"]]
- 00b03300 bytes 3890eb97
+ 00b03728 bytes 3e8feb97
- 00b03308 ["INT_ADD", "register:40f0:8", ["const:b03308:8", "const:4:8"]]
- 00b03308 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03730 ["INT_ADD", "register:40f0:8", ["const:b03730:8", "const:4:8"]]
+ 00b03730 ["CALL", null, ["callee:008514f8:8"]]
- 00b03308 bytes 6c38f597
+ 00b03730 bytes 7237f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac7fb259323d891dd2d0d6b1ac8369ff"></a>

### [`00b0338c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0338c.md) → [`00b037b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b037b4.md) FUN_00b037b4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b037e0",
      "incomplete_value": true,
      "site": "00b037e4",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b033b8",
      "incomplete_value": true,
      "site": "00b033bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b033bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0338c.md#insn-00b033bc) · [`00b033a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0338c.md#insn-00b033a8) · [`00b033b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0338c.md#insn-00b033b8)
- 新版 `00b037e4`（命令位置の公開資料なし） · `00b037d0`（命令位置の公開資料なし）

~~~diff
- 00b033bc ["INT_ADD", "register:40f0:8", ["const:b033bc:8", "const:4:8"]]
- 00b033bc ["CALL", null, ["callee:005e7420:8"]]
+ 00b037e4 ["INT_ADD", "register:40f0:8", ["const:b037e4:8", "const:4:8"]]
+ 00b037e4 ["CALL", null, ["callee:005e7420:8"]]
- 00b033bc bytes 0990eb97
+ 00b037e4 bytes 0f8feb97
- 00b033a8 ["INT_ADD", "register:40f0:8", ["const:b033a8:8", "const:4:8"]]
- 00b033a8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b037d0 ["INT_ADD", "register:40f0:8", ["const:b037d0:8", "const:4:8"]]
+ 00b037d0 ["CALL", null, ["callee:008514f8:8"]]
- 00b033a8 bytes 4438f597
+ 00b037d0 bytes 4a37f597
- 00b033b8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b033b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b033b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b033b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b033b8 bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2164131357bf44e3507bf2e9d50a11e"></a>

### [`00b03580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03580.md) → [`00b039a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b039a8.md) FUN_00b039a8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b0359c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03580.md#insn-00b0359c) · [`00b035b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03580.md#insn-00b035b0) · [`00b035b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03580.md#insn-00b035b4)
- 新版 `00b039c4`（命令位置の公開資料なし） · `00b039d8`（命令位置の公開資料なし） · `00b039dc`（命令位置の公開資料なし）

~~~diff
- 00b0359c ["INT_ADD", "register:40f0:8", ["const:b0359c:8", "const:4:8"]]
- 00b0359c ["CALL", null, ["callee:008514f8:8"]]
+ 00b039c4 ["INT_ADD", "register:40f0:8", ["const:b039c4:8", "const:4:8"]]
+ 00b039c4 ["CALL", null, ["callee:008514f8:8"]]
- 00b0359c bytes c737f597
+ 00b039c4 bytes cd36f597
- 00b035b0 ["INT_ADD", "register:40f0:8", ["const:b035b0:8", "const:4:8"]]
- 00b035b0 ["CALL", null, ["callee:005e7420:8"]]
+ 00b039d8 ["INT_ADD", "register:40f0:8", ["const:b039d8:8", "const:4:8"]]
+ 00b039d8 ["CALL", null, ["callee:005e7420:8"]]
- 00b035b0 bytes 8c8feb97
+ 00b039d8 bytes 928eeb97
- 00b035b4 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b035b4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b035b4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b035b4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b039dc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b039dc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b039dc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b039dc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b035b4 bytes 60000037
+ 00b039dc bytes 60000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4029251969588c452f9d4be3d798789"></a>

### [`00b03618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03618.md) → [`00b03a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03a40.md) FUN_00b03a40

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 71.43% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b03634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03618.md#insn-00b03634) · [`00b03648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03618.md#insn-00b03648) · [`00b03658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03618.md#insn-00b03658)
- 新版 `00b03a5c`（命令位置の公開資料なし） · `00b03a70`（命令位置の公開資料なし） · `00b03a80`（命令位置の公開資料なし）

~~~diff
- 00b03634 ["INT_ADD", "register:40f0:8", ["const:b03634:8", "const:4:8"]]
- 00b03634 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03a5c ["INT_ADD", "register:40f0:8", ["const:b03a5c:8", "const:4:8"]]
+ 00b03a5c ["CALL", null, ["callee:008514f8:8"]]
- 00b03634 bytes a137f597
+ 00b03a5c bytes a736f597
- 00b03648 ["INT_ADD", "register:40f0:8", ["const:b03648:8", "const:4:8"]]
- 00b03648 ["CALL", null, ["callee:005e7420:8"]]
+ 00b03a70 ["INT_ADD", "register:40f0:8", ["const:b03a70:8", "const:4:8"]]
+ 00b03a70 ["CALL", null, ["callee:005e7420:8"]]
- 00b03648 bytes 668feb97
+ 00b03a70 bytes 6c8eeb97
- 00b03658 ["INT_ADD", "register:40f0:8", ["const:b03658:8", "const:4:8"]]
- 00b03658 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03a80 ["INT_ADD", "register:40f0:8", ["const:b03a80:8", "const:4:8"]]
+ 00b03a80 ["CALL", null, ["callee:008514f8:8"]]
- 00b03658 bytes 9837f597
+ 00b03a80 bytes 9e36f597
~~~


<a id="compare-8ad3bb6cc7012bfea1649c21af3fa8d5"></a>

### [`00b036b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b036b0.md) → [`00b03ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03ad8.md) FUN_00b03ad8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b03b04",
      "incomplete_value": true,
      "site": "00b03b08",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00b03708",
      "DATA",
      [
        "storage",
        "0023d42c",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b03b30",
      "DATA",
      [
        "storage",
        "0023d42c",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b036e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b036b0.md#insn-00b036e0) · [`00b036cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b036b0.md#insn-00b036cc) · [`00b036e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b036b0.md#insn-00b036e8)
- 新版 `00b03b08`（命令位置の公開資料なし） · `00b03af4`（命令位置の公開資料なし） · `00b03b10`（命令位置の公開資料なし）

~~~diff
- 00b036e0 ["INT_ADD", "register:40f0:8", ["const:b036e0:8", "const:4:8"]]
- 00b036e0 ["CALL", null, ["callee:005e7420:8"]]
+ 00b03b08 ["INT_ADD", "register:40f0:8", ["const:b03b08:8", "const:4:8"]]
+ 00b03b08 ["CALL", null, ["callee:005e7420:8"]]
- 00b036e0 bytes 408feb97
+ 00b03b08 bytes 468eeb97
- 00b036cc ["INT_ADD", "register:40f0:8", ["const:b036cc:8", "const:4:8"]]
- 00b036cc ["CALL", null, ["callee:008514f8:8"]]
+ 00b03af4 ["INT_ADD", "register:40f0:8", ["const:b03af4:8", "const:4:8"]]
+ 00b03af4 ["CALL", null, ["callee:008514f8:8"]]
- 00b036cc bytes 7b37f597
+ 00b03af4 bytes 8136f597
- 00b036e8 ["INT_ADD", "register:40f0:8", ["const:b036e8:8", "const:4:8"]]
- 00b036e8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03b10 ["INT_ADD", "register:40f0:8", ["const:b03b10:8", "const:4:8"]]
+ 00b03b10 ["CALL", null, ["callee:008514f8:8"]]
- 00b036e8 bytes 7437f597
+ 00b03b10 bytes 7a36f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54265eb6efbdea8bb4f6e2831ed9bd5d"></a>

### [`00b0376c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0376c.md) → [`00b03b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03b94.md) FUN_00b03b94

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 16件 [`005e0f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0f50.md) [`005e44ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e44ec.md) [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`0075959c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00759/0075959c.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 16件 [`005e0f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e0/005e0f90.md) [`005e452c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e4/005e452c.md) [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00707ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707ee0.md) [`007595dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00759/007595dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 16.67% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b03770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0376c.md#insn-00b03770) · [`00b03790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0376c.md#insn-00b03790) · [`00b037a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0376c.md#insn-00b037a4)
- 新版 `00b03b98`（命令位置の公開資料なし） · `00b03bb8`（命令位置の公開資料なし） · `00b03bcc`（命令位置の公開資料なし）

~~~diff
- 00b03770 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b03770 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b03b98 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00b03b98 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b03770 bytes 2b020054
+ 00b03b98 bytes 2b020054
- 00b03790 ["INT_ADD", "register:40f0:8", ["const:b03790:8", "const:4:8"]]
- 00b03790 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03bb8 ["INT_ADD", "register:40f0:8", ["const:b03bb8:8", "const:4:8"]]
+ 00b03bb8 ["CALL", null, ["callee:008514f8:8"]]
- 00b03790 bytes 4a37f597
+ 00b03bb8 bytes 5036f597
- 00b037a4 ["INT_ADD", "register:40f0:8", ["const:b037a4:8", "const:4:8"]]
- 00b037a4 ["CALL", null, ["callee:005e7420:8"]]
+ 00b03bcc ["INT_ADD", "register:40f0:8", ["const:b03bcc:8", "const:4:8"]]
+ 00b03bcc ["CALL", null, ["callee:005e7420:8"]]
- 00b037a4 bytes 0f8feb97
+ 00b03bcc bytes 158eeb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc2623e01f91cc5ea7d666158c185abd"></a>

### [`00b039b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b039b8.md) → [`00b03de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03de0.md) FUN_00b03de0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b03e04",
      "incomplete_value": true,
      "site": "00b03e08",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b039dc",
      "incomplete_value": true,
      "site": "00b039e0",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b039e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b039b8.md#insn-00b039e0) · [`00b039cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b039b8.md#insn-00b039cc) · [`00b039dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b039b8.md#insn-00b039dc)
- 新版 `00b03e08`（命令位置の公開資料なし） · `00b03df4`（命令位置の公開資料なし）

~~~diff
- 00b039e0 ["INT_ADD", "register:40f0:8", ["const:b039e0:8", "const:4:8"]]
- 00b039e0 ["CALL", null, ["callee:005e7420:8"]]
+ 00b03e08 ["INT_ADD", "register:40f0:8", ["const:b03e08:8", "const:4:8"]]
+ 00b03e08 ["CALL", null, ["callee:005e7420:8"]]
- 00b039e0 bytes 808eeb97
+ 00b03e08 bytes 868deb97
- 00b039cc ["INT_ADD", "register:40f0:8", ["const:b039cc:8", "const:4:8"]]
- 00b039cc ["CALL", null, ["callee:008514f8:8"]]
+ 00b03df4 ["INT_ADD", "register:40f0:8", ["const:b03df4:8", "const:4:8"]]
+ 00b03df4 ["CALL", null, ["callee:008514f8:8"]]
- 00b039cc bytes bb36f597
+ 00b03df4 bytes c135f597
- 00b039dc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b039dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b039dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b039dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b039dc bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7e05232dec1682c7e6053b4aedaa0d2"></a>

### [`00b03a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03a14.md) → [`00b03e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03e3c.md) FUN_00b03e3c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00b005b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b00/00b005b4.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 14.29% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b03e60",
      "incomplete_value": true,
      "site": "00b03e64",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": null,
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
      "unmatched:00b03a58",
      "DATA",
      [
        "storage",
        "0023d718",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b03e80",
      "DATA",
      [
        "storage",
        "0023d718",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b03a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03a14.md#insn-00b03a3c) · [`00b03a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03a14.md#insn-00b03a28) · [`00b03a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03a14.md#insn-00b03a40)
- 新版 `00b03e64`（命令位置の公開資料なし） · `00b03e50`（命令位置の公開資料なし） · `00b03e68`（命令位置の公開資料なし）

~~~diff
- 00b03a3c ["INT_ADD", "register:40f0:8", ["const:b03a3c:8", "const:4:8"]]
- 00b03a3c ["CALL", null, ["callee:005e7420:8"]]
+ 00b03e64 ["INT_ADD", "register:40f0:8", ["const:b03e64:8", "const:4:8"]]
+ 00b03e64 ["CALL", null, ["callee:005e7420:8"]]
- 00b03a3c bytes 698eeb97
+ 00b03e64 bytes 6f8deb97
- 00b03a28 ["INT_ADD", "register:40f0:8", ["const:b03a28:8", "const:4:8"]]
- 00b03a28 ["CALL", null, ["callee:008514f8:8"]]
+ 00b03e50 ["INT_ADD", "register:40f0:8", ["const:b03e50:8", "const:4:8"]]
+ 00b03e50 ["CALL", null, ["callee:008514f8:8"]]
- 00b03a28 bytes a436f597
+ 00b03e50 bytes aa35f597
- 00b03a40 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b03a40 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b03a40 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b03a40 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b03e68 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b03e68 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b03e68 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b03e68 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b03a40 bytes 00010037
+ 00b03e68 bytes 00010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a3f288001d29949f1e10eef7e4dee32"></a>

### [`00b042c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b042c8.md) → [`00b046f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b046f0.md) FUN_00b046f0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b042ec",
      "incomplete_value": true,
      "site": "00b042f0",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04328"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b04750"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b042f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b042c8.md#insn-00b042f0) · [`00b04328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b042c8.md#insn-00b04328)
- 新版 `00b04718`（命令位置の公開資料なし） · `00b04750`（命令位置の公開資料なし）

~~~diff
- 00b042f0 ["INT_ADD", "register:40f0:8", ["const:b042f0:8", "const:4:8"]]
- 00b042f0 ["CALL", null, ["callee:005e7420:8"]]
+ 00b04718 ["INT_ADD", "register:40f0:8", ["const:b04718:8", "const:4:8"]]
+ 00b04718 ["CALL", null, ["callee:005e7420:8"]]
- 00b042f0 bytes 3c8ceb97
+ 00b04718 bytes 428beb97
- 00b04328 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b04328 ["RETURN", null, ["register:0:8"]]
- 00b04328 bytes c0035fd6
+ 00b04750 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b04750 ["RETURN", null, ["register:0:8"]]
+ 00b04750 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-900555bf32fe8195c5825aed0991506e"></a>

### [`00b04390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04390.md) → [`00b047b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b047b8.md) FUN_00b047b8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b043a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04390.md#insn-00b043a4) · [`00b043b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04390.md#insn-00b043b8) · [`00b043bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04390.md#insn-00b043bc)
- 新版 `00b047cc`（命令位置の公開資料なし） · `00b047e0`（命令位置の公開資料なし） · `00b047e4`（命令位置の公開資料なし）

~~~diff
- 00b043a4 ["INT_ADD", "register:40f0:8", ["const:b043a4:8", "const:4:8"]]
- 00b043a4 ["CALL", null, ["callee:008514f8:8"]]
+ 00b047cc ["INT_ADD", "register:40f0:8", ["const:b047cc:8", "const:4:8"]]
+ 00b047cc ["CALL", null, ["callee:008514f8:8"]]
- 00b043a4 bytes 4534f597
+ 00b047cc bytes 4b33f597
- 00b043b8 ["INT_ADD", "register:40f0:8", ["const:b043b8:8", "const:4:8"]]
- 00b043b8 ["CALL", null, ["callee:005e7420:8"]]
+ 00b047e0 ["INT_ADD", "register:40f0:8", ["const:b047e0:8", "const:4:8"]]
+ 00b047e0 ["CALL", null, ["callee:005e7420:8"]]
- 00b043b8 bytes 0a8ceb97
+ 00b047e0 bytes 108beb97
- 00b043bc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b043bc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b043bc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b043bc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b047e4 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b047e4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b047e4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b047e4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b043bc bytes 40010037
+ 00b047e4 bytes 40010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-364a1c2b475a2b123f5dd612f1def686"></a>

### [`00b043f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b043f4.md) → [`00b0481c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b0481c.md) FUN_00b0481c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md)
- 新版 呼出元 4件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 12.50% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b04418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b043f4.md#insn-00b04418) · [`00b0442c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b043f4.md#insn-00b0442c) · [`00b04434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b043f4.md#insn-00b04434)
- 新版 `00b04840`（命令位置の公開資料なし） · `00b04854`（命令位置の公開資料なし） · `00b0485c`（命令位置の公開資料なし）

~~~diff
- 00b04418 ["INT_ADD", "register:40f0:8", ["const:b04418:8", "const:4:8"]]
- 00b04418 ["CALL", null, ["callee:008514f8:8"]]
+ 00b04840 ["INT_ADD", "register:40f0:8", ["const:b04840:8", "const:4:8"]]
+ 00b04840 ["CALL", null, ["callee:008514f8:8"]]
- 00b04418 bytes 2834f597
+ 00b04840 bytes 2e33f597
- 00b0442c ["INT_ADD", "register:40f0:8", ["const:b0442c:8", "const:4:8"]]
- 00b0442c ["CALL", null, ["callee:005e7420:8"]]
+ 00b04854 ["INT_ADD", "register:40f0:8", ["const:b04854:8", "const:4:8"]]
+ 00b04854 ["CALL", null, ["callee:005e7420:8"]]
- 00b0442c bytes ed8beb97
+ 00b04854 bytes f38aeb97
- 00b04434 ["INT_ADD", "register:40f0:8", ["const:b04434:8", "const:4:8"]]
- 00b04434 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0485c ["INT_ADD", "register:40f0:8", ["const:b0485c:8", "const:4:8"]]
+ 00b0485c ["CALL", null, ["callee:008514f8:8"]]
- 00b04434 bytes 2134f597
+ 00b0485c bytes 2733f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90d5f9fc972505fe1d6850a671fd6f96"></a>

### [`00b044c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b044c4.md) → [`00b048ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b048ec.md) FUN_00b048ec

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) [`00af566c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af5/00af566c.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md)
- 新版 呼出元 4件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b044e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b044c4.md#insn-00b044e8) · [`00b044fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b044c4.md#insn-00b044fc) · [`00b04504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b044c4.md#insn-00b04504)
- 新版 `00b04910`（命令位置の公開資料なし） · `00b04924`（命令位置の公開資料なし） · `00b0492c`（命令位置の公開資料なし）

~~~diff
- 00b044e8 ["INT_ADD", "register:40f0:8", ["const:b044e8:8", "const:4:8"]]
- 00b044e8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b04910 ["INT_ADD", "register:40f0:8", ["const:b04910:8", "const:4:8"]]
+ 00b04910 ["CALL", null, ["callee:008514f8:8"]]
- 00b044e8 bytes f433f597
+ 00b04910 bytes fa32f597
- 00b044fc ["INT_ADD", "register:40f0:8", ["const:b044fc:8", "const:4:8"]]
- 00b044fc ["CALL", null, ["callee:005e7420:8"]]
+ 00b04924 ["INT_ADD", "register:40f0:8", ["const:b04924:8", "const:4:8"]]
+ 00b04924 ["CALL", null, ["callee:005e7420:8"]]
- 00b044fc bytes b98beb97
+ 00b04924 bytes bf8aeb97
- 00b04504 ["INT_ADD", "register:40f0:8", ["const:b04504:8", "const:4:8"]]
- 00b04504 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0492c ["INT_ADD", "register:40f0:8", ["const:b0492c:8", "const:4:8"]]
+ 00b0492c ["CALL", null, ["callee:008514f8:8"]]
- 00b04504 bytes ed33f597
+ 00b0492c bytes f332f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6eea3a46bc4f89d155729304e31e9100"></a>

### [`00b04594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04594.md) → [`00b049bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b049bc.md) FUN_00b049bc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006c52b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c5/006c52b8.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 14.29% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b049e0",
      "incomplete_value": true,
      "site": "00b049e4",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b045b8",
      "incomplete_value": true,
      "site": "00b045bc",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b045bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04594.md#insn-00b045bc) · [`00b045a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04594.md#insn-00b045a8) · [`00b045b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04594.md#insn-00b045b8)
- 新版 `00b049e4`（命令位置の公開資料なし） · `00b049d0`（命令位置の公開資料なし）

~~~diff
- 00b045bc ["INT_ADD", "register:40f0:8", ["const:b045bc:8", "const:4:8"]]
- 00b045bc ["CALL", null, ["callee:005e7420:8"]]
+ 00b049e4 ["INT_ADD", "register:40f0:8", ["const:b049e4:8", "const:4:8"]]
+ 00b049e4 ["CALL", null, ["callee:005e7420:8"]]
- 00b045bc bytes 898beb97
+ 00b049e4 bytes 8f8aeb97
- 00b045a8 ["INT_ADD", "register:40f0:8", ["const:b045a8:8", "const:4:8"]]
- 00b045a8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b049d0 ["INT_ADD", "register:40f0:8", ["const:b049d0:8", "const:4:8"]]
+ 00b049d0 ["CALL", null, ["callee:008514f8:8"]]
- 00b045a8 bytes c433f597
+ 00b049d0 bytes ca32f597
- 00b045b8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b045b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b045b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b045b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b045b8 bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b572bd196c2314b146330b294a74e65e"></a>

### [`00b045f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b045f8.md) → [`00b04a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04a20.md) FUN_00b04a20

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) · 呼出先 1件 [`00b03c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b03c30.md)
- 新版 呼出元 1件 [`005bc7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005bc/005bc7cc.md) · 呼出先 1件 [`00b04058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04058.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b046e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b046f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0473c"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b04634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b045f8.md#insn-00b04634) · [`00b046e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b045f8.md#insn-00b046e0) · [`00b046f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b045f8.md#insn-00b046f4)
- 新版 `00b04a5c`（命令位置の公開資料なし）

~~~diff
- 00b04634 ["INT_ADD", "register:40f0:8", ["const:b04634:8", "const:4:8"]]
- 00b04634 ["CALL", null, ["callee:00b04058:8"]]
+ 00b04a5c ["INT_ADD", "register:40f0:8", ["const:b04a5c:8", "const:4:8"]]
+ 00b04a5c ["CALL", null, ["callee:00b04058:8"]]
- 00b04634 bytes 7ffdff97
+ 00b04a5c bytes 7ffdff97
- 00b046e0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b046e0 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00b046e0 ["COPY", "tmp:2:4", ["register:4040:4"]]
- 00b046e0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b046e0 bytes 17119f1a
- 00b046f4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b046f4 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00b046f4 ["COPY", "tmp:2:4", ["register:4040:4"]]
- 00b046f4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b046f4 bytes 08119f1a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb50c58dcad1b0ab71e825bdce74da91"></a>

### [`00b04854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md) → [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md) FUN_00b04c7c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 14件 [`006c6444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6444.md) [`00afeea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afeea4.md) [`00b0284c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0284c.md) [`00b0291c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b0291c.md) [`00b029ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b029ec.md) · 呼出先 14件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00853c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c30.md) [`00903da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903da8.md) [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md)
- 新版 呼出元 14件 [`006c6484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6484.md) [`00aff2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00aff2cc.md) [`00b02c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02c74.md) [`00b02d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02d44.md) [`00b02e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02e14.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00853c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c70.md) [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.95% / 新版 84.95%

CFGの説明率　旧版 32.26% / 新版 30.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 2件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04864"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04864"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04868"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b04864",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b04868",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0486c",
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
      "00b04c8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b04c90",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b04c94",
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

- 旧版 [`00b04864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md#insn-00b04864) · [`00b04868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md#insn-00b04868) · [`00b0486c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04854.md#insn-00b0486c)

~~~diff
- 00b04864 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b04864 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b04864 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00b04864 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b04864 bytes f85f0da9
- 00b04868 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b04868 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b04868 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00b04868 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b04868 bytes f6570ea9
- 00b0486c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b0486c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b0486c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00b0486c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0486c bytes f44f0fa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d2d0fadd5f76281b3c25c291a7d3018"></a>

### [`00b04eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04eac.md) → [`00b052d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b052d4.md) FUN_00b052d4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.68% / 新版 94.68%

CFGの説明率　旧版 3.45% / 新版 5.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b05314",
      "incomplete_value": true,
      "site": "00b05318",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04eec",
      "incomplete_value": true,
      "site": "00b04ef0",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b05344",
      "incomplete_value": true,
      "site": "00b05358",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b05348",
      "incomplete_value": true,
      "site": "00b05358",
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
    "old": null,
    "ordinal": 3,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b04ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04eac.md#insn-00b04ef0) · [`00b04f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04eac.md#insn-00b04f30) · [`00b04f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b04/00b04eac.md#insn-00b04f88)
- 新版 `00b05318`（命令位置の公開資料なし） · `00b05358`（命令位置の公開資料なし） · `00b053b0`（命令位置の公開資料なし）

~~~diff
- 00b04ef0 ["INT_ADD", "register:40f0:8", ["const:b04ef0:8", "const:4:8"]]
- 00b04ef0 ["CALL", null, ["callee:005e7420:8"]]
+ 00b05318 ["INT_ADD", "register:40f0:8", ["const:b05318:8", "const:4:8"]]
+ 00b05318 ["CALL", null, ["callee:005e7420:8"]]
- 00b04ef0 bytes 3c89eb97
+ 00b05318 bytes 4288eb97
- 00b04f30 ["INT_ADD", "register:40f0:8", ["const:b04f30:8", "const:4:8"]]
- 00b04f30 ["CALL", null, ["callee:00afeae8:8"]]
+ 00b05358 ["INT_ADD", "register:40f0:8", ["const:b05358:8", "const:4:8"]]
+ 00b05358 ["CALL", null, ["callee:00afeae8:8"]]
- 00b04f30 bytes e4e5ff97
+ 00b05358 bytes e4e5ff97
- 00b04f88 ["INT_ADD", "register:40f0:8", ["const:b04f88:8", "const:4:8"]]
- 00b04f88 ["CALL", null, ["callee:005e7420:8"]]
+ 00b053b0 ["INT_ADD", "register:40f0:8", ["const:b053b0:8", "const:4:8"]]
+ 00b053b0 ["CALL", null, ["callee:005e7420:8"]]
- 00b04f88 bytes 1689eb97
+ 00b053b0 bytes 1c88eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b294317f01c8b62a15d5caa17e12b7b4"></a>

### [`00b05024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05024.md) → [`00b0544c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b0544c.md) FUN_00b0544c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 74.47% / 新版 74.47%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0547c",
      "incomplete_value": true,
      "site": "00b05480",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b050dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b05504"
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
      "unmatched:00b05080",
      "DATA",
      [
        "storage",
        "0030a4a8",
        null,
        null
      ]
    ],
    [
      "unmatched:00b050ac",
      "DATA",
      [
        "storage",
        "0030a49c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b054a8",
      "DATA",
      [
        "storage",
        "0030a4e8",
        null,
        null
      ]
    ],
    [
      "00b054d4",
      "DATA",
      [
        "storage",
        "0030a4dc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05024.md#insn-00b05058) · [`00b050dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05024.md#insn-00b050dc)
- 新版 `00b05480`（命令位置の公開資料なし） · `00b05504`（命令位置の公開資料なし）

~~~diff
- 00b05058 ["INT_ADD", "register:40f0:8", ["const:b05058:8", "const:4:8"]]
- 00b05058 ["CALL", null, ["callee:005e7420:8"]]
+ 00b05480 ["INT_ADD", "register:40f0:8", ["const:b05480:8", "const:4:8"]]
+ 00b05480 ["CALL", null, ["callee:005e7420:8"]]
- 00b05058 bytes e288eb97
+ 00b05480 bytes e887eb97
- 00b050dc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b050dc ["RETURN", null, ["register:0:8"]]
- 00b050dc bytes c0035fd6
+ 00b05504 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b05504 ["RETURN", null, ["register:0:8"]]
+ 00b05504 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd02373a3de6f53ac7d8abe8c7b08e48"></a>

### [`00b050e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b050e0.md) → [`00b05508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05508.md) FUN_00b05508

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 78.72% / 新版 78.72%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0513c",
      "DATA",
      [
        "storage",
        "0030a4c0",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05168",
      "DATA",
      [
        "storage",
        "0030a4b4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b05564",
      "DATA",
      [
        "storage",
        "0030a500",
        null,
        null
      ]
    ],
    [
      "00b05590",
      "DATA",
      [
        "storage",
        "0030a4f4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b050e0.md#insn-00b05100) · [`00b05114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b050e0.md#insn-00b05114) · [`00b0511c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b050e0.md#insn-00b0511c)
- 新版 `00b05528`（命令位置の公開資料なし） · `00b0553c`（命令位置の公開資料なし） · `00b05544`（命令位置の公開資料なし）

~~~diff
- 00b05100 ["INT_ADD", "register:40f0:8", ["const:b05100:8", "const:4:8"]]
- 00b05100 ["CALL", null, ["callee:008514f8:8"]]
+ 00b05528 ["INT_ADD", "register:40f0:8", ["const:b05528:8", "const:4:8"]]
+ 00b05528 ["CALL", null, ["callee:008514f8:8"]]
- 00b05100 bytes ee30f597
+ 00b05528 bytes f42ff597
- 00b05114 ["INT_ADD", "register:40f0:8", ["const:b05114:8", "const:4:8"]]
- 00b05114 ["CALL", null, ["callee:005e7420:8"]]
+ 00b0553c ["INT_ADD", "register:40f0:8", ["const:b0553c:8", "const:4:8"]]
+ 00b0553c ["CALL", null, ["callee:005e7420:8"]]
- 00b05114 bytes b388eb97
+ 00b0553c bytes b987eb97
- 00b0511c ["INT_ADD", "register:40f0:8", ["const:b0511c:8", "const:4:8"]]
- 00b0511c ["CALL", null, ["callee:008514f8:8"]]
+ 00b05544 ["INT_ADD", "register:40f0:8", ["const:b05544:8", "const:4:8"]]
+ 00b05544 ["CALL", null, ["callee:008514f8:8"]]
- 00b0511c bytes e730f597
+ 00b05544 bytes ed2ff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b571c81ec755d40c48431949da9f83e8"></a>

### [`00b0519c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b0519c.md) → [`00b055c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b055c4.md) FUN_00b055c4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b05210",
      "incomplete_value": true,
      "site": "00b0522c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
      "definition_site": "00b05200",
      "incomplete_value": true,
      "site": "00b0522c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b05204",
      "incomplete_value": true,
      "site": "00b0522c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b0522c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b0519c.md#insn-00b0522c) · [`00b051b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b0519c.md#insn-00b051b8) · [`00b051cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b0519c.md#insn-00b051cc)
- 新版 `00b05654`（命令位置の公開資料なし） · `00b055e0`（命令位置の公開資料なし） · `00b055f4`（命令位置の公開資料なし）

~~~diff
- 00b0522c ["INT_ADD", "register:40f0:8", ["const:b0522c:8", "const:4:8"]]
- 00b0522c ["CALL", null, ["callee:00afeae8:8"]]
+ 00b05654 ["INT_ADD", "register:40f0:8", ["const:b05654:8", "const:4:8"]]
+ 00b05654 ["CALL", null, ["callee:00afeae8:8"]]
- 00b0522c bytes 25e5ff97
+ 00b05654 bytes 25e5ff97
- 00b051b8 ["INT_ADD", "register:40f0:8", ["const:b051b8:8", "const:4:8"]]
- 00b051b8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b055e0 ["INT_ADD", "register:40f0:8", ["const:b055e0:8", "const:4:8"]]
+ 00b055e0 ["CALL", null, ["callee:008514f8:8"]]
- 00b051b8 bytes c030f597
+ 00b055e0 bytes c62ff597
- 00b051cc ["INT_ADD", "register:40f0:8", ["const:b051cc:8", "const:4:8"]]
- 00b051cc ["CALL", null, ["callee:005e7420:8"]]
+ 00b055f4 ["INT_ADD", "register:40f0:8", ["const:b055f4:8", "const:4:8"]]
+ 00b055f4 ["CALL", null, ["callee:005e7420:8"]]
- 00b051cc bytes 8588eb97
+ 00b055f4 bytes 8b87eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce3387a8db2df7e4cfbc329c280d9b4b"></a>

### [`00b05244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05244.md) → [`00b0566c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b0566c.md) FUN_00b0566c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 14.29% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05244"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05244"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05248"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05244",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05248",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0524c",
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
      "00b0566c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b05670",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b05674",
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

- 旧版 [`00b05244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05244.md#insn-00b05244) · [`00b05248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05244.md#insn-00b05248) · [`00b0524c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05244.md#insn-00b0524c)

~~~diff
- 00b05244 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05244 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05244 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b05244 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05244 bytes fd7bbda9
- 00b05248 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b05248 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b05248 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05248 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05248 bytes f65701a9
- 00b0524c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b0524c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b0524c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b0524c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0524c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c63e752496ec591cc93d63e3c038abc"></a>

### [`00b052ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b052ec.md) → [`00b05714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05714.md) FUN_00b05714

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 14.29% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b05788",
      "incomplete_value": true,
      "site": "00b057a4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b05778",
      "incomplete_value": true,
      "site": "00b057a4",
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
    "old": null,
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0577c",
      "incomplete_value": true,
      "site": "00b057a4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b0537c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b052ec.md#insn-00b0537c) · [`00b05308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b052ec.md#insn-00b05308) · [`00b0531c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b052ec.md#insn-00b0531c)
- 新版 `00b057a4`（命令位置の公開資料なし） · `00b05730`（命令位置の公開資料なし） · `00b05744`（命令位置の公開資料なし）

~~~diff
- 00b0537c ["INT_ADD", "register:40f0:8", ["const:b0537c:8", "const:4:8"]]
- 00b0537c ["CALL", null, ["callee:00afeae8:8"]]
+ 00b057a4 ["INT_ADD", "register:40f0:8", ["const:b057a4:8", "const:4:8"]]
+ 00b057a4 ["CALL", null, ["callee:00afeae8:8"]]
- 00b0537c bytes d1e4ff97
+ 00b057a4 bytes d1e4ff97
- 00b05308 ["INT_ADD", "register:40f0:8", ["const:b05308:8", "const:4:8"]]
- 00b05308 ["CALL", null, ["callee:008514f8:8"]]
+ 00b05730 ["INT_ADD", "register:40f0:8", ["const:b05730:8", "const:4:8"]]
+ 00b05730 ["CALL", null, ["callee:008514f8:8"]]
- 00b05308 bytes 6c30f597
+ 00b05730 bytes 722ff597
- 00b0531c ["INT_ADD", "register:40f0:8", ["const:b0531c:8", "const:4:8"]]
- 00b0531c ["CALL", null, ["callee:005e7420:8"]]
+ 00b05744 ["INT_ADD", "register:40f0:8", ["const:b05744:8", "const:4:8"]]
+ 00b05744 ["CALL", null, ["callee:005e7420:8"]]
- 00b0531c bytes 3188eb97
+ 00b05744 bytes 3787eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f7eec10a889146db3782d96d13fe5b"></a>

### [`00b05394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05394.md) → [`00b057bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b057bc.md) FUN_00b057bc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b057e0",
      "incomplete_value": true,
      "site": "00b057e4",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b053b8",
      "incomplete_value": true,
      "site": "00b053bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b053bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05394.md#insn-00b053bc) · [`00b053a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05394.md#insn-00b053a8) · [`00b053b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05394.md#insn-00b053b8)
- 新版 `00b057e4`（命令位置の公開資料なし） · `00b057d0`（命令位置の公開資料なし）

~~~diff
- 00b053bc ["INT_ADD", "register:40f0:8", ["const:b053bc:8", "const:4:8"]]
- 00b053bc ["CALL", null, ["callee:005e7420:8"]]
+ 00b057e4 ["INT_ADD", "register:40f0:8", ["const:b057e4:8", "const:4:8"]]
+ 00b057e4 ["CALL", null, ["callee:005e7420:8"]]
- 00b053bc bytes 0988eb97
+ 00b057e4 bytes 0f87eb97
- 00b053a8 ["INT_ADD", "register:40f0:8", ["const:b053a8:8", "const:4:8"]]
- 00b053a8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b057d0 ["INT_ADD", "register:40f0:8", ["const:b057d0:8", "const:4:8"]]
+ 00b057d0 ["CALL", null, ["callee:008514f8:8"]]
- 00b053a8 bytes 4430f597
+ 00b057d0 bytes 4a2ff597
- 00b053b8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b053b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b053b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b053b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b053b8 bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-838a42f18b5daa7da215b550466fc40f"></a>

### [`00b053f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b053f0.md) → [`00b05818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05818.md) FUN_00b05818

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b05410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b053f0.md#insn-00b05410) · [`00b05424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b053f0.md#insn-00b05424) · [`00b0542c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b053f0.md#insn-00b0542c)
- 新版 `00b05838`（命令位置の公開資料なし） · `00b0584c`（命令位置の公開資料なし） · `00b05854`（命令位置の公開資料なし）

~~~diff
- 00b05410 ["INT_ADD", "register:40f0:8", ["const:b05410:8", "const:4:8"]]
- 00b05410 ["CALL", null, ["callee:008514f8:8"]]
+ 00b05838 ["INT_ADD", "register:40f0:8", ["const:b05838:8", "const:4:8"]]
+ 00b05838 ["CALL", null, ["callee:008514f8:8"]]
- 00b05410 bytes 2a30f597
+ 00b05838 bytes 302ff597
- 00b05424 ["INT_ADD", "register:40f0:8", ["const:b05424:8", "const:4:8"]]
- 00b05424 ["CALL", null, ["callee:005e7420:8"]]
+ 00b0584c ["INT_ADD", "register:40f0:8", ["const:b0584c:8", "const:4:8"]]
+ 00b0584c ["CALL", null, ["callee:005e7420:8"]]
- 00b05424 bytes ef87eb97
+ 00b0584c bytes f586eb97
- 00b0542c ["INT_ADD", "register:40f0:8", ["const:b0542c:8", "const:4:8"]]
- 00b0542c ["CALL", null, ["callee:008514f8:8"]]
+ 00b05854 ["INT_ADD", "register:40f0:8", ["const:b05854:8", "const:4:8"]]
+ 00b05854 ["CALL", null, ["callee:008514f8:8"]]
- 00b0542c bytes 2330f597
+ 00b05854 bytes 292ff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5095e62b5ae478032295bbe72148a6"></a>

### [`00b054c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b054c0.md) → [`00b058e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b058e8.md) FUN_00b058e8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 25.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b054c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b054c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b054c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b054c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b054c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b054c8",
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
      "00b058e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b058ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b058f0",
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

- 旧版 [`00b054c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b054c0.md#insn-00b054c0) · [`00b054c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b054c0.md#insn-00b054c4) · [`00b054c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b054c0.md#insn-00b054c8)

~~~diff
- 00b054c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b054c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b054c0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b054c0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b054c0 bytes fd7bbca9
- 00b054c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b054c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b054c4 bytes f70b00f9
- 00b054c8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b054c8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b054c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b054c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b054c8 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcc4208a3ac9107a2b948f6dfefea90d"></a>

### [`00b05590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05590.md) → [`00b059b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b059b8.md) FUN_00b059b8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b055b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05590.md#insn-00b055b0) · [`00b055c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05590.md#insn-00b055c4) · [`00b055cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05590.md#insn-00b055cc)
- 新版 `00b059d8`（命令位置の公開資料なし） · `00b059ec`（命令位置の公開資料なし） · `00b059f4`（命令位置の公開資料なし）

~~~diff
- 00b055b0 ["INT_ADD", "register:40f0:8", ["const:b055b0:8", "const:4:8"]]
- 00b055b0 ["CALL", null, ["callee:008514f8:8"]]
+ 00b059d8 ["INT_ADD", "register:40f0:8", ["const:b059d8:8", "const:4:8"]]
+ 00b059d8 ["CALL", null, ["callee:008514f8:8"]]
- 00b055b0 bytes c22ff597
+ 00b059d8 bytes c82ef597
- 00b055c4 ["INT_ADD", "register:40f0:8", ["const:b055c4:8", "const:4:8"]]
- 00b055c4 ["CALL", null, ["callee:005e7420:8"]]
+ 00b059ec ["INT_ADD", "register:40f0:8", ["const:b059ec:8", "const:4:8"]]
+ 00b059ec ["CALL", null, ["callee:005e7420:8"]]
- 00b055c4 bytes 8787eb97
+ 00b059ec bytes 8d86eb97
- 00b055cc ["INT_ADD", "register:40f0:8", ["const:b055cc:8", "const:4:8"]]
- 00b055cc ["CALL", null, ["callee:008514f8:8"]]
+ 00b059f4 ["INT_ADD", "register:40f0:8", ["const:b059f4:8", "const:4:8"]]
+ 00b059f4 ["CALL", null, ["callee:008514f8:8"]]
- 00b055cc bytes bb2ff597
+ 00b059f4 bytes c12ef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7db979a325eabe693888fa137395a298"></a>

### [`00b05774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05774.md) → [`00b05b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05b9c.md) FUN_00b05b9c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05774"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05774"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05778"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05774",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05778",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0577c",
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
      "00b05b9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b05ba0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b05ba4",
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

- 旧版 [`00b05774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05774.md#insn-00b05774) · [`00b05778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05774.md#insn-00b05778) · [`00b0577c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05774.md#insn-00b0577c)

~~~diff
- 00b05774 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05774 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05774 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b05774 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05774 bytes fd7bbda9
- 00b05778 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b05778 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b05778 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05778 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05778 bytes f65701a9
- 00b0577c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b0577c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b0577c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b0577c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0577c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-754d2a6d95355edf9567036e8cde1bc5"></a>

### [`00b058c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b058c4.md) → [`00b05cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05cec.md) FUN_00b05cec

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`00685548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685548.md) [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 4件 [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b058e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b058c4.md#insn-00b058e0) · [`00b058f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b058c4.md#insn-00b058f4) · [`00b058f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b058c4.md#insn-00b058f8)
- 新版 `00b05d08`（命令位置の公開資料なし） · `00b05d1c`（命令位置の公開資料なし） · `00b05d20`（命令位置の公開資料なし）

~~~diff
- 00b058e0 ["INT_ADD", "register:40f0:8", ["const:b058e0:8", "const:4:8"]]
- 00b058e0 ["CALL", null, ["callee:008514f8:8"]]
+ 00b05d08 ["INT_ADD", "register:40f0:8", ["const:b05d08:8", "const:4:8"]]
+ 00b05d08 ["CALL", null, ["callee:008514f8:8"]]
- 00b058e0 bytes f62ef597
+ 00b05d08 bytes fc2df597
- 00b058f4 ["INT_ADD", "register:40f0:8", ["const:b058f4:8", "const:4:8"]]
- 00b058f4 ["CALL", null, ["callee:005e7420:8"]]
+ 00b05d1c ["INT_ADD", "register:40f0:8", ["const:b05d1c:8", "const:4:8"]]
+ 00b05d1c ["CALL", null, ["callee:005e7420:8"]]
- 00b058f4 bytes bb86eb97
+ 00b05d1c bytes c185eb97
- 00b058f8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b058f8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b058f8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b058f8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b05d20 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b05d20 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b05d20 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b05d20 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b058f8 bytes 60000037
+ 00b05d20 bytes 60000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ab2fbbc7fc7cdb752a2c75c78f350ae"></a>

### [`00b05950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05950.md) → [`00b05d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05d78.md) FUN_00b05d78

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 5件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`0066a3c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a3c8.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 5件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`0066a408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0066a/0066a408.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 14.29% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b0599c",
      "incomplete_value": true,
      "site": "00b059bc",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
      "definition_site": "00b05994",
      "incomplete_value": true,
      "site": "00b059bc",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b059a0",
      "incomplete_value": true,
      "site": "00b059bc",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b059bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05950.md#insn-00b059bc) · [`00b05a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05950.md#insn-00b05a08)
- 新版 `00b05de4`（命令位置の公開資料なし） · `00b05e30`（命令位置の公開資料なし）

~~~diff
- 00b059bc ["INT_ADD", "register:40f0:8", ["const:b059bc:8", "const:4:8"]]
- 00b059bc ["CALL", null, ["callee:00afeae8:8"]]
+ 00b05de4 ["INT_ADD", "register:40f0:8", ["const:b05de4:8", "const:4:8"]]
+ 00b05de4 ["CALL", null, ["callee:00afeae8:8"]]
- 00b059bc bytes 41e3ff97
+ 00b05de4 bytes 41e3ff97
- 00b05a08 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b05a08 ["RETURN", null, ["register:0:8"]]
- 00b05a08 bytes c0035fd6
+ 00b05e30 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b05e30 ["RETURN", null, ["register:0:8"]]
+ 00b05e30 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-448387abe5f6005d43efe35601f0522c"></a>

### [`00b05a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05a0c.md) → [`00b05e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05e34.md) FUN_00b05e34

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 20.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b05a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05a0c.md#insn-00b05a28) · [`00b05a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05a0c.md#insn-00b05a3c) · [`00b05a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05a0c.md#insn-00b05a44)
- 新版 `00b05e50`（命令位置の公開資料なし） · `00b05e64`（命令位置の公開資料なし） · `00b05e6c`（命令位置の公開資料なし）

~~~diff
- 00b05a28 ["INT_ADD", "register:40f0:8", ["const:b05a28:8", "const:4:8"]]
- 00b05a28 ["CALL", null, ["callee:008514f8:8"]]
+ 00b05e50 ["INT_ADD", "register:40f0:8", ["const:b05e50:8", "const:4:8"]]
+ 00b05e50 ["CALL", null, ["callee:008514f8:8"]]
- 00b05a28 bytes a42ef597
+ 00b05e50 bytes aa2df597
- 00b05a3c ["INT_ADD", "register:40f0:8", ["const:b05a3c:8", "const:4:8"]]
- 00b05a3c ["CALL", null, ["callee:005e7420:8"]]
+ 00b05e64 ["INT_ADD", "register:40f0:8", ["const:b05e64:8", "const:4:8"]]
+ 00b05e64 ["CALL", null, ["callee:005e7420:8"]]
- 00b05a3c bytes 6986eb97
+ 00b05e64 bytes 6f85eb97
- 00b05a44 ["INT_ADD", "register:40f0:8", ["const:b05a44:8", "const:4:8"]]
- 00b05a44 ["CALL", null, ["callee:008514f8:8"]]
+ 00b05e6c ["INT_ADD", "register:40f0:8", ["const:b05e6c:8", "const:4:8"]]
+ 00b05e6c ["CALL", null, ["callee:008514f8:8"]]
- 00b05a44 bytes 9d2ef597
+ 00b05e6c bytes a32df597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4a03e0ba57a34e0590cba5b6bd8cc3a"></a>

### [`00b05ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05ab4.md) → [`00b05edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05edc.md) FUN_00b05edc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b05b28",
      "incomplete_value": true,
      "site": "00b05b44",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
      "definition_site": "00b05b18",
      "incomplete_value": true,
      "site": "00b05b44",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b05b1c",
      "incomplete_value": true,
      "site": "00b05b44",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b05b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05ab4.md#insn-00b05b44) · [`00b05ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05ab4.md#insn-00b05ad0) · [`00b05ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05ab4.md#insn-00b05ae4)
- 新版 `00b05f6c`（命令位置の公開資料なし） · `00b05ef8`（命令位置の公開資料なし） · `00b05f0c`（命令位置の公開資料なし）

~~~diff
- 00b05b44 ["INT_ADD", "register:40f0:8", ["const:b05b44:8", "const:4:8"]]
- 00b05b44 ["CALL", null, ["callee:00afeae8:8"]]
+ 00b05f6c ["INT_ADD", "register:40f0:8", ["const:b05f6c:8", "const:4:8"]]
+ 00b05f6c ["CALL", null, ["callee:00afeae8:8"]]
- 00b05b44 bytes dfe2ff97
+ 00b05f6c bytes dfe2ff97
- 00b05ad0 ["INT_ADD", "register:40f0:8", ["const:b05ad0:8", "const:4:8"]]
- 00b05ad0 ["CALL", null, ["callee:008514f8:8"]]
+ 00b05ef8 ["INT_ADD", "register:40f0:8", ["const:b05ef8:8", "const:4:8"]]
+ 00b05ef8 ["CALL", null, ["callee:008514f8:8"]]
- 00b05ad0 bytes 7a2ef597
+ 00b05ef8 bytes 802df597
- 00b05ae4 ["INT_ADD", "register:40f0:8", ["const:b05ae4:8", "const:4:8"]]
- 00b05ae4 ["CALL", null, ["callee:005e7420:8"]]
+ 00b05f0c ["INT_ADD", "register:40f0:8", ["const:b05f0c:8", "const:4:8"]]
+ 00b05f0c ["CALL", null, ["callee:005e7420:8"]]
- 00b05ae4 bytes 3f86eb97
+ 00b05f0c bytes 4585eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80dcaed81cfeb25547b98ad03e86f887"></a>

### [`00b05b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05b5c.md) → [`00b05f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05f84.md) FUN_00b05f84

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 20.00% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b05bd0",
      "incomplete_value": true,
      "site": "00b05bec",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
      "definition_site": "00b05bc0",
      "incomplete_value": true,
      "site": "00b05bec",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b05bc4",
      "incomplete_value": true,
      "site": "00b05bec",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b05bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05b5c.md#insn-00b05bec) · [`00b05b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05b5c.md#insn-00b05b78) · [`00b05b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05b5c.md#insn-00b05b8c)
- 新版 `00b06014`（命令位置の公開資料なし） · `00b05fa0`（命令位置の公開資料なし） · `00b05fb4`（命令位置の公開資料なし）

~~~diff
- 00b05bec ["INT_ADD", "register:40f0:8", ["const:b05bec:8", "const:4:8"]]
- 00b05bec ["CALL", null, ["callee:00afeae8:8"]]
+ 00b06014 ["INT_ADD", "register:40f0:8", ["const:b06014:8", "const:4:8"]]
+ 00b06014 ["CALL", null, ["callee:00afeae8:8"]]
- 00b05bec bytes b5e2ff97
+ 00b06014 bytes b5e2ff97
- 00b05b78 ["INT_ADD", "register:40f0:8", ["const:b05b78:8", "const:4:8"]]
- 00b05b78 ["CALL", null, ["callee:008514f8:8"]]
+ 00b05fa0 ["INT_ADD", "register:40f0:8", ["const:b05fa0:8", "const:4:8"]]
+ 00b05fa0 ["CALL", null, ["callee:008514f8:8"]]
- 00b05b78 bytes 502ef597
+ 00b05fa0 bytes 562df597
- 00b05b8c ["INT_ADD", "register:40f0:8", ["const:b05b8c:8", "const:4:8"]]
- 00b05b8c ["CALL", null, ["callee:005e7420:8"]]
+ 00b05fb4 ["INT_ADD", "register:40f0:8", ["const:b05fb4:8", "const:4:8"]]
+ 00b05fb4 ["CALL", null, ["callee:005e7420:8"]]
- 00b05b8c bytes 1586eb97
+ 00b05fb4 bytes 1b85eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df29a1c2948306fac13dce4d506fc954"></a>

### [`00b05c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05c04.md) → [`00b0602c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0602c.md) FUN_00b0602c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 5件 [`0046da7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da7c.md) [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md) [`00b02304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b02/00b02304.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 5件 [`0046dabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046dabc.md) [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 98.53% / 新版 98.53%

CFGの説明率　旧版 8.33% / 新版 9.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b060ec",
      "incomplete_value": true,
      "site": "00b060fc",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b060f0",
      "incomplete_value": true,
      "site": "00b060fc",
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
    "old": null,
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00b05c60",
      "incomplete_value": true,
      "site": "00b05c74",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b05cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05c04.md#insn-00b05cd4) · [`00b05c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05c04.md#insn-00b05c24) · [`00b05c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05c04.md#insn-00b05c38)
- 新版 `00b060fc`（命令位置の公開資料なし） · `00b0604c`（命令位置の公開資料なし） · `00b06060`（命令位置の公開資料なし）

~~~diff
- 00b05cd4 ["INT_ADD", "register:40f0:8", ["const:b05cd4:8", "const:4:8"]]
- 00b05cd4 ["CALL", null, ["callee:00b0272c:8"]]
+ 00b060fc ["INT_ADD", "register:40f0:8", ["const:b060fc:8", "const:4:8"]]
+ 00b060fc ["CALL", null, ["callee:00b0272c:8"]]
- 00b05cd4 bytes 8cf1ff97
+ 00b060fc bytes 8cf1ff97
- 00b05c24 ["INT_ADD", "register:40f0:8", ["const:b05c24:8", "const:4:8"]]
- 00b05c24 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0604c ["INT_ADD", "register:40f0:8", ["const:b0604c:8", "const:4:8"]]
+ 00b0604c ["CALL", null, ["callee:008514f8:8"]]
- 00b05c24 bytes 252ef597
+ 00b0604c bytes 2b2df597
- 00b05c38 ["INT_ADD", "register:40f0:8", ["const:b05c38:8", "const:4:8"]]
- 00b05c38 ["CALL", null, ["callee:005e7420:8"]]
+ 00b06060 ["INT_ADD", "register:40f0:8", ["const:b06060:8", "const:4:8"]]
+ 00b06060 ["CALL", null, ["callee:005e7420:8"]]
- 00b05c38 bytes ea85eb97
+ 00b06060 bytes f084eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67170daafec230d7033b7362a9e09fe5"></a>

### [`00b05d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05d14.md) → [`00b0613c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0613c.md) FUN_00b0613c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05d14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05d14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05d18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05d14",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05d18",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05d1c",
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
      "00b0613c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b06140",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b06144",
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

- 旧版 [`00b05d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05d14.md#insn-00b05d14) · [`00b05d18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05d14.md#insn-00b05d18) · [`00b05d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05d14.md#insn-00b05d1c)

~~~diff
- 00b05d14 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05d14 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05d14 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b05d14 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05d14 bytes fd7bbda9
- 00b05d18 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b05d18 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b05d18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05d18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05d18 bytes f65701a9
- 00b05d1c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b05d1c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b05d1c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b05d1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05d1c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-668599d046839c7aa6f1a6996fd59b29"></a>

### [`00b05dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05dbc.md) → [`00b061e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b061e4.md) FUN_00b061e4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 2件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05dbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05dbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05dc0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05dbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05dc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05dc4",
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
      "00b061e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b061e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b061ec",
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

- 旧版 [`00b05dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05dbc.md#insn-00b05dbc) · [`00b05dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05dbc.md#insn-00b05dc0) · [`00b05dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05dbc.md#insn-00b05dc4)

~~~diff
- 00b05dbc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05dbc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05dbc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b05dbc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05dbc bytes fd7bbda9
- 00b05dc0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b05dc0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b05dc0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05dc0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05dc0 bytes f65701a9
- 00b05dc4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b05dc4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b05dc4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b05dc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05dc4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a67890409381bfb85917c62201fd4960"></a>

### [`00b05e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05e64.md) → [`00b0628c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0628c.md) FUN_00b0628c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 14.29% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05e68"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05e68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05e6c",
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
      "00b0628c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b06290",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b06294",
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

- 旧版 [`00b05e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05e64.md#insn-00b05e64) · [`00b05e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05e64.md#insn-00b05e68) · [`00b05e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05e64.md#insn-00b05e6c)

~~~diff
- 00b05e64 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05e64 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05e64 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b05e64 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05e64 bytes fd7bbda9
- 00b05e68 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b05e68 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b05e68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05e68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05e68 bytes f65701a9
- 00b05e6c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b05e6c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b05e6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b05e6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05e6c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-810e2eaea4549771ec9f11d8f6374eff"></a>

### [`00b05f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05f0c.md) → [`00b06334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b06334.md) FUN_00b06334

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b06360",
      "incomplete_value": true,
      "site": "00b06364",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b05f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05f0c.md#insn-00b05f3c) · [`00b05f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05f0c.md#insn-00b05f28) · [`00b05f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05f0c.md#insn-00b05f40)
- 新版 `00b06364`（命令位置の公開資料なし） · `00b06350`（命令位置の公開資料なし） · `00b06368`（命令位置の公開資料なし）

~~~diff
- 00b05f3c ["INT_ADD", "register:40f0:8", ["const:b05f3c:8", "const:4:8"]]
- 00b05f3c ["CALL", null, ["callee:005e7420:8"]]
+ 00b06364 ["INT_ADD", "register:40f0:8", ["const:b06364:8", "const:4:8"]]
+ 00b06364 ["CALL", null, ["callee:005e7420:8"]]
- 00b05f3c bytes 2985eb97
+ 00b06364 bytes 2f84eb97
- 00b05f28 ["INT_ADD", "register:40f0:8", ["const:b05f28:8", "const:4:8"]]
- 00b05f28 ["CALL", null, ["callee:008514f8:8"]]
+ 00b06350 ["INT_ADD", "register:40f0:8", ["const:b06350:8", "const:4:8"]]
+ 00b06350 ["CALL", null, ["callee:008514f8:8"]]
- 00b05f28 bytes 642df597
+ 00b06350 bytes 6a2cf597
- 00b05f40 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b05f40 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b05f40 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b05f40 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b06368 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b06368 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b06368 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b06368 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b05f40 bytes 60000037
+ 00b06368 bytes 60000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-502e0d4e463b1c1edd7ce452c95b9fc7"></a>

### [`00b05f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05f98.md) → [`00b063c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b063c0.md) FUN_00b063c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00afe6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b05fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05f98.md#insn-00b05fb4) · [`00b05fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05f98.md#insn-00b05fc8) · [`00b05fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b05/00b05f98.md#insn-00b05fd8)
- 新版 `00b063dc`（命令位置の公開資料なし） · `00b063f0`（命令位置の公開資料なし） · `00b06400`（命令位置の公開資料なし）

~~~diff
- 00b05fb4 ["INT_ADD", "register:40f0:8", ["const:b05fb4:8", "const:4:8"]]
- 00b05fb4 ["CALL", null, ["callee:008514f8:8"]]
+ 00b063dc ["INT_ADD", "register:40f0:8", ["const:b063dc:8", "const:4:8"]]
+ 00b063dc ["CALL", null, ["callee:008514f8:8"]]
- 00b05fb4 bytes 412df597
+ 00b063dc bytes 472cf597
- 00b05fc8 ["INT_ADD", "register:40f0:8", ["const:b05fc8:8", "const:4:8"]]
- 00b05fc8 ["CALL", null, ["callee:005e7420:8"]]
+ 00b063f0 ["INT_ADD", "register:40f0:8", ["const:b063f0:8", "const:4:8"]]
+ 00b063f0 ["CALL", null, ["callee:005e7420:8"]]
- 00b05fc8 bytes 0685eb97
+ 00b063f0 bytes 0c84eb97
- 00b05fd8 ["INT_ADD", "register:40f0:8", ["const:b05fd8:8", "const:4:8"]]
- 00b05fd8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b06400 ["INT_ADD", "register:40f0:8", ["const:b06400:8", "const:4:8"]]
+ 00b06400 ["CALL", null, ["callee:008514f8:8"]]
- 00b05fd8 bytes 382df597
+ 00b06400 bytes 3e2cf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d75cca0f6fbd374a770f6664186eaa1"></a>

### [`00b06024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06024.md) → [`00b0644c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0644c.md) FUN_00b0644c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 2件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b06038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06024.md#insn-00b06038) · [`00b0604c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06024.md#insn-00b0604c) · [`00b06050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06024.md#insn-00b06050)
- 新版 `00b06460`（命令位置の公開資料なし） · `00b06474`（命令位置の公開資料なし） · `00b06478`（命令位置の公開資料なし）

~~~diff
- 00b06038 ["INT_ADD", "register:40f0:8", ["const:b06038:8", "const:4:8"]]
- 00b06038 ["CALL", null, ["callee:008514f8:8"]]
+ 00b06460 ["INT_ADD", "register:40f0:8", ["const:b06460:8", "const:4:8"]]
+ 00b06460 ["CALL", null, ["callee:008514f8:8"]]
- 00b06038 bytes 202df597
+ 00b06460 bytes 262cf597
- 00b0604c ["INT_ADD", "register:40f0:8", ["const:b0604c:8", "const:4:8"]]
- 00b0604c ["CALL", null, ["callee:005e7420:8"]]
+ 00b06474 ["INT_ADD", "register:40f0:8", ["const:b06474:8", "const:4:8"]]
+ 00b06474 ["CALL", null, ["callee:005e7420:8"]]
- 00b0604c bytes e584eb97
+ 00b06474 bytes eb83eb97
- 00b06050 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b06050 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b06050 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b06050 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b06478 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b06478 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b06478 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b06478 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b06050 bytes 00010037
+ 00b06478 bytes 00010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb7092a127dde8f18275e7f4225082ab"></a>

### [`00b06080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06080.md) → [`00b064a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b064a8.md) FUN_00b064a8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 2件 [`005e73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e73e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 20.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b064cc",
      "incomplete_value": true,
      "site": "00b064d0",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b060a4",
      "incomplete_value": true,
      "site": "00b060a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b060a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06080.md#insn-00b060a8) · [`00b06094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06080.md#insn-00b06094) · [`00b060a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06080.md#insn-00b060a4)
- 新版 `00b064d0`（命令位置の公開資料なし） · `00b064bc`（命令位置の公開資料なし）

~~~diff
- 00b060a8 ["INT_ADD", "register:40f0:8", ["const:b060a8:8", "const:4:8"]]
- 00b060a8 ["CALL", null, ["callee:005e7420:8"]]
+ 00b064d0 ["INT_ADD", "register:40f0:8", ["const:b064d0:8", "const:4:8"]]
+ 00b064d0 ["CALL", null, ["callee:005e7420:8"]]
- 00b060a8 bytes ce84eb97
+ 00b064d0 bytes d483eb97
- 00b06094 ["INT_ADD", "register:40f0:8", ["const:b06094:8", "const:4:8"]]
- 00b06094 ["CALL", null, ["callee:008514f8:8"]]
+ 00b064bc ["INT_ADD", "register:40f0:8", ["const:b064bc:8", "const:4:8"]]
+ 00b064bc ["CALL", null, ["callee:008514f8:8"]]
- 00b06094 bytes 092df597
+ 00b064bc bytes 0f2cf597
- 00b060a4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b060a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b060a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b060a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b060a4 bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19425fc35e6dbed4f20a2ef807d892ae"></a>

### [`00b06534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06534.md) → [`00b0695c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0695c.md) FUN_00b0695c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006c6dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c6/006c6dd0.md) [`006cb190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cb/006cb190.md) · 呼出先 10件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00853c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c30.md) [`00903da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00903/00903da8.md) [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md)
- 新版 呼出元 2件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`006cb1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cb/006cb1d0.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00853c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c70.md) [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.96% / 新版 46.96%

CFGの説明率　旧版 33.86% / 新版 33.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 38件, `unresolved_call_alignment` 19件, `unresolved_store_alignment` 42件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b06708"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0671c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0671c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b065e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0698c"
      ]
    ],
    [
      "00b06ae4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b066d8"
      ]
    ],
    [
      "unmatched:00b066c8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b066f8"
      ]
    ]
  ],
  "added": [
    [
      "00b06a0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0698c"
      ]
    ],
    [
      "00b06ae4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b06b00"
      ]
    ],
    [
      "00b06af0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b06b20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06534.md#insn-00b06668) · [`00b06708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06534.md#insn-00b06708) · [`00b0671c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b06/00b06534.md#insn-00b0671c)
- 新版 `00b06a90`（命令位置の公開資料なし）

~~~diff
- 00b06668 ["INT_ADD", "register:40f0:8", ["const:b06668:8", "const:4:8"]]
- 00b06668 ["CALL", null, ["callee:00c57eb0:8"]]
+ 00b06a90 ["INT_ADD", "register:40f0:8", ["const:b06a90:8", "const:4:8"]]
+ 00b06a90 ["CALL", null, ["callee:00c57eb0:8"]]
- 00b06668 bytes 12450594
+ 00b06a90 bytes 08450594
- 00b06708 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:1c:8"]]
- 00b06708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00b06708 bytes 141c00b9
- 00b0671c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b0671c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b0671c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b0671c ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b0671c bytes bf7e00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7468fe79ee2ebe26353b3b3c4506cc88"></a>

### [`00b071b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b071b0.md) → [`00b075d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b075d8.md) _INIT_252

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00b07614",
      "incomplete_value": true,
      "site": "00b07630",
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
      "definition_site": "00b071ec",
      "incomplete_value": true,
      "site": "00b07208",
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
      "definition_site": "00b07638",
      "incomplete_value": true,
      "site": "00b07654",
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
      "definition_site": "00b07210",
      "incomplete_value": true,
      "site": "00b0722c",
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
      "definition_site": "00b07658",
      "incomplete_value": true,
      "site": "00b07674",
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
      "definition_site": "00b07230",
      "incomplete_value": true,
      "site": "00b0724c",
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
      "00b07614",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00b07638",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00b07658",
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
      "00b07614",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b07638",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b07658",
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

- 旧版 [`00b07310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b071b0.md#insn-00b07310) · [`00b073e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b071b0.md#insn-00b073e4) · [`00b071dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b071b0.md#insn-00b071dc)
- 新版 `00b07738`（命令位置の公開資料なし） · `00b0780c`（命令位置の公開資料なし） · `00b07604`（命令位置の公開資料なし）

~~~diff
- 00b07310 ["INT_ADD", "register:40f0:8", ["const:b07310:8", "const:4:8"]]
- 00b07310 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00b07738 ["INT_ADD", "register:40f0:8", ["const:b07738:8", "const:4:8"]]
+ 00b07738 ["CALL", null, ["callee:0043b7f8:8"]]
- 00b07310 bytes 2ad1e497
+ 00b07738 bytes 30d0e497
- 00b073e4 ["INT_ADD", "register:40f0:8", ["const:b073e4:8", "const:4:8"]]
- 00b073e4 ["CALL", null, ["callee:00c57e30:8"]]
+ 00b0780c ["INT_ADD", "register:40f0:8", ["const:b0780c:8", "const:4:8"]]
+ 00b0780c ["CALL", null, ["callee:00c57e30:8"]]
- 00b073e4 bytes 93410594
+ 00b0780c bytes 89410594
- 00b071dc ["COPY", "tmp:0:8", ["const:968:8"]]
- 00b071dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b071dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b071dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b07604 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00b07604 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b07604 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b07604 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b071dc bytes 73a22591
+ 00b07604 bytes 73a23591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8976941fe9a4b4c12410b76fda49d107"></a>

### [`00b075a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b075a0.md) → [`00b079c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b079c8.md) FUN_00b079c8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 25件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00446d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446d30.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 25件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00446d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.84% / 新版 97.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 8件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b07a0c",
      "incomplete_value": false,
      "site": "00b07a14",
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
      "definition_site": "00b075e4",
      "incomplete_value": false,
      "site": "00b075ec",
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
      "definition_site": "00b07a78",
      "incomplete_value": true,
      "site": "00b07a78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:253:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b07650",
      "incomplete_value": true,
      "site": "00b07650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:213:8"
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
      "definition_site": "00b07b00",
      "incomplete_value": true,
      "site": "00b07b0c",
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
                "const:9e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b076d8",
      "incomplete_value": true,
      "site": "00b076e4",
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
                "const:91c:8"
              ]
            ]
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
      "00b07a14",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00b07a74",
      "READ",
      [
        "storage",
        "002af213",
        null,
        "string"
      ]
    ],
    [
      "00b07b00",
      "READ",
      [
        "storage",
        "002a091c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b07a14",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00b07a74",
      "READ",
      [
        "storage",
        "002af253",
        null,
        "string"
      ]
    ],
    [
      "00b07b00",
      "READ",
      [
        "storage",
        "002a09e9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b08694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b075a0.md#insn-00b08694) · [`00b075dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b075a0.md#insn-00b075dc) · [`00b075e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b075a0.md#insn-00b075e4)
- 新版 `00b08abc`（命令位置の公開資料なし） · `00b07a04`（命令位置の公開資料なし） · `00b07a0c`（命令位置の公開資料なし）

~~~diff
- 00b08694 ["INT_ADD", "register:40f0:8", ["const:b08694:8", "const:4:8"]]
- 00b08694 ["CALL", null, ["callee:00442930:8"]]
+ 00b08abc ["INT_ADD", "register:40f0:8", ["const:b08abc:8", "const:4:8"]]
+ 00b08abc ["CALL", null, ["callee:00442930:8"]]
- 00b08694 bytes 97e8e497
+ 00b08abc bytes 9de7e497
- 00b075dc ["INT_ADD", "register:40f0:8", ["const:b075dc:8", "const:4:8"]]
- 00b075dc ["CALL", null, ["callee:00487e20:8"]]
+ 00b07a04 ["INT_ADD", "register:40f0:8", ["const:b07a04:8", "const:4:8"]]
+ 00b07a04 ["CALL", null, ["callee:00487e20:8"]]
- 00b075dc bytes 0102e697
+ 00b07a04 bytes 0701e697
- 00b075e4 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00b075e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b075e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b075e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b07a0c ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00b07a0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b07a0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b07a0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b075e4 bytes 08e12491
+ 00b07a0c bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f9e5bb97a6d8f76f4e16494df0ae830"></a>

### [`00b08d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08d78.md) → [`00b091a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b091a0.md) FUN_00b091a0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00963e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00963/00963e3c.md) · 呼出先 2件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 1件 [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) · 呼出先 2件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b09204",
      "incomplete_value": false,
      "site": "00b09208",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b08ddc",
      "incomplete_value": false,
      "site": "00b08de0",
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
            "const:f0:8"
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
      "00b09204",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b09204",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b08de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08d78.md#insn-00b08de0) · [`00b08ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08d78.md#insn-00b08ddc) · [`00b08de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08d78.md#insn-00b08de4)
- 新版 `00b09208`（命令位置の公開資料なし） · `00b09204`（命令位置の公開資料なし） · `00b0920c`（命令位置の公開資料なし）

~~~diff
- 00b08de0 ["INT_ADD", "register:40f0:8", ["const:b08de0:8", "const:4:8"]]
- 00b08de0 ["CALL", null, ["callee:00442930:8"]]
+ 00b09208 ["INT_ADD", "register:40f0:8", ["const:b09208:8", "const:4:8"]]
+ 00b09208 ["CALL", null, ["callee:00442930:8"]]
- 00b08de0 bytes c4e6e497
+ 00b09208 bytes cae5e497
- 00b08ddc ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00b08ddc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b08ddc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b08ddc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b09204 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00b09204 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b09204 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b09204 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b08ddc bytes 00c00391
+ 00b09204 bytes 00f40691
- 00b08de4 ["INT_ADD", "register:40f0:8", ["const:b08de4:8", "const:4:8"]]
- 00b08de4 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0920c ["INT_ADD", "register:40f0:8", ["const:b0920c:8", "const:4:8"]]
+ 00b0920c ["CALL", null, ["callee:008514f8:8"]]
- 00b08de4 bytes b521f597
+ 00b0920c bytes bb20f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7eb222f647a7c441fab219aaab96158"></a>

### [`00b08e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08e4c.md) → [`00b09274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09274.md) _INIT_253

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00b092b0",
      "incomplete_value": true,
      "site": "00b092cc",
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
      "definition_site": "00b08e88",
      "incomplete_value": true,
      "site": "00b08ea4",
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
      "definition_site": "00b092d4",
      "incomplete_value": true,
      "site": "00b092f0",
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
      "definition_site": "00b08eac",
      "incomplete_value": true,
      "site": "00b08ec8",
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
      "definition_site": "00b092f4",
      "incomplete_value": true,
      "site": "00b09310",
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
      "definition_site": "00b08ecc",
      "incomplete_value": true,
      "site": "00b08ee8",
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
      "00b092b0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00b092d4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00b092f4",
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
      "00b092b0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b092d4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b092f4",
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

- 旧版 [`00b08fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08e4c.md#insn-00b08fac) · [`00b09080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08e4c.md#insn-00b09080) · [`00b08e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b08/00b08e4c.md#insn-00b08e78)
- 新版 `00b093d4`（命令位置の公開資料なし） · `00b094a8`（命令位置の公開資料なし） · `00b092a0`（命令位置の公開資料なし）

~~~diff
- 00b08fac ["INT_ADD", "register:40f0:8", ["const:b08fac:8", "const:4:8"]]
- 00b08fac ["CALL", null, ["callee:0043b7f8:8"]]
+ 00b093d4 ["INT_ADD", "register:40f0:8", ["const:b093d4:8", "const:4:8"]]
+ 00b093d4 ["CALL", null, ["callee:0043b7f8:8"]]
- 00b08fac bytes 03cae497
+ 00b093d4 bytes 09c9e497
- 00b09080 ["INT_ADD", "register:40f0:8", ["const:b09080:8", "const:4:8"]]
- 00b09080 ["CALL", null, ["callee:00c57e30:8"]]
+ 00b094a8 ["INT_ADD", "register:40f0:8", ["const:b094a8:8", "const:4:8"]]
+ 00b094a8 ["CALL", null, ["callee:00c57e30:8"]]
- 00b09080 bytes 6c3a0594
+ 00b094a8 bytes 623a0594
- 00b08e78 ["COPY", "tmp:0:8", ["const:980:8"]]
- 00b08e78 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b08e78 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b08e78 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b092a0 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00b092a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b092a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b092a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b08e78 bytes 73022691
+ 00b092a0 bytes 73023691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cc417223b638323960a2ec5583ea172"></a>

### [`00b0b218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b218.md) → [`00b0b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md) FUN_00b0b640

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`00aefbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefbb0.md) [`00b0ccac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0ccac.md) [`00b0cdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cdc8.md) · 呼出先 32件 [`0046dab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dab4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md)
- 新版 呼出元 4件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00aeffd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aeffd8.md) [`00b0d0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d0d4.md) [`00b0d1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d1f0.md) · 呼出先 32件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 94.29% / 新版 90.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0b6a4",
      "incomplete_value": false,
      "site": "00b0b6a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0b27c",
      "incomplete_value": false,
      "site": "00b0b27c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0b6dc",
      "incomplete_value": false,
      "site": "00b0b6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0b2b4",
      "incomplete_value": false,
      "site": "00b0b2b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0b6fc",
      "incomplete_value": false,
      "site": "00b0b6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0b2d4",
      "incomplete_value": false,
      "site": "00b0b2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0b6a4",
      "DATA",
      [
        "storage",
        "00c8e9f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0b6dc",
      "DATA",
      [
        "storage",
        "00c8eb78",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0b6fc",
      "DATA",
      [
        "storage",
        "00c8ebf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0b6a4",
      "DATA",
      [
        "storage",
        "00c8edf8",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0b6dc",
      "DATA",
      [
        "storage",
        "00c8ef78",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0b6fc",
      "DATA",
      [
        "storage",
        "00c8eff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b218.md#insn-00b0b5d4) · [`00b0b5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b218.md#insn-00b0b5dc) · [`00b0b5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b218.md#insn-00b0b5fc)
- 新版 `00b0ba24`（命令位置の公開資料なし）

~~~diff
- 00b0b5d4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b0b5d4 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00b0b5d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b0b5d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0b5d4 bytes e85304a9
- 00b0b5dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b0b5dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b0b5dc bytes f53300f9
- 00b0b5fc ["INT_ADD", "register:40f0:8", ["const:b0b5fc:8", "const:4:8"]]
- 00b0b5fc ["CALL", null, ["callee:008b6fec:8"]]
+ 00b0ba24 ["INT_ADD", "register:40f0:8", ["const:b0ba24:8", "const:4:8"]]
+ 00b0ba24 ["CALL", null, ["callee:008b6fec:8"]]
- 00b0b5fc bytes 6baef697
+ 00b0ba24 bytes 72adf697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c60a9bb717a19627cf9ce02b6bbe7f5"></a>

### [`00b0b8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b8d8.md) → [`00b0bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0bd00.md) FUN_00b0bd00

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00b0b218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b218.md) [`00b0d474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d474.md) [`00b0d5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d5b0.md) · 呼出先 20件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 3件 [`00b0b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md) [`00b0d89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d89c.md) [`00b0d9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d9d8.md) · 呼出先 20件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.41% / 新版 91.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 7件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0bfbc",
      "incomplete_value": false,
      "site": "00b0bfbc",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
    "old": {
      "definition_site": "00b0bb94",
      "incomplete_value": false,
      "site": "00b0bb94",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b00:8"
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
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0bfc0",
      "incomplete_value": false,
      "site": "00b0bfc0",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0bb98",
      "incomplete_value": false,
      "site": "00b0bb98",
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
            "const:b00:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0bfbc",
      "incomplete_value": false,
      "site": "00b0bfc0",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
    "old": {
      "definition_site": "00b0bb94",
      "incomplete_value": false,
      "site": "00b0bb98",
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
                "const:ca4000:8"
              ],
              [
                "leaf",
                "const:b00:8"
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
    "ordinal": 31,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0be70",
      "READ",
      [
        "storage",
        "002b83cf",
        null,
        "string"
      ]
    ],
    [
      "00b0be9c",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b0bee0",
      "PARAM",
      [
        "storage",
        "00ca4b00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0be70",
      "READ",
      [
        "storage",
        "002b840f",
        null,
        "string"
      ]
    ],
    [
      "00b0be9c",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b0bee0",
      "PARAM",
      [
        "storage",
        "00ca4f00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0bac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b8d8.md#insn-00b0bac0) · [`00b0bb70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b8d8.md#insn-00b0bb70) · [`00b0bbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b8d8.md#insn-00b0bbac)
- 新版 `00b0bee8`（命令位置の公開資料なし） · `00b0bf98`（命令位置の公開資料なし） · `00b0bfd4`（命令位置の公開資料なし）

~~~diff
- 00b0bac0 ["INT_ADD", "register:40f0:8", ["const:b0bac0:8", "const:4:8"]]
- 00b0bac0 ["CALL", null, ["callee:0047e60c:8"]]
+ 00b0bee8 ["INT_ADD", "register:40f0:8", ["const:b0bee8:8", "const:4:8"]]
+ 00b0bee8 ["CALL", null, ["callee:0047e60c:8"]]
- 00b0bac0 bytes c3cae597
+ 00b0bee8 bytes c9c9e597
- 00b0bb70 ["INT_ADD", "register:40f0:8", ["const:b0bb70:8", "const:4:8"]]
- 00b0bb70 ["CALL", null, ["callee:00c57e50:8"]]
+ 00b0bf98 ["INT_ADD", "register:40f0:8", ["const:b0bf98:8", "const:4:8"]]
+ 00b0bf98 ["CALL", null, ["callee:00c57e50:8"]]
- 00b0bb70 bytes b82f0594
+ 00b0bf98 bytes ae2f0594
- 00b0bbac ["INT_ADD", "register:40f0:8", ["const:b0bbac:8", "const:4:8"]]
- 00b0bbac ["CALL", null, ["callee:00c57e30:8"]]
+ 00b0bfd4 ["INT_ADD", "register:40f0:8", ["const:b0bfd4:8", "const:4:8"]]
+ 00b0bfd4 ["CALL", null, ["callee:00c57e30:8"]]
- 00b0bbac bytes a12f0594
+ 00b0bfd4 bytes 972f0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d95aab877bd5f67487847fb2356fe6a"></a>

### [`00b0c600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c600.md) → [`00b0ca28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca28.md) FUN_00b0ca28

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b0c3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c3f4.md) [`00b0c628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c628.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`00b0c81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c81c.md) [`00b0ca50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca50.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b0ca34",
      "incomplete_value": false,
      "site": "00b0ca38",
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
      "definition_site": "00b0c60c",
      "incomplete_value": false,
      "site": "00b0c610",
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
      "00b0ca34",
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
      "00b0ca34",
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

- 旧版 [`00b0c610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c600.md#insn-00b0c610) · [`00b0c60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c600.md#insn-00b0c60c)
- 新版 `00b0ca38`（命令位置の公開資料なし） · `00b0ca34`（命令位置の公開資料なし）

~~~diff
- 00b0c610 ["INT_ADD", "register:40f0:8", ["const:b0c610:8", "const:4:8"]]
- 00b0c610 ["CALL", null, ["callee:0043b778:8"]]
+ 00b0ca38 ["INT_ADD", "register:40f0:8", ["const:b0ca38:8", "const:4:8"]]
+ 00b0ca38 ["CALL", null, ["callee:0043b778:8"]]
- 00b0c610 bytes 4abce497
+ 00b0ca38 bytes 50bbe497
- 00b0c60c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b0c60c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b0c60c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b0c60c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b0ca34 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b0ca34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0ca34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0ca34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b0c60c bytes 00303c91
+ 00b0ca34 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d794d4c3a7cb6c9d80f1b0761477f2f1"></a>

### [`00b0c614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c614.md) → [`00b0ca3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca3c.md) FUN_00b0ca3c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b092e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b092e0.md) [`00b0aa78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0aa78.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 2件 [`00b09708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md) [`00b0aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0aea0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00b0ca48",
      "incomplete_value": false,
      "site": "00b0ca4c",
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
      "definition_site": "00b0c620",
      "incomplete_value": false,
      "site": "00b0c624",
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
      "00b0ca48",
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
      "00b0ca48",
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

- 旧版 [`00b0c624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c614.md#insn-00b0c624) · [`00b0c620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c614.md#insn-00b0c620)
- 新版 `00b0ca4c`（命令位置の公開資料なし） · `00b0ca48`（命令位置の公開資料なし）

~~~diff
- 00b0c624 ["INT_ADD", "register:40f0:8", ["const:b0c624:8", "const:4:8"]]
- 00b0c624 ["CALL", null, ["callee:0043b778:8"]]
+ 00b0ca4c ["INT_ADD", "register:40f0:8", ["const:b0ca4c:8", "const:4:8"]]
+ 00b0ca4c ["CALL", null, ["callee:0043b778:8"]]
- 00b0c624 bytes 45bce497
+ 00b0ca4c bytes 4bbbe497
- 00b0c620 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00b0c620 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b0c620 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b0c620 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b0ca48 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b0ca48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0ca48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0ca48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b0c620 bytes 00303c91
+ 00b0ca48 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adfd5b8cb076f081e44d3a7bc54c11cc"></a>

### [`00b0c7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c7b8.md) → [`00b0cbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cbe0.md) FUN_00b0cbe0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00b0cc04",
      "incomplete_value": false,
      "site": "00b0cc08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0c7dc",
      "incomplete_value": false,
      "site": "00b0c7e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "00b0cc08",
      "DATA",
      [
        "storage",
        "00c8e9f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0cc08",
      "DATA",
      [
        "storage",
        "00c8edf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0c7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c7b8.md#insn-00b0c7cc) · [`00b0c7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c7b8.md#insn-00b0c7dc)
- 新版 `00b0cbf4`（命令位置の公開資料なし） · `00b0cc04`（命令位置の公開資料なし）

~~~diff
- 00b0c7cc ["INT_ADD", "register:40f0:8", ["const:b0c7cc:8", "const:4:8"]]
- 00b0c7cc ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0cbf4 ["INT_ADD", "register:40f0:8", ["const:b0cbf4:8", "const:4:8"]]
+ 00b0cbf4 ["CALL", null, ["callee:00c57e90:8"]]
- 00b0c7cc bytes b12c0594
+ 00b0cbf4 bytes a72c0594
- 00b0c7dc ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00b0c7dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0c7dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0c7dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0cc04 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00b0cc04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0cc04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0cc04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0c7dc bytes 08e12791
+ 00b0cc04 bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-121b1c493e38454cbd1b879add2905bc"></a>

### [`00b0c7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c7f8.md) → [`00b0cc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cc20.md) FUN_00b0cc20

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00b0cc24",
      "incomplete_value": false,
      "site": "00b0cc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0c7fc",
      "incomplete_value": false,
      "site": "00b0c800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
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
      "00b0cc28",
      "DATA",
      [
        "storage",
        "00c8e9f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0cc28",
      "DATA",
      [
        "storage",
        "00c8edf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0c7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c7f8.md#insn-00b0c7fc)
- 新版 `00b0cc24`（命令位置の公開資料なし）

~~~diff
- 00b0c7fc ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00b0c7fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0c7fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0c7fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0cc24 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00b0cc24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0cc24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0cc24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0c7fc bytes 08e12791
+ 00b0cc24 bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e6ecf5e2c23222f3f49a2f6fe9fed0f"></a>

### [`00b0c820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c820.md) → [`00b0cc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cc48.md) FUN_00b0cc48

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.82% / 新版 93.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0cd30",
      "incomplete_value": true,
      "site": "00b0cd40",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:968:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0c908",
      "incomplete_value": true,
      "site": "00b0c918",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:89b:8"
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
      "definition_site": "00b0cd74",
      "incomplete_value": false,
      "site": "00b0cd74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0c94c",
      "incomplete_value": false,
      "site": "00b0c94c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "definition_site": "00b0cdd8",
      "incomplete_value": true,
      "site": "00b0cde8",
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
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:3bd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0c9b0",
      "incomplete_value": true,
      "site": "00b0c9c0",
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
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:37d:8"
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
      "00b0cc9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00b0cd30",
      "READ",
      [
        "storage",
        "002a389b",
        null,
        "string"
      ]
    ],
    [
      "00b0cd74",
      "DATA",
      [
        "storage",
        "00c8ea68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0cc9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00b0cd30",
      "READ",
      [
        "storage",
        "002a3968",
        null,
        "string"
      ]
    ],
    [
      "00b0cd74",
      "DATA",
      [
        "storage",
        "00c8ee68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0c874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c820.md#insn-00b0c874) · [`00b0c880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c820.md#insn-00b0c880) · [`00b0c8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0c820.md#insn-00b0c8b8)
- 新版 `00b0cc9c`（命令位置の公開資料なし） · `00b0cca8`（命令位置の公開資料なし） · `00b0cce0`（命令位置の公開資料なし）

~~~diff
- 00b0c874 ["INT_ADD", "register:40f0:8", ["const:b0c874:8", "const:4:8"]]
- 00b0c874 ["CALL", null, ["ram:47acb4:8"]]
+ 00b0cc9c ["INT_ADD", "register:40f0:8", ["const:b0cc9c:8", "const:4:8"]]
+ 00b0cc9c ["CALL", null, ["ram:47acf4:8"]]
- 00b0c874 bytes 10b9e597
+ 00b0cc9c bytes 16b8e597
- 00b0c880 ["INT_ADD", "register:40f0:8", ["const:b0c880:8", "const:4:8"]]
- 00b0c880 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00b0cca8 ["INT_ADD", "register:40f0:8", ["const:b0cca8:8", "const:4:8"]]
+ 00b0cca8 ["CALL", null, ["callee:0047cdd4:8"]]
- 00b0c880 bytes 45c1e597
+ 00b0cca8 bytes 4bc0e597
- 00b0c8b8 ["INT_ADD", "register:40f0:8", ["const:b0c8b8:8", "const:4:8"]]
- 00b0c8b8 ["CALL", null, ["callee:008514f8:8"]]
+ 00b0cce0 ["INT_ADD", "register:40f0:8", ["const:b0cce0:8", "const:4:8"]]
+ 00b0cce0 ["CALL", null, ["callee:008514f8:8"]]
- 00b0c8b8 bytes 0013f597
+ 00b0cce0 bytes 0612f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb4547f31a1f677bfcbe0fd028724a70"></a>

### [`00b0cc44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cc44.md) → [`00b0d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d06c.md) FUN_00b0d06c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00b0d090",
      "incomplete_value": false,
      "site": "00b0d094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0cc68",
      "incomplete_value": false,
      "site": "00b0cc6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "00b0d094",
      "DATA",
      [
        "storage",
        "00c8ea68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d094",
      "DATA",
      [
        "storage",
        "00c8ee68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0cc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cc44.md#insn-00b0cc58) · [`00b0cc68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cc44.md#insn-00b0cc68)
- 新版 `00b0d080`（命令位置の公開資料なし） · `00b0d090`（命令位置の公開資料なし）

~~~diff
- 00b0cc58 ["INT_ADD", "register:40f0:8", ["const:b0cc58:8", "const:4:8"]]
- 00b0cc58 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0d080 ["INT_ADD", "register:40f0:8", ["const:b0d080:8", "const:4:8"]]
+ 00b0d080 ["CALL", null, ["callee:00c57e90:8"]]
- 00b0cc58 bytes 8e2b0594
+ 00b0d080 bytes 842b0594
- 00b0cc68 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 00b0cc68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cc68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cc68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d090 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00b0d090 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d090 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d090 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0cc68 bytes 08a12991
+ 00b0d090 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d4959b604d2c49e84fafef497bccc8d"></a>

### [`00b0cc84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cc84.md) → [`00b0d0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d0ac.md) FUN_00b0d0ac

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00b0d0b0",
      "incomplete_value": false,
      "site": "00b0d0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0cc88",
      "incomplete_value": false,
      "site": "00b0cc8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:a68:8"
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
      "00b0d0b4",
      "DATA",
      [
        "storage",
        "00c8ea68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d0b4",
      "DATA",
      [
        "storage",
        "00c8ee68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0cc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cc84.md#insn-00b0cc88)
- 新版 `00b0d0b0`（命令位置の公開資料なし）

~~~diff
- 00b0cc88 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 00b0cc88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cc88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cc88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d0b0 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 00b0d0b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d0b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d0b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0cc88 bytes 08a12991
+ 00b0d0b0 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-431a6519d01286010a842c7b3ee1b2c1"></a>

### [`00b0ccac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0ccac.md) → [`00b0d0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d0d4.md) FUN_00b0d0d4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00b0b218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b218.md) [`00b0be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0be2c.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00b0b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md) [`00b0c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

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
      "site": "00b0d104",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0ccdc",
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
      "00b0d104",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00b0d104",
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

- 旧版 [`00b0ccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0ccac.md#insn-00b0ccdc) · [`00b0cce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0ccac.md#insn-00b0cce8)
- 新版 `00b0d104`（命令位置の公開資料なし） · `00b0d110`（命令位置の公開資料なし）

~~~diff
- 00b0ccdc ["INT_ADD", "register:40f0:8", ["const:b0ccdc:8", "const:4:8"]]
- 00b0ccdc ["CALL", null, ["ram:47acb4:8"]]
+ 00b0d104 ["INT_ADD", "register:40f0:8", ["const:b0d104:8", "const:4:8"]]
+ 00b0d104 ["CALL", null, ["ram:47acf4:8"]]
- 00b0ccdc bytes f6b7e597
+ 00b0d104 bytes fcb6e597
- 00b0cce8 ["INT_ADD", "register:40f0:8", ["const:b0cce8:8", "const:4:8"]]
- 00b0cce8 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00b0d110 ["INT_ADD", "register:40f0:8", ["const:b0d110:8", "const:4:8"]]
+ 00b0d110 ["CALL", null, ["callee:0047cdd4:8"]]
- 00b0cce8 bytes 2bc0e597
+ 00b0d110 bytes 31bfe597
~~~


<a id="compare-884b4fd9821b9211e7a1c6eaf95fb5e1"></a>

### [`00b0cd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cd60.md) → [`00b0d188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d188.md) FUN_00b0d188

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00b0d1ac",
      "incomplete_value": false,
      "site": "00b0d1b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0cd84",
      "incomplete_value": false,
      "site": "00b0cd88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "00b0d1b0",
      "DATA",
      [
        "storage",
        "00c8eae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d1b0",
      "DATA",
      [
        "storage",
        "00c8eee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0cd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cd60.md#insn-00b0cd74) · [`00b0cd84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cd60.md#insn-00b0cd84)
- 新版 `00b0d19c`（命令位置の公開資料なし） · `00b0d1ac`（命令位置の公開資料なし）

~~~diff
- 00b0cd74 ["INT_ADD", "register:40f0:8", ["const:b0cd74:8", "const:4:8"]]
- 00b0cd74 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0d19c ["INT_ADD", "register:40f0:8", ["const:b0d19c:8", "const:4:8"]]
+ 00b0d19c ["CALL", null, ["callee:00c57e90:8"]]
- 00b0cd74 bytes 472b0594
+ 00b0d19c bytes 3d2b0594
- 00b0cd84 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 00b0cd84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cd84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cd84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d1ac ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 00b0d1ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d1ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d1ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0cd84 bytes 08a12b91
+ 00b0d1ac bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fd654161a3bfbf23907e5bfdbb0b316"></a>

### [`00b0cda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cda0.md) → [`00b0d1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d1c8.md) FUN_00b0d1c8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00b0d1cc",
      "incomplete_value": false,
      "site": "00b0d1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0cda4",
      "incomplete_value": false,
      "site": "00b0cda8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "00b0d1d0",
      "DATA",
      [
        "storage",
        "00c8eae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d1d0",
      "DATA",
      [
        "storage",
        "00c8eee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0cda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cda0.md#insn-00b0cda4)
- 新版 `00b0d1cc`（命令位置の公開資料なし）

~~~diff
- 00b0cda4 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 00b0cda4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cda4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cda4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d1cc ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 00b0d1cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d1cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d1cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0cda4 bytes 08a12b91
+ 00b0d1cc bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6da8a09c7a005df537a3666fa2f8b08"></a>

### [`00b0cdc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cdc8.md) → [`00b0d1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d1f0.md) FUN_00b0d1f0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md) [`00b0b218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b218.md) [`00b0be2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0be2c.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00b0b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md) [`00b0c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

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
      "site": "00b0d220",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0cdf8",
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
      "00b0d220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00b0d220",
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

- 旧版 [`00b0cdf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cdc8.md#insn-00b0cdf8) · [`00b0ce04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cdc8.md#insn-00b0ce04)
- 新版 `00b0d220`（命令位置の公開資料なし） · `00b0d22c`（命令位置の公開資料なし）

~~~diff
- 00b0cdf8 ["INT_ADD", "register:40f0:8", ["const:b0cdf8:8", "const:4:8"]]
- 00b0cdf8 ["CALL", null, ["ram:47acb4:8"]]
+ 00b0d220 ["INT_ADD", "register:40f0:8", ["const:b0d220:8", "const:4:8"]]
+ 00b0d220 ["CALL", null, ["ram:47acf4:8"]]
- 00b0cdf8 bytes afb7e597
+ 00b0d220 bytes b5b6e597
- 00b0ce04 ["INT_ADD", "register:40f0:8", ["const:b0ce04:8", "const:4:8"]]
- 00b0ce04 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00b0d22c ["INT_ADD", "register:40f0:8", ["const:b0d22c:8", "const:4:8"]]
+ 00b0d22c ["CALL", null, ["callee:0047cdd4:8"]]
- 00b0ce04 bytes e4bfe597
+ 00b0d22c bytes eabee597
~~~


<a id="compare-857328a9f3feb412444708d0cafcf1de"></a>

### [`00b0ce7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0ce7c.md) → [`00b0d2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2a4.md) FUN_00b0d2a4

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0d2c8",
      "incomplete_value": false,
      "site": "00b0d2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0cea0",
      "incomplete_value": false,
      "site": "00b0cea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "00b0d2c8",
      "DATA",
      [
        "storage",
        "00c8eb78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d2c8",
      "DATA",
      [
        "storage",
        "00c8ef78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0ce90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0ce7c.md#insn-00b0ce90) · [`00b0ce9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0ce7c.md#insn-00b0ce9c)
- 新版 `00b0d2b8`（命令位置の公開資料なし） · `00b0d2c4`（命令位置の公開資料なし）

~~~diff
- 00b0ce90 ["INT_ADD", "register:40f0:8", ["const:b0ce90:8", "const:4:8"]]
- 00b0ce90 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0d2b8 ["INT_ADD", "register:40f0:8", ["const:b0d2b8:8", "const:4:8"]]
+ 00b0d2b8 ["CALL", null, ["callee:00c57e90:8"]]
- 00b0ce90 bytes 002b0594
+ 00b0d2b8 bytes f62a0594
- 00b0ce9c ["COPY", "tmp:0:8", ["const:b78:8"]]
- 00b0ce9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0ce9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0ce9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d2c4 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 00b0d2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0ce9c bytes 08e12d91
+ 00b0d2c4 bytes 08e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f8381a4a2c4e9b03e7246ae61382267"></a>

### [`00b0ceb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0ceb0.md) → [`00b0d2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2d8.md) FUN_00b0d2d8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0d2e4",
      "incomplete_value": false,
      "site": "00b0d2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0cebc",
      "incomplete_value": false,
      "site": "00b0cebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "00b0d2e4",
      "DATA",
      [
        "storage",
        "00c8eb78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d2e4",
      "DATA",
      [
        "storage",
        "00c8ef78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0ceb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0ceb0.md#insn-00b0ceb8)
- 新版 `00b0d2e0`（命令位置の公開資料なし）

~~~diff
- 00b0ceb8 ["COPY", "tmp:0:8", ["const:b78:8"]]
- 00b0ceb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b0ceb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b0ceb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b0d2e0 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 00b0d2e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0d2e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0d2e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b0ceb8 bytes 29e12d91
+ 00b0d2e0 bytes 29e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bce113252412bc622a57be5e8fd675ea"></a>

### [`00b0cf40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cf40.md) → [`00b0d368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d368.md) FUN_00b0d368

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00b0d38c",
      "incomplete_value": false,
      "site": "00b0d390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0cf64",
      "incomplete_value": false,
      "site": "00b0cf68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "00b0d390",
      "DATA",
      [
        "storage",
        "00c8ebf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d390",
      "DATA",
      [
        "storage",
        "00c8eff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0cf54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cf40.md#insn-00b0cf54) · [`00b0cf64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cf40.md#insn-00b0cf64)
- 新版 `00b0d37c`（命令位置の公開資料なし） · `00b0d38c`（命令位置の公開資料なし）

~~~diff
- 00b0cf54 ["INT_ADD", "register:40f0:8", ["const:b0cf54:8", "const:4:8"]]
- 00b0cf54 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0d37c ["INT_ADD", "register:40f0:8", ["const:b0d37c:8", "const:4:8"]]
+ 00b0d37c ["CALL", null, ["callee:00c57e90:8"]]
- 00b0cf54 bytes cf2a0594
+ 00b0d37c bytes c52a0594
- 00b0cf64 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00b0cf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d38c ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 00b0d38c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d38c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d38c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0cf64 bytes 08e12f91
+ 00b0d38c bytes 08e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86c0ed8f4a54cda0f079a5eb92782d49"></a>

### [`00b0cf80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cf80.md) → [`00b0d3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d3a8.md) FUN_00b0d3a8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00b0d3ac",
      "incomplete_value": false,
      "site": "00b0d3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0cf84",
      "incomplete_value": false,
      "site": "00b0cf88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
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
      "00b0d3b0",
      "DATA",
      [
        "storage",
        "00c8ebf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d3b0",
      "DATA",
      [
        "storage",
        "00c8eff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0cf84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0c/00b0cf80.md#insn-00b0cf84)
- 新版 `00b0d3ac`（命令位置の公開資料なし）

~~~diff
- 00b0cf84 ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00b0cf84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cf84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cf84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d3ac ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 00b0d3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0cf84 bytes 08e12f91
+ 00b0d3ac bytes 08e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e2e6e5202b8cab5abc859e81e70707f"></a>

### [`00b0d41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d41c.md) → [`00b0d844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d844.md) FUN_00b0d844

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0d864",
      "incomplete_value": false,
      "site": "00b0d868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0d43c",
      "incomplete_value": false,
      "site": "00b0d440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "00b0d868",
      "DATA",
      [
        "storage",
        "00c8ec78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d868",
      "DATA",
      [
        "storage",
        "00c8f078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d41c.md#insn-00b0d430) · [`00b0d438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d41c.md#insn-00b0d438) · [`00b0d43c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d41c.md#insn-00b0d43c)
- 新版 `00b0d858`（命令位置の公開資料なし） · `00b0d860`（命令位置の公開資料なし） · `00b0d864`（命令位置の公開資料なし）

~~~diff
- 00b0d430 ["INT_ADD", "register:40f0:8", ["const:b0d430:8", "const:4:8"]]
- 00b0d430 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0d858 ["INT_ADD", "register:40f0:8", ["const:b0d858:8", "const:4:8"]]
+ 00b0d858 ["CALL", null, ["callee:00c57e90:8"]]
- 00b0d430 bytes 98290594
+ 00b0d858 bytes 8e290594
- 00b0d438 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b0d860 ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b0d438 bytes 080c00b0
+ 00b0d860 bytes 080c00d0
- 00b0d43c ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00b0d43c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d43c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d43c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d864 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00b0d864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d43c bytes 08e13191
+ 00b0d864 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e88de4112d6004d86e6ce7f6ffbe93f1"></a>

### [`00b0d454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d454.md) → [`00b0d87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d87c.md) FUN_00b0d87c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0d880",
      "incomplete_value": false,
      "site": "00b0d884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0d458",
      "incomplete_value": false,
      "site": "00b0d45c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "00b0d884",
      "DATA",
      [
        "storage",
        "00c8ec78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d884",
      "DATA",
      [
        "storage",
        "00c8f078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d454.md#insn-00b0d454) · [`00b0d458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d454.md#insn-00b0d458)
- 新版 `00b0d87c`（命令位置の公開資料なし） · `00b0d880`（命令位置の公開資料なし）

~~~diff
- 00b0d454 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b0d87c ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b0d454 bytes 080c00b0
+ 00b0d87c bytes 080c00d0
- 00b0d458 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00b0d458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d880 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00b0d880 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d880 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d880 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d458 bytes 08e13191
+ 00b0d880 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47a95e71e1ba1d16d548280287fb8108"></a>

### [`00b0d474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d474.md) → [`00b0d89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d89c.md) FUN_00b0d89c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00b0af5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0af5c.md) [`00b0b8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b8d8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00b0b384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b384.md) [`00b0bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0bd00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

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
      "site": "00b0d8c4",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0d49c",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "00b0d8d0",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0d4a8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00b0d8c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00b0d8d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00b0d8c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00b0d8d0",
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

- 旧版 [`00b0d49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d474.md#insn-00b0d49c) · [`00b0d4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d474.md#insn-00b0d4a8) · [`00b0d4dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d474.md#insn-00b0d4dc)
- 新版 `00b0d8c4`（命令位置の公開資料なし） · `00b0d8d0`（命令位置の公開資料なし） · `00b0d904`（命令位置の公開資料なし）

~~~diff
- 00b0d49c ["INT_ADD", "register:40f0:8", ["const:b0d49c:8", "const:4:8"]]
- 00b0d49c ["CALL", null, ["ram:47acb4:8"]]
+ 00b0d8c4 ["INT_ADD", "register:40f0:8", ["const:b0d8c4:8", "const:4:8"]]
+ 00b0d8c4 ["CALL", null, ["ram:47acf4:8"]]
- 00b0d49c bytes 06b6e597
+ 00b0d8c4 bytes 0cb5e597
- 00b0d4a8 ["INT_ADD", "register:40f0:8", ["const:b0d4a8:8", "const:4:8"]]
- 00b0d4a8 ["CALL", null, ["ram:47acb4:8"]]
+ 00b0d8d0 ["INT_ADD", "register:40f0:8", ["const:b0d8d0:8", "const:4:8"]]
+ 00b0d8d0 ["CALL", null, ["ram:47acf4:8"]]
- 00b0d4a8 bytes 03b6e597
+ 00b0d8d0 bytes 09b5e597
- 00b0d4dc ["INT_ADD", "register:40f0:8", ["const:b0d4dc:8", "const:4:8"]]
- 00b0d4dc ["CALL", null, ["callee:00b0b384:8"]]
+ 00b0d904 ["INT_ADD", "register:40f0:8", ["const:b0d904:8", "const:4:8"]]
+ 00b0d904 ["CALL", null, ["callee:00b0b384:8"]]
- 00b0d4dc bytes a0f6ff97
+ 00b0d904 bytes a0f6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6eb9b5e53a6124ca649c3834fc908ade"></a>

### [`00b0d558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d558.md) → [`00b0d980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d980.md) FUN_00b0d980

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0d9a0",
      "incomplete_value": false,
      "site": "00b0d9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0d578",
      "incomplete_value": false,
      "site": "00b0d57c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "00b0d9a4",
      "DATA",
      [
        "storage",
        "00c8ecf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d9a4",
      "DATA",
      [
        "storage",
        "00c8f0f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d558.md#insn-00b0d56c) · [`00b0d574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d558.md#insn-00b0d574) · [`00b0d578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d558.md#insn-00b0d578)
- 新版 `00b0d994`（命令位置の公開資料なし） · `00b0d99c`（命令位置の公開資料なし） · `00b0d9a0`（命令位置の公開資料なし）

~~~diff
- 00b0d56c ["INT_ADD", "register:40f0:8", ["const:b0d56c:8", "const:4:8"]]
- 00b0d56c ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0d994 ["INT_ADD", "register:40f0:8", ["const:b0d994:8", "const:4:8"]]
+ 00b0d994 ["CALL", null, ["callee:00c57e90:8"]]
- 00b0d56c bytes 49290594
+ 00b0d994 bytes 3f290594
- 00b0d574 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b0d99c ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b0d574 bytes 080c00b0
+ 00b0d99c bytes 080c00d0
- 00b0d578 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00b0d578 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d578 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d578 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d9a0 ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 00b0d9a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d9a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d9a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d578 bytes 08e13391
+ 00b0d9a0 bytes 08e10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02df402055cf341cf9ac72d41d0bc4ce"></a>

### [`00b0d590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d590.md) → [`00b0d9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d9b8.md) FUN_00b0d9b8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0d9bc",
      "incomplete_value": false,
      "site": "00b0d9c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8f000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0d594",
      "incomplete_value": false,
      "site": "00b0d598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8e000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "00b0d9c0",
      "DATA",
      [
        "storage",
        "00c8ecf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d9c0",
      "DATA",
      [
        "storage",
        "00c8f0f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d590.md#insn-00b0d590) · [`00b0d594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d590.md#insn-00b0d594)
- 新版 `00b0d9b8`（命令位置の公開資料なし） · `00b0d9bc`（命令位置の公開資料なし）

~~~diff
- 00b0d590 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b0d9b8 ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b0d590 bytes 080c00b0
+ 00b0d9b8 bytes 080c00d0
- 00b0d594 ["COPY", "tmp:0:8", ["const:cf8:8"]]
- 00b0d594 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d594 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d594 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d9bc ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 00b0d9bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d9bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d9bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d594 bytes 08e13391
+ 00b0d9bc bytes 08e10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c407a244262c07e28809b6d627dd187e"></a>

### [`00b0d5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d5b0.md) → [`00b0d9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d9d8.md) FUN_00b0d9d8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00b0af5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0af5c.md) [`00b0b8d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0b/00b0b8d8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00b0b384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b384.md) [`00b0bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0bd00.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

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
      "site": "00b0da00",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0d5d8",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "00b0da0c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0d5e4",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00b0da00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00b0da0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00b0da00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00b0da0c",
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

- 旧版 [`00b0d5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d5b0.md#insn-00b0d5d8) · [`00b0d5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d5b0.md#insn-00b0d5e4) · [`00b0d61c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d5b0.md#insn-00b0d61c)
- 新版 `00b0da00`（命令位置の公開資料なし） · `00b0da0c`（命令位置の公開資料なし） · `00b0da44`（命令位置の公開資料なし）

~~~diff
- 00b0d5d8 ["INT_ADD", "register:40f0:8", ["const:b0d5d8:8", "const:4:8"]]
- 00b0d5d8 ["CALL", null, ["ram:47acb4:8"]]
+ 00b0da00 ["INT_ADD", "register:40f0:8", ["const:b0da00:8", "const:4:8"]]
+ 00b0da00 ["CALL", null, ["ram:47acf4:8"]]
- 00b0d5d8 bytes b7b5e597
+ 00b0da00 bytes bdb4e597
- 00b0d5e4 ["INT_ADD", "register:40f0:8", ["const:b0d5e4:8", "const:4:8"]]
- 00b0d5e4 ["CALL", null, ["ram:47acb4:8"]]
+ 00b0da0c ["INT_ADD", "register:40f0:8", ["const:b0da0c:8", "const:4:8"]]
+ 00b0da0c ["CALL", null, ["ram:47acf4:8"]]
- 00b0d5e4 bytes b4b5e597
+ 00b0da0c bytes bab4e597
- 00b0d61c ["INT_ADD", "register:40f0:8", ["const:b0d61c:8", "const:4:8"]]
- 00b0d61c ["CALL", null, ["callee:00b0b384:8"]]
+ 00b0da44 ["INT_ADD", "register:40f0:8", ["const:b0da44:8", "const:4:8"]]
+ 00b0da44 ["CALL", null, ["callee:00b0b384:8"]]
- 00b0d61c bytes 50f6ff97
+ 00b0da44 bytes 50f6ff97
~~~


<a id="compare-7f477fd771a384a3b149e031de492a27"></a>

### [`00b0d74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d74c.md) → [`00b0db74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0db74.md) _INIT_254

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00b0dbb0",
      "incomplete_value": true,
      "site": "00b0dbcc",
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
      "definition_site": "00b0d788",
      "incomplete_value": true,
      "site": "00b0d7a4",
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
      "definition_site": "00b0dbd4",
      "incomplete_value": true,
      "site": "00b0dbf0",
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
      "definition_site": "00b0d7ac",
      "incomplete_value": true,
      "site": "00b0d7c8",
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
      "definition_site": "00b0dbf4",
      "incomplete_value": true,
      "site": "00b0dc10",
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
      "definition_site": "00b0d7cc",
      "incomplete_value": true,
      "site": "00b0d7e8",
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
      "00b0dbb0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00b0dbd4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00b0dbf4",
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
      "00b0dbb0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b0dbd4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b0dbf4",
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

- 旧版 [`00b0d8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d74c.md#insn-00b0d8ac) · [`00b0d980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d74c.md#insn-00b0d980) · [`00b0d778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0d74c.md#insn-00b0d778)
- 新版 `00b0dcd4`（命令位置の公開資料なし） · `00b0dda8`（命令位置の公開資料なし） · `00b0dba0`（命令位置の公開資料なし）

~~~diff
- 00b0d8ac ["INT_ADD", "register:40f0:8", ["const:b0d8ac:8", "const:4:8"]]
- 00b0d8ac ["CALL", null, ["callee:0043b7f8:8"]]
+ 00b0dcd4 ["INT_ADD", "register:40f0:8", ["const:b0dcd4:8", "const:4:8"]]
+ 00b0dcd4 ["CALL", null, ["callee:0043b7f8:8"]]
- 00b0d8ac bytes c3b7e497
+ 00b0dcd4 bytes c9b6e497
- 00b0d980 ["INT_ADD", "register:40f0:8", ["const:b0d980:8", "const:4:8"]]
- 00b0d980 ["CALL", null, ["callee:00c57e30:8"]]
+ 00b0dda8 ["INT_ADD", "register:40f0:8", ["const:b0dda8:8", "const:4:8"]]
+ 00b0dda8 ["CALL", null, ["callee:00c57e30:8"]]
- 00b0d980 bytes 2c280594
+ 00b0dda8 bytes 22280594
- 00b0d778 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00b0d778 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b0d778 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b0d778 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b0dba0 ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00b0dba0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b0dba0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b0dba0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b0d778 bytes 73622691
+ 00b0dba0 bytes 73623691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-174c3083da307ccce6cee610ec5fe8c3"></a>

### [`00b0dadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0dadc.md) → [`00b0df04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0df04.md) FUN_00b0df04

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) [`007a0744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a0744.md) [`00b0dadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0dadc.md) · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492dc8.md) [`005da544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005da544.md) [`00684f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684f70.md)
- 新版 呼出元 3件 [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) [`007a0784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0784.md) [`00b0df04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0df04.md) · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`005da584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005da/005da584.md) [`00684fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684fb0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.16% / 新版 89.16%

CFGの説明率　旧版 80.22% / 新版 77.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 8件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0e098",
      "incomplete_value": true,
      "site": "00b0e0ac",
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
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:d92:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dc70",
      "incomplete_value": true,
      "site": "00b0dc84",
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
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:d52:8"
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
      "definition_site": "00b0e174",
      "incomplete_value": true,
      "site": "00b0e184",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:6e1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dd4c",
      "incomplete_value": true,
      "site": "00b0dd5c",
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
                "const:2a3000:8"
              ],
              [
                "leaf",
                "const:614:8"
              ]
            ]
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
      "definition_site": "00b0e178",
      "incomplete_value": true,
      "site": "00b0e188",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dd50",
      "incomplete_value": true,
      "site": "00b0dd60",
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
                "const:f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0e064",
      "PARAM",
      [
        "storage",
        "002beb0e",
        null,
        null
      ]
    ],
    [
      "00b0e098",
      "READ",
      [
        "storage",
        "002bdd52",
        null,
        "string"
      ]
    ],
    [
      "00b0e0c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071ecc0"
      ]
    ]
  ],
  "added": [
    [
      "00b0e064",
      "PARAM",
      [
        "storage",
        "002beb4e",
        null,
        null
      ]
    ],
    [
      "00b0e098",
      "READ",
      [
        "storage",
        "002bdd92",
        null,
        "string"
      ]
    ],
    [
      "00b0e0c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071ed00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0dca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0dadc.md#insn-00b0dca0) · [`00b0dd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0dadc.md#insn-00b0dd10) · [`00b0de68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0d/00b0dadc.md#insn-00b0de68)
- 新版 `00b0e0c8`（命令位置の公開資料なし） · `00b0e138`（命令位置の公開資料なし）

~~~diff
- 00b0dca0 ["INT_ADD", "register:40f0:8", ["const:b0dca0:8", "const:4:8"]]
- 00b0dca0 ["CALL", null, ["ram:71ecc0:8"]]
+ 00b0e0c8 ["INT_ADD", "register:40f0:8", ["const:b0e0c8:8", "const:4:8"]]
+ 00b0e0c8 ["CALL", null, ["ram:71ed00:8"]]
- 00b0dca0 bytes 0844f097
+ 00b0e0c8 bytes 0e43f097
- 00b0dd10 ["INT_ADD", "register:40f0:8", ["const:b0dd10:8", "const:4:8"]]
- 00b0dd10 ["CALL", null, ["ram:71ecc0:8"]]
+ 00b0e138 ["INT_ADD", "register:40f0:8", ["const:b0e138:8", "const:4:8"]]
+ 00b0e138 ["CALL", null, ["ram:71ed00:8"]]
- 00b0dd10 bytes ec43f097
+ 00b0e138 bytes f242f097
- 00b0de68 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b0de68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0de68 bytes e81300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f4f7af01dbd1510d49229152cf1f10f"></a>

### [`00b0e17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e17c.md) → [`00b0e5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e5a4.md) _INIT_255

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 52.54% / 新版 52.54%

CFGの説明率　旧版 87.50% / 新版 93.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0e1ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0e1c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0e1c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0e1ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b0e1b8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b0e1c0",
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
      "00b0e5d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00b0e5e0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b0e5e8",
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

- 旧版 [`00b0e1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e17c.md#insn-00b0e1ac) · [`00b0e1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e17c.md#insn-00b0e1c0) · [`00b0e1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e17c.md#insn-00b0e1c4)

~~~diff
- 00b0e1ac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b0e1ac ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b0e1ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b0e1ac bytes a9831ff8
- 00b0e1c0 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00b0e1c0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00b0e1c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00b0e1c0 bytes ea130278
- 00b0e1c4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b0e1c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b0e1c4 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dc03cce6e8e20d54750e6311c0f513f"></a>

### [`00b0e50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e50c.md) → [`00b0e934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e934.md) FUN_00b0e934

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) [`007aca8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007aca8c.md) [`007ad0c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ad/007ad0c4.md) [`00b0e654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e654.md) · 呼出先 7件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`00492c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492c8c.md) [`009a754c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a7/009a754c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 4件 [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) [`007acacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md) [`007ad104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad104.md) [`00b0ea7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0ea7c.md) · 呼出先 7件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`00492ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492ccc.md) [`009a76e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a7/009a76e8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.13% / 新版 84.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0e978",
      "incomplete_value": true,
      "site": "00b0e984",
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
                "const:e00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0e550",
      "incomplete_value": true,
      "site": "00b0e55c",
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
                "const:dc0:8"
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
      "definition_site": "00b0e974",
      "incomplete_value": true,
      "site": "00b0e988",
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
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:3ce:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0e54c",
      "incomplete_value": true,
      "site": "00b0e560",
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
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:38e:8"
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
      "definition_site": "00b0e974",
      "incomplete_value": true,
      "site": "00b0e988",
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
      "definition_site": "00b0e54c",
      "incomplete_value": true,
      "site": "00b0e560",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0e974",
      "READ",
      [
        "storage",
        "002b038e",
        null,
        "string"
      ]
    ],
    [
      "00b0e974",
      "READ",
      [
        "storage",
        "002b039e",
        null,
        "string"
      ]
    ],
    [
      "00b0e978",
      "READ",
      [
        "storage",
        "002c2dc0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b0e974",
      "READ",
      [
        "storage",
        "002b03ce",
        null,
        "string"
      ]
    ],
    [
      "00b0e974",
      "READ",
      [
        "storage",
        "002b03de",
        null,
        "string"
      ]
    ],
    [
      "00b0e978",
      "READ",
      [
        "storage",
        "002c2e00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e50c.md#insn-00b0e57c) · [`00b0e5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e50c.md#insn-00b0e5b4) · [`00b0e53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e50c.md#insn-00b0e53c)
- 新版 `00b0e9a4`（命令位置の公開資料なし） · `00b0e9dc`（命令位置の公開資料なし） · `00b0e964`（命令位置の公開資料なし）

~~~diff
- 00b0e57c ["INT_ADD", "register:40f0:8", ["const:b0e57c:8", "const:4:8"]]
- 00b0e57c ["CALL", null, ["callee:00c58190:8"]]
+ 00b0e9a4 ["INT_ADD", "register:40f0:8", ["const:b0e9a4:8", "const:4:8"]]
+ 00b0e9a4 ["CALL", null, ["callee:00c58190:8"]]
- 00b0e57c bytes 05260594
+ 00b0e9a4 bytes fb250594
- 00b0e5b4 ["INT_ADD", "register:40f0:8", ["const:b0e5b4:8", "const:4:8"]]
- 00b0e5b4 ["CALL", null, ["ram:48ccb8:8"]]
+ 00b0e9dc ["INT_ADD", "register:40f0:8", ["const:b0e9dc:8", "const:4:8"]]
+ 00b0e9dc ["CALL", null, ["ram:48ccf8:8"]]
- 00b0e5b4 bytes c1f9e597
+ 00b0e9dc bytes c7f8e597
- 00b0e53c ["INT_ADD", "register:40f0:8", ["const:b0e53c:8", "const:4:8"]]
- 00b0e53c ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0e964 ["INT_ADD", "register:40f0:8", ["const:b0e964:8", "const:4:8"]]
+ 00b0e964 ["CALL", null, ["callee:00c57e90:8"]]
- 00b0e53c bytes 55250594
+ 00b0e964 bytes 4b250594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dde9a6985dbd5b1d4e37f7e61095d55"></a>

### [`00b0e654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e654.md) → [`00b0ea7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0ea7c.md) FUN_00b0ea7c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007981d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/007981d4.md) · 呼出先 15件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00451998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451998.md) [`004593b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/004593b0.md) [`0059715c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059715c.md) [`005974c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md)
- 新版 呼出元 1件 [`00798214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798214.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`004593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md) [`0059719c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md) [`00597504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597504.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0eac0",
      "incomplete_value": false,
      "site": "00b0eacc",
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
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0e698",
      "incomplete_value": false,
      "site": "00b0e6a4",
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
            "const:278:8"
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
      "definition_site": "00b0eb7c",
      "incomplete_value": true,
      "site": "00b0eb80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b0e754",
      "incomplete_value": true,
      "site": "00b0e758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0eb78",
      "incomplete_value": true,
      "site": "00b0eb84",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b0e750",
      "incomplete_value": true,
      "site": "00b0e75c",
      "value": [
        "LOAD",
        "8",
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
      "00b0eacc",
      "DATA",
      [
        "storage",
        "00c6d278",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eb08",
      "DATA",
      [
        "storage",
        "00c63360",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eb54",
      "READ",
      [
        "storage",
        "00c63368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0eacc",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eb08",
      "DATA",
      [
        "storage",
        "00c63760",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eb54",
      "READ",
      [
        "storage",
        "00c63768",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e654.md#insn-00b0e684) · [`00b0e698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e654.md#insn-00b0e698) · [`00b0e6bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e654.md#insn-00b0e6bc)
- 新版 `00b0eaac`（命令位置の公開資料なし） · `00b0eac0`（命令位置の公開資料なし） · `00b0eae4`（命令位置の公開資料なし）

~~~diff
- 00b0e684 ["INT_ADD", "register:40f0:8", ["const:b0e684:8", "const:4:8"]]
- 00b0e684 ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0eaac ["INT_ADD", "register:40f0:8", ["const:b0eaac:8", "const:4:8"]]
+ 00b0eaac ["CALL", null, ["callee:00c57e90:8"]]
- 00b0e684 bytes 03250594
+ 00b0eaac bytes f9240594
- 00b0e698 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00b0e698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b0e698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b0e698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b0eac0 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00b0eac0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0eac0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0eac0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b0e698 bytes 29e10991
+ 00b0eac0 bytes 29e11991
- 00b0e6bc ["COPY", "tmp:0:8", ["const:360:8"]]
- 00b0e6bc ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00b0e6bc ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00b0e6bc ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00b0eae4 ["COPY", "tmp:0:8", ["const:760:8"]]
+ 00b0eae4 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00b0eae4 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00b0eae4 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00b0e6bc bytes 39830d91
+ 00b0eae4 bytes 39831d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b323609eb25d96c0f8a00d6a5991d37"></a>

### [`00b0ec54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0ec54.md) → [`00b0f07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f07c.md) _INIT_256

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00b0f0b8",
      "incomplete_value": true,
      "site": "00b0f0d4",
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
      "definition_site": "00b0ec90",
      "incomplete_value": true,
      "site": "00b0ecac",
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
      "definition_site": "00b0f0dc",
      "incomplete_value": true,
      "site": "00b0f0f8",
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
      "definition_site": "00b0ecb4",
      "incomplete_value": true,
      "site": "00b0ecd0",
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
      "definition_site": "00b0f0fc",
      "incomplete_value": true,
      "site": "00b0f118",
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
      "definition_site": "00b0ecd4",
      "incomplete_value": true,
      "site": "00b0ecf0",
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
      "00b0f0b8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00b0f0dc",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00b0f0fc",
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
      "00b0f0b8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b0f0dc",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b0f0fc",
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

- 旧版 [`00b0edb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0ec54.md#insn-00b0edb4) · [`00b0ee88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0ec54.md#insn-00b0ee88) · [`00b0ec80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0ec54.md#insn-00b0ec80)
- 新版 `00b0f1dc`（命令位置の公開資料なし） · `00b0f2b0`（命令位置の公開資料なし） · `00b0f0a8`（命令位置の公開資料なし）

~~~diff
- 00b0edb4 ["INT_ADD", "register:40f0:8", ["const:b0edb4:8", "const:4:8"]]
- 00b0edb4 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00b0f1dc ["INT_ADD", "register:40f0:8", ["const:b0f1dc:8", "const:4:8"]]
+ 00b0f1dc ["CALL", null, ["callee:0043b7f8:8"]]
- 00b0edb4 bytes 81b2e497
+ 00b0f1dc bytes 87b1e497
- 00b0ee88 ["INT_ADD", "register:40f0:8", ["const:b0ee88:8", "const:4:8"]]
- 00b0ee88 ["CALL", null, ["callee:00c57e30:8"]]
+ 00b0f2b0 ["INT_ADD", "register:40f0:8", ["const:b0f2b0:8", "const:4:8"]]
+ 00b0f2b0 ["CALL", null, ["callee:00c57e30:8"]]
- 00b0ee88 bytes ea220594
+ 00b0f2b0 bytes e0220594
- 00b0ec80 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00b0ec80 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b0ec80 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b0ec80 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b0f0a8 ["COPY", "tmp:0:8", ["const:dc8:8"]]
+ 00b0f0a8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b0f0a8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b0f0a8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b0ec80 bytes 73222791
+ 00b0f0a8 bytes 73223791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba98f2782d1f4664854f038f0455f6c0"></a>

### [`00b0f1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f1cc.md) → [`00b0f5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f5f4.md) FUN_00b0f5f4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)
- 新版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 90.73% / 新版 90.73%

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
      "definition_site": "00b0f62c",
      "incomplete_value": false,
      "site": "00b0f634",
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
      "definition_site": "00b0f204",
      "incomplete_value": false,
      "site": "00b0f20c",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0f648",
      "incomplete_value": true,
      "site": "00b0f654",
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
                "const:86c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0f220",
      "incomplete_value": true,
      "site": "00b0f22c",
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
                "const:82c:8"
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
      "definition_site": "00b0f7ac",
      "incomplete_value": true,
      "site": "00b0f7b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00b0f384",
      "incomplete_value": true,
      "site": "00b0f388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b0f634",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0f648",
      "READ",
      [
        "storage",
        "002b982c",
        null,
        "string"
      ]
    ],
    [
      "00b0f79c",
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
      "00b0f634",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0f648",
      "READ",
      [
        "storage",
        "002b986c",
        null,
        "string"
      ]
    ],
    [
      "00b0f79c",
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

- 旧版 [`00b0f1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f1cc.md#insn-00b0f1fc) · [`00b0f204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f1cc.md#insn-00b0f204) · [`00b0f21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f1cc.md#insn-00b0f21c)
- 新版 `00b0f624`（命令位置の公開資料なし） · `00b0f62c`（命令位置の公開資料なし） · `00b0f644`（命令位置の公開資料なし）

~~~diff
- 00b0f1fc ["INT_ADD", "register:40f0:8", ["const:b0f1fc:8", "const:4:8"]]
- 00b0f1fc ["CALL", null, ["callee:00487e20:8"]]
+ 00b0f624 ["INT_ADD", "register:40f0:8", ["const:b0f624:8", "const:4:8"]]
+ 00b0f624 ["CALL", null, ["callee:00487e20:8"]]
- 00b0f1fc bytes f9e2e597
+ 00b0f624 bytes ffe1e597
- 00b0f204 ["COPY", "tmp:0:8", ["const:938:8"]]
- 00b0f204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0f204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0f204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0f62c ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00b0f62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0f62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0f62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0f204 bytes 08e12491
+ 00b0f62c bytes 08e13491
- 00b0f21c ["COPY", "tmp:0:8", ["const:82c:8"]]
- 00b0f21c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0f21c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0f21c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0f644 ["COPY", "tmp:0:8", ["const:86c:8"]]
+ 00b0f644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0f644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0f644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0f21c bytes 08b12091
+ 00b0f644 bytes 08b12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53c3f2ab48f0314f5bb9b55780c63f8b"></a>

### [`00b0f48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f48c.md) → [`00b0f8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f8b4.md) FUN_00b0f8b4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a8509c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a85/00a8509c.md) [`00b0f5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f5f0.md) · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00b1090c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b1090c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 2件 [`00a85294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a85/00a85294.md) [`00b0fa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0fa18.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00b10d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d34.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.88% / 新版 98.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0f954",
      "incomplete_value": false,
      "site": "00b0f958",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0f52c",
      "incomplete_value": false,
      "site": "00b0f530",
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
            "const:f0:8"
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
      "00b0f954",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0f954",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0f530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f48c.md#insn-00b0f530) · [`00b0f52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f48c.md#insn-00b0f52c) · [`00b0f55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0f/00b0f48c.md#insn-00b0f55c)
- 新版 `00b0f958`（命令位置の公開資料なし） · `00b0f954`（命令位置の公開資料なし） · `00b0f984`（命令位置の公開資料なし）

~~~diff
- 00b0f530 ["INT_ADD", "register:40f0:8", ["const:b0f530:8", "const:4:8"]]
- 00b0f530 ["CALL", null, ["callee:00442930:8"]]
+ 00b0f958 ["INT_ADD", "register:40f0:8", ["const:b0f958:8", "const:4:8"]]
+ 00b0f958 ["CALL", null, ["callee:00442930:8"]]
- 00b0f530 bytes f0cce497
+ 00b0f958 bytes f6cbe497
- 00b0f52c ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00b0f52c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b0f52c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b0f52c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b0f954 ["COPY", "tmp:0:8", ["const:1bd:8"]]
+ 00b0f954 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0f954 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0f954 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b0f52c bytes 00c00391
+ 00b0f954 bytes 00f40691
- 00b0f55c ["INT_ADD", "register:40f0:8", ["const:b0f55c:8", "const:4:8"]]
- 00b0f55c ["CALL", null, ["callee:00c57e90:8"]]
+ 00b0f984 ["INT_ADD", "register:40f0:8", ["const:b0f984:8", "const:4:8"]]
+ 00b0f984 ["CALL", null, ["callee:00c57e90:8"]]
- 00b0f55c bytes 4d210594
+ 00b0f984 bytes 43210594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

