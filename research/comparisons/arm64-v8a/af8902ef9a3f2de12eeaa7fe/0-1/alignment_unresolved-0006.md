# v15.7.3 → v15.7.4 · 命令位置の検査未完了 (6)

[一覧の目次](README.md)

<a id="compare-8e758d9ccf51d16130c69992e1dac03d"></a>

### [`00be0230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0230.md) → [`00be0280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0280.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b47b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b58.md) [`00b88a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b88/00b88a90.md) · 呼出先 1件 [`00b47f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47f30.md)
- 新版 呼出元 2件 [`00b47b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47b9c.md) [`00b88ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b88/00b88ad4.md) · 呼出先 1件 [`00b47f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f74.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

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
        "00c1e9a8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be023c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b47f74"
      ]
    ]
  ],
  "added": [
    [
      "00be0284",
      "READ",
      [
        "storage",
        "00c1e9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00be028c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b47f74"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0230.md#insn-00be0234) · [`00be0238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0230.md#insn-00be0238) · [`00be023c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0230.md#insn-00be023c)

~~~diff
- 00be0234 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9a8:8"]]
- 00be0234 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0234 bytes 11d644f9
- 00be0238 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 00be0238 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0238 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0238 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0238 bytes 10a22691
- 00be023c ["COPY", "register:0:8", ["register:4088:8"]]
- 00be023c ["BRANCHIND", null, ["register:0:8"]]
- 00be023c bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25b0ee07ba83e6212a0ced447859fed8"></a>

### [`00be0240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0240.md) → [`00be0290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0290.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEEC2Ev

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b46598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46598.md) [`00b46718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md) [`00b46ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46ee0.md) · 呼出先 1件 [`00b4890c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b4890c.md)
- 新版 呼出元 3件 [`00b465dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b465dc.md) [`00b4675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4675c.md) [`00b46f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46f24.md) · 呼出先 1件 [`00b48950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48950.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0244",
      "READ",
      [
        "storage",
        "00c1e9b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be024c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48950"
      ]
    ]
  ],
  "added": [
    [
      "00be0294",
      "READ",
      [
        "storage",
        "00c1ea00",
        null,
        "pointer"
      ]
    ],
    [
      "00be029c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48950"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0240.md#insn-00be0240) · [`00be0244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0240.md#insn-00be0244) · [`00be0248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0240.md#insn-00be0248)

~~~diff
- 00be0240 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0240 bytes f00100d0
- 00be0244 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9b0:8"]]
- 00be0244 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0244 bytes 11da44f9
- 00be0248 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 00be0248 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0248 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0248 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0248 bytes 10c22691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b75ad5b50d59f34fed7c82e6e0cb8f6"></a>

### [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md) → [`00be02a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02a0.md) _ZNSt6__ndk113basic_filebufIcNS_11char_traitsIcEEED2Ev

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`00b46598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46598.md) [`00b466dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b466dc.md) [`00b46718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md) [`00b46ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46ee0.md) [`00b47150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47150.md) · 呼出先 1件 [`00b47b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b58.md)
- 新版 呼出元 12件 [`00b465dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b465dc.md) [`00b46720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46720.md) [`00b4675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4675c.md) [`00b46f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46f24.md) [`00b47194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47194.md) · 呼出先 1件 [`00b47b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47b9c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0254",
      "READ",
      [
        "storage",
        "00c1e9b8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be025c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b47b9c"
      ]
    ]
  ],
  "added": [
    [
      "00be02a4",
      "READ",
      [
        "storage",
        "00c1ea08",
        null,
        "pointer"
      ]
    ],
    [
      "00be02ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b47b9c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md#insn-00be0250) · [`00be0254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md#insn-00be0254) · [`00be0258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md#insn-00be0258)

~~~diff
- 00be0250 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0250 bytes f00100d0
- 00be0254 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9b8:8"]]
- 00be0254 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0254 bytes 11de44f9
- 00be0258 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 00be0258 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0258 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0258 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0258 bytes 10e22691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef7facc49ec7fb5fadc1271f11cf7e01"></a>

### [`00be0260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0260.md) → [`00be02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02b0.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b46718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md) · 呼出先 1件 [`00b46cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46cc8.md)
- 新版 呼出元 1件 [`00b4675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4675c.md) · 呼出先 1件 [`00b46d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46d0c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0264",
      "READ",
      [
        "storage",
        "00c1e9c0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be026c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b46d0c"
      ]
    ]
  ],
  "added": [
    [
      "00be02b4",
      "READ",
      [
        "storage",
        "00c1ea10",
        null,
        "pointer"
      ]
    ],
    [
      "00be02bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b46d0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0260.md#insn-00be0260) · [`00be0264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0260.md#insn-00be0264) · [`00be0268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0260.md#insn-00be0268)

~~~diff
- 00be0260 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0260 bytes f00100d0
- 00be0264 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9c0:8"]]
- 00be0264 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0264 bytes 11e244f9
- 00be0268 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00be0268 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0268 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0268 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0268 bytes 10022791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-283a1cea59d291d0d72b7c85c9e38be5"></a>

### [`00be0270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0270.md) → [`00be02c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02c0.md) &lt;EXTERNAL&gt;::fseeko

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b47e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47e00.md) [`00b47ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47ec0.md) [`00b47f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47f30.md) · 呼出先 1件 [`010a5668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5668.md)
- 新版 呼出元 3件 [`00b47e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md) [`00b47f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f04.md) [`00b47f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47f74.md) · 呼出先 1件 [`010a5668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5668.md)

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
        "00c1e9c8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be027c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5668"
      ]
    ]
  ],
  "added": [
    [
      "00be02c4",
      "READ",
      [
        "storage",
        "00c1ea18",
        null,
        "pointer"
      ]
    ],
    [
      "00be02cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5668"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0270.md#insn-00be0270) · [`00be0274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0270.md#insn-00be0274) · [`00be0278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0270.md#insn-00be0278)

~~~diff
- 00be0270 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0270 bytes f00100d0
- 00be0274 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9c8:8"]]
- 00be0274 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0274 bytes 11e644f9
- 00be0278 ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00be0278 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0278 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0278 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0278 bytes 10222791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-729be25746e7313a582d21bdc253ba27"></a>

### [`00be0280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0280.md) → [`00be02d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02d0.md) &lt;EXTERNAL&gt;::ftello

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b47e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47e00.md) · 呼出先 1件 [`010a5670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5670.md)
- 新版 呼出元 1件 [`00b47e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47e44.md) · 呼出先 1件 [`010a5670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5670.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

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
        "00c1e9d0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be028c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5670"
      ]
    ]
  ],
  "added": [
    [
      "00be02d4",
      "READ",
      [
        "storage",
        "00c1ea20",
        null,
        "pointer"
      ]
    ],
    [
      "00be02dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5670"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0280.md#insn-00be0280) · [`00be0284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0280.md#insn-00be0284) · [`00be0288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0280.md#insn-00be0288)

~~~diff
- 00be0280 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0280 bytes f00100d0
- 00be0284 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9d0:8"]]
- 00be0284 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0284 bytes 11ea44f9
- 00be0288 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00be0288 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0288 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0288 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0288 bytes 10422791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e57e74264557e6ce34d97c83b3b7324"></a>

### [`00be0290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0290.md) → [`00be02e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02e0.md) &lt;EXTERNAL&gt;::realpath

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4778c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b4778c.md) · 呼出先 1件 [`010a5678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5678.md)
- 新版 呼出元 1件 [`00b477d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b477d0.md) · 呼出先 1件 [`010a5678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5678.md)

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
        "00c1e9d8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be029c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5678"
      ]
    ]
  ],
  "added": [
    [
      "00be02e4",
      "READ",
      [
        "storage",
        "00c1ea28",
        null,
        "pointer"
      ]
    ],
    [
      "00be02ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5678"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0290.md#insn-00be0290) · [`00be0294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0290.md#insn-00be0294) · [`00be0298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0290.md#insn-00be0298)

~~~diff
- 00be0290 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0290 bytes f00100d0
- 00be0294 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9d8:8"]]
- 00be0294 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0294 bytes 11ee44f9
- 00be0298 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 00be0298 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0298 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0298 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0298 bytes 10622791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd6a5d1abdb24669edbf4b29a75e411a"></a>

### [`00be02a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02a0.md) → [`00be02f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02f0.md) &lt;EXTERNAL&gt;::setlocale

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b47878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47878.md) [`00ba84f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba84f4.md) · 呼出先 1件 [`010a5680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5680.md)
- 新版 呼出元 2件 [`00b478bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b478bc.md) [`00ba8538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8538.md) · 呼出先 1件 [`010a5680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5680.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be02a4",
      "READ",
      [
        "storage",
        "00c1e9e0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be02ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5680"
      ]
    ]
  ],
  "added": [
    [
      "00be02f4",
      "READ",
      [
        "storage",
        "00c1ea30",
        null,
        "pointer"
      ]
    ],
    [
      "00be02fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "010a5680"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be02a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02a0.md#insn-00be02a0) · [`00be02a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02a0.md#insn-00be02a4) · [`00be02a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02a0.md#insn-00be02a8)

~~~diff
- 00be02a0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be02a0 bytes f00100d0
- 00be02a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9e0:8"]]
- 00be02a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be02a4 bytes 11f244f9
- 00be02a8 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 00be02a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be02a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be02a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be02a8 bytes 10822791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fddbafb7d43a220283ff026e96c3295e"></a>

### [`00be02d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02d0.md) → [`00be0320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0320.md) _ZN8firebase9messaging10FutureData7DestroyEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4ce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md) · 呼出先 1件 [`00b4947c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b4947c.md)
- 新版 呼出元 1件 [`00b4ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4ced4.md) · 呼出先 1件 [`00b494c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b494c0.md)

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
        "00c1e9f8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be02dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b494c0"
      ]
    ]
  ],
  "added": [
    [
      "00be0324",
      "READ",
      [
        "storage",
        "00c1ea48",
        null,
        "pointer"
      ]
    ],
    [
      "00be032c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b494c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be02d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02d0.md#insn-00be02d0) · [`00be02d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02d0.md#insn-00be02d4) · [`00be02d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02d0.md#insn-00be02d8)

~~~diff
- 00be02d0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be02d0 bytes f00100d0
- 00be02d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9f8:8"]]
- 00be02d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be02d4 bytes 11fe44f9
- 00be02d8 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00be02d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be02d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be02d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be02d8 bytes 10e22791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f66f82cea70b2f1f8e656f2c2cd7177a"></a>

### [`00be02f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02f0.md) → [`00be0340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0340.md) _ZN8firebase9messaging11SetListenerEPNS0_8ListenerE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b48d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48d8c.md) [`00b4ce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md) · 呼出先 1件 [`00b48c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c44.md)
- 新版 呼出元 2件 [`00b48dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48dd0.md) [`00b4ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4ced4.md) · 呼出先 1件 [`00b48c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c88.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be02f4",
      "READ",
      [
        "storage",
        "00c1ea08",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be02fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48c88"
      ]
    ]
  ],
  "added": [
    [
      "00be0344",
      "READ",
      [
        "storage",
        "00c1ea58",
        null,
        "pointer"
      ]
    ],
    [
      "00be034c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48c88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be02f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02f0.md#insn-00be02f0) · [`00be02f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02f0.md#insn-00be02f4) · [`00be02f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02f0.md#insn-00be02f8)

~~~diff
- 00be02f0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be02f0 bytes f00100d0
- 00be02f4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a08:8"]]
- 00be02f4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be02f4 bytes 110645f9
- 00be02f8 ["COPY", "tmp:0:8", ["const:a08:8"]]
- 00be02f8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be02f8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be02f8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be02f8 bytes 10222891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cc9651376409a276582800af2a56590"></a>

### [`00be0300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0300.md) → [`00be0350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0350.md) _ZN8firebase9messaging12NotificationC2ERKS1_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b49acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49acc.md) · 呼出先 1件 [`00b49cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49cfc.md)
- 新版 呼出元 1件 [`00b49b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49b10.md) · 呼出先 1件 [`00b49d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49d40.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0304",
      "READ",
      [
        "storage",
        "00c1ea10",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be030c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49d40"
      ]
    ]
  ],
  "added": [
    [
      "00be0354",
      "READ",
      [
        "storage",
        "00c1ea60",
        null,
        "pointer"
      ]
    ],
    [
      "00be035c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49d40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0300.md#insn-00be0300) · [`00be0304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0300.md#insn-00be0304) · [`00be0308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0300.md#insn-00be0308)

~~~diff
- 00be0300 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0300 bytes f00100d0
- 00be0304 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a10:8"]]
- 00be0304 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0304 bytes 110a45f9
- 00be0308 ["COPY", "tmp:0:8", ["const:a10:8"]]
- 00be0308 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0308 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0308 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0308 bytes 10422891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d75e3dfee6bd1773f8df2d2696ea2b16"></a>

### [`00be0330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0330.md) → [`00be0380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0380.md) _ZN8firebase9messaging16PollableListenerD1Ev

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b49074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49074.md) · 呼出先 1件 [`00b48fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48fb8.md)
- 新版 呼出元 1件 [`00b490b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490b8.md) · 呼出先 1件 [`00b48ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48ffc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0334",
      "READ",
      [
        "storage",
        "00c1ea28",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be033c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48ffc"
      ]
    ]
  ],
  "added": [
    [
      "00be0384",
      "READ",
      [
        "storage",
        "00c1ea78",
        null,
        "pointer"
      ]
    ],
    [
      "00be038c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48ffc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0330.md#insn-00be0330) · [`00be0334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0330.md#insn-00be0334) · [`00be0338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0330.md#insn-00be0338)

~~~diff
- 00be0330 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0330 bytes f00100d0
- 00be0334 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a28:8"]]
- 00be0334 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0334 bytes 111645f9
- 00be0338 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 00be0338 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0338 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0338 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0338 bytes 10a22891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-762bbc882ab96e9fb46f4c3db6a7d7d0"></a>

### [`00be0340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0340.md) → [`00be0390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0390.md) _ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b48c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c44.md) · 呼出先 1件 [`00b4b59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b59c.md)
- 新版 呼出元 1件 [`00b48c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c88.md) · 呼出先 1件 [`00b4b5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b5e0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0344",
      "READ",
      [
        "storage",
        "00c1ea30",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be034c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4b5e0"
      ]
    ]
  ],
  "added": [
    [
      "00be0394",
      "READ",
      [
        "storage",
        "00c1ea80",
        null,
        "pointer"
      ]
    ],
    [
      "00be039c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4b5e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0340.md#insn-00be0340) · [`00be0344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0340.md#insn-00be0344) · [`00be0348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0340.md#insn-00be0348)

~~~diff
- 00be0340 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0340 bytes f00100d0
- 00be0344 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a30:8"]]
- 00be0344 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0344 bytes 111a45f9
- 00be0348 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00be0348 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0348 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0348 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0348 bytes 10c22891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f40c72997e1df372fcd3e8c303e49c"></a>

### [`00be0350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0350.md) → [`00be03a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03a0.md) _ZN8firebase9messaging20PollableListenerImpl11PollMessageEPNS0_7MessageE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b49220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49220.md) · 呼出先 1件 [`00b49228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49228.md)
- 新版 呼出元 1件 [`00b49264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49264.md) · 呼出先 1件 [`00b4926c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4926c.md)

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
        "00c1ea38",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be035c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4926c"
      ]
    ]
  ],
  "added": [
    [
      "00be03a4",
      "READ",
      [
        "storage",
        "00c1ea88",
        null,
        "pointer"
      ]
    ],
    [
      "00be03ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4926c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0350.md#insn-00be0350) · [`00be0354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0350.md#insn-00be0354) · [`00be0358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0350.md#insn-00be0358)

~~~diff
- 00be0350 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0350 bytes f00100d0
- 00be0354 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a38:8"]]
- 00be0354 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0354 bytes 111e45f9
- 00be0358 ["COPY", "tmp:0:8", ["const:a38:8"]]
- 00be0358 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0358 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0358 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0358 bytes 10e22891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3df3013e3ecca021d1dafe43ef695ba5"></a>

### [`00be0390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0390.md) → [`00be03e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03e0.md) _ZN8firebase9messaging20SetListenerIfNotNullEPNS0_8ListenerE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4c480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md) · 呼出先 1件 [`00b48d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48d8c.md)
- 新版 呼出元 1件 [`00b4c4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4c4c4.md) · 呼出先 1件 [`00b48dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48dd0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

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
        "00c1ea58",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be039c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48dd0"
      ]
    ]
  ],
  "added": [
    [
      "00be03e4",
      "READ",
      [
        "storage",
        "00c1eaa8",
        null,
        "pointer"
      ]
    ],
    [
      "00be03ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48dd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0390.md#insn-00be0390) · [`00be0394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0390.md#insn-00be0394) · [`00be0398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0390.md#insn-00be0398)

~~~diff
- 00be0390 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0390 bytes f00100d0
- 00be0394 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a58:8"]]
- 00be0394 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0394 bytes 112e45f9
- 00be0398 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00be0398 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0398 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0398 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0398 bytes 10622991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-963a0436c1130410ca7556ee6888614a"></a>

### [`00be03a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03a0.md) → [`00be03f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03f0.md) _ZN8firebase9messaging23NotifyListenerOnMessageERKNS0_7MessageE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4b884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b884.md) [`00b4e898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e898.md) · 呼出先 1件 [`00b48da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48da0.md)
- 新版 呼出元 2件 [`00b4b8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b8c8.md) [`00b4e8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e8dc.md) · 呼出先 1件 [`00b48de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48de4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be03a4",
      "READ",
      [
        "storage",
        "00c1ea60",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be03ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48de4"
      ]
    ]
  ],
  "added": [
    [
      "00be03f4",
      "READ",
      [
        "storage",
        "00c1eab0",
        null,
        "pointer"
      ]
    ],
    [
      "00be03fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48de4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be03a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03a0.md#insn-00be03a0) · [`00be03a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03a0.md#insn-00be03a4) · [`00be03a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03a0.md#insn-00be03a8)

~~~diff
- 00be03a0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be03a0 bytes f00100d0
- 00be03a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a60:8"]]
- 00be03a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be03a4 bytes 113245f9
- 00be03a8 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00be03a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be03a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be03a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be03a8 bytes 10822991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9beba28b8b99a155ce91bc835cf488ed"></a>

### [`00be03b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03b0.md) → [`00be0400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0400.md) _ZN8firebase9messaging29NotifyListenerOnTokenReceivedEPKc

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b4e89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e89c.md) [`00b4ea4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ea4c.md) · 呼出先 1件 [`00b48e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48e10.md)
- 新版 呼出元 2件 [`00b4e8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e8e0.md) [`00b4ea90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ea90.md) · 呼出先 1件 [`00b48e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48e54.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be03b4",
      "READ",
      [
        "storage",
        "00c1ea68",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be03bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48e54"
      ]
    ]
  ],
  "added": [
    [
      "00be0404",
      "READ",
      [
        "storage",
        "00c1eab8",
        null,
        "pointer"
      ]
    ],
    [
      "00be040c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b48e54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be03b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03b0.md#insn-00be03b0) · [`00be03b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03b0.md#insn-00be03b4) · [`00be03b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03b0.md#insn-00be03b8)

~~~diff
- 00be03b0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be03b0 bytes f00100d0
- 00be03b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a68:8"]]
- 00be03b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be03b4 bytes 113645f9
- 00be03b8 ["COPY", "tmp:0:8", ["const:a68:8"]]
- 00be03b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be03b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be03b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be03b8 bytes 10a22991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ad316d444689c9a47b4f9cb75605b10"></a>

### [`00be03d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03d0.md) → [`00be0420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0420.md) _ZN8firebase9messaging7MessageD2Ev

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00b490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b490a0.md) [`00b49228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49228.md) [`00b494f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494f4.md) [`00b4b884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b884.md) [`00b4f0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4f/00b4f0b4.md) · 呼出先 1件 [`00b4960c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b4960c.md)
- 新版 呼出元 5件 [`00b490e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490e4.md) [`00b4926c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4926c.md) [`00b49538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49538.md) [`00b4b8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b8c8.md) [`00b4f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4f/00b4f0f8.md) · 呼出先 1件 [`00b49650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49650.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be03d4",
      "READ",
      [
        "storage",
        "00c1ea78",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be03dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49650"
      ]
    ]
  ],
  "added": [
    [
      "00be0424",
      "READ",
      [
        "storage",
        "00c1eac8",
        null,
        "pointer"
      ]
    ],
    [
      "00be042c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49650"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be03d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03d0.md#insn-00be03d0) · [`00be03d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03d0.md#insn-00be03d4) · [`00be03d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03d0.md#insn-00be03d8)

~~~diff
- 00be03d0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be03d0 bytes f00100d0
- 00be03d4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:a78:8"]]
- 00be03d4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be03d4 bytes 113e45f9
- 00be03d8 ["COPY", "tmp:0:8", ["const:a78:8"]]
- 00be03d8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be03d8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be03d8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be03d8 bytes 10e22991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6881679ea489ef4ef6451cb419ae2186"></a>

### [`00be0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0420.md) → [`00be0470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0470.md) _ZN8firebase9messaging9TerminateEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b48b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48b90.md) [`00b494c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494c8.md) · 呼出先 1件 [`00b4ce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md)
- 新版 呼出元 2件 [`00b48bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48bd4.md) [`00b4950c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b4950c.md) · 呼出先 1件 [`00b4ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4ced4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

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
        "00c1eaa0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be042c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4ced4"
      ]
    ]
  ],
  "added": [
    [
      "00be0474",
      "READ",
      [
        "storage",
        "00c1eaf0",
        null,
        "pointer"
      ]
    ],
    [
      "00be047c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4ced4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0420.md#insn-00be0420) · [`00be0424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0420.md#insn-00be0424) · [`00be0428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0420.md#insn-00be0428)

~~~diff
- 00be0420 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0420 bytes f00100d0
- 00be0424 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:aa0:8"]]
- 00be0424 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0424 bytes 115245f9
- 00be0428 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00be0428 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0428 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0428 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0428 bytes 10822a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a4ad5b7d7daca2b26f0853a9ab1dde2"></a>

### [`00be0440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0440.md) → [`00be0490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0490.md) _ZNSt6__ndk112__deque_baseIN8firebase9messaging7MessageENS_9allocatorIS3_EEE5clearEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b48fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48fb8.md) · 呼出先 1件 [`00b494f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b494f4.md)
- 新版 呼出元 1件 [`00b48ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48ffc.md) · 呼出先 1件 [`00b49538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49538.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0444",
      "READ",
      [
        "storage",
        "00c1eab0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be044c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49538"
      ]
    ]
  ],
  "added": [
    [
      "00be0494",
      "READ",
      [
        "storage",
        "00c1eb00",
        null,
        "pointer"
      ]
    ],
    [
      "00be049c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49538"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0440.md#insn-00be0440) · [`00be0444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0440.md#insn-00be0444) · [`00be0448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0440.md#insn-00be0448)

~~~diff
- 00be0440 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0440 bytes f00100d0
- 00be0444 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ab0:8"]]
- 00be0444 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0444 bytes 115a45f9
- 00be0448 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00be0448 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0448 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0448 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0448 bytes 10c22a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-334d4223a244239e22c8cfe086736927"></a>

### [`00be0450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0450.md) → [`00be04a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04a0.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE10push_frontEOS4_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md) · 呼出先 1件 [`00b4a698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a698.md)
- 新版 呼出元 1件 [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md) · 呼出先 1件 [`00b4a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a6dc.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0454",
      "READ",
      [
        "storage",
        "00c1eab8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be045c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a6dc"
      ]
    ]
  ],
  "added": [
    [
      "00be04a4",
      "READ",
      [
        "storage",
        "00c1eb08",
        null,
        "pointer"
      ]
    ],
    [
      "00be04ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a6dc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0450.md#insn-00be0450) · [`00be0454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0450.md#insn-00be0454) · [`00be0458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0450.md#insn-00be0458)

~~~diff
- 00be0450 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0450 bytes f00100d0
- 00be0454 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ab8:8"]]
- 00be0454 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0454 bytes 115e45f9
- 00be0458 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 00be0458 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0458 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0458 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0458 bytes 10e22a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-811098a35a2b06839e6b21329328875b"></a>

### [`00be0460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0460.md) → [`00be04b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04b0.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md) · 呼出先 1件 [`00b4a558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a558.md)
- 新版 呼出元 1件 [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md) · 呼出先 1件 [`00b4a59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a59c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0464",
      "READ",
      [
        "storage",
        "00c1eac0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be046c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a59c"
      ]
    ]
  ],
  "added": [
    [
      "00be04b4",
      "READ",
      [
        "storage",
        "00c1eb10",
        null,
        "pointer"
      ]
    ],
    [
      "00be04bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a59c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0460.md#insn-00be0460) · [`00be0464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0460.md#insn-00be0464) · [`00be0468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0460.md#insn-00be0468)

~~~diff
- 00be0460 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0460 bytes f00100d0
- 00be0464 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ac0:8"]]
- 00be0464 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0464 bytes 116245f9
- 00be0468 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 00be0468 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0468 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0468 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0468 bytes 10022b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-673456f340cf0d3d806425c38c730130"></a>

### [`00be0470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0470.md) → [`00be04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04c0.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE10push_frontERKS4_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md) · 呼出先 1件 [`00b4a918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a918.md)
- 新版 呼出元 1件 [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md) · 呼出先 1件 [`00b4a95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a95c.md)

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
        "00c1eac8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be047c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a95c"
      ]
    ]
  ],
  "added": [
    [
      "00be04c4",
      "READ",
      [
        "storage",
        "00c1eb18",
        null,
        "pointer"
      ]
    ],
    [
      "00be04cc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a95c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0470.md#insn-00be0470) · [`00be0474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0470.md#insn-00be0474) · [`00be0478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0470.md#insn-00be0478)

~~~diff
- 00be0470 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0470 bytes f00100d0
- 00be0474 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ac8:8"]]
- 00be0474 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0474 bytes 116645f9
- 00be0478 ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00be0478 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0478 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0478 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0478 bytes 10222b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb3dd82e708823b73da30ea5ae48eead"></a>

### [`00be0480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0480.md) → [`00be04d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04d0.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md) · 呼出先 1件 [`00b4a7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a7d8.md)
- 新版 呼出元 1件 [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md) · 呼出先 1件 [`00b4a81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a81c.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

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
        "00c1ead0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be048c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a81c"
      ]
    ]
  ],
  "added": [
    [
      "00be04d4",
      "READ",
      [
        "storage",
        "00c1eb20",
        null,
        "pointer"
      ]
    ],
    [
      "00be04dc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a81c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0480.md#insn-00be0480) · [`00be0484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0480.md#insn-00be0484) · [`00be0488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0480.md#insn-00be0488)

~~~diff
- 00be0480 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be0480 bytes f00100d0
- 00be0484 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ad0:8"]]
- 00be0484 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0484 bytes 116a45f9
- 00be0488 ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 00be0488 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0488 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0488 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0488 bytes 10422b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79b081043b25bfd662fc1bc625868b90"></a>

### [`00be0490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0490.md) → [`00be04e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04e0.md) _ZNSt6__ndk15dequeIN8firebase9messaging7MessageENS_9allocatorIS3_EEE19__add_back_capacityEv

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00b490a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b490a0.md) · 呼出先 1件 [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md)
- 新版 呼出元 1件 [`00b490e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b490e4.md) · 呼出先 1件 [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be0494",
      "READ",
      [
        "storage",
        "00c1ead8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be049c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a248"
      ]
    ]
  ],
  "added": [
    [
      "00be04e4",
      "READ",
      [
        "storage",
        "00c1eb28",
        null,
        "pointer"
      ]
    ],
    [
      "00be04ec",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b4a248"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be0494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0490.md#insn-00be0494) · [`00be0498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0490.md#insn-00be0498) · [`00be049c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0490.md#insn-00be049c)

~~~diff
- 00be0494 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ad8:8"]]
- 00be0494 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be0494 bytes 116e45f9
- 00be0498 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 00be0498 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be0498 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be0498 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be0498 bytes 10622b91
- 00be049c ["COPY", "register:0:8", ["register:4088:8"]]
- 00be049c ["BRANCHIND", null, ["register:0:8"]]
- 00be049c bytes 20021fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4de2b2b22247dd6363f5ee44fc3c22f3"></a>

### [`00be04a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04a0.md) → [`00be04f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04f0.md) _ZNSt6__ndk16vectorIhNS_9allocatorIhEEE6assignIPhEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIhNS_15iterator_

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b49acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49acc.md) · 呼出先 1件 [`00b49eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b49/00b49eec.md)
- 新版 呼出元 1件 [`00b49b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49b10.md) · 呼出先 1件 [`00b49f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b49/00b49f30.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

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
        "00c1eae0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be04ac",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49f30"
      ]
    ]
  ],
  "added": [
    [
      "00be04f4",
      "READ",
      [
        "storage",
        "00c1eb30",
        null,
        "pointer"
      ]
    ],
    [
      "00be04fc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b49f30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be04a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04a0.md#insn-00be04a0) · [`00be04a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04a0.md#insn-00be04a4) · [`00be04a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04a0.md#insn-00be04a8)

~~~diff
- 00be04a0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be04a0 bytes f00100d0
- 00be04a4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ae0:8"]]
- 00be04a4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be04a4 bytes 117245f9
- 00be04a8 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 00be04a8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be04a8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be04a8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be04a8 bytes 10822b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7344cbf4816658397cae47a765c26db5"></a>

### [`00be04b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04b0.md) → [`00be0500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0500.md) _ZNK3com6google8firebase9messaging3cpp15SerializedEvent6VerifyERN11flatbuffers8VerifierE

採用 · 移動量 `+0x50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b4ee88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ee88.md) · 呼出先 1件 [`00b5020c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b50/00b5020c.md)
- 新版 呼出元 1件 [`00b4eecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4eecc.md) · 呼出先 1件 [`00b50250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b50/00b50250.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00be04b4",
      "READ",
      [
        "storage",
        "00c1eae8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00be04bc",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b50250"
      ]
    ]
  ],
  "added": [
    [
      "00be0504",
      "READ",
      [
        "storage",
        "00c1eb38",
        null,
        "pointer"
      ]
    ],
    [
      "00be050c",
      "COMPUTED_CALL",
      [
        "mapped_function",
        "00b50250"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be04b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04b0.md#insn-00be04b0) · [`00be04b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04b0.md#insn-00be04b4) · [`00be04b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be04b0.md#insn-00be04b8)

~~~diff
- 00be04b0 ["COPY", "register:4080:8", ["const:c1e000:8"]]
- 00be04b0 bytes f00100d0
- 00be04b4 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:ae8:8"]]
- 00be04b4 ["LOAD", "register:4088:8", ["const:1b1:8", "tmp:0:8"]]
- 00be04b4 bytes 117645f9
- 00be04b8 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 00be04b8 ["INT_CARRY", "register:105:1", ["register:4080:8", "tmp:0:8"]]
- 00be04b8 ["INT_SCARRY", "register:106:1", ["register:4080:8", "tmp:0:8"]]
- 00be04b8 ["INT_ADD", "tmp:1:8", ["register:4080:8", "tmp:0:8"]]
- 00be04b8 bytes 10a22b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

