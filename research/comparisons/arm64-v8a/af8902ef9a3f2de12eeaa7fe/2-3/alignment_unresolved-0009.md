# v16.0.0 → v16.0.1 · 命令位置の検査未完了 (9)

[一覧の目次](README.md)

<a id="compare-ae1718fafaae86665d5c9e5638fbba0d"></a>

### [`00b642cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b642cc.md) → [`00b646f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b646f4.md) _ZNK8firebase7Variant14assert_is_blobEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b190.md) · 呼出先 2件 [`00c5a8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a8a0.md) [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 1件 [`00c5b590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b590.md) · 呼出先 2件 [`00c5aca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aca0.md) [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 52.17% / 新版 52.17%

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
      "site": "00b64300"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b64728"
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
      "unmatched:00b642fc",
      "PARAM",
      [
        "storage",
        "002bbe08",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b64300",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aca0"
      ]
    ],
    [
      "unmatched:00b6430c",
      "READ",
      [
        "storage",
        "00c9b3f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b64724",
      "PARAM",
      [
        "storage",
        "002bbe48",
        null,
        "string"
      ]
    ],
    [
      "00b64728",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5aca0"
      ]
    ],
    [
      "00b64734",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b642cc.md#insn-00b64300) · [`00b642e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b642cc.md#insn-00b642e4)
- 新版 `00b64728`（命令位置の公開資料なし） · `00b6470c`（命令位置の公開資料なし）

~~~diff
- 00b64300 ["INT_ADD", "register:40f0:8", ["const:b64300:8", "const:4:8"]]
- 00b64300 ["CALL", null, ["callee:00c5aca0:8"]]
- 00b64300 bytes 68d90394
+ 00b64728 ["INT_ADD", "register:40f0:8", ["const:b64728:8", "const:4:8"]]
+ 00b64728 ["CALL", null, ["callee:00c5aca0:8"]]
+ 00b64728 bytes 5ed90394
- 00b642e4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b642e4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b6470c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b6470c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b642e4 bytes 81000054
+ 00b6470c bytes 81000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40e8e09a87337b5b116cf66f9ec8a026"></a>

### [`00b64564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64564.md) → [`00b6498c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b64/00b6498c.md) _ZNK8firebase7Variant7AsInt64Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5a6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a6f0.md) · 呼出先 3件 [`00c58190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58190.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md)
- 新版 呼出元 1件 [`00c5aaf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aaf0.md) · 呼出先 3件 [`00c58590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58590.md) [`00c5a830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a830.md) [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b649b8",
      "DATA",
      [
        "storage",
        "0030bc22",
        "switchD_00b6459c::switchdataD_0030bc22",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b649b8",
      "DATA",
      [
        "storage",
        "0030bc62",
        "switchD_00b649c4::switchdataD_0030bc62",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b64588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64564.md#insn-00b64588) · [`00b6458c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64564.md#insn-00b6458c) · [`00b645d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64564.md#insn-00b645d0)
- 新版 `00b649b0`（命令位置の公開資料なし） · `00b649f8`（命令位置の公開資料なし）

~~~diff
- 00b64588 ["COPY", "tmp:0:8", ["const:c22:8"]]
- 00b64588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b64588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b64588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b649b0 ["COPY", "tmp:0:8", ["const:c62:8"]]
+ 00b649b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b649b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b649b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b64588 bytes 08893091
+ 00b649b0 bytes 08893191
- 00b6458c ["COPY", "register:4058:8", ["const:b645a0:8"]]
- 00b6458c bytes ab000010
- 00b645d0 ["INT_ADD", "register:40f0:8", ["const:b645d0:8", "const:4:8"]]
- 00b645d0 ["CALL", null, ["callee:00c5a8f0:8"]]
+ 00b649f8 ["INT_ADD", "register:40f0:8", ["const:b649f8:8", "const:4:8"]]
+ 00b649f8 ["CALL", null, ["callee:00c5a8f0:8"]]
- 00b645d0 bytes c8d70394
+ 00b649f8 bytes bed70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-646889acc531954ba08a6a7a807832d1"></a>

### [`00b64f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64f50.md) → [`00b65378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65378.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE15__emp

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ba10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba10.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4f0.md) [`00c5b1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1a0.md) [`00c5b1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b1e0.md)
- 新版 呼出元 1件 [`00c5be10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be10.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8f0.md) [`00c5b5a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5a0.md) [`00c5b5e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b5e0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 82.35% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65018"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65440"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b65018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64f50.md#insn-00b65018) · [`00b64f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b64/00b64f50.md#insn-00b64f6c)
- 新版 `00b65440`（命令位置の公開資料なし） · `00b65394`（命令位置の公開資料なし）

~~~diff
- 00b65018 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00b65018 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b65018 bytes 680a00f9
+ 00b65440 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
+ 00b65440 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b65440 bytes 680a00f9
- 00b64f6c ["INT_ADD", "register:40f0:8", ["const:b64f6c:8", "const:4:8"]]
- 00b64f6c ["CALL", null, ["callee:00c57e90:8"]]
+ 00b65394 ["INT_ADD", "register:40f0:8", ["const:b65394:8", "const:4:8"]]
+ 00b65394 ["CALL", null, ["callee:00c57e90:8"]]
- 00b64f6c bytes c9ca0394
+ 00b65394 bytes bfca0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b19e3c66de95fc0faf57148359e2952"></a>

### [`00b65270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65270.md) → [`00b65698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65698.md) _ZN8firebase3app8GetClassEv

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
      "site": "00b65278"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b656a0"
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
      "unmatched:00b65274",
      "READ",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6569c",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65270.md#insn-00b65278) · [`00b65270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65270.md#insn-00b65270)
- 新版 `00b656a0`（命令位置の公開資料なし）

~~~diff
- 00b65278 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b65278 ["RETURN", null, ["register:0:8"]]
- 00b65278 bytes c0035fd6
+ 00b656a0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b656a0 ["RETURN", null, ["register:0:8"]]
+ 00b656a0 bytes c0035fd6
- 00b65270 ["COPY", "register:4040:8", ["const:1125000:8"]]
- 00b65270 bytes 082e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-537d13d7d3570272a7c2c9fb640f5d51"></a>

### [`00b6527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6527c.md) → [`00b656a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b656a4.md) _ZN8firebase3app15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 20.00% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b652d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b656fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b652bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b656b8",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b652b0",
      "READ",
      [
        "storage",
        "01125c50",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b652d4",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b656b8",
      "READ",
      [
        "storage",
        "01126058",
        null,
        "undefined1"
      ]
    ],
    [
      "00b656d8",
      "READ",
      [
        "storage",
        "01126050",
        null,
        "undefined8"
      ]
    ],
    [
      "00b656fc",
      "WRITE",
      [
        "storage",
        "01126058",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b652bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6527c.md#insn-00b652bc) · [`00b652d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b6527c.md#insn-00b652d4)
- 新版 `00b656e4`（命令位置の公開資料なし）

~~~diff
- 00b652bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b652bc ["INT_ADD", "register:40f0:8", ["const:b652bc:8", "const:4:8"]]
- 00b652bc ["CALLIND", null, ["register:0:8"]]
- 00b652bc bytes 00013fd6
- 00b652d4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b652d4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c58:8"]]
- 00b652d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b652d4 bytes a0623139
+ 00b656e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b656e4 ["INT_ADD", "register:40f0:8", ["const:b656e4:8", "const:4:8"]]
+ 00b656e4 ["CALLIND", null, ["register:0:8"]]
+ 00b656e4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aca51b0b3567a6bd0f937d93b811066"></a>

### [`00b652e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b652e8.md) → [`00b65710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65710.md) _ZN8firebase3app12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af60.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 14.29% / 新版 14.29%

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
      "site": "00b652e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b652ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b652ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b652e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b652ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b652f0",
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
      "00b65710",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b65714",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b65718",
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

- 旧版 [`00b652e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b652e8.md#insn-00b652e8) · [`00b652ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b652e8.md#insn-00b652ec) · [`00b652f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b652e8.md#insn-00b652f0)

~~~diff
- 00b652e8 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b652e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b652e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b652e8 bytes f50f1df8
- 00b652ec ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b652ec ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b652ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b652ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b652ec bytes f44f01a9
- 00b652f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b652f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b652f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b652f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b652f0 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f52db86b182584ebe240be6f9181778b"></a>

### [`00b65474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65474.md) → [`00b6589c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b6589c.md) _ZN8firebase3app10GetFieldIdENS0_5FieldE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b000.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

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
      "site": "00b65494"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b658bc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b654ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b658b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65498"
      ]
    ],
    [
      "unmatched:00b65490",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b65494",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5b000"
      ]
    ]
  ],
  "added": [
    [
      "00b658b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b658c0"
      ]
    ],
    [
      "00b658b8",
      "PARAM",
      [
        "storage",
        "002a951e",
        null,
        "string"
      ]
    ],
    [
      "00b658bc",
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

- 旧版 [`00b65494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65474.md#insn-00b65494) · [`00b654ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b65474.md#insn-00b654ac)
- 新版 `00b658bc`（命令位置の公開資料なし）

~~~diff
- 00b65494 ["INT_ADD", "register:40f0:8", ["const:b65494:8", "const:4:8"]]
- 00b65494 ["CALL", null, ["callee:00c5b000:8"]]
- 00b65494 bytes dbd50394
- 00b654ac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b654ac ["RETURN", null, ["register:0:8"]]
- 00b654ac bytes c0035fd6
+ 00b658bc ["INT_ADD", "register:40f0:8", ["const:b658bc:8", "const:4:8"]]
+ 00b658bc ["CALL", null, ["callee:00c5b000:8"]]
+ 00b658bc bytes d1d50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51ccece69919934104c4d233d70a3404"></a>

### [`00b654b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b654b0.md) → [`00b658d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b658d8.md) _ZN8firebase15options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEN

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.25% / 新版 31.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b654dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65904"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b654c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b658e8",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b654c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b654e0"
      ]
    ],
    [
      "unmatched:00b654d0",
      "PARAM",
      [
        "storage",
        "002a2989",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b658e8",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b658ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65908"
      ]
    ],
    [
      "00b658f8",
      "PARAM",
      [
        "storage",
        "002a2a56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b654c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b654b0.md#insn-00b654c4) · [`00b654d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b654b0.md#insn-00b654d4) · [`00b654dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b654b0.md#insn-00b654dc)

~~~diff
- 00b654c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b654c4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b654c4 bytes e80000b5
- 00b654d4 ["INT_ADD", "register:40f0:8", ["const:b654d4:8", "const:4:8"]]
- 00b654d4 ["CALL", null, ["callee:00c5af10:8"]]
- 00b654d4 bytes 8fd50394
- 00b654dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb0:8"]]
- 00b654dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b654dc bytes 605a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0498eb5bcb5d3c993df62108ab5b68e4"></a>

### [`00b654f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b654f0.md) → [`00b65918`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b65/00b65918.md) _ZN8firebase15options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5af10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5af10.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.25% / 新版 31.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6551c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65944"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65504"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65928",
      "READ",
      [
        "storage",
        "01125cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65504",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65520"
      ]
    ],
    [
      "unmatched:00b6550c",
      "PARAM",
      [
        "storage",
        "002a2989",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65928",
      "READ",
      [
        "storage",
        "011260b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6592c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65948"
      ]
    ],
    [
      "00b65934",
      "PARAM",
      [
        "storage",
        "002a2a56",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b654f0.md#insn-00b65504) · [`00b65514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b654f0.md#insn-00b65514) · [`00b6551c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b65/00b654f0.md#insn-00b6551c)

~~~diff
- 00b65504 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b65504 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b65504 bytes e80000b5
- 00b65514 ["INT_ADD", "register:40f0:8", ["const:b65514:8", "const:4:8"]]
- 00b65514 ["CALL", null, ["callee:00c5af10:8"]]
- 00b65514 bytes 7fd50394
- 00b6551c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb0:8"]]
- 00b6551c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6551c bytes 605a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b9b72308379623f303463f848814c27"></a>

### [`00b67e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e68.md) → [`00b68290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b68/00b68290.md) _ZNK8firebase10AppOptionseqERKS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bae0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5bee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bee0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 73.53% / 新版 73.53%

CFGの説明率　旧版 40.21% / 新版 39.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 32件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67f74"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67f98"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b67fa8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b683a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b67fb0"
      ]
    ],
    [
      "unmatched:00b67f98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b687b4"
      ]
    ],
    [
      "unmatched:00b67fa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b67f8c"
      ]
    ]
  ],
  "added": [
    [
      "00b683a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b683d8"
      ]
    ],
    [
      "00b683c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b687b4"
      ]
    ],
    [
      "00b683d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b683b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b67f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e68.md#insn-00b67f14) · [`00b67f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e68.md#insn-00b67f74) · [`00b67f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b67/00b67e68.md#insn-00b67f98)
- 新版 `00b6833c`（命令位置の公開資料なし）

~~~diff
- 00b67f14 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:4", "const:0:4"]]
- 00b67f14 ["CBRANCH", null, ["local:b106:8", "tmp:0:1"]]
+ 00b6833c ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:4", "const:0:4"]]
+ 00b6833c ["CBRANCH", null, ["local:b109:8", "tmp:0:1"]]
- 00b67f14 bytes c0230035
+ 00b6833c bytes c0230035
- 00b67f74 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b67f74 ["COPY", "tmp:1:8", ["register:4068:8"]]
- 00b67f74 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b67f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:1:8"]]
- 00b67f74 bytes a015899a
- 00b67f98 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b67f98 ["CBRANCH", null, ["local:b106:8", "tmp:0:1"]]
- 00b67f98 bytes a11f0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dcf37a0f56715177476acff60278c8b"></a>

### [`00b6a414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a414.md) → [`00b6a83c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6a/00b6a83c.md) _ZN11flatbuffers6ParserD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b510.md) · 呼出先 13件 [`00540890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540890.md) [`0073a2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073a/0073a2c4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4a0.md) [`00c5b4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4b0.md)
- 新版 呼出元 1件 [`00c5b910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b910.md) · 呼出先 13件 [`005408d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005408d0.md) [`0073a304`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073a/0073a304.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8a0.md) [`00c5b8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.26% / 新版 95.26%

CFGの説明率　旧版 87.50% / 新版 91.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a414"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6a418"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6a414",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6a418",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6a41c",
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
      "00b6a83c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b6a840",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6a844",
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

- 旧版 [`00b6a414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a414.md#insn-00b6a414) · [`00b6a418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a414.md#insn-00b6a418) · [`00b6a41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a414.md#insn-00b6a41c)

~~~diff
- 00b6a414 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b6a414 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b6a414 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6a414 bytes f70f1cf8
- 00b6a418 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b6a418 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b6a418 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6a418 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6a418 bytes f65701a9
- 00b6a41c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6a41c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6a41c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6a41c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6a41c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21b906f7db71b2ba286d89fce9ba450b"></a>

### [`00b6ae80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6ae80.md) → [`00b6b2a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b2a8.md) _ZNSt6__ndk16vectorIPN11flatbuffers9NamespaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6e0.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5bae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bae0.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 52.94% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6aed4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6aed8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6b2fc"
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
      "unmatched:00b6aed8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b388"
      ]
    ]
  ],
  "added": [
    [
      "00b6b300",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b388"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6aed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6ae80.md#insn-00b6aed4) · [`00b6aed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6ae80.md#insn-00b6aed8)
- 新版 `00b6b2fc`（命令位置の公開資料なし）

~~~diff
- 00b6aed4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6aed4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b6aed4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b6aed4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b6aed4 bytes 1931899a
- 00b6aed8 ["INT_EQUAL", "tmp:0:1", ["register:40c8:8", "const:0:8"]]
- 00b6aed8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b6aed8 bytes 590400b4
+ 00b6b2fc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b6b2fc ["COPY", "tmp:1:8", ["register:4040:8"]]
+ 00b6b2fc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b6b2fc ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00b6b2fc bytes 1931899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f582319d07145c8602fdf374a8a789b3"></a>

### [`00b6af68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6af68.md) → [`00b6b390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b390.md) _ZNK8firebase3fbs14GoogleServices6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b590.md) · 呼出先 2件 [`00c5b580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b580.md) [`00c5b5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5e0.md)
- 新版 呼出元 1件 [`00c5b990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b990.md) · 呼出先 2件 [`00c5b980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b980.md) [`00c5b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 92.03% / 新版 92.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b2e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6b710"
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
      "unmatched:00b6b2e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b720"
      ]
    ]
  ],
  "added": [
    [
      "00b6b710",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b720"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6af68.md#insn-00b6b2e8) · [`00b6af98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6af68.md#insn-00b6af98)
- 新版 `00b6b710`（命令位置の公開資料なし） · `00b6b3c0`（命令位置の公開資料なし）

~~~diff
- 00b6b2e8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6b2e8 ["CBRANCH", null, ["local:b72:8", "tmp:0:1"]]
- 00b6b2e8 bytes 83000054
+ 00b6b710 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b6b710 ["CBRANCH", null, ["local:b71:8", "tmp:0:1"]]
+ 00b6b710 bytes 83000054
- 00b6af98 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b6af98 ["CBRANCH", null, ["local:b71:8", "tmp:0:1"]]
+ 00b6b3c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b6b3c0 ["CBRANCH", null, ["local:b70:8", "tmp:0:1"]]
- 00b6af98 bytes e81a0035
+ 00b6b3c0 bytes e81a0035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac627631b953532598e52eb802813930"></a>

### [`00b6b320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6b320.md) → [`00b6b748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6b/00b6b748.md) _ZNK8firebase3fbs11ProjectInfo6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b580.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5b980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b980.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 51.82% / 新版 51.82%

CFGの説明率　旧版 26.94% / 新版 26.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 42件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b3f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b3fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b408"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6b810",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6b404"
      ]
    ],
    [
      "unmatched:00b6b3f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bb88"
      ]
    ],
    [
      "unmatched:00b6b3fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6b40c"
      ]
    ]
  ],
  "added": [
    [
      "00b6b810",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b82c"
      ]
    ],
    [
      "00b6b81c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bb88"
      ]
    ],
    [
      "00b6b824",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6b834"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6b320.md#insn-00b6b3f4) · [`00b6b3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6b320.md#insn-00b6b3fc) · [`00b6b408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6b320.md#insn-00b6b408)

~~~diff
- 00b6b3f4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4088:4", "const:0:4"]]
- 00b6b3f4 ["CBRANCH", null, ["local:b104:8", "tmp:0:1"]]
- 00b6b3f4 bytes 711b0035
- 00b6b3fc ["CBRANCH", null, ["local:b21:8", "register:102:1"]]
- 00b6b3fc bytes 82000054
- 00b6b408 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6b408 ["CBRANCH", null, ["local:b102:8", "tmp:0:1"]]
- 00b6b408 bytes 431a0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96d4f7042c3aea87a1284a9691d44430"></a>

### [`00b6bfdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6bfdc.md) → [`00b6c404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c404.md) _ZNK8firebase3fbs11OAuthClient6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b570.md) · 呼出先 1件 [`00c5b560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b560.md)
- 新版 呼出元 1件 [`00c5b970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b970.md) · 呼出先 1件 [`00c5b960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b960.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 70.64% / 新版 70.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c0c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c0c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6bff8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c42c"
      ]
    ],
    [
      "unmatched:00b6c0c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c674"
      ]
    ],
    [
      "unmatched:00b6c0c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c500"
      ]
    ]
  ],
  "added": [
    [
      "00b6c420",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c42c"
      ]
    ],
    [
      "00b6c4e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c674"
      ]
    ],
    [
      "00b6c4f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c500"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6bff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6bfdc.md#insn-00b6bff8) · [`00b6c0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6bfdc.md#insn-00b6c0c0) · [`00b6c0c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6b/00b6bfdc.md#insn-00b6c0c8)

~~~diff
- 00b6bff8 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b6bff8 bytes 60000054
- 00b6c0c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4088:4", "const:0:4"]]
- 00b6c0c0 ["CBRANCH", null, ["local:b59:8", "tmp:0:1"]]
- 00b6c0c0 bytes 710c0035
- 00b6c0c8 ["CBRANCH", null, ["local:b21:8", "register:102:1"]]
- 00b6c0c8 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1070ffdcf775dc4bb1aa647e5c3ded23"></a>

### [`00b6c25c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6c25c.md) → [`00b6c684`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c684.md) _ZNK8firebase3fbs11AndroidInfo6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b560.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5b960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b960.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.53% / 新版 97.53%

CFGの説明率　旧版 80.73% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c418"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c478"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6c840"
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
      "unmatched:00b6c418",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c850"
      ]
    ],
    [
      "unmatched:00b6c478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c8b0"
      ]
    ]
  ],
  "added": [
    [
      "00b6c840",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c850"
      ]
    ],
    [
      "00b6c8a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c8b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6c25c.md#insn-00b6c418) · [`00b6c478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6c25c.md#insn-00b6c478)
- 新版 `00b6c840`（命令位置の公開資料なし）

~~~diff
- 00b6c418 ["CBRANCH", null, ["local:b42:8", "register:102:1"]]
- 00b6c418 bytes 82000054
- 00b6c478 ["CBRANCH", null, ["local:b51:8", "register:102:1"]]
- 00b6c478 bytes 82000054
+ 00b6c840 ["CBRANCH", null, ["local:b43:8", "register:102:1"]]
+ 00b6c840 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ec8c88e7b01f8d0f6912363ad51b48"></a>

### [`00b6c4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6c4e4.md) → [`00b6c90c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6c90c.md) _ZNK8firebase3fbs6ApiKey6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5b9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9d0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 64.29% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c5c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c620"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c654"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6c5c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c9f8"
      ]
    ],
    [
      "unmatched:00b6c620",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ca58"
      ]
    ],
    [
      "unmatched:00b6c654",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6caac"
      ]
    ]
  ],
  "added": [
    [
      "00b6c9e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6c9f8"
      ]
    ],
    [
      "00b6ca48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ca58"
      ]
    ],
    [
      "00b6ca7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6caac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6c4e4.md#insn-00b6c5c0) · [`00b6c620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6c4e4.md#insn-00b6c620) · [`00b6c654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6c4e4.md#insn-00b6c654)

~~~diff
- 00b6c5c0 ["CBRANCH", null, ["local:b22:8", "register:102:1"]]
- 00b6c5c0 bytes 82000054
- 00b6c620 ["CBRANCH", null, ["local:b31:8", "register:102:1"]]
- 00b6c620 bytes 82000054
- 00b6c654 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6c654 ["CBRANCH", null, ["local:b38:8", "tmp:0:1"]]
- 00b6c654 bytes 83010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b79bc5a53023d590d9d2a5745e619e34"></a>

### [`00b6c68c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6c68c.md) → [`00b6cab4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6cab4.md) _ZNK8firebase3fbs8Services6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5f0.md) · 呼出先 2件 [`00c5b540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b540.md) [`00c5b5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5a0.md)
- 新版 呼出元 1件 [`00c5b9f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9f0.md) · 呼出先 2件 [`00c5b940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b940.md) [`00c5b9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 87.05% / 新版 85.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c880"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6c900"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6cca8"
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
      "unmatched:00b6c880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ce28"
      ]
    ],
    [
      "unmatched:00b6c900",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ce28"
      ]
    ]
  ],
  "added": [
    [
      "00b6cca8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ce28"
      ]
    ],
    [
      "00b6cd28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ce28"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6c68c.md#insn-00b6c880) · [`00b6c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6c68c.md#insn-00b6c900)
- 新版 `00b6cca8`（命令位置の公開資料なし）

~~~diff
- 00b6c880 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6c880 ["CBRANCH", null, ["local:b73:8", "tmp:0:1"]]
- 00b6c880 bytes 030c0054
- 00b6c900 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b6c900 ["CBRANCH", null, ["local:b73:8", "tmp:0:1"]]
- 00b6c900 bytes 03080054
+ 00b6cca8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b6cca8 ["CBRANCH", null, ["local:b75:8", "tmp:0:1"]]
+ 00b6cca8 bytes 030c0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f8efd7ff21def2f8dc201eb94e8b501"></a>

### [`00b6ca0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6ca0c.md) → [`00b6ce34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6ce34.md) _ZNK8firebase3fbs16AnalyticsService6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5a0.md) · 呼出先 1件 [`00c5b5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5b0.md)
- 新版 呼出元 1件 [`00c5b9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9a0.md) · 呼出先 1件 [`00c5b9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 76.47% / 新版 75.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cb30"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6cf58"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cba8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6cb30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cf68"
      ]
    ]
  ],
  "added": [
    [
      "00b6cf58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cf68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6cb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6ca0c.md#insn-00b6cb30) · [`00b6cba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6ca0c.md#insn-00b6cba8)
- 新版 `00b6cf58`（命令位置の公開資料なし）

~~~diff
- 00b6cb30 ["CBRANCH", null, ["local:b29:8", "register:102:1"]]
- 00b6cb30 bytes 82000054
- 00b6cba8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6cba8 ["RETURN", null, ["register:0:8"]]
- 00b6cba8 bytes c0035fd6
+ 00b6cf58 ["CBRANCH", null, ["local:b28:8", "register:102:1"]]
+ 00b6cf58 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-279dd4a28e059a6717290a274e521476"></a>

### [`00b6cbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6cbac.md) → [`00b6cfd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6c/00b6cfd4.md) _ZNK8firebase3fbs17AnalyticsProperty6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5b0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5b9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9b0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 71.01% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cc88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6d0b0"
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
      "unmatched:00b6cc88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d0c0"
      ]
    ],
    [
      "unmatched:00b6cce8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d120"
      ]
    ]
  ],
  "added": [
    [
      "00b6d0b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d0c0"
      ]
    ],
    [
      "00b6d110",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d120"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6cc88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6cbac.md#insn-00b6cc88) · [`00b6cce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6cbac.md#insn-00b6cce8)
- 新版 `00b6d0b0`（命令位置の公開資料なし）

~~~diff
- 00b6cc88 ["CBRANCH", null, ["local:b21:8", "register:102:1"]]
- 00b6cc88 bytes 82000054
- 00b6cce8 ["CBRANCH", null, ["local:b30:8", "register:102:1"]]
- 00b6cce8 bytes 82000054
+ 00b6d0b0 ["CBRANCH", null, ["local:b21:8", "register:102:1"]]
+ 00b6d0b0 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89a7a20753c632fba4a5827cfce4a044"></a>

### [`00b6cd54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6cd54.md) → [`00b6d17c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d17c.md) _ZNK8firebase3fbs10AdsService6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b540.md) · 呼出先 1件 [`00c5b5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b5a0.md)
- 新版 呼出元 1件 [`00c5b940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b940.md) · 呼出先 1件 [`00c5b9a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b9a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 59.26% / 新版 59.26%

CFGの説明率　旧版 36.49% / 新版 36.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 31件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cdb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ce38"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ce40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6cdb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d4c8"
      ]
    ],
    [
      "unmatched:00b6ce38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d4cc"
      ]
    ],
    [
      "unmatched:00b6ce40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d278"
      ]
    ]
  ],
  "added": [
    [
      "00b6d1dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d4c8"
      ]
    ],
    [
      "00b6d260",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d4cc"
      ]
    ],
    [
      "00b6d268",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d278"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6cdb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6cd54.md#insn-00b6cdb4) · [`00b6ce38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6cd54.md#insn-00b6ce38) · [`00b6ce40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6c/00b6cd54.md#insn-00b6ce40)

~~~diff
- 00b6cdb4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6cdb4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b6cdb4 ["CBRANCH", null, ["local:b78:8", "tmp:1:1"]]
- 00b6cdb4 bytes 68170054
- 00b6ce38 ["INT_NOTEQUAL", "tmp:0:1", ["register:4088:4", "const:0:4"]]
- 00b6ce38 ["CBRANCH", null, ["local:b79:8", "tmp:0:1"]]
- 00b6ce38 bytes 71130035
- 00b6ce40 ["CBRANCH", null, ["local:b22:8", "register:102:1"]]
- 00b6ce40 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f684a6f79cf7c70c63fe531f9cf9b824"></a>

### [`00b6d0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d0b4.md) → [`00b6d4dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d4dc.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4f0.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b610.md) [`00c5ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md)
- 新版 呼出元 1件 [`00c5b8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8f0.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba10.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 85.71% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d128"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b6d550"
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
      "unmatched:00b6d128",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6d550",
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

- 旧版 [`00b6d128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d0b4.md#insn-00b6d128) · [`00b6d0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d0b4.md#insn-00b6d0d4)
- 新版 `00b6d550`（命令位置の公開資料なし） · `00b6d4fc`（命令位置の公開資料なし）

~~~diff
- 00b6d128 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d128 ["INT_ADD", "register:40f0:8", ["const:b6d128:8", "const:4:8"]]
- 00b6d128 ["CALLIND", null, ["register:0:8"]]
- 00b6d128 bytes 00013fd6
+ 00b6d550 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6d550 ["INT_ADD", "register:40f0:8", ["const:b6d550:8", "const:4:8"]]
+ 00b6d550 ["CALLIND", null, ["register:0:8"]]
+ 00b6d550 bytes 00013fd6
- 00b6d0d4 ["INT_ADD", "register:40f0:8", ["const:b6d0d4:8", "const:4:8"]]
- 00b6d0d4 ["CALL", null, ["callee:00c5ba10:8"]]
+ 00b6d4fc ["INT_ADD", "register:40f0:8", ["const:b6d4fc:8", "const:4:8"]]
+ 00b6d4fc ["CALL", null, ["callee:00c5ba10:8"]]
- 00b6d0d4 bytes 4fb90394
+ 00b6d4fc bytes 45b90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfb2bde3f6ac47cf243de9db32c51a66"></a>

### [`00b6d228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d228.md) → [`00b6d650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d650.md) _ZN11flatbuffers11SymbolTableINS_7EnumDefEED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b4c0.md) · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b470.md) [`00c5b520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b520.md) [`00c5b660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b660.md) [`00c5b670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b670.md)
- 新版 呼出元 1件 [`00c5b8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b8c0.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b870.md) [`00c5b920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b920.md) [`00c5ba60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba60.md) [`00c5ba70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.48% / 新版 84.48%

CFGの説明率　旧版 77.78% / 新版 72.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d22c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d22c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d228",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6d22c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6d230",
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
      "00b6d650",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b6d654",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6d658",
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

- 旧版 [`00b6d228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d228.md#insn-00b6d228) · [`00b6d22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d228.md#insn-00b6d22c) · [`00b6d230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d228.md#insn-00b6d230)

~~~diff
- 00b6d228 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b6d228 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b6d228 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6d228 bytes f70f1cf8
- 00b6d22c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b6d22c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b6d22c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6d22c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6d22c bytes f65701a9
- 00b6d230 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6d230 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6d230 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6d230 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6d230 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c656ba5487b3cd430080da9f2db3599b"></a>

### [`00b6d488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d488.md) → [`00b6d8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d8b0.md) _ZNSt6__ndk16__treeINS_12__value_typeImNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEENS_19__map_value_compareImS8_NS_4lessImEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6b0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 1件 [`00c5bab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bab0.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5bab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d48c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d48c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d490"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d48c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6d490",
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
      "00b6d8b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6d8b8",
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

- 旧版 [`00b6d48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d488.md#insn-00b6d48c) · [`00b6d490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d488.md#insn-00b6d490)
- 新版 `00b6d8b4`（命令位置の公開資料なし）

~~~diff
- 00b6d48c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6d48c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6d48c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6d48c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6d48c bytes f44fbea9
- 00b6d490 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6d490 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6d490 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6d490 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6d490 bytes fd7b01a9
+ 00b6d8b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b6d8b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b6d8b4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b6d8b4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b6d8b4 bytes f44fbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d6708701876d0692d940ed9d909f43d"></a>

### [`00b6d598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d598.md) → [`00b6d9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6d9c0.md) _ZN11flatbuffers10DefinitionD2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b470.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b650.md)
- 新版 呼出元 1件 [`00c5b870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b870.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 89.19% / 新版 91.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d5e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b6da0c"
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
      "unmatched:00b6d5e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6da84"
      ]
    ]
  ],
  "added": [
    [
      "00b6da0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6da84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d598.md#insn-00b6d5e4) · [`00b6d5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6d598.md#insn-00b6d5b4)
- 新版 `00b6da0c`（命令位置の公開資料なし） · `00b6d9dc`（命令位置の公開資料なし）

~~~diff
- 00b6d5e4 ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
- 00b6d5e4 bytes c0030054
+ 00b6da0c ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
+ 00b6da0c bytes c0030054
- 00b6d5b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b6d5b4 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00b6d9dc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b6d9dc ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b6d5b4 bytes c1030054
+ 00b6d9dc bytes c1030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42211c492e1db7f70e6d659ada3d5ef0"></a>

### [`00b6da68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da68.md) → [`00b6de90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6de90.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers4TypeEEENS_19__map_value_comp

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5b640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b640.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5b640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b640.md)
- 新版 呼出元 1件 [`00c5ba40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba40.md) · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5ba40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5ba40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 25.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6da6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6da6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6da70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6da6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6da70",
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
      "00b6de94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6de98",
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

- 旧版 [`00b6da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da68.md#insn-00b6da6c) · [`00b6da70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6d/00b6da68.md#insn-00b6da70)
- 新版 `00b6de94`（命令位置の公開資料なし）

~~~diff
- 00b6da6c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6da6c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6da6c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6da6c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6da6c bytes f44fbea9
- 00b6da70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6da70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6da70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6da70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6da70 bytes fd7b01a9
+ 00b6de94 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 00b6de94 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 00b6de94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b6de94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b6de94 bytes f44fbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1602394895afe2a37ed92848eb24b7b7"></a>

### [`00b70ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ad4.md) → [`00b70efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b70/00b70efc.md) _ZN11flatbuffers6ToUTF8EjPNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c3f0.md) · 呼出先 1件 [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md)
- 新版 呼出元 1件 [`00c5c7f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c7f0.md) · 呼出先 1件 [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 65.38% / 新版 65.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b70f0c"
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
      "unmatched:00b70ae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b70af8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70f30"
      ]
    ],
    [
      "unmatched:00b70b34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70f6c"
      ]
    ]
  ],
  "added": [
    [
      "00b70f0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b70f20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70f30"
      ]
    ],
    [
      "00b70f54",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70f8c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b70ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ad4.md#insn-00b70ae4) · [`00b70af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ad4.md#insn-00b70af8) · [`00b70b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ad4.md#insn-00b70b34)

~~~diff
- 00b70ae4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b70ae4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b70ae4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b70ae4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b70ae4 bytes fd7b04a9
- 00b70af8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b70af8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b70af8 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00b70af8 bytes 88000054
- 00b70b34 ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
- 00b70b34 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f502ad161254b0a15421897657c4f7c"></a>

### [`00b70ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ce0.md) → [`00b71108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71108.md) _ZNK11flatbuffers6Parser7IsIdentEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 71.43% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70d44"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b7116c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b70d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ce0.md#insn-00b70d44) · [`00b70cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b70/00b70ce0.md#insn-00b70cf4)
- 新版 `00b7116c`（命令位置の公開資料なし） · `00b7111c`（命令位置の公開資料なし）

~~~diff
- 00b70d44 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b70d44 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b70d44 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b70d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00b70d44 bytes 4015889a
+ 00b7116c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b7116c ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00b7116c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00b7116c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
+ 00b7116c bytes 4015889a
- 00b70cf4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b70cf4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b7111c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b7111c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b70cf4 bytes 61030054
+ 00b7111c bytes 61030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7066717c6da1fe997c7daaf71057ef3"></a>

### [`00b714d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b714d8.md) → [`00b71900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b71/00b71900.md) _ZNK11flatbuffers6Parser12LookupStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c6b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5cab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b714d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b714dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b714dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b714d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b714dc",
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
      "00b71900",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b71904",
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

- 旧版 [`00b714d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b714d8.md#insn-00b714d8) · [`00b714dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b71/00b714d8.md#insn-00b714dc)
- 新版 `00b71900`（命令位置の公開資料なし）

~~~diff
- 00b714d8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b714d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b714d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b714d8 bytes f30f1ef8
- 00b714dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b714dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b714dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b714dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b714dc bytes fd7b01a9
+ 00b71900 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00b71900 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00b71900 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00b71900 bytes f30f1ef8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77e634ae39491bb0b5edb3ac619778a7"></a>

### [`00b7297c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b7297c.md) → [`00b72da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b72/00b72da4.md) _ZN11flatbuffers11SymbolTableINS_8FieldDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bca0.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c0a0.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 55.56% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b729b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b72dd8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b729f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b729b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b729c8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72e80"
      ]
    ],
    [
      "unmatched:00b729f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72e38"
      ]
    ]
  ],
  "added": [
    [
      "00b72dd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b72df0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72e80"
      ]
    ],
    [
      "00b72e18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b72e38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b729b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b7297c.md#insn-00b729b0) · [`00b729f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b7297c.md#insn-00b729f0) · [`00b72b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b72/00b7297c.md#insn-00b72b0c)

~~~diff
- 00b729b0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b729b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b729b0 bytes e80700f9
- 00b729f0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b729f0 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b729f0 bytes 03010054
- 00b72b0c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b72b0c ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 00b72b0c bytes 21010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00fd7c3faafd68dbfdcc8231e86e251e"></a>

### [`00b7674c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b7674c.md) → [`00b76b74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b76/00b76b74.md) _ZN11flatbuffers11SymbolTableINS_5ValueEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc60.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c060.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.27% / 新版 97.27%

CFGの説明率　旧版 85.71% / 新版 90.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76790"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b76794"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b76bb8"
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
      "unmatched:00b7678c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76bc4"
      ]
    ]
  ],
  "added": [
    [
      "00b76bb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b76bc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7678c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b7674c.md#insn-00b7678c) · [`00b76790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b7674c.md#insn-00b76790) · [`00b76794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b76/00b7674c.md#insn-00b76794)

~~~diff
- 00b7678c ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 00b7678c bytes 82000054
- 00b76790 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b76790 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b76790 ["INT_ADD", "register:4048:8", ["register:4048:8", "const:8:8"]]
- 00b76790 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b76790 bytes 338500f8
- 00b76794 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:20:8"]]
- 00b76794 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b76794 bytes 891200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c309d669ce7d94f761482477d509b16c"></a>

### [`00b7d6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d6d4.md) → [`00b7dafc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dafc.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementIsEEvtT_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bdf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bdf0.md) · 呼出先 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c1f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1f0.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.81% / 新版 76.81%

CFGの説明率　旧版 9.38% / 新版 15.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d6d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d6d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d6d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7d6d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7d6d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7d6dc",
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
      "00b7dafc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b7db00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b7db04",
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

- 旧版 [`00b7d6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d6d4.md#insn-00b7d6d4) · [`00b7d6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d6d4.md#insn-00b7d6d8) · [`00b7d6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d6d4.md#insn-00b7d6dc)

~~~diff
- 00b7d6d4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b7d6d4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b7d6d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b7d6d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7d6d4 bytes f657bda9
- 00b7d6d8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b7d6d8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b7d6d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b7d6d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7d6d8 bytes f44f01a9
- 00b7d6dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7d6dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7d6dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b7d6dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7d6dc bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-716052c4760b1cf70e1ebab75b8ef696"></a>

### [`00b7d8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d8fc.md) → [`00b7dd24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7d/00b7dd24.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementItEEvtT_S3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5be10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be10.md) · 呼出先 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c210.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.65% / 新版 98.65%

CFGの説明率　旧版 83.33% / 新版 90.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7d920"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b7dd48"
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
      "unmatched:00b7d920",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7dd54"
      ]
    ]
  ],
  "added": [
    [
      "00b7dd48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7dd54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d8fc.md#insn-00b7d920) · [`00b7d928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d8fc.md#insn-00b7d928)
- 新版 `00b7dd48`（命令位置の公開資料なし） · `00b7dd50`（命令位置の公開資料なし）

~~~diff
- 00b7d920 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b7d920 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b7d920 bytes 61000054
+ 00b7dd48 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b7dd48 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b7dd48 bytes 61000054
- 00b7d928 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b7d928 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
+ 00b7dd50 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00b7dd50 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b7d928 bytes 68070034
+ 00b7dd50 bytes 68070034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52d29eb73d5fc077e5869f9814164442"></a>

### [`00b7de98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7de98.md) → [`00b7e2c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e2c0.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIijEET0_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5be40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be40.md) · 呼出先 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c240.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 35.29% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7df10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7df20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b7e338"
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
      "unmatched:00b7df14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e358"
      ]
    ],
    [
      "00b7e354",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7df1c"
      ]
    ],
    [
      "unmatched:00b7df40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e37c"
      ]
    ]
  ],
  "added": [
    [
      "00b7e33c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e358"
      ]
    ],
    [
      "00b7e354",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e344"
      ]
    ],
    [
      "00b7e368",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b7e37c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7df10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7de98.md#insn-00b7df10) · [`00b7df14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7de98.md#insn-00b7df14) · [`00b7df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7de98.md#insn-00b7df20)

~~~diff
- 00b7df10 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b7df10 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b7df10 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b7df10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b7df10 bytes 3f010039
- 00b7df14 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00b7df14 bytes e0000054
- 00b7df20 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b7df20 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b7df20 ["COPY", "tmp:2:8", ["register:4040:8"]]
- 00b7df20 ["COPY", "tmp:3:8", ["tmp:2:8"]]
- 00b7df20 bytes 3f692838
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-772cedc4bd551a94561053b5ad8da8c4"></a>

### [`00b7e448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e448.md) → [`00b7e870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7e/00b7e870.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIljEET0_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5be60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be60.md) · 呼出先 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md)
- 新版 呼出元 1件 [`00c5c260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c260.md) · 呼出先 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 70.59% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e4b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e4bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e4c0"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e448.md#insn-00b7e4b8) · [`00b7e4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e448.md#insn-00b7e4bc) · [`00b7e4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7e/00b7e448.md#insn-00b7e4c0)

~~~diff
- 00b7e4b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:40:8"]]
- 00b7e4b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b7e4b8 bytes 692200f9
- 00b7e4bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:30:8"]]
- 00b7e4bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b7e4bc bytes 683200b9
- 00b7e4c0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b7e4c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b7e4c0 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b7e4c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b7e4c0 bytes 3f010039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f867376f8759a9b7b31d715793ba892f"></a>

### [`00b82464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82464.md) → [`00b8288c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b8288c.md) _ZN11flatbuffers11SymbolTableINS_9StructDefEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bcb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bcb0.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c0b0.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 88.24% / 新版 90.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b824c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b828f0"
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
      "unmatched:00b824c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8291c"
      ]
    ]
  ],
  "added": [
    [
      "00b828f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8291c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b824c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82464.md#insn-00b824c8) · [`00b824b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82464.md#insn-00b824b0)
- 新版 `00b828f0`（命令位置の公開資料なし） · `00b828d8`（命令位置の公開資料なし）

~~~diff
- 00b824c8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b824c8 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b824c8 bytes 6a0100b5
+ 00b828f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00b828f0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b828f0 bytes 6a0100b5
- 00b824b0 ["BRANCH", null, ["local:b14:8"]]
+ 00b828d8 ["BRANCH", null, ["local:b13:8"]]
- 00b824b0 bytes 24000014
+ 00b828d8 bytes 24000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-401305945e0343b3611394b53300208e"></a>

### [`00b82750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82750.md) → [`00b82b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b82/00b82b78.md) _ZN11flatbuffers7EnumDef16RemoveDuplicatesEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c410.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c5b520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b520.md)
- 新版 呼出元 1件 [`00c5c810`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c810.md) · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5b920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b920.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 92.50% / 新版 90.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82844"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b82c6c"
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
      "unmatched:00b82844",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b82c58"
      ]
    ]
  ],
  "added": [
    [
      "00b82c6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b82c58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82750.md#insn-00b82844) · [`00b8276c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b82/00b82750.md#insn-00b8276c)
- 新版 `00b82c6c`（命令位置の公開資料なし） · `00b82b94`（命令位置の公開資料なし）

~~~diff
- 00b82844 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b82844 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b82844 bytes 61ffff54
+ 00b82c6c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b82c6c ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
+ 00b82c6c bytes 61ffff54
- 00b8276c ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
+ 00b82b94 ["CBRANCH", null, ["local:b26:8", "register:101:1"]]
- 00b8276c bytes 80080054
+ 00b82b94 bytes 80080054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ff9c83ee86145b603646823833643e6"></a>

### [`00b843e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b843e0.md) → [`00b84808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b84/00b84808.md) _ZN11flatbuffers11SymbolTableINS_4TypeEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc50.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c050.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 87.88% / 新版 82.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84444"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b8486c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84590"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b84444",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84898"
      ]
    ]
  ],
  "added": [
    [
      "00b8486c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b84898"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b843e0.md#insn-00b84444) · [`00b84590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b843e0.md#insn-00b84590)
- 新版 `00b8486c`（命令位置の公開資料なし）

~~~diff
- 00b84444 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00b84444 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b84444 bytes 6a0100b5
- 00b84590 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b84590 ["RETURN", null, ["register:0:8"]]
- 00b84590 bytes c0035fd6
+ 00b8486c ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00b8486c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b8486c bytes 6a0100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b578fa782fd869f74ca440fa23bb4968"></a>

### [`00b84c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84c34.md) → [`00b8505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b85/00b8505c.md) _ZN11flatbuffers6Parser15UniqueNamespaceEPNS_9NamespaceE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1d0.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5d0.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 85.81% / 新版 85.81%

CFGの説明率　旧版 55.07% / 新版 52.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84c5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b84e0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b85084"
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
      "unmatched:00b84c5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b84cb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85188"
      ]
    ],
    [
      "unmatched:00b84ce8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b850a4"
      ]
    ]
  ],
  "added": [
    [
      "00b85084",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00b850e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b85188"
      ]
    ],
    [
      "00b85110",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b850a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b84c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84c34.md#insn-00b84c5c) · [`00b84cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84c34.md#insn-00b84cb8) · [`00b84cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b84/00b84c34.md#insn-00b84cd8)

~~~diff
- 00b84c5c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00b84c5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00b84c5c bytes e10700f9
- 00b84cb8 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 00b84cb8 bytes 40050054
- 00b84cd8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b84cd8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b84cd8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b84cd8 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b84cd8 bytes 02018b9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07d894a0dbbaca74cb8622683a383a6b"></a>

### [`00b89548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89548.md) → [`00b89970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b89/00b89970.md) _ZN11flatbuffers6Parser24ParseProtoCurliesOrIdentEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5c2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c6f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6f0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 80.00% / 新版 76.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b895e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b89a08"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b895e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89548.md#insn-00b895e0) · [`00b89564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89548.md#insn-00b89564)
- 新版 `00b89a08`（命令位置の公開資料なし） · `00b8998c`（命令位置の公開資料なし）

~~~diff
- 00b895e0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b895e0 ["RETURN", null, ["register:0:8"]]
- 00b895e0 bytes c0035fd6
+ 00b89a08 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b89a08 ["RETURN", null, ["register:0:8"]]
+ 00b89a08 bytes c0035fd6
- 00b89564 ["INT_ADD", "register:40f0:8", ["const:b89564:8", "const:4:8"]]
- 00b89564 ["CALL", null, ["callee:00c5c6f0:8"]]
+ 00b8998c ["INT_ADD", "register:40f0:8", ["const:b8998c:8", "const:4:8"]]
+ 00b8998c ["CALL", null, ["callee:00c5c6f0:8"]]
- 00b89564 bytes 634b0394
+ 00b8998c bytes 594b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d0bd59be5e9b53a4fd05c276a0219f8"></a>

### [`00b8abe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8abe8.md) → [`00b8b010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8b/00b8b010.md) _ZN11flexbuffers7Builder9EndVectorEmbb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c510.md) · 呼出先 6件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5c4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c4b0.md)
- 新版 呼出元 1件 [`00c5c910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c910.md) · 呼出先 6件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5c8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c8b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.25% / 新版 94.25%

CFGの説明率　旧版 73.08% / 新版 67.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8acf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8acf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b8b118"
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
      "unmatched:00b8acc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8b164"
      ]
    ]
  ],
  "added": [
    [
      "00b8b0ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b8b164"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8acc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8abe8.md#insn-00b8acc0) · [`00b8acc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8abe8.md#insn-00b8acc4) · [`00b8acf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8abe8.md#insn-00b8acf0)

~~~diff
- 00b8acc0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b8acc0 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b8acc0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b8acc0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b8acc0 bytes 1a31899a
- 00b8acc4 ["INT_EQUAL", "tmp:0:1", ["register:40d0:8", "const:0:8"]]
- 00b8acc4 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b8acc4 bytes da0300b4
- 00b8acf0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b8acf0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b8acf0 ["COPY", "tmp:2:8", ["register:4040:8"]]
- 00b8acf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b8acf0 bytes 145500a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2adad21e55c230aa674f5e8168fd6618"></a>

### [`00b8d398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d398.md) → [`00b8d7c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8d/00b8d7c0.md) _ZN11flatbuffers6Parser16CheckPrivateLeakEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c1f0.md) · 呼出先 1件 [`00c5c2d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c2d0.md)
- 新版 呼出元 1件 [`00c5c5f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c5f0.md) · 呼出先 1件 [`00c5c6d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c6d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 92.11% / 新版 89.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8d49c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b8d8c4"
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
      "unmatched:00b8d49c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c6d0"
      ]
    ]
  ],
  "added": [
    [
      "00b8d8c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5c6d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8d49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d398.md#insn-00b8d49c) · [`00b8d3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8d/00b8d398.md#insn-00b8d3b4)
- 新版 `00b8d8c4`（命令位置の公開資料なし） · `00b8d7dc`（命令位置の公開資料なし）

~~~diff
- 00b8d49c ["INT_ADD", "register:40f0:8", ["const:b8d49c:8", "const:4:8"]]
- 00b8d49c ["CALL", null, ["callee:00c5c6d0:8"]]
- 00b8d49c bytes 8d3b0394
+ 00b8d8c4 ["INT_ADD", "register:40f0:8", ["const:b8d8c4:8", "const:4:8"]]
+ 00b8d8c4 ["CALL", null, ["callee:00c5c6d0:8"]]
+ 00b8d8c4 bytes 833b0394
- 00b8d3b4 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 00b8d3b4 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
+ 00b8d7dc ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 00b8d7dc ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00b8d3b4 bytes 09080034
+ 00b8d7dc bytes 09080034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcd014b0236a8562cc8cbc77bb6635ce"></a>

### [`00b91080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91080.md) → [`00b914a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b91/00b914a8.md) _ZNK11flatbuffers4Type9SerializeEPNS_21FlatBufferBuilderImplILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c5d0.md) · 呼出先 1件 [`00c5bb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bb50.md)
- 新版 呼出元 1件 [`00c5c9d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c9d0.md) · 呼出先 1件 [`00c5bf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bf50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 81.36% / 新版 81.36%

CFGの説明率　旧版 47.50% / 新版 55.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b910cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9111c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b91120"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b910a8",
      "DATA",
      [
        "storage",
        "0030e16a",
        "switchD_00b910b4::switchdataD_0030e16a",
        "byte"
      ]
    ],
    [
      "unmatched:00b910cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b91560"
      ]
    ],
    [
      "unmatched:00b91120",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b91560"
      ]
    ]
  ],
  "added": [
    [
      "00b914d0",
      "DATA",
      [
        "storage",
        "0030e1aa",
        "switchD_00b914dc::switchdataD_0030e1aa",
        "byte"
      ]
    ],
    [
      "00b914f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b91560"
      ]
    ],
    [
      "00b91548",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b91560"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b910cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91080.md#insn-00b910cc) · [`00b9111c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91080.md#insn-00b9111c) · [`00b91120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b91/00b91080.md#insn-00b91120)

~~~diff
- 00b910cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b910cc ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00b910cc bytes 690300b5
- 00b9111c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b9111c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b9111c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b9111c ["COPY", "register:4030:8", ["tmp:0:8"]]
- 00b9111c bytes 66018a9a
- 00b91120 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b91120 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00b91120 bytes c90000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91c991c3fec3175a22a4b8434a47940e"></a>

### [`00b9289c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b9289c.md) → [`00b92cc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b92/00b92cc4.md) _ZN11flatbuffers11SymbolTableINS_7EnumValEE3AddERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEPS1_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bc80.md) · 呼出先 9件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5c080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c080.md) · 呼出先 9件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 75.76% / 新版 69.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b92920"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b92d48"
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
      "unmatched:00b92920",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b92e20"
      ]
    ]
  ],
  "added": [
    [
      "00b92d48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b92e20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b92920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b9289c.md#insn-00b92920) · [`00b928e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b92/00b9289c.md#insn-00b928e8)
- 新版 `00b92d48`（命令位置の公開資料なし） · `00b92d10`（命令位置の公開資料なし）

~~~diff
- 00b92920 ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
- 00b92920 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00b92920 bytes db0600b4
+ 00b92d48 ["INT_EQUAL", "tmp:0:1", ["register:40d8:8", "const:0:8"]]
+ 00b92d48 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
+ 00b92d48 bytes db0600b4
- 00b928e8 ["BRANCH", null, ["local:b13:8"]]
+ 00b92d10 ["BRANCH", null, ["local:b14:8"]]
- 00b928e8 bytes 24000014
+ 00b92d10 bytes 24000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b488d563001c84e499ce327fd643f77c"></a>

### [`00b95588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95588.md) → [`00b959b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b959b0.md) _ZN11flatbuffers11EqualByNameERKNS_4TypeES2_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bbd0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5bfd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bfd0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 71.70% / 新版 76.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95694"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9569c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b956a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b956a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95b1c"
      ]
    ]
  ],
  "added": [
    [
      "00b95acc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b95b1c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b95694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95588.md#insn-00b95694) · [`00b9569c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95588.md#insn-00b9569c) · [`00b956a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95588.md#insn-00b956a4)

~~~diff
- 00b95694 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b95694 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b95694 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00b95694 ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b95694 bytes 02018d9a
- 00b9569c ["COPY", "tmp:0:8", ["register:4078:8"]]
- 00b9569c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b9569c ["COPY", "tmp:0:8", ["register:4070:8"]]
- 00b9569c ["COPY", "register:4068:8", ["tmp:0:8"]]
- 00b9569c bytes ed018e9a
- 00b956a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b956a4 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 00b956a4 bytes 81020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4335b27a366981f1171a939d90653235"></a>

### [`00b957ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b957ec.md) → [`00b95c14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95c14.md) _ZN11flatbuffers19StringToIntegerImplImEEbPT_PKcib

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bdc0.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5cd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd60.md)
- 新版 呼出元 1件 [`00c5c1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1c0.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d160.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 59.52% / 新版 58.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95928"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b95d50"
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
      "00b95c60",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "00b95cc8",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ],
    [
      "00b95ce8",
      "READ",
      [
        "storage",
        "00c9b430",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b95c60",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b95cc8",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ],
    [
      "00b95ce8",
      "READ",
      [
        "storage",
        "00c9b830",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b95928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b957ec.md#insn-00b95928) · [`00b95820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b957ec.md#insn-00b95820)
- 新版 `00b95d50`（命令位置の公開資料なし） · `00b95c48`（命令位置の公開資料なし）

~~~diff
- 00b95928 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b95928 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
- 00b95928 bytes e1000054
+ 00b95d50 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b95d50 ["CBRANCH", null, ["local:b30:8", "tmp:0:1"]]
+ 00b95d50 bytes e1000054
- 00b95820 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00b95820 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00b95820 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00b95c48 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00b95c48 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
+ 00b95c48 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00b95820 bytes 6d010054
+ 00b95c48 bytes 6d010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba5abcf475e566439ffd344b15af4c8c"></a>

### [`00b95aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95aa8.md) → [`00b95ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b95/00b95ed0.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumValEEENS_19__map_value_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c690.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ca90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca90.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 69.57% / 新版 69.57%

CFGの説明率　旧版 32.14% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b95aac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b95aa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b95aac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b95ab0",
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
      "00b95ed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b95ed4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b95ed8",
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

- 旧版 [`00b95aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95aa8.md#insn-00b95aa8) · [`00b95aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95aa8.md#insn-00b95aac) · [`00b95ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95aa8.md#insn-00b95ab0)

~~~diff
- 00b95aa8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b95aa8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b95aa8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b95aa8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b95aa8 bytes f85fbca9
- 00b95aac ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b95aac ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b95aac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b95aac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b95aac bytes f65701a9
- 00b95ab0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b95ab0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b95ab0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b95ab0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b95ab0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1d732cb2d88888282ac743b588aaee6"></a>

### [`00b961d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b961d4.md) → [`00b965fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b96/00b965fc.md) _ZN11flatbuffers19StringToIntegerImplIlEEbPT_PKcib

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bdb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bdb0.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5cd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd50.md)
- 新版 呼出元 1件 [`00c5c1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1b0.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5d150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d150.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.51% / 新版 88.51%

CFGの説明率　旧版 40.91% / 新版 41.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b961d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b961dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b961dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b961d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b961dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b961e0",
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
      "00b96600",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b96604",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b96608",
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

- 旧版 [`00b961d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b961d4.md#insn-00b961d8) · [`00b961dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b961d4.md#insn-00b961dc) · [`00b961e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b96/00b961d4.md#insn-00b961e0)

~~~diff
- 00b961d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b961d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b961d8 bytes f70b00f9
- 00b961dc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b961dc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b961dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b961dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b961dc bytes f65702a9
- 00b961e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b961e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b961e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b961e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b961e0 bytes f44f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82e28181d560347c7e84d79542c67155"></a>

### [`00b98f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98f2c.md) → [`00b99354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b99354.md) _ZNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE8overflowEi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4e0.md) [`00c5ba70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8e0.md) [`00c5be70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be70.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.81% / 新版 97.81%

CFGの説明率　旧版 97.87% / 新版 95.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b99144",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b9956c",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b98fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98f2c.md#insn-00b98fdc) · [`00b99058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98f2c.md#insn-00b99058) · [`00b99144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b98/00b98f2c.md#insn-00b99144)
- 新版 `00b99404`（命令位置の公開資料なし） · `00b99480`（命令位置の公開資料なし）

~~~diff
- 00b98fdc ["INT_ADD", "register:40f0:8", ["const:b98fdc:8", "const:4:8"]]
- 00b98fdc ["CALL", null, ["callee:00c5a8e0:8"]]
+ 00b99404 ["INT_ADD", "register:40f0:8", ["const:b99404:8", "const:4:8"]]
+ 00b99404 ["CALL", null, ["callee:00c5a8e0:8"]]
- 00b98fdc bytes 41050394
+ 00b99404 bytes 37050394
- 00b99058 ["INT_ADD", "register:40f0:8", ["const:b99058:8", "const:4:8"]]
- 00b99058 ["CALL", null, ["callee:00c5be70:8"]]
+ 00b99480 ["INT_ADD", "register:40f0:8", ["const:b99480:8", "const:4:8"]]
+ 00b99480 ["CALL", null, ["callee:00c5be70:8"]]
- 00b99058 bytes 860a0394
+ 00b99480 bytes 7c0a0394
- 00b99144 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00b99144 ["LOAD", "tmp:1:8", ["const:1b1:8", "tmp:0:8"]]
- 00b99144 ["INT_ADD", "tmp:2:8", ["tmp:0:8", "const:8:8"]]
- 00b99144 ["LOAD", "tmp:3:8", ["const:1b1:8", "tmp:2:8"]]
- 00b99144 bytes fa6741a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33f5f38e5863e66d84e8d97bf57d2789"></a>

### [`00b992b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b992b8.md) → [`00b996e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b996e0.md) _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c57db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57db0.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c581b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581b0.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 49.62% / 新版 49.62%

CFGの説明率　旧版 20.31% / 新版 20.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99324"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99368"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99398"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b99314",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b998e8"
      ]
    ],
    [
      "unmatched:00b9931c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b997ac"
      ]
    ],
    [
      "unmatched:00b9932c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b998d0"
      ]
    ]
  ],
  "added": [
    [
      "00b9973c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b998e8"
      ]
    ],
    [
      "00b99744",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b997ac"
      ]
    ],
    [
      "00b99754",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b998d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b99314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b992b8.md#insn-00b99314) · [`00b9931c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b992b8.md#insn-00b9931c) · [`00b99324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b992b8.md#insn-00b99324)

~~~diff
- 00b99314 ["CBRANCH", null, ["local:b42:8", "register:102:1"]]
- 00b99314 bytes 620d0054
- 00b9931c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b9931c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b9931c ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 00b9931c bytes 48030054
- 00b99324 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b99324 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b99324 ["INT_ADD", "register:4098:8", ["register:4098:8", "const:1:8"]]
- 00b99324 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b99324 bytes 68160038
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb282426ccf39cda6a843065e5fa361f"></a>

### [`00b994c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b994c4.md) → [`00b998ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b99/00b998ec.md) FUN_00b998ec

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00b89fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b89/00b89fd8.md) [`00b8a110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b8a/00b8a110.md) [`00b9b2d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9b2d4.md) [`00bafc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00bafc4c.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 4件 [`00b8a400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a400.md) [`00b8a538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b8a/00b8a538.md) [`00b9b6fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9b/00b9b6fc.md) [`00bb0074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb0/00bb0074.md) · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.42% / 新版 92.42%

CFGの説明率　旧版 60.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9956c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b99994"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99534"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b99538",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b999ec"
      ]
    ]
  ],
  "added": [
    [
      "00b99960",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b999ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b99534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b994c4.md#insn-00b99534) · [`00b99538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b994c4.md#insn-00b99538) · [`00b9956c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b99/00b994c4.md#insn-00b9956c)

~~~diff
- 00b99534 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b99534 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b99534 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b99534 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00b99534 bytes 3931889a
- 00b99538 ["INT_EQUAL", "tmp:0:1", ["register:40c8:8", "const:0:8"]]
- 00b99538 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00b99538 bytes 790400b4
- 00b9956c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b9956c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b9956c bytes 0001803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fe7b71720d61f3577b725dfb9afe40e"></a>

### [`00b9a6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a6d0.md) → [`00b9aaf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9a/00b9aaf8.md) _ZNSt6__ndk127__insertion_sort_incompleteIRZN11flexbuffers7Builder6EndMapEmEUlRKZNS2_6EndMapEmE8TwoValueS5_E_PS3_EEbT0_S9_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9d0.md) · 呼出先 4件 [`00b9a3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a3f0.md) [`00c5b450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b450.md) [`00c5cc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc90.md) [`00c5ccd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccd0.md)
- 新版 呼出元 1件 [`00c5cdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cdd0.md) · 呼出先 4件 [`00b9a818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9a/00b9a818.md) [`00c5b850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b850.md) [`00c5d090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d090.md) [`00c5d0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0d0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 80.85% / 新版 84.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9a7a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b9abc8"
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
      "unmatched:00b9a718",
      "DATA",
      [
        "storage",
        "0030e192",
        "switchD_00b9a724::switchdataD_0030e192",
        "byte"
      ]
    ],
    [
      "unmatched:00b9a7a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9acdc"
      ]
    ]
  ],
  "added": [
    [
      "00b9ab40",
      "DATA",
      [
        "storage",
        "0030e1d2",
        "switchD_00b9ab4c::switchdataD_0030e1d2",
        "byte"
      ]
    ],
    [
      "00b9abc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9acdc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9a7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a6d0.md#insn-00b9a7a0) · [`00b9a708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a6d0.md#insn-00b9a708)
- 新版 `00b9abc8`（命令位置の公開資料なし） · `00b9ab30`（命令位置の公開資料なし）

~~~diff
- 00b9a7a0 ["CBRANCH", null, ["local:b27:8", "register:101:1"]]
- 00b9a7a0 bytes a0080054
+ 00b9abc8 ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
+ 00b9abc8 bytes a0080054
- 00b9a708 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b9a708 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b9a708 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
+ 00b9ab30 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b9ab30 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00b9ab30 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00b9a708 bytes a8020054
+ 00b9ab30 bytes a8020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09dfffe762928ac23ddb596b754488c6"></a>

### [`00b9a900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a900.md) → [`00b9ad28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9a/00b9ad28.md) _ZN11flexbuffers7Builder8WriteAnyERKNS0_5ValueEh

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c500.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5cc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc80.md)
- 新版 呼出元 1件 [`00c5c900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c900.md) · 呼出先 2件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5d080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d080.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.72% / 新版 87.72%

CFGの説明率　旧版 70.59% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9a9c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b9ade8"
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
      "unmatched:00b9a934",
      "DATA",
      [
        "storage",
        "0030e198",
        "switchD_00b9a93c::switchdataD_0030e198",
        "byte"
      ]
    ],
    [
      "unmatched:00b9a9c0",
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
      "00b9ad5c",
      "DATA",
      [
        "storage",
        "0030e1d8",
        "switchD_00b9ad64::switchdataD_0030e1d8",
        "byte"
      ]
    ],
    [
      "00b9ade8",
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

- 旧版 [`00b9a9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a900.md#insn-00b9a9c0) · [`00b9a92c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a900.md#insn-00b9a92c)
- 新版 `00b9ade8`（命令位置の公開資料なし）

~~~diff
- 00b9a9c0 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00b9a9c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b9a9c0 bytes e80300f9
+ 00b9ade8 ["COPY", "tmp:0:8", ["register:8:8"]]
+ 00b9ade8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00b9ade8 bytes e80300f9
- 00b9a92c ["COPY", "tmp:0:8", ["const:198:8"]]
- 00b9a92c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b9a92c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b9a92c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b9a92c bytes 29610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-195a5dc864dd50ac53a998536593e6f2"></a>

### [`00b9a9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a9e4.md) → [`00b9ae0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9a/00b9ae0c.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertENS_11__wrap_iterIPKhEEmRS5_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc70.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5d070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d070.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 92.24% / 新版 92.24%

CFGの説明率　旧版 75.24% / 新版 75.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9aa20"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9aa30"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9aab8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9aa20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9ae88"
      ]
    ],
    [
      "unmatched:00b9aa30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9b174"
      ]
    ],
    [
      "unmatched:00b9aab8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9af2c"
      ]
    ]
  ],
  "added": [
    [
      "00b9ae48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9ae88"
      ]
    ],
    [
      "00b9ae58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9b174"
      ]
    ],
    [
      "00b9aee0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9af2c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9aa20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a9e4.md#insn-00b9aa20) · [`00b9aa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a9e4.md#insn-00b9aa30) · [`00b9aab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9a9e4.md#insn-00b9aab8)

~~~diff
- 00b9aa20 ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
- 00b9aa20 bytes 02020054
- 00b9aa30 ["CBRANCH", null, ["local:b67:8", "register:100:1"]]
- 00b9aa30 bytes e4180054
- 00b9aab8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b9aab8 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00b9aab8 bytes 63020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-519049bf1680fa4a1cef5478155d2734"></a>

### [`00b9ad50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9ad50.md) → [`00b9b178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9b/00b9b178.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6insertIPKhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cc80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cc80.md) · 呼出先 5件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5d080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d080.md) · 呼出先 5件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 98.33% / 新版 98.33%

CFGの説明率　旧版 95.65% / 新版 94.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9afac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9afac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b9b3d4"
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
      "unmatched:00b9afb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9b3c8"
      ]
    ]
  ],
  "added": [
    [
      "00b9b3dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9b3c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9afac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9ad50.md#insn-00b9afac) · [`00b9afb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9a/00b9ad50.md#insn-00b9afb4)
- 新版 `00b9b3d4`（命令位置の公開資料なし）

~~~diff
- 00b9afac ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:fffffffffffffff0:8"]]
- 00b9afac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b9afac ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b9afac ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b9afac bytes a0853fad
- 00b9afb4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b9afb4 ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
- 00b9afb4 bytes 61ffff54
+ 00b9b3d4 ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:fffffffffffffff0:8"]]
+ 00b9b3d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00b9b3d4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
+ 00b9b3d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
+ 00b9b3d4 bytes a0853fad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4e8d889f8b7ec4313e08df6e9045e4d"></a>

### [`00b9b680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9b680.md) → [`00b9baa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9b/00b9baa8.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6StringEEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf70.md) · 呼出先 2件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c370.md) · 呼出先 2件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 65.38% / 新版 62.96%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9b680"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9b680"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9b684"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9b680",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9b684",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9b688",
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
      "00b9baa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b9baac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b9bab0",
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

- 旧版 [`00b9b680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9b680.md#insn-00b9b680) · [`00b9b684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9b680.md#insn-00b9b684) · [`00b9b688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9b680.md#insn-00b9b688)

~~~diff
- 00b9b680 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b9b680 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b9b680 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b9b680 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b9b680 bytes f657bda9
- 00b9b684 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b9b684 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b9b684 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b9b684 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9b684 bytes f44f01a9
- 00b9b688 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b9b688 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b9b688 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b9b688 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9b688 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85ab57eb800f1bda4db66e463585078c"></a>

### [`00b9bb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9bb40.md) → [`00b9bf68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9b/00b9bf68.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection4EnumEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5bf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf90.md) · 呼出先 2件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c390.md) · 呼出先 2件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 93.42% / 新版 93.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `store_value` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9bc34"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b9c06c",
      "incomplete_value": true,
      "site": "00b9c078",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b9bc44",
      "incomplete_value": true,
      "site": "00b9bc50",
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
            "const:8:8"
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
      "site": "00b9c05c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b9bc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9bb40.md#insn-00b9bc34) · [`00b9bba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9bb40.md#insn-00b9bba0)
- 新版 `00b9c05c`（命令位置の公開資料なし） · `00b9bfc8`（命令位置の公開資料なし）

~~~diff
- 00b9bc34 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b9bc34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b9bc34 bytes 0a0100f9
+ 00b9c05c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00b9c05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00b9c05c bytes 0a0100f9
- 00b9bba0 ["INT_ADD", "register:40f0:8", ["const:b9bba0:8", "const:4:8"]]
- 00b9bba0 ["CALL", null, ["callee:00c5c1a0:8"]]
+ 00b9bfc8 ["INT_ADD", "register:40f0:8", ["const:b9bfc8:8", "const:4:8"]]
+ 00b9bfc8 ["CALL", null, ["callee:00c5c1a0:8"]]
- 00b9bba0 bytes 80000394
+ 00b9bfc8 bytes 76000394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b78f4d5d99fcb0f2474c03fb00a90dcd"></a>

### [`00b9bc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9bc70.md) → [`00b9c098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9c/00b9c098.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection6ObjectEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bfb0.md) · 呼出先 2件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c3b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c3b0.md) · 呼出先 2件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.42% / 新版 93.42%

CFGの説明率　旧版 61.54% / 新版 55.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9bd0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9bd1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b9c134"
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
      "00b9c0d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b9bd10"
      ]
    ],
    [
      "00b9c11c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b9bd10"
      ]
    ],
    [
      "unmatched:00b9bd0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9c124"
      ]
    ]
  ],
  "added": [
    [
      "00b9c0d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9c138"
      ]
    ],
    [
      "00b9c11c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9c138"
      ]
    ],
    [
      "00b9c134",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9c124"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9bd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9bc70.md#insn-00b9bd0c) · [`00b9bd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9bc70.md#insn-00b9bd1c)
- 新版 `00b9c134`（命令位置の公開資料なし）

~~~diff
- 00b9bd0c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b9bd0c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00b9bd0c bytes 81ffff54
- 00b9bd1c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b9bd1c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b9bd1c bytes 61000054
+ 00b9c134 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00b9c134 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b9c134 bytes 81ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6fdacaef1c45e70e7f87eb319d7e0c8"></a>

### [`00b9bed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9bed0.md) → [`00b9c2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9c/00b9c2f8.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection5FieldEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bfa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bfa0.md) · 呼出先 2件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c3a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c3a0.md) · 呼出先 2件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.11% / 新版 92.11%

CFGの説明率　旧版 30.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9bf48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9bf4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9bf50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9bf6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9c384"
      ]
    ]
  ],
  "added": [
    [
      "00b9c394",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9c384"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9bf48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9bed0.md#insn-00b9bf48) · [`00b9bf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9bed0.md#insn-00b9bf4c) · [`00b9bf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9b/00b9bed0.md#insn-00b9bf50)

~~~diff
- 00b9bf48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:40:8"]]
- 00b9bf48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b9bf48 bytes 892200f9
- 00b9bf4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:30:8"]]
- 00b9bf4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b9bf4c bytes 883200b9
- 00b9bf50 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b9bf50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b9bf50 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00b9bf50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b9bf50 bytes 3f010039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c08a80e1da097a396ac8791f82676bae"></a>

### [`00b9c000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c000.md) → [`00b9c428`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9c/00b9c428.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetIN10reflection4TypeEEEvtNS_6OffsetIT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bf50.md) · 呼出先 2件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c350.md) · 呼出先 2件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.58% / 新版 81.58%

CFGの説明率　旧版 18.75% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c000"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c000"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c004"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9c000",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9c004",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9c008",
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
      "00b9c428",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b9c42c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b9c430",
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

- 旧版 [`00b9c000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c000.md#insn-00b9c000) · [`00b9c004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c000.md#insn-00b9c004) · [`00b9c008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c000.md#insn-00b9c008)

~~~diff
- 00b9c000 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b9c000 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b9c000 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b9c000 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b9c000 bytes f657bda9
- 00b9c004 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b9c004 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b9c004 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b9c004 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9c004 bytes f44f01a9
- 00b9c008 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b9c008 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b9c008 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b9c008 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b9c008 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c8c66c437a47c35c7c2440c9f3a0f20"></a>

### [`00b9c260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c260.md) → [`00b9c688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9c/00b9c688.md) _ZN11flatbuffers21FlatBufferBuilderImplILb0EE9AddOffsetINS_6VectorINS_6OffsetIN10reflection7EnumValEEEjEEEEvtNS4_IT_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bfc0.md) · 呼出先 2件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) [`00c5be50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5be50.md)
- 新版 呼出元 1件 [`00c5c3c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c3c0.md) · 呼出先 2件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) [`00c5c250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c250.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 59.26% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c2a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c2e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b9c6c8"
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
      "unmatched:00b9c2a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9c728"
      ]
    ],
    [
      "unmatched:00b9c2e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9c728"
      ]
    ]
  ],
  "added": [
    [
      "00b9c6c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9c728"
      ]
    ],
    [
      "00b9c70c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9c728"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9c2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c260.md#insn-00b9c2a0) · [`00b9c2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c260.md#insn-00b9c2e4)
- 新版 `00b9c6c8`（命令位置の公開資料なし）

~~~diff
- 00b9c2a0 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00b9c2a0 bytes 00030054
- 00b9c2e4 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00b9c2e4 bytes e0000054
+ 00b9c6c8 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
+ 00b9c6c8 bytes 00030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6628eb650993fb5d08fadf86a3772a0e"></a>

### [`00b9c568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c568.md) → [`00b9c990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9c/00b9c990.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEbEENS_19__map_value_compareIS7_S8_NS_4lessI

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c6c0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cac0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.20% / 新版 94.20%

CFGの説明率　旧版 91.30% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c59c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9c5a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b9c9c4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b9c59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c568.md#insn-00b9c59c) · [`00b9c5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9c568.md#insn-00b9c5a0)
- 新版 `00b9c9c4`（命令位置の公開資料なし）

~~~diff
- 00b9c59c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b9c59c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b9c59c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b9c59c ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00b9c59c bytes 7601899a
- 00b9c5a0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b9c5a0 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00b9c5a0 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00b9c5a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00b9c5a0 bytes 5515819a
+ 00b9c9c4 ["COPY", "tmp:0:8", ["register:4058:8"]]
+ 00b9c9c4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00b9c9c4 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00b9c9c4 ["COPY", "register:40b0:8", ["tmp:0:8"]]
+ 00b9c9c4 bytes 7601899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9c02eef83025446e484d760cbcd82b3"></a>

### [`00b9cb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9cb48.md) → [`00b9cf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9c/00b9cf70.md) _ZNSt6__ndk118__stable_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection8KeyValueEEEPNS1_6OffsetIS6_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c870.md) · 呼出先 3件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5c740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c740.md) [`00c5c930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c930.md)
- 新版 呼出元 1件 [`00c5cc70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cc70.md) · 呼出先 3件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5cb40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cb40.md) [`00c5cd30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cd30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.60% / 新版 96.60%

CFGの説明率　旧版 76.92% / 新版 73.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9cce8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9cdb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9ce50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9cce8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9d134"
      ]
    ],
    [
      "unmatched:00b9cdb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9d220"
      ]
    ],
    [
      "unmatched:00b9ce50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9d264"
      ]
    ]
  ],
  "added": [
    [
      "00b9d110",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9d134"
      ]
    ],
    [
      "00b9d1e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9d220"
      ]
    ],
    [
      "00b9d278",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9d264"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9cce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9cb48.md#insn-00b9cce8) · [`00b9cdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9cb48.md#insn-00b9cdb8) · [`00b9ce50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9c/00b9cb48.md#insn-00b9ce50)

~~~diff
- 00b9cce8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b9cce8 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00b9cce8 bytes 21010054
- 00b9cdb8 ["CBRANCH", null, ["local:b27:8", "register:102:1"]]
- 00b9cdb8 bytes 02020054
- 00b9ce50 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b9ce50 ["CBRANCH", null, ["local:b31:8", "tmp:0:1"]]
- 00b9ce50 bytes 61ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57c7e935ddc075c94b3b416af53e7c61"></a>

### [`00b9e328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9e/00b9e328.md) → [`00b9e750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9e/00b9e750.md) _ZNK10reflection6Object6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c560.md) · 呼出先 2件 [`00c5c550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c550.md) [`00c5c5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c5b0.md)
- 新版 呼出元 1件 [`00c5c960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c960.md) · 呼出先 2件 [`00c5c950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c950.md) [`00c5c9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c9b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 83.50% / 新版 83.50%

CFGの説明率　旧版 64.85% / 新版 60.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9e4b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9e4e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9e594"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9e4b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9e950"
      ]
    ],
    [
      "unmatched:00b9e4e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9e874"
      ]
    ],
    [
      "unmatched:00b9e594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9e874"
      ]
    ]
  ],
  "added": [
    [
      "00b9e8dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9e950"
      ]
    ],
    [
      "00b9e90c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9e874"
      ]
    ],
    [
      "00b9eaf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9eb00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9e374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9e/00b9e328.md#insn-00b9e374) · [`00b9e4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9e/00b9e328.md#insn-00b9e4a8) · [`00b9e4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9e/00b9e328.md#insn-00b9e4b4)
- 新版 `00b9e79c`（命令位置の公開資料なし） · `00b9e8d0`（命令位置の公開資料なし）

~~~diff
- 00b9e374 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00b9e374 ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
+ 00b9e79c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00b9e79c ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00b9e374 bytes e3060054
+ 00b9e79c bytes e3060054
- 00b9e4a8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b9e4a8 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
+ 00b9e8d0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b9e8d0 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00b9e4a8 bytes 28fdffb4
+ 00b9e8d0 bytes 28fdffb4
- 00b9e4b4 ["CBRANCH", null, ["local:b47:8", "register:101:1"]]
- 00b9e4b4 bytes a0030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-548b3136dc215071f1ca33a1dfb0006b"></a>

### [`00b9f558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9f/00b9f558.md) → [`00b9f980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b9f/00b9f980.md) _ZNK10reflection8KeyValue6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c5b0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5c9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c9b0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 78.34% / 新版 78.34%

CFGの説明率　旧版 41.80% / 新版 44.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9f564"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9f5a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9f5c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9f564",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9f998"
      ]
    ],
    [
      "unmatched:00b9f5a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9fa88"
      ]
    ],
    [
      "unmatched:00b9f5c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9fa88"
      ]
    ]
  ],
  "added": [
    [
      "00b9f98c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9f998"
      ]
    ],
    [
      "00b9f994",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9fa88"
      ]
    ],
    [
      "00b9f9d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b9fa88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9f564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9f/00b9f558.md#insn-00b9f564) · [`00b9f5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9f/00b9f558.md#insn-00b9f5a8) · [`00b9f5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b9f/00b9f558.md#insn-00b9f5c4)

~~~diff
- 00b9f564 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00b9f564 bytes 60000054
- 00b9f5a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b9f5a8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b9f5a8 ["CBRANCH", null, ["local:b26:8", "tmp:1:1"]]
- 00b9f5a8 bytes c8050054
- 00b9f5c4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b9f5c4 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00b9f5c4 bytes e8040035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebcb8267d4b61a2be2012b9a786358bf"></a>

### [`00ba001c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba0/00ba001c.md) → [`00ba0444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba0/00ba0444.md) _ZNK10reflection7EnumVal6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c580.md) · 呼出先 2件 [`00c5c540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c540.md) [`00c5c5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c5b0.md)
- 新版 呼出元 1件 [`00c5c980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c980.md) · 呼出先 2件 [`00c5c940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c940.md) [`00c5c9b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c9b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 89.44% / 新版 89.44%

CFGの説明率　旧版 46.36% / 新版 48.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 16件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba00d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba00f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba0184"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba00d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba056c"
      ]
    ],
    [
      "unmatched:00ba00f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba0568"
      ]
    ],
    [
      "00ba0598",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ba018c"
      ]
    ]
  ],
  "added": [
    [
      "00ba04f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba056c"
      ]
    ],
    [
      "00ba051c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba0568"
      ]
    ],
    [
      "00ba0598",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba05b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba0068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba0/00ba001c.md#insn-00ba0068) · [`00ba00c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba0/00ba001c.md#insn-00ba00c4) · [`00ba00d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba0/00ba001c.md#insn-00ba00d0)
- 新版 `00ba0490`（命令位置の公開資料なし） · `00ba04ec`（命令位置の公開資料なし）

~~~diff
- 00ba0068 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba0068 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
+ 00ba0490 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00ba0490 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 00ba0068 bytes e3060054
+ 00ba0490 bytes e3060054
- 00ba00c4 ["INT_RIGHT", "tmp:0:4", ["register:4068:4", "const:0:4"]]
- 00ba00c4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ba00c4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ba00c4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00ba04ec ["INT_RIGHT", "tmp:0:4", ["register:4068:4", "const:0:4"]]
+ 00ba04ec ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00ba04ec ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00ba04ec ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00ba00c4 bytes ed030037
+ 00ba04ec bytes ed030037
- 00ba00d0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba00d0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00ba00d0 ["CBRANCH", null, ["local:b27:8", "tmp:1:1"]]
- 00ba00d0 bytes a9030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf3e31f0a0d065f3b780f31fe41b912a"></a>

### [`00ba1270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1270.md) → [`00ba1698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba1/00ba1698.md) _ZNK10reflection10SchemaFile6VerifyERN11flatbuffers16VerifierTemplateILb0EEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c520.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5c920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c920.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.37% / 新版 96.37%

CFGの説明率　旧版 75.97% / 新版 77.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba1294"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba1308"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba13dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba1294",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba1994"
      ]
    ],
    [
      "unmatched:00ba1308",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba1994"
      ]
    ],
    [
      "00ba18ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba1784"
      ]
    ]
  ],
  "added": [
    [
      "00ba16bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba1994"
      ]
    ],
    [
      "00ba1730",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba1994"
      ]
    ],
    [
      "00ba1774",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba1784"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba1294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1270.md#insn-00ba1294) · [`00ba1308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1270.md#insn-00ba1308) · [`00ba13dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1270.md#insn-00ba13dc)

~~~diff
- 00ba1294 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba1294 ["CBRANCH", null, ["local:b71:8", "tmp:0:1"]]
- 00ba1294 bytes c3160054
- 00ba1308 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba1308 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00ba1308 ["CBRANCH", null, ["local:b71:8", "tmp:1:1"]]
- 00ba1308 bytes 29130054
- 00ba13dc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba13dc ["CBRANCH", null, ["local:b71:8", "tmp:0:1"]]
- 00ba13dc bytes 830c0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2273678169b3225cc414835c71a76f46"></a>

### [`00ba1d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1d84.md) → [`00ba21ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba2/00ba21ac.md) _ZN11flatbuffers15vector_downwardIjE10reallocateEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5bda0.md) · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c5ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md) [`00c5ba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba50.md)
- 新版 呼出元 1件 [`00c5c1a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5c1a0.md) · 呼出先 3件 [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5be40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be40.md) [`00c5be50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be50.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 68.75% / 新版 68.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba1eac"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00ba22d4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba1eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1d84.md#insn-00ba1eac) · [`00ba1df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1d84.md#insn-00ba1df4)
- 新版 `00ba22d4`（命令位置の公開資料なし） · `00ba221c`（命令位置の公開資料なし）

~~~diff
- 00ba1eac ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ba1eac ["RETURN", null, ["register:0:8"]]
- 00ba1eac bytes c0035fd6
+ 00ba22d4 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00ba22d4 ["RETURN", null, ["register:0:8"]]
+ 00ba22d4 bytes c0035fd6
- 00ba1df4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00ba1df4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00ba221c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00ba221c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00ba1df4 bytes 000200b4
+ 00ba221c bytes 000200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d33ae050856427e089c11087824bab8"></a>

### [`00ba1eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1eb0.md) → [`00ba22d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba2/00ba22d8.md) _ZNSt6__ndk113__stable_sortIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EEEEvT0_S

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c710.md) · 呼出先 4件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5c710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c710.md) [`00c5c7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c7a0.md) [`00c5c840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c840.md)
- 新版 呼出元 1件 [`00c5cb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cb10.md) · 呼出先 4件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5cb10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cb10.md) [`00c5cba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cba0.md) [`00c5cc40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cc40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.21% / 新版 91.21%

CFGの説明率　旧版 50.65% / 新版 48.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2060"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba2488"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2064"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba2064",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba2418"
      ]
    ],
    [
      "unmatched:00ba20f0",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba2254",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba26a4"
      ]
    ]
  ],
  "added": [
    [
      "00ba248c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba2418"
      ]
    ],
    [
      "00ba2518",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ba267c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba26a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1eb0.md#insn-00ba2060) · [`00ba2064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1eb0.md#insn-00ba2064) · [`00ba2254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1eb0.md#insn-00ba2254)

~~~diff
- 00ba2060 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4:8"]]
- 00ba2060 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:4"]]
- 00ba2060 bytes 1c0500b9
- 00ba2064 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ba2064 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00ba2064 bytes 61fcff54
- 00ba2254 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba2254 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00ba2254 ["CBRANCH", null, ["local:b34:8", "tmp:1:1"]]
- 00ba2254 bytes 49010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-031333bbfa90e5aeb5c43f1765c193b6"></a>

### [`00ba2728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2728.md) → [`00ba2b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba2/00ba2b50.md) _ZNSt6__ndk115__inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EEEEvT0

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c7a0.md) · 呼出先 4件 [`00ba311c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba3/00ba311c.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5c7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c7a0.md) [`00c5c960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c960.md)
- 新版 呼出元 1件 [`00c5cba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cba0.md) · 呼出先 4件 [`00ba3544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba3/00ba3544.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5cba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cba0.md) [`00c5cd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cd60.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.48% / 新版 92.48%

CFGの説明率　旧版 63.16% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2748"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba2748"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba274c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba2748",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba274c",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba2750",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba2b70",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00ba2b74",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "00ba2b78",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba2748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2728.md#insn-00ba2748) · [`00ba274c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2728.md#insn-00ba274c) · [`00ba2750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2728.md#insn-00ba2750)

~~~diff
- 00ba2748 ["COPY", "tmp:0:8", ["register:4018:8"]]
- 00ba2748 ["COPY", "tmp:1:8", ["register:4038:8"]]
- 00ba2748 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:28:8"]]
- 00ba2748 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba2748 bytes e39f02a9
- 00ba274c ["COPY", "tmp:0:8", ["register:4030:8"]]
- 00ba274c ["COPY", "tmp:1:8", ["register:4010:8"]]
- 00ba274c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:18:8"]]
- 00ba274c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba274c bytes e68b01a9
- 00ba2750 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00ba2750 ["COPY", "tmp:1:8", ["register:4028:8"]]
- 00ba2750 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:38:8"]]
- 00ba2750 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba2750 bytes e19703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d2219cf00ee2954c7a2f019a5984edf"></a>

### [`00ba2b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2b50.md) → [`00ba2f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba2/00ba2f78.md) _ZNSt6__ndk121__insertion_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c900.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cd00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cd00.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 80.00% / 新版 76.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba2b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2b50.md#insn-00ba2b78) · [`00ba2b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2b50.md#insn-00ba2b94) · [`00ba2c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2b50.md#insn-00ba2c00)
- 新版 `00ba2fa0`（命令位置の公開資料なし） · `00ba2fbc`（命令位置の公開資料なし） · `00ba3028`（命令位置の公開資料なし）

~~~diff
- 00ba2b78 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 00ba2fa0 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00ba2b78 bytes 800b0054
+ 00ba2fa0 bytes 800b0054
- 00ba2b94 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 00ba2fbc ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00ba2b94 bytes a00a0054
+ 00ba2fbc bytes a00a0054
- 00ba2c00 ["INT_ADD", "register:40f0:8", ["const:ba2c00:8", "const:4:8"]]
- 00ba2c00 ["CALL", null, ["callee:00c58050:8"]]
+ 00ba3028 ["INT_ADD", "register:40f0:8", ["const:ba3028:8", "const:4:8"]]
+ 00ba3028 ["CALL", null, ["callee:00c58050:8"]]
- 00ba2c00 bytes 14d40294
+ 00ba3028 bytes 0ad40294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8590afee59c2cd1c90a7ca4fc6e60a0"></a>

### [`00ba2d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2d08.md) → [`00ba3130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba3/00ba3130.md) _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c960.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5c8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c8a0.md)
- 新版 呼出元 1件 [`00c5cd60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cd60.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5cca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cca0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.15% / 新版 84.15%

CFGの説明率　旧版 79.25% / 新版 76.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba2d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2d08.md#insn-00ba2d50) · [`00ba2d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2d08.md#insn-00ba2d58) · [`00ba2d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2d08.md#insn-00ba2d78)
- 新版 `00ba3178`（命令位置の公開資料なし） · `00ba3180`（命令位置の公開資料なし） · `00ba31a0`（命令位置の公開資料なし）

~~~diff
- 00ba2d50 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ba2d50 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00ba2d50 ["CBRANCH", null, ["local:b18:8", "tmp:1:1"]]
+ 00ba3178 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00ba3178 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
+ 00ba3178 ["CBRANCH", null, ["local:b19:8", "tmp:1:1"]]
- 00ba2d50 bytes cd0b0054
+ 00ba3178 bytes cd0b0054
- 00ba2d58 ["CBRANCH", null, ["local:b27:8", "register:101:1"]]
+ 00ba3180 ["CBRANCH", null, ["local:b29:8", "register:101:1"]]
- 00ba2d58 bytes 80110054
+ 00ba3180 bytes 80110054
- 00ba2d78 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba2d78 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00ba2d78 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
+ 00ba31a0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00ba31a0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00ba31a0 ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
- 00ba2d78 bytes 49030054
+ 00ba31a0 bytes 49030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88e73c3b29cfbaff41ee557634c94baf"></a>

### [`00ba2fe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2fe4.md) → [`00ba340c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba3/00ba340c.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection5FieldEEEPNS1_6OffsetIS6_EES

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c8a0.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cca0.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 74.36% / 新版 74.36%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba303c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba3464"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3118"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba303c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba3528"
      ]
    ],
    [
      "unmatched:00ba310c",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba3110",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba3464",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba3528"
      ]
    ],
    [
      "00ba3534",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ba3538",
      "READ",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba303c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2fe4.md#insn-00ba303c) · [`00ba3118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba2/00ba2fe4.md#insn-00ba3118)
- 新版 `00ba3464`（命令位置の公開資料なし）

~~~diff
- 00ba303c ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00ba303c bytes 20060054
- 00ba3118 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ba3118 ["RETURN", null, ["register:0:8"]]
- 00ba3118 bytes c0035fd6
+ 00ba3464 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 00ba3464 bytes 20060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6054d3bb19ec2b77ce7fdac7eb8d286f"></a>

### [`00ba3f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba3/00ba3f84.md) → [`00ba43ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba4/00ba43ac.md) _ZNSt6__ndk121__insertion_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS6_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c910.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cd10.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 68.18% / 新版 68.18%

CFGの説明率　旧版 25.00% / 新版 22.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3f98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3f98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3f9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba3f98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba3f9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba3fa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba43c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ba43c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ba43d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba3/00ba3f84.md#insn-00ba3f98) · [`00ba3f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba3/00ba3f84.md#insn-00ba3f9c) · [`00ba3fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba3/00ba3f84.md#insn-00ba3fa8)

~~~diff
- 00ba3f98 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ba3f98 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ba3f98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00ba3f98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba3f98 bytes f44f05a9
- 00ba3f9c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ba3f9c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ba3f9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00ba3f9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba3f9c bytes fd7b06a9
- 00ba3fa8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00ba3fa8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00ba3fa8 bytes e10700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caa6e7bdee1e68f771772bbe1c509d6a"></a>

### [`00ba413c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba413c.md) → [`00ba4564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba4/00ba4564.md) _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetI

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c970.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5c8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c8b0.md)
- 新版 呼出元 1件 [`00c5cd70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cd70.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5ccb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ccb0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 72.68% / 新版 72.68%

CFGの説明率　旧版 30.65% / 新版 30.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba414c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba414c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4150"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba414c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba4150",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba4154",
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
      "00ba4574",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ba4578",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ba457c",
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

- 旧版 [`00ba414c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba413c.md#insn-00ba414c) · [`00ba4150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba413c.md#insn-00ba4150) · [`00ba4154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba413c.md#insn-00ba4154)

~~~diff
- 00ba414c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ba414c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ba414c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00ba414c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba414c bytes f65706a9
- 00ba4150 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ba4150 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ba4150 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00ba4150 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba4150 bytes f44f07a9
- 00ba4154 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ba4154 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ba4154 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00ba4154 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba4154 bytes fd7b08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6bf626b2233f73e91e40e62dbee0786"></a>

### [`00ba4418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba4418.md) → [`00ba4840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba4/00ba4840.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS6_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c8b0.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ccb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ccb0.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 64.10% / 新版 64.10%

CFGの説明率　旧版 16.67% / 新版 19.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4458"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4478"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba44d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba4458",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ba447c"
      ]
    ],
    [
      "unmatched:00ba4478",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba4930"
      ]
    ]
  ],
  "added": [
    [
      "00ba4880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba48a4"
      ]
    ],
    [
      "00ba48a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba4930"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba4418.md#insn-00ba4458) · [`00ba4478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba4418.md#insn-00ba4478) · [`00ba44d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba4418.md#insn-00ba44d8)

~~~diff
- 00ba4458 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ba4458 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00ba4458 bytes 21010054
- 00ba4478 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00ba4478 bytes 80040054
- 00ba44d8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba44d8 ["COPY", "tmp:1:4", ["register:40e0:4"]]
- 00ba44d8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00ba44d8 ["COPY", "tmp:1:4", ["register:40d8:4"]]
- 00ba44d8 bytes 82339b1a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38e5a13cc6f001ea08fdd37f7f65a875"></a>

### [`00ba4550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba4550.md) → [`00ba4978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba4/00ba4978.md) FUN_00ba4978

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ba3b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba3/00ba3b5c.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)
- 新版 呼出元 1件 [`00ba3f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba3/00ba3f84.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.19% / 新版 77.19%

CFGの説明率　旧版 32.00% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4550"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4554"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba4554"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba4550",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba4554",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba4558",
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
      "00ba4978",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ba497c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ba4980",
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

- 旧版 [`00ba4550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba4550.md#insn-00ba4550) · [`00ba4554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba4550.md#insn-00ba4554) · [`00ba4558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba4/00ba4550.md#insn-00ba4558)

~~~diff
- 00ba4550 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00ba4550 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ba4550 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ba4550 bytes f50f1df8
- 00ba4554 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ba4554 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ba4554 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ba4554 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba4554 bytes f44f01a9
- 00ba4558 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ba4558 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ba4558 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ba4558 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba4558 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64bb8486f5e425b19d3a9a1948d3f071"></a>

### [`00ba5570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba5/00ba5570.md) → [`00ba5998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba5/00ba5998.md) _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c950.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5c890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c890.md)
- 新版 呼出元 1件 [`00c5cd50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cd50.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5cc90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cc90.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.49% / 新版 70.49%

CFGの説明率　旧版 22.97% / 新版 27.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba55b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba5634"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba5634"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba55b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba55e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba5be8"
      ]
    ],
    [
      "unmatched:00ba55f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba5a34"
      ]
    ]
  ],
  "added": [
    [
      "00ba59dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00ba5a08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba5a70"
      ]
    ],
    [
      "00ba5a1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba5a34"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba55b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba5/00ba5570.md#insn-00ba55b4) · [`00ba55e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba5/00ba5570.md#insn-00ba55e0) · [`00ba55f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba5/00ba5570.md#insn-00ba55f4)

~~~diff
- 00ba55b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00ba55b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ba55b4 bytes e81700f9
- 00ba55e0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba55e0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00ba55e0 ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
- 00ba55e0 bytes 49030054
- 00ba55f4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba55f4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00ba55f4 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00ba55f4 bytes c9000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9081b2f29f46056cde237e71a453f46"></a>

### [`00ba584c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba5/00ba584c.md) → [`00ba5c74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba5/00ba5c74.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS6_EESA

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c890.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cc90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cc90.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 64.10% / 新版 64.10%

CFGの説明率　旧版 42.11% / 新版 47.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba584c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba584c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba5850"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba584c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba5850",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba5854",
      "WRITE",
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
      "00ba5c74",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00ba5c78",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ba5c7c",
      "WRITE",
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

- 旧版 [`00ba584c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba5/00ba584c.md#insn-00ba584c) · [`00ba5850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba5/00ba584c.md#insn-00ba5850) · [`00ba5854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba5/00ba584c.md#insn-00ba5854)

~~~diff
- 00ba584c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00ba584c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00ba584c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00ba584c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ba584c bytes fc6fbaa9
- 00ba5850 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00ba5850 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00ba5850 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ba5850 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba5850 bytes fa6701a9
- 00ba5854 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ba5854 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ba5854 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ba5854 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba5854 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1111338817fc7b0baaffc96034a3bf70"></a>

### [`00ba69a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba6/00ba69a4.md) → [`00ba6dcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba6/00ba6dcc.md) _ZNSt6__ndk124__buffered_inplace_mergeIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6Offset

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c980.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c5c8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c8c0.md)
- 新版 呼出元 1件 [`00c5cd80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cd80.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5ccc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ccc0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 54.10% / 新版 54.10%

CFGの説明率　旧版 5.48% / 新版 5.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba69a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba69a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba69ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba69a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba69ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba69b0",
      "WRITE",
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
      "00ba6dd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00ba6dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ba6dd8",
      "WRITE",
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

- 旧版 [`00ba69a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba6/00ba69a4.md#insn-00ba69a8) · [`00ba69ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba6/00ba69a4.md#insn-00ba69ac) · [`00ba69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba6/00ba69a4.md#insn-00ba69b0)

~~~diff
- 00ba69a8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00ba69a8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00ba69a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00ba69a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba69a8 bytes fc6f03a9
- 00ba69ac ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00ba69ac ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00ba69ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00ba69ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba69ac bytes fa6704a9
- 00ba69b0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ba69b0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ba69b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00ba69b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba69b0 bytes f85f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd97241ee6da6ca9b291110ad421cdda"></a>

### [`00ba6c80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba6/00ba6c80.md) → [`00ba70a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba7/00ba70a8.md) _ZNSt6__ndk120__half_inplace_mergeIN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection7ServiceEEEPNS1_6OffsetIS6_E

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c8c0.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ccc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ccc0.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 3.70% / 新版 4.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba6c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba6c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ba70bc"
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
      "unmatched:00ba6c94",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ba719c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7198"
      ]
    ],
    [
      "unmatched:00ba6d74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba71c4"
      ]
    ]
  ],
  "added": [
    [
      "00ba70bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ba7108",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba7198"
      ]
    ],
    [
      "00ba719c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba71c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba6/00ba6c80.md#insn-00ba6c94) · [`00ba6d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba6/00ba6c80.md#insn-00ba6d74) · [`00ba6db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba6/00ba6c80.md#insn-00ba6db4)

~~~diff
- 00ba6c94 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ba6c94 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ba6c94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00ba6c94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba6c94 bytes fd7b05a9
- 00ba6d74 ["CBRANCH", null, ["local:b20:8", "register:101:1"]]
- 00ba6d74 bytes 40010054
- 00ba6db4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ba6db4 ["RETURN", null, ["register:0:8"]]
- 00ba6db4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a378f63fa79c563c81b46b45d24d805c"></a>

### [`00ba7c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba7/00ba7c20.md) → [`00ba8048`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba8/00ba8048.md) _ZNSt6__ndk121__insertion_sort_moveIRN11flatbuffers21FlatBufferBuilderImplILb0EE18TableKeyComparatorIN10reflection10SchemaFileEEEPNS1_6Offse

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c8e0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cce0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cce0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 73.64% / 新版 73.64%

CFGの説明率　旧版 20.00% / 新版 17.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7c24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7c24"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7c28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba7c24",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba7c28",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba7c2c",
      "WRITE",
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
      "00ba804c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00ba8050",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ba8054",
      "WRITE",
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

- 旧版 [`00ba7c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba7/00ba7c20.md#insn-00ba7c24) · [`00ba7c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba7/00ba7c20.md#insn-00ba7c28) · [`00ba7c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba7/00ba7c20.md#insn-00ba7c2c)

~~~diff
- 00ba7c24 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00ba7c24 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00ba7c24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ba7c24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba7c24 bytes fc6f01a9
- 00ba7c28 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00ba7c28 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00ba7c28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ba7c28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba7c28 bytes fa6702a9
- 00ba7c2c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ba7c2c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ba7c2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00ba7c2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba7c2c bytes f85f03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f5f21a279adbd52d2ce969243eb3b93"></a>

### [`00ba8584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8584.md) → [`00ba89ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba8/00ba89ac.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_co

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c670.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ca70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ca70.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 79.71% / 新版 79.71%

CFGの説明率　旧版 38.46% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba85a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba85b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba85bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba85a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8aa4"
      ]
    ],
    [
      "unmatched:00ba8608",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba89ec"
      ]
    ],
    [
      "unmatched:00ba862c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8aa4"
      ]
    ]
  ],
  "added": [
    [
      "00ba89c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8aa4"
      ]
    ],
    [
      "00ba8a30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba89ec"
      ]
    ],
    [
      "00ba8a54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8aa4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba85a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8584.md#insn-00ba85a0) · [`00ba85b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8584.md#insn-00ba85b8) · [`00ba85bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8584.md#insn-00ba85bc)

~~~diff
- 00ba85a0 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00ba85a0 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00ba85a0 bytes f70600b4
- 00ba85b8 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00ba85b8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00ba85b8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ba85b8 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00ba85b8 bytes 7601899a
- 00ba85bc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ba85bc ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00ba85bc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00ba85bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00ba85bc bytes 5515819a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d886e9b0050de4291ae63c3f1091d0e1"></a>

### [`00ba8a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8a48.md) → [`00ba8e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba8/00ba8e70.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers9StructDefEEENS_19__map_valu

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c6b0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cab0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 62.32% / 新版 62.32%

CFGの説明率　旧版 12.90% / 新版 8.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8a7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8a80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8ac0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba8acc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8eb0"
      ]
    ],
    [
      "unmatched:00ba8b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8f60"
      ]
    ]
  ],
  "added": [
    [
      "00ba8ef4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8eb0"
      ]
    ],
    [
      "00ba8f3c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ba8f60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8a48.md#insn-00ba8a7c) · [`00ba8a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8a48.md#insn-00ba8a80) · [`00ba8ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8a48.md#insn-00ba8ac0)

~~~diff
- 00ba8a7c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00ba8a7c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00ba8a7c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ba8a7c ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00ba8a7c bytes 7601899a
- 00ba8a80 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ba8a80 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00ba8a80 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00ba8a80 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00ba8a80 bytes 5515819a
- 00ba8ac0 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00ba8ac0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00ba8ac0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00ba8ac0 ["COPY", "register:40c0:8", ["tmp:0:8"]]
- 00ba8ac0 bytes 78018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-219ca080e0b0a50579c60e2e038d3c49"></a>

### [`00ba8b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8b5c.md) → [`00ba8f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba8/00ba8f84.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb50.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cf50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf50.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 63.77% / 新版 63.77%

CFGの説明率　旧版 13.79% / 新版 13.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 8件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8b5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8b5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8b60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba8b5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba8b60",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba8b64",
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
      "00ba8f84",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ba8f88",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ba8f8c",
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

- 旧版 [`00ba8b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8b5c.md#insn-00ba8b5c) · [`00ba8b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8b5c.md#insn-00ba8b60) · [`00ba8b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8b5c.md#insn-00ba8b64)

~~~diff
- 00ba8b5c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ba8b5c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ba8b5c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00ba8b5c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ba8b5c bytes f85fbca9
- 00ba8b60 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ba8b60 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ba8b60 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ba8b60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba8b60 bytes f65701a9
- 00ba8b64 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ba8b64 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ba8b64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ba8b64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba8b64 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f111db8b7b4a6226afb92089c7a091b"></a>

### [`00ba8fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8fb4.md) → [`00ba93dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba9/00ba93dc.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers5ValueEEENS_19__map_value_com

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cab0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ceb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ceb0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.71% / 新版 79.71%

CFGの説明率　旧版 25.93% / 新版 28.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8fb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8fb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8fb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba8fb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba8fb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba8fbc",
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
      "00ba93dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ba93e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ba93e4",
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

- 旧版 [`00ba8fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8fb4.md#insn-00ba8fb4) · [`00ba8fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8fb4.md#insn-00ba8fb8) · [`00ba8fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba8/00ba8fb4.md#insn-00ba8fbc)

~~~diff
- 00ba8fb4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ba8fb4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ba8fb4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00ba8fb4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ba8fb4 bytes f85fbca9
- 00ba8fb8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ba8fb8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ba8fb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ba8fb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba8fb8 bytes f65701a9
- 00ba8fbc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ba8fbc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ba8fbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ba8fbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba8fbc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e89a07cf51fabc3d8433127ee2557466"></a>

### [`00ba9800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba9/00ba9800.md) → [`00ba9c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ba9/00ba9c28.md) _ZNKSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers8FieldDefEEENS_19__map_value

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c6a0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5caa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5caa0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 75.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9838"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ba9c60"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9910"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba9/00ba9800.md#insn-00ba9838) · [`00ba9910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba9/00ba9800.md#insn-00ba9910)
- 新版 `00ba9c60`（命令位置の公開資料なし）

~~~diff
- 00ba9838 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ba9838 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00ba9838 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00ba9838 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00ba9838 bytes 5515819a
- 00ba9910 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ba9910 ["RETURN", null, ["register:0:8"]]
- 00ba9910 bytes c0035fd6
+ 00ba9c60 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00ba9c60 ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00ba9c60 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
+ 00ba9c60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
+ 00ba9c60 bytes 5515819a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c3bf2ee9a65e0379d7e69c34e361fc2"></a>

### [`00baa424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baa/00baa424.md) → [`00baa84c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baa/00baa84c.md) _ZNSt6__ndk114__split_bufferINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEERNS_9allocatorIS6_EEE9push_backEOS6_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5c770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c770.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)
- 新版 呼出元 1件 [`00c5cb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cb70.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5b140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 63.79% / 新版 63.79%

CFGの説明率　旧版 9.80% / 新版 9.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baa424"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baa428"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baa428"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00baa424",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00baa428",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00baa42c",
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
      "00baa84c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00baa850",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00baa854",
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

- 旧版 [`00baa424`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baa/00baa424.md#insn-00baa424) · [`00baa428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baa/00baa424.md#insn-00baa428) · [`00baa42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baa/00baa424.md#insn-00baa42c)

~~~diff
- 00baa424 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00baa424 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00baa424 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00baa424 bytes f90f1bf8
- 00baa428 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00baa428 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00baa428 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00baa428 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00baa428 bytes f85f01a9
- 00baa42c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00baa42c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00baa42c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00baa42c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00baa42c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5817ba37c460895048a4ea5375761cba"></a>

### [`00bac528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac528.md) → [`00bac950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bac/00bac950.md) FUN_00bac950

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00babb74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bab/00babb74.md) [`00bac7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac7d4.md) [`00baccbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00baccbc.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`00babf9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bab/00babf9c.md) [`00bacbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bac/00bacbfc.md) [`00bad0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00bad0e4.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.44% / 新版 75.44%

CFGの説明率　旧版 7.69% / 新版 7.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 19件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bac528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bac528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bac52c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bac528",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bac52c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bac530",
      "WRITE",
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
      "00bac950",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00bac954",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00bac958",
      "WRITE",
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

- 旧版 [`00bac528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac528.md#insn-00bac528) · [`00bac52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac528.md#insn-00bac52c) · [`00bac530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac528.md#insn-00bac530)

~~~diff
- 00bac528 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bac528 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bac528 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00bac528 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bac528 bytes fc6fbaa9
- 00bac52c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bac52c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bac52c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bac52c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bac52c bytes fa6701a9
- 00bac530 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bac530 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bac530 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bac530 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bac530 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c3bc351ced885b3ed079a351f65bd8f"></a>

### [`00bac7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac7d4.md) → [`00bacbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bac/00bacbfc.md) FUN_00bacbfc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00babb74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bab/00babb74.md) [`00bac9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac9dc.md) [`00baccbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00baccbc.md) · 呼出先 2件 [`00bac528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac528.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`00babf9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bab/00babf9c.md) [`00bace04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bac/00bace04.md) [`00bad0e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00bad0e4.md) · 呼出先 2件 [`00bac950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bac/00bac950.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 64.62% / 新版 64.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 20件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bac820"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bac848"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bac850"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bac820",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bacca8"
      ]
    ],
    [
      "unmatched:00bac854",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baccb0"
      ]
    ],
    [
      "unmatched:00bac870",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58050"
      ]
    ]
  ],
  "added": [
    [
      "00bacc48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bacca8"
      ]
    ],
    [
      "00bacc7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baccb0"
      ]
    ],
    [
      "00bacc98",
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

- 旧版 [`00bac820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac7d4.md#insn-00bac820) · [`00bac848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac7d4.md#insn-00bac848) · [`00bac850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bac7d4.md#insn-00bac850)

~~~diff
- 00bac820 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bac820 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00bac820 bytes 01030054
- 00bac848 ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00bac848 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bac848 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00bac848 ["COPY", "register:40e0:8", ["tmp:0:8"]]
- 00bac848 bytes bc018b9a
- 00bac850 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bac850 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bac850 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bac850 ["COPY", "tmp:1:8", ["register:40e0:8"]]
- 00bac850 bytes 62339c9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8515b7b84693160b846e53fa56d2e0d8"></a>

### [`00bad99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bad99c.md) → [`00baddc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00baddc4.md) FUN_00baddc4

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bacfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bacfd0.md) [`00badc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00badc48.md) [`00bae130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae130.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`00bad3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00bad3f8.md) [`00bae070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae070.md) [`00bae558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae558.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.18% / 新版 70.18%

CFGの説明率　旧版 38.57% / 新版 36.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bad99c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bad99c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bad9a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bad99c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bad9a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bad9a4",
      "WRITE",
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
      "00baddc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00baddc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00baddcc",
      "WRITE",
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

- 旧版 [`00bad99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bad99c.md#insn-00bad99c) · [`00bad9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bad99c.md#insn-00bad9a0) · [`00bad9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bad99c.md#insn-00bad9a4)

~~~diff
- 00bad99c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bad99c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bad99c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00bad99c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bad99c bytes fc6fbaa9
- 00bad9a0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bad9a0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bad9a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bad9a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bad9a0 bytes fa6701a9
- 00bad9a4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bad9a4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bad9a4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bad9a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bad9a4 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50db889f15bd8e40c20d5db84070404e"></a>

### [`00badc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00badc48.md) → [`00bae070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae070.md) FUN_00bae070

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bacfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bacfd0.md) [`00bade50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bade50.md) [`00bae130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae130.md) · 呼出先 2件 [`00bad99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bad99c.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 3件 [`00bad3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00bad3f8.md) [`00bae278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae278.md) [`00bae558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae558.md) · 呼出先 2件 [`00baddc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00baddc4.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 79.23% / 新版 79.23%

CFGの説明率　旧版 25.00% / 新版 28.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00badcb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00badcbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00badcc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00badcc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bae124"
      ]
    ],
    [
      "unmatched:00badce4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58050"
      ]
    ],
    [
      "unmatched:00badce8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bae124"
      ]
    ]
  ],
  "added": [
    [
      "00bae0f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bae124"
      ]
    ],
    [
      "00bae10c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58050"
      ]
    ],
    [
      "00bae110",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bae124"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00badcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00badc48.md#insn-00badcb4) · [`00badcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00badc48.md#insn-00badcbc) · [`00badcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00badc48.md#insn-00badcc4)

~~~diff
- 00badcb4 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00badcb4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00badcb4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00badcb4 ["COPY", "register:40d8:8", ["tmp:0:8"]]
- 00badcb4 bytes 9b018a9a
- 00badcbc ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00badcbc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00badcbc ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00badcbc ["COPY", "register:40e0:8", ["tmp:0:8"]]
- 00badcbc bytes bc018b9a
- 00badcc4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00badcc4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00badcc4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00badcc4 ["COPY", "tmp:1:8", ["register:40e0:8"]]
- 00badcc4 bytes 62339c9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb056b5ddf3b5ce29d06b26ce63595a4"></a>

### [`00bade50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bade50.md) → [`00bae278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae278.md) FUN_00bae278

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bacfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bacfd0.md) [`00bae130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae130.md) · 呼出先 2件 [`00badc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00badc48.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 2件 [`00bad3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00bad3f8.md) [`00bae558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae558.md) · 呼出先 2件 [`00bae070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae070.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 96.74% / 新版 96.74%

CFGの説明率　旧版 54.24% / 新版 54.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00baded8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae06c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae0dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bae06c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bae528"
      ]
    ],
    [
      "unmatched:00bae0e0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c58050"
      ]
    ]
  ],
  "added": [
    [
      "00bae494",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bae528"
      ]
    ],
    [
      "00bae508",
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

- 旧版 [`00baded8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bade50.md#insn-00baded8) · [`00bae06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bade50.md#insn-00bae06c) · [`00bae0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bade50.md#insn-00bae0dc)

~~~diff
- 00baded8 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00baded8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00baded8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00baded8 ["COPY", "register:40e0:8", ["tmp:0:8"]]
- 00baded8 bytes 9c018a9a
- 00bae06c ["CBRANCH", null, ["local:b33:8", "register:102:1"]]
- 00bae06c bytes a2040054
- 00bae0dc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bae0dc ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00bae0dc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00bae0dc ["INT_ADD", "tmp:1:8", ["register:40c0:8", "const:1:8"]]
- 00bae0dc bytes 6115989a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1cab17e458cdb686092bb11936991f2"></a>

### [`00bae130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae130.md) → [`00bae558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae558.md) FUN_00bae558

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bacfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bac/00bacfd0.md) · 呼出先 4件 [`00bad99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bad99c.md) [`00badc48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00badc48.md) [`00bade50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bad/00bade50.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00bad3f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00bad3f8.md) · 呼出先 4件 [`00baddc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bad/00baddc4.md) [`00bae070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae070.md) [`00bae278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00bae278.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.39% / 新版 92.39%

CFGの説明率　旧版 90.28% / 新版 90.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae294"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae354"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae35c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bae59c",
      "DATA",
      [
        "storage",
        "0030e1d2",
        "switchD_00bae180::switchdataD_0030e1d2",
        "byte"
      ]
    ],
    [
      "unmatched:00bae368",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bae7c0"
      ]
    ]
  ],
  "added": [
    [
      "00bae59c",
      "DATA",
      [
        "storage",
        "0030e212",
        "switchD_00bae5a8::switchdataD_0030e212",
        "byte"
      ]
    ],
    [
      "00bae790",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bae7c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bae294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae130.md#insn-00bae294) · [`00bae354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae130.md#insn-00bae354) · [`00bae35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00bae130.md#insn-00bae35c)

~~~diff
- 00bae294 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00bae294 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bae294 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bae294 ["COPY", "register:40b8:8", ["tmp:0:8"]]
- 00bae294 bytes 97018a9a
- 00bae354 ["COPY", "tmp:0:8", ["register:4060:8"]]
- 00bae354 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bae354 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bae354 ["COPY", "register:40e0:8", ["tmp:0:8"]]
- 00bae354 bytes 9c018a9a
- 00bae35c ["COPY", "tmp:0:8", ["register:4068:8"]]
- 00bae35c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bae35c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00bae35c ["COPY", "register:40a8:8", ["tmp:0:8"]]
- 00bae35c bytes b5018b9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5e07a0cde41791efe7a3eec8af85651"></a>

### [`00baea00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baea00.md) → [`00baee28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bae/00baee28.md) _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9f0.md) · 呼出先 5件 [`00baf09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf09c.md) [`00c5c7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c7f0.md) [`00c5c9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9b0.md) [`00c5c9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9f0.md) [`00c5ccb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccb0.md)
- 新版 呼出元 1件 [`00c5cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cdf0.md) · 呼出先 5件 [`00baf4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf4c4.md) [`00c5cbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cbf0.md) [`00c5cdb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cdb0.md) [`00c5cdf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cdf0.md) [`00c5d0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00baf1c4",
      "DATA",
      [
        "storage",
        "0030e1d8",
        "switchD_00baeda4::switchdataD_0030e1d8",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00baf1c4",
      "DATA",
      [
        "storage",
        "0030e218",
        "switchD_00baf1cc::switchdataD_0030e218",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baeaa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baea00.md#insn-00baeaa4) · [`00baeab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baea00.md#insn-00baeab8) · [`00baead4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bae/00baea00.md#insn-00baead4)
- 新版 `00baeecc`（命令位置の公開資料なし） · `00baeee0`（命令位置の公開資料なし） · `00baeefc`（命令位置の公開資料なし）

~~~diff
- 00baeaa4 ["INT_ADD", "register:40f0:8", ["const:baeaa4:8", "const:4:8"]]
- 00baeaa4 ["CALL", null, ["callee:00baf4c4:8"]]
+ 00baeecc ["INT_ADD", "register:40f0:8", ["const:baeecc:8", "const:4:8"]]
+ 00baeecc ["CALL", null, ["callee:00baf4c4:8"]]
- 00baeaa4 bytes 7e010094
+ 00baeecc bytes 7e010094
- 00baeab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baeab8 ["INT_ADD", "register:40f0:8", ["const:baeab8:8", "const:4:8"]]
- 00baeab8 ["CALLIND", null, ["register:0:8"]]
+ 00baeee0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baeee0 ["INT_ADD", "register:40f0:8", ["const:baeee0:8", "const:4:8"]]
+ 00baeee0 ["CALLIND", null, ["register:0:8"]]
- 00baeab8 bytes 00013fd6
+ 00baeee0 bytes 00013fd6
- 00baead4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00baead4 ["INT_ADD", "register:40f0:8", ["const:baead4:8", "const:4:8"]]
- 00baead4 ["CALLIND", null, ["register:0:8"]]
+ 00baeefc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baeefc ["INT_ADD", "register:40f0:8", ["const:baeefc:8", "const:4:8"]]
+ 00baeefc ["CALLIND", null, ["register:0:8"]]
- 00baead4 bytes 00013fd6
+ 00baeefc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4888734d386264d314be1917140cb04a"></a>

### [`00baf300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf300.md) → [`00baf728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf728.md) _ZNSt6__ndk127__insertion_sort_incompleteIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEbT0_SA_T_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5c9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5c9b0.md) · 呼出先 2件 [`00baf09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf09c.md) [`00c5ccb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ccb0.md)
- 新版 呼出元 1件 [`00c5cdb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cdb0.md) · 呼出先 2件 [`00baf4c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf4c4.md) [`00c5d0b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00baf768",
      "DATA",
      [
        "storage",
        "0030e1de",
        "switchD_00baf34c::switchdataD_0030e1de",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00baf768",
      "DATA",
      [
        "storage",
        "0030e21e",
        "switchD_00baf774::switchdataD_0030e21e",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf300.md#insn-00baf338) · [`00baf33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf300.md#insn-00baf33c) · [`00baf35c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf300.md#insn-00baf35c)
- 新版 `00baf760`（命令位置の公開資料なし） · `00baf784`（命令位置の公開資料なし）

~~~diff
- 00baf338 ["COPY", "tmp:0:8", ["const:1de:8"]]
- 00baf338 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00baf338 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00baf338 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00baf760 ["COPY", "tmp:0:8", ["const:21e:8"]]
+ 00baf760 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00baf760 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00baf760 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00baf338 bytes 29790791
+ 00baf760 bytes 29790891
- 00baf33c ["COPY", "register:4050:8", ["const:baf350:8"]]
- 00baf33c bytes aa000010
- 00baf35c ["COPY", "register:0:8", ["register:4040:8"]]
- 00baf35c ["INT_ADD", "register:40f0:8", ["const:baf35c:8", "const:4:8"]]
- 00baf35c ["CALLIND", null, ["register:0:8"]]
+ 00baf784 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00baf784 ["INT_ADD", "register:40f0:8", ["const:baf784:8", "const:4:8"]]
+ 00baf784 ["CALLIND", null, ["register:0:8"]]
- 00baf35c bytes 00013fd6
+ 00baf784 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc8c50638a872a14966e685b38a6adb3"></a>

### [`00baf5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf5b0.md) → [`00baf9d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00baf9d8.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ca70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca70.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ce70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ce70.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 60.87% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf5e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf5e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bafa0c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00baf5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf5b0.md#insn-00baf5e4) · [`00baf5e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf5b0.md#insn-00baf5e8) · [`00baf6c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf5b0.md#insn-00baf6c0)

~~~diff
- 00baf5e4 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00baf5e4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00baf5e4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00baf5e4 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 00baf5e4 bytes 7601899a
- 00baf5e8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00baf5e8 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00baf5e8 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00baf5e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "const:1:8"]]
- 00baf5e8 bytes 5515819a
- 00baf6c0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00baf6c0 ["RETURN", null, ["register:0:8"]]
- 00baf6c0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5805639db4419c957fef1e962bd51c4b"></a>

### [`00baf6c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf6c4.md) → [`00bafaec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00bafaec.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers10ServiceDefEEENS_19__map_val

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5ca60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ca60.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5ce60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5ce60.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 87.10% / 新版 84.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf720"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bafb48"
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
      "unmatched:00baf720",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bafbd4"
      ]
    ]
  ],
  "added": [
    [
      "00bafb48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bafbd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf6c4.md#insn-00baf720) · [`00baf6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf6c4.md#insn-00baf6ec)
- 新版 `00bafb48`（命令位置の公開資料なし） · `00bafb14`（命令位置の公開資料なし）

~~~diff
- 00baf720 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00baf720 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00baf720 bytes 680400b4
+ 00bafb48 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00bafb48 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 00bafb48 bytes 680400b4
- 00baf6ec ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00baf6ec ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 00bafb14 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
+ 00bafb14 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00baf6ec bytes 570600b4
+ 00bafb14 bytes 570600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cae7808a85a5b8c9b68963cfe66048a"></a>

### [`00baf8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf8f8.md) → [`00bafd20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00bafd20.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7RPCCallEEENS_19__map_value_c

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5cb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cb20.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cf20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cf20.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 47.06% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf93c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf948"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf954"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00baf940",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00baf95c"
      ]
    ],
    [
      "unmatched:00baf948",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bafe08"
      ]
    ],
    [
      "unmatched:00baf954",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bafe08"
      ]
    ]
  ],
  "added": [
    [
      "00bafd68",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00bafd84"
      ]
    ],
    [
      "00bafd70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bafe08"
      ]
    ],
    [
      "00bafd7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bafe08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf8f8.md#insn-00baf93c) · [`00baf948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf8f8.md#insn-00baf948) · [`00baf954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf8f8.md#insn-00baf954)

~~~diff
- 00baf93c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00baf93c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00baf93c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00baf93c ["INT_ADD", "tmp:1:8", ["register:4010:8", "const:1:8"]]
- 00baf93c bytes 5515829a
- 00baf948 ["CBRANCH", null, ["local:b20:8", "register:102:1"]]
- 00baf948 bytes c2040054
- 00baf954 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00baf954 ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 00baf954 bytes 680400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673c4026a72c0206275cee049d007f4f"></a>

### [`00bafa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00bafa18.md) → [`00bafe40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00baf/00bafe40.md) _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_c

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00c5caf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5caf0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 1件 [`00c5cef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5c/00c5cef0.md) · 呼出先 1件 [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 91.30% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bafa34"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bafe5c"
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
      "unmatched:00bafa34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baff38"
      ]
    ]
  ],
  "added": [
    [
      "00bafe5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00baff38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bafa34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00bafa18.md#insn-00bafa34) · [`00bafa30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00bafa18.md#insn-00bafa30)
- 新版 `00bafe5c`（命令位置の公開資料なし）

~~~diff
- 00bafa34 ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
- 00bafa34 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00bafa34 bytes f70600b4
+ 00bafe5c ["INT_EQUAL", "tmp:0:1", ["register:40b8:8", "const:0:8"]]
+ 00bafe5c ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
+ 00bafe5c bytes f70600b4
- 00bafa30 ["INT_ADD", "register:4098:8", ["register:4098:8", "const:8:8"]]
- 00bafa30 ["LOAD", "register:40b8:8", ["const:1b1:8", "register:4098:8"]]
- 00bafa30 bytes 778e40f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

