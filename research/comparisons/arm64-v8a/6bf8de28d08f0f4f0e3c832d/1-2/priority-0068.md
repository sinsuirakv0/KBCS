# v16.0.1 → v16.0.2 · 最優先の変更候補 (68)

[一覧の目次](README.md)

<a id="compare-b7cfb1c3ee38f54349d082b6a029573c"></a>

### [`00b03650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03650.md) → [`00b036ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b036ec.md) FUN_00b036ec

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 3件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 11.11% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03650"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03650"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b03654"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b03650",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b03654",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b03658",
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
      "00b036ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b036f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b036f4",
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

- 旧版 [`00b03650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03650.md#insn-00b03650) · [`00b03654`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03650.md#insn-00b03654) · [`00b03658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03650.md#insn-00b03658)

~~~diff
- 00b03650 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b03650 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b03650 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b03650 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b03650 bytes fd7bbda9
- 00b03654 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b03654 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b03654 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b03654 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b03654 bytes f65701a9
- 00b03658 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b03658 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b03658 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b03658 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b03658 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66c87fd841f187d2f0370786f902538a"></a>

### [`00b036f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b036f8.md) → [`00b03794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03794.md) FUN_00b03794

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b0272c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b0272c.md)
- 新版 呼出元 4件 [`006855c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/006855c8.md) [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b027c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b027c8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b03714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b036f8.md#insn-00b03714) · [`00b03728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b036f8.md#insn-00b03728) · [`00b03730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b036f8.md#insn-00b03730)
- 新版 [`00b037b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03794.md#insn-00b037b0) · [`00b037c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03794.md#insn-00b037c4) · [`00b037cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03794.md#insn-00b037cc)

~~~diff
- 00b03714 ["INT_ADD", "register:40f0:8", ["const:b03714:8", "const:4:8"]]
- 00b03714 ["CALL", null, ["callee:00851550:8"]]
+ 00b037b0 ["INT_ADD", "register:40f0:8", ["const:b037b0:8", "const:4:8"]]
+ 00b037b0 ["CALL", null, ["callee:00851550:8"]]
- 00b03714 bytes 7937f597
+ 00b037b0 bytes 6837f597
- 00b03728 ["INT_ADD", "register:40f0:8", ["const:b03728:8", "const:4:8"]]
- 00b03728 ["CALL", null, ["callee:005e7460:8"]]
+ 00b037c4 ["INT_ADD", "register:40f0:8", ["const:b037c4:8", "const:4:8"]]
+ 00b037c4 ["CALL", null, ["callee:005e7460:8"]]
- 00b03728 bytes 3e8feb97
+ 00b037c4 bytes 278feb97
- 00b03730 ["INT_ADD", "register:40f0:8", ["const:b03730:8", "const:4:8"]]
- 00b03730 ["CALL", null, ["callee:00851550:8"]]
+ 00b037cc ["INT_ADD", "register:40f0:8", ["const:b037cc:8", "const:4:8"]]
+ 00b037cc ["CALL", null, ["callee:00851550:8"]]
- 00b03730 bytes 7237f597
+ 00b037cc bytes 6137f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9edefec5e41d4f962d78f2a4d8142e91"></a>

### [`00b03e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03e3c.md) → [`00b03ed8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03ed8.md) FUN_00b03ed8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00b009dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b00/00b009dc.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 3件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00b00a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b00/00b00a78.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b03e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03e3c.md#insn-00b03e50) · [`00b03e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03e3c.md#insn-00b03e64) · [`00b03e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03e3c.md#insn-00b03e68)
- 新版 [`00b03eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03ed8.md#insn-00b03eec) · [`00b03f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03ed8.md#insn-00b03f00) · [`00b03f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b03/00b03ed8.md#insn-00b03f04)

~~~diff
- 00b03e50 ["INT_ADD", "register:40f0:8", ["const:b03e50:8", "const:4:8"]]
- 00b03e50 ["CALL", null, ["callee:00851550:8"]]
+ 00b03eec ["INT_ADD", "register:40f0:8", ["const:b03eec:8", "const:4:8"]]
+ 00b03eec ["CALL", null, ["callee:00851550:8"]]
- 00b03e50 bytes aa35f597
+ 00b03eec bytes 9935f597
- 00b03e64 ["INT_ADD", "register:40f0:8", ["const:b03e64:8", "const:4:8"]]
- 00b03e64 ["CALL", null, ["callee:005e7460:8"]]
+ 00b03f00 ["INT_ADD", "register:40f0:8", ["const:b03f00:8", "const:4:8"]]
+ 00b03f00 ["CALL", null, ["callee:005e7460:8"]]
- 00b03e64 bytes 6f8deb97
+ 00b03f00 bytes 588deb97
- 00b03e68 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b03e68 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b03e68 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b03e68 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b03f04 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b03f04 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b03f04 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b03f04 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b03e68 bytes 00010037
+ 00b03f04 bytes 00010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c4bbed5c6c269813c653024fc8ab550"></a>

### [`00b046f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b046f0.md) → [`00b0478c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b0478c.md) FUN_00b0478c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`006c5350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c5350.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b047b0",
      "incomplete_value": true,
      "site": "00b047b4",
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
      "site": "00b04750"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b047ec"
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
      "unmatched:00b04734",
      "DATA",
      [
        "storage",
        "0023d790",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b047d0",
      "DATA",
      [
        "storage",
        "0023d790",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b046f0.md#insn-00b04718) · [`00b04750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b046f0.md#insn-00b04750)
- 新版 [`00b047b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b0478c.md#insn-00b047b4) · [`00b047ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b0478c.md#insn-00b047ec)

~~~diff
- 00b04718 ["INT_ADD", "register:40f0:8", ["const:b04718:8", "const:4:8"]]
- 00b04718 ["CALL", null, ["callee:005e7460:8"]]
+ 00b047b4 ["INT_ADD", "register:40f0:8", ["const:b047b4:8", "const:4:8"]]
+ 00b047b4 ["CALL", null, ["callee:005e7460:8"]]
- 00b04718 bytes 428beb97
+ 00b047b4 bytes 2b8beb97
- 00b04750 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b04750 ["RETURN", null, ["register:0:8"]]
- 00b04750 bytes c0035fd6
+ 00b047ec ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b047ec ["RETURN", null, ["register:0:8"]]
+ 00b047ec bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6970749876201207daa0a5b18a312f50"></a>

### [`00b04754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04754.md) → [`00b047f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b047f0.md) FUN_00b047f0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`006c5350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c5350.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

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
      "definition_site": "00b04814",
      "incomplete_value": true,
      "site": "00b04818",
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

- 旧版 [`00b0477c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04754.md#insn-00b0477c) · [`00b04768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04754.md#insn-00b04768) · [`00b04780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04754.md#insn-00b04780)
- 新版 [`00b04818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b047f0.md#insn-00b04818) · [`00b04804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b047f0.md#insn-00b04804) · [`00b0481c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b047f0.md#insn-00b0481c)

~~~diff
- 00b0477c ["INT_ADD", "register:40f0:8", ["const:b0477c:8", "const:4:8"]]
- 00b0477c ["CALL", null, ["callee:005e7460:8"]]
+ 00b04818 ["INT_ADD", "register:40f0:8", ["const:b04818:8", "const:4:8"]]
+ 00b04818 ["CALL", null, ["callee:005e7460:8"]]
- 00b0477c bytes 298beb97
+ 00b04818 bytes 128beb97
- 00b04768 ["INT_ADD", "register:40f0:8", ["const:b04768:8", "const:4:8"]]
- 00b04768 ["CALL", null, ["callee:00851550:8"]]
+ 00b04804 ["INT_ADD", "register:40f0:8", ["const:b04804:8", "const:4:8"]]
+ 00b04804 ["CALL", null, ["callee:00851550:8"]]
- 00b04768 bytes 6433f597
+ 00b04804 bytes 5333f597
- 00b04780 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b04780 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b04780 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b04780 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b0481c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b0481c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b0481c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b0481c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b04780 bytes 40010037
+ 00b0481c bytes 40010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21262beddef2b719e5fb7a7f2cdbba87"></a>

### [`00b047b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b047b8.md) → [`00b04854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04854.md) FUN_00b04854

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`006c5350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c5350.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b047cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b047b8.md#insn-00b047cc) · [`00b047e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b047b8.md#insn-00b047e0) · [`00b047e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b047b8.md#insn-00b047e8)
- 新版 [`00b04868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04854.md#insn-00b04868) · [`00b0487c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04854.md#insn-00b0487c) · [`00b04884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04854.md#insn-00b04884)

~~~diff
- 00b047cc ["INT_ADD", "register:40f0:8", ["const:b047cc:8", "const:4:8"]]
- 00b047cc ["CALL", null, ["callee:00851550:8"]]
+ 00b04868 ["INT_ADD", "register:40f0:8", ["const:b04868:8", "const:4:8"]]
+ 00b04868 ["CALL", null, ["callee:00851550:8"]]
- 00b047cc bytes 4b33f597
+ 00b04868 bytes 3a33f597
- 00b047e0 ["INT_ADD", "register:40f0:8", ["const:b047e0:8", "const:4:8"]]
- 00b047e0 ["CALL", null, ["callee:005e7460:8"]]
+ 00b0487c ["INT_ADD", "register:40f0:8", ["const:b0487c:8", "const:4:8"]]
+ 00b0487c ["CALL", null, ["callee:005e7460:8"]]
- 00b047e0 bytes 108beb97
+ 00b0487c bytes f98aeb97
- 00b047e8 ["INT_ADD", "register:40f0:8", ["const:b047e8:8", "const:4:8"]]
- 00b047e8 ["CALL", null, ["callee:00851550:8"]]
+ 00b04884 ["INT_ADD", "register:40f0:8", ["const:b04884:8", "const:4:8"]]
+ 00b04884 ["CALL", null, ["callee:00851550:8"]]
- 00b047e8 bytes 4433f597
+ 00b04884 bytes 3333f597
~~~


<a id="compare-1a72d48188ea5b5e579b48f803f338f5"></a>

### [`00b048ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b048ec.md) → [`00b04988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04988.md) FUN_00b04988

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c52f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c5/006c52f8.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) [`00af5a94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af5/00af5a94.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md)
- 新版 呼出元 4件 [`006855c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/006855c8.md) [`006c5350`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c5/006c5350.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) [`00af5b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af5/00af5b30.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00b04d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04d18.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 55.56% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b04910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b048ec.md#insn-00b04910) · [`00b04924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b048ec.md#insn-00b04924) · [`00b0492c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b048ec.md#insn-00b0492c)
- 新版 [`00b049ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04988.md#insn-00b049ac) · [`00b049c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04988.md#insn-00b049c0) · [`00b049c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04988.md#insn-00b049c8)

~~~diff
- 00b04910 ["INT_ADD", "register:40f0:8", ["const:b04910:8", "const:4:8"]]
- 00b04910 ["CALL", null, ["callee:00851550:8"]]
+ 00b049ac ["INT_ADD", "register:40f0:8", ["const:b049ac:8", "const:4:8"]]
+ 00b049ac ["CALL", null, ["callee:00851550:8"]]
- 00b04910 bytes fa32f597
+ 00b049ac bytes e932f597
- 00b04924 ["INT_ADD", "register:40f0:8", ["const:b04924:8", "const:4:8"]]
- 00b04924 ["CALL", null, ["callee:005e7460:8"]]
+ 00b049c0 ["INT_ADD", "register:40f0:8", ["const:b049c0:8", "const:4:8"]]
+ 00b049c0 ["CALL", null, ["callee:005e7460:8"]]
- 00b04924 bytes bf8aeb97
+ 00b049c0 bytes a88aeb97
- 00b0492c ["INT_ADD", "register:40f0:8", ["const:b0492c:8", "const:4:8"]]
- 00b0492c ["CALL", null, ["callee:00851550:8"]]
+ 00b049c8 ["INT_ADD", "register:40f0:8", ["const:b049c8:8", "const:4:8"]]
+ 00b049c8 ["CALL", null, ["callee:00851550:8"]]
- 00b0492c bytes f332f597
+ 00b049c8 bytes e232f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03cde704a19d5a259048192fda94dbc8"></a>

### [`00b04c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md) → [`00b04d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b04/00b04d18.md) FUN_00b04d18

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 14件 [`006c6484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6484.md) [`00aff2cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aff/00aff2cc.md) [`00b02c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02c74.md) [`00b02d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02d44.md) [`00b02e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b02/00b02e14.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00853c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c70.md) [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md)
- 新版 呼出元 14件 [`006c64dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c64dc.md) [`00aff368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aff/00aff368.md) [`00b02d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b02d10.md) [`00b02de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b02de0.md) [`00b02eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b02/00b02eb0.md) · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00853cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853cc8.md) [`00903f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00903/00903f98.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.03% / 新版 89.03%

CFGの説明率　旧版 41.12% / 新版 41.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 2件, `unresolved_branch_alignment` 13件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04cf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04cf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b04fec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b04cc4",
      "READ",
      [
        "storage",
        "0030a52c",
        null,
        null
      ]
    ],
    [
      "unmatched:00b04cc4",
      "READ",
      [
        "storage",
        "0030a53c",
        null,
        null
      ]
    ],
    [
      "00b04d80",
      "READ",
      [
        "storage",
        "0030a54c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b04d60",
      "READ",
      [
        "storage",
        "0030a56c",
        null,
        null
      ]
    ],
    [
      "00b04d60",
      "READ",
      [
        "storage",
        "0030a57c",
        null,
        null
      ]
    ],
    [
      "00b04d80",
      "READ",
      [
        "storage",
        "0030a58c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md#insn-00b04cf0) · [`00b04d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md#insn-00b04d14) · [`00b04d28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b04/00b04c7c.md#insn-00b04d28)

~~~diff
- 00b04cf0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b04cf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00b04cf0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b04cf0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00b04cf0 bytes e18301ad
- 00b04d14 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b04d14 ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
- 00b04d14 bytes 080800b4
- 00b04d28 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b04d28 ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
- 00b04d28 bytes 680700b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46439d2409037c6149148e775e6e207d"></a>

### [`00b052d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b052d4.md) → [`00b05370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05370.md) FUN_00b05370

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.94% / 新版 98.94%

CFGの説明率　旧版 63.16% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b053f4",
      "incomplete_value": true,
      "site": "00b05410",
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
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b053e4",
      "incomplete_value": true,
      "site": "00b05410",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b053e8",
      "incomplete_value": true,
      "site": "00b05410",
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
    "ordinal": 8,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b05374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b052d4.md#insn-00b05374) · [`00b05410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b052d4.md#insn-00b05410) · [`00b0542c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b052d4.md#insn-00b0542c)
- 新版 [`00b05410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05370.md#insn-00b05410) · [`00b054ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05370.md#insn-00b054ac) · [`00b054c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05370.md#insn-00b054c8)

~~~diff
- 00b05374 ["INT_ADD", "register:40f0:8", ["const:b05374:8", "const:4:8"]]
- 00b05374 ["CALL", null, ["callee:00851550:8"]]
+ 00b05410 ["INT_ADD", "register:40f0:8", ["const:b05410:8", "const:4:8"]]
+ 00b05410 ["CALL", null, ["callee:00851550:8"]]
- 00b05374 bytes 6130f597
+ 00b05410 bytes 5030f597
- 00b05410 ["INT_ADD", "register:40f0:8", ["const:b05410:8", "const:4:8"]]
- 00b05410 ["CALL", null, ["callee:00afeb84:8"]]
+ 00b054ac ["INT_ADD", "register:40f0:8", ["const:b054ac:8", "const:4:8"]]
+ 00b054ac ["CALL", null, ["callee:00afeb84:8"]]
- 00b05410 bytes b6e5ff97
+ 00b054ac bytes b6e5ff97
- 00b0542c ["INT_ADD", "register:40f0:8", ["const:b0542c:8", "const:4:8"]]
- 00b0542c ["CALL", null, ["callee:00afeb84:8"]]
+ 00b054c8 ["INT_ADD", "register:40f0:8", ["const:b054c8:8", "const:4:8"]]
+ 00b054c8 ["CALL", null, ["callee:00afeb84:8"]]
- 00b0542c bytes afe5ff97
+ 00b054c8 bytes afe5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04abb318d8d71128fec08ec30c0c70e2"></a>

### [`00b05508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05508.md) → [`00b055a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b055a4.md) FUN_00b055a4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.34% / 新版 72.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0550c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0550c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05510"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0550c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05510",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b05600",
      "DATA",
      [
        "storage",
        "0030a500",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b055a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b055ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b05600",
      "DATA",
      [
        "storage",
        "0030a540",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0550c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05508.md#insn-00b0550c) · [`00b05510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05508.md#insn-00b05510)
- 新版 [`00b055a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b055a4.md#insn-00b055a8)

~~~diff
- 00b0550c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b0550c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b0550c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b0550c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b0550c bytes f65701a9
- 00b05510 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b05510 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b05510 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b05510 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05510 bytes f44f02a9
+ 00b055a8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
+ 00b055a8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
+ 00b055a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
+ 00b055a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00b055a8 bytes f65701a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5a866016b036ced265e4823f88287cb"></a>

### [`00b0566c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b0566c.md) → [`00b05708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05708.md) FUN_00b05708

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 28.57% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0566c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0566c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05670"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b0566c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05670",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05674",
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
      "00b05708",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b0570c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b05710",
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

- 旧版 [`00b0566c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b0566c.md#insn-00b0566c) · [`00b05670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b0566c.md#insn-00b05670) · [`00b05674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b0566c.md#insn-00b05674)

~~~diff
- 00b0566c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b0566c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b0566c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b0566c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b0566c bytes fd7bbda9
- 00b05670 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b05670 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b05670 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05670 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05670 bytes f65701a9
- 00b05674 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b05674 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b05674 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b05674 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05674 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ed1d718be8a3e18ab89d1bf49b5d0f3"></a>

### [`00b05b40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05b40.md) → [`00b05bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05bdc.md) FUN_00b05bdc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 2件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 2件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b05b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05b40.md#insn-00b05b54) · [`00b05b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05b40.md#insn-00b05b68) · [`00b05b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05b40.md#insn-00b05b6c)
- 新版 [`00b05bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05bdc.md#insn-00b05bf0) · [`00b05c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05bdc.md#insn-00b05c04) · [`00b05c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05bdc.md#insn-00b05c08)

~~~diff
- 00b05b54 ["INT_ADD", "register:40f0:8", ["const:b05b54:8", "const:4:8"]]
- 00b05b54 ["CALL", null, ["callee:00851550:8"]]
+ 00b05bf0 ["INT_ADD", "register:40f0:8", ["const:b05bf0:8", "const:4:8"]]
+ 00b05bf0 ["CALL", null, ["callee:00851550:8"]]
- 00b05b54 bytes 692ef597
+ 00b05bf0 bytes 582ef597
- 00b05b68 ["INT_ADD", "register:40f0:8", ["const:b05b68:8", "const:4:8"]]
- 00b05b68 ["CALL", null, ["callee:005e7460:8"]]
+ 00b05c04 ["INT_ADD", "register:40f0:8", ["const:b05c04:8", "const:4:8"]]
+ 00b05c04 ["CALL", null, ["callee:005e7460:8"]]
- 00b05b68 bytes 2e86eb97
+ 00b05c04 bytes 1786eb97
- 00b05b6c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b05b6c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b05b6c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b05b6c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b05c08 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b05c08 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b05c08 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b05c08 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b05b6c bytes 00010037
+ 00b05c08 bytes 00010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84c822b34001444c7689a3270ea3aca5"></a>

### [`00b05b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05b9c.md) → [`00b05c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05c38.md) FUN_00b05c38

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 16.67% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05b9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05b9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b05ba0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b05b9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05ba0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b05ba4",
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
      "00b05c38",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b05c3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b05c40",
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

- 旧版 [`00b05b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05b9c.md#insn-00b05b9c) · [`00b05ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05b9c.md#insn-00b05ba0) · [`00b05ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05b9c.md#insn-00b05ba4)

~~~diff
- 00b05b9c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b05b9c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b05b9c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b05b9c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b05b9c bytes fd7bbda9
- 00b05ba0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b05ba0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b05ba0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b05ba0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05ba0 bytes f65701a9
- 00b05ba4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b05ba4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b05ba4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b05ba4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b05ba4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c51efce8dc2bf6de5b9e3c91b2e943ed"></a>

### [`00b05c44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05c44.md) → [`00b05ce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05ce0.md) FUN_00b05ce0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b05cb8",
      "incomplete_value": true,
      "site": "00b05cd4",
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
      "definition_site": "00b05ca8",
      "incomplete_value": true,
      "site": "00b05cd4",
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
      "definition_site": "00b05cac",
      "incomplete_value": true,
      "site": "00b05cd4",
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

- 旧版 [`00b05cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05c44.md#insn-00b05cd4) · [`00b05c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05c44.md#insn-00b05c60) · [`00b05c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05c44.md#insn-00b05c74)
- 新版 [`00b05d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05ce0.md#insn-00b05d70) · [`00b05cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05ce0.md#insn-00b05cfc) · [`00b05d10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05ce0.md#insn-00b05d10)

~~~diff
- 00b05cd4 ["INT_ADD", "register:40f0:8", ["const:b05cd4:8", "const:4:8"]]
- 00b05cd4 ["CALL", null, ["callee:00afeb84:8"]]
+ 00b05d70 ["INT_ADD", "register:40f0:8", ["const:b05d70:8", "const:4:8"]]
+ 00b05d70 ["CALL", null, ["callee:00afeb84:8"]]
- 00b05cd4 bytes 85e3ff97
+ 00b05d70 bytes 85e3ff97
- 00b05c60 ["INT_ADD", "register:40f0:8", ["const:b05c60:8", "const:4:8"]]
- 00b05c60 ["CALL", null, ["callee:00851550:8"]]
+ 00b05cfc ["INT_ADD", "register:40f0:8", ["const:b05cfc:8", "const:4:8"]]
+ 00b05cfc ["CALL", null, ["callee:00851550:8"]]
- 00b05c60 bytes 262ef597
+ 00b05cfc bytes 152ef597
- 00b05c74 ["INT_ADD", "register:40f0:8", ["const:b05c74:8", "const:4:8"]]
- 00b05c74 ["CALL", null, ["callee:005e7460:8"]]
+ 00b05d10 ["INT_ADD", "register:40f0:8", ["const:b05d10:8", "const:4:8"]]
+ 00b05d10 ["CALL", null, ["callee:005e7460:8"]]
- 00b05c74 bytes eb85eb97
+ 00b05d10 bytes d485eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e131f864a5e226f02e668847b77d5cb"></a>

### [`00b05cec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05cec.md) → [`00b05d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05d88.md) FUN_00b05d88

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`005f5790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005f5/005f5790.md) [`00685588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00685/00685588.md) [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 4件 [`005f57d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005f5/005f57d0.md) [`006855c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00685/006855c8.md) [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b05d08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05cec.md#insn-00b05d08) · [`00b05d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05cec.md#insn-00b05d1c) · [`00b05d20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05cec.md#insn-00b05d20)
- 新版 [`00b05da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05d88.md#insn-00b05da4) · [`00b05db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05d88.md#insn-00b05db8) · [`00b05dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05d88.md#insn-00b05dbc)

~~~diff
- 00b05d08 ["INT_ADD", "register:40f0:8", ["const:b05d08:8", "const:4:8"]]
- 00b05d08 ["CALL", null, ["callee:00851550:8"]]
+ 00b05da4 ["INT_ADD", "register:40f0:8", ["const:b05da4:8", "const:4:8"]]
+ 00b05da4 ["CALL", null, ["callee:00851550:8"]]
- 00b05d08 bytes fc2df597
+ 00b05da4 bytes eb2df597
- 00b05d1c ["INT_ADD", "register:40f0:8", ["const:b05d1c:8", "const:4:8"]]
- 00b05d1c ["CALL", null, ["callee:005e7460:8"]]
+ 00b05db8 ["INT_ADD", "register:40f0:8", ["const:b05db8:8", "const:4:8"]]
+ 00b05db8 ["CALL", null, ["callee:005e7460:8"]]
- 00b05d1c bytes c185eb97
+ 00b05db8 bytes aa85eb97
- 00b05d20 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b05d20 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b05d20 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b05d20 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b05dbc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b05dbc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b05dbc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b05dbc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b05d20 bytes 60000037
+ 00b05dbc bytes 60000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2682ffecc201e824f4e335a552873dd8"></a>

### [`00b05e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05e34.md) → [`00b05ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05ed0.md) FUN_00b05ed0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 14.29% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b05efc",
      "incomplete_value": true,
      "site": "00b05f00",
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
      "definition_site": "00b05e60",
      "incomplete_value": true,
      "site": "00b05e64",
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
    "new": {
      "definition_site": "00b05f44",
      "incomplete_value": true,
      "site": "00b05f60",
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
      "definition_site": "00b05f34",
      "incomplete_value": true,
      "site": "00b05f60",
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

- 旧版 [`00b05e64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05e34.md#insn-00b05e64) · [`00b05ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05e34.md#insn-00b05ec4) · [`00b05e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05e34.md#insn-00b05e50)
- 新版 [`00b05f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05ed0.md#insn-00b05f00) · [`00b05f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05ed0.md#insn-00b05f60) · [`00b05eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05ed0.md#insn-00b05eec)

~~~diff
- 00b05e64 ["INT_ADD", "register:40f0:8", ["const:b05e64:8", "const:4:8"]]
- 00b05e64 ["CALL", null, ["callee:005e7460:8"]]
+ 00b05f00 ["INT_ADD", "register:40f0:8", ["const:b05f00:8", "const:4:8"]]
+ 00b05f00 ["CALL", null, ["callee:005e7460:8"]]
- 00b05e64 bytes 6f85eb97
+ 00b05f00 bytes 5885eb97
- 00b05ec4 ["INT_ADD", "register:40f0:8", ["const:b05ec4:8", "const:4:8"]]
- 00b05ec4 ["CALL", null, ["callee:00afeb84:8"]]
+ 00b05f60 ["INT_ADD", "register:40f0:8", ["const:b05f60:8", "const:4:8"]]
+ 00b05f60 ["CALL", null, ["callee:00afeb84:8"]]
- 00b05ec4 bytes 09e3ff97
+ 00b05f60 bytes 09e3ff97
- 00b05e50 ["INT_ADD", "register:40f0:8", ["const:b05e50:8", "const:4:8"]]
- 00b05e50 ["CALL", null, ["callee:00851550:8"]]
+ 00b05eec ["INT_ADD", "register:40f0:8", ["const:b05eec:8", "const:4:8"]]
+ 00b05eec ["CALL", null, ["callee:00851550:8"]]
- 00b05e50 bytes aa2df597
+ 00b05eec bytes 992df597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-507d9b07fe7e99325b678adf6a494981"></a>

### [`00b05edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05edc.md) → [`00b05f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05f78.md) FUN_00b05f78

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b05f08",
      "incomplete_value": true,
      "site": "00b05f0c",
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
      "definition_site": "00b05f54",
      "incomplete_value": false,
      "site": "00b05f6c",
      "value": [
        "leaf",
        "const:3:8"
      ]
    },
    "ordinal": 3,
    "slot": 4
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b05f0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05edc.md#insn-00b05f0c) · [`00b05f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05edc.md#insn-00b05f6c) · [`00b05ef8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05edc.md#insn-00b05ef8)
- 新版 [`00b05fa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05f78.md#insn-00b05fa8) · [`00b06008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05f78.md#insn-00b06008) · [`00b05f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b05/00b05f78.md#insn-00b05f94)

~~~diff
- 00b05f0c ["INT_ADD", "register:40f0:8", ["const:b05f0c:8", "const:4:8"]]
- 00b05f0c ["CALL", null, ["callee:005e7460:8"]]
+ 00b05fa8 ["INT_ADD", "register:40f0:8", ["const:b05fa8:8", "const:4:8"]]
+ 00b05fa8 ["CALL", null, ["callee:005e7460:8"]]
- 00b05f0c bytes 4585eb97
+ 00b05fa8 bytes 2e85eb97
- 00b05f6c ["INT_ADD", "register:40f0:8", ["const:b05f6c:8", "const:4:8"]]
- 00b05f6c ["CALL", null, ["callee:00afeb84:8"]]
+ 00b06008 ["INT_ADD", "register:40f0:8", ["const:b06008:8", "const:4:8"]]
+ 00b06008 ["CALL", null, ["callee:00afeb84:8"]]
- 00b05f6c bytes dfe2ff97
+ 00b06008 bytes dfe2ff97
- 00b05ef8 ["INT_ADD", "register:40f0:8", ["const:b05ef8:8", "const:4:8"]]
- 00b05ef8 ["CALL", null, ["callee:00851550:8"]]
+ 00b05f94 ["INT_ADD", "register:40f0:8", ["const:b05f94:8", "const:4:8"]]
+ 00b05f94 ["CALL", null, ["callee:00851550:8"]]
- 00b05ef8 bytes 802df597
+ 00b05f94 bytes 6f2df597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db054d712f2bd36adb676f0d131e459a"></a>

### [`00b05f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05f84.md) → [`00b06020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b06020.md) FUN_00b06020

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 12.50% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b06094",
      "incomplete_value": true,
      "site": "00b060b0",
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
      "definition_site": "00b06084",
      "incomplete_value": true,
      "site": "00b060b0",
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
      "definition_site": "00b06088",
      "incomplete_value": true,
      "site": "00b060b0",
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

- 旧版 [`00b06014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05f84.md#insn-00b06014) · [`00b05fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05f84.md#insn-00b05fa0) · [`00b05fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b05/00b05f84.md#insn-00b05fb4)
- 新版 [`00b060b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b06020.md#insn-00b060b0) · [`00b0603c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b06020.md#insn-00b0603c) · [`00b06050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b06020.md#insn-00b06050)

~~~diff
- 00b06014 ["INT_ADD", "register:40f0:8", ["const:b06014:8", "const:4:8"]]
- 00b06014 ["CALL", null, ["callee:00afeb84:8"]]
+ 00b060b0 ["INT_ADD", "register:40f0:8", ["const:b060b0:8", "const:4:8"]]
+ 00b060b0 ["CALL", null, ["callee:00afeb84:8"]]
- 00b06014 bytes b5e2ff97
+ 00b060b0 bytes b5e2ff97
- 00b05fa0 ["INT_ADD", "register:40f0:8", ["const:b05fa0:8", "const:4:8"]]
- 00b05fa0 ["CALL", null, ["callee:00851550:8"]]
+ 00b0603c ["INT_ADD", "register:40f0:8", ["const:b0603c:8", "const:4:8"]]
+ 00b0603c ["CALL", null, ["callee:00851550:8"]]
- 00b05fa0 bytes 562df597
+ 00b0603c bytes 452df597
- 00b05fb4 ["INT_ADD", "register:40f0:8", ["const:b05fb4:8", "const:4:8"]]
- 00b05fb4 ["CALL", null, ["callee:005e7460:8"]]
+ 00b06050 ["INT_ADD", "register:40f0:8", ["const:b06050:8", "const:4:8"]]
+ 00b06050 ["CALL", null, ["callee:005e7460:8"]]
- 00b05fb4 bytes 1b85eb97
+ 00b06050 bytes 0485eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fcc427ab7736e8c372f9f75ddf1a7da"></a>

### [`00b0613c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0613c.md) → [`00b061d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b061d8.md) FUN_00b061d8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 1件 [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b061b8",
      "incomplete_value": false,
      "site": "00b061cc",
      "value": [
        "leaf",
        "const:1:8"
      ]
    },
    "ordinal": 3,
    "slot": 5
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b06194",
      "DATA",
      [
        "storage",
        "0023d3b8",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ],
  "added": [
    [
      "00b06230",
      "DATA",
      [
        "storage",
        "0023d3b8",
        null,
        "Elf64_Rela[1815]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b061cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0613c.md#insn-00b061cc) · [`00b06158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0613c.md#insn-00b06158) · [`00b0616c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0613c.md#insn-00b0616c)
- 新版 [`00b06268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b061d8.md#insn-00b06268) · [`00b061f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b061d8.md#insn-00b061f4) · [`00b06208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b061d8.md#insn-00b06208)

~~~diff
- 00b061cc ["INT_ADD", "register:40f0:8", ["const:b061cc:8", "const:4:8"]]
- 00b061cc ["CALL", null, ["callee:00afeb84:8"]]
+ 00b06268 ["INT_ADD", "register:40f0:8", ["const:b06268:8", "const:4:8"]]
+ 00b06268 ["CALL", null, ["callee:00afeb84:8"]]
- 00b061cc bytes 47e2ff97
+ 00b06268 bytes 47e2ff97
- 00b06158 ["INT_ADD", "register:40f0:8", ["const:b06158:8", "const:4:8"]]
- 00b06158 ["CALL", null, ["callee:00851550:8"]]
+ 00b061f4 ["INT_ADD", "register:40f0:8", ["const:b061f4:8", "const:4:8"]]
+ 00b061f4 ["CALL", null, ["callee:00851550:8"]]
- 00b06158 bytes e82cf597
+ 00b061f4 bytes d72cf597
- 00b0616c ["INT_ADD", "register:40f0:8", ["const:b0616c:8", "const:4:8"]]
- 00b0616c ["CALL", null, ["callee:005e7460:8"]]
+ 00b06208 ["INT_ADD", "register:40f0:8", ["const:b06208:8", "const:4:8"]]
+ 00b06208 ["CALL", null, ["callee:005e7460:8"]]
- 00b0616c bytes ad84eb97
+ 00b06208 bytes 9684eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4af2124a76def559132bc8657acae160"></a>

### [`00b061e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b061e4.md) → [`00b06280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b06280.md) FUN_00b06280

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`00a4f3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a4f/00a4f3b4.md) · 呼出先 3件 [`005e7420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e7/005e7420.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00afeae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afe/00afeae8.md)
- 新版 呼出元 2件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`00a4f424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a4f/00a4f424.md) · 呼出先 3件 [`005e7460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005e7/005e7460.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00afeb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 7.14% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b061e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b061e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b061e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b061e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b061e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b061ec",
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
      "00b06280",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b06284",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b06288",
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

- 旧版 [`00b061e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b061e4.md#insn-00b061e4) · [`00b061e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b061e4.md#insn-00b061e8) · [`00b061ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b061e4.md#insn-00b061ec)

~~~diff
- 00b061e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b061e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b061e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b061e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b061e4 bytes fd7bbda9
- 00b061e8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b061e8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b061e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b061e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b061e8 bytes f65701a9
- 00b061ec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b061ec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b061ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b061ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b061ec bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36eaaa5c7d06188229e18a00917ebd71"></a>

### [`00b0695c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0695c.md) → [`00b069f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b06/00b069f8.md) FUN_00b069f8

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006c6e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006c6/006c6e10.md) [`006cb1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006cb/006cb1d0.md) · 呼出先 10件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00853c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00853/00853c70.md) [`00903f44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00903/00903f44.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md)
- 新版 呼出元 2件 [`006c6e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006c6/006c6e68.md) [`006cb228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006cb/006cb228.md) · 呼出先 10件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`00853cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00853/00853cc8.md) [`00903f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00903/00903f98.md) [`009e1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009e1/009e1014.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 42.98% / 新版 42.98%

CFGの説明率　旧版 30.16% / 新版 30.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 39件, `unresolved_call_alignment` 20件, `unresolved_store_alignment` 55件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b06b30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b06b44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b06b44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b06a0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b06a28"
      ]
    ],
    [
      "00b06b80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b06b00"
      ]
    ],
    [
      "unmatched:00b06af0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b06b20"
      ]
    ]
  ],
  "added": [
    [
      "00b06aa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b06a28"
      ]
    ],
    [
      "00b06b80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b06b9c"
      ]
    ],
    [
      "00b06b8c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b06bbc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0695c.md#insn-00b06b30) · [`00b06b44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0695c.md#insn-00b06b44) · [`00b06b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b06/00b0695c.md#insn-00b06b4c)

~~~diff
- 00b06b30 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:1c:8"]]
- 00b06b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00b06b30 bytes 141c00b9
- 00b06b44 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b06b44 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b06b44 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b06b44 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00b06b44 bytes bf7e00a9
- 00b06b4c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:10:8"]]
- 00b06b4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00b06b4c bytes bb0a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6456bed2231cb5a4f81013ce4240c4a"></a>

### [`00b075d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b075d8.md) → [`00b07674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07674.md) _INIT_252

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00b076b0",
      "incomplete_value": true,
      "site": "00b076cc",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b076d4",
      "incomplete_value": true,
      "site": "00b076f0",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b076f4",
      "incomplete_value": true,
      "site": "00b07710",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00b076b0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b076d4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b076f4",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b076b0",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00b076d4",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00b076f4",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0768c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b075d8.md#insn-00b0768c) · [`00b076cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b075d8.md#insn-00b076cc) · [`00b07738`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b075d8.md#insn-00b07738)
- 新版 [`00b07728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07674.md#insn-00b07728) · [`00b07768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07674.md#insn-00b07768) · [`00b077d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07674.md#insn-00b077d4)

~~~diff
- 00b0768c ["COPY", "tmp:0:8", ["const:5d2:8"]]
- 00b0768c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b0768c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b0768c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b07728 ["COPY", "tmp:0:8", ["const:576:8"]]
+ 00b07728 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b07728 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b07728 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b0768c bytes 29491791
+ 00b07728 bytes 29d91591
- 00b076cc ["COPY", "tmp:0:8", ["const:f09:8"]]
- 00b076cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b076cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b076cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b07768 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00b07768 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b07768 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b07768 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b076cc bytes 29253c91
+ 00b07768 bytes 29f13a91
- 00b07738 ["INT_ADD", "register:40f0:8", ["const:b07738:8", "const:4:8"]]
- 00b07738 ["CALL", null, ["callee:0043b838:8"]]
+ 00b077d4 ["INT_ADD", "register:40f0:8", ["const:b077d4:8", "const:4:8"]]
+ 00b077d4 ["CALL", null, ["callee:0043b838:8"]]
- 00b07738 bytes 30d0e497
+ 00b077d4 bytes 19d0e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d834f7a8ceebd89a0aa617d6f4ad503d"></a>

### [`00b079c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b079c8.md) → [`00b07a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07a64.md) FUN_00b07a64

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 25件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0044108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/0044108c.md) [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00446d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/00446d70.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 25件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`004410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/004410cc.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00446db0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446db0.md)

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
      "definition_site": "00b07aa8",
      "incomplete_value": false,
      "site": "00b07ab0",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b07b14",
      "incomplete_value": true,
      "site": "00b07b14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 27,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b07b9c",
      "incomplete_value": true,
      "site": "00b07ba8",
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
                "const:99c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00b07ab0",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00b07b10",
      "READ",
      [
        "storage",
        "002af253",
        null,
        "string"
      ]
    ],
    [
      "00b07b9c",
      "READ",
      [
        "storage",
        "002a09e9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b07ab0",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "00b07b10",
      "READ",
      [
        "storage",
        "002af1f7",
        null,
        "string"
      ]
    ],
    [
      "00b07b9c",
      "READ",
      [
        "storage",
        "002a099c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b07a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b079c8.md#insn-00b07a70) · [`00b08abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b079c8.md#insn-00b08abc) · [`00b07a04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b07/00b079c8.md#insn-00b07a04)
- 新版 [`00b07b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07a64.md#insn-00b07b0c) · [`00b08b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07a64.md#insn-00b08b58) · [`00b07aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b07/00b07a64.md#insn-00b07aa0)

~~~diff
- 00b07a70 ["COPY", "tmp:0:8", ["const:253:8"]]
- 00b07a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b07a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b07a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b07b0c ["COPY", "tmp:0:8", ["const:1f7:8"]]
+ 00b07b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b07b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b07b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b07a70 bytes 084d0991
+ 00b07b0c bytes 08dd0791
- 00b08abc ["INT_ADD", "register:40f0:8", ["const:b08abc:8", "const:4:8"]]
- 00b08abc ["CALL", null, ["callee:00442970:8"]]
+ 00b08b58 ["INT_ADD", "register:40f0:8", ["const:b08b58:8", "const:4:8"]]
+ 00b08b58 ["CALL", null, ["callee:00442970:8"]]
- 00b08abc bytes 9de7e497
+ 00b08b58 bytes 86e7e497
- 00b07a04 ["INT_ADD", "register:40f0:8", ["const:b07a04:8", "const:4:8"]]
- 00b07a04 ["CALL", null, ["callee:00487e60:8"]]
+ 00b07aa0 ["INT_ADD", "register:40f0:8", ["const:b07aa0:8", "const:4:8"]]
+ 00b07aa0 ["CALL", null, ["callee:00487e60:8"]]
- 00b07a04 bytes 0701e697
+ 00b07aa0 bytes f000e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52f1ba13366dacae557c734d6cd638f7"></a>

### [`00b091a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b091a0.md) → [`00b0923c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b0923c.md) FUN_00b0923c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00963fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00963/00963fd8.md) · 呼出先 2件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0096402c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00964/0096402c.md) · 呼出先 2件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

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
      "definition_site": "00b092a0",
      "incomplete_value": false,
      "site": "00b092a4",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b092a0",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b092a0",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b09208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b091a0.md#insn-00b09208) · [`00b09204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b091a0.md#insn-00b09204) · [`00b0920c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b091a0.md#insn-00b0920c)
- 新版 [`00b092a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b0923c.md#insn-00b092a4) · [`00b092a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b0923c.md#insn-00b092a0) · [`00b092a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b0923c.md#insn-00b092a8)

~~~diff
- 00b09208 ["INT_ADD", "register:40f0:8", ["const:b09208:8", "const:4:8"]]
- 00b09208 ["CALL", null, ["callee:00442970:8"]]
+ 00b092a4 ["INT_ADD", "register:40f0:8", ["const:b092a4:8", "const:4:8"]]
+ 00b092a4 ["CALL", null, ["callee:00442970:8"]]
- 00b09208 bytes cae5e497
+ 00b092a4 bytes b3e5e497
- 00b09204 ["COPY", "tmp:0:8", ["const:1bd:8"]]
- 00b09204 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b09204 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b09204 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b092a0 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 00b092a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b092a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b092a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b09204 bytes 00f40691
+ 00b092a0 bytes 00c00591
- 00b0920c ["INT_ADD", "register:40f0:8", ["const:b0920c:8", "const:4:8"]]
- 00b0920c ["CALL", null, ["callee:00851550:8"]]
+ 00b092a8 ["INT_ADD", "register:40f0:8", ["const:b092a8:8", "const:4:8"]]
+ 00b092a8 ["CALL", null, ["callee:00851550:8"]]
- 00b0920c bytes bb20f597
+ 00b092a8 bytes aa20f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f677ee23dc362bdba1df8a764a92d511"></a>

### [`00b09274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09274.md) → [`00b09310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b09310.md) _INIT_253

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00b0934c",
      "incomplete_value": true,
      "site": "00b09368",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b09370",
      "incomplete_value": true,
      "site": "00b0938c",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b09390",
      "incomplete_value": true,
      "site": "00b093ac",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00b0934c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b09370",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b09390",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0934c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00b09370",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00b09390",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b09328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09274.md#insn-00b09328) · [`00b09368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09274.md#insn-00b09368) · [`00b093d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09274.md#insn-00b093d4)
- 新版 [`00b093c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b09310.md#insn-00b093c4) · [`00b09404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b09310.md#insn-00b09404) · [`00b09470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b09310.md#insn-00b09470)

~~~diff
- 00b09328 ["COPY", "tmp:0:8", ["const:5d2:8"]]
- 00b09328 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b09328 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b09328 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b093c4 ["COPY", "tmp:0:8", ["const:576:8"]]
+ 00b093c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b093c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b093c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b09328 bytes 29491791
+ 00b093c4 bytes 29d91591
- 00b09368 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 00b09368 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b09368 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b09368 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b09404 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00b09404 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b09404 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b09404 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b09368 bytes 29253c91
+ 00b09404 bytes 29f13a91
- 00b093d4 ["INT_ADD", "register:40f0:8", ["const:b093d4:8", "const:4:8"]]
- 00b093d4 ["CALL", null, ["callee:0043b838:8"]]
+ 00b09470 ["INT_ADD", "register:40f0:8", ["const:b09470:8", "const:4:8"]]
+ 00b09470 ["CALL", null, ["callee:0043b838:8"]]
- 00b093d4 bytes 09c9e497
+ 00b09470 bytes f2c8e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fb25001511ba5079e9d295dc2b08bdd"></a>

### [`00b0b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md) → [`00b0b6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b6dc.md) FUN_00b0b6dc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`007cceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007cc/007cceec.md) [`00aeffd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aeffd8.md) [`00b0d0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d0d4.md) [`00b0d1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d1f0.md) · 呼出先 32件 [`0046daf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046daf4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6fec.md)
- 新版 呼出元 4件 [`007ccf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007cc/007ccf44.md) [`00af0074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af0/00af0074.md) [`00b0d170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d170.md) [`00b0d28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d28c.md) · 呼出先 32件 [`0046db34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db34.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md) [`008b7044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7044.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.57% / 新版 93.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0b740",
      "incomplete_value": false,
      "site": "00b0b740",
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
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0b778",
      "incomplete_value": false,
      "site": "00b0b778",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0b798",
      "incomplete_value": false,
      "site": "00b0b798",
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
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0b740",
      "DATA",
      [
        "storage",
        "00c8edf8",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0b778",
      "DATA",
      [
        "storage",
        "00c8ef78",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0b798",
      "DATA",
      [
        "storage",
        "00c8eff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0b740",
      "DATA",
      [
        "storage",
        "00c8eec8",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0b778",
      "DATA",
      [
        "storage",
        "00c8f048",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0b798",
      "DATA",
      [
        "storage",
        "00c8f0c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0b740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md#insn-00b0b740) · [`00b0b92c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md#insn-00b0b92c) · [`00b0b960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md#insn-00b0b960)
- 新版 [`00b0b7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b6dc.md#insn-00b0b7dc) · [`00b0b9c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b6dc.md#insn-00b0b9c8) · [`00b0b9fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b6dc.md#insn-00b0b9fc)

~~~diff
- 00b0b740 ["INT_ADD", "register:40f0:8", ["const:b0b740:8", "const:4:8"]]
- 00b0b740 ["CALL", null, ["callee:008b97d4:8"]]
+ 00b0b7dc ["INT_ADD", "register:40f0:8", ["const:b0b7dc:8", "const:4:8"]]
+ 00b0b7dc ["CALL", null, ["callee:008b97d4:8"]]
- 00b0b740 bytes 0fb8f697
+ 00b0b7dc bytes feb7f697
- 00b0b92c ["INT_ADD", "register:40f0:8", ["const:b0b92c:8", "const:4:8"]]
- 00b0b92c ["CALL", null, ["callee:00c53da0:8"]]
+ 00b0b9c8 ["INT_ADD", "register:40f0:8", ["const:b0b9c8:8", "const:4:8"]]
+ 00b0b9c8 ["CALL", null, ["callee:00c53da0:8"]]
- 00b0b92c bytes f5200594
+ 00b0b9c8 bytes f6200594
- 00b0b960 ["INT_ADD", "register:40f0:8", ["const:b0b960:8", "const:4:8"]]
- 00b0b960 ["CALL", null, ["callee:00c57f80:8"]]
+ 00b0b9fc ["INT_ADD", "register:40f0:8", ["const:b0b9fc:8", "const:4:8"]]
+ 00b0b9fc ["CALL", null, ["callee:00c57f80:8"]]
- 00b0b960 bytes 54310594
+ 00b0b9fc bytes 61310594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-689b5d7541e6f5aee2d46399608ee02f"></a>

### [`00b0bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0bd00.md) → [`00b0bd9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0bd9c.md) FUN_00b0bd9c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00b0b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md) [`00b0d89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d89c.md) [`00b0d9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d9d8.md) · 呼出先 20件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 3件 [`00b0b6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b6dc.md) [`00b0d938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d938.md) [`00b0da74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0da74.md) · 呼出先 20件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

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
      "definition_site": "00b0c058",
      "incomplete_value": false,
      "site": "00b0c058",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0c05c",
      "incomplete_value": false,
      "site": "00b0c05c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0c058",
      "incomplete_value": false,
      "site": "00b0c05c",
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
                "const:ca5000:8"
              ],
              [
                "leaf",
                "const:0:8"
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
      "00b0bf0c",
      "READ",
      [
        "storage",
        "002b840f",
        null,
        "string"
      ]
    ],
    [
      "00b0bf38",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b0bf7c",
      "PARAM",
      [
        "storage",
        "00ca4f00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0bf0c",
      "READ",
      [
        "storage",
        "002b83bb",
        null,
        "string"
      ]
    ],
    [
      "00b0bf38",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "00b0bf7c",
      "PARAM",
      [
        "storage",
        "00ca5000",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0bee8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0bd00.md#insn-00b0bee8) · [`00b0bf44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0bd00.md#insn-00b0bf44) · [`00b0bf98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0bd00.md#insn-00b0bf98)
- 新版 [`00b0bf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0bd9c.md#insn-00b0bf84) · [`00b0bfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0bd9c.md#insn-00b0bfe0) · [`00b0c034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0bd9c.md#insn-00b0c034)

~~~diff
- 00b0bee8 ["INT_ADD", "register:40f0:8", ["const:b0bee8:8", "const:4:8"]]
- 00b0bee8 ["CALL", null, ["callee:0047e64c:8"]]
+ 00b0bf84 ["INT_ADD", "register:40f0:8", ["const:b0bf84:8", "const:4:8"]]
+ 00b0bf84 ["CALL", null, ["callee:0047e64c:8"]]
- 00b0bee8 bytes c9c9e597
+ 00b0bf84 bytes b2c9e597
- 00b0bf44 ["INT_ADD", "register:40f0:8", ["const:b0bf44:8", "const:4:8"]]
- 00b0bf44 ["CALL", null, ["callee:00c57f50:8"]]
+ 00b0bfe0 ["INT_ADD", "register:40f0:8", ["const:b0bfe0:8", "const:4:8"]]
+ 00b0bfe0 ["CALL", null, ["callee:00c57f50:8"]]
- 00b0bf44 bytes cf2f0594
+ 00b0bfe0 bytes dc2f0594
- 00b0bf98 ["INT_ADD", "register:40f0:8", ["const:b0bf98:8", "const:4:8"]]
- 00b0bf98 ["CALL", null, ["callee:00c57f20:8"]]
+ 00b0c034 ["INT_ADD", "register:40f0:8", ["const:b0c034:8", "const:4:8"]]
+ 00b0c034 ["CALL", null, ["callee:00c57f20:8"]]
- 00b0bf98 bytes ae2f0594
+ 00b0c034 bytes bb2f0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-713c89703e98217f21d4001b4b5013f8"></a>

### [`00b0c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md) → [`00b0c2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0c2f0.md) FUN_00b0c2f0

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b0d0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d0d4.md) [`00b0d1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d1f0.md) · 呼出先 12件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md) [`00802ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ca8.md) [`00802ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802ee0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 2件 [`00b0d170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d170.md) [`00b0d28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d28c.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00802bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802bb0.md) [`00802d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802d00.md) [`00802f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00802/00802f38.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.73% / 新版 99.73%

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
      "site": "00b0c894",
      "value": [
        "leaf",
        "ram:ad6af8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0c7f8",
      "value": [
        "leaf",
        "ram:ad6a88:8"
      ]
    },
    "ordinal": 21,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0c894",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ad6a88"
      ]
    ]
  ],
  "added": [
    [
      "00b0c894",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ad6af8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0c7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md#insn-00b0c7f8) · [`00b0c294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md#insn-00b0c294) · [`00b0c29c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md#insn-00b0c29c)
- 新版 [`00b0c894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0c2f0.md#insn-00b0c894) · [`00b0c330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0c2f0.md#insn-00b0c330) · [`00b0c338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0c2f0.md#insn-00b0c338)

~~~diff
- 00b0c7f8 ["INT_ADD", "register:40f0:8", ["const:b0c7f8:8", "const:4:8"]]
- 00b0c7f8 ["CALL", null, ["ram:ad6a88:8"]]
+ 00b0c894 ["INT_ADD", "register:40f0:8", ["const:b0c894:8", "const:4:8"]]
+ 00b0c894 ["CALL", null, ["ram:ad6af8:8"]]
- 00b0c7f8 bytes a428ff97
+ 00b0c894 bytes 9928ff97
- 00b0c294 ["INT_ADD", "register:40f0:8", ["const:b0c294:8", "const:4:8"]]
- 00b0c294 ["CALL", null, ["callee:00802bb0:8"]]
+ 00b0c330 ["INT_ADD", "register:40f0:8", ["const:b0c330:8", "const:4:8"]]
+ 00b0c330 ["CALL", null, ["callee:00802bb0:8"]]
- 00b0c294 bytes 31daf397
+ 00b0c330 bytes 20daf397
- 00b0c29c ["INT_ADD", "register:40f0:8", ["const:b0c29c:8", "const:4:8"]]
- 00b0c29c ["CALL", null, ["callee:00802d00:8"]]
+ 00b0c338 ["INT_ADD", "register:40f0:8", ["const:b0c338:8", "const:4:8"]]
+ 00b0c338 ["CALL", null, ["callee:00802d00:8"]]
- 00b0c29c bytes 83daf397
+ 00b0c338 bytes 72daf397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-786420d0f6daf8fb05dbd5de8007ebc5"></a>

### [`00b0ca28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca28.md) → [`00b0cac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cac4.md) FUN_00b0cac4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b0c81c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c81c.md) [`00b0ca50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca50.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`00b0c8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0c8b8.md) [`00b0caec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0caec.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b0cad0",
      "incomplete_value": false,
      "site": "00b0cad4",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0cad0",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0cad0",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0ca38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca28.md#insn-00b0ca38) · [`00b0ca34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca28.md#insn-00b0ca34)
- 新版 [`00b0cad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cac4.md#insn-00b0cad4) · [`00b0cad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cac4.md#insn-00b0cad0)

~~~diff
- 00b0ca38 ["INT_ADD", "register:40f0:8", ["const:b0ca38:8", "const:4:8"]]
- 00b0ca38 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b0cad4 ["INT_ADD", "register:40f0:8", ["const:b0cad4:8", "const:4:8"]]
+ 00b0cad4 ["CALL", null, ["callee:0043b7b8:8"]]
- 00b0ca38 bytes 50bbe497
+ 00b0cad4 bytes 39bbe497
- 00b0ca34 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b0ca34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b0ca34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b0ca34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b0cad0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b0cad0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0cad0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0cad0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b0ca34 bytes 00303d91
+ 00b0cad0 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dcf8391350e4818280aed3ec4042008"></a>

### [`00b0ca3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca3c.md) → [`00b0cad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cad8.md) FUN_00b0cad8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b09708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b09708.md) [`00b0aea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0aea0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`00b097a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b09/00b097a4.md) [`00b0af3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0a/00b0af3c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b0cae4",
      "incomplete_value": false,
      "site": "00b0cae8",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0cae4",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0cae4",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0ca4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca3c.md#insn-00b0ca4c) · [`00b0ca48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0ca3c.md#insn-00b0ca48)
- 新版 [`00b0cae8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cad8.md#insn-00b0cae8) · [`00b0cae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cad8.md#insn-00b0cae4)

~~~diff
- 00b0ca4c ["INT_ADD", "register:40f0:8", ["const:b0ca4c:8", "const:4:8"]]
- 00b0ca4c ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b0cae8 ["INT_ADD", "register:40f0:8", ["const:b0cae8:8", "const:4:8"]]
+ 00b0cae8 ["CALL", null, ["callee:0043b7b8:8"]]
- 00b0ca4c bytes 4bbbe497
+ 00b0cae8 bytes 34bbe497
- 00b0ca48 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b0ca48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b0ca48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b0ca48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b0cae4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b0cae4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0cae4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0cae4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b0ca48 bytes 00303d91
+ 00b0cae4 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fadf0eacae4a77b6003cb5d93486d643"></a>

### [`00b0cbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cbe0.md) → [`00b0cc7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cc7c.md) FUN_00b0cc7c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00b0cca0",
      "incomplete_value": false,
      "site": "00b0cca4",
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
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0cca4",
      "DATA",
      [
        "storage",
        "00c8edf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0cca4",
      "DATA",
      [
        "storage",
        "00c8eec8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0cbf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cbe0.md#insn-00b0cbf4) · [`00b0cc04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cbe0.md#insn-00b0cc04)
- 新版 [`00b0cc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cc7c.md#insn-00b0cc90) · [`00b0cca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cc7c.md#insn-00b0cca0)

~~~diff
- 00b0cbf4 ["INT_ADD", "register:40f0:8", ["const:b0cbf4:8", "const:4:8"]]
- 00b0cbf4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0cc90 ["INT_ADD", "register:40f0:8", ["const:b0cc90:8", "const:4:8"]]
+ 00b0cc90 ["CALL", null, ["callee:00c57f60:8"]]
- 00b0cbf4 bytes a72c0594
+ 00b0cc90 bytes b42c0594
- 00b0cc04 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00b0cc04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cc04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cc04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0cca0 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00b0cca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0cca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0cca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0cc04 bytes 08e13791
+ 00b0cca0 bytes 08213b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d1d3295ad19fbe011fdcc5e320c7cd4"></a>

### [`00b0cc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cc20.md) → [`00b0ccbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0ccbc.md) FUN_00b0ccbc

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0ccc0",
      "incomplete_value": false,
      "site": "00b0ccc4",
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
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0ccc4",
      "DATA",
      [
        "storage",
        "00c8edf8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0ccc4",
      "DATA",
      [
        "storage",
        "00c8eec8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0cc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cc20.md#insn-00b0cc24)
- 新版 [`00b0ccc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0ccbc.md#insn-00b0ccc0)

~~~diff
- 00b0cc24 ["COPY", "tmp:0:8", ["const:df8:8"]]
- 00b0cc24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cc24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0cc24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0ccc0 ["COPY", "tmp:0:8", ["const:ec8:8"]]
+ 00b0ccc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0ccc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0ccc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0cc24 bytes 08e13791
+ 00b0ccc0 bytes 08213b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a59c192e2228aa819195f3ad14c687f"></a>

### [`00b0cc48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cc48.md) → [`00b0cce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cce4.md) FUN_00b0cce4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00447f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00447/00447f34.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

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
      "definition_site": "00b0cdcc",
      "incomplete_value": true,
      "site": "00b0cddc",
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
                "const:91b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0ce10",
      "incomplete_value": false,
      "site": "00b0ce10",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0ce74",
      "incomplete_value": true,
      "site": "00b0ce84",
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
                "const:361:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00b0cd38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00b0cdcc",
      "READ",
      [
        "storage",
        "002a3968",
        null,
        "string"
      ]
    ],
    [
      "00b0ce10",
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
      "00b0cd38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00b0cdcc",
      "READ",
      [
        "storage",
        "002a391b",
        null,
        "string"
      ]
    ],
    [
      "00b0ce10",
      "DATA",
      [
        "storage",
        "00c8ef38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0cc9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cc48.md#insn-00b0cc9c) · [`00b0cd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cc48.md#insn-00b0cd4c) · [`00b0cca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0cc48.md#insn-00b0cca8)
- 新版 [`00b0cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cce4.md#insn-00b0cd38) · [`00b0cde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cce4.md#insn-00b0cde8) · [`00b0cd44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0cce4.md#insn-00b0cd44)

~~~diff
- 00b0cc9c ["INT_ADD", "register:40f0:8", ["const:b0cc9c:8", "const:4:8"]]
- 00b0cc9c ["CALL", null, ["ram:47acf4:8"]]
+ 00b0cd38 ["INT_ADD", "register:40f0:8", ["const:b0cd38:8", "const:4:8"]]
+ 00b0cd38 ["CALL", null, ["ram:47ad34:8"]]
- 00b0cc9c bytes 16b8e597
+ 00b0cd38 bytes ffb7e597
- 00b0cd4c ["INT_ADD", "register:40f0:8", ["const:b0cd4c:8", "const:4:8"]]
- 00b0cd4c ["CALL", null, ["callee:0048ce94:8"]]
+ 00b0cde8 ["INT_ADD", "register:40f0:8", ["const:b0cde8:8", "const:4:8"]]
+ 00b0cde8 ["CALL", null, ["callee:0048ce94:8"]]
- 00b0cd4c bytes 4200e697
+ 00b0cde8 bytes 2b00e697
- 00b0cca8 ["INT_ADD", "register:40f0:8", ["const:b0cca8:8", "const:4:8"]]
- 00b0cca8 ["CALL", null, ["callee:0047ce14:8"]]
+ 00b0cd44 ["INT_ADD", "register:40f0:8", ["const:b0cd44:8", "const:4:8"]]
+ 00b0cd44 ["CALL", null, ["callee:0047ce14:8"]]
- 00b0cca8 bytes 4bc0e597
+ 00b0cd44 bytes 34c0e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8acd067032e7761145768df1ee46b1e4"></a>

### [`00b0d06c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d06c.md) → [`00b0d108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d108.md) FUN_00b0d108

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00b0d12c",
      "incomplete_value": false,
      "site": "00b0d130",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0d130",
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
      "00b0d130",
      "DATA",
      [
        "storage",
        "00c8ef38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d06c.md#insn-00b0d080) · [`00b0d090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d06c.md#insn-00b0d090)
- 新版 [`00b0d11c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d108.md#insn-00b0d11c) · [`00b0d12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d108.md#insn-00b0d12c)

~~~diff
- 00b0d080 ["INT_ADD", "register:40f0:8", ["const:b0d080:8", "const:4:8"]]
- 00b0d080 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0d11c ["INT_ADD", "register:40f0:8", ["const:b0d11c:8", "const:4:8"]]
+ 00b0d11c ["CALL", null, ["callee:00c57f60:8"]]
- 00b0d080 bytes 842b0594
+ 00b0d11c bytes 912b0594
- 00b0d090 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 00b0d090 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d090 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d090 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d12c ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00b0d12c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d12c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d12c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d090 bytes 08a13991
+ 00b0d12c bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f75107be7f91a359a25ca18beeff166"></a>

### [`00b0d0ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d0ac.md) → [`00b0d148`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d148.md) FUN_00b0d148

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0d14c",
      "incomplete_value": false,
      "site": "00b0d150",
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
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0d150",
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
      "00b0d150",
      "DATA",
      [
        "storage",
        "00c8ef38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d0ac.md#insn-00b0d0b0)
- 新版 [`00b0d14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d148.md#insn-00b0d14c)

~~~diff
- 00b0d0b0 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 00b0d0b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d0b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d0b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d14c ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00b0d14c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d14c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d14c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d0b0 bytes 08a13991
+ 00b0d14c bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88935a2f7fb30b146dac57935d4d148d"></a>

### [`00b0d0d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d0d4.md) → [`00b0d170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d170.md) FUN_00b0d170

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00b0b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md) [`00b0c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00b0b6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b6dc.md) [`00b0c2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0c2f0.md)

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
      "site": "00b0d1a0",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0d104",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00b0d1a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00b0d1a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d0d4.md#insn-00b0d104) · [`00b0d110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d0d4.md#insn-00b0d110)
- 新版 [`00b0d1a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d170.md#insn-00b0d1a0) · [`00b0d1ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d170.md#insn-00b0d1ac)

~~~diff
- 00b0d104 ["INT_ADD", "register:40f0:8", ["const:b0d104:8", "const:4:8"]]
- 00b0d104 ["CALL", null, ["ram:47acf4:8"]]
+ 00b0d1a0 ["INT_ADD", "register:40f0:8", ["const:b0d1a0:8", "const:4:8"]]
+ 00b0d1a0 ["CALL", null, ["ram:47ad34:8"]]
- 00b0d104 bytes fcb6e597
+ 00b0d1a0 bytes e5b6e597
- 00b0d110 ["INT_ADD", "register:40f0:8", ["const:b0d110:8", "const:4:8"]]
- 00b0d110 ["CALL", null, ["callee:0047ce14:8"]]
+ 00b0d1ac ["INT_ADD", "register:40f0:8", ["const:b0d1ac:8", "const:4:8"]]
+ 00b0d1ac ["CALL", null, ["callee:0047ce14:8"]]
- 00b0d110 bytes 31bfe597
+ 00b0d1ac bytes 1abfe597
~~~


<a id="compare-101844693c51bbd3a2ca45ea55f380c7"></a>

### [`00b0d188`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d188.md) → [`00b0d224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d224.md) FUN_00b0d224

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00b0d248",
      "incomplete_value": false,
      "site": "00b0d24c",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0d24c",
      "DATA",
      [
        "storage",
        "00c8eee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d24c",
      "DATA",
      [
        "storage",
        "00c8efb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d188.md#insn-00b0d19c) · [`00b0d1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d188.md#insn-00b0d1ac)
- 新版 [`00b0d238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d224.md#insn-00b0d238) · [`00b0d248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d224.md#insn-00b0d248)

~~~diff
- 00b0d19c ["INT_ADD", "register:40f0:8", ["const:b0d19c:8", "const:4:8"]]
- 00b0d19c ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0d238 ["INT_ADD", "register:40f0:8", ["const:b0d238:8", "const:4:8"]]
+ 00b0d238 ["CALL", null, ["callee:00c57f60:8"]]
- 00b0d19c bytes 3d2b0594
+ 00b0d238 bytes 4a2b0594
- 00b0d1ac ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00b0d1ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d1ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d1ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d248 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00b0d248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d1ac bytes 08a13b91
+ 00b0d248 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22c1a4ac675b56883b14de82558a96ce"></a>

### [`00b0d1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d1c8.md) → [`00b0d264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d264.md) FUN_00b0d264

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0d268",
      "incomplete_value": false,
      "site": "00b0d26c",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0d26c",
      "DATA",
      [
        "storage",
        "00c8eee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d26c",
      "DATA",
      [
        "storage",
        "00c8efb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d1cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d1c8.md#insn-00b0d1cc)
- 新版 [`00b0d268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d264.md#insn-00b0d268)

~~~diff
- 00b0d1cc ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00b0d1cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d1cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d1cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d268 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00b0d268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d1cc bytes 08a13b91
+ 00b0d268 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32dc19c3228ee78b75ebb3f2bd711591"></a>

### [`00b0d1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d1f0.md) → [`00b0d28c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d28c.md) FUN_00b0d28c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md) [`00b0b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b640.md) [`00b0c254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0c/00b0c254.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md) [`00b0b6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b6dc.md) [`00b0c2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0c/00b0c2f0.md)

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
      "site": "00b0d2bc",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0d220",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00b0d2bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00b0d2bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d1f0.md#insn-00b0d220) · [`00b0d22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d1f0.md#insn-00b0d22c)
- 新版 [`00b0d2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d28c.md#insn-00b0d2bc) · [`00b0d2c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d28c.md#insn-00b0d2c8)

~~~diff
- 00b0d220 ["INT_ADD", "register:40f0:8", ["const:b0d220:8", "const:4:8"]]
- 00b0d220 ["CALL", null, ["ram:47acf4:8"]]
+ 00b0d2bc ["INT_ADD", "register:40f0:8", ["const:b0d2bc:8", "const:4:8"]]
+ 00b0d2bc ["CALL", null, ["ram:47ad34:8"]]
- 00b0d220 bytes b5b6e597
+ 00b0d2bc bytes 9eb6e597
- 00b0d22c ["INT_ADD", "register:40f0:8", ["const:b0d22c:8", "const:4:8"]]
- 00b0d22c ["CALL", null, ["callee:0047ce14:8"]]
+ 00b0d2c8 ["INT_ADD", "register:40f0:8", ["const:b0d2c8:8", "const:4:8"]]
+ 00b0d2c8 ["CALL", null, ["callee:0047ce14:8"]]
- 00b0d22c bytes eabee597
+ 00b0d2c8 bytes d3bee597
~~~


<a id="compare-0be2a59d4777713f0bfb3cbde752c9d5"></a>

### [`00b0d2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2a4.md) → [`00b0d340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d340.md) FUN_00b0d340

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00b0d364",
      "incomplete_value": false,
      "site": "00b0d364",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0d364",
      "DATA",
      [
        "storage",
        "00c8ef78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d364",
      "DATA",
      [
        "storage",
        "00c8f048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d2b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2a4.md#insn-00b0d2b8) · [`00b0d2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2a4.md#insn-00b0d2c0) · [`00b0d2c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2a4.md#insn-00b0d2c4)
- 新版 [`00b0d354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d340.md#insn-00b0d354) · [`00b0d35c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d340.md#insn-00b0d35c) · [`00b0d360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d340.md#insn-00b0d360)

~~~diff
- 00b0d2b8 ["INT_ADD", "register:40f0:8", ["const:b0d2b8:8", "const:4:8"]]
- 00b0d2b8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0d354 ["INT_ADD", "register:40f0:8", ["const:b0d354:8", "const:4:8"]]
+ 00b0d354 ["CALL", null, ["callee:00c57f60:8"]]
- 00b0d2b8 bytes f62a0594
+ 00b0d354 bytes 032b0594
- 00b0d2c0 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b0d35c ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b0d2c0 bytes 080c00b0
+ 00b0d35c bytes 080c00d0
- 00b0d2c4 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00b0d2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d360 ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00b0d360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d2c4 bytes 08e13d91
+ 00b0d360 bytes 08210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8a5107d6110ffb107e7ca116143d456"></a>

### [`00b0d2d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2d8.md) → [`00b0d374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d374.md) FUN_00b0d374

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0d380",
      "incomplete_value": false,
      "site": "00b0d380",
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
            "const:48:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0d380",
      "DATA",
      [
        "storage",
        "00c8ef78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d380",
      "DATA",
      [
        "storage",
        "00c8f048",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2d8.md#insn-00b0d2dc) · [`00b0d2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2d8.md#insn-00b0d2e0)
- 新版 [`00b0d378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d374.md#insn-00b0d378) · [`00b0d37c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d374.md#insn-00b0d37c)

~~~diff
- 00b0d2dc ["COPY", "register:4048:8", ["const:c8e000:8"]]
+ 00b0d378 ["COPY", "register:4048:8", ["const:c8f000:8"]]
- 00b0d2dc bytes 090c00b0
+ 00b0d378 bytes 090c00d0
- 00b0d2e0 ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00b0d2e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b0d2e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b0d2e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b0d37c ["COPY", "tmp:0:8", ["const:48:8"]]
+ 00b0d37c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0d37c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0d37c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b0d2e0 bytes 29e13d91
+ 00b0d37c bytes 29210191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d2144f32c054c5ba443a58e1770fd98"></a>

### [`00b0d368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d368.md) → [`00b0d404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d404.md) FUN_00b0d404

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00b0d428",
      "incomplete_value": false,
      "site": "00b0d42c",
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
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0d42c",
      "DATA",
      [
        "storage",
        "00c8eff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d42c",
      "DATA",
      [
        "storage",
        "00c8f0c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d37c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d368.md#insn-00b0d37c) · [`00b0d388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d368.md#insn-00b0d388) · [`00b0d38c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d368.md#insn-00b0d38c)
- 新版 [`00b0d418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d404.md#insn-00b0d418) · [`00b0d424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d404.md#insn-00b0d424) · [`00b0d428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d404.md#insn-00b0d428)

~~~diff
- 00b0d37c ["INT_ADD", "register:40f0:8", ["const:b0d37c:8", "const:4:8"]]
- 00b0d37c ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0d418 ["INT_ADD", "register:40f0:8", ["const:b0d418:8", "const:4:8"]]
+ 00b0d418 ["CALL", null, ["callee:00c57f60:8"]]
- 00b0d37c bytes c52a0594
+ 00b0d418 bytes d22a0594
- 00b0d388 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b0d424 ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b0d388 bytes 080c00b0
+ 00b0d424 bytes 080c00d0
- 00b0d38c ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 00b0d38c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d38c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d38c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d428 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00b0d428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d38c bytes 08e13f91
+ 00b0d428 bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae1f8ebe83b996eaf15b628b9dd4513f"></a>

### [`00b0d3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d3a8.md) → [`00b0d444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d444.md) FUN_00b0d444

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0d448",
      "incomplete_value": false,
      "site": "00b0d44c",
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
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0d44c",
      "DATA",
      [
        "storage",
        "00c8eff8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d44c",
      "DATA",
      [
        "storage",
        "00c8f0c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d3a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d3a8.md#insn-00b0d3a8) · [`00b0d3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d3a8.md#insn-00b0d3ac)
- 新版 [`00b0d444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d444.md#insn-00b0d444) · [`00b0d448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d444.md#insn-00b0d448)

~~~diff
- 00b0d3a8 ["COPY", "register:4040:8", ["const:c8e000:8"]]
+ 00b0d444 ["COPY", "register:4040:8", ["const:c8f000:8"]]
- 00b0d3a8 bytes 080c00b0
+ 00b0d444 bytes 080c00d0
- 00b0d3ac ["COPY", "tmp:0:8", ["const:ff8:8"]]
- 00b0d3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d448 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 00b0d448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d3ac bytes 08e13f91
+ 00b0d448 bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61a2531e0a996a61a827d2af838ec990"></a>

### [`00b0d844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d844.md) → [`00b0d8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d8e0.md) FUN_00b0d8e0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00b0d900",
      "incomplete_value": false,
      "site": "00b0d904",
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
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0d904",
      "DATA",
      [
        "storage",
        "00c8f078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d904",
      "DATA",
      [
        "storage",
        "00c8f148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d844.md#insn-00b0d858) · [`00b0d864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d844.md#insn-00b0d864)
- 新版 [`00b0d8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d8e0.md#insn-00b0d8f4) · [`00b0d900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d8e0.md#insn-00b0d900)

~~~diff
- 00b0d858 ["INT_ADD", "register:40f0:8", ["const:b0d858:8", "const:4:8"]]
- 00b0d858 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0d8f4 ["INT_ADD", "register:40f0:8", ["const:b0d8f4:8", "const:4:8"]]
+ 00b0d8f4 ["CALL", null, ["callee:00c57f60:8"]]
- 00b0d858 bytes 8e290594
+ 00b0d8f4 bytes 9b290594
- 00b0d864 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00b0d864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d900 ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00b0d900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d864 bytes 08e10191
+ 00b0d900 bytes 08210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa9f5bdba48e40d2d19c79fe46e45ff7"></a>

### [`00b0d87c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d87c.md) → [`00b0d918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d918.md) FUN_00b0d918

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0d91c",
      "incomplete_value": false,
      "site": "00b0d920",
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
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0d920",
      "DATA",
      [
        "storage",
        "00c8f078",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0d920",
      "DATA",
      [
        "storage",
        "00c8f148",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d87c.md#insn-00b0d880)
- 新版 [`00b0d91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d918.md#insn-00b0d91c)

~~~diff
- 00b0d880 ["COPY", "tmp:0:8", ["const:78:8"]]
- 00b0d880 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d880 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d880 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0d91c ["COPY", "tmp:0:8", ["const:148:8"]]
+ 00b0d91c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d91c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0d91c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d880 bytes 08e10191
+ 00b0d91c bytes 08210591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d79bb1899dd34d86962e321e120d9b9"></a>

### [`00b0d89c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d89c.md) → [`00b0d938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d938.md) FUN_00b0d938

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00b0b384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b384.md) [`00b0bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0bd00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00b0b420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b420.md) [`00b0bd9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0bd9c.md)

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
      "site": "00b0d960",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0d8c4",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00b0d96c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0d8d0",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00b0d960",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00b0d96c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00b0d960",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00b0d96c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d89c.md#insn-00b0d8c4) · [`00b0d8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d89c.md#insn-00b0d8d0) · [`00b0d904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d89c.md#insn-00b0d904)
- 新版 [`00b0d960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d938.md#insn-00b0d960) · [`00b0d96c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d938.md#insn-00b0d96c) · [`00b0d9a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0d938.md#insn-00b0d9a0)

~~~diff
- 00b0d8c4 ["INT_ADD", "register:40f0:8", ["const:b0d8c4:8", "const:4:8"]]
- 00b0d8c4 ["CALL", null, ["ram:47acf4:8"]]
+ 00b0d960 ["INT_ADD", "register:40f0:8", ["const:b0d960:8", "const:4:8"]]
+ 00b0d960 ["CALL", null, ["ram:47ad34:8"]]
- 00b0d8c4 bytes 0cb5e597
+ 00b0d960 bytes f5b4e597
- 00b0d8d0 ["INT_ADD", "register:40f0:8", ["const:b0d8d0:8", "const:4:8"]]
- 00b0d8d0 ["CALL", null, ["ram:47acf4:8"]]
+ 00b0d96c ["INT_ADD", "register:40f0:8", ["const:b0d96c:8", "const:4:8"]]
+ 00b0d96c ["CALL", null, ["ram:47ad34:8"]]
- 00b0d8d0 bytes 09b5e597
+ 00b0d96c bytes f2b4e597
- 00b0d904 ["INT_ADD", "register:40f0:8", ["const:b0d904:8", "const:4:8"]]
- 00b0d904 ["CALL", null, ["callee:00b0b420:8"]]
+ 00b0d9a0 ["INT_ADD", "register:40f0:8", ["const:b0d9a0:8", "const:4:8"]]
+ 00b0d9a0 ["CALL", null, ["callee:00b0b420:8"]]
- 00b0d904 bytes a0f6ff97
+ 00b0d9a0 bytes a0f6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-354beaf2442676156e49999a915dc148"></a>

### [`00b0d980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d980.md) → [`00b0da1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0da1c.md) FUN_00b0da1c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00b0da3c",
      "incomplete_value": false,
      "site": "00b0da40",
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
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0da40",
      "DATA",
      [
        "storage",
        "00c8f0f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0da40",
      "DATA",
      [
        "storage",
        "00c8f1c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d980.md#insn-00b0d994) · [`00b0d9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d980.md#insn-00b0d9a0)
- 新版 [`00b0da30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0da1c.md#insn-00b0da30) · [`00b0da3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0da1c.md#insn-00b0da3c)

~~~diff
- 00b0d994 ["INT_ADD", "register:40f0:8", ["const:b0d994:8", "const:4:8"]]
- 00b0d994 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0da30 ["INT_ADD", "register:40f0:8", ["const:b0da30:8", "const:4:8"]]
+ 00b0da30 ["CALL", null, ["callee:00c57f60:8"]]
- 00b0d994 bytes 3f290594
+ 00b0da30 bytes 4c290594
- 00b0d9a0 ["COPY", "tmp:0:8", ["const:f8:8"]]
- 00b0d9a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d9a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d9a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0da3c ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00b0da3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0da3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0da3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d9a0 bytes 08e10391
+ 00b0da3c bytes 08210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-634287f12aae9f038ef196a5ea684133"></a>

### [`00b0d9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d9b8.md) → [`00b0da54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0da54.md) FUN_00b0da54

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b0da58",
      "incomplete_value": false,
      "site": "00b0da5c",
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
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0da5c",
      "DATA",
      [
        "storage",
        "00c8f0f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0da5c",
      "DATA",
      [
        "storage",
        "00c8f1c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d9bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d9b8.md#insn-00b0d9bc)
- 新版 [`00b0da58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0da54.md#insn-00b0da58)

~~~diff
- 00b0d9bc ["COPY", "tmp:0:8", ["const:f8:8"]]
- 00b0d9bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d9bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0d9bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0da58 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00b0da58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0da58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0da58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0d9bc bytes 08e10391
+ 00b0da58 bytes 08210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8af293e85b24314097bca1ceff09c24d"></a>

### [`00b0d9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d9d8.md) → [`00b0da74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0da74.md) FUN_00b0da74

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00b0b384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0b384.md) [`00b0bd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0b/00b0bd00.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`00b0b420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0b420.md) [`00b0bd9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0b/00b0bd9c.md)

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
      "site": "00b0da9c",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0da00",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "site": "00b0daa8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b0da0c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00b0da9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00b0daa8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00b0da9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ],
    [
      "00b0daa8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0da00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d9d8.md#insn-00b0da00) · [`00b0da0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d9d8.md#insn-00b0da0c) · [`00b0da44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d9d8.md#insn-00b0da44)
- 新版 [`00b0da9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0da74.md#insn-00b0da9c) · [`00b0daa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0da74.md#insn-00b0daa8) · [`00b0dae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0da74.md#insn-00b0dae0)

~~~diff
- 00b0da00 ["INT_ADD", "register:40f0:8", ["const:b0da00:8", "const:4:8"]]
- 00b0da00 ["CALL", null, ["ram:47acf4:8"]]
+ 00b0da9c ["INT_ADD", "register:40f0:8", ["const:b0da9c:8", "const:4:8"]]
+ 00b0da9c ["CALL", null, ["ram:47ad34:8"]]
- 00b0da00 bytes bdb4e597
+ 00b0da9c bytes a6b4e597
- 00b0da0c ["INT_ADD", "register:40f0:8", ["const:b0da0c:8", "const:4:8"]]
- 00b0da0c ["CALL", null, ["ram:47acf4:8"]]
+ 00b0daa8 ["INT_ADD", "register:40f0:8", ["const:b0daa8:8", "const:4:8"]]
+ 00b0daa8 ["CALL", null, ["ram:47ad34:8"]]
- 00b0da0c bytes bab4e597
+ 00b0daa8 bytes a3b4e597
- 00b0da44 ["INT_ADD", "register:40f0:8", ["const:b0da44:8", "const:4:8"]]
- 00b0da44 ["CALL", null, ["callee:00b0b420:8"]]
+ 00b0dae0 ["INT_ADD", "register:40f0:8", ["const:b0dae0:8", "const:4:8"]]
+ 00b0dae0 ["CALL", null, ["callee:00b0b420:8"]]
- 00b0da44 bytes 50f6ff97
+ 00b0dae0 bytes 50f6ff97
~~~


<a id="compare-e037ee63f9710c48bfc6558ee5d30d0a"></a>

### [`00b0db74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0db74.md) → [`00b0dc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0dc10.md) _INIT_254

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00b0dc4c",
      "incomplete_value": true,
      "site": "00b0dc68",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0dc70",
      "incomplete_value": true,
      "site": "00b0dc8c",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0dc90",
      "incomplete_value": true,
      "site": "00b0dcac",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00b0dc4c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b0dc70",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b0dc90",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0dc4c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00b0dc70",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00b0dc90",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0dc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0db74.md#insn-00b0dc28) · [`00b0dc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0db74.md#insn-00b0dc68) · [`00b0dcd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0db74.md#insn-00b0dcd4)
- 新版 [`00b0dcc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0dc10.md#insn-00b0dcc4) · [`00b0dd04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0dc10.md#insn-00b0dd04) · [`00b0dd70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0dc10.md#insn-00b0dd70)

~~~diff
- 00b0dc28 ["COPY", "tmp:0:8", ["const:5d2:8"]]
- 00b0dc28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b0dc28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b0dc28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b0dcc4 ["COPY", "tmp:0:8", ["const:576:8"]]
+ 00b0dcc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0dcc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0dcc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b0dc28 bytes 29491791
+ 00b0dcc4 bytes 29d91591
- 00b0dc68 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 00b0dc68 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b0dc68 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b0dc68 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b0dd04 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00b0dd04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0dd04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0dd04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b0dc68 bytes 29253c91
+ 00b0dd04 bytes 29f13a91
- 00b0dcd4 ["INT_ADD", "register:40f0:8", ["const:b0dcd4:8", "const:4:8"]]
- 00b0dcd4 ["CALL", null, ["callee:0043b838:8"]]
+ 00b0dd70 ["INT_ADD", "register:40f0:8", ["const:b0dd70:8", "const:4:8"]]
+ 00b0dd70 ["CALL", null, ["callee:0043b838:8"]]
- 00b0dcd4 bytes c9b6e497
+ 00b0dd70 bytes b2b6e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7121abf00e1957c9b110b82bc206445f"></a>

### [`00b0df04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0df04.md) → [`00b0dfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0dfa0.md) FUN_00b0dfa0

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) [`007a0784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007a0/007a0784.md) [`00b0df04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0df04.md) · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00492e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492e08.md) [`005da584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005da/005da584.md) [`00684fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00684/00684fb0.md)
- 新版 呼出元 3件 [`00798ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md) [`007a07dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md) [`00b0dfa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0dfa0.md) · 呼出先 16件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00492e48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492e48.md) [`005da5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005da/005da5c4.md) [`00684ff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00684/00684ff0.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.25% / 新版 88.25%

CFGの説明率　旧版 75.53% / 新版 75.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0e134",
      "incomplete_value": true,
      "site": "00b0e148",
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
                "const:d3e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0e210",
      "incomplete_value": true,
      "site": "00b0e220",
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
                "const:694:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0e214",
      "incomplete_value": true,
      "site": "00b0e224",
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
      "00b0e100",
      "PARAM",
      [
        "storage",
        "002beb4e",
        null,
        null
      ]
    ],
    [
      "00b0e134",
      "READ",
      [
        "storage",
        "002bdd92",
        null,
        "string"
      ]
    ],
    [
      "00b0e1b4",
      "PARAM",
      [
        "storage",
        "002acb25",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0e100",
      "PARAM",
      [
        "storage",
        "002beafa",
        null,
        null
      ]
    ],
    [
      "00b0e134",
      "READ",
      [
        "storage",
        "002bdd3e",
        null,
        "string"
      ]
    ],
    [
      "00b0e1b4",
      "PARAM",
      [
        "storage",
        "002acac9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0df04.md#insn-00b0e010) · [`00b0e1ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0df04.md#insn-00b0e1ac) · [`00b0e218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0df04.md#insn-00b0e218)
- 新版 [`00b0e0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0dfa0.md#insn-00b0e0ac) · [`00b0e248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0dfa0.md#insn-00b0e248) · [`00b0e2b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0d/00b0dfa0.md#insn-00b0e2b4)

~~~diff
- 00b0e010 ["INT_ADD", "register:40f0:8", ["const:b0e010:8", "const:4:8"]]
- 00b0e010 ["CALL", null, ["local:b0:8"]]
+ 00b0e0ac ["INT_ADD", "register:40f0:8", ["const:b0e0ac:8", "const:4:8"]]
+ 00b0e0ac ["CALL", null, ["local:b0:8"]]
- 00b0e010 bytes bdffff97
+ 00b0e0ac bytes bdffff97
- 00b0e1ac ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b0e1ac ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b0e1ac ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b0e1ac ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b0e248 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
+ 00b0e248 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b0e248 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b0e248 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b0e1ac bytes 09080037
+ 00b0e248 bytes 09080037
- 00b0e218 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00b0e218 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b0e218 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b0e218 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b0e2b4 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
+ 00b0e2b4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b0e2b4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b0e2b4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b0e218 bytes 49060037
+ 00b0e2b4 bytes 49060037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d66f08b9a35e47eafa1be80e49b4f8f"></a>

### [`00b0e5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e5a4.md) → [`00b0e640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0e640.md) _INIT_255

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00b0e67c",
      "incomplete_value": true,
      "site": "00b0e698",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0e5e0",
      "incomplete_value": true,
      "site": "00b0e5fc",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0e6a0",
      "incomplete_value": true,
      "site": "00b0e6bc",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0e604",
      "incomplete_value": true,
      "site": "00b0e620",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0e6c0",
      "incomplete_value": true,
      "site": "00b0e6dc",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0e624",
      "incomplete_value": true,
      "site": "00b0e640",
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
      "00b0e67c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b0e6a0",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b0e6c0",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0e67c",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00b0e6a0",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00b0e6c0",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e5a4.md#insn-00b0e658) · [`00b0e698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e5a4.md#insn-00b0e698) · [`00b0e704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e5a4.md#insn-00b0e704)
- 新版 [`00b0e6f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0e640.md#insn-00b0e6f4) · [`00b0e734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0e640.md#insn-00b0e734) · [`00b0e7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0e640.md#insn-00b0e7a0)

~~~diff
- 00b0e658 ["COPY", "tmp:0:8", ["const:5d2:8"]]
- 00b0e658 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b0e658 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b0e658 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b0e6f4 ["COPY", "tmp:0:8", ["const:576:8"]]
+ 00b0e6f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0e6f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0e6f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b0e658 bytes 29491791
+ 00b0e6f4 bytes 29d91591
- 00b0e698 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 00b0e698 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b0e698 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b0e698 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b0e734 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00b0e734 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0e734 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0e734 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b0e698 bytes 29253c91
+ 00b0e734 bytes 29f13a91
- 00b0e704 ["INT_ADD", "register:40f0:8", ["const:b0e704:8", "const:4:8"]]
- 00b0e704 ["CALL", null, ["callee:0043b838:8"]]
+ 00b0e7a0 ["INT_ADD", "register:40f0:8", ["const:b0e7a0:8", "const:4:8"]]
+ 00b0e7a0 ["CALL", null, ["callee:0043b838:8"]]
- 00b0e704 bytes 3db4e497
+ 00b0e7a0 bytes 26b4e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3e88a72600e37ca7437d42a2e235d3e"></a>

### [`00b0e934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e934.md) → [`00b0e9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0e9d0.md) FUN_00b0e9d0

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00798ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798ea0.md) [`007acacc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ac/007acacc.md) [`007ad104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ad/007ad104.md) [`00b0ea7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0ea7c.md) · 呼出先 7件 [`0048ccf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ccf8.md) [`00492ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00492/00492ccc.md) [`009a76e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a7/009a76e8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 4件 [`00798ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md) [`007acb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ac/007acb24.md) [`007ad15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007ad/007ad15c.md) [`00b0eb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0eb18.md) · 呼出先 7件 [`0048cd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cd38.md) [`00492d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00492/00492d0c.md) [`009a773c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009a7/009a773c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00b0ea14",
      "incomplete_value": true,
      "site": "00b0ea20",
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
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0ea10",
      "incomplete_value": true,
      "site": "00b0ea24",
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
                "const:372:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0ea10",
      "incomplete_value": true,
      "site": "00b0ea24",
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
      "00b0ea10",
      "READ",
      [
        "storage",
        "002b03ce",
        null,
        "string"
      ]
    ],
    [
      "00b0ea10",
      "READ",
      [
        "storage",
        "002b03de",
        null,
        "string"
      ]
    ],
    [
      "00b0ea14",
      "READ",
      [
        "storage",
        "002c2e00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b0ea10",
      "READ",
      [
        "storage",
        "002b0372",
        null,
        "string"
      ]
    ],
    [
      "00b0ea10",
      "READ",
      [
        "storage",
        "002b0382",
        null,
        "string"
      ]
    ],
    [
      "00b0ea14",
      "READ",
      [
        "storage",
        "002c2e40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e9a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e934.md#insn-00b0e9a4) · [`00b0e9dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e934.md#insn-00b0e9dc) · [`00b0ea78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0e934.md#insn-00b0ea78)
- 新版 [`00b0ea40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0e9d0.md#insn-00b0ea40) · [`00b0ea78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0e9d0.md#insn-00b0ea78) · [`00b0eb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0e9d0.md#insn-00b0eb14)

~~~diff
- 00b0e9a4 ["INT_ADD", "register:40f0:8", ["const:b0e9a4:8", "const:4:8"]]
- 00b0e9a4 ["CALL", null, ["callee:00c58260:8"]]
+ 00b0ea40 ["INT_ADD", "register:40f0:8", ["const:b0ea40:8", "const:4:8"]]
+ 00b0ea40 ["CALL", null, ["callee:00c58260:8"]]
- 00b0e9a4 bytes fb250594
+ 00b0ea40 bytes 08260594
- 00b0e9dc ["INT_ADD", "register:40f0:8", ["const:b0e9dc:8", "const:4:8"]]
- 00b0e9dc ["CALL", null, ["ram:48ccf8:8"]]
+ 00b0ea78 ["INT_ADD", "register:40f0:8", ["const:b0ea78:8", "const:4:8"]]
+ 00b0ea78 ["CALL", null, ["ram:48cd38:8"]]
- 00b0e9dc bytes c7f8e597
+ 00b0ea78 bytes b0f8e597
- 00b0ea78 ["INT_ADD", "register:40f0:8", ["const:b0ea78:8", "const:4:8"]]
- 00b0ea78 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00b0eb14 ["INT_ADD", "register:40f0:8", ["const:b0eb14:8", "const:4:8"]]
+ 00b0eb14 ["CALL", null, ["callee:00c57fb0:8"]]
- 00b0ea78 bytes 1a250594
+ 00b0eb14 bytes 27250594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb4b7ee08fe977d1a10b2ec9a50d02ce"></a>

### [`00b0ea7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0ea7c.md) → [`00b0eb18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0eb18.md) FUN_00b0eb18

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00798214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00798/00798214.md) · 呼出先 15件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004519d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004519d8.md) [`004593f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004593f0.md) [`0059719c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/0059719c.md) [`00597504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597504.md)
- 新版 呼出元 1件 [`0079826c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/0079826c.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`00459430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459430.md) [`005971dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/005971dc.md) [`00597544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597544.md)

変更の種類 constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.54% / 新版 89.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0eb5c",
      "incomplete_value": false,
      "site": "00b0eb68",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0ec18",
      "incomplete_value": true,
      "site": "00b0ec1c",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0ec14",
      "incomplete_value": true,
      "site": "00b0ec20",
      "value": [
        "LOAD",
        "8",
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
      "00b0eb68",
      "DATA",
      [
        "storage",
        "00c6d678",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eba4",
      "DATA",
      [
        "storage",
        "00c63760",
        null,
        "pointer"
      ]
    ],
    [
      "00b0ebf0",
      "READ",
      [
        "storage",
        "00c63768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b0eb68",
      "DATA",
      [
        "storage",
        "00c6d748",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eba4",
      "DATA",
      [
        "storage",
        "00c63830",
        null,
        "pointer"
      ]
    ],
    [
      "00b0ebf0",
      "READ",
      [
        "storage",
        "00c63838",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0eae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0ea7c.md#insn-00b0eae4) · [`00b0ec20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0ea7c.md#insn-00b0ec20) · [`00b0eaac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0e/00b0ea7c.md#insn-00b0eaac)
- 新版 [`00b0eb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0eb18.md#insn-00b0eb80) · [`00b0ecbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0eb18.md#insn-00b0ecbc) · [`00b0eb48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0e/00b0eb18.md#insn-00b0eb48)

~~~diff
- 00b0eae4 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00b0eae4 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00b0eae4 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00b0eae4 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00b0eb80 ["COPY", "tmp:0:8", ["const:830:8"]]
+ 00b0eb80 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00b0eb80 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00b0eb80 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00b0eae4 bytes 39831d91
+ 00b0eb80 bytes 39c32091
- 00b0ec20 ["INT_ADD", "register:40f0:8", ["const:b0ec20:8", "const:4:8"]]
- 00b0ec20 ["CALL", null, ["callee:00c58280:8"]]
+ 00b0ecbc ["INT_ADD", "register:40f0:8", ["const:b0ecbc:8", "const:4:8"]]
+ 00b0ecbc ["CALL", null, ["callee:00c58280:8"]]
- 00b0ec20 bytes 64250594
+ 00b0ecbc bytes 71250594
- 00b0eaac ["INT_ADD", "register:40f0:8", ["const:b0eaac:8", "const:4:8"]]
- 00b0eaac ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0eb48 ["INT_ADD", "register:40f0:8", ["const:b0eb48:8", "const:4:8"]]
+ 00b0eb48 ["CALL", null, ["callee:00c57f60:8"]]
- 00b0eaac bytes f9240594
+ 00b0eb48 bytes 06250594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bde2f580179609a73500b67003595886"></a>

### [`00b0f07c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f07c.md) → [`00b0f118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f118.md) _INIT_256

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00b0f154",
      "incomplete_value": true,
      "site": "00b0f170",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0f178",
      "incomplete_value": true,
      "site": "00b0f194",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0f198",
      "incomplete_value": true,
      "site": "00b0f1b4",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00b0f154",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b0f178",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b0f198",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0f154",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00b0f178",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00b0f198",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0f130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f07c.md#insn-00b0f130) · [`00b0f170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f07c.md#insn-00b0f170) · [`00b0f1dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f07c.md#insn-00b0f1dc)
- 新版 [`00b0f1cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f118.md#insn-00b0f1cc) · [`00b0f20c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f118.md#insn-00b0f20c) · [`00b0f278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f118.md#insn-00b0f278)

~~~diff
- 00b0f130 ["COPY", "tmp:0:8", ["const:5d2:8"]]
- 00b0f130 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b0f130 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b0f130 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b0f1cc ["COPY", "tmp:0:8", ["const:576:8"]]
+ 00b0f1cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0f1cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0f1cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b0f130 bytes 29491791
+ 00b0f1cc bytes 29d91591
- 00b0f170 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 00b0f170 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b0f170 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b0f170 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b0f20c ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00b0f20c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0f20c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0f20c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b0f170 bytes 29253c91
+ 00b0f20c bytes 29f13a91
- 00b0f1dc ["INT_ADD", "register:40f0:8", ["const:b0f1dc:8", "const:4:8"]]
- 00b0f1dc ["CALL", null, ["callee:0043b838:8"]]
+ 00b0f278 ["INT_ADD", "register:40f0:8", ["const:b0f278:8", "const:4:8"]]
+ 00b0f278 ["CALL", null, ["callee:0043b838:8"]]
- 00b0f1dc bytes 87b1e497
+ 00b0f278 bytes 70b1e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67cdf295a84ea4db7a0b1e41fc15a9be"></a>

### [`00b0f5f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f5f4.md) → [`00b0f690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f690.md) FUN_00b0f690

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)

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
      "definition_site": "00b0f6c8",
      "incomplete_value": false,
      "site": "00b0f6d0",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0f6e4",
      "incomplete_value": true,
      "site": "00b0f6f0",
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
                "const:818:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0f848",
      "incomplete_value": true,
      "site": "00b0f84c",
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
      "00b0f6d0",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0f6e4",
      "READ",
      [
        "storage",
        "002b986c",
        null,
        "string"
      ]
    ],
    [
      "00b0f838",
      "READ",
      [
        "storage",
        "00c9abb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b0f6d0",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "00b0f6e4",
      "READ",
      [
        "storage",
        "002b9818",
        null,
        "string"
      ]
    ],
    [
      "00b0f838",
      "READ",
      [
        "storage",
        "00c9ac80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0f624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f5f4.md#insn-00b0f624) · [`00b0f62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f5f4.md#insn-00b0f62c) · [`00b0f644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f5f4.md#insn-00b0f644)
- 新版 [`00b0f6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f690.md#insn-00b0f6c0) · [`00b0f6c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f690.md#insn-00b0f6c8) · [`00b0f6e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f690.md#insn-00b0f6e0)

~~~diff
- 00b0f624 ["INT_ADD", "register:40f0:8", ["const:b0f624:8", "const:4:8"]]
- 00b0f624 ["CALL", null, ["callee:00487e60:8"]]
+ 00b0f6c0 ["INT_ADD", "register:40f0:8", ["const:b0f6c0:8", "const:4:8"]]
+ 00b0f6c0 ["CALL", null, ["callee:00487e60:8"]]
- 00b0f624 bytes ffe1e597
+ 00b0f6c0 bytes e8e1e597
- 00b0f62c ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00b0f62c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0f62c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0f62c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0f6c8 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00b0f6c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0f6c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0f6c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0f62c bytes 08e13491
+ 00b0f6c8 bytes 08213891
- 00b0f644 ["COPY", "tmp:0:8", ["const:86c:8"]]
- 00b0f644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0f644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0f644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0f6e0 ["COPY", "tmp:0:8", ["const:818:8"]]
+ 00b0f6e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0f6e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0f6e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0f644 bytes 08b12191
+ 00b0f6e0 bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65b8b00006977412a0e6fb2c4c6d5aaf"></a>

### [`00b0f8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f8b4.md) → [`00b0f950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f950.md) FUN_00b0f950

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00a85294`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a85/00a85294.md) [`00b0fa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0fa18.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00b10d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d34.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 2件 [`00a85304`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a85/00a85304.md) [`00b0fab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0fab4.md) · 呼出先 6件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00b10dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10dd0.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

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
      "definition_site": "00b0f9f0",
      "incomplete_value": false,
      "site": "00b0f9f4",
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
            "const:170:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00b0f9f0",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0f9f0",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0f958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f8b4.md#insn-00b0f958) · [`00b0f954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f8b4.md#insn-00b0f954) · [`00b0f984`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f8b4.md#insn-00b0f984)
- 新版 [`00b0f9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f950.md#insn-00b0f9f4) · [`00b0f9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f950.md#insn-00b0f9f0) · [`00b0fa20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f950.md#insn-00b0fa20)

~~~diff
- 00b0f958 ["INT_ADD", "register:40f0:8", ["const:b0f958:8", "const:4:8"]]
- 00b0f958 ["CALL", null, ["callee:00442970:8"]]
+ 00b0f9f4 ["INT_ADD", "register:40f0:8", ["const:b0f9f4:8", "const:4:8"]]
+ 00b0f9f4 ["CALL", null, ["callee:00442970:8"]]
- 00b0f958 bytes f6cbe497
+ 00b0f9f4 bytes dfcbe497
- 00b0f954 ["COPY", "tmp:0:8", ["const:1bd:8"]]
- 00b0f954 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b0f954 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b0f954 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b0f9f0 ["COPY", "tmp:0:8", ["const:170:8"]]
+ 00b0f9f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0f9f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0f9f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b0f954 bytes 00f40691
+ 00b0f9f0 bytes 00c00591
- 00b0f984 ["INT_ADD", "register:40f0:8", ["const:b0f984:8", "const:4:8"]]
- 00b0f984 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b0fa20 ["INT_ADD", "register:40f0:8", ["const:b0fa20:8", "const:4:8"]]
+ 00b0fa20 ["CALL", null, ["callee:00c57f60:8"]]
- 00b0f984 bytes 43210594
+ 00b0fa20 bytes 50210594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2bd935e16555caf109fbc3e8c0f0f04"></a>

### [`00b0fa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0fa18.md) → [`00b0fab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0fab4.md) FUN_00b0fab4

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008609ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00860/008609ec.md) · 呼出先 14件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`0046d7b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d7b0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`007de5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de5fc.md)
- 新版 呼出元 1件 [`00860a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00860/00860a44.md) · 呼出先 14件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`0046d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d7f0.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`007de654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007de/007de654.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.55% / 新版 73.55%

CFGの説明率　旧版 56.20% / 新版 56.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 52件, `unresolved_call_alignment` 17件, `unresolved_store_alignment` 63件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0fb74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0fb7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b0fb84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0fbcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0fb48"
      ]
    ],
    [
      "unmatched:00b0fb38",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0fb68"
      ]
    ],
    [
      "unmatched:00b0fb44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0fb68"
      ]
    ]
  ],
  "added": [
    [
      "00b0fbcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0fbe4"
      ]
    ],
    [
      "00b0fbd4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0fc04"
      ]
    ],
    [
      "00b0fbe0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0fc04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0fb74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0fa18.md#insn-00b0fb74) · [`00b0fb7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0fa18.md#insn-00b0fb7c) · [`00b0fb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0fa18.md#insn-00b0fb84)

~~~diff
- 00b0fb74 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:38:8"]]
- 00b0fb74 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b0fb74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b0fb74 bytes 1f1c00f9
- 00b0fb7c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00b0fb7c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00b0fb7c ["INT_ADD", "register:4040:8", ["register:4040:8", "const:30:8"]]
- 00b0fb7c ["STORE", null, ["const:1b1:8", "register:4040:8", "tmp:1:8"]]
- 00b0fb7c bytes 1f0d03f8
- 00b0fb84 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:28:8"]]
- 00b0fb84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b0fb84 bytes 081400f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b92e924239f8e3ae6b31a57897ed4795"></a>

### [`00b10d34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d34.md) → [`00b10dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10dd0.md) FUN_00b10dd0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b0f40c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f40c.md) [`00b0f8b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0f8b4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 2件 [`00b0f4a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f4a8.md) [`00b0f950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0f950.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b10ddc",
      "incomplete_value": false,
      "site": "00b10de0",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b10d40",
      "incomplete_value": false,
      "site": "00b10d44",
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
      "00b10ddc",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b10ddc",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b10d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d34.md#insn-00b10d44) · [`00b10d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d34.md#insn-00b10d40)
- 新版 [`00b10de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10dd0.md#insn-00b10de0) · [`00b10ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10dd0.md#insn-00b10ddc)

~~~diff
- 00b10d44 ["INT_ADD", "register:40f0:8", ["const:b10d44:8", "const:4:8"]]
- 00b10d44 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b10de0 ["INT_ADD", "register:40f0:8", ["const:b10de0:8", "const:4:8"]]
+ 00b10de0 ["CALL", null, ["callee:0043b7b8:8"]]
- 00b10d44 bytes 8daae497
+ 00b10de0 bytes 76aae497
- 00b10d40 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b10d40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b10d40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b10d40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b10ddc ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b10ddc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b10ddc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b10ddc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b10d40 bytes 00303d91
+ 00b10ddc bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b11d09bfc63f246dc4900b7f2c5efdac"></a>

### [`00b10d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d48.md) → [`00b10de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10de4.md) FUN_00b10de4

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b0fa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0f/00b0fa18.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 1件 [`00b0fab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b0f/00b0fab4.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

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
      "definition_site": "00b10df0",
      "incomplete_value": false,
      "site": "00b10df4",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b10d54",
      "incomplete_value": false,
      "site": "00b10d58",
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
      "00b10df0",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b10df0",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b10d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d48.md#insn-00b10d58) · [`00b10d54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d48.md#insn-00b10d54)
- 新版 [`00b10df4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10de4.md#insn-00b10df4) · [`00b10df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10de4.md#insn-00b10df0)

~~~diff
- 00b10d58 ["INT_ADD", "register:40f0:8", ["const:b10d58:8", "const:4:8"]]
- 00b10d58 ["CALL", null, ["callee:00442970:8"]]
+ 00b10df4 ["INT_ADD", "register:40f0:8", ["const:b10df4:8", "const:4:8"]]
+ 00b10df4 ["CALL", null, ["callee:00442970:8"]]
- 00b10d58 bytes f6c6e497
+ 00b10df4 bytes dfc6e497
- 00b10d54 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b10d54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b10d54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b10d54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b10df0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b10df0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b10df0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b10df0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b10d54 bytes 00303d91
+ 00b10df0 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0c8d8805619adf18b2876a33b30317f"></a>

### [`00b10d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d5c.md) → [`00b10df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10df8.md) _INIT_257

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00b10e34",
      "incomplete_value": true,
      "site": "00b10e50",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b10d98",
      "incomplete_value": true,
      "site": "00b10db4",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b10e58",
      "incomplete_value": true,
      "site": "00b10e74",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b10dbc",
      "incomplete_value": true,
      "site": "00b10dd8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b10e78",
      "incomplete_value": true,
      "site": "00b10e94",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b10ddc",
      "incomplete_value": true,
      "site": "00b10df8",
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
      "00b10e34",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b10e58",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b10e78",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b10e34",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00b10e58",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00b10e78",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b10e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d5c.md#insn-00b10e10) · [`00b10e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d5c.md#insn-00b10e50) · [`00b10ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b10/00b10d5c.md#insn-00b10ebc)
- 新版 [`00b10eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10df8.md#insn-00b10eac) · [`00b10eec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10df8.md#insn-00b10eec) · [`00b10f58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b10/00b10df8.md#insn-00b10f58)

~~~diff
- 00b10e10 ["COPY", "tmp:0:8", ["const:5d2:8"]]
- 00b10e10 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b10e10 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b10e10 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b10eac ["COPY", "tmp:0:8", ["const:576:8"]]
+ 00b10eac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b10eac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b10eac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b10e10 bytes 29491791
+ 00b10eac bytes 29d91591
- 00b10e50 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 00b10e50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b10e50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b10e50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b10eec ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00b10eec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b10eec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b10eec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b10e50 bytes 29253c91
+ 00b10eec bytes 29f13a91
- 00b10ebc ["INT_ADD", "register:40f0:8", ["const:b10ebc:8", "const:4:8"]]
- 00b10ebc ["CALL", null, ["callee:0043b838:8"]]
+ 00b10f58 ["INT_ADD", "register:40f0:8", ["const:b10f58:8", "const:4:8"]]
+ 00b10f58 ["CALL", null, ["callee:0043b838:8"]]
- 00b10ebc bytes 4faae497
+ 00b10f58 bytes 38aae497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4747166be721d48f7085c92508fe355"></a>

### [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md) → [`00b11188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md) FUN_00b11188

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 147件 [`0046d120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d120.md) [`0046e970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e970.md) [`0046f0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046f/0046f0b4.md) [`0047af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047af10.md) [`004891c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/004891c4.md) · 呼出先 20件 [`0043dba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043dba4.md) [`00470e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470e54.md) [`00471724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471724.md) [`00471930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00471/00471930.md) [`00481430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481430.md)
- 新版 呼出元 147件 [`0046d160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d160.md) [`0046e9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046e/0046e9b0.md) [`0046f0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046f/0046f0f4.md) [`0047af50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047af50.md) [`00489204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00489/00489204.md) · 呼出先 20件 [`0043dbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043dbe4.md) [`00470e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470e94.md) [`00471764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471764.md) [`00471970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00471/00471970.md) [`00481470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481470.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.53% / 新版 95.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1130c",
      "incomplete_value": true,
      "site": "00b1130c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b11270",
      "incomplete_value": true,
      "site": "00b11270",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5dc:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b114bc",
      "incomplete_value": false,
      "site": "00b114c0",
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
            "const:248:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b11420",
      "incomplete_value": false,
      "site": "00b11424",
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
            "const:178:8"
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
      "definition_site": "00b114f4",
      "incomplete_value": true,
      "site": "00b114f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b11458",
      "incomplete_value": true,
      "site": "00b11458",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5dc:8"
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
      "00b111cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "00b11268",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "00b112ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccf8"
      ]
    ]
  ],
  "added": [
    [
      "00b111cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e94"
      ]
    ],
    [
      "00b11268",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e94"
      ]
    ],
    [
      "00b112ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048cd38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b11130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md#insn-00b11130) · [`00b111b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md#insn-00b111b4) · [`00b111cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md#insn-00b111cc)
- 新版 [`00b111cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md#insn-00b111cc) · [`00b11250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md#insn-00b11250) · [`00b11268`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11188.md#insn-00b11268)

~~~diff
- 00b11130 ["INT_ADD", "register:40f0:8", ["const:b11130:8", "const:4:8"]]
- 00b11130 ["CALL", null, ["ram:470e54:8"]]
+ 00b111cc ["INT_ADD", "register:40f0:8", ["const:b111cc:8", "const:4:8"]]
+ 00b111cc ["CALL", null, ["ram:470e94:8"]]
- 00b11130 bytes 497fe597
+ 00b111cc bytes 327fe597
- 00b111b4 ["INT_ADD", "register:40f0:8", ["const:b111b4:8", "const:4:8"]]
- 00b111b4 ["CALL", null, ["callee:00488094:8"]]
+ 00b11250 ["INT_ADD", "register:40f0:8", ["const:b11250:8", "const:4:8"]]
+ 00b11250 ["CALL", null, ["callee:00488094:8"]]
- 00b111b4 bytes a8dbe597
+ 00b11250 bytes 91dbe597
- 00b111cc ["INT_ADD", "register:40f0:8", ["const:b111cc:8", "const:4:8"]]
- 00b111cc ["CALL", null, ["ram:470e54:8"]]
+ 00b11268 ["INT_ADD", "register:40f0:8", ["const:b11268:8", "const:4:8"]]
+ 00b11268 ["CALL", null, ["ram:470e94:8"]]
- 00b111cc bytes 227fe597
+ 00b11268 bytes 0b7fe597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f90982fafc9d7304496e35beb7d331c0"></a>

### [`00b11888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11888.md) → [`00b11924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11924.md) _INIT_258

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

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
      "definition_site": "00b11960",
      "incomplete_value": true,
      "site": "00b1197c",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b118c4",
      "incomplete_value": true,
      "site": "00b118e0",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b11984",
      "incomplete_value": true,
      "site": "00b119a0",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b118e8",
      "incomplete_value": true,
      "site": "00b11904",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b119a4",
      "incomplete_value": true,
      "site": "00b119c0",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b11908",
      "incomplete_value": true,
      "site": "00b11924",
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
      "00b11960",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b11984",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b119a4",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b11960",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00b11984",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00b119a4",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1193c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11888.md#insn-00b1193c) · [`00b1197c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11888.md#insn-00b1197c) · [`00b119e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11888.md#insn-00b119e8)
- 新版 [`00b119d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11924.md#insn-00b119d8) · [`00b11a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11924.md#insn-00b11a18) · [`00b11a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11924.md#insn-00b11a84)

~~~diff
- 00b1193c ["COPY", "tmp:0:8", ["const:5d2:8"]]
- 00b1193c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b1193c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b1193c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b119d8 ["COPY", "tmp:0:8", ["const:576:8"]]
+ 00b119d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b119d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b119d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b1193c bytes 29491791
+ 00b119d8 bytes 29d91591
- 00b1197c ["COPY", "tmp:0:8", ["const:f09:8"]]
- 00b1197c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b1197c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b1197c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b11a18 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00b11a18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b11a18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b11a18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b1197c bytes 29253c91
+ 00b11a18 bytes 29f13a91
- 00b119e8 ["INT_ADD", "register:40f0:8", ["const:b119e8:8", "const:4:8"]]
- 00b119e8 ["CALL", null, ["callee:0043b838:8"]]
+ 00b11a84 ["INT_ADD", "register:40f0:8", ["const:b11a84:8", "const:4:8"]]
+ 00b11a84 ["CALL", null, ["callee:0043b838:8"]]
- 00b119e8 bytes 84a7e497
+ 00b11a84 bytes 6da7e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18bd3dce68cfd1142d289b27a5bba37c"></a>

### [`00b11c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11c80.md) → [`00b11d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11d1c.md) FUN_00b11d1c

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005ba798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba798.md) · 呼出先 7件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f91c.md) [`00470e54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470e54.md) [`00470f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470f34.md) [`00a35b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a35/00a35b98.md)
- 新版 呼出元 1件 [`005ba7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba7d8.md) · 呼出先 7件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f95c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f95c.md) [`00470e94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470e94.md) [`00470f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470f74.md) [`00a35bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a35/00a35bec.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

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
      "site": "00b11d94",
      "value": [
        "leaf",
        "ram:470e94:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b11cf8",
      "value": [
        "leaf",
        "ram:470e54:8"
      ]
    },
    "ordinal": 5,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b11d6c",
      "READ",
      [
        "storage",
        "00c9b610",
        null,
        "pointer"
      ]
    ],
    [
      "00b11d94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e54"
      ]
    ],
    [
      "00b11d98",
      "PARAM",
      [
        "storage",
        "011218d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b11d6c",
      "READ",
      [
        "storage",
        "00c9b6e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b11d94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00470e94"
      ]
    ],
    [
      "00b11d98",
      "PARAM",
      [
        "storage",
        "011219d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b11cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11c80.md#insn-00b11cf8) · [`00b11ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11c80.md#insn-00b11ca0) · [`00b11ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11c80.md#insn-00b11ca4)
- 新版 [`00b11d94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11d1c.md#insn-00b11d94) · [`00b11d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11d1c.md#insn-00b11d3c) · [`00b11d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11d1c.md#insn-00b11d40)

~~~diff
- 00b11cf8 ["INT_ADD", "register:40f0:8", ["const:b11cf8:8", "const:4:8"]]
- 00b11cf8 ["CALL", null, ["ram:470e54:8"]]
+ 00b11d94 ["INT_ADD", "register:40f0:8", ["const:b11d94:8", "const:4:8"]]
+ 00b11d94 ["CALL", null, ["ram:470e94:8"]]
- 00b11cf8 bytes 577ce597
+ 00b11d94 bytes 407ce597
- 00b11ca0 ["INT_ADD", "register:40f0:8", ["const:b11ca0:8", "const:4:8"]]
- 00b11ca0 ["CALL", null, ["callee:00a38150:8"]]
+ 00b11d3c ["INT_ADD", "register:40f0:8", ["const:b11d3c:8", "const:4:8"]]
+ 00b11d3c ["CALL", null, ["callee:00a38150:8"]]
- 00b11ca0 bytes 1799fc97
+ 00b11d3c bytes 0599fc97
- 00b11ca4 ["INT_ADD", "register:40f0:8", ["const:b11ca4:8", "const:4:8"]]
- 00b11ca4 ["CALL", null, ["callee:00a35bec:8"]]
+ 00b11d40 ["INT_ADD", "register:40f0:8", ["const:b11d40:8", "const:4:8"]]
+ 00b11d40 ["CALL", null, ["callee:00a35bec:8"]]
- 00b11ca4 bytes bd8ffc97
+ 00b11d40 bytes ab8ffc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3429453048d2121d472cf20c701c84e2"></a>

### [`00b13030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b13030.md) → [`00b130cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b130cc.md) FUN_00b130cc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b11d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b11d84.md) · 呼出先 13件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`0048792c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048792c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md)
- 新版 呼出元 1件 [`00b11e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b11/00b11e20.md) · 呼出先 13件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`0048797c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048797c.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md)

変更の種類 constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1310c",
      "incomplete_value": false,
      "site": "00b13118",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b13070",
      "incomplete_value": false,
      "site": "00b1307c",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1312c",
      "incomplete_value": true,
      "site": "00b13144",
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
                "const:482:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b13090",
      "incomplete_value": true,
      "site": "00b130a8",
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
                "const:4de:8"
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
      "definition_site": "00b13148",
      "incomplete_value": true,
      "site": "00b13148",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b130ac",
      "incomplete_value": true,
      "site": "00b130ac",
      "value": [
        "LOAD",
        "8",
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
      "00b13118",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "00b1312c",
      "READ",
      [
        "storage",
        "002b14de",
        null,
        "string"
      ]
    ],
    [
      "00b13134",
      "READ",
      [
        "storage",
        "002b14ec",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b13118",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "00b1312c",
      "READ",
      [
        "storage",
        "002b1482",
        null,
        "string"
      ]
    ],
    [
      "00b13134",
      "READ",
      [
        "storage",
        "002b1490",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b13200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b13030.md#insn-00b13200) · [`00b13204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b13030.md#insn-00b13204) · [`00b13210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b13030.md#insn-00b13210)

~~~diff
- 00b13200 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b13200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b13200 bytes e80f00f9
- 00b13204 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00b13204 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b13204 bytes e93300f9
- 00b13210 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b13210 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b13210 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00b13210 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00b13210 bytes 696a28f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7246898a191b5b0c4fb6e81ce414304"></a>

### [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) → [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) FUN_00b13398

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 49件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`0046c460`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c460.md) [`00470714`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470714.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 49件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`0046c4a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046c4a0.md) [`00470754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470754.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 56.75% / 新版 56.75%

CFGの説明率　旧版 23.84% / 新版 23.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 55件, `store_condition` 32件, `store_destination` 4件, `store_value` 9件, `unresolved_branch_alignment` 464件, `unresolved_call_alignment` 309件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 377件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b13344"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b13368"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1336c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b13344",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00b13344",
      "WRITE",
      [
        "storage",
        "Stack[-0x1e0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1334c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57f60"
      ]
    ]
  ],
  "added": [
    [
      "00b133e0",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ],
    [
      "00b133e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x1e0]",
        null,
        null
      ]
    ],
    [
      "00b133e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57f60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b13344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md#insn-00b13344) · [`00b13368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md#insn-00b13368) · [`00b1336c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md#insn-00b1336c)

~~~diff
- 00b13344 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:410:8"]]
- 00b13344 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b13344 bytes e80b02f9
- 00b13368 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:400:8"]]
- 00b13368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b13368 bytes e00302f9
- 00b1336c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b1336c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b1336c bytes 0000803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80fb3fa7a1cba0d7bb488be35db917ea"></a>

### [`00b1d31c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1d/00b1d31c.md) → [`00b1d3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1d/00b1d3b8.md) FUN_00b1d3b8

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 13件 [`00487a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487a64.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`0048826c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/0048826c.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 13件 [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`004882ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/004882ac.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.30% / 新版 67.30%

CFGの説明率　旧版 17.99% / 新版 17.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 27件, `unresolved_call_alignment` 33件, `unresolved_store_alignment` 45件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d354"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d368"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1d384"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1d354",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1d358",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487e60"
      ]
    ],
    [
      "unmatched:00b1d368",
      "DATA",
      [
        "storage",
        "00c64d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b1d3f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b1d3f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00487e60"
      ]
    ],
    [
      "00b1d404",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1d354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1d/00b1d31c.md#insn-00b1d354) · [`00b1d368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1d/00b1d31c.md#insn-00b1d368) · [`00b1d384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1d/00b1d31c.md#insn-00b1d384)

~~~diff
- 00b1d354 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b1d354 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00b1d354 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b1d354 bytes a8831ff8
- 00b1d368 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:f0:8"]]
- 00b1d368 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b1d368 bytes e87b00f9
- 00b1d384 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:c8:8"]]
- 00b1d384 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b1d384 bytes e9cb00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce83a6450a1a29953575fd60dd9e2f4a"></a>

### [`00b1e088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1e088.md) → [`00b1e124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1e/00b1e124.md) FUN_00b1e124

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 25件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 26件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`0044e108`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044e/0044e108.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048795c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048795c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.40% / 新版 82.40%

CFGの説明率　旧版 41.64% / 新版 41.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_condition` 2件, `store_value` 1件, `unresolved_branch_alignment` 17件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e098"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e098"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1e09c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b1e098",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1e09c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b1e0b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x3c8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b1e134",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b1e138",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b1e150",
      "WRITE",
      [
        "storage",
        "Stack[-0x3c8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1e098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1e088.md#insn-00b1e098) · [`00b1e09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1e088.md#insn-00b1e09c) · [`00b1e0b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1e088.md#insn-00b1e0b4)

~~~diff
- 00b1e098 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b1e098 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b1e098 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b1e098 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1e098 bytes f65704a9
- 00b1e09c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b1e09c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b1e09c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b1e09c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b1e09c bytes f44f05a9
- 00b1e0b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b1e0b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b1e0b4 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df8bd2016fbda10586fe87c3fd5a5c0d"></a>

### [`00b1ef98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ef98.md) → [`00b1f034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f034.md) FUN_00b1f034

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005ba798`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005ba/005ba798.md) · 呼出先 14件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f78c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f78c.md) [`0056085c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00560/0056085c.md) [`00597ebc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00597/00597ebc.md) [`00880cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00880/00880cf4.md)
- 新版 呼出元 1件 [`005ba7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005ba7d8.md) · 呼出先 14件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f7cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f7cc.md) [`0056089c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00560/0056089c.md) [`00597efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597efc.md) [`00880d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00880/00880d4c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.35% / 新版 79.35%

CFGの説明率　旧版 46.03% / 新版 46.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f014"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f064"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b1f068"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1f084",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b1eff4"
      ]
    ],
    [
      "unmatched:00b1f000",
      "READ",
      [
        "storage",
        "002affda",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b1f014",
      "WRITE",
      [
        "storage",
        "Stack[-0x7f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b1f084",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b1f090"
      ]
    ],
    [
      "00b1f09c",
      "READ",
      [
        "storage",
        "002aff7e",
        null,
        "string"
      ]
    ],
    [
      "00b1f0b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x7f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1efc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ef98.md#insn-00b1efc8) · [`00b1efd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ef98.md#insn-00b1efd0) · [`00b1f014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1e/00b1ef98.md#insn-00b1f014)
- 新版 [`00b1f064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f034.md#insn-00b1f064) · [`00b1f06c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f034.md#insn-00b1f06c)

~~~diff
- 00b1efc8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00b1efc8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b1efc8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b1efc8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b1f064 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00b1f064 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b1f064 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b1f064 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b1efc8 bytes 80150036
+ 00b1f064 bytes 80150036
- 00b1efd0 ["INT_ADD", "register:40f0:8", ["const:b1efd0:8", "const:4:8"]]
- 00b1efd0 ["CALL", null, ["callee:00a1a7a4:8"]]
+ 00b1f06c ["INT_ADD", "register:40f0:8", ["const:b1f06c:8", "const:4:8"]]
+ 00b1f06c ["CALL", null, ["callee:00a1a7a4:8"]]
- 00b1efd0 bytes e0edfb97
+ 00b1f06c bytes ceedfb97
- 00b1f014 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00b1f014 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b1f014 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7dcc90764526fe7ae8bb8a6667f5975"></a>

### [`00b299e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b299e8.md) → [`00b29a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29a84.md) FUN_00b29a84

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00753310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00753/00753310.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00753368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00753/00753368.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 82.35% / 新版 73.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b29a28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b299e8.md#insn-00b29a28) · [`00b29a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b299e8.md#insn-00b29a54) · [`00b29a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b299e8.md#insn-00b29a60)
- 新版 [`00b29ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29a84.md#insn-00b29ac4) · [`00b29af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29a84.md#insn-00b29af0) · [`00b29afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29a84.md#insn-00b29afc)

~~~diff
- 00b29a28 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b29a28 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00b29ac4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00b29ac4 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b29a28 bytes 0a0700b5
+ 00b29ac4 bytes 0a0700b5
- 00b29a54 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b29a54 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00b29af0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b29af0 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00b29a54 bytes e80500b5
+ 00b29af0 bytes e80500b5
- 00b29a60 ["INT_ADD", "register:40f0:8", ["const:b29a60:8", "const:4:8"]]
- 00b29a60 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b29afc ["INT_ADD", "register:40f0:8", ["const:b29afc:8", "const:4:8"]]
+ 00b29afc ["CALL", null, ["callee:00c57f60:8"]]
- 00b29a60 bytes 0cb90494
+ 00b29afc bytes 19b90494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ecc434fb828e6f61ce5a1b046656f3f"></a>

### [`00b29b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29b14.md) → [`00b29bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29bb0.md) FUN_00b29bb0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b29cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cc4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b29d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29d60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 68.52% / 新版 68.52%

CFGの説明率　旧版 35.00% / 新版 35.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b29b50"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b29b7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b29bec"
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
      "unmatched:00b29b50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b29c70"
      ]
    ],
    [
      "unmatched:00b29b7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b29d54"
      ]
    ]
  ],
  "added": [
    [
      "00b29bec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b29c70"
      ]
    ],
    [
      "00b29c18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b29d54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b29b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29b14.md#insn-00b29b50) · [`00b29b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29b14.md#insn-00b29b7c) · [`00b29bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29b14.md#insn-00b29bc8)
- 新版 [`00b29c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29bb0.md#insn-00b29c64)

~~~diff
- 00b29b50 ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
- 00b29b50 bytes 22040054
- 00b29b7c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b29b7c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b29b7c ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 00b29b7c bytes e8090054
- 00b29bc8 ["INT_ADD", "register:40f0:8", ["const:b29bc8:8", "const:4:8"]]
- 00b29bc8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b29c64 ["INT_ADD", "register:40f0:8", ["const:b29c64:8", "const:4:8"]]
+ 00b29c64 ["CALL", null, ["callee:00c57f60:8"]]
- 00b29bc8 bytes b2b80494
+ 00b29c64 bytes bfb80494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-163ccda866437c5f5a884a80d46b886f"></a>

### [`00b29cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cc4.md) → [`00b29d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29d60.md) FUN_00b29d60

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b29b14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29b14.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b29bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29bb0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b29d6c",
      "incomplete_value": false,
      "site": "00b29d70",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b29cd0",
      "incomplete_value": false,
      "site": "00b29cd4",
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
      "00b29d6c",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b29d6c",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b29cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cc4.md#insn-00b29cd4) · [`00b29cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cc4.md#insn-00b29cd0)
- 新版 [`00b29d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29d60.md#insn-00b29d70) · [`00b29d6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29d60.md#insn-00b29d6c)

~~~diff
- 00b29cd4 ["INT_ADD", "register:40f0:8", ["const:b29cd4:8", "const:4:8"]]
- 00b29cd4 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b29d70 ["INT_ADD", "register:40f0:8", ["const:b29d70:8", "const:4:8"]]
+ 00b29d70 ["CALL", null, ["callee:0043b7b8:8"]]
- 00b29cd4 bytes a946e497
+ 00b29d70 bytes 9246e497
- 00b29cd0 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b29cd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b29cd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b29cd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b29d6c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b29d6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b29d6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b29d6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b29cd0 bytes 00303d91
+ 00b29d6c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc4929393f76ff4eb82205a3f5e80f3c"></a>

### [`00b29e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e6c.md) → [`00b29f08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29f08.md) FUN_00b29f08

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b29cd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29cd8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b29d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29d74.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b29f14",
      "incomplete_value": false,
      "site": "00b29f18",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b29e78",
      "incomplete_value": false,
      "site": "00b29e7c",
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
      "00b29f14",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b29f14",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b29e7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e6c.md#insn-00b29e7c) · [`00b29e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e6c.md#insn-00b29e78)
- 新版 [`00b29f18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29f08.md#insn-00b29f18) · [`00b29f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29f08.md#insn-00b29f14)

~~~diff
- 00b29e7c ["INT_ADD", "register:40f0:8", ["const:b29e7c:8", "const:4:8"]]
- 00b29e7c ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b29f18 ["INT_ADD", "register:40f0:8", ["const:b29f18:8", "const:4:8"]]
+ 00b29f18 ["CALL", null, ["callee:0043b7b8:8"]]
- 00b29e7c bytes 3f46e497
+ 00b29f18 bytes 2846e497
- 00b29e78 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b29e78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b29e78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b29e78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b29f14 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b29f14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b29f14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b29f14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b29e78 bytes 00303d91
+ 00b29f14 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56c0cc00c4eb9b687bbc1b07570b90c0"></a>

### [`00b2a010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a010.md) → [`00b2a0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a0ac.md) FUN_00b2a0ac

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b29e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b29/00b29e80.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b29f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b29/00b29f1c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b2a0b8",
      "incomplete_value": false,
      "site": "00b2a0bc",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2a01c",
      "incomplete_value": false,
      "site": "00b2a020",
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
      "00b2a0b8",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2a0b8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a010.md#insn-00b2a020) · [`00b2a01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a010.md#insn-00b2a01c)
- 新版 [`00b2a0bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a0ac.md#insn-00b2a0bc) · [`00b2a0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a0ac.md#insn-00b2a0b8)

~~~diff
- 00b2a020 ["INT_ADD", "register:40f0:8", ["const:b2a020:8", "const:4:8"]]
- 00b2a020 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b2a0bc ["INT_ADD", "register:40f0:8", ["const:b2a0bc:8", "const:4:8"]]
+ 00b2a0bc ["CALL", null, ["callee:0043b7b8:8"]]
- 00b2a020 bytes d645e497
+ 00b2a0bc bytes bf45e497
- 00b2a01c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b2a01c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a01c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a01c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a0b8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b2a0b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a0b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a0b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a01c bytes 00303d91
+ 00b2a0b8 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-740101f6c3cb307f4ac0b002f426e88c"></a>

### [`00b2a150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a150.md) → [`00b2a1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a1ec.md) FUN_00b2a1ec

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2a024`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a024.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b2a0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a0c0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b2a1f8",
      "incomplete_value": false,
      "site": "00b2a1fc",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2a15c",
      "incomplete_value": false,
      "site": "00b2a160",
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
      "00b2a1f8",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2a1f8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a150.md#insn-00b2a160) · [`00b2a15c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a150.md#insn-00b2a15c)
- 新版 [`00b2a1fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a1ec.md#insn-00b2a1fc) · [`00b2a1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a1ec.md#insn-00b2a1f8)

~~~diff
- 00b2a160 ["INT_ADD", "register:40f0:8", ["const:b2a160:8", "const:4:8"]]
- 00b2a160 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b2a1fc ["INT_ADD", "register:40f0:8", ["const:b2a1fc:8", "const:4:8"]]
+ 00b2a1fc ["CALL", null, ["callee:0043b7b8:8"]]
- 00b2a160 bytes 8645e497
+ 00b2a1fc bytes 6f45e497
- 00b2a15c ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b2a15c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a15c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a15c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a1f8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b2a1f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a1f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a1f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a15c bytes 00303d91
+ 00b2a1f8 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48f9bb661d802034283a32c31930ef54"></a>

### [`00b2a2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a2f8.md) → [`00b2a394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a394.md) FUN_00b2a394

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2a164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a164.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b2a200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a200.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b2a3a0",
      "incomplete_value": false,
      "site": "00b2a3a4",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2a304",
      "incomplete_value": false,
      "site": "00b2a308",
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
      "00b2a3a0",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2a3a0",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a2f8.md#insn-00b2a308) · [`00b2a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a2f8.md#insn-00b2a304)
- 新版 [`00b2a3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a394.md#insn-00b2a3a4) · [`00b2a3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a394.md#insn-00b2a3a0)

~~~diff
- 00b2a308 ["INT_ADD", "register:40f0:8", ["const:b2a308:8", "const:4:8"]]
- 00b2a308 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b2a3a4 ["INT_ADD", "register:40f0:8", ["const:b2a3a4:8", "const:4:8"]]
+ 00b2a3a4 ["CALL", null, ["callee:0043b7b8:8"]]
- 00b2a308 bytes 1c45e497
+ 00b2a3a4 bytes 0545e497
- 00b2a304 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b2a304 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a304 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a304 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a3a0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b2a3a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a3a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a3a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a304 bytes 00303d91
+ 00b2a3a0 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8a00ba8f5fa4f2894ac4a336755761a"></a>

### [`00b2a49c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a49c.md) → [`00b2a538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a538.md) FUN_00b2a538

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2a30c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a30c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b2a3a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a3a8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b2a544",
      "incomplete_value": false,
      "site": "00b2a548",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2a4a8",
      "incomplete_value": false,
      "site": "00b2a4ac",
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
      "00b2a544",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2a544",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a49c.md#insn-00b2a4ac) · [`00b2a4a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a49c.md#insn-00b2a4a8)
- 新版 [`00b2a548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a538.md#insn-00b2a548) · [`00b2a544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a538.md#insn-00b2a544)

~~~diff
- 00b2a4ac ["INT_ADD", "register:40f0:8", ["const:b2a4ac:8", "const:4:8"]]
- 00b2a4ac ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b2a548 ["INT_ADD", "register:40f0:8", ["const:b2a548:8", "const:4:8"]]
+ 00b2a548 ["CALL", null, ["callee:0043b7b8:8"]]
- 00b2a4ac bytes b344e497
+ 00b2a548 bytes 9c44e497
- 00b2a4a8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b2a4a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a4a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a4a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a544 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b2a544 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a544 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a544 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a4a8 bytes 00303d91
+ 00b2a544 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de1e11deb15821b0642238ade776e702"></a>

### [`00b2a4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4b0.md) → [`00b2a54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a54c.md) FUN_00b2a54c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b2a558",
      "incomplete_value": false,
      "site": "00b2a55c",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2a4bc",
      "incomplete_value": false,
      "site": "00b2a4c0",
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
      "00b2a558",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2a558",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a4c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4b0.md#insn-00b2a4c0) · [`00b2a4bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4b0.md#insn-00b2a4bc)
- 新版 [`00b2a55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a54c.md#insn-00b2a55c) · [`00b2a558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a54c.md#insn-00b2a558)

~~~diff
- 00b2a4c0 ["INT_ADD", "register:40f0:8", ["const:b2a4c0:8", "const:4:8"]]
- 00b2a4c0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b2a55c ["INT_ADD", "register:40f0:8", ["const:b2a55c:8", "const:4:8"]]
+ 00b2a55c ["CALL", null, ["callee:0043b7b8:8"]]
- 00b2a4c0 bytes ae44e497
+ 00b2a55c bytes 9744e497
- 00b2a4bc ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b2a4bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a4bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a4bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a558 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b2a558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a4bc bytes 00303d91
+ 00b2a558 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6715f036a86c2525bd930f61b836a91"></a>

### [`00b2a5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a5f0.md) → [`00b2a68c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a68c.md) FUN_00b2a68c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2a4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a4c4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b2a560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a560.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b2a698",
      "incomplete_value": false,
      "site": "00b2a69c",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2a5fc",
      "incomplete_value": false,
      "site": "00b2a600",
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
      "00b2a698",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2a698",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a5f0.md#insn-00b2a600) · [`00b2a5fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a5f0.md#insn-00b2a5fc)
- 新版 [`00b2a69c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a68c.md#insn-00b2a69c) · [`00b2a698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a68c.md#insn-00b2a698)

~~~diff
- 00b2a600 ["INT_ADD", "register:40f0:8", ["const:b2a600:8", "const:4:8"]]
- 00b2a600 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b2a69c ["INT_ADD", "register:40f0:8", ["const:b2a69c:8", "const:4:8"]]
+ 00b2a69c ["CALL", null, ["callee:0043b7b8:8"]]
- 00b2a600 bytes 5e44e497
+ 00b2a69c bytes 4744e497
- 00b2a5fc ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b2a5fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a5fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a5fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a698 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b2a698 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a698 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a698 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a5fc bytes 00303d91
+ 00b2a698 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a37e214f463cd7c0816722fa471fbae9"></a>

### [`00b2a604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a604.md) → [`00b2a6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a6a0.md) FUN_00b2a6a0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b132fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b13/00b132fc.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2a7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a7bc.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00b13398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b13/00b13398.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b2a858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a858.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 61.90% / 新版 54.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b2a74c",
      "incomplete_value": true,
      "site": "00b2a75c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "INT_MULT",
            "8",
            [
              [
                "live",
                "register:40b0:8"
              ],
              [
                "leaf",
                "const:62:8"
              ]
            ]
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
    "new": null,
    "old": {
      "definition_site": "00b2a72c",
      "incomplete_value": false,
      "site": "00b2a75c",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2a7f4",
      "incomplete_value": true,
      "site": "00b2a7f8",
      "value": [
        "live",
        "register:40b8:8"
      ]
    },
    "old": {
      "definition_site": "00b2a758",
      "incomplete_value": true,
      "site": "00b2a75c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:62:8"
          ],
          [
            "INT_MULT",
            "8",
            [
              "INT_RIGHT",
              [
                "leaf",
                "const:62:8"
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


#### 変更候補の命令位置

- 旧版 [`00b2a75c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a604.md#insn-00b2a75c) · [`00b2a774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a604.md#insn-00b2a774) · [`00b2a66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a604.md#insn-00b2a66c)
- 新版 [`00b2a7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a6a0.md#insn-00b2a7f8) · [`00b2a810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a6a0.md#insn-00b2a810) · [`00b2a708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a6a0.md#insn-00b2a708)

~~~diff
- 00b2a75c ["INT_ADD", "register:40f0:8", ["const:b2a75c:8", "const:4:8"]]
- 00b2a75c ["CALL", null, ["callee:00c58160:8"]]
+ 00b2a7f8 ["INT_ADD", "register:40f0:8", ["const:b2a7f8:8", "const:4:8"]]
+ 00b2a7f8 ["CALL", null, ["callee:00c58160:8"]]
- 00b2a75c bytes 4db60494
+ 00b2a7f8 bytes 5ab60494
- 00b2a774 ["INT_ADD", "register:40f0:8", ["const:b2a774:8", "const:4:8"]]
- 00b2a774 ["CALL", null, ["callee:00c580d0:8"]]
+ 00b2a810 ["INT_ADD", "register:40f0:8", ["const:b2a810:8", "const:4:8"]]
+ 00b2a810 ["CALL", null, ["callee:00c580d0:8"]]
- 00b2a774 bytes 23b60494
+ 00b2a810 bytes 30b60494
- 00b2a66c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b2a66c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b2a66c ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
+ 00b2a708 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b2a708 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b2a708 ["CBRANCH", null, ["local:b18:8", "tmp:1:1"]]
- 00b2a66c bytes 280a0054
+ 00b2a708 bytes 280a0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5f0232662814f991198de28094584bf"></a>

### [`00b2a7bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a7bc.md) → [`00b2a858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a858.md) FUN_00b2a858

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2a604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a604.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b2a6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a6a0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b2a864",
      "incomplete_value": false,
      "site": "00b2a868",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2a7c8",
      "incomplete_value": false,
      "site": "00b2a7cc",
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
      "00b2a864",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2a864",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a7bc.md#insn-00b2a7cc) · [`00b2a7c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a7bc.md#insn-00b2a7c8)
- 新版 [`00b2a868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a858.md#insn-00b2a868) · [`00b2a864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a858.md#insn-00b2a864)

~~~diff
- 00b2a7cc ["INT_ADD", "register:40f0:8", ["const:b2a7cc:8", "const:4:8"]]
- 00b2a7cc ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b2a868 ["INT_ADD", "register:40f0:8", ["const:b2a868:8", "const:4:8"]]
+ 00b2a868 ["CALL", null, ["callee:0043b7b8:8"]]
- 00b2a7cc bytes eb43e497
+ 00b2a868 bytes d443e497
- 00b2a7c8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b2a7c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a7c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2a7c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2a864 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b2a864 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a864 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2a864 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2a7c8 bytes 00303d91
+ 00b2a864 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52329ec18c0eb00e6c5a07d2788e088d"></a>

### [`00b2aab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aab0.md) → [`00b2ab4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ab4c.md) FUN_00b2ab4c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2a83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2a83c.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b2a8d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2a8d8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b2ab58",
      "incomplete_value": false,
      "site": "00b2ab5c",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2aabc",
      "incomplete_value": false,
      "site": "00b2aac0",
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
      "00b2ab58",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2ab58",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2aac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aab0.md#insn-00b2aac0) · [`00b2aabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2aab0.md#insn-00b2aabc)
- 新版 [`00b2ab5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ab4c.md#insn-00b2ab5c) · [`00b2ab58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ab4c.md#insn-00b2ab58)

~~~diff
- 00b2aac0 ["INT_ADD", "register:40f0:8", ["const:b2aac0:8", "const:4:8"]]
- 00b2aac0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b2ab5c ["INT_ADD", "register:40f0:8", ["const:b2ab5c:8", "const:4:8"]]
+ 00b2ab5c ["CALL", null, ["callee:0043b7b8:8"]]
- 00b2aac0 bytes 2e43e497
+ 00b2ab5c bytes 1743e497
- 00b2aabc ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b2aabc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2aabc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2aabc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2ab58 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b2ab58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2ab58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2ab58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2aabc bytes 00303d91
+ 00b2ab58 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cf42f08568a922619df7874f47ccf6d"></a>

### [`00b2abb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abb8.md) → [`00b2ac54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ac54.md) FUN_00b2ac54

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b2ac60",
      "incomplete_value": false,
      "site": "00b2ac64",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2abc4",
      "incomplete_value": false,
      "site": "00b2abc8",
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
      "00b2ac60",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2ac60",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2abc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abb8.md#insn-00b2abc8) · [`00b2abc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2a/00b2abb8.md#insn-00b2abc4)
- 新版 [`00b2ac64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ac54.md#insn-00b2ac64) · [`00b2ac60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ac54.md#insn-00b2ac60)

~~~diff
- 00b2abc8 ["INT_ADD", "register:40f0:8", ["const:b2abc8:8", "const:4:8"]]
- 00b2abc8 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b2ac64 ["INT_ADD", "register:40f0:8", ["const:b2ac64:8", "const:4:8"]]
+ 00b2ac64 ["CALL", null, ["callee:0043b7b8:8"]]
- 00b2abc8 bytes ec42e497
+ 00b2ac64 bytes d542e497
- 00b2abc4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b2abc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2abc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2abc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2ac60 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b2ac60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2ac60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2ac60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2abc4 bytes 00303d91
+ 00b2ac60 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3207b9b7538dcb2115b4a46e01ec4a50"></a>

### [`00b2b070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b070.md) → [`00b2b10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b10c.md) FUN_00b2b10c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b1f428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b1f/00b1f428.md) · 呼出先 11件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00615ecc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615ecc.md) [`006524c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/006524c0.md) [`0065254c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00652/0065254c.md) [`00b2b2f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b2f4.md)
- 新版 呼出元 1件 [`00b1f4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b1f/00b1f4c4.md) · 呼出先 11件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00615f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615f0c.md) [`00652500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652500.md) [`0065258c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/0065258c.md) [`00b2b390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b390.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 93.33% / 新版 91.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2b2a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b2b340"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00b2b2a4"
      ],
      [
        "FALL_THROUGH",
        "00b2b340"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b2b340",
      "incomplete_value": true,
      "site": "00b2b350",
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
      "definition_site": "00b2b2a4",
      "incomplete_value": true,
      "site": "00b2b2b4",
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
    "ordinal": 29,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2b2a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2b38c"
      ]
    ]
  ],
  "added": [
    [
      "00b2b340",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2b38c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b070.md#insn-00b2b2a4) · [`00b2b114`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b070.md#insn-00b2b114)
- 新版 [`00b2b340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b10c.md#insn-00b2b340) · [`00b2b1b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b10c.md#insn-00b2b1b0)

~~~diff
- 00b2b2a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b2b2a4 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
- 00b2b2a4 bytes 61020054
+ 00b2b340 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b2b340 ["CBRANCH", null, ["local:b32:8", "tmp:0:1"]]
+ 00b2b340 bytes 61020054
- 00b2b114 ["INT_ADD", "register:40f0:8", ["const:b2b114:8", "const:4:8"]]
- 00b2b114 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b2b1b0 ["INT_ADD", "register:40f0:8", ["const:b2b1b0:8", "const:4:8"]]
+ 00b2b1b0 ["CALL", null, ["callee:00c57f60:8"]]
- 00b2b114 bytes 5fb30494
+ 00b2b1b0 bytes 6cb30494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3468c7fb2a67d71a9230bd59f847bb6"></a>

### [`00b2b4cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b4cc.md) → [`00b2b568`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b568.md) FUN_00b2b568

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2b070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b070.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b2b10c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b10c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b2b574",
      "incomplete_value": false,
      "site": "00b2b578",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b4d8",
      "incomplete_value": false,
      "site": "00b2b4dc",
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
      "00b2b574",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2b574",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2b4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b4cc.md#insn-00b2b4dc) · [`00b2b4d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b4cc.md#insn-00b2b4d8)
- 新版 [`00b2b578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b568.md#insn-00b2b578) · [`00b2b574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b568.md#insn-00b2b574)

~~~diff
- 00b2b4dc ["INT_ADD", "register:40f0:8", ["const:b2b4dc:8", "const:4:8"]]
- 00b2b4dc ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b2b578 ["INT_ADD", "register:40f0:8", ["const:b2b578:8", "const:4:8"]]
+ 00b2b578 ["CALL", null, ["callee:0043b7b8:8"]]
- 00b2b4dc bytes a740e497
+ 00b2b578 bytes 9040e497
- 00b2b4d8 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b2b4d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2b4d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2b4d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2b574 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b2b574 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2b574 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2b574 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2b4d8 bytes 00303d91
+ 00b2b574 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-588d4b6d72e4cfa7bdcad2bf80cfc5bd"></a>

### [`00b2b4e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b4e0.md) → [`00b2b57c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b57c.md) _INIT_259

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00bc47f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc4/00bc47f0.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 74.04% / 新版 74.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 11件, `store_value` 9件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2b5b8",
      "incomplete_value": true,
      "site": "00b2b5d4",
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
                "const:f66:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b51c",
      "incomplete_value": true,
      "site": "00b2b538",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2b5dc",
      "incomplete_value": true,
      "site": "00b2b5f8",
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b540",
      "incomplete_value": true,
      "site": "00b2b55c",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2b5fc",
      "incomplete_value": true,
      "site": "00b2b618",
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
                "const:d6e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b560",
      "incomplete_value": true,
      "site": "00b2b57c",
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
      "00b2b5b8",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00b2b5dc",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00b2b5fc",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2b5b8",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00b2b5dc",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00b2b5fc",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2b594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b4e0.md#insn-00b2b594) · [`00b2b5d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b4e0.md#insn-00b2b5d4) · [`00b2b640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b4e0.md#insn-00b2b640)
- 新版 [`00b2b630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b57c.md#insn-00b2b630) · [`00b2b670`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b57c.md#insn-00b2b670) · [`00b2b6dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b57c.md#insn-00b2b6dc)

~~~diff
- 00b2b594 ["COPY", "tmp:0:8", ["const:5d2:8"]]
- 00b2b594 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b2b594 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b2b594 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b2b630 ["COPY", "tmp:0:8", ["const:576:8"]]
+ 00b2b630 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2b630 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2b630 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b2b594 bytes 29491791
+ 00b2b630 bytes 29d91591
- 00b2b5d4 ["COPY", "tmp:0:8", ["const:f09:8"]]
- 00b2b5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b2b5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b2b5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b2b670 ["COPY", "tmp:0:8", ["const:ebc:8"]]
+ 00b2b670 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2b670 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2b670 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b2b5d4 bytes 29253c91
+ 00b2b670 bytes 29f13a91
- 00b2b640 ["INT_ADD", "register:40f0:8", ["const:b2b640:8", "const:4:8"]]
- 00b2b640 ["CALL", null, ["callee:0043b838:8"]]
+ 00b2b6dc ["INT_ADD", "register:40f0:8", ["const:b2b6dc:8", "const:4:8"]]
+ 00b2b6dc ["CALL", null, ["callee:0043b838:8"]]
- 00b2b640 bytes 6e40e497
+ 00b2b6dc bytes 5740e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab224573576d6232e77e2e9d7cb13e78"></a>

### [`00b2b8f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b8f4.md) → [`00b2b990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b990.md) FUN_00b2b990

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043affc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043affc.md) · 呼出先 20件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f520`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f520.md) [`0046ca90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca90.md) [`0046cabc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046cabc.md) [`00495280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00495/00495280.md)
- 新版 呼出元 1件 [`0043b03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b03c.md) · 呼出先 20件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f560.md) [`0046cad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cad0.md) [`0046cafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046cafc.md) [`004952c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00495/004952c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.08% / 新版 91.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2ba44",
      "incomplete_value": false,
      "site": "00b2ba54",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b9a8",
      "incomplete_value": false,
      "site": "00b2b9b8",
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
            "const:2e8:8"
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
      "definition_site": "00b2bb74",
      "incomplete_value": false,
      "site": "00b2bb84",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2bad8",
      "incomplete_value": false,
      "site": "00b2bae8",
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
            "const:268:8"
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
      "definition_site": "00b2ba70",
      "incomplete_value": true,
      "site": "00b2ba70",
      "value": [
        "LOAD",
        "8",
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
                "const:e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2b9d4",
      "incomplete_value": true,
      "site": "00b2b9d4",
      "value": [
        "LOAD",
        "8",
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
                "const:e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2ba48",
      "READ",
      [
        "storage",
        "00c9b240",
        null,
        "pointer"
      ]
    ],
    [
      "00b2ba54",
      "DATA",
      [
        "storage",
        "00c8f2e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00b2ba58",
      "READ",
      [
        "storage",
        "00ca6510",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b2ba48",
      "READ",
      [
        "storage",
        "00c9b310",
        null,
        "pointer"
      ]
    ],
    [
      "00b2ba54",
      "DATA",
      [
        "storage",
        "00c8f3b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00b2ba58",
      "READ",
      [
        "storage",
        "00ca6610",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2b91c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b8f4.md#insn-00b2b91c) · [`00b2b9d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b8f4.md#insn-00b2b9d4) · [`00b2bb04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2b8f4.md#insn-00b2bb04)
- 新版 [`00b2b9b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b990.md#insn-00b2b9b8) · [`00b2ba70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b990.md#insn-00b2ba70) · [`00b2bba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2b990.md#insn-00b2bba0)

~~~diff
- 00b2b91c ["INT_ADD", "register:40f0:8", ["const:b2b91c:8", "const:4:8"]]
- 00b2b91c ["CALL", null, ["callee:0046cafc:8"]]
+ 00b2b9b8 ["INT_ADD", "register:40f0:8", ["const:b2b9b8:8", "const:4:8"]]
+ 00b2b9b8 ["CALL", null, ["callee:0046cafc:8"]]
- 00b2b91c bytes 6804e597
+ 00b2b9b8 bytes 5104e597
- 00b2b9d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2b9d4 ["INT_ADD", "register:40f0:8", ["const:b2b9d4:8", "const:4:8"]]
- 00b2b9d4 ["CALLIND", null, ["register:0:8"]]
+ 00b2ba70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2ba70 ["INT_ADD", "register:40f0:8", ["const:b2ba70:8", "const:4:8"]]
+ 00b2ba70 ["CALLIND", null, ["register:0:8"]]
- 00b2b9d4 bytes 00013fd6
+ 00b2ba70 bytes 00013fd6
- 00b2bb04 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2bb04 ["INT_ADD", "register:40f0:8", ["const:b2bb04:8", "const:4:8"]]
- 00b2bb04 ["CALLIND", null, ["register:0:8"]]
+ 00b2bba0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2bba0 ["INT_ADD", "register:40f0:8", ["const:b2bba0:8", "const:4:8"]]
+ 00b2bba0 ["CALLIND", null, ["register:0:8"]]
- 00b2bb04 bytes 00013fd6
+ 00b2bba0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-120b02db8a6d178b64f181f8034148a2"></a>

### [`00b2bc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bc5c.md) → [`00b2bcf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2bcf8.md) FUN_00b2bcf8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) · 呼出先 8件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00b2cee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2cee4.md) · 呼出先 8件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.42% / 新版 93.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2bd40",
      "incomplete_value": true,
      "site": "00b2bd40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f3e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2bca4",
      "incomplete_value": true,
      "site": "00b2bca4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f9a:8"
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
      "definition_site": "00b2bd38",
      "incomplete_value": true,
      "site": "00b2bd44",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b2bc9c",
      "incomplete_value": true,
      "site": "00b2bca8",
      "value": [
        "LOAD",
        "8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2bd30",
      "READ",
      [
        "storage",
        "002a5f9a",
        null,
        "string"
      ]
    ],
    [
      "00b2bd38",
      "READ",
      [
        "storage",
        "002a5fa1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2bd30",
      "READ",
      [
        "storage",
        "002a5f3e",
        null,
        "string"
      ]
    ],
    [
      "00b2bd38",
      "READ",
      [
        "storage",
        "002a5f45",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2bd44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bc5c.md#insn-00b2bd44) · [`00b2bc7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bc5c.md#insn-00b2bc7c) · [`00b2bc84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bc5c.md#insn-00b2bc84)
- 新版 [`00b2bde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2bcf8.md#insn-00b2bde0) · [`00b2bd18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2bcf8.md#insn-00b2bd18) · [`00b2bd20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2bcf8.md#insn-00b2bd20)

~~~diff
- 00b2bd44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2bd44 ["INT_ADD", "register:40f0:8", ["const:b2bd44:8", "const:4:8"]]
- 00b2bd44 ["CALLIND", null, ["register:0:8"]]
+ 00b2bde0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2bde0 ["INT_ADD", "register:40f0:8", ["const:b2bde0:8", "const:4:8"]]
+ 00b2bde0 ["CALLIND", null, ["register:0:8"]]
- 00b2bd44 bytes 00013fd6
+ 00b2bde0 bytes 00013fd6
- 00b2bc7c ["INT_ADD", "register:40f0:8", ["const:b2bc7c:8", "const:4:8"]]
- 00b2bc7c ["CALL", null, ["callee:00588eac:8"]]
+ 00b2bd18 ["INT_ADD", "register:40f0:8", ["const:b2bd18:8", "const:4:8"]]
+ 00b2bd18 ["CALL", null, ["callee:00588eac:8"]]
- 00b2bc7c bytes 7c74e997
+ 00b2bd18 bytes 6574e997
- 00b2bc84 ["INT_ADD", "register:40f0:8", ["const:b2bc84:8", "const:4:8"]]
- 00b2bc84 ["CALL", null, ["callee:0058919c:8"]]
+ 00b2bd20 ["INT_ADD", "register:40f0:8", ["const:b2bd20:8", "const:4:8"]]
+ 00b2bd20 ["CALL", null, ["callee:0058919c:8"]]
- 00b2bc84 bytes 3675e997
+ 00b2bd20 bytes 1f75e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b036edc3c291b3e60fda1157e935d0eb"></a>

### [`00b2bdc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bdc8.md) → [`00b2be64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2be64.md) FUN_00b2be64

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) · 呼出先 8件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00b2cee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2cee4.md) · 呼出先 8件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 94.12% / 新版 88.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2bea4",
      "incomplete_value": true,
      "site": "00b2bebc",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:eab:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2be08",
      "incomplete_value": true,
      "site": "00b2be20",
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
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:f07:8"
              ]
            ]
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
      "00b2bea4",
      "READ",
      [
        "storage",
        "002abf07",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2bea4",
      "READ",
      [
        "storage",
        "002abeab",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2bde8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bdc8.md#insn-00b2bde8) · [`00b2bdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bdc8.md#insn-00b2bdf0) · [`00b2bdfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2b/00b2bdc8.md#insn-00b2bdfc)
- 新版 [`00b2be84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2be64.md#insn-00b2be84) · [`00b2be8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2be64.md#insn-00b2be8c) · [`00b2be98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2b/00b2be64.md#insn-00b2be98)

~~~diff
- 00b2bde8 ["INT_ADD", "register:40f0:8", ["const:b2bde8:8", "const:4:8"]]
- 00b2bde8 ["CALL", null, ["callee:00588eac:8"]]
+ 00b2be84 ["INT_ADD", "register:40f0:8", ["const:b2be84:8", "const:4:8"]]
+ 00b2be84 ["CALL", null, ["callee:00588eac:8"]]
- 00b2bde8 bytes 2174e997
+ 00b2be84 bytes 0a74e997
- 00b2bdf0 ["INT_ADD", "register:40f0:8", ["const:b2bdf0:8", "const:4:8"]]
- 00b2bdf0 ["CALL", null, ["callee:0058919c:8"]]
+ 00b2be8c ["INT_ADD", "register:40f0:8", ["const:b2be8c:8", "const:4:8"]]
+ 00b2be8c ["CALL", null, ["callee:0058919c:8"]]
- 00b2bdf0 bytes db74e997
+ 00b2be8c bytes c474e997
- 00b2bdfc ["COPY", "tmp:0:8", ["const:f07:8"]]
- 00b2bdfc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b2bdfc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b2bdfc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b2be98 ["COPY", "tmp:0:8", ["const:eab:8"]]
+ 00b2be98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2be98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b2be98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b2bdfc bytes 291d3c91
+ 00b2be98 bytes 29ad3a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-988f48efc1d020bd60fc2c5cbc649b50"></a>

### [`00b2c09c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c09c.md) → [`00b2c138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c138.md) FUN_00b2c138

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) · 呼出先 8件 [`005762b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00576/005762b8.md) [`00588e6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00588/00588e6c.md) [`00589144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589144.md) [`0058915c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/0058915c.md) [`00589320`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00589/00589320.md)
- 新版 呼出元 1件 [`00b2cee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2cee4.md) · 呼出先 8件 [`005762f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00576/005762f8.md) [`00588eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00588/00588eac.md) [`00589184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589184.md) [`0058919c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/0058919c.md) [`00589360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00589/00589360.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.95% / 新版 95.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2c178",
      "incomplete_value": true,
      "site": "00b2c18c",
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
                "const:893:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c0dc",
      "incomplete_value": true,
      "site": "00b2c0f0",
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
                "const:8e7:8"
              ]
            ]
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
      "00b2c178",
      "READ",
      [
        "storage",
        "002b98e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2c178",
      "READ",
      [
        "storage",
        "002b9893",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2c18c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c09c.md#insn-00b2c18c) · [`00b2c0bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c09c.md#insn-00b2c0bc) · [`00b2c0c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c09c.md#insn-00b2c0c4)
- 新版 [`00b2c228`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c138.md#insn-00b2c228) · [`00b2c158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c138.md#insn-00b2c158) · [`00b2c160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c138.md#insn-00b2c160)

~~~diff
- 00b2c18c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2c18c ["INT_ADD", "register:40f0:8", ["const:b2c18c:8", "const:4:8"]]
- 00b2c18c ["CALLIND", null, ["register:0:8"]]
+ 00b2c228 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2c228 ["INT_ADD", "register:40f0:8", ["const:b2c228:8", "const:4:8"]]
+ 00b2c228 ["CALLIND", null, ["register:0:8"]]
- 00b2c18c bytes 00013fd6
+ 00b2c228 bytes 00013fd6
- 00b2c0bc ["INT_ADD", "register:40f0:8", ["const:b2c0bc:8", "const:4:8"]]
- 00b2c0bc ["CALL", null, ["callee:00588eac:8"]]
+ 00b2c158 ["INT_ADD", "register:40f0:8", ["const:b2c158:8", "const:4:8"]]
+ 00b2c158 ["CALL", null, ["callee:00588eac:8"]]
- 00b2c0bc bytes 6c73e997
+ 00b2c158 bytes 5573e997
- 00b2c0c4 ["INT_ADD", "register:40f0:8", ["const:b2c0c4:8", "const:4:8"]]
- 00b2c0c4 ["CALL", null, ["callee:0058919c:8"]]
+ 00b2c160 ["INT_ADD", "register:40f0:8", ["const:b2c160:8", "const:4:8"]]
+ 00b2c160 ["CALL", null, ["callee:0058919c:8"]]
- 00b2c0c4 bytes 2674e997
+ 00b2c160 bytes 0f74e997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1052539bf3c666e9f91919541cefbf44"></a>

### [`00b2c200`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md) → [`00b2c29c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c29c.md) FUN_00b2c29c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043af2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043af2c.md) · 呼出先 19件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`0046796c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/0046796c.md) [`0046d968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d968.md) [`0046db00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046db00.md) [`0048b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048b/0048b390.md)
- 新版 呼出元 1件 [`0043af6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af6c.md) · 呼出先 19件 [`004678a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004678a0.md) [`004679ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/004679ac.md) [`0046d9a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d9a8.md) [`0046db40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046db40.md) [`0048b3d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048b/0048b3d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.38% / 新版 89.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2c2e8",
      "incomplete_value": true,
      "site": "00b2c2e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c24c",
      "incomplete_value": true,
      "site": "00b2c24c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e1d:8"
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
      "definition_site": "00b2c350",
      "incomplete_value": true,
      "site": "00b2c354",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:188:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c2b4",
      "incomplete_value": true,
      "site": "00b2c2b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c4000:8"
              ],
              [
                "leaf",
                "const:148:8"
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
      "definition_site": "00b2c3ac",
      "incomplete_value": true,
      "site": "00b2c3ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c310",
      "incomplete_value": true,
      "site": "00b2c310",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5dc:8"
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
      "00b2c2d4",
      "READ",
      [
        "storage",
        "002b8e1d",
        null,
        "string"
      ]
    ],
    [
      "00b2c350",
      "READ",
      [
        "storage",
        "002c4148",
        null,
        "undefined8"
      ]
    ],
    [
      "00b2c388",
      "READ",
      [
        "storage",
        "00ca4c94",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b2c2d4",
      "READ",
      [
        "storage",
        "002b8dc9",
        null,
        "string"
      ]
    ],
    [
      "00b2c350",
      "READ",
      [
        "storage",
        "002c4188",
        null,
        "undefined8"
      ]
    ],
    [
      "00b2c388",
      "READ",
      [
        "storage",
        "00ca4d94",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2c274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md#insn-00b2c274) · [`00b2c2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md#insn-00b2c2dc) · [`00b2c2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c200.md#insn-00b2c2e8)
- 新版 [`00b2c310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c29c.md#insn-00b2c310) · [`00b2c378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c29c.md#insn-00b2c378) · [`00b2c384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c29c.md#insn-00b2c384)

~~~diff
- 00b2c274 ["INT_ADD", "register:40f0:8", ["const:b2c274:8", "const:4:8"]]
- 00b2c274 ["CALL", null, ["callee:00c58480:8"]]
+ 00b2c310 ["INT_ADD", "register:40f0:8", ["const:b2c310:8", "const:4:8"]]
+ 00b2c310 ["CALL", null, ["callee:00c58480:8"]]
- 00b2c274 bytes 4fb00494
+ 00b2c310 bytes 5cb00494
- 00b2c2dc ["INT_ADD", "register:40f0:8", ["const:b2c2dc:8", "const:4:8"]]
- 00b2c2dc ["CALL", null, ["callee:0055f500:8"]]
+ 00b2c378 ["INT_ADD", "register:40f0:8", ["const:b2c378:8", "const:4:8"]]
+ 00b2c378 ["CALL", null, ["callee:0055f500:8"]]
- 00b2c2dc bytes 79cce897
+ 00b2c378 bytes 62cce897
- 00b2c2e8 ["COPY", "tmp:0:8", ["const:c70:8"]]
- 00b2c2e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b2c2e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b2c2e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b2c384 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00b2c384 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2c384 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2c384 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b2c2e8 bytes 08c13191
+ 00b2c384 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dec6448ccc7c2ac14e1a7e2f4056112a"></a>

### [`00b2c424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c424.md) → [`00b2c4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4c0.md) FUN_00b2c4c0

採用 · 移動量 `+0x9c` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043b658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b658.md) · 呼出先 5件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f534.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047b7cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047b/0047b7cc.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)
- 新版 呼出元 1件 [`0043b698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b698.md) · 呼出先 5件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f574.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047b80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047b/0047b80c.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00b2c4d8",
      "value": [
        "leaf",
        "ram:47ad34:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b2c43c",
      "value": [
        "leaf",
        "ram:47acf4:8"
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
      "00b2c4d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ],
  "added": [
    [
      "00b2c4d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2c43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c424.md#insn-00b2c43c) · [`00b2c42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c424.md#insn-00b2c42c) · [`00b2c438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c424.md#insn-00b2c438)
- 新版 [`00b2c4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4c0.md#insn-00b2c4d8) · [`00b2c4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4c0.md#insn-00b2c4c8) · [`00b2c4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4c0.md#insn-00b2c4d4)

~~~diff
- 00b2c43c ["INT_ADD", "register:40f0:8", ["const:b2c43c:8", "const:4:8"]]
- 00b2c43c ["CALL", null, ["ram:47acf4:8"]]
+ 00b2c4d8 ["INT_ADD", "register:40f0:8", ["const:b2c4d8:8", "const:4:8"]]
+ 00b2c4d8 ["CALL", null, ["ram:47ad34:8"]]
- 00b2c43c bytes 2e3ae597
+ 00b2c4d8 bytes 173ae597
- 00b2c42c ["INT_ADD", "register:40f0:8", ["const:b2c42c:8", "const:4:8"]]
- 00b2c42c ["CALL", null, ["callee:00851550:8"]]
+ 00b2c4c8 ["INT_ADD", "register:40f0:8", ["const:b2c4c8:8", "const:4:8"]]
+ 00b2c4c8 ["CALL", null, ["callee:00851550:8"]]
- 00b2c42c bytes 3394f497
+ 00b2c4c8 bytes 2294f497
- 00b2c438 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2c438 ["INT_ADD", "register:40f0:8", ["const:b2c438:8", "const:4:8"]]
- 00b2c438 ["CALLIND", null, ["register:0:8"]]
+ 00b2c4d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b2c4d4 ["INT_ADD", "register:40f0:8", ["const:b2c4d4:8", "const:4:8"]]
+ 00b2c4d4 ["CALLIND", null, ["register:0:8"]]
- 00b2c438 bytes 00013fd6
+ 00b2c4d4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d308af860e8474bef039c2bbe19d98e"></a>

### [`00b2c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md) → [`00b2c4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4ec.md) FUN_00b2c4ec

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0043b5bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b5bc.md) [`00b2d858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d858.md) · 呼出先 24件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00442b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442b38.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md)
- 新版 呼出元 2件 [`0043b5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b5fc.md) [`00b2d8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d8f4.md) · 呼出先 24件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00442b78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442b78.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.12% / 新版 98.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2c6e8",
      "incomplete_value": false,
      "site": "00b2c6e8",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c64c",
      "incomplete_value": false,
      "site": "00b2c64c",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2c7c4",
      "incomplete_value": true,
      "site": "00b2c7d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c728",
      "incomplete_value": true,
      "site": "00b2c734",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:454:8"
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2caf8",
      "incomplete_value": true,
      "site": "00b2cb08",
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
                "const:f4e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2ca5c",
      "incomplete_value": true,
      "site": "00b2ca6c",
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
                "const:faa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 75,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2c6e8",
      "DATA",
      [
        "storage",
        "00c8f368",
        null,
        "undefined *"
      ]
    ],
    [
      "00b2c7c4",
      "READ",
      [
        "storage",
        "002b0454",
        null,
        "string"
      ]
    ],
    [
      "00b2c860",
      "READ",
      [
        "storage",
        "00c8f390",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2c6e8",
      "DATA",
      [
        "storage",
        "00c8f438",
        null,
        "undefined *"
      ]
    ],
    [
      "00b2c7c4",
      "READ",
      [
        "storage",
        "002b03f8",
        null,
        "string"
      ]
    ],
    [
      "00b2c860",
      "READ",
      [
        "storage",
        "00c8f460",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2caf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md#insn-00b2caf4) · [`00b2cb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md#insn-00b2cb0c) · [`00b2cba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md#insn-00b2cba8)
- 新版 [`00b2cb90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4ec.md#insn-00b2cb90) · [`00b2cba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4ec.md#insn-00b2cba8) · [`00b2cc44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4ec.md#insn-00b2cc44)

~~~diff
- 00b2caf4 ["INT_ADD", "register:40f0:8", ["const:b2caf4:8", "const:4:8"]]
- 00b2caf4 ["CALL", null, ["ram:48ccf8:8"]]
+ 00b2cb90 ["INT_ADD", "register:40f0:8", ["const:b2cb90:8", "const:4:8"]]
+ 00b2cb90 ["CALL", null, ["ram:48cd38:8"]]
- 00b2caf4 bytes 8180e597
+ 00b2cb90 bytes 6a80e597
- 00b2cb0c ["INT_ADD", "register:40f0:8", ["const:b2cb0c:8", "const:4:8"]]
- 00b2cb0c ["CALL", null, ["callee:00c57f80:8"]]
+ 00b2cba8 ["INT_ADD", "register:40f0:8", ["const:b2cba8:8", "const:4:8"]]
+ 00b2cba8 ["CALL", null, ["callee:00c57f80:8"]]
- 00b2cb0c bytes e9ac0494
+ 00b2cba8 bytes f6ac0494
- 00b2cba8 ["INT_ADD", "register:40f0:8", ["const:b2cba8:8", "const:4:8"]]
- 00b2cba8 ["CALL", null, ["ram:48ccf8:8"]]
+ 00b2cc44 ["INT_ADD", "register:40f0:8", ["const:b2cc44:8", "const:4:8"]]
+ 00b2cc44 ["CALL", null, ["ram:48cd38:8"]]
- 00b2cba8 bytes 5480e597
+ 00b2cc44 bytes 3d80e597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83fbf822106bb96e01da78bc79c927d5"></a>

### [`00b2ce48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md) → [`00b2cee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2cee4.md) FUN_00b2cee4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0043af2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043af2c.md) [`0043b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b2ac.md) · 呼出先 23件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f424.md) [`0043f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f42c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`0046ca54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca54.md)
- 新版 呼出元 2件 [`0043af6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043af6c.md) [`0043b2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b2ec.md) · 呼出先 23件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f464.md) [`0043f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f46c.md) [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md) [`0046ca94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca94.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2cf2c",
      "incomplete_value": true,
      "site": "00b2cf48",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:51c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2ce90",
      "incomplete_value": true,
      "site": "00b2ceac",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:4ed:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b2cff0",
      "incomplete_value": true,
      "site": "00b2cff0",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2cf54",
      "incomplete_value": true,
      "site": "00b2cf54",
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
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b2cff4",
      "incomplete_value": true,
      "site": "00b2cff4",
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
            "const:24:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2cf58",
      "incomplete_value": true,
      "site": "00b2cf58",
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
            "const:24:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2cf2c",
      "READ",
      [
        "storage",
        "002a94ed",
        null,
        "string"
      ]
    ],
    [
      "00b2cfec",
      "READ",
      [
        "storage",
        "00c9ab68",
        null,
        "pointer"
      ]
    ],
    [
      "00b2cff0",
      "WRITE",
      [
        "storage",
        "00ca4c98",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b2cf2c",
      "READ",
      [
        "storage",
        "002a951c",
        null,
        "string"
      ]
    ],
    [
      "00b2cfec",
      "READ",
      [
        "storage",
        "00c9ac38",
        null,
        "pointer"
      ]
    ],
    [
      "00b2cff0",
      "WRITE",
      [
        "storage",
        "00ca4d98",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2cff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md#insn-00b2cff0) · [`00b2d1e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md#insn-00b2d1e8) · [`00b2ce6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2ce48.md#insn-00b2ce6c)
- 新版 [`00b2d08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2cee4.md#insn-00b2d08c) · [`00b2d284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2cee4.md#insn-00b2d284) · [`00b2cf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2cee4.md#insn-00b2cf08)

~~~diff
- 00b2cff0 ["INT_ADD", "register:40f0:8", ["const:b2cff0:8", "const:4:8"]]
- 00b2cff0 ["CALL", null, ["callee:00b2bcf8:8"]]
+ 00b2d08c ["INT_ADD", "register:40f0:8", ["const:b2d08c:8", "const:4:8"]]
+ 00b2d08c ["CALL", null, ["callee:00b2bcf8:8"]]
- 00b2cff0 bytes 1bfbff97
+ 00b2d08c bytes 1bfbff97
- 00b2d1e8 ["INT_ADD", "register:40f0:8", ["const:b2d1e8:8", "const:4:8"]]
- 00b2d1e8 ["CALL", null, ["ram:48ccf8:8"]]
+ 00b2d284 ["INT_ADD", "register:40f0:8", ["const:b2d284:8", "const:4:8"]]
+ 00b2d284 ["CALL", null, ["ram:48cd38:8"]]
- 00b2d1e8 bytes c47ee597
+ 00b2d284 bytes ad7ee597
- 00b2ce6c ["INT_ADD", "register:40f0:8", ["const:b2ce6c:8", "const:4:8"]]
- 00b2ce6c ["CALL", null, ["callee:00588eac:8"]]
+ 00b2cf08 ["INT_ADD", "register:40f0:8", ["const:b2cf08:8", "const:4:8"]]
+ 00b2cf08 ["CALL", null, ["callee:00588eac:8"]]
- 00b2ce6c bytes 0070e997
+ 00b2cf08 bytes e96fe997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36a70fa4bf39f8fe86ad6a5137ec307d"></a>

### [`00b2d338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d338.md) → [`00b2d3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d3d4.md) FUN_00b2d3d4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0043b594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b594.md) · 呼出先 8件 [`0043e94c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043e/0043e94c.md) [`0043f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f42c.md) [`0043f438`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043f/0043f438.md) [`004440e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00444/004440e0.md) [`004466f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00446/004466f8.md)
- 新版 呼出元 1件 [`0043b5d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b5d4.md) · 呼出先 8件 [`0043e98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043e/0043e98c.md) [`0043f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f46c.md) [`0043f478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043f/0043f478.md) [`00444120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00444/00444120.md) [`00446738`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00446/00446738.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 44.44% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b2d340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d338.md#insn-00b2d340) · [`00b2d348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d338.md#insn-00b2d348) · [`00b2d34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d338.md#insn-00b2d34c)
- 新版 [`00b2d3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d3d4.md#insn-00b2d3dc) · [`00b2d3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d3d4.md#insn-00b2d3e4) · [`00b2d3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d3d4.md#insn-00b2d3e8)

~~~diff
- 00b2d340 ["INT_RIGHT", "tmp:0:4", ["register:4008:4", "const:0:4"]]
- 00b2d340 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b2d340 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b2d340 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b2d3dc ["INT_RIGHT", "tmp:0:4", ["register:4008:4", "const:0:4"]]
+ 00b2d3dc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b2d3dc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b2d3dc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b2d340 bytes e1020036
+ 00b2d3dc bytes e1020036
- 00b2d348 ["INT_ADD", "register:40f0:8", ["const:b2d348:8", "const:4:8"]]
- 00b2d348 ["CALL", null, ["callee:0066d11c:8"]]
+ 00b2d3e4 ["INT_ADD", "register:40f0:8", ["const:b2d3e4:8", "const:4:8"]]
+ 00b2d3e4 ["CALL", null, ["callee:0066d11c:8"]]
- 00b2d348 bytes 65ffec97
+ 00b2d3e4 bytes 4effec97
- 00b2d34c ["INT_ADD", "register:40f0:8", ["const:b2d34c:8", "const:4:8"]]
- 00b2d34c ["CALL", null, ["callee:00851550:8"]]
+ 00b2d3e8 ["INT_ADD", "register:40f0:8", ["const:b2d3e8:8", "const:4:8"]]
+ 00b2d3e8 ["CALL", null, ["callee:00851550:8"]]
- 00b2d34c bytes 6b90f497
+ 00b2d3e8 bytes 5a90f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f2fa7d5a4d373da828ac55560418b19"></a>

### [`00b2d45c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d45c.md) → [`00b2d4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d4f8.md) FUN_00b2d4f8

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

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
      "definition_site": "00b2d50c",
      "incomplete_value": false,
      "site": "00b2d510",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2d470",
      "incomplete_value": false,
      "site": "00b2d474",
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
            "const:2e8:8"
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
      "00b2d510",
      "DATA",
      [
        "storage",
        "00c8f2e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2d510",
      "DATA",
      [
        "storage",
        "00c8f3b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d45c.md#insn-00b2d468) · [`00b2d470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d45c.md#insn-00b2d470)
- 新版 [`00b2d504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d4f8.md#insn-00b2d504) · [`00b2d50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d4f8.md#insn-00b2d50c)

~~~diff
- 00b2d468 ["INT_ADD", "register:40f0:8", ["const:b2d468:8", "const:4:8"]]
- 00b2d468 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b2d504 ["INT_ADD", "register:40f0:8", ["const:b2d504:8", "const:4:8"]]
+ 00b2d504 ["CALL", null, ["callee:00c57f60:8"]]
- 00b2d468 bytes 8aaa0494
+ 00b2d504 bytes 97aa0494
- 00b2d470 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 00b2d470 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b2d470 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b2d470 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b2d50c ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 00b2d50c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2d50c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2d50c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b2d470 bytes 08a10b91
+ 00b2d50c bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b90e9409fbeb653ab0cc4c014796438"></a>

### [`00b2d480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d480.md) → [`00b2d51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d51c.md) FUN_00b2d51c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00b2d520",
      "incomplete_value": false,
      "site": "00b2d524",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2d484",
      "incomplete_value": false,
      "site": "00b2d488",
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
            "const:2e8:8"
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
      "00b2d524",
      "DATA",
      [
        "storage",
        "00c8f2e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2d524",
      "DATA",
      [
        "storage",
        "00c8f3b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d480.md#insn-00b2d484)
- 新版 [`00b2d520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d51c.md#insn-00b2d520)

~~~diff
- 00b2d484 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 00b2d484 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b2d484 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b2d484 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b2d520 ["COPY", "tmp:0:8", ["const:3b8:8"]]
+ 00b2d520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2d520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b2d520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b2d484 bytes 08a10b91
+ 00b2d520 bytes 08e10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4514fc1757dd3e7b035614c114e80cb"></a>

### [`00b2d4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d4dc.md) → [`00b2d578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d578.md) FUN_00b2d578

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b2c450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2c/00b2c450.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00b2d6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d6e0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00b2c4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2c/00b2c4ec.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00b2d77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d77c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 97.64% / 新版 97.64%

CFGの説明率　旧版 77.27% / 新版 75.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d6a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b2d73c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b2d6a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b2d6a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2d748"
      ]
    ],
    [
      "unmatched:00b2d64c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b2d740",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b2d748"
      ]
    ],
    [
      "00b2d6e8",
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

- 旧版 [`00b2d5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d4dc.md#insn-00b2d5b0) · [`00b2d64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d4dc.md#insn-00b2d64c) · [`00b2d6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d4dc.md#insn-00b2d6a0)
- 新版 [`00b2d64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d578.md#insn-00b2d64c)

~~~diff
- 00b2d5b0 ["BRANCH", null, ["local:b25:8"]]
+ 00b2d64c ["BRANCH", null, ["local:b26:8"]]
- 00b2d5b0 bytes 37000014
+ 00b2d64c bytes 37000014
- 00b2d64c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b2d64c ["INT_ADD", "register:40f0:8", ["const:b2d64c:8", "const:4:8"]]
- 00b2d64c ["CALLIND", null, ["register:0:8"]]
- 00b2d64c bytes 00013fd6
- 00b2d6a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00b2d6a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b2d6a0 bytes 680a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f417eef43a25d91a38e4b94b2c640609"></a>

### [`00b2d6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d6e0.md) → [`00b2d77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d77c.md) FUN_00b2d77c

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2d4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d4dc.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`00b2d578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d578.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "00b2d788",
      "incomplete_value": false,
      "site": "00b2d78c",
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
            "const:f8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2d6ec",
      "incomplete_value": false,
      "site": "00b2d6f0",
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
      "00b2d788",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2d788",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d6e0.md#insn-00b2d6f0) · [`00b2d6ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d6e0.md#insn-00b2d6ec)
- 新版 [`00b2d78c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d77c.md#insn-00b2d78c) · [`00b2d788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d77c.md#insn-00b2d788)

~~~diff
- 00b2d6f0 ["INT_ADD", "register:40f0:8", ["const:b2d6f0:8", "const:4:8"]]
- 00b2d6f0 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00b2d78c ["INT_ADD", "register:40f0:8", ["const:b2d78c:8", "const:4:8"]]
+ 00b2d78c ["CALL", null, ["callee:0043b7b8:8"]]
- 00b2d6f0 bytes 2238e497
+ 00b2d78c bytes 0b38e497
- 00b2d6ec ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 00b2d6ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b2d6ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b2d6ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b2d788 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 00b2d788 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2d788 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b2d788 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b2d6ec bytes 00303d91
+ 00b2d788 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af1cf22027fcb4c11d019ff4aa6bc353"></a>

### [`00b2d754`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d754.md) → [`00b2d7f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d7f0.md) FUN_00b2d7f0

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2d820",
      "incomplete_value": false,
      "site": "00b2d820",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2d784",
      "incomplete_value": false,
      "site": "00b2d784",
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
            "const:368:8"
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
      "00b2d820",
      "DATA",
      [
        "storage",
        "00c8f368",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b2d820",
      "DATA",
      [
        "storage",
        "00c8f438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2d768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d754.md#insn-00b2d768) · [`00b2d778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d754.md#insn-00b2d778) · [`00b2d7a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b2d/00b2d754.md#insn-00b2d7a8)
- 新版 [`00b2d804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d7f0.md#insn-00b2d804) · [`00b2d814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d7f0.md#insn-00b2d814) · [`00b2d844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2d/00b2d7f0.md#insn-00b2d844)

~~~diff
- 00b2d768 ["INT_ADD", "register:40f0:8", ["const:b2d768:8", "const:4:8"]]
- 00b2d768 ["CALL", null, ["callee:00c57f60:8"]]
+ 00b2d804 ["INT_ADD", "register:40f0:8", ["const:b2d804:8", "const:4:8"]]
+ 00b2d804 ["CALL", null, ["callee:00c57f60:8"]]
- 00b2d768 bytes caa90494
+ 00b2d804 bytes d7a90494
- 00b2d778 ["COPY", "tmp:0:8", ["const:368:8"]]
- 00b2d778 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00b2d778 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00b2d778 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00b2d814 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00b2d814 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00b2d814 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00b2d814 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00b2d778 bytes 6ba10d91
+ 00b2d814 bytes 6be11091
- 00b2d7a8 ["INT_ADD", "register:40f0:8", ["const:b2d7a8:8", "const:4:8"]]
- 00b2d7a8 ["CALL", null, ["callee:0043bb60:8"]]
+ 00b2d844 ["INT_ADD", "register:40f0:8", ["const:b2d844:8", "const:4:8"]]
+ 00b2d844 ["CALL", null, ["callee:0043bb60:8"]]
- 00b2d7a8 bytes de38e497
+ 00b2d844 bytes c738e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

