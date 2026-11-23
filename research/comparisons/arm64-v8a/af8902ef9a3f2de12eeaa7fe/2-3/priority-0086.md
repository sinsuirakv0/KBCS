# v16.0.0 → v16.0.1 · 最優先の変更候補 (86)

[一覧の目次](README.md)

<a id="compare-f3a3d96a38af6b28c2cae3cc19f9193e"></a>

### [`00be3af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md) → [`00be3f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f20.md) FUN_00be3f20

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be3ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3ad8.md) [`00be3af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md) · 呼出先 4件 [`00be3af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md) [`00bea758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00bea758.md) [`00beaa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beaa18.md) [`00beab40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beab40.md)
- 新版 呼出元 2件 [`00be3f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f00.md) [`00be3f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f20.md) · 呼出先 4件 [`00be3f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be3/00be3f20.md) [`00beab80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00beab80.md) [`00beae40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00beae40.md) [`00beaf68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00beaf68.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.56% / 新版 99.56%

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
      "site": "00be42b0",
      "value": [
        "leaf",
        "ram:beab80:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be3e88",
      "value": [
        "leaf",
        "ram:bea758:8"
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
      "site": "00be42c4",
      "value": [
        "leaf",
        "ram:beab80:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be3e9c",
      "value": [
        "leaf",
        "ram:bea758:8"
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
      "00be42b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bea758"
      ]
    ],
    [
      "00be42c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bea758"
      ]
    ]
  ],
  "added": [
    [
      "00be42b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beab80"
      ]
    ],
    [
      "00be42c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beab80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be3e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md#insn-00be3e88) · [`00be3e9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md#insn-00be3e9c) · [`00be3eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be3/00be3af8.md#insn-00be3eb8)
- 新版 `00be42b0`（命令位置の公開資料なし） · `00be42c4`（命令位置の公開資料なし） · `00be42e0`（命令位置の公開資料なし）

~~~diff
- 00be3e88 ["INT_ADD", "register:40f0:8", ["const:be3e88:8", "const:4:8"]]
- 00be3e88 ["CALL", null, ["ram:bea758:8"]]
+ 00be42b0 ["INT_ADD", "register:40f0:8", ["const:be42b0:8", "const:4:8"]]
+ 00be42b0 ["CALL", null, ["ram:beab80:8"]]
- 00be3e88 bytes 341a0094
+ 00be42b0 bytes 341a0094
- 00be3e9c ["INT_ADD", "register:40f0:8", ["const:be3e9c:8", "const:4:8"]]
- 00be3e9c ["CALL", null, ["ram:bea758:8"]]
+ 00be42c4 ["INT_ADD", "register:40f0:8", ["const:be42c4:8", "const:4:8"]]
+ 00be42c4 ["CALL", null, ["ram:beab80:8"]]
- 00be3e9c bytes 2f1a0094
+ 00be42c4 bytes 2f1a0094
- 00be3eb8 ["INT_ADD", "register:40f0:8", ["const:be3eb8:8", "const:4:8"]]
- 00be3eb8 ["CALL", null, ["local:b0:8"]]
+ 00be42e0 ["INT_ADD", "register:40f0:8", ["const:be42e0:8", "const:4:8"]]
+ 00be42e0 ["CALL", null, ["local:b0:8"]]
- 00be3eb8 bytes 10ffff97
+ 00be42e0 bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3c45011d73e6bbffe2b5261ca15101d"></a>

### [`00be4234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md) → [`00be465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be465c.md) FUN_00be465c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be4214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4214.md) [`00be4234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md) · 呼出先 4件 [`00be4234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md) [`00beae3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bea/00beae3c.md) [`00beb0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb0fc.md) [`00beb224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb224.md)
- 新版 呼出元 2件 [`00be463c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be463c.md) [`00be465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be465c.md) · 呼出先 4件 [`00be465c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be465c.md) [`00beb264`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb264.md) [`00beb524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb524.md) [`00beb64c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb64c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.56% / 新版 99.56%

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
      "site": "00be49ec",
      "value": [
        "leaf",
        "ram:beb264:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be45c4",
      "value": [
        "leaf",
        "ram:beae3c:8"
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
      "site": "00be4a00",
      "value": [
        "leaf",
        "ram:beb264:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be45d8",
      "value": [
        "leaf",
        "ram:beae3c:8"
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
      "00be49ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beae3c"
      ]
    ],
    [
      "00be4a00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beae3c"
      ]
    ]
  ],
  "added": [
    [
      "00be49ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb264"
      ]
    ],
    [
      "00be4a00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb264"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be45c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md#insn-00be45c4) · [`00be45d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md#insn-00be45d8) · [`00be45f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4234.md#insn-00be45f4)
- 新版 `00be49ec`（命令位置の公開資料なし） · `00be4a00`（命令位置の公開資料なし） · `00be4a1c`（命令位置の公開資料なし）

~~~diff
- 00be45c4 ["INT_ADD", "register:40f0:8", ["const:be45c4:8", "const:4:8"]]
- 00be45c4 ["CALL", null, ["ram:beae3c:8"]]
+ 00be49ec ["INT_ADD", "register:40f0:8", ["const:be49ec:8", "const:4:8"]]
+ 00be49ec ["CALL", null, ["ram:beb264:8"]]
- 00be45c4 bytes 1e1a0094
+ 00be49ec bytes 1e1a0094
- 00be45d8 ["INT_ADD", "register:40f0:8", ["const:be45d8:8", "const:4:8"]]
- 00be45d8 ["CALL", null, ["ram:beae3c:8"]]
+ 00be4a00 ["INT_ADD", "register:40f0:8", ["const:be4a00:8", "const:4:8"]]
+ 00be4a00 ["CALL", null, ["ram:beb264:8"]]
- 00be45d8 bytes 191a0094
+ 00be4a00 bytes 191a0094
- 00be45f4 ["INT_ADD", "register:40f0:8", ["const:be45f4:8", "const:4:8"]]
- 00be45f4 ["CALL", null, ["local:b0:8"]]
+ 00be4a1c ["INT_ADD", "register:40f0:8", ["const:be4a1c:8", "const:4:8"]]
+ 00be4a1c ["CALL", null, ["local:b0:8"]]
- 00be45f4 bytes 10ffff97
+ 00be4a1c bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17bae9ee02f367b6f20f89e2084f09d3"></a>

### [`00be4970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md) → [`00be4d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d98.md) FUN_00be4d98

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be4950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4950.md) [`00be4970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md) · 呼出先 4件 [`00be4970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md) [`00beb520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb520.md) [`00beb7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb7c0.md) [`00beb8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00beb/00beb8e8.md)
- 新版 呼出元 2件 [`00be4d78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d78.md) [`00be4d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d98.md) · 呼出先 4件 [`00be4d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be4/00be4d98.md) [`00beb948`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb948.md) [`00bebbe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00bebbe8.md) [`00bebd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00bebd10.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.55% / 新版 99.55%

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
      "site": "00be5128",
      "value": [
        "leaf",
        "ram:beb948:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be4d00",
      "value": [
        "leaf",
        "ram:beb520:8"
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
      "site": "00be513c",
      "value": [
        "leaf",
        "ram:beb948:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be4d14",
      "value": [
        "leaf",
        "ram:beb520:8"
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
      "00be5128",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb520"
      ]
    ],
    [
      "00be513c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb520"
      ]
    ]
  ],
  "added": [
    [
      "00be5128",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb948"
      ]
    ],
    [
      "00be513c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beb948"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be4d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md#insn-00be4d00) · [`00be4d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md#insn-00be4d14) · [`00be4d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be4/00be4970.md#insn-00be4d30)
- 新版 `00be5128`（命令位置の公開資料なし） · `00be513c`（命令位置の公開資料なし） · `00be5158`（命令位置の公開資料なし）

~~~diff
- 00be4d00 ["INT_ADD", "register:40f0:8", ["const:be4d00:8", "const:4:8"]]
- 00be4d00 ["CALL", null, ["ram:beb520:8"]]
+ 00be5128 ["INT_ADD", "register:40f0:8", ["const:be5128:8", "const:4:8"]]
+ 00be5128 ["CALL", null, ["ram:beb948:8"]]
- 00be4d00 bytes 081a0094
+ 00be5128 bytes 081a0094
- 00be4d14 ["INT_ADD", "register:40f0:8", ["const:be4d14:8", "const:4:8"]]
- 00be4d14 ["CALL", null, ["ram:beb520:8"]]
+ 00be513c ["INT_ADD", "register:40f0:8", ["const:be513c:8", "const:4:8"]]
+ 00be513c ["CALL", null, ["ram:beb948:8"]]
- 00be4d14 bytes 031a0094
+ 00be513c bytes 031a0094
- 00be4d30 ["INT_ADD", "register:40f0:8", ["const:be4d30:8", "const:4:8"]]
- 00be4d30 ["CALL", null, ["local:b0:8"]]
+ 00be5158 ["INT_ADD", "register:40f0:8", ["const:be5158:8", "const:4:8"]]
+ 00be5158 ["CALL", null, ["local:b0:8"]]
- 00be4d30 bytes 10ffff97
+ 00be5158 bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ed9186d11a95363190b611b7f5f1995"></a>

### [`00be7400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md) → [`00be7828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7828.md) FUN_00be7828

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be73e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be73e0.md) [`00be7400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md) · 呼出先 4件 [`00be7400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md) [`00beddb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bed/00beddb8.md) [`00bee058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee058.md) [`00bee180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee180.md)
- 新版 呼出元 2件 [`00be7808`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7808.md) [`00be7828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7828.md) · 呼出先 4件 [`00be7828`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7828.md) [`00bee1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00bee1e0.md) [`00bee480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00bee480.md) [`00bee5a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00bee5a8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.55% / 新版 99.55%

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
      "site": "00be7bb8",
      "value": [
        "leaf",
        "ram:bee1e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be7790",
      "value": [
        "leaf",
        "ram:beddb8:8"
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
      "site": "00be7bcc",
      "value": [
        "leaf",
        "ram:bee1e0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be77a4",
      "value": [
        "leaf",
        "ram:beddb8:8"
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
      "00be7bb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beddb8"
      ]
    ],
    [
      "00be7bcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00beddb8"
      ]
    ]
  ],
  "added": [
    [
      "00be7bb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee1e0"
      ]
    ],
    [
      "00be7bcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee1e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be7790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md#insn-00be7790) · [`00be77a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md#insn-00be77a4) · [`00be77c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7400.md#insn-00be77c0)
- 新版 `00be7bb8`（命令位置の公開資料なし） · `00be7bcc`（命令位置の公開資料なし） · `00be7be8`（命令位置の公開資料なし）

~~~diff
- 00be7790 ["INT_ADD", "register:40f0:8", ["const:be7790:8", "const:4:8"]]
- 00be7790 ["CALL", null, ["ram:beddb8:8"]]
+ 00be7bb8 ["INT_ADD", "register:40f0:8", ["const:be7bb8:8", "const:4:8"]]
+ 00be7bb8 ["CALL", null, ["ram:bee1e0:8"]]
- 00be7790 bytes 8a190094
+ 00be7bb8 bytes 8a190094
- 00be77a4 ["INT_ADD", "register:40f0:8", ["const:be77a4:8", "const:4:8"]]
- 00be77a4 ["CALL", null, ["ram:beddb8:8"]]
+ 00be7bcc ["INT_ADD", "register:40f0:8", ["const:be7bcc:8", "const:4:8"]]
+ 00be7bcc ["CALL", null, ["ram:bee1e0:8"]]
- 00be77a4 bytes 85190094
+ 00be7bcc bytes 85190094
- 00be77c0 ["INT_ADD", "register:40f0:8", ["const:be77c0:8", "const:4:8"]]
- 00be77c0 ["CALL", null, ["local:b0:8"]]
+ 00be7be8 ["INT_ADD", "register:40f0:8", ["const:be7be8:8", "const:4:8"]]
+ 00be7be8 ["CALL", null, ["local:b0:8"]]
- 00be77c0 bytes 10ffff97
+ 00be7be8 bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b8dd9199ba141fdcdf9e069294282b1"></a>

### [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) → [`00be7f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f40.md) FUN_00be7f40

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be7af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7af8.md) [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) · 呼出先 4件 [`00be7b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md) [`00bee458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee458.md) [`00bee6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee6f8.md) [`00bee820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00bee820.md)
- 新版 呼出元 2件 [`00be7f20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f20.md) [`00be7f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f40.md) · 呼出先 4件 [`00be7f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be7/00be7f40.md) [`00bee880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00bee880.md) [`00beeb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beeb20.md) [`00beec48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beec48.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.55% / 新版 99.55%

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
      "site": "00be82d0",
      "value": [
        "leaf",
        "ram:bee880:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be7ea8",
      "value": [
        "leaf",
        "ram:bee458:8"
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
      "site": "00be82e4",
      "value": [
        "leaf",
        "ram:bee880:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00be7ebc",
      "value": [
        "leaf",
        "ram:bee458:8"
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
      "00be82d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee458"
      ]
    ],
    [
      "00be82e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee458"
      ]
    ]
  ],
  "added": [
    [
      "00be82d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee880"
      ]
    ],
    [
      "00be82e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bee880"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00be7ea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md#insn-00be7ea8) · [`00be7ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md#insn-00be7ebc) · [`00be7ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be7/00be7b18.md#insn-00be7ed8)
- 新版 `00be82d0`（命令位置の公開資料なし） · `00be82e4`（命令位置の公開資料なし） · `00be8300`（命令位置の公開資料なし）

~~~diff
- 00be7ea8 ["INT_ADD", "register:40f0:8", ["const:be7ea8:8", "const:4:8"]]
- 00be7ea8 ["CALL", null, ["ram:bee458:8"]]
+ 00be82d0 ["INT_ADD", "register:40f0:8", ["const:be82d0:8", "const:4:8"]]
+ 00be82d0 ["CALL", null, ["ram:bee880:8"]]
- 00be7ea8 bytes 6c190094
+ 00be82d0 bytes 6c190094
- 00be7ebc ["INT_ADD", "register:40f0:8", ["const:be7ebc:8", "const:4:8"]]
- 00be7ebc ["CALL", null, ["ram:bee458:8"]]
+ 00be82e4 ["INT_ADD", "register:40f0:8", ["const:be82e4:8", "const:4:8"]]
+ 00be82e4 ["CALL", null, ["ram:bee880:8"]]
- 00be7ebc bytes 67190094
+ 00be82e4 bytes 67190094
- 00be7ed8 ["INT_ADD", "register:40f0:8", ["const:be7ed8:8", "const:4:8"]]
- 00be7ed8 ["CALL", null, ["local:b0:8"]]
+ 00be8300 ["INT_ADD", "register:40f0:8", ["const:be8300:8", "const:4:8"]]
+ 00be8300 ["CALL", null, ["local:b0:8"]]
- 00be7ed8 bytes 10ffff97
+ 00be8300 bytes 10ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaa4509cbcb45aaab1fba296746a3365"></a>

### [`00bef52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef52c.md) → [`00bef954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef954.md) _ZNSt6__ndk16chrono12system_clock3nowEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md) · 呼出先 3件 [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c59300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59300.md)
- 新版 呼出元 1件 [`00c58580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58580.md) · 呼出先 3件 [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c59700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59700.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bef9c0",
      "incomplete_value": false,
      "site": "00bef9c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:9dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bef598",
      "incomplete_value": false,
      "site": "00bef59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:99d:8"
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
      "00bef9c0",
      "PARAM",
      [
        "storage",
        "002b499d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bef9c0",
      "PARAM",
      [
        "storage",
        "002b49dd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bef59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef52c.md#insn-00bef59c) · [`00bef544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef52c.md#insn-00bef544) · [`00bef58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef52c.md#insn-00bef58c)
- 新版 `00bef9c4`（命令位置の公開資料なし） · `00bef96c`（命令位置の公開資料なし） · `00bef9b4`（命令位置の公開資料なし）

~~~diff
- 00bef59c ["INT_ADD", "register:40f0:8", ["const:bef59c:8", "const:4:8"]]
- 00bef59c ["CALL", null, ["callee:00c58120:8"]]
+ 00bef9c4 ["INT_ADD", "register:40f0:8", ["const:bef9c4:8", "const:4:8"]]
+ 00bef9c4 ["CALL", null, ["callee:00c58120:8"]]
- 00bef59c bytes e1a10194
+ 00bef9c4 bytes d7a10194
- 00bef544 ["INT_ADD", "register:40f0:8", ["const:bef544:8", "const:4:8"]]
- 00bef544 ["CALL", null, ["callee:00c59700:8"]]
+ 00bef96c ["INT_ADD", "register:40f0:8", ["const:bef96c:8", "const:4:8"]]
+ 00bef96c ["CALL", null, ["callee:00c59700:8"]]
- 00bef544 bytes 6fa70194
+ 00bef96c bytes 65a70194
- 00bef58c ["INT_ADD", "register:40f0:8", ["const:bef58c:8", "const:4:8"]]
- 00bef58c ["CALL", null, ["callee:00c580c0:8"]]
+ 00bef9b4 ["INT_ADD", "register:40f0:8", ["const:bef9b4:8", "const:4:8"]]
+ 00bef9b4 ["CALL", null, ["callee:00c580c0:8"]]
- 00bef58c bytes cda10194
+ 00bef9b4 bytes c3a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76668f1ae61032ff905a6475132038d0"></a>

### [`00bef5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef5e0.md) → [`00befa08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa08.md) _ZNSt6__ndk16chrono12steady_clock3nowEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ac0.md) · 呼出先 3件 [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c59300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59300.md)
- 新版 呼出元 1件 [`00c57ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ec0.md) · 呼出先 3件 [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c59700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59700.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00befa54",
      "incomplete_value": false,
      "site": "00befa58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:19f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bef62c",
      "incomplete_value": false,
      "site": "00bef630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a5000:8"
          ],
          [
            "leaf",
            "const:c3:8"
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
      "00befa54",
      "PARAM",
      [
        "storage",
        "002a50c3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00befa54",
      "PARAM",
      [
        "storage",
        "002a519f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bef630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef5e0.md#insn-00bef630) · [`00bef5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef5e0.md#insn-00bef5f8) · [`00bef620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef5e0.md#insn-00bef620)
- 新版 `00befa58`（命令位置の公開資料なし） · `00befa20`（命令位置の公開資料なし） · `00befa48`（命令位置の公開資料なし）

~~~diff
- 00bef630 ["INT_ADD", "register:40f0:8", ["const:bef630:8", "const:4:8"]]
- 00bef630 ["CALL", null, ["callee:00c58120:8"]]
+ 00befa58 ["INT_ADD", "register:40f0:8", ["const:befa58:8", "const:4:8"]]
+ 00befa58 ["CALL", null, ["callee:00c58120:8"]]
- 00bef630 bytes bca10194
+ 00befa58 bytes b2a10194
- 00bef5f8 ["INT_ADD", "register:40f0:8", ["const:bef5f8:8", "const:4:8"]]
- 00bef5f8 ["CALL", null, ["callee:00c59700:8"]]
+ 00befa20 ["INT_ADD", "register:40f0:8", ["const:befa20:8", "const:4:8"]]
+ 00befa20 ["CALL", null, ["callee:00c59700:8"]]
- 00bef5f8 bytes 42a70194
+ 00befa20 bytes 38a70194
- 00bef620 ["INT_ADD", "register:40f0:8", ["const:bef620:8", "const:4:8"]]
- 00bef620 ["CALL", null, ["callee:00c580c0:8"]]
+ 00befa48 ["INT_ADD", "register:40f0:8", ["const:befa48:8", "const:4:8"]]
+ 00befa48 ["CALL", null, ["callee:00c580c0:8"]]
- 00bef620 bytes a8a10194
+ 00befa48 bytes 9ea10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8d5c05308f5fb9cdde0768dabf47587"></a>

### [`00bef6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef6e4.md) → [`00befb0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb0c.md) _ZNSt16nested_exceptionC2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5db40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df40.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00befb28",
      "incomplete_value": true,
      "site": "00befb2c",
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
      "definition_site": "00bef700",
      "incomplete_value": true,
      "site": "00bef704",
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
      "00befb24",
      "READ",
      [
        "storage",
        "00c9b670",
        null,
        "pointer"
      ]
    ],
    [
      "00befb2c",
      "DATA",
      [
        "storage",
        "00c925d8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00befb24",
      "READ",
      [
        "storage",
        "00c9ba70",
        null,
        "pointer"
      ]
    ],
    [
      "00befb2c",
      "DATA",
      [
        "storage",
        "00c929d8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bef6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef6e4.md#insn-00bef6fc) · [`00bef708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef6e4.md#insn-00bef708)
- 新版 `00befb24`（命令位置の公開資料なし） · `00befb30`（命令位置の公開資料なし）

~~~diff
- 00bef6fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:670:8"]]
- 00bef6fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00befb24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
+ 00befb24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bef6fc bytes 083943f9
+ 00befb24 bytes 083945f9
- 00bef708 ["INT_ADD", "register:40f0:8", ["const:bef708:8", "const:4:8"]]
- 00bef708 ["CALL", null, ["callee:00c5df40:8"]]
+ 00befb30 ["INT_ADD", "register:40f0:8", ["const:befb30:8", "const:4:8"]]
+ 00befb30 ["CALL", null, ["callee:00c5df40:8"]]
- 00bef708 bytes 0eb90194
+ 00befb30 bytes 04b90194
~~~


<a id="compare-cc0c7fab9c6664f26d3ea01995b8029f"></a>

### [`00bef800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef800.md) → [`00befc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc28.md) _ZNSt6__ndk112__next_primeEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a420.md) · 呼出先 1件 [`00beff20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff20.md)
- 新版 呼出元 1件 [`00c5a820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a820.md) · 呼出先 1件 [`00bf0348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0348.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf0340",
      "incomplete_value": false,
      "site": "00bf0344",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00beff18",
      "incomplete_value": false,
      "site": "00beff1c",
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
            "const:250:8"
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
      "00befc58",
      "READ",
      [
        "storage",
        "003102e8",
        null,
        "undefined4"
      ]
    ],
    [
      "00befc58",
      "READ",
      [
        "storage",
        "003102b8",
        null,
        "undefined4"
      ]
    ],
    [
      "00befc6c",
      "READ",
      [
        "storage",
        "00310288",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00befc58",
      "READ",
      [
        "storage",
        "00310328",
        null,
        "undefined4"
      ]
    ],
    [
      "00befc58",
      "READ",
      [
        "storage",
        "003102f8",
        null,
        "undefined4"
      ]
    ],
    [
      "00befc6c",
      "READ",
      [
        "storage",
        "003102c8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00beff1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef800.md#insn-00beff1c) · [`00bef818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef800.md#insn-00bef818) · [`00bef884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef800.md#insn-00bef884)
- 新版 `00bf0344`（命令位置の公開資料なし） · `00befc40`（命令位置の公開資料なし） · `00befcac`（命令位置の公開資料なし）

~~~diff
- 00beff1c ["INT_ADD", "register:40f0:8", ["const:beff1c:8", "const:4:8"]]
- 00beff1c ["CALL", null, ["callee:00bf0348:8"]]
+ 00bf0344 ["INT_ADD", "register:40f0:8", ["const:bf0344:8", "const:4:8"]]
+ 00bf0344 ["CALL", null, ["callee:00bf0348:8"]]
- 00beff1c bytes 01000094
+ 00bf0344 bytes 01000094
- 00bef818 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00bef818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bef818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bef818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00befc40 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 00befc40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00befc40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00befc40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bef818 bytes 08210a91
+ 00befc40 bytes 08210b91
- 00bef884 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00bef884 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bef884 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bef884 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00befcac ["COPY", "tmp:0:8", ["const:388:8"]]
+ 00befcac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00befcac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00befcac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bef884 bytes 29210d91
+ 00befcac bytes 29210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8d1362c359cf9626c04cd0dc72c266e"></a>

### [`00beff20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff20.md) → [`00bf0348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0348.md) FUN_00bf0348

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bef800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef800.md) · 呼出先 4件 [`00beff74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff74.md) [`00c37934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 1件 [`00befc28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc28.md) · 呼出先 4件 [`00bf039c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf039c.md) [`00c37d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf037c",
      "incomplete_value": true,
      "site": "00bf0384",
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
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00beff54",
      "incomplete_value": true,
      "site": "00beff5c",
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
                "const:678:8"
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
      "definition_site": "00bf0380",
      "incomplete_value": true,
      "site": "00bf0384",
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
                "const:a80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00beff58",
      "incomplete_value": true,
      "site": "00beff5c",
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
                "const:680:8"
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
      "00bf037c",
      "READ",
      [
        "storage",
        "00c9b678",
        null,
        "pointer"
      ]
    ],
    [
      "00bf037c",
      "PARAM",
      [
        "storage",
        "00c964b0",
        "_ZTISt14overflow_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf0380",
      "READ",
      [
        "storage",
        "00c9b680",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf037c",
      "READ",
      [
        "storage",
        "00c9ba78",
        null,
        "pointer"
      ]
    ],
    [
      "00bf037c",
      "PARAM",
      [
        "storage",
        "00c968b0",
        "_ZTISt14overflow_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf0380",
      "READ",
      [
        "storage",
        "00c9ba80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00beff5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff20.md#insn-00beff5c) · [`00beff38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff20.md#insn-00beff38) · [`00beff44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beff20.md#insn-00beff44)
- 新版 `00bf0384`（命令位置の公開資料なし） · `00bf0360`（命令位置の公開資料なし） · `00bf036c`（命令位置の公開資料なし）

~~~diff
- 00beff5c ["INT_ADD", "register:40f0:8", ["const:beff5c:8", "const:4:8"]]
- 00beff5c ["CALL", null, ["callee:00c57f10:8"]]
+ 00bf0384 ["INT_ADD", "register:40f0:8", ["const:bf0384:8", "const:4:8"]]
+ 00bf0384 ["CALL", null, ["callee:00c57f10:8"]]
- 00beff5c bytes ed9e0194
+ 00bf0384 bytes e39e0194
- 00beff38 ["INT_ADD", "register:40f0:8", ["const:beff38:8", "const:4:8"]]
- 00beff38 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00bf0360 ["INT_ADD", "register:40f0:8", ["const:bf0360:8", "const:4:8"]]
+ 00bf0360 ["CALL", null, ["callee:00c57ef0:8"]]
- 00beff38 bytes ee9e0194
+ 00bf0360 bytes e49e0194
- 00beff44 ["INT_ADD", "register:40f0:8", ["const:beff44:8", "const:4:8"]]
- 00beff44 ["CALL", null, ["callee:00bf039c:8"]]
+ 00bf036c ["INT_ADD", "register:40f0:8", ["const:bf036c:8", "const:4:8"]]
+ 00bf036c ["CALL", null, ["callee:00bf039c:8"]]
- 00beff44 bytes 0c000094
+ 00bf036c bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43fbe4341915c829f196964509255bff"></a>

### [`00beffe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beffe0.md) → [`00bf0408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0408.md) _ZNKSt6__ndk112bad_weak_ptr4whatEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf0410",
      "incomplete_value": false,
      "site": "00bf0414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:10b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00beffe8",
      "incomplete_value": false,
      "site": "00beffec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:cb:8"
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
      "00bf0410",
      "DATA",
      [
        "storage",
        "002bb0cb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf0410",
      "DATA",
      [
        "storage",
        "002bb10b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00beffe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00beffe0.md#insn-00beffe8)
- 新版 `00bf0410`（命令位置の公開資料なし）

~~~diff
- 00beffe8 ["COPY", "tmp:0:8", ["const:cb:8"]]
- 00beffe8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00beffe8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00beffe8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf0410 ["COPY", "tmp:0:8", ["const:10b:8"]]
+ 00bf0410 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf0410 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf0410 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00beffe8 bytes 002c0391
+ 00bf0410 bytes 002c0491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1248f9002f8152c65d7e85a717a68a16"></a>

### [`00bf02f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf02f0.md) → [`00bf0718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0718.md) _ZSt17__throw_bad_allocv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5db80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db80.md) · 呼出先 4件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c58640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58640.md)
- 新版 呼出元 1件 [`00c5df80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df80.md) · 呼出先 4件 [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c58a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a40.md)

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
      "definition_site": "00bf0744",
      "incomplete_value": true,
      "site": "00bf074c",
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf031c",
      "incomplete_value": true,
      "site": "00bf0324",
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
                "const:9e8:8"
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
      "definition_site": "00bf0748",
      "incomplete_value": true,
      "site": "00bf074c",
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf0320",
      "incomplete_value": true,
      "site": "00bf0324",
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
                "const:9f0:8"
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
      "00bf0744",
      "READ",
      [
        "storage",
        "00c9a9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0744",
      "PARAM",
      [
        "storage",
        "00c96298",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf0748",
      "READ",
      [
        "storage",
        "00c9a9f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf0744",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0744",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf0748",
      "READ",
      [
        "storage",
        "00c9adf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf02f0.md#insn-00bf0324) · [`00bf0304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf02f0.md#insn-00bf0304) · [`00bf030c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf02f0.md#insn-00bf030c)
- 新版 `00bf074c`（命令位置の公開資料なし） · `00bf072c`（命令位置の公開資料なし） · `00bf0734`（命令位置の公開資料なし）

~~~diff
- 00bf0324 ["INT_ADD", "register:40f0:8", ["const:bf0324:8", "const:4:8"]]
- 00bf0324 ["CALL", null, ["callee:00c57f10:8"]]
+ 00bf074c ["INT_ADD", "register:40f0:8", ["const:bf074c:8", "const:4:8"]]
+ 00bf074c ["CALL", null, ["callee:00c57f10:8"]]
- 00bf0324 bytes fb9d0194
+ 00bf074c bytes f19d0194
- 00bf0304 ["INT_ADD", "register:40f0:8", ["const:bf0304:8", "const:4:8"]]
- 00bf0304 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00bf072c ["INT_ADD", "register:40f0:8", ["const:bf072c:8", "const:4:8"]]
+ 00bf072c ["CALL", null, ["callee:00c57ef0:8"]]
- 00bf0304 bytes fb9d0194
+ 00bf072c bytes f19d0194
- 00bf030c ["INT_ADD", "register:40f0:8", ["const:bf030c:8", "const:4:8"]]
- 00bf030c ["CALL", null, ["callee:00c58a40:8"]]
+ 00bf0734 ["INT_ADD", "register:40f0:8", ["const:bf0734:8", "const:4:8"]]
+ 00bf0734 ["CALL", null, ["callee:00c58a40:8"]]
- 00bf030c bytes cda00194
+ 00bf0734 bytes c3a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3795e58c2bdad0454fa98790cf82006b"></a>

### [`00bf0328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0328.md) → [`00bf0750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0750.md) _ZNSt11logic_errorC2ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5db90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db90.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5df90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df90.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf0770",
      "incomplete_value": true,
      "site": "00bf0774",
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
      "definition_site": "00bf0348",
      "incomplete_value": true,
      "site": "00bf034c",
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
      "00bf076c",
      "READ",
      [
        "storage",
        "00c9b690",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0774",
      "DATA",
      [
        "storage",
        "00c962d8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf076c",
      "READ",
      [
        "storage",
        "00c9ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0774",
      "DATA",
      [
        "storage",
        "00c966d8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf0344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0328.md#insn-00bf0344) · [`00bf0364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0328.md#insn-00bf0364) · [`00bf0370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0328.md#insn-00bf0370)
- 新版 `00bf076c`（命令位置の公開資料なし） · `00bf078c`（命令位置の公開資料なし） · `00bf0798`（命令位置の公開資料なし）

~~~diff
- 00bf0344 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:690:8"]]
- 00bf0344 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf076c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
+ 00bf076c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf0344 bytes 084943f9
+ 00bf076c bytes 084945f9
- 00bf0364 ["INT_ADD", "register:40f0:8", ["const:bf0364:8", "const:4:8"]]
- 00bf0364 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf078c ["INT_ADD", "register:40f0:8", ["const:bf078c:8", "const:4:8"]]
+ 00bf078c ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf0364 bytes 1f9e0194
+ 00bf078c bytes 159e0194
- 00bf0370 ["INT_ADD", "register:40f0:8", ["const:bf0370:8", "const:4:8"]]
- 00bf0370 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf0798 ["INT_ADD", "register:40f0:8", ["const:bf0798:8", "const:4:8"]]
+ 00bf0798 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf0370 bytes c89d0194
+ 00bf0798 bytes be9d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-304c7010a11f129f4be77c2547674d82"></a>

### [`00bf03bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf03bc.md) → [`00bf07e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf07e4.md) _ZNSt11logic_errorC1EPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b30.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c57f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f30.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf0808",
      "incomplete_value": true,
      "site": "00bf080c",
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
      "definition_site": "00bf03e0",
      "incomplete_value": true,
      "site": "00bf03e4",
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
      "00bf0804",
      "READ",
      [
        "storage",
        "00c9b690",
        null,
        "pointer"
      ]
    ],
    [
      "00bf080c",
      "DATA",
      [
        "storage",
        "00c962d8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf0804",
      "READ",
      [
        "storage",
        "00c9ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00bf080c",
      "DATA",
      [
        "storage",
        "00c966d8",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf03dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf03bc.md#insn-00bf03dc) · [`00bf03ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf03bc.md#insn-00bf03ec) · [`00bf03f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf03bc.md#insn-00bf03f8)
- 新版 `00bf0804`（命令位置の公開資料なし） · `00bf0814`（命令位置の公開資料なし） · `00bf0820`（命令位置の公開資料なし）

~~~diff
- 00bf03dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:690:8"]]
- 00bf03dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf0804 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
+ 00bf0804 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf03dc bytes 084943f9
+ 00bf0804 bytes 084945f9
- 00bf03ec ["INT_ADD", "register:40f0:8", ["const:bf03ec:8", "const:4:8"]]
- 00bf03ec ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf0814 ["INT_ADD", "register:40f0:8", ["const:bf0814:8", "const:4:8"]]
+ 00bf0814 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf03ec bytes fd9d0194
+ 00bf0814 bytes f39d0194
- 00bf03f8 ["INT_ADD", "register:40f0:8", ["const:bf03f8:8", "const:4:8"]]
- 00bf03f8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf0820 ["INT_ADD", "register:40f0:8", ["const:bf0820:8", "const:4:8"]]
+ 00bf0820 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf03f8 bytes a69d0194
+ 00bf0820 bytes 9c9d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4ad308ea4fef2494c9bbae965324b1c"></a>

### [`00bf04d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf04d8.md) → [`00bf0900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0900.md) _ZNSt13runtime_errorC1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5dba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dba0.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 1件 [`00c5dfa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfa0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf0920",
      "incomplete_value": true,
      "site": "00bf0924",
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
      "definition_site": "00bf04f8",
      "incomplete_value": true,
      "site": "00bf04fc",
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
      "00bf091c",
      "READ",
      [
        "storage",
        "00c9b698",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0924",
      "DATA",
      [
        "storage",
        "00c96300",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf091c",
      "READ",
      [
        "storage",
        "00c9ba98",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0924",
      "DATA",
      [
        "storage",
        "00c96700",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf04f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf04d8.md#insn-00bf04f4) · [`00bf0514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf04d8.md#insn-00bf0514) · [`00bf0520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf04d8.md#insn-00bf0520)
- 新版 `00bf091c`（命令位置の公開資料なし） · `00bf093c`（命令位置の公開資料なし） · `00bf0948`（命令位置の公開資料なし）

~~~diff
- 00bf04f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:698:8"]]
- 00bf04f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf091c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a98:8"]]
+ 00bf091c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf04f4 bytes 084d43f9
+ 00bf091c bytes 084d45f9
- 00bf0514 ["INT_ADD", "register:40f0:8", ["const:bf0514:8", "const:4:8"]]
- 00bf0514 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf093c ["INT_ADD", "register:40f0:8", ["const:bf093c:8", "const:4:8"]]
+ 00bf093c ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf0514 bytes b39d0194
+ 00bf093c bytes a99d0194
- 00bf0520 ["INT_ADD", "register:40f0:8", ["const:bf0520:8", "const:4:8"]]
- 00bf0520 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf0948 ["INT_ADD", "register:40f0:8", ["const:bf0948:8", "const:4:8"]]
+ 00bf0948 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf0520 bytes 5c9d0194
+ 00bf0948 bytes 529d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b3c717802e73f558fffc1bbbb30e717"></a>

### [`00bf056c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf056c.md) → [`00bf0994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0994.md) _ZNSt13runtime_errorC1EPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c5a4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4d0.md) [`00c5dbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbc0.md) · 呼出先 3件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 2件 [`00c5a8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8d0.md) [`00c5dfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfc0.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf09b8",
      "incomplete_value": true,
      "site": "00bf09bc",
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
      "definition_site": "00bf0590",
      "incomplete_value": true,
      "site": "00bf0594",
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
      "00bf09b4",
      "READ",
      [
        "storage",
        "00c9b698",
        null,
        "pointer"
      ]
    ],
    [
      "00bf09bc",
      "DATA",
      [
        "storage",
        "00c96300",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf09b4",
      "READ",
      [
        "storage",
        "00c9ba98",
        null,
        "pointer"
      ]
    ],
    [
      "00bf09bc",
      "DATA",
      [
        "storage",
        "00c96700",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf058c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf056c.md#insn-00bf058c) · [`00bf059c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf056c.md#insn-00bf059c) · [`00bf05a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf056c.md#insn-00bf05a8)
- 新版 `00bf09b4`（命令位置の公開資料なし） · `00bf09c4`（命令位置の公開資料なし） · `00bf09d0`（命令位置の公開資料なし）

~~~diff
- 00bf058c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:698:8"]]
- 00bf058c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf09b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a98:8"]]
+ 00bf09b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf058c bytes 084d43f9
+ 00bf09b4 bytes 084d45f9
- 00bf059c ["INT_ADD", "register:40f0:8", ["const:bf059c:8", "const:4:8"]]
- 00bf059c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00bf09c4 ["INT_ADD", "register:40f0:8", ["const:bf09c4:8", "const:4:8"]]
+ 00bf09c4 ["CALL", null, ["callee:00c57fe0:8"]]
- 00bf059c bytes 919d0194
+ 00bf09c4 bytes 879d0194
- 00bf05a8 ["INT_ADD", "register:40f0:8", ["const:bf05a8:8", "const:4:8"]]
- 00bf05a8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf09d0 ["INT_ADD", "register:40f0:8", ["const:bf09d0:8", "const:4:8"]]
+ 00bf09d0 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf05a8 bytes 3a9d0194
+ 00bf09d0 bytes 309d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57d4806f83e8e0e8804010bf7130f5ed"></a>

### [`00bf0688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0688.md) → [`00bf0ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0ab0.md) _ZNSt6__ndk121__throw_runtime_errorEPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md) · 呼出先 4件 [`00c37934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37934.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5dbc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbc0.md)
- 新版 呼出元 1件 [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md) · 呼出先 4件 [`00c37d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37d5c.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5dfc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf0ae4",
      "incomplete_value": true,
      "site": "00bf0aec",
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
                "const:aa0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf06bc",
      "incomplete_value": true,
      "site": "00bf06c4",
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
                "const:6a0:8"
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
      "definition_site": "00bf0ae8",
      "incomplete_value": true,
      "site": "00bf0aec",
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
                "const:aa8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf06c0",
      "incomplete_value": true,
      "site": "00bf06c4",
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
                "const:6a8:8"
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
      "00bf0ae4",
      "READ",
      [
        "storage",
        "00c9b6a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0ae4",
      "PARAM",
      [
        "storage",
        "00c96458",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf0ae8",
      "READ",
      [
        "storage",
        "00c9b6a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf0ae4",
      "READ",
      [
        "storage",
        "00c9baa0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf0ae4",
      "PARAM",
      [
        "storage",
        "00c96858",
        "_ZTISt13runtime_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf0ae8",
      "READ",
      [
        "storage",
        "00c9baa8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf06c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0688.md#insn-00bf06c4) · [`00bf06a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0688.md#insn-00bf06a0) · [`00bf06ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0688.md#insn-00bf06ac)
- 新版 `00bf0aec`（命令位置の公開資料なし） · `00bf0ac8`（命令位置の公開資料なし） · `00bf0ad4`（命令位置の公開資料なし）

~~~diff
- 00bf06c4 ["INT_ADD", "register:40f0:8", ["const:bf06c4:8", "const:4:8"]]
- 00bf06c4 ["CALL", null, ["callee:00c57f10:8"]]
+ 00bf0aec ["INT_ADD", "register:40f0:8", ["const:bf0aec:8", "const:4:8"]]
+ 00bf0aec ["CALL", null, ["callee:00c57f10:8"]]
- 00bf06c4 bytes 139d0194
+ 00bf0aec bytes 099d0194
- 00bf06a0 ["INT_ADD", "register:40f0:8", ["const:bf06a0:8", "const:4:8"]]
- 00bf06a0 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00bf0ac8 ["INT_ADD", "register:40f0:8", ["const:bf0ac8:8", "const:4:8"]]
+ 00bf0ac8 ["CALL", null, ["callee:00c57ef0:8"]]
- 00bf06a0 bytes 149d0194
+ 00bf0ac8 bytes 0a9d0194
- 00bf06ac ["INT_ADD", "register:40f0:8", ["const:bf06ac:8", "const:4:8"]]
- 00bf06ac ["CALL", null, ["callee:00c5dfc0:8"]]
+ 00bf0ad4 ["INT_ADD", "register:40f0:8", ["const:bf0ad4:8", "const:4:8"]]
+ 00bf0ad4 ["CALL", null, ["callee:00c5dfc0:8"]]
- 00bf06ac bytes 45b50194
+ 00bf0ad4 bytes 3bb50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70f245266dbad659d13a4c1b8cab2342"></a>

### [`00bf1c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1c7c.md) → [`00bf20a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf20a4.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmRKS5_mm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf214c",
      "incomplete_value": false,
      "site": "00bf2150",
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
            "const:714:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf1d24",
      "incomplete_value": false,
      "site": "00bf1d28",
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
            "const:6d4:8"
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
      "00bf214c",
      "PARAM",
      [
        "storage",
        "002af6d4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf214c",
      "PARAM",
      [
        "storage",
        "002af714",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf1d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1c7c.md#insn-00bf1d28) · [`00bf1cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1c7c.md#insn-00bf1cf4) · [`00bf1d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf1c7c.md#insn-00bf1d24)
- 新版 `00bf2150`（命令位置の公開資料なし） · `00bf211c`（命令位置の公開資料なし） · `00bf214c`（命令位置の公開資料なし）

~~~diff
- 00bf1d28 ["INT_ADD", "register:40f0:8", ["const:bf1d28:8", "const:4:8"]]
- 00bf1d28 ["CALL", null, ["callee:00442930:8"]]
+ 00bf2150 ["INT_ADD", "register:40f0:8", ["const:bf2150:8", "const:4:8"]]
+ 00bf2150 ["CALL", null, ["callee:00442930:8"]]
- 00bf1d28 bytes f242e197
+ 00bf2150 bytes f841e197
- 00bf1cf4 ["INT_ADD", "register:40f0:8", ["const:bf1cf4:8", "const:4:8"]]
- 00bf1cf4 ["CALL", null, ["callee:00c58050:8"]]
+ 00bf211c ["INT_ADD", "register:40f0:8", ["const:bf211c:8", "const:4:8"]]
+ 00bf211c ["CALL", null, ["callee:00c58050:8"]]
- 00bf1cf4 bytes d7970194
+ 00bf211c bytes cd970194
- 00bf1d24 ["COPY", "tmp:0:8", ["const:6d4:8"]]
- 00bf1d24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf1d24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf1d24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf214c ["COPY", "tmp:0:8", ["const:714:8"]]
+ 00bf214c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf214c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf214c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf1d24 bytes 00501b91
+ 00bf214c bytes 00501c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d8c485cd35197815b252a9d6ef1073d"></a>

### [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) → [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) FUN_00bf28d8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 17件 [`00bf22d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf22d8.md) [`00bf29b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf29b4.md) [`00bf2bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2bf4.md) [`00bf2c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2c3c.md) [`00bf2de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf2de8.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 17件 [`00bf2700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2700.md) [`00bf2ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2ddc.md) [`00bf301c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf301c.md) [`00bf3064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3064.md) [`00bf3210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3210.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf28e8",
      "incomplete_value": false,
      "site": "00bf28ec",
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
            "const:f23:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf24c0",
      "incomplete_value": false,
      "site": "00bf24c4",
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
            "const:ee3:8"
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
      "00bf28e8",
      "PARAM",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf28e8",
      "PARAM",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf24c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md#insn-00bf24c4) · [`00bf24c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md#insn-00bf24c0)
- 新版 `00bf28ec`（命令位置の公開資料なし） · `00bf28e8`（命令位置の公開資料なし）

~~~diff
- 00bf24c4 ["INT_ADD", "register:40f0:8", ["const:bf24c4:8", "const:4:8"]]
- 00bf24c4 ["CALL", null, ["callee:00442930:8"]]
+ 00bf28ec ["INT_ADD", "register:40f0:8", ["const:bf28ec:8", "const:4:8"]]
+ 00bf28ec ["CALL", null, ["callee:00442930:8"]]
- 00bf24c4 bytes 0b41e197
+ 00bf28ec bytes 1140e197
- 00bf24c0 ["COPY", "tmp:0:8", ["const:ee3:8"]]
- 00bf24c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf24c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf24c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf28e8 ["COPY", "tmp:0:8", ["const:f23:8"]]
+ 00bf28e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf28e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf28e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf24c0 bytes 008c3b91
+ 00bf28e8 bytes 008c3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-449b2e71365b93e5090b55208354151c"></a>

### [`00bf40e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf40e8.md) → [`00bf4510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4510.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmRKS5_mm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00c5dc40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00c5e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf45c0",
      "incomplete_value": false,
      "site": "00bf45c4",
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
            "const:714:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4198",
      "incomplete_value": false,
      "site": "00bf419c",
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
            "const:6d4:8"
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
      "00bf45c0",
      "PARAM",
      [
        "storage",
        "002af6d4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf45c0",
      "PARAM",
      [
        "storage",
        "002af714",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf419c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf40e8.md#insn-00bf419c) · [`00bf416c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf40e8.md#insn-00bf416c) · [`00bf4198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf40e8.md#insn-00bf4198)
- 新版 `00bf45c4`（命令位置の公開資料なし） · `00bf4594`（命令位置の公開資料なし） · `00bf45c0`（命令位置の公開資料なし）

~~~diff
- 00bf419c ["INT_ADD", "register:40f0:8", ["const:bf419c:8", "const:4:8"]]
- 00bf419c ["CALL", null, ["callee:00442930:8"]]
+ 00bf45c4 ["INT_ADD", "register:40f0:8", ["const:bf45c4:8", "const:4:8"]]
+ 00bf45c4 ["CALL", null, ["callee:00442930:8"]]
- 00bf419c bytes d539e197
+ 00bf45c4 bytes db38e197
- 00bf416c ["INT_ADD", "register:40f0:8", ["const:bf416c:8", "const:4:8"]]
- 00bf416c ["CALL", null, ["callee:00c5e040:8"]]
+ 00bf4594 ["INT_ADD", "register:40f0:8", ["const:bf4594:8", "const:4:8"]]
+ 00bf4594 ["CALL", null, ["callee:00c5e040:8"]]
- 00bf416c bytes b5a60194
+ 00bf4594 bytes aba60194
- 00bf4198 ["COPY", "tmp:0:8", ["const:6d4:8"]]
- 00bf4198 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4198 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4198 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf45c0 ["COPY", "tmp:0:8", ["const:714:8"]]
+ 00bf45c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf45c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf45c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf4198 bytes 00501b91
+ 00bf45c0 bytes 00501c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0eff47e35fe4308404f52a51c9f4600e"></a>

### [`00bf4748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4748.md) → [`00bf4b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b70.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_length_errorEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5ac90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac90.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00c5b090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b090.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf4b80",
      "incomplete_value": false,
      "site": "00bf4b84",
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
            "const:f23:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4758",
      "incomplete_value": false,
      "site": "00bf475c",
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
            "const:ee3:8"
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
      "00bf4b80",
      "PARAM",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf4b80",
      "PARAM",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4748.md#insn-00bf475c) · [`00bf4758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4748.md#insn-00bf4758)
- 新版 `00bf4b84`（命令位置の公開資料なし） · `00bf4b80`（命令位置の公開資料なし）

~~~diff
- 00bf475c ["INT_ADD", "register:40f0:8", ["const:bf475c:8", "const:4:8"]]
- 00bf475c ["CALL", null, ["callee:0043b778:8"]]
+ 00bf4b84 ["INT_ADD", "register:40f0:8", ["const:bf4b84:8", "const:4:8"]]
+ 00bf4b84 ["CALL", null, ["callee:0043b778:8"]]
- 00bf475c bytes f71be197
+ 00bf4b84 bytes fd1ae197
- 00bf4758 ["COPY", "tmp:0:8", ["const:ee3:8"]]
- 00bf4758 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4758 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4758 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf4b80 ["COPY", "tmp:0:8", ["const:f23:8"]]
+ 00bf4b80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf4b80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf4b80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf4758 bytes 008c3b91
+ 00bf4b80 bytes 008c3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e66b0352f107e6e9510003bc37d979d"></a>

### [`00bf4760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4760.md) → [`00bf4b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4b88.md) _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_out_of_rangeEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5d050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d050.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)
- 新版 呼出元 1件 [`00c5d450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d450.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf4b98",
      "incomplete_value": false,
      "site": "00bf4b9c",
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
            "const:f23:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4770",
      "incomplete_value": false,
      "site": "00bf4774",
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
            "const:ee3:8"
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
      "00bf4b98",
      "PARAM",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf4b98",
      "PARAM",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4760.md#insn-00bf4774) · [`00bf4770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4760.md#insn-00bf4770)
- 新版 `00bf4b9c`（命令位置の公開資料なし） · `00bf4b98`（命令位置の公開資料なし）

~~~diff
- 00bf4774 ["INT_ADD", "register:40f0:8", ["const:bf4774:8", "const:4:8"]]
- 00bf4774 ["CALL", null, ["callee:00442930:8"]]
+ 00bf4b9c ["INT_ADD", "register:40f0:8", ["const:bf4b9c:8", "const:4:8"]]
+ 00bf4b9c ["CALL", null, ["callee:00442930:8"]]
- 00bf4774 bytes 5f38e197
+ 00bf4b9c bytes 6537e197
- 00bf4770 ["COPY", "tmp:0:8", ["const:ee3:8"]]
- 00bf4770 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4770 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bf4770 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bf4b98 ["COPY", "tmp:0:8", ["const:f23:8"]]
+ 00bf4b98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf4b98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bf4b98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bf4770 bytes 008c3b91
+ 00bf4b98 bytes 008c3c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c68312a6aacfb54917b73188d9e9c25"></a>

### [`00bf4778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4778.md) → [`00bf4ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4ba0.md) _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c60.md) · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00481e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md) [`00bf7d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7d54.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c58190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58190.md)
- 新版 呼出元 1件 [`00c58060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58060.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`00bf817c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c58590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58590.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf4cc0",
      "incomplete_value": true,
      "site": "00bf4cc0",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4898",
      "incomplete_value": true,
      "site": "00bf4898",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf4cc8",
      "incomplete_value": true,
      "site": "00bf4cc8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf48a0",
      "incomplete_value": true,
      "site": "00bf48a0",
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
                "const:6:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf4c6c",
      "incomplete_value": false,
      "site": "00bf4c7c",
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
            "const:dc6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4844",
      "incomplete_value": false,
      "site": "00bf4854",
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
            "const:d86:8"
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
      "00bf4c6c",
      "PARAM",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf4cb0",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf4cb4",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf4c6c",
      "PARAM",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf4cb0",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf4cb4",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4778.md#insn-00bf4854) · [`00bf47c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4778.md#insn-00bf47c8) · [`00bf47e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4778.md#insn-00bf47e4)
- 新版 `00bf4c7c`（命令位置の公開資料なし） · `00bf4bf0`（命令位置の公開資料なし） · `00bf4c0c`（命令位置の公開資料なし）

~~~diff
- 00bf4854 ["INT_ADD", "register:40f0:8", ["const:bf4854:8", "const:4:8"]]
- 00bf4854 ["CALL", null, ["callee:00481e80:8"]]
+ 00bf4c7c ["INT_ADD", "register:40f0:8", ["const:bf4c7c:8", "const:4:8"]]
+ 00bf4c7c ["CALL", null, ["callee:00481e80:8"]]
- 00bf4854 bytes 7b35e297
+ 00bf4c7c bytes 8134e297
- 00bf47c8 ["INT_ADD", "register:40f0:8", ["const:bf47c8:8", "const:4:8"]]
- 00bf47c8 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf4bf0 ["INT_ADD", "register:40f0:8", ["const:bf4bf0:8", "const:4:8"]]
+ 00bf4bf0 ["CALL", null, ["callee:00c580c0:8"]]
- 00bf47c8 bytes 3e8d0194
+ 00bf4bf0 bytes 348d0194
- 00bf47e4 ["INT_ADD", "register:40f0:8", ["const:bf47e4:8", "const:4:8"]]
- 00bf47e4 ["CALL", null, ["callee:00c58590:8"]]
+ 00bf4c0c ["INT_ADD", "register:40f0:8", ["const:bf4c0c:8", "const:4:8"]]
+ 00bf4c0c ["CALL", null, ["callee:00c58590:8"]]
- 00bf47e4 bytes 6b8e0194
+ 00bf4c0c bytes 618e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c912fbdb4e667a4ab4739d12cf6a7fd6"></a>

### [`00bf48d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf48d4.md) → [`00bf4cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4cfc.md) _ZNSt6__ndk14stolERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00481e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md) [`00bf7d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7d54.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`00bf817c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf4dc0",
      "incomplete_value": false,
      "site": "00bf4dd0",
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
            "const:dc6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4998",
      "incomplete_value": false,
      "site": "00bf49a8",
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
            "const:d86:8"
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
      "00bf4dc0",
      "PARAM",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf4dc0",
      "PARAM",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf49a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf48d4.md#insn-00bf49a8) · [`00bf4924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf48d4.md#insn-00bf4924) · [`00bf4940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf48d4.md#insn-00bf4940)
- 新版 `00bf4dd0`（命令位置の公開資料なし） · `00bf4d4c`（命令位置の公開資料なし） · `00bf4d68`（命令位置の公開資料なし）

~~~diff
- 00bf49a8 ["INT_ADD", "register:40f0:8", ["const:bf49a8:8", "const:4:8"]]
- 00bf49a8 ["CALL", null, ["callee:00481e80:8"]]
+ 00bf4dd0 ["INT_ADD", "register:40f0:8", ["const:bf4dd0:8", "const:4:8"]]
+ 00bf4dd0 ["CALL", null, ["callee:00481e80:8"]]
- 00bf49a8 bytes 2635e297
+ 00bf4dd0 bytes 2c34e297
- 00bf4924 ["INT_ADD", "register:40f0:8", ["const:bf4924:8", "const:4:8"]]
- 00bf4924 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf4d4c ["INT_ADD", "register:40f0:8", ["const:bf4d4c:8", "const:4:8"]]
+ 00bf4d4c ["CALL", null, ["callee:00c580c0:8"]]
- 00bf4924 bytes e78c0194
+ 00bf4d4c bytes dd8c0194
- 00bf4940 ["INT_ADD", "register:40f0:8", ["const:bf4940:8", "const:4:8"]]
- 00bf4940 ["CALL", null, ["callee:00c58590:8"]]
+ 00bf4d68 ["INT_ADD", "register:40f0:8", ["const:bf4d68:8", "const:4:8"]]
+ 00bf4d68 ["CALL", null, ["callee:00c58590:8"]]
- 00bf4940 bytes 148e0194
+ 00bf4d68 bytes 0a8e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-089e5171e17d8a79663059de440a624a"></a>

### [`00bf49ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf49ec.md) → [`00bf4e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4e14.md) _ZNSt6__ndk15stoulERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c585f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585f0.md) · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)
- 新版 呼出元 1件 [`00c589f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589f0.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.01% / 新版 89.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf4f10",
      "incomplete_value": true,
      "site": "00bf4f10",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4ae8",
      "incomplete_value": true,
      "site": "00bf4ae8",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf4f14",
      "incomplete_value": true,
      "site": "00bf4f14",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4aec",
      "incomplete_value": true,
      "site": "00bf4aec",
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
                "const:6:8"
              ]
            ]
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
      "definition_site": "00bf4f50",
      "incomplete_value": true,
      "site": "00bf4f50",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4b28",
      "incomplete_value": true,
      "site": "00bf4b28",
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
                "const:42e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf4ef8",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf4efc",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf4f38",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf4ef8",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf4efc",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf4f38",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf49ec.md#insn-00bf4a48) · [`00bf4a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf49ec.md#insn-00bf4a64) · [`00bf4a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf49ec.md#insn-00bf4a94)
- 新版 `00bf4e70`（命令位置の公開資料なし） · `00bf4e8c`（命令位置の公開資料なし） · `00bf4ebc`（命令位置の公開資料なし）

~~~diff
- 00bf4a48 ["INT_ADD", "register:40f0:8", ["const:bf4a48:8", "const:4:8"]]
- 00bf4a48 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf4e70 ["INT_ADD", "register:40f0:8", ["const:bf4e70:8", "const:4:8"]]
+ 00bf4e70 ["CALL", null, ["callee:00c580c0:8"]]
- 00bf4a48 bytes 9e8c0194
+ 00bf4e70 bytes 948c0194
- 00bf4a64 ["INT_ADD", "register:40f0:8", ["const:bf4a64:8", "const:4:8"]]
- 00bf4a64 ["CALL", null, ["callee:00c5e060:8"]]
+ 00bf4e8c ["INT_ADD", "register:40f0:8", ["const:bf4e8c:8", "const:4:8"]]
+ 00bf4e8c ["CALL", null, ["callee:00c5e060:8"]]
- 00bf4a64 bytes 7fa40194
+ 00bf4e8c bytes 75a40194
- 00bf4a94 ["INT_ADD", "register:40f0:8", ["const:bf4a94:8", "const:4:8"]]
- 00bf4a94 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf4ebc ["INT_ADD", "register:40f0:8", ["const:bf4ebc:8", "const:4:8"]]
+ 00bf4ebc ["CALL", null, ["callee:00c5e050:8"]]
- 00bf4a94 bytes 6fa40194
+ 00bf4ebc bytes 65a40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8dfdb43d539cf0ff0818d4c04075509"></a>

### [`00bf4b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4b58.md) → [`00bf4f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4f80.md) _ZNSt6__ndk15stollERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e30.md) · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c581a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581a0.md)
- 新版 呼出元 1件 [`00c58230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58230.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c585a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.01% / 新版 89.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf507c",
      "incomplete_value": true,
      "site": "00bf507c",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4c54",
      "incomplete_value": true,
      "site": "00bf4c54",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf5080",
      "incomplete_value": true,
      "site": "00bf5080",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4c58",
      "incomplete_value": true,
      "site": "00bf4c58",
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
                "const:6:8"
              ]
            ]
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
      "definition_site": "00bf50bc",
      "incomplete_value": true,
      "site": "00bf50bc",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4c94",
      "incomplete_value": true,
      "site": "00bf4c94",
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
                "const:42e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf5064",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf5068",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf50a4",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5064",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5068",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf50a4",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4b58.md#insn-00bf4bb4) · [`00bf4bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4b58.md#insn-00bf4bd0) · [`00bf4c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4b58.md#insn-00bf4c00)
- 新版 `00bf4fdc`（命令位置の公開資料なし） · `00bf4ff8`（命令位置の公開資料なし） · `00bf5028`（命令位置の公開資料なし）

~~~diff
- 00bf4bb4 ["INT_ADD", "register:40f0:8", ["const:bf4bb4:8", "const:4:8"]]
- 00bf4bb4 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf4fdc ["INT_ADD", "register:40f0:8", ["const:bf4fdc:8", "const:4:8"]]
+ 00bf4fdc ["CALL", null, ["callee:00c580c0:8"]]
- 00bf4bb4 bytes 438c0194
+ 00bf4fdc bytes 398c0194
- 00bf4bd0 ["INT_ADD", "register:40f0:8", ["const:bf4bd0:8", "const:4:8"]]
- 00bf4bd0 ["CALL", null, ["callee:00c585a0:8"]]
+ 00bf4ff8 ["INT_ADD", "register:40f0:8", ["const:bf4ff8:8", "const:4:8"]]
+ 00bf4ff8 ["CALL", null, ["callee:00c585a0:8"]]
- 00bf4bd0 bytes 748d0194
+ 00bf4ff8 bytes 6a8d0194
- 00bf4c00 ["INT_ADD", "register:40f0:8", ["const:bf4c00:8", "const:4:8"]]
- 00bf4c00 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf5028 ["INT_ADD", "register:40f0:8", ["const:bf5028:8", "const:4:8"]]
+ 00bf5028 ["CALL", null, ["callee:00c5e050:8"]]
- 00bf4c00 bytes 14a40194
+ 00bf5028 bytes 0aa40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d756cd079ebacfcb2893f5b65a02e893"></a>

### [`00bf4cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4cc4.md) → [`00bf50ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf50ec.md) _ZNSt6__ndk16stoullERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e40.md) · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)
- 新版 呼出元 1件 [`00c58240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58240.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.13% / 新版 89.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf51ec",
      "incomplete_value": true,
      "site": "00bf51ec",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4dc4",
      "incomplete_value": true,
      "site": "00bf4dc4",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
              ]
            ]
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
      "definition_site": "00bf51f0",
      "incomplete_value": true,
      "site": "00bf51f0",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4dc8",
      "incomplete_value": true,
      "site": "00bf4dc8",
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
                "const:6:8"
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
      "definition_site": "00bf522c",
      "incomplete_value": true,
      "site": "00bf522c",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4e04",
      "incomplete_value": true,
      "site": "00bf4e04",
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
                "const:42e:8"
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
      "00bf51d4",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf51d8",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf5214",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf51d4",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf51d8",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5214",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4cc4.md#insn-00bf4d24) · [`00bf4d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4cc4.md#insn-00bf4d40) · [`00bf4d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4cc4.md#insn-00bf4d70)
- 新版 `00bf514c`（命令位置の公開資料なし） · `00bf5168`（命令位置の公開資料なし） · `00bf5198`（命令位置の公開資料なし）

~~~diff
- 00bf4d24 ["INT_ADD", "register:40f0:8", ["const:bf4d24:8", "const:4:8"]]
- 00bf4d24 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf514c ["INT_ADD", "register:40f0:8", ["const:bf514c:8", "const:4:8"]]
+ 00bf514c ["CALL", null, ["callee:00c580c0:8"]]
- 00bf4d24 bytes e78b0194
+ 00bf514c bytes dd8b0194
- 00bf4d40 ["INT_ADD", "register:40f0:8", ["const:bf4d40:8", "const:4:8"]]
- 00bf4d40 ["CALL", null, ["callee:00c5e070:8"]]
+ 00bf5168 ["INT_ADD", "register:40f0:8", ["const:bf5168:8", "const:4:8"]]
+ 00bf5168 ["CALL", null, ["callee:00c5e070:8"]]
- 00bf4d40 bytes cca30194
+ 00bf5168 bytes c2a30194
- 00bf4d70 ["INT_ADD", "register:40f0:8", ["const:bf4d70:8", "const:4:8"]]
- 00bf4d70 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf5198 ["INT_ADD", "register:40f0:8", ["const:bf5198:8", "const:4:8"]]
+ 00bf5198 ["CALL", null, ["callee:00c5e050:8"]]
- 00bf4d70 bytes b8a30194
+ 00bf5198 bytes aea30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91568198ed9934231e17f2717d1fa82e"></a>

### [`00bf4e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4e34.md) → [`00bf525c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf525c.md) _ZNSt6__ndk14stofERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c581e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581e0.md) · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c581b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581b0.md)
- 新版 呼出元 1件 [`00c585e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585e0.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c585b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5338",
      "incomplete_value": true,
      "site": "00bf5338",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4f10",
      "incomplete_value": true,
      "site": "00bf4f10",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf5340",
      "incomplete_value": true,
      "site": "00bf5340",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4f18",
      "incomplete_value": true,
      "site": "00bf4f18",
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
                "const:6:8"
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
      "definition_site": "00bf5370",
      "incomplete_value": true,
      "site": "00bf5370",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf4f48",
      "incomplete_value": true,
      "site": "00bf4f48",
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
                "const:42e:8"
              ]
            ]
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
      "00bf5328",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf532c",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf5360",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5328",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf532c",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5360",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4e34.md#insn-00bf4e80) · [`00bf4e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4e34.md#insn-00bf4e98) · [`00bf4ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4e34.md#insn-00bf4ec8)
- 新版 `00bf52a8`（命令位置の公開資料なし） · `00bf52c0`（命令位置の公開資料なし） · `00bf52f0`（命令位置の公開資料なし）

~~~diff
- 00bf4e80 ["INT_ADD", "register:40f0:8", ["const:bf4e80:8", "const:4:8"]]
- 00bf4e80 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf52a8 ["INT_ADD", "register:40f0:8", ["const:bf52a8:8", "const:4:8"]]
+ 00bf52a8 ["CALL", null, ["callee:00c580c0:8"]]
- 00bf4e80 bytes 908b0194
+ 00bf52a8 bytes 868b0194
- 00bf4e98 ["INT_ADD", "register:40f0:8", ["const:bf4e98:8", "const:4:8"]]
- 00bf4e98 ["CALL", null, ["callee:00c585b0:8"]]
+ 00bf52c0 ["INT_ADD", "register:40f0:8", ["const:bf52c0:8", "const:4:8"]]
+ 00bf52c0 ["CALL", null, ["callee:00c585b0:8"]]
- 00bf4e98 bytes c68c0194
+ 00bf52c0 bytes bc8c0194
- 00bf4ec8 ["INT_ADD", "register:40f0:8", ["const:bf4ec8:8", "const:4:8"]]
- 00bf4ec8 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf52f0 ["INT_ADD", "register:40f0:8", ["const:bf52f0:8", "const:4:8"]]
+ 00bf52f0 ["CALL", null, ["callee:00c5e050:8"]]
- 00bf4ec8 bytes 62a30194
+ 00bf52f0 bytes 58a30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d0f648ac2fee74640080a04b9f795d3"></a>

### [`00bf4f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4f7c.md) → [`00bf53a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf53a4.md) _ZNSt6__ndk14stodERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e50.md) · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c581c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c581c0.md)
- 新版 呼出元 1件 [`00c58250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58250.md) · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c585c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5480",
      "incomplete_value": true,
      "site": "00bf5480",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5058",
      "incomplete_value": true,
      "site": "00bf5058",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf5488",
      "incomplete_value": true,
      "site": "00bf5488",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5060",
      "incomplete_value": true,
      "site": "00bf5060",
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
                "const:6:8"
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
      "definition_site": "00bf54b8",
      "incomplete_value": true,
      "site": "00bf54b8",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5090",
      "incomplete_value": true,
      "site": "00bf5090",
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
                "const:42e:8"
              ]
            ]
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
      "00bf5470",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf5474",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf54a8",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5470",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5474",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf54a8",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf4fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4f7c.md#insn-00bf4fc8) · [`00bf4fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4f7c.md#insn-00bf4fe0) · [`00bf5010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4f7c.md#insn-00bf5010)
- 新版 `00bf53f0`（命令位置の公開資料なし） · `00bf5408`（命令位置の公開資料なし） · `00bf5438`（命令位置の公開資料なし）

~~~diff
- 00bf4fc8 ["INT_ADD", "register:40f0:8", ["const:bf4fc8:8", "const:4:8"]]
- 00bf4fc8 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf53f0 ["INT_ADD", "register:40f0:8", ["const:bf53f0:8", "const:4:8"]]
+ 00bf53f0 ["CALL", null, ["callee:00c580c0:8"]]
- 00bf4fc8 bytes 3e8b0194
+ 00bf53f0 bytes 348b0194
- 00bf4fe0 ["INT_ADD", "register:40f0:8", ["const:bf4fe0:8", "const:4:8"]]
- 00bf4fe0 ["CALL", null, ["callee:00c585c0:8"]]
+ 00bf5408 ["INT_ADD", "register:40f0:8", ["const:bf5408:8", "const:4:8"]]
+ 00bf5408 ["CALL", null, ["callee:00c585c0:8"]]
- 00bf4fe0 bytes 788c0194
+ 00bf5408 bytes 6e8c0194
- 00bf5010 ["INT_ADD", "register:40f0:8", ["const:bf5010:8", "const:4:8"]]
- 00bf5010 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf5438 ["INT_ADD", "register:40f0:8", ["const:bf5438:8", "const:4:8"]]
+ 00bf5438 ["CALL", null, ["callee:00c5e050:8"]]
- 00bf5010 bytes 10a30194
+ 00bf5438 bytes 06a30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a28a68ca99c0d2e7dd56246ca92f2508"></a>

### [`00bf50c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf50c4.md) → [`00bf54ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf54ec.md) _ZNSt6__ndk15stoldERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.76% / 新版 88.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf55e0",
      "incomplete_value": true,
      "site": "00bf55e0",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf51b8",
      "incomplete_value": true,
      "site": "00bf51b8",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf55e4",
      "incomplete_value": true,
      "site": "00bf55e4",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf51bc",
      "incomplete_value": true,
      "site": "00bf51bc",
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
                "const:6:8"
              ]
            ]
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
      "definition_site": "00bf5620",
      "incomplete_value": true,
      "site": "00bf5620",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf51f8",
      "incomplete_value": true,
      "site": "00bf51f8",
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
                "const:42e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf55c8",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf55cc",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf5608",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf55c8",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf55cc",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5608",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf511c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf50c4.md#insn-00bf511c) · [`00bf5134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf50c4.md#insn-00bf5134) · [`00bf5164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf50c4.md#insn-00bf5164)
- 新版 `00bf5544`（命令位置の公開資料なし） · `00bf555c`（命令位置の公開資料なし） · `00bf558c`（命令位置の公開資料なし）

~~~diff
- 00bf511c ["INT_ADD", "register:40f0:8", ["const:bf511c:8", "const:4:8"]]
- 00bf511c ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf5544 ["INT_ADD", "register:40f0:8", ["const:bf5544:8", "const:4:8"]]
+ 00bf5544 ["CALL", null, ["callee:00c580c0:8"]]
- 00bf511c bytes e98a0194
+ 00bf5544 bytes df8a0194
- 00bf5134 ["INT_ADD", "register:40f0:8", ["const:bf5134:8", "const:4:8"]]
- 00bf5134 ["CALL", null, ["callee:00c5e080:8"]]
+ 00bf555c ["INT_ADD", "register:40f0:8", ["const:bf555c:8", "const:4:8"]]
+ 00bf555c ["CALL", null, ["callee:00c5e080:8"]]
- 00bf5134 bytes d3a20194
+ 00bf555c bytes c9a20194
- 00bf5164 ["INT_ADD", "register:40f0:8", ["const:bf5164:8", "const:4:8"]]
- 00bf5164 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf558c ["INT_ADD", "register:40f0:8", ["const:bf558c:8", "const:4:8"]]
+ 00bf558c ["CALL", null, ["callee:00c5e050:8"]]
- 00bf5164 bytes bba20194
+ 00bf558c bytes b1a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23dcbb29eede23dcdb10b965e4dce7cf"></a>

### [`00bf5228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5228.md) → [`00bf5650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5650.md) _ZNSt6__ndk14stoiERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00481e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md) [`00bf7d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7d54.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`00bf817c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.41% / 新版 92.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5778",
      "incomplete_value": true,
      "site": "00bf5778",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5350",
      "incomplete_value": true,
      "site": "00bf5350",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf5780",
      "incomplete_value": true,
      "site": "00bf5780",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5358",
      "incomplete_value": true,
      "site": "00bf5358",
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
                "const:6:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf5724",
      "incomplete_value": false,
      "site": "00bf5734",
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
            "const:dc6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf52fc",
      "incomplete_value": false,
      "site": "00bf530c",
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
            "const:d86:8"
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
      "00bf5724",
      "PARAM",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf5768",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf576c",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5724",
      "PARAM",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5768",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf576c",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf530c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5228.md#insn-00bf530c) · [`00bf527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5228.md#insn-00bf527c) · [`00bf5298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5228.md#insn-00bf5298)
- 新版 `00bf5734`（命令位置の公開資料なし） · `00bf56a4`（命令位置の公開資料なし） · `00bf56c0`（命令位置の公開資料なし）

~~~diff
- 00bf530c ["INT_ADD", "register:40f0:8", ["const:bf530c:8", "const:4:8"]]
- 00bf530c ["CALL", null, ["callee:00481e80:8"]]
+ 00bf5734 ["INT_ADD", "register:40f0:8", ["const:bf5734:8", "const:4:8"]]
+ 00bf5734 ["CALL", null, ["callee:00481e80:8"]]
- 00bf530c bytes cd32e297
+ 00bf5734 bytes d331e297
- 00bf527c ["INT_ADD", "register:40f0:8", ["const:bf527c:8", "const:4:8"]]
- 00bf527c ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf56a4 ["INT_ADD", "register:40f0:8", ["const:bf56a4:8", "const:4:8"]]
+ 00bf56a4 ["CALL", null, ["callee:00c580c0:8"]]
- 00bf527c bytes 918a0194
+ 00bf56a4 bytes 878a0194
- 00bf5298 ["INT_ADD", "register:40f0:8", ["const:bf5298:8", "const:4:8"]]
- 00bf5298 ["CALL", null, ["callee:00c5e090:8"]]
+ 00bf56c0 ["INT_ADD", "register:40f0:8", ["const:bf56c0:8", "const:4:8"]]
+ 00bf56c0 ["CALL", null, ["callee:00c5e090:8"]]
- 00bf5298 bytes 7ea20194
+ 00bf56c0 bytes 74a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f6808ccaf1a37cbf54786a4df348335"></a>

### [`00bf538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf538c.md) → [`00bf57b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf57b4.md) _ZNSt6__ndk14stolERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00481e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md) [`00bf7d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7d54.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`00bf817c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf5880",
      "incomplete_value": false,
      "site": "00bf5890",
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
            "const:dc6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5458",
      "incomplete_value": false,
      "site": "00bf5468",
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
            "const:d86:8"
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
      "00bf5880",
      "PARAM",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5880",
      "PARAM",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf538c.md#insn-00bf5468) · [`00bf53e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf538c.md#insn-00bf53e0) · [`00bf53fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf538c.md#insn-00bf53fc)
- 新版 `00bf5890`（命令位置の公開資料なし） · `00bf5808`（命令位置の公開資料なし） · `00bf5824`（命令位置の公開資料なし）

~~~diff
- 00bf5468 ["INT_ADD", "register:40f0:8", ["const:bf5468:8", "const:4:8"]]
- 00bf5468 ["CALL", null, ["callee:00481e80:8"]]
+ 00bf5890 ["INT_ADD", "register:40f0:8", ["const:bf5890:8", "const:4:8"]]
+ 00bf5890 ["CALL", null, ["callee:00481e80:8"]]
- 00bf5468 bytes 7632e297
+ 00bf5890 bytes 7c31e297
- 00bf53e0 ["INT_ADD", "register:40f0:8", ["const:bf53e0:8", "const:4:8"]]
- 00bf53e0 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf5808 ["INT_ADD", "register:40f0:8", ["const:bf5808:8", "const:4:8"]]
+ 00bf5808 ["CALL", null, ["callee:00c580c0:8"]]
- 00bf53e0 bytes 388a0194
+ 00bf5808 bytes 2e8a0194
- 00bf53fc ["INT_ADD", "register:40f0:8", ["const:bf53fc:8", "const:4:8"]]
- 00bf53fc ["CALL", null, ["callee:00c5e090:8"]]
+ 00bf5824 ["INT_ADD", "register:40f0:8", ["const:bf5824:8", "const:4:8"]]
+ 00bf5824 ["CALL", null, ["callee:00c5e090:8"]]
- 00bf53fc bytes 25a20194
+ 00bf5824 bytes 1ba20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1103a97bb603ca4942c3f5fdbd4d7840"></a>

### [`00bf54ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf54ac.md) → [`00bf58d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf58d4.md) _ZNSt6__ndk15stoulERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf59d8",
      "incomplete_value": true,
      "site": "00bf59d8",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf55b0",
      "incomplete_value": true,
      "site": "00bf55b0",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf59dc",
      "incomplete_value": true,
      "site": "00bf59dc",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf55b4",
      "incomplete_value": true,
      "site": "00bf55b4",
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
                "const:6:8"
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
      "definition_site": "00bf5a18",
      "incomplete_value": true,
      "site": "00bf5a18",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf55f0",
      "incomplete_value": true,
      "site": "00bf55f0",
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
                "const:42e:8"
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
      "00bf59c0",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf59c8",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf5a00",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf59c0",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf59c8",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5a00",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf54ac.md#insn-00bf5504) · [`00bf5520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf54ac.md#insn-00bf5520) · [`00bf555c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf54ac.md#insn-00bf555c)
- 新版 `00bf592c`（命令位置の公開資料なし） · `00bf5948`（命令位置の公開資料なし） · `00bf5984`（命令位置の公開資料なし）

~~~diff
- 00bf5504 ["INT_ADD", "register:40f0:8", ["const:bf5504:8", "const:4:8"]]
- 00bf5504 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf592c ["INT_ADD", "register:40f0:8", ["const:bf592c:8", "const:4:8"]]
+ 00bf592c ["CALL", null, ["callee:00c580c0:8"]]
- 00bf5504 bytes ef890194
+ 00bf592c bytes e5890194
- 00bf5520 ["INT_ADD", "register:40f0:8", ["const:bf5520:8", "const:4:8"]]
- 00bf5520 ["CALL", null, ["callee:00c5e0a0:8"]]
+ 00bf5948 ["INT_ADD", "register:40f0:8", ["const:bf5948:8", "const:4:8"]]
+ 00bf5948 ["CALL", null, ["callee:00c5e0a0:8"]]
- 00bf5520 bytes e0a10194
+ 00bf5948 bytes d6a10194
- 00bf555c ["INT_ADD", "register:40f0:8", ["const:bf555c:8", "const:4:8"]]
- 00bf555c ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf5984 ["INT_ADD", "register:40f0:8", ["const:bf5984:8", "const:4:8"]]
+ 00bf5984 ["CALL", null, ["callee:00c5e050:8"]]
- 00bf555c bytes bda10194
+ 00bf5984 bytes b3a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92cb91179f08e5a5583f1978c64151b3"></a>

### [`00bf5628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5628.md) → [`00bf5a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5a50.md) _ZNSt6__ndk15stollERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.36% / 新版 89.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5b54",
      "incomplete_value": true,
      "site": "00bf5b54",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf572c",
      "incomplete_value": true,
      "site": "00bf572c",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf5b58",
      "incomplete_value": true,
      "site": "00bf5b58",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5730",
      "incomplete_value": true,
      "site": "00bf5730",
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
                "const:6:8"
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
      "definition_site": "00bf5b94",
      "incomplete_value": true,
      "site": "00bf5b94",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf576c",
      "incomplete_value": true,
      "site": "00bf576c",
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
                "const:42e:8"
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
      "00bf5b3c",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf5b44",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf5b7c",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5b3c",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5b44",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5b7c",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5628.md#insn-00bf5680) · [`00bf569c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5628.md#insn-00bf569c) · [`00bf56d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5628.md#insn-00bf56d8)
- 新版 `00bf5aa8`（命令位置の公開資料なし） · `00bf5ac4`（命令位置の公開資料なし） · `00bf5b00`（命令位置の公開資料なし）

~~~diff
- 00bf5680 ["INT_ADD", "register:40f0:8", ["const:bf5680:8", "const:4:8"]]
- 00bf5680 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf5aa8 ["INT_ADD", "register:40f0:8", ["const:bf5aa8:8", "const:4:8"]]
+ 00bf5aa8 ["CALL", null, ["callee:00c580c0:8"]]
- 00bf5680 bytes 90890194
+ 00bf5aa8 bytes 86890194
- 00bf569c ["INT_ADD", "register:40f0:8", ["const:bf569c:8", "const:4:8"]]
- 00bf569c ["CALL", null, ["callee:00c5e0b0:8"]]
+ 00bf5ac4 ["INT_ADD", "register:40f0:8", ["const:bf5ac4:8", "const:4:8"]]
+ 00bf5ac4 ["CALL", null, ["callee:00c5e0b0:8"]]
- 00bf569c bytes 85a10194
+ 00bf5ac4 bytes 7ba10194
- 00bf56d8 ["INT_ADD", "register:40f0:8", ["const:bf56d8:8", "const:4:8"]]
- 00bf56d8 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf5b00 ["INT_ADD", "register:40f0:8", ["const:bf5b00:8", "const:4:8"]]
+ 00bf5b00 ["CALL", null, ["callee:00c5e050:8"]]
- 00bf56d8 bytes 5ea10194
+ 00bf5b00 bytes 54a10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-caa0ebfc4611e1e2272069e371bd16da"></a>

### [`00bf57a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf57a4.md) → [`00bf5bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5bcc.md) _ZNSt6__ndk16stoullERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5cd4",
      "incomplete_value": true,
      "site": "00bf5cd4",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf58ac",
      "incomplete_value": true,
      "site": "00bf58ac",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf5cd8",
      "incomplete_value": true,
      "site": "00bf5cd8",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf58b0",
      "incomplete_value": true,
      "site": "00bf58b0",
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
                "const:6:8"
              ]
            ]
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
      "definition_site": "00bf5d14",
      "incomplete_value": true,
      "site": "00bf5d14",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf58ec",
      "incomplete_value": true,
      "site": "00bf58ec",
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
                "const:42e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf5cbc",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf5cc4",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf5cfc",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5cbc",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5cc4",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5cfc",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf57a4.md#insn-00bf5800) · [`00bf581c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf57a4.md#insn-00bf581c) · [`00bf5858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf57a4.md#insn-00bf5858)
- 新版 `00bf5c28`（命令位置の公開資料なし） · `00bf5c44`（命令位置の公開資料なし） · `00bf5c80`（命令位置の公開資料なし）

~~~diff
- 00bf5800 ["INT_ADD", "register:40f0:8", ["const:bf5800:8", "const:4:8"]]
- 00bf5800 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf5c28 ["INT_ADD", "register:40f0:8", ["const:bf5c28:8", "const:4:8"]]
+ 00bf5c28 ["CALL", null, ["callee:00c580c0:8"]]
- 00bf5800 bytes 30890194
+ 00bf5c28 bytes 26890194
- 00bf581c ["INT_ADD", "register:40f0:8", ["const:bf581c:8", "const:4:8"]]
- 00bf581c ["CALL", null, ["callee:00c5e0c0:8"]]
+ 00bf5c44 ["INT_ADD", "register:40f0:8", ["const:bf5c44:8", "const:4:8"]]
+ 00bf5c44 ["CALL", null, ["callee:00c5e0c0:8"]]
- 00bf581c bytes 29a10194
+ 00bf5c44 bytes 1fa10194
- 00bf5858 ["INT_ADD", "register:40f0:8", ["const:bf5858:8", "const:4:8"]]
- 00bf5858 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf5c80 ["INT_ADD", "register:40f0:8", ["const:bf5c80:8", "const:4:8"]]
+ 00bf5c80 ["CALL", null, ["callee:00c5e050:8"]]
- 00bf5858 bytes fea00194
+ 00bf5c80 bytes f4a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e6498c86db5ce5c370340e6252043fc"></a>

### [`00bf5924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5924.md) → [`00bf5d4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5d4c.md) _ZNSt6__ndk14stofERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5e30",
      "incomplete_value": true,
      "site": "00bf5e30",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5a08",
      "incomplete_value": true,
      "site": "00bf5a08",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf5e38",
      "incomplete_value": true,
      "site": "00bf5e38",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5a10",
      "incomplete_value": true,
      "site": "00bf5a10",
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
                "const:6:8"
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
      "definition_site": "00bf5e68",
      "incomplete_value": true,
      "site": "00bf5e68",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5a40",
      "incomplete_value": true,
      "site": "00bf5a40",
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
                "const:42e:8"
              ]
            ]
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
      "00bf5e20",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf5e24",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf5e58",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5e20",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5e24",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5e58",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5924.md#insn-00bf5974) · [`00bf598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5924.md#insn-00bf598c) · [`00bf59c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5924.md#insn-00bf59c0)
- 新版 `00bf5d9c`（命令位置の公開資料なし） · `00bf5db4`（命令位置の公開資料なし） · `00bf5de8`（命令位置の公開資料なし）

~~~diff
- 00bf5974 ["INT_ADD", "register:40f0:8", ["const:bf5974:8", "const:4:8"]]
- 00bf5974 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf5d9c ["INT_ADD", "register:40f0:8", ["const:bf5d9c:8", "const:4:8"]]
+ 00bf5d9c ["CALL", null, ["callee:00c580c0:8"]]
- 00bf5974 bytes d3880194
+ 00bf5d9c bytes c9880194
- 00bf598c ["INT_ADD", "register:40f0:8", ["const:bf598c:8", "const:4:8"]]
- 00bf598c ["CALL", null, ["callee:00c5e0d0:8"]]
+ 00bf5db4 ["INT_ADD", "register:40f0:8", ["const:bf5db4:8", "const:4:8"]]
+ 00bf5db4 ["CALL", null, ["callee:00c5e0d0:8"]]
- 00bf598c bytes d1a00194
+ 00bf5db4 bytes c7a00194
- 00bf59c0 ["INT_ADD", "register:40f0:8", ["const:bf59c0:8", "const:4:8"]]
- 00bf59c0 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf5de8 ["INT_ADD", "register:40f0:8", ["const:bf5de8:8", "const:4:8"]]
+ 00bf5de8 ["CALL", null, ["callee:00c5e050:8"]]
- 00bf59c0 bytes a4a00194
+ 00bf5de8 bytes 9aa00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99c312a3a17cf71ad4231bb09ef4162a"></a>

### [`00bf5a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5a7c.md) → [`00bf5ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5ea4.md) _ZNSt6__ndk14stodERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf5f88",
      "incomplete_value": true,
      "site": "00bf5f88",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5b60",
      "incomplete_value": true,
      "site": "00bf5b60",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf5f90",
      "incomplete_value": true,
      "site": "00bf5f90",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5b68",
      "incomplete_value": true,
      "site": "00bf5b68",
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
                "const:6:8"
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
      "definition_site": "00bf5fc0",
      "incomplete_value": true,
      "site": "00bf5fc0",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5b98",
      "incomplete_value": true,
      "site": "00bf5b98",
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
                "const:42e:8"
              ]
            ]
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
      "00bf5f78",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf5f7c",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf5fb0",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf5f78",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf5f7c",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf5fb0",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5a7c.md#insn-00bf5acc) · [`00bf5ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5a7c.md#insn-00bf5ae4) · [`00bf5b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5a7c.md#insn-00bf5b18)
- 新版 `00bf5ef4`（命令位置の公開資料なし） · `00bf5f0c`（命令位置の公開資料なし） · `00bf5f40`（命令位置の公開資料なし）

~~~diff
- 00bf5acc ["INT_ADD", "register:40f0:8", ["const:bf5acc:8", "const:4:8"]]
- 00bf5acc ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf5ef4 ["INT_ADD", "register:40f0:8", ["const:bf5ef4:8", "const:4:8"]]
+ 00bf5ef4 ["CALL", null, ["callee:00c580c0:8"]]
- 00bf5acc bytes 7d880194
+ 00bf5ef4 bytes 73880194
- 00bf5ae4 ["INT_ADD", "register:40f0:8", ["const:bf5ae4:8", "const:4:8"]]
- 00bf5ae4 ["CALL", null, ["callee:00c5e0e0:8"]]
+ 00bf5f0c ["INT_ADD", "register:40f0:8", ["const:bf5f0c:8", "const:4:8"]]
+ 00bf5f0c ["CALL", null, ["callee:00c5e0e0:8"]]
- 00bf5ae4 bytes 7fa00194
+ 00bf5f0c bytes 75a00194
- 00bf5b18 ["INT_ADD", "register:40f0:8", ["const:bf5b18:8", "const:4:8"]]
- 00bf5b18 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf5f40 ["INT_ADD", "register:40f0:8", ["const:bf5f40:8", "const:4:8"]]
+ 00bf5f40 ["CALL", null, ["callee:00c5e050:8"]]
- 00bf5b18 bytes 4ea00194
+ 00bf5f40 bytes 44a00194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cde5ae7c74afa1d835269314da6c5c92"></a>

### [`00bf5bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5bd4.md) → [`00bf5ffc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5ffc.md) _ZNSt6__ndk15stoldERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf60f0",
      "incomplete_value": true,
      "site": "00bf60f0",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:dc6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5cc8",
      "incomplete_value": true,
      "site": "00bf5cc8",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:d86:8"
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
      "definition_site": "00bf60f4",
      "incomplete_value": true,
      "site": "00bf60f4",
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
                "const:6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5ccc",
      "incomplete_value": true,
      "site": "00bf5ccc",
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
                "const:6:8"
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
      "definition_site": "00bf6130",
      "incomplete_value": true,
      "site": "00bf6130",
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
                "const:50a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf5d08",
      "incomplete_value": true,
      "site": "00bf5d08",
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
                "const:42e:8"
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
      "00bf60d8",
      "READ",
      [
        "storage",
        "002b9d86",
        null,
        "string"
      ]
    ],
    [
      "00bf60e0",
      "READ",
      [
        "storage",
        "002b9d8c",
        null,
        "string"
      ]
    ],
    [
      "00bf6118",
      "READ",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf60d8",
      "READ",
      [
        "storage",
        "002b9dc6",
        null,
        "string"
      ]
    ],
    [
      "00bf60e0",
      "READ",
      [
        "storage",
        "002b9dcc",
        null,
        "string"
      ]
    ],
    [
      "00bf6118",
      "READ",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf5c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5bd4.md#insn-00bf5c24) · [`00bf5c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5bd4.md#insn-00bf5c3c) · [`00bf5c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5bd4.md#insn-00bf5c78)
- 新版 `00bf604c`（命令位置の公開資料なし） · `00bf6064`（命令位置の公開資料なし） · `00bf60a0`（命令位置の公開資料なし）

~~~diff
- 00bf5c24 ["INT_ADD", "register:40f0:8", ["const:bf5c24:8", "const:4:8"]]
- 00bf5c24 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf604c ["INT_ADD", "register:40f0:8", ["const:bf604c:8", "const:4:8"]]
+ 00bf604c ["CALL", null, ["callee:00c580c0:8"]]
- 00bf5c24 bytes 27880194
+ 00bf604c bytes 1d880194
- 00bf5c3c ["INT_ADD", "register:40f0:8", ["const:bf5c3c:8", "const:4:8"]]
- 00bf5c3c ["CALL", null, ["callee:00c5e0f0:8"]]
+ 00bf6064 ["INT_ADD", "register:40f0:8", ["const:bf6064:8", "const:4:8"]]
+ 00bf6064 ["CALL", null, ["callee:00c5e0f0:8"]]
- 00bf5c3c bytes 2da00194
+ 00bf6064 bytes 23a00194
- 00bf5c78 ["INT_ADD", "register:40f0:8", ["const:bf5c78:8", "const:4:8"]]
- 00bf5c78 ["CALL", null, ["callee:00c5e050:8"]]
+ 00bf60a0 ["INT_ADD", "register:40f0:8", ["const:bf60a0:8", "const:4:8"]]
+ 00bf60a0 ["CALL", null, ["callee:00c5e050:8"]]
- 00bf5c78 bytes f69f0194
+ 00bf60a0 bytes ec9f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0371040fb4f2d3eb79897bfd9de2591"></a>

### [`00bf798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf798c.md) → [`00bf7db4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf7/00bf7db4.md) _ZNSt6__ndk110to_wstringEf

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a490.md) [`00c5dd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd10.md) [`00c5dd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a890.md) [`00c5e110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e110.md) [`00c5e120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e120.md)

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
      "definition_site": "00bf7df0",
      "incomplete_value": true,
      "site": "00bf7df8",
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf79c8",
      "incomplete_value": true,
      "site": "00bf79d0",
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
                "const:240:8"
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
      "00bf7df0",
      "READ",
      [
        "storage",
        "002c3240",
        null,
        null
      ]
    ],
    [
      "00bf7e58",
      "PARAM",
      [
        "storage",
        "003104b4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf7df0",
      "READ",
      [
        "storage",
        "002c3280",
        null,
        null
      ]
    ],
    [
      "00bf7e58",
      "PARAM",
      [
        "storage",
        "003104f4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf79b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf798c.md#insn-00bf79b8) · [`00bf79c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf798c.md#insn-00bf79c8) · [`00bf79f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf798c.md#insn-00bf79f0)
- 新版 `00bf7de0`（命令位置の公開資料なし） · `00bf7df0`（命令位置の公開資料なし） · `00bf7e18`（命令位置の公開資料なし）

~~~diff
- 00bf79b8 ["INT_ADD", "register:40f0:8", ["const:bf79b8:8", "const:4:8"]]
- 00bf79b8 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf7de0 ["INT_ADD", "register:40f0:8", ["const:bf7de0:8", "const:4:8"]]
+ 00bf7de0 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf79b8 bytes 36800194
+ 00bf7de0 bytes 2c800194
- 00bf79c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:240:8"]]
- 00bf79c8 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00bf79c8 ["COPY", "register:5030:8", ["const:0:8"]]
- 00bf79c8 ["COPY", "register:5038:8", ["const:0:8"]]
+ 00bf7df0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
+ 00bf7df0 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bf7df0 ["COPY", "register:5030:8", ["const:0:8"]]
+ 00bf7df0 ["COPY", "register:5038:8", ["const:0:8"]]
- 00bf79c8 bytes 0191c03d
+ 00bf7df0 bytes 01a1c03d
- 00bf79f0 ["INT_ADD", "register:40f0:8", ["const:bf79f0:8", "const:4:8"]]
- 00bf79f0 ["CALL", null, ["callee:00c5a890:8"]]
+ 00bf7e18 ["INT_ADD", "register:40f0:8", ["const:bf7e18:8", "const:4:8"]]
+ 00bf7e18 ["CALL", null, ["callee:00c5a890:8"]]
- 00bf79f0 bytes a88a0194
+ 00bf7e18 bytes 9e8a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-600ca7d93a4b8429f2b585815e593854"></a>

### [`00bf7ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7ad4.md) → [`00bf7efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf7/00bf7efc.md) _ZNSt6__ndk110to_wstringEd

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a490.md) [`00c5dd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd10.md) [`00c5dd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a890.md) [`00c5e110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e110.md) [`00c5e120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e120.md)

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
      "definition_site": "00bf7f38",
      "incomplete_value": true,
      "site": "00bf7f40",
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf7b10",
      "incomplete_value": true,
      "site": "00bf7b18",
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
                "const:240:8"
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
      "00bf7f38",
      "READ",
      [
        "storage",
        "002c3240",
        null,
        null
      ]
    ],
    [
      "00bf7f9c",
      "PARAM",
      [
        "storage",
        "003104b4",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf7f38",
      "READ",
      [
        "storage",
        "002c3280",
        null,
        null
      ]
    ],
    [
      "00bf7f9c",
      "PARAM",
      [
        "storage",
        "003104f4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf7b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7ad4.md#insn-00bf7b00) · [`00bf7b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7ad4.md#insn-00bf7b10) · [`00bf7b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7ad4.md#insn-00bf7b38)
- 新版 `00bf7f28`（命令位置の公開資料なし） · `00bf7f38`（命令位置の公開資料なし） · `00bf7f60`（命令位置の公開資料なし）

~~~diff
- 00bf7b00 ["INT_ADD", "register:40f0:8", ["const:bf7b00:8", "const:4:8"]]
- 00bf7b00 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf7f28 ["INT_ADD", "register:40f0:8", ["const:bf7f28:8", "const:4:8"]]
+ 00bf7f28 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf7b00 bytes e47f0194
+ 00bf7f28 bytes da7f0194
- 00bf7b10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:240:8"]]
- 00bf7b10 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00bf7b10 ["COPY", "register:5030:8", ["const:0:8"]]
- 00bf7b10 ["COPY", "register:5038:8", ["const:0:8"]]
+ 00bf7f38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
+ 00bf7f38 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bf7f38 ["COPY", "register:5030:8", ["const:0:8"]]
+ 00bf7f38 ["COPY", "register:5038:8", ["const:0:8"]]
- 00bf7b10 bytes 0191c03d
+ 00bf7f38 bytes 01a1c03d
- 00bf7b38 ["INT_ADD", "register:40f0:8", ["const:bf7b38:8", "const:4:8"]]
- 00bf7b38 ["CALL", null, ["callee:00c5a890:8"]]
+ 00bf7f60 ["INT_ADD", "register:40f0:8", ["const:bf7f60:8", "const:4:8"]]
+ 00bf7f60 ["CALL", null, ["callee:00c5a890:8"]]
- 00bf7b38 bytes 568a0194
+ 00bf7f60 bytes 4c8a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13263f3bf86f33e7abebd05b7655fe1c"></a>

### [`00bf7c18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7c18.md) → [`00bf8040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8040.md) _ZNSt6__ndk110to_wstringEe

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c5a490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a490.md) [`00c5dd10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd10.md) [`00c5dd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c5a890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a890.md) [`00c5e110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e110.md) [`00c5e120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf8078",
      "incomplete_value": true,
      "site": "00bf8080",
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf7c50",
      "incomplete_value": true,
      "site": "00bf7c58",
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
                "const:240:8"
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
      "00bf8078",
      "READ",
      [
        "storage",
        "002c3240",
        null,
        null
      ]
    ],
    [
      "00bf80dc",
      "PARAM",
      [
        "storage",
        "00310524",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf8078",
      "READ",
      [
        "storage",
        "002c3280",
        null,
        null
      ]
    ],
    [
      "00bf80dc",
      "PARAM",
      [
        "storage",
        "00310564",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf7c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7c18.md#insn-00bf7c40) · [`00bf7c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7c18.md#insn-00bf7c50) · [`00bf7c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7c18.md#insn-00bf7c78)
- 新版 `00bf8068`（命令位置の公開資料なし） · `00bf8078`（命令位置の公開資料なし） · `00bf80a0`（命令位置の公開資料なし）

~~~diff
- 00bf7c40 ["INT_ADD", "register:40f0:8", ["const:bf7c40:8", "const:4:8"]]
- 00bf7c40 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf8068 ["INT_ADD", "register:40f0:8", ["const:bf8068:8", "const:4:8"]]
+ 00bf8068 ["CALL", null, ["callee:00c57e90:8"]]
- 00bf7c40 bytes 947f0194
+ 00bf8068 bytes 8a7f0194
- 00bf7c50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:240:8"]]
- 00bf7c50 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00bf7c50 ["COPY", "register:5030:8", ["const:0:8"]]
- 00bf7c50 ["COPY", "register:5038:8", ["const:0:8"]]
+ 00bf8078 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
+ 00bf8078 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bf8078 ["COPY", "register:5030:8", ["const:0:8"]]
+ 00bf8078 ["COPY", "register:5038:8", ["const:0:8"]]
- 00bf7c50 bytes 0191c03d
+ 00bf8078 bytes 01a1c03d
- 00bf7c78 ["INT_ADD", "register:40f0:8", ["const:bf7c78:8", "const:4:8"]]
- 00bf7c78 ["CALL", null, ["callee:00c5a890:8"]]
+ 00bf80a0 ["INT_ADD", "register:40f0:8", ["const:bf80a0:8", "const:4:8"]]
+ 00bf80a0 ["CALL", null, ["callee:00c5a890:8"]]
- 00bf7c78 bytes 068a0194
+ 00bf80a0 bytes fc890194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9843ee5f0521fd6a7f7e6fd2fcb7fe11"></a>

### [`00bf7d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7d54.md) → [`00bf817c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf817c.md) FUN_00bf817c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00bf4778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4778.md) [`00bf48d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf48d4.md) [`00bf5228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf5228.md) [`00bf538c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf538c.md) · 呼出先 4件 [`00481e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md) [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c5dc50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dc50.md)
- 新版 呼出元 4件 [`00bf4ba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4ba0.md) [`00bf4cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4cfc.md) [`00bf5650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5650.md) [`00bf57b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf57b4.md) · 呼出先 4件 [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c5e050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf8194",
      "incomplete_value": false,
      "site": "00bf81a0",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf7d6c",
      "incomplete_value": false,
      "site": "00bf7d78",
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
            "const:42e:8"
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
      "00bf8194",
      "PARAM",
      [
        "storage",
        "002a742e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf8194",
      "PARAM",
      [
        "storage",
        "002a750a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf7d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7d54.md#insn-00bf7d78) · [`00bf7d6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7d54.md#insn-00bf7d6c) · [`00bf7d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7d54.md#insn-00bf7d8c)
- 新版 `00bf81a0`（命令位置の公開資料なし） · `00bf8194`（命令位置の公開資料なし） · `00bf81b4`（命令位置の公開資料なし）

~~~diff
- 00bf7d78 ["INT_ADD", "register:40f0:8", ["const:bf7d78:8", "const:4:8"]]
- 00bf7d78 ["CALL", null, ["callee:00481e80:8"]]
+ 00bf81a0 ["INT_ADD", "register:40f0:8", ["const:bf81a0:8", "const:4:8"]]
+ 00bf81a0 ["CALL", null, ["callee:00481e80:8"]]
- 00bf7d78 bytes 3228e297
+ 00bf81a0 bytes 3827e297
- 00bf7d6c ["COPY", "tmp:0:8", ["const:42e:8"]]
- 00bf7d6c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bf7d6c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bf7d6c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bf8194 ["COPY", "tmp:0:8", ["const:50a:8"]]
+ 00bf8194 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf8194 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf8194 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bf7d6c bytes 21b81091
+ 00bf8194 bytes 21281491
- 00bf7d8c ["INT_ADD", "register:40f0:8", ["const:bf7d8c:8", "const:4:8"]]
- 00bf7d8c ["CALL", null, ["callee:00bf81cc:8"]]
+ 00bf81b4 ["INT_ADD", "register:40f0:8", ["const:bf81b4:8", "const:4:8"]]
+ 00bf81b4 ["CALL", null, ["callee:00bf81cc:8"]]
- 00bf7d8c bytes 06000094
+ 00bf81b4 bytes 06000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-162e23685bcc7c3ede4151c60cb956be"></a>

### [`00bf7da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md) → [`00bf81cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf81cc.md) FUN_00bf81cc

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 13件 [`00bf49ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf49ec.md) [`00bf4b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4b58.md) [`00bf4cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4cc4.md) [`00bf4e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4e34.md) [`00bf4f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf4f7c.md) · 呼出先 4件 [`00bf7df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7df8.md) [`00c378a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c378a4.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 13件 [`00bf4e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4e14.md) [`00bf4f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4f80.md) [`00bf50ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf50ec.md) [`00bf525c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf525c.md) [`00bf53a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf53a4.md) · 呼出先 4件 [`00bf8220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8220.md) [`00c37ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ccc.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf8200",
      "incomplete_value": true,
      "site": "00bf8208",
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf7dd8",
      "incomplete_value": true,
      "site": "00bf7de0",
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
                "const:6b8:8"
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
      "definition_site": "00bf8204",
      "incomplete_value": true,
      "site": "00bf8208",
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
                "const:ac0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf7ddc",
      "incomplete_value": true,
      "site": "00bf7de0",
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
                "const:6c0:8"
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
      "00bf8200",
      "READ",
      [
        "storage",
        "00c9b6b8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8200",
      "PARAM",
      [
        "storage",
        "00c96398",
        "_ZTISt16invalid_argument",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf8204",
      "READ",
      [
        "storage",
        "00c9b6c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf8200",
      "READ",
      [
        "storage",
        "00c9bab8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8200",
      "PARAM",
      [
        "storage",
        "00c96798",
        "_ZTISt16invalid_argument",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf8204",
      "READ",
      [
        "storage",
        "00c9bac0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf7de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md#insn-00bf7de0) · [`00bf7dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md#insn-00bf7dbc) · [`00bf7dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf7/00bf7da4.md#insn-00bf7dc8)
- 新版 `00bf8208`（命令位置の公開資料なし） · `00bf81e4`（命令位置の公開資料なし） · `00bf81f0`（命令位置の公開資料なし）

~~~diff
- 00bf7de0 ["INT_ADD", "register:40f0:8", ["const:bf7de0:8", "const:4:8"]]
- 00bf7de0 ["CALL", null, ["callee:00c57f10:8"]]
+ 00bf8208 ["INT_ADD", "register:40f0:8", ["const:bf8208:8", "const:4:8"]]
+ 00bf8208 ["CALL", null, ["callee:00c57f10:8"]]
- 00bf7de0 bytes 4c7f0194
+ 00bf8208 bytes 427f0194
- 00bf7dbc ["INT_ADD", "register:40f0:8", ["const:bf7dbc:8", "const:4:8"]]
- 00bf7dbc ["CALL", null, ["callee:00c57ef0:8"]]
+ 00bf81e4 ["INT_ADD", "register:40f0:8", ["const:bf81e4:8", "const:4:8"]]
+ 00bf81e4 ["CALL", null, ["callee:00c57ef0:8"]]
- 00bf7dbc bytes 4d7f0194
+ 00bf81e4 bytes 437f0194
- 00bf7dc8 ["INT_ADD", "register:40f0:8", ["const:bf7dc8:8", "const:4:8"]]
- 00bf7dc8 ["CALL", null, ["callee:00bf8220:8"]]
+ 00bf81f0 ["INT_ADD", "register:40f0:8", ["const:bf81f0:8", "const:4:8"]]
+ 00bf81f0 ["CALL", null, ["callee:00bf8220:8"]]
- 00bf7dc8 bytes 0c000094
+ 00bf81f0 bytes 0c000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73eca6ff8902a082306d65a7b4f5e63c"></a>

### [`00bf81e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf81e8.md) → [`00bf8610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8610.md) FUN_00bf8610

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00bf831c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf831c.md) [`00bf83e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf83e4.md) [`00bfaa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaa50.md) · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md)
- 新版 呼出元 3件 [`00bf8744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8744.md) [`00bf880c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf880c.md) [`00bfae78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfae78.md) · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf8680",
      "incomplete_value": false,
      "site": "00bf8694",
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
            "const:e5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8258",
      "incomplete_value": false,
      "site": "00bf826c",
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
            "const:e1b:8"
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
      "00bf8674",
      "READ",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf8680",
      "PARAM",
      [
        "storage",
        "002b7e1b",
        null,
        "string"
      ]
    ],
    [
      "00bf8698",
      "PARAM",
      [
        "storage",
        "002a630e",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bf8674",
      "READ",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf8680",
      "PARAM",
      [
        "storage",
        "002b7e5b",
        null,
        "string"
      ]
    ],
    [
      "00bf8698",
      "PARAM",
      [
        "storage",
        "002a63ea",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf826c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf81e8.md#insn-00bf826c) · [`00bf820c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf81e8.md#insn-00bf820c) · [`00bf8228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf81e8.md#insn-00bf8228)
- 新版 `00bf8694`（命令位置の公開資料なし） · `00bf8634`（命令位置の公開資料なし） · `00bf8650`（命令位置の公開資料なし）

~~~diff
- 00bf826c ["INT_ADD", "register:40f0:8", ["const:bf826c:8", "const:4:8"]]
- 00bf826c ["CALL", null, ["callee:00c5e100:8"]]
+ 00bf8694 ["INT_ADD", "register:40f0:8", ["const:bf8694:8", "const:4:8"]]
+ 00bf8694 ["CALL", null, ["callee:00c5e100:8"]]
- 00bf826c bytes a5960194
+ 00bf8694 bytes 9b960194
- 00bf820c ["INT_ADD", "register:40f0:8", ["const:bf820c:8", "const:4:8"]]
- 00bf820c ["CALL", null, ["callee:00c580c0:8"]]
+ 00bf8634 ["INT_ADD", "register:40f0:8", ["const:bf8634:8", "const:4:8"]]
+ 00bf8634 ["CALL", null, ["callee:00c580c0:8"]]
- 00bf820c bytes ad7e0194
+ 00bf8634 bytes a37e0194
- 00bf8228 ["INT_ADD", "register:40f0:8", ["const:bf8228:8", "const:4:8"]]
- 00bf8228 ["CALL", null, ["callee:00c5e190:8"]]
+ 00bf8650 ["INT_ADD", "register:40f0:8", ["const:bf8650:8", "const:4:8"]]
+ 00bf8650 ["CALL", null, ["callee:00c5e190:8"]]
- 00bf8228 bytes da960194
+ 00bf8650 bytes d0960194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec75e77666056668a33479fca17ce8a6"></a>

### [`00bf8384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8384.md) → [`00bf87ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf87ac.md) _ZNSt6__ndk116generic_categoryEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf87e0",
      "incomplete_value": false,
      "site": "00bf87e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf83b8",
      "incomplete_value": false,
      "site": "00bf83bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf87f0",
      "incomplete_value": false,
      "site": "00bf87f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf83c8",
      "incomplete_value": false,
      "site": "00bf83cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf87cc",
      "incomplete_value": false,
      "site": "00bf87d8",
      "value": [
        "leaf",
        "const:ca47e8:8"
      ]
    },
    "old": {
      "definition_site": "00bf83a4",
      "incomplete_value": false,
      "site": "00bf83b0",
      "value": [
        "leaf",
        "const:ca43e8:8"
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
      "00bf87c0",
      "READ",
      [
        "storage",
        "01126f60",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf87cc",
      "DATA",
      [
        "storage",
        "00ca43e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf87e0",
      "PARAM",
      [
        "storage",
        "01126f60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bf87c0",
      "READ",
      [
        "storage",
        "01127360",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf87cc",
      "DATA",
      [
        "storage",
        "00ca47e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bf87e0",
      "PARAM",
      [
        "storage",
        "01127360",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf83bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8384.md#insn-00bf83bc) · [`00bf83cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8384.md#insn-00bf83cc) · [`00bf8390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8384.md#insn-00bf8390)
- 新版 `00bf87e4`（命令位置の公開資料なし） · `00bf87f4`（命令位置の公開資料なし） · `00bf87b8`（命令位置の公開資料なし）

~~~diff
- 00bf83bc ["INT_ADD", "register:40f0:8", ["const:bf83bc:8", "const:4:8"]]
- 00bf83bc ["CALL", null, ["callee:00c57e50:8"]]
+ 00bf87e4 ["INT_ADD", "register:40f0:8", ["const:bf87e4:8", "const:4:8"]]
+ 00bf87e4 ["CALL", null, ["callee:00c57e50:8"]]
- 00bf83bc bytes a57d0194
+ 00bf87e4 bytes 9b7d0194
- 00bf83cc ["INT_ADD", "register:40f0:8", ["const:bf83cc:8", "const:4:8"]]
- 00bf83cc ["CALL", null, ["callee:00c57e70:8"]]
+ 00bf87f4 ["INT_ADD", "register:40f0:8", ["const:bf87f4:8", "const:4:8"]]
+ 00bf87f4 ["CALL", null, ["callee:00c57e70:8"]]
- 00bf83cc bytes a97d0194
+ 00bf87f4 bytes 9f7d0194
- 00bf8390 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bf87b8 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bf8390 bytes 682900d0
+ 00bf87b8 bytes 682900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c0aafc45e03e4d41dfe298d9eace689"></a>

### [`00bf846c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf846c.md) → [`00bf8894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8894.md) _ZNSt6__ndk115system_categoryEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf88c8",
      "incomplete_value": false,
      "site": "00bf88cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf84a0",
      "incomplete_value": false,
      "site": "00bf84a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf88d8",
      "incomplete_value": false,
      "site": "00bf88dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf84b0",
      "incomplete_value": false,
      "site": "00bf84b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf88b4",
      "incomplete_value": false,
      "site": "00bf88c0",
      "value": [
        "leaf",
        "const:ca47f0:8"
      ]
    },
    "old": {
      "definition_site": "00bf848c",
      "incomplete_value": false,
      "site": "00bf8498",
      "value": [
        "leaf",
        "const:ca43f0:8"
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
      "00bf88a8",
      "READ",
      [
        "storage",
        "01126f68",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf88b4",
      "DATA",
      [
        "storage",
        "00ca43f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf88c8",
      "PARAM",
      [
        "storage",
        "01126f68",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bf88a8",
      "READ",
      [
        "storage",
        "01127368",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf88b4",
      "DATA",
      [
        "storage",
        "00ca47f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf88c8",
      "PARAM",
      [
        "storage",
        "01127368",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf84a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf846c.md#insn-00bf84a4) · [`00bf84b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf846c.md#insn-00bf84b4) · [`00bf8478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf846c.md#insn-00bf8478)
- 新版 `00bf88cc`（命令位置の公開資料なし） · `00bf88dc`（命令位置の公開資料なし） · `00bf88a0`（命令位置の公開資料なし）

~~~diff
- 00bf84a4 ["INT_ADD", "register:40f0:8", ["const:bf84a4:8", "const:4:8"]]
- 00bf84a4 ["CALL", null, ["callee:00c57e50:8"]]
+ 00bf88cc ["INT_ADD", "register:40f0:8", ["const:bf88cc:8", "const:4:8"]]
+ 00bf88cc ["CALL", null, ["callee:00c57e50:8"]]
- 00bf84a4 bytes 6b7d0194
+ 00bf88cc bytes 617d0194
- 00bf84b4 ["INT_ADD", "register:40f0:8", ["const:bf84b4:8", "const:4:8"]]
- 00bf84b4 ["CALL", null, ["callee:00c57e70:8"]]
+ 00bf88dc ["INT_ADD", "register:40f0:8", ["const:bf88dc:8", "const:4:8"]]
+ 00bf88dc ["CALL", null, ["callee:00c57e70:8"]]
- 00bf84b4 bytes 6f7d0194
+ 00bf88dc bytes 657d0194
- 00bf8478 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bf88a0 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bf8478 bytes 682900d0
+ 00bf88a0 bytes 682900f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fbf0a563e3eb78c4ad47eaa9d90f52d"></a>

### [`00bf85ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf85ec.md) → [`00bf8a14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8a14.md) FUN_00bf8a14

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00bf84f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf84f4.md) [`00bf86c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf86c0.md) [`00bf88d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf88d4.md) [`00bf89e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf89e0.md) · 呼出先 3件 [`007dcedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dc/007dcedc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)
- 新版 呼出元 4件 [`00bf891c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf891c.md) [`00bf8ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8ae8.md) [`00bf8cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8cfc.md) [`00bf8e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf8/00bf8e08.md) · 呼出先 3件 [`007dcf1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007dc/007dcf1c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf8a5c",
      "incomplete_value": false,
      "site": "00bf8a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:76e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8634",
      "incomplete_value": false,
      "site": "00bf863c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:72e:8"
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
      "00bf8a5c",
      "PARAM",
      [
        "storage",
        "002bd72e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf8a5c",
      "PARAM",
      [
        "storage",
        "002bd76e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf863c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf85ec.md#insn-00bf863c) · [`00bf8634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf85ec.md#insn-00bf8634) · [`00bf8654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf85ec.md#insn-00bf8654)
- 新版 `00bf8a64`（命令位置の公開資料なし） · `00bf8a5c`（命令位置の公開資料なし） · `00bf8a7c`（命令位置の公開資料なし）

~~~diff
- 00bf863c ["INT_ADD", "register:40f0:8", ["const:bf863c:8", "const:4:8"]]
- 00bf863c ["CALL", null, ["callee:00c57f70:8"]]
+ 00bf8a64 ["INT_ADD", "register:40f0:8", ["const:bf8a64:8", "const:4:8"]]
+ 00bf8a64 ["CALL", null, ["callee:00c57f70:8"]]
- 00bf863c bytes 4d7d0194
+ 00bf8a64 bytes 437d0194
- 00bf8634 ["COPY", "tmp:0:8", ["const:72e:8"]]
- 00bf8634 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bf8634 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bf8634 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bf8a5c ["COPY", "tmp:0:8", ["const:76e:8"]]
+ 00bf8a5c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf8a5c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf8a5c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bf8634 bytes 21b81c91
+ 00bf8a5c bytes 21b81d91
- 00bf8654 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bf8654 ["INT_ADD", "register:40f0:8", ["const:bf8654:8", "const:4:8"]]
- 00bf8654 ["CALLIND", null, ["register:0:8"]]
+ 00bf8a7c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bf8a7c ["INT_ADD", "register:40f0:8", ["const:bf8a7c:8", "const:4:8"]]
+ 00bf8a7c ["CALLIND", null, ["register:0:8"]]
- 00bf8654 bytes 20013fd6
+ 00bf8a7c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d404ea2b8390fee52282ec11a44ac76e"></a>

### [`00bf8c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c60.md) → [`00bf9088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9088.md) FUN_00bf9088

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bf8c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c40.md) · 呼出先 4件 [`00bf8c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c0c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5ddb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddb0.md)
- 新版 呼出元 1件 [`00bf9068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9068.md) · 呼出先 4件 [`00bf9034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9034.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c5e1b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf90d0",
      "incomplete_value": true,
      "site": "00bf90d8",
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
                "const:ae0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8ca8",
      "incomplete_value": true,
      "site": "00bf8cb0",
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
                "const:6e0:8"
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
      "definition_site": "00bf90d4",
      "incomplete_value": true,
      "site": "00bf90d8",
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
                "const:ad8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf8cac",
      "incomplete_value": true,
      "site": "00bf8cb0",
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
                "const:6d8:8"
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
      "00bf90d0",
      "READ",
      [
        "storage",
        "00c9b6e0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf90d0",
      "PARAM",
      [
        "storage",
        "00c927a0",
        "_ZTINSt6__ndk112system_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf90d4",
      "READ",
      [
        "storage",
        "00c9b6d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf90d0",
      "READ",
      [
        "storage",
        "00c9bae0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf90d0",
      "PARAM",
      [
        "storage",
        "00c92ba0",
        "_ZTINSt6__ndk112system_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bf90d4",
      "READ",
      [
        "storage",
        "00c9bad8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf8cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c60.md#insn-00bf8cb0) · [`00bf8c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c60.md#insn-00bf8c84) · [`00bf8c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c60.md#insn-00bf8c98)
- 新版 `00bf90d8`（命令位置の公開資料なし） · `00bf90ac`（命令位置の公開資料なし） · `00bf90c0`（命令位置の公開資料なし）

~~~diff
- 00bf8cb0 ["INT_ADD", "register:40f0:8", ["const:bf8cb0:8", "const:4:8"]]
- 00bf8cb0 ["CALL", null, ["callee:00c57f10:8"]]
+ 00bf90d8 ["INT_ADD", "register:40f0:8", ["const:bf90d8:8", "const:4:8"]]
+ 00bf90d8 ["CALL", null, ["callee:00c57f10:8"]]
- 00bf8cb0 bytes 987b0194
+ 00bf90d8 bytes 8e7b0194
- 00bf8c84 ["INT_ADD", "register:40f0:8", ["const:bf8c84:8", "const:4:8"]]
- 00bf8c84 ["CALL", null, ["callee:00c57ef0:8"]]
+ 00bf90ac ["INT_ADD", "register:40f0:8", ["const:bf90ac:8", "const:4:8"]]
+ 00bf90ac ["CALL", null, ["callee:00c57ef0:8"]]
- 00bf8c84 bytes 9b7b0194
+ 00bf90ac bytes 917b0194
- 00bf8c98 ["INT_ADD", "register:40f0:8", ["const:bf8c98:8", "const:4:8"]]
- 00bf8c98 ["CALL", null, ["callee:00c5e1b0:8"]]
+ 00bf90c0 ["INT_ADD", "register:40f0:8", ["const:bf90c0:8", "const:4:8"]]
+ 00bf90c0 ["CALL", null, ["callee:00c5e1b0:8"]]
- 00bf8c98 bytes 46940194
+ 00bf90c0 bytes 3c940194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5afa15c6a34a2818d50ade333b26eef9"></a>

### [`00bf9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9134.md) → [`00bf955c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf955c.md) _ZNSt6__ndk115future_categoryEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f10.md) · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c58310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58310.md) · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9590",
      "incomplete_value": false,
      "site": "00bf9594",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9168",
      "incomplete_value": false,
      "site": "00bf916c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf95a0",
      "incomplete_value": false,
      "site": "00bf95a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9178",
      "incomplete_value": false,
      "site": "00bf917c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf957c",
      "incomplete_value": false,
      "site": "00bf9588",
      "value": [
        "leaf",
        "const:ca47f8:8"
      ]
    },
    "old": {
      "definition_site": "00bf9154",
      "incomplete_value": false,
      "site": "00bf9160",
      "value": [
        "leaf",
        "const:ca43f8:8"
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
      "00bf9570",
      "READ",
      [
        "storage",
        "01126f70",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf957c",
      "DATA",
      [
        "storage",
        "00ca43f8",
        null,
        null
      ]
    ],
    [
      "00bf9590",
      "PARAM",
      [
        "storage",
        "01126f70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bf9570",
      "READ",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf957c",
      "DATA",
      [
        "storage",
        "00ca47f8",
        null,
        null
      ]
    ],
    [
      "00bf9590",
      "PARAM",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf916c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9134.md#insn-00bf916c) · [`00bf917c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9134.md#insn-00bf917c) · [`00bf9140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9134.md#insn-00bf9140)
- 新版 `00bf9594`（命令位置の公開資料なし） · `00bf95a4`（命令位置の公開資料なし） · `00bf9568`（命令位置の公開資料なし）

~~~diff
- 00bf916c ["INT_ADD", "register:40f0:8", ["const:bf916c:8", "const:4:8"]]
- 00bf916c ["CALL", null, ["callee:00c57e50:8"]]
+ 00bf9594 ["INT_ADD", "register:40f0:8", ["const:bf9594:8", "const:4:8"]]
+ 00bf9594 ["CALL", null, ["callee:00c57e50:8"]]
- 00bf916c bytes 397a0194
+ 00bf9594 bytes 2f7a0194
- 00bf917c ["INT_ADD", "register:40f0:8", ["const:bf917c:8", "const:4:8"]]
- 00bf917c ["CALL", null, ["callee:00c57e70:8"]]
+ 00bf95a4 ["INT_ADD", "register:40f0:8", ["const:bf95a4:8", "const:4:8"]]
+ 00bf95a4 ["CALL", null, ["callee:00c57e70:8"]]
- 00bf917c bytes 3d7a0194
+ 00bf95a4 bytes 337a0194
- 00bf9140 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bf9568 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bf9140 bytes 682900b0
+ 00bf9568 bytes 682900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ab61a0828189d280c0e849c5f7dabda"></a>

### [`00bf95e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf95e8.md) → [`00bf9a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9a10.md) _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c580a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580a0.md) · 呼出先 3件 [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md)
- 新版 呼出元 1件 [`00c584a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584a0.md) · 呼出先 3件 [`00c580f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580f0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9a94",
      "incomplete_value": false,
      "site": "00bf9a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:a1b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf966c",
      "incomplete_value": false,
      "site": "00bf9674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:9db:8"
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
      "00bf9a94",
      "PARAM",
      [
        "storage",
        "002be9db",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf9a94",
      "PARAM",
      [
        "storage",
        "002bea1b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf95e8.md#insn-00bf9674) · [`00bf9614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf95e8.md#insn-00bf9614) · [`00bf9644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf95e8.md#insn-00bf9644)
- 新版 `00bf9a9c`（命令位置の公開資料なし） · `00bf9a3c`（命令位置の公開資料なし） · `00bf9a6c`（命令位置の公開資料なし）

~~~diff
- 00bf9674 ["INT_ADD", "register:40f0:8", ["const:bf9674:8", "const:4:8"]]
- 00bf9674 ["CALL", null, ["callee:00c58120:8"]]
+ 00bf9a9c ["INT_ADD", "register:40f0:8", ["const:bf9a9c:8", "const:4:8"]]
+ 00bf9a9c ["CALL", null, ["callee:00c58120:8"]]
- 00bf9674 bytes ab790194
+ 00bf9a9c bytes a1790194
- 00bf9614 ["INT_ADD", "register:40f0:8", ["const:bf9614:8", "const:4:8"]]
- 00bf9614 ["CALL", null, ["callee:00c58480:8"]]
+ 00bf9a3c ["INT_ADD", "register:40f0:8", ["const:bf9a3c:8", "const:4:8"]]
+ 00bf9a3c ["CALL", null, ["callee:00c58480:8"]]
- 00bf9614 bytes 9b7a0194
+ 00bf9a3c bytes 917a0194
- 00bf9644 ["INT_ADD", "register:40f0:8", ["const:bf9644:8", "const:4:8"]]
- 00bf9644 ["CALL", null, ["callee:00c580f0:8"]]
+ 00bf9a6c ["INT_ADD", "register:40f0:8", ["const:bf9a6c:8", "const:4:8"]]
+ 00bf9a6c ["CALL", null, ["callee:00c580f0:8"]]
- 00bf9644 bytes ab790194
+ 00bf9a6c bytes a1790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-525d49160c6024f73865de613f08dc5a"></a>

### [`00bf987c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf987c.md) → [`00bf9ca4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9ca4.md) _ZNSt6__ndk17promiseIvEC1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf9cd4",
      "incomplete_value": true,
      "site": "00bf9cd4",
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
      "definition_site": "00bf98ac",
      "incomplete_value": true,
      "site": "00bf98ac",
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
      "00bf9cc8",
      "READ",
      [
        "storage",
        "00c9a850",
        null,
        "pointer"
      ]
    ],
    [
      "00bf9cd4",
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
      "00bf9cc8",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "00bf9cd4",
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

- 旧版 [`00bf9894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf987c.md#insn-00bf9894) · [`00bf98a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf987c.md#insn-00bf98a0)
- 新版 `00bf9cbc`（命令位置の公開資料なし） · `00bf9cc8`（命令位置の公開資料なし）

~~~diff
- 00bf9894 ["INT_ADD", "register:40f0:8", ["const:bf9894:8", "const:4:8"]]
- 00bf9894 ["CALL", null, ["callee:00c57e90:8"]]
+ 00bf9cbc ["INT_ADD", "register:40f0:8", ["const:bf9cbc:8", "const:4:8"]]
+ 00bf9cbc ["CALL", null, ["callee:00c57e90:8"]]
- 00bf9894 bytes 7f780194
+ 00bf9cbc bytes 75780194
- 00bf98a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:850:8"]]
- 00bf98a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf9cc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
+ 00bf9cc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf98a0 bytes 082944f9
+ 00bf9cc8 bytes 082946f9
~~~


<a id="compare-aad3a722238e6913b5515181313bf495"></a>

### [`00bf98d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf98d0.md) → [`00bf9cf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9cf8.md) _ZNSt6__ndk17promiseIvED1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0045a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a688.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0045a6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0045a/0045a6c8.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.11% / 新版 90.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf9d64",
      "incomplete_value": false,
      "site": "00bf9d64",
      "value": [
        "leaf",
        "const:ca47f8:8"
      ]
    },
    "old": {
      "definition_site": "00bf993c",
      "incomplete_value": false,
      "site": "00bf993c",
      "value": [
        "leaf",
        "const:ca43f8:8"
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf9da0",
      "incomplete_value": true,
      "site": "00bf9da8",
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
      "definition_site": "00bf9978",
      "incomplete_value": true,
      "site": "00bf9980",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9dbc",
      "incomplete_value": true,
      "site": "00bf9dc4",
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9994",
      "incomplete_value": true,
      "site": "00bf999c",
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
                "const:858:8"
              ]
            ]
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
      "00bf9d50",
      "READ",
      [
        "storage",
        "01126f70",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9d64",
      "DATA",
      [
        "storage",
        "00ca43f8",
        null,
        null
      ]
    ],
    [
      "00bf9d98",
      "READ",
      [
        "storage",
        "00c9a860",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bf9d50",
      "READ",
      [
        "storage",
        "01127370",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9d64",
      "DATA",
      [
        "storage",
        "00ca47f8",
        null,
        null
      ]
    ],
    [
      "00bf9d98",
      "READ",
      [
        "storage",
        "00c9ac60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf999c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf98d0.md#insn-00bf999c) · [`00bf9a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf98d0.md#insn-00bf9a24) · [`00bf9a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf98d0.md#insn-00bf9a34)
- 新版 `00bf9dc4`（命令位置の公開資料なし） · `00bf9e4c`（命令位置の公開資料なし） · `00bf9e5c`（命令位置の公開資料なし）

~~~diff
- 00bf999c ["INT_ADD", "register:40f0:8", ["const:bf999c:8", "const:4:8"]]
- 00bf999c ["CALL", null, ["callee:00c58330:8"]]
+ 00bf9dc4 ["INT_ADD", "register:40f0:8", ["const:bf9dc4:8", "const:4:8"]]
+ 00bf9dc4 ["CALL", null, ["callee:00c58330:8"]]
- 00bf999c bytes 65790194
+ 00bf9dc4 bytes 5b790194
- 00bf9a24 ["INT_ADD", "register:40f0:8", ["const:bf9a24:8", "const:4:8"]]
- 00bf9a24 ["CALL", null, ["callee:00c57e50:8"]]
+ 00bf9e4c ["INT_ADD", "register:40f0:8", ["const:bf9e4c:8", "const:4:8"]]
+ 00bf9e4c ["CALL", null, ["callee:00c57e50:8"]]
- 00bf9a24 bytes 0b780194
+ 00bf9e4c bytes 01780194
- 00bf9a34 ["INT_ADD", "register:40f0:8", ["const:bf9a34:8", "const:4:8"]]
- 00bf9a34 ["CALL", null, ["callee:00c57e70:8"]]
+ 00bf9e5c ["INT_ADD", "register:40f0:8", ["const:bf9e5c:8", "const:4:8"]]
+ 00bf9e5c ["CALL", null, ["callee:00c57e70:8"]]
- 00bf9a34 bytes 0f780194
+ 00bf9e5c bytes 05780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54ffe1bde0aea2d1f9d7ff8fc4f95ed9"></a>

### [`00bf9c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9c60.md) → [`00bfa088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa088.md) FUN_00bfa088

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

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
      "definition_site": "00bfa0b0",
      "incomplete_value": true,
      "site": "00bfa0b0",
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
      "definition_site": "00bf9c88",
      "incomplete_value": true,
      "site": "00bf9c88",
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
      "00bfa0a4",
      "READ",
      [
        "storage",
        "00c9a850",
        null,
        "pointer"
      ]
    ],
    [
      "00bfa0b0",
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
      "00bfa0a4",
      "READ",
      [
        "storage",
        "00c9ac50",
        null,
        "pointer"
      ]
    ],
    [
      "00bfa0b0",
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

- 旧版 [`00bf9c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9c60.md#insn-00bf9c7c) · [`00bf9c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9c60.md#insn-00bf9c8c) · [`00bf9c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9c60.md#insn-00bf9c94)
- 新版 `00bfa0a4`（命令位置の公開資料なし） · `00bfa0b4`（命令位置の公開資料なし） · `00bfa0bc`（命令位置の公開資料なし）

~~~diff
- 00bf9c7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:850:8"]]
- 00bf9c7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfa0a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c50:8"]]
+ 00bfa0a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bf9c7c bytes 082944f9
+ 00bfa0a4 bytes 082946f9
- 00bf9c8c ["INT_ADD", "register:40f0:8", ["const:bf9c8c:8", "const:4:8"]]
- 00bf9c8c ["CALL", null, ["callee:00c580d0:8"]]
+ 00bfa0b4 ["INT_ADD", "register:40f0:8", ["const:bfa0b4:8", "const:4:8"]]
+ 00bfa0b4 ["CALL", null, ["callee:00c580d0:8"]]
- 00bf9c8c bytes 11780194
+ 00bfa0b4 bytes 07780194
- 00bf9c94 ["INT_ADD", "register:40f0:8", ["const:bf9c94:8", "const:4:8"]]
- 00bf9c94 ["CALL", null, ["callee:00c57e60:8"]]
+ 00bfa0bc ["INT_ADD", "register:40f0:8", ["const:bfa0bc:8", "const:4:8"]]
+ 00bfa0bc ["CALL", null, ["callee:00c57e60:8"]]
- 00bf9c94 bytes 73770194
+ 00bfa0bc bytes 69770194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64fe4ce36a943431f2c22e393ca15d11"></a>

### [`00bf9d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d08.md) → [`00bfa130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa130.md) _ZNSt6__ndk15mutex4lockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) · 呼出先 2件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md)
- 新版 呼出元 1件 [`00c580e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580e0.md) · 呼出先 2件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa154",
      "incomplete_value": false,
      "site": "00bfa158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:79e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9d2c",
      "incomplete_value": false,
      "site": "00bf9d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:75e:8"
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
      "00bfa154",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa154",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d08.md#insn-00bf9d30) · [`00bf9d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d08.md#insn-00bf9d14) · [`00bf9d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d08.md#insn-00bf9d2c)
- 新版 `00bfa158`（命令位置の公開資料なし） · `00bfa13c`（命令位置の公開資料なし） · `00bfa154`（命令位置の公開資料なし）

~~~diff
- 00bf9d30 ["INT_ADD", "register:40f0:8", ["const:bf9d30:8", "const:4:8"]]
- 00bf9d30 ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa158 ["INT_ADD", "register:40f0:8", ["const:bfa158:8", "const:4:8"]]
+ 00bfa158 ["CALL", null, ["callee:00c58120:8"]]
- 00bf9d30 bytes fc770194
+ 00bfa158 bytes f2770194
- 00bf9d14 ["INT_ADD", "register:40f0:8", ["const:bf9d14:8", "const:4:8"]]
- 00bf9d14 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00bfa13c ["INT_ADD", "register:40f0:8", ["const:bfa13c:8", "const:4:8"]]
+ 00bfa13c ["CALL", null, ["callee:00c5b6a0:8"]]
- 00bf9d14 bytes 63850194
+ 00bfa13c bytes 59850194
- 00bf9d2c ["COPY", "tmp:0:8", ["const:75e:8"]]
- 00bf9d2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bf9d2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bf9d2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfa154 ["COPY", "tmp:0:8", ["const:79e:8"]]
+ 00bfa154 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa154 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa154 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bf9d2c bytes 21781d91
+ 00bfa154 bytes 21781e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7091c6d31b78fc25b1aafcd1b550e9d4"></a>

### [`00bf9d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d7c.md) → [`00bfa1a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa1a4.md) _ZNSt6__ndk115recursive_mutexC1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cc0.md) · 呼出先 6件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5b290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b290.md) [`00c5ba80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba80.md) [`00c5ba90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba90.md) [`00c5baa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5baa0.md)
- 新版 呼出元 1件 [`00c5a0c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0c0.md) · 呼出先 6件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5b690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b690.md) [`00c5be80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be80.md) [`00c5be90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5be90.md) [`00c5bea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5bea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa240",
      "incomplete_value": false,
      "site": "00bfa244",
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
            "const:8c3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9e18",
      "incomplete_value": false,
      "site": "00bf9e1c",
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
            "const:7f6:8"
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
      "00bfa240",
      "PARAM",
      [
        "storage",
        "002a87f6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa240",
      "PARAM",
      [
        "storage",
        "002a88c3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d7c.md#insn-00bf9e1c) · [`00bf9d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d7c.md#insn-00bf9d98) · [`00bf9da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d7c.md#insn-00bf9da8)
- 新版 `00bfa244`（命令位置の公開資料なし） · `00bfa1c0`（命令位置の公開資料なし） · `00bfa1d0`（命令位置の公開資料なし）

~~~diff
- 00bf9e1c ["INT_ADD", "register:40f0:8", ["const:bf9e1c:8", "const:4:8"]]
- 00bf9e1c ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa244 ["INT_ADD", "register:40f0:8", ["const:bfa244:8", "const:4:8"]]
+ 00bfa244 ["CALL", null, ["callee:00c58120:8"]]
- 00bf9e1c bytes c1770194
+ 00bfa244 bytes b7770194
- 00bf9d98 ["INT_ADD", "register:40f0:8", ["const:bf9d98:8", "const:4:8"]]
- 00bf9d98 ["CALL", null, ["callee:00c5bea0:8"]]
+ 00bfa1c0 ["INT_ADD", "register:40f0:8", ["const:bfa1c0:8", "const:4:8"]]
+ 00bfa1c0 ["CALL", null, ["callee:00c5bea0:8"]]
- 00bf9d98 bytes 42870194
+ 00bfa1c0 bytes 38870194
- 00bf9da8 ["INT_ADD", "register:40f0:8", ["const:bf9da8:8", "const:4:8"]]
- 00bf9da8 ["CALL", null, ["callee:00c5beb0:8"]]
+ 00bfa1d0 ["INT_ADD", "register:40f0:8", ["const:bfa1d0:8", "const:4:8"]]
+ 00bfa1d0 ["CALL", null, ["callee:00c5beb0:8"]]
- 00bf9da8 bytes 42870194
+ 00bfa1d0 bytes 38870194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88b92679ee28c0166914117c6239e2b5"></a>

### [`00bf9e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e40.md) → [`00bfa268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa268.md) _ZNSt6__ndk115recursive_mutex4lockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) · 呼出先 2件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md)
- 新版 呼出元 1件 [`00c5a0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0e0.md) · 呼出先 2件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa28c",
      "incomplete_value": false,
      "site": "00bfa290",
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
            "const:51a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9e64",
      "incomplete_value": false,
      "site": "00bf9e68",
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
            "const:43e:8"
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
      "00bfa28c",
      "PARAM",
      [
        "storage",
        "002a743e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa28c",
      "PARAM",
      [
        "storage",
        "002a751a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e40.md#insn-00bf9e68) · [`00bf9e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e40.md#insn-00bf9e4c) · [`00bf9e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e40.md#insn-00bf9e64)
- 新版 `00bfa290`（命令位置の公開資料なし） · `00bfa274`（命令位置の公開資料なし） · `00bfa28c`（命令位置の公開資料なし）

~~~diff
- 00bf9e68 ["INT_ADD", "register:40f0:8", ["const:bf9e68:8", "const:4:8"]]
- 00bf9e68 ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa290 ["INT_ADD", "register:40f0:8", ["const:bfa290:8", "const:4:8"]]
+ 00bfa290 ["CALL", null, ["callee:00c58120:8"]]
- 00bf9e68 bytes ae770194
+ 00bfa290 bytes a4770194
- 00bf9e4c ["INT_ADD", "register:40f0:8", ["const:bf9e4c:8", "const:4:8"]]
- 00bf9e4c ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00bfa274 ["INT_ADD", "register:40f0:8", ["const:bfa274:8", "const:4:8"]]
+ 00bfa274 ["CALL", null, ["callee:00c5b6a0:8"]]
- 00bf9e4c bytes 15850194
+ 00bfa274 bytes 0b850194
- 00bf9e64 ["COPY", "tmp:0:8", ["const:43e:8"]]
- 00bf9e64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bf9e64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bf9e64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfa28c ["COPY", "tmp:0:8", ["const:51a:8"]]
+ 00bfa28c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa28c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa28c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bf9e64 bytes 21f81091
+ 00bfa28c bytes 21681491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3839f70de4abf502628e97cb1d5bf4eb"></a>

### [`00bf9ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ed0.md) → [`00bfa2f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa2f8.md) _ZNSt6__ndk111timed_mutexD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa33c",
      "incomplete_value": false,
      "site": "00bfa340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:79e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9f14",
      "incomplete_value": false,
      "site": "00bf9f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:75e:8"
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
      "00bfa33c",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa33c",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ed0.md#insn-00bf9f18) · [`00bf9ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ed0.md#insn-00bf9ee4) · [`00bf9ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ed0.md#insn-00bf9ef0)
- 新版 `00bfa340`（命令位置の公開資料なし） · `00bfa30c`（命令位置の公開資料なし） · `00bfa318`（命令位置の公開資料なし）

~~~diff
- 00bf9f18 ["INT_ADD", "register:40f0:8", ["const:bf9f18:8", "const:4:8"]]
- 00bf9f18 ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa340 ["INT_ADD", "register:40f0:8", ["const:bfa340:8", "const:4:8"]]
+ 00bfa340 ["CALL", null, ["callee:00c58120:8"]]
- 00bf9f18 bytes 82770194
+ 00bfa340 bytes 78770194
- 00bf9ee4 ["INT_ADD", "register:40f0:8", ["const:bf9ee4:8", "const:4:8"]]
- 00bf9ee4 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00bfa30c ["INT_ADD", "register:40f0:8", ["const:bfa30c:8", "const:4:8"]]
+ 00bfa30c ["CALL", null, ["callee:00c5b6a0:8"]]
- 00bf9ee4 bytes ef840194
+ 00bfa30c bytes e5840194
- 00bf9ef0 ["INT_ADD", "register:40f0:8", ["const:bf9ef0:8", "const:4:8"]]
- 00bf9ef0 ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00bfa318 ["INT_ADD", "register:40f0:8", ["const:bfa318:8", "const:4:8"]]
+ 00bfa318 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00bf9ef0 bytes f0840194
+ 00bfa318 bytes e6840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d3ec85f4664b9d09ce24ef5374994be"></a>

### [`00bf9f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9f24.md) → [`00bfa34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa34c.md) _ZNSt6__ndk111timed_mutex4lockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa3d0",
      "incomplete_value": false,
      "site": "00bfa3d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:79e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf9fa8",
      "incomplete_value": false,
      "site": "00bf9fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:75e:8"
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
      "00bfa3d0",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa3d0",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bf9fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9f24.md#insn-00bf9fac) · [`00bf9f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9f24.md#insn-00bf9f48) · [`00bf9f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9f24.md#insn-00bf9f60)
- 新版 `00bfa3d4`（命令位置の公開資料なし） · `00bfa370`（命令位置の公開資料なし） · `00bfa388`（命令位置の公開資料なし）

~~~diff
- 00bf9fac ["INT_ADD", "register:40f0:8", ["const:bf9fac:8", "const:4:8"]]
- 00bf9fac ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa3d4 ["INT_ADD", "register:40f0:8", ["const:bfa3d4:8", "const:4:8"]]
+ 00bfa3d4 ["CALL", null, ["callee:00c58120:8"]]
- 00bf9fac bytes 5d770194
+ 00bfa3d4 bytes 53770194
- 00bf9f48 ["INT_ADD", "register:40f0:8", ["const:bf9f48:8", "const:4:8"]]
- 00bf9f48 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00bfa370 ["INT_ADD", "register:40f0:8", ["const:bfa370:8", "const:4:8"]]
+ 00bfa370 ["CALL", null, ["callee:00c5b6a0:8"]]
- 00bf9f48 bytes d6840194
+ 00bfa370 bytes cc840194
- 00bf9f60 ["INT_ADD", "register:40f0:8", ["const:bf9f60:8", "const:4:8"]]
- 00bf9f60 ["CALL", null, ["callee:00c58480:8"]]
+ 00bfa388 ["INT_ADD", "register:40f0:8", ["const:bfa388:8", "const:4:8"]]
+ 00bfa388 ["CALL", null, ["callee:00c58480:8"]]
- 00bf9f60 bytes 48780194
+ 00bfa388 bytes 3e780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ca1bf87dc4e7b8716c32235538e71aa"></a>

### [`00bfa014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa014.md) → [`00bfa43c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa43c.md) _ZNSt6__ndk111timed_mutex6unlockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c58d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d10.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c59110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59110.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa480",
      "incomplete_value": false,
      "site": "00bfa484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:79e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa058",
      "incomplete_value": false,
      "site": "00bfa05c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:75e:8"
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
      "00bfa480",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa480",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa014.md#insn-00bfa05c) · [`00bfa028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa014.md#insn-00bfa028) · [`00bfa038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa014.md#insn-00bfa038)
- 新版 `00bfa484`（命令位置の公開資料なし） · `00bfa450`（命令位置の公開資料なし） · `00bfa460`（命令位置の公開資料なし）

~~~diff
- 00bfa05c ["INT_ADD", "register:40f0:8", ["const:bfa05c:8", "const:4:8"]]
- 00bfa05c ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa484 ["INT_ADD", "register:40f0:8", ["const:bfa484:8", "const:4:8"]]
+ 00bfa484 ["CALL", null, ["callee:00c58120:8"]]
- 00bfa05c bytes 31770194
+ 00bfa484 bytes 27770194
- 00bfa028 ["INT_ADD", "register:40f0:8", ["const:bfa028:8", "const:4:8"]]
- 00bfa028 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00bfa450 ["INT_ADD", "register:40f0:8", ["const:bfa450:8", "const:4:8"]]
+ 00bfa450 ["CALL", null, ["callee:00c5b6a0:8"]]
- 00bfa028 bytes 9e840194
+ 00bfa450 bytes 94840194
- 00bfa038 ["INT_ADD", "register:40f0:8", ["const:bfa038:8", "const:4:8"]]
- 00bfa038 ["CALL", null, ["callee:00c59110:8"]]
+ 00bfa460 ["INT_ADD", "register:40f0:8", ["const:bfa460:8", "const:4:8"]]
+ 00bfa460 ["CALL", null, ["callee:00c59110:8"]]
- 00bfa038 bytes 367b0194
+ 00bfa460 bytes 2c7b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4c3b00d1a64783b63ec22ca2e65d206"></a>

### [`00bfa084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa084.md) → [`00bfa4ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa4ac.md) _ZNSt6__ndk121recursive_timed_mutexD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e60.md) [`00c580d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580d0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa4f0",
      "incomplete_value": false,
      "site": "00bfa4f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:79e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa0c8",
      "incomplete_value": false,
      "site": "00bfa0cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:75e:8"
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
      "00bfa4f0",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa4f0",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa084.md#insn-00bfa0cc) · [`00bfa098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa084.md#insn-00bfa098) · [`00bfa0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa084.md#insn-00bfa0a4)
- 新版 `00bfa4f4`（命令位置の公開資料なし） · `00bfa4c0`（命令位置の公開資料なし） · `00bfa4cc`（命令位置の公開資料なし）

~~~diff
- 00bfa0cc ["INT_ADD", "register:40f0:8", ["const:bfa0cc:8", "const:4:8"]]
- 00bfa0cc ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa4f4 ["INT_ADD", "register:40f0:8", ["const:bfa4f4:8", "const:4:8"]]
+ 00bfa4f4 ["CALL", null, ["callee:00c58120:8"]]
- 00bfa0cc bytes 15770194
+ 00bfa4f4 bytes 0b770194
- 00bfa098 ["INT_ADD", "register:40f0:8", ["const:bfa098:8", "const:4:8"]]
- 00bfa098 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00bfa4c0 ["INT_ADD", "register:40f0:8", ["const:bfa4c0:8", "const:4:8"]]
+ 00bfa4c0 ["CALL", null, ["callee:00c5b6a0:8"]]
- 00bfa098 bytes 82840194
+ 00bfa4c0 bytes 78840194
- 00bfa0a4 ["INT_ADD", "register:40f0:8", ["const:bfa0a4:8", "const:4:8"]]
- 00bfa0a4 ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00bfa4cc ["INT_ADD", "register:40f0:8", ["const:bfa4cc:8", "const:4:8"]]
+ 00bfa4cc ["CALL", null, ["callee:00c5b6b0:8"]]
- 00bfa0a4 bytes 83840194
+ 00bfa4cc bytes 79840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae22973600be51c573f59e2ad00e80df"></a>

### [`00bfa0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa0d8.md) → [`00bfa500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa500.md) _ZNSt6__ndk121recursive_timed_mutex4lockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md) [`00c58220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58220.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c58480`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58480.md) [`00c58620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58620.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa5ac",
      "incomplete_value": false,
      "site": "00bfa5b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:79e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa184",
      "incomplete_value": false,
      "site": "00bfa188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:75e:8"
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
      "definition_site": "00bfa5b8",
      "incomplete_value": false,
      "site": "00bfa5c0",
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
            "const:dc7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa190",
      "incomplete_value": false,
      "site": "00bfa198",
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
            "const:cfa:8"
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
      "00bfa5ac",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ],
    [
      "00bfa5b8",
      "PARAM",
      [
        "storage",
        "002a3cfa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa5ac",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ],
    [
      "00bfa5b8",
      "PARAM",
      [
        "storage",
        "002a3dc7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa0d8.md#insn-00bfa188) · [`00bfa198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa0d8.md#insn-00bfa198) · [`00bfa0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa0d8.md#insn-00bfa0f0)
- 新版 `00bfa5b0`（命令位置の公開資料なし） · `00bfa5c0`（命令位置の公開資料なし） · `00bfa518`（命令位置の公開資料なし）

~~~diff
- 00bfa188 ["INT_ADD", "register:40f0:8", ["const:bfa188:8", "const:4:8"]]
- 00bfa188 ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa5b0 ["INT_ADD", "register:40f0:8", ["const:bfa5b0:8", "const:4:8"]]
+ 00bfa5b0 ["CALL", null, ["callee:00c58120:8"]]
- 00bfa188 bytes e6760194
+ 00bfa5b0 bytes dc760194
- 00bfa198 ["INT_ADD", "register:40f0:8", ["const:bfa198:8", "const:4:8"]]
- 00bfa198 ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa5c0 ["INT_ADD", "register:40f0:8", ["const:bfa5c0:8", "const:4:8"]]
+ 00bfa5c0 ["CALL", null, ["callee:00c58120:8"]]
- 00bfa198 bytes e2760194
+ 00bfa5c0 bytes d8760194
- 00bfa0f0 ["INT_ADD", "register:40f0:8", ["const:bfa0f0:8", "const:4:8"]]
- 00bfa0f0 ["CALL", null, ["callee:00c58620:8"]]
+ 00bfa518 ["INT_ADD", "register:40f0:8", ["const:bfa518:8", "const:4:8"]]
+ 00bfa518 ["CALL", null, ["callee:00c58620:8"]]
- 00bfa0f0 bytes 4c780194
+ 00bfa518 bytes 42780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20582eae120c5e8d1e3f728797d10290"></a>

### [`00bfa240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa240.md) → [`00bfa668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa668.md) _ZNSt6__ndk121recursive_timed_mutex6unlockEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c58d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d10.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c59110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59110.md) [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md) [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa6d0",
      "incomplete_value": false,
      "site": "00bfa6d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:79e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa2a8",
      "incomplete_value": false,
      "site": "00bfa2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:75e:8"
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
      "00bfa6d0",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa6d0",
      "PARAM",
      [
        "storage",
        "002b179e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa240.md#insn-00bfa2ac) · [`00bfa254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa240.md#insn-00bfa254) · [`00bfa270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa240.md#insn-00bfa270)
- 新版 `00bfa6d4`（命令位置の公開資料なし） · `00bfa67c`（命令位置の公開資料なし） · `00bfa698`（命令位置の公開資料なし）

~~~diff
- 00bfa2ac ["INT_ADD", "register:40f0:8", ["const:bfa2ac:8", "const:4:8"]]
- 00bfa2ac ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa6d4 ["INT_ADD", "register:40f0:8", ["const:bfa6d4:8", "const:4:8"]]
+ 00bfa6d4 ["CALL", null, ["callee:00c58120:8"]]
- 00bfa2ac bytes 9d760194
+ 00bfa6d4 bytes 93760194
- 00bfa254 ["INT_ADD", "register:40f0:8", ["const:bfa254:8", "const:4:8"]]
- 00bfa254 ["CALL", null, ["callee:00c5b6a0:8"]]
+ 00bfa67c ["INT_ADD", "register:40f0:8", ["const:bfa67c:8", "const:4:8"]]
+ 00bfa67c ["CALL", null, ["callee:00c5b6a0:8"]]
- 00bfa254 bytes 13840194
+ 00bfa67c bytes 09840194
- 00bfa270 ["INT_ADD", "register:40f0:8", ["const:bfa270:8", "const:4:8"]]
- 00bfa270 ["CALL", null, ["callee:00c5b6b0:8"]]
+ 00bfa698 ["INT_ADD", "register:40f0:8", ["const:bfa698:8", "const:4:8"]]
+ 00bfa698 ["CALL", null, ["callee:00c5b6b0:8"]]
- 00bfa270 bytes 10840194
+ 00bfa698 bytes 06840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4653a9ed23ee2516ba3ef92dc556d83"></a>

### [`00bfa2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2dc.md) → [`00bfa704`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa704.md) _ZNSt6__ndk16thread4joinEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d70.md) · 呼出先 2件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5d240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d240.md)
- 新版 呼出元 1件 [`00c58170`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58170.md) · 呼出先 2件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5d640`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d640.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa748",
      "incomplete_value": false,
      "site": "00bfa74c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:2e7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa320",
      "incomplete_value": false,
      "site": "00bfa324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a6000:8"
          ],
          [
            "leaf",
            "const:20b:8"
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
      "00bfa748",
      "PARAM",
      [
        "storage",
        "002a620b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa748",
      "PARAM",
      [
        "storage",
        "002a62e7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2dc.md#insn-00bfa324) · [`00bfa2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2dc.md#insn-00bfa2fc) · [`00bfa320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2dc.md#insn-00bfa320)
- 新版 `00bfa74c`（命令位置の公開資料なし） · `00bfa724`（命令位置の公開資料なし） · `00bfa748`（命令位置の公開資料なし）

~~~diff
- 00bfa324 ["INT_ADD", "register:40f0:8", ["const:bfa324:8", "const:4:8"]]
- 00bfa324 ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa74c ["INT_ADD", "register:40f0:8", ["const:bfa74c:8", "const:4:8"]]
+ 00bfa74c ["CALL", null, ["callee:00c58120:8"]]
- 00bfa324 bytes 7f760194
+ 00bfa74c bytes 75760194
- 00bfa2fc ["INT_ADD", "register:40f0:8", ["const:bfa2fc:8", "const:4:8"]]
- 00bfa2fc ["CALL", null, ["callee:00c5d640:8"]]
+ 00bfa724 ["INT_ADD", "register:40f0:8", ["const:bfa724:8", "const:4:8"]]
+ 00bfa724 ["CALL", null, ["callee:00c5d640:8"]]
- 00bfa2fc bytes d18b0194
+ 00bfa724 bytes c78b0194
- 00bfa320 ["COPY", "tmp:0:8", ["const:20b:8"]]
- 00bfa320 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa320 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa320 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfa748 ["COPY", "tmp:0:8", ["const:2e7:8"]]
+ 00bfa748 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa748 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa748 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bfa320 bytes 212c0891
+ 00bfa748 bytes 219c0b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38c0c64d749fa886197454e54bffe80c"></a>

### [`00bfa328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa328.md) → [`00bfa750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa750.md) _ZNSt6__ndk16thread6detachEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58110.md) · 呼出先 2件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5de80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de80.md)
- 新版 呼出元 1件 [`00c58510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58510.md) · 呼出先 2件 [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5e280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e280.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa790",
      "incomplete_value": false,
      "site": "00bfa794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:54b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa368",
      "incomplete_value": false,
      "site": "00bfa36c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:50b:8"
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
      "00bfa790",
      "PARAM",
      [
        "storage",
        "002ae50b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa790",
      "PARAM",
      [
        "storage",
        "002ae54b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa328.md#insn-00bfa36c) · [`00bfa344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa328.md#insn-00bfa344) · [`00bfa368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa328.md#insn-00bfa368)
- 新版 `00bfa794`（命令位置の公開資料なし） · `00bfa76c`（命令位置の公開資料なし） · `00bfa790`（命令位置の公開資料なし）

~~~diff
- 00bfa36c ["INT_ADD", "register:40f0:8", ["const:bfa36c:8", "const:4:8"]]
- 00bfa36c ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa794 ["INT_ADD", "register:40f0:8", ["const:bfa794:8", "const:4:8"]]
+ 00bfa794 ["CALL", null, ["callee:00c58120:8"]]
- 00bfa36c bytes 6d760194
+ 00bfa794 bytes 63760194
- 00bfa344 ["INT_ADD", "register:40f0:8", ["const:bfa344:8", "const:4:8"]]
- 00bfa344 ["CALL", null, ["callee:00c5e280:8"]]
+ 00bfa76c ["INT_ADD", "register:40f0:8", ["const:bfa76c:8", "const:4:8"]]
+ 00bfa76c ["CALL", null, ["callee:00c5e280:8"]]
- 00bfa344 bytes cf8e0194
+ 00bfa76c bytes c58e0194
- 00bfa368 ["COPY", "tmp:0:8", ["const:50b:8"]]
- 00bfa368 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa368 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00bfa368 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bfa790 ["COPY", "tmp:0:8", ["const:54b:8"]]
+ 00bfa790 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa790 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bfa790 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00bfa368 bytes 212c1491
+ 00bfa790 bytes 212c1591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-687fdfbc9c9a9b66dcb82ae2b70d43ff"></a>

### [`00bfa41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa41c.md) → [`00bfa844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa844.md) _ZNSt6__ndk119__thread_local_dataEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) · 呼出先 3件 [`00bfa4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4a0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c58130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58130.md) · 呼出先 3件 [`00bfa8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8c8.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfa8a4",
      "incomplete_value": true,
      "site": "00bfa8a4",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa47c",
      "incomplete_value": true,
      "site": "00bfa47c",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa880",
      "incomplete_value": false,
      "site": "00bfa884",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa458",
      "incomplete_value": false,
      "site": "00bfa45c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa894",
      "incomplete_value": false,
      "site": "00bfa898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa46c",
      "incomplete_value": false,
      "site": "00bfa470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "00bfa860",
      "READ",
      [
        "storage",
        "01126f88",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfa868",
      "READ",
      [
        "storage",
        "01126f80",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfa868",
      "DATA",
      [
        "storage",
        "01126f78",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfa860",
      "READ",
      [
        "storage",
        "01127388",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfa868",
      "READ",
      [
        "storage",
        "01127380",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfa868",
      "DATA",
      [
        "storage",
        "01127378",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa41c.md#insn-00bfa45c) · [`00bfa470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa41c.md#insn-00bfa470) · [`00bfa47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa41c.md#insn-00bfa47c)
- 新版 `00bfa884`（命令位置の公開資料なし） · `00bfa898`（命令位置の公開資料なし） · `00bfa8a4`（命令位置の公開資料なし）

~~~diff
- 00bfa45c ["INT_ADD", "register:40f0:8", ["const:bfa45c:8", "const:4:8"]]
- 00bfa45c ["CALL", null, ["callee:00c57e50:8"]]
+ 00bfa884 ["INT_ADD", "register:40f0:8", ["const:bfa884:8", "const:4:8"]]
+ 00bfa884 ["CALL", null, ["callee:00c57e50:8"]]
- 00bfa45c bytes 7d750194
+ 00bfa884 bytes 73750194
- 00bfa470 ["INT_ADD", "register:40f0:8", ["const:bfa470:8", "const:4:8"]]
- 00bfa470 ["CALL", null, ["callee:00bfa8c8:8"]]
+ 00bfa898 ["INT_ADD", "register:40f0:8", ["const:bfa898:8", "const:4:8"]]
+ 00bfa898 ["CALL", null, ["callee:00bfa8c8:8"]]
- 00bfa470 bytes 0c000094
+ 00bfa898 bytes 0c000094
- 00bfa47c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f80:8"]]
- 00bfa47c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00bfa8a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:380:8"]]
+ 00bfa8a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bfa47c bytes 93c207f9
+ 00bfa8a4 bytes 93c201f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8f07ee8503e02af46fd381346dec9f1"></a>

### [`00bfa4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4a0.md) → [`00bfa8c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa8c8.md) FUN_00bfa8c8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bfa41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa41c.md) · 呼出先 3件 [`00bfa854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa854.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c59f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f00.md)
- 新版 呼出元 1件 [`00bfa844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa844.md) · 呼出先 3件 [`00bfac7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac7c.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5a300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa8d8",
      "incomplete_value": false,
      "site": "00bfa8dc",
      "value": [
        "leaf",
        "const:bfac7c:8"
      ]
    },
    "old": {
      "definition_site": "00bfa4b0",
      "incomplete_value": false,
      "site": "00bfa4b4",
      "value": [
        "leaf",
        "const:bfa854:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa8f4",
      "incomplete_value": false,
      "site": "00bfa8f8",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa4cc",
      "incomplete_value": false,
      "site": "00bfa4d0",
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
            "const:d23:8"
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
      "00bfa8d8",
      "PARAM",
      [
        "storage",
        "00bfa854",
        null,
        null
      ]
    ],
    [
      "00bfa8f4",
      "PARAM",
      [
        "storage",
        "002a3d23",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa8d8",
      "PARAM",
      [
        "storage",
        "00bfac7c",
        null,
        null
      ]
    ],
    [
      "00bfa8f4",
      "PARAM",
      [
        "storage",
        "002a3df0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4a0.md#insn-00bfa4b4) · [`00bfa4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4a0.md#insn-00bfa4d0) · [`00bfa4b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4a0.md#insn-00bfa4b0)
- 新版 `00bfa8dc`（命令位置の公開資料なし） · `00bfa8f8`（命令位置の公開資料なし） · `00bfa8d8`（命令位置の公開資料なし）

~~~diff
- 00bfa4b4 ["INT_ADD", "register:40f0:8", ["const:bfa4b4:8", "const:4:8"]]
- 00bfa4b4 ["CALL", null, ["callee:00c5a300:8"]]
+ 00bfa8dc ["INT_ADD", "register:40f0:8", ["const:bfa8dc:8", "const:4:8"]]
+ 00bfa8dc ["CALL", null, ["callee:00c5a300:8"]]
- 00bfa4b4 bytes 937e0194
+ 00bfa8dc bytes 897e0194
- 00bfa4d0 ["INT_ADD", "register:40f0:8", ["const:bfa4d0:8", "const:4:8"]]
- 00bfa4d0 ["CALL", null, ["callee:00c58120:8"]]
+ 00bfa8f8 ["INT_ADD", "register:40f0:8", ["const:bfa8f8:8", "const:4:8"]]
+ 00bfa8f8 ["CALL", null, ["callee:00c58120:8"]]
- 00bfa4d0 bytes 14760194
+ 00bfa8f8 bytes 0a760194
- 00bfa4b0 ["COPY", "register:4008:8", ["const:bfa854:8"]]
+ 00bfa8d8 ["COPY", "register:4008:8", ["const:bfac7c:8"]]
- 00bfa4b0 bytes 211d0010
+ 00bfa8d8 bytes 211d0010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cdab277158bb07e545118577e6eeeb1"></a>

### [`00bfa824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa824.md) → [`00bfac4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac4c.md) FUN_00bfac4c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bfa5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa5a0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00bfa9c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfa9c8.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfac5c",
      "incomplete_value": false,
      "site": "00bfac60",
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
      "definition_site": "00bfa834",
      "incomplete_value": false,
      "site": "00bfa838",
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
      "00bfac5c",
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
      "00bfac5c",
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

- 旧版 [`00bfa838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa824.md#insn-00bfa838) · [`00bfa834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa824.md#insn-00bfa834)
- 新版 `00bfac60`（命令位置の公開資料なし） · `00bfac5c`（命令位置の公開資料なし）

~~~diff
- 00bfa838 ["INT_ADD", "register:40f0:8", ["const:bfa838:8", "const:4:8"]]
- 00bfa838 ["CALL", null, ["callee:0043b778:8"]]
+ 00bfac60 ["INT_ADD", "register:40f0:8", ["const:bfac60:8", "const:4:8"]]
+ 00bfac60 ["CALL", null, ["callee:0043b778:8"]]
- 00bfa838 bytes c003e197
+ 00bfac60 bytes c602e197
- 00bfa834 ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00bfa834 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bfa834 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bfa834 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bfac5c ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00bfac5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfac5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfac5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bfa834 bytes 00303c91
+ 00bfac5c bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-202799ebc8589cad2606eecc29cf790e"></a>

### [`00bfa83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa83c.md) → [`00bfac64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfac64.md) FUN_00bfac64

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bfa69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa69c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00bfaac4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaac4.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfac74",
      "incomplete_value": false,
      "site": "00bfac78",
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
      "definition_site": "00bfa84c",
      "incomplete_value": false,
      "site": "00bfa850",
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
      "00bfac74",
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
      "00bfac74",
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

- 旧版 [`00bfa850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa83c.md#insn-00bfa850) · [`00bfa84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa83c.md#insn-00bfa84c)
- 新版 `00bfac78`（命令位置の公開資料なし） · `00bfac74`（命令位置の公開資料なし）

~~~diff
- 00bfa850 ["INT_ADD", "register:40f0:8", ["const:bfa850:8", "const:4:8"]]
- 00bfa850 ["CALL", null, ["callee:0043b778:8"]]
+ 00bfac78 ["INT_ADD", "register:40f0:8", ["const:bfac78:8", "const:4:8"]]
+ 00bfac78 ["CALL", null, ["callee:0043b778:8"]]
- 00bfa850 bytes ba03e197
+ 00bfac78 bytes c002e197
- 00bfa84c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00bfa84c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bfa84c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bfa84c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bfac74 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00bfac74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfac74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfac74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bfa84c bytes 00303c91
+ 00bfac74 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be93438562e67bc96becebe03ab9fdd6"></a>

### [`00bfa88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa88c.md) → [`00bfacb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfacb4.md) _ZNSt6__ndk113random_deviceC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) · 呼出先 4件 [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5d210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d210.md)
- 新版 呼出元 1件 [`00c583a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583a0.md) · 呼出先 4件 [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5d610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d610.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfad10",
      "incomplete_value": false,
      "site": "00bfad20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:a02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa8e8",
      "incomplete_value": false,
      "site": "00bfa8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:9c2:8"
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
      "00bfad10",
      "PARAM",
      [
        "storage",
        "002b49c2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfad10",
      "PARAM",
      [
        "storage",
        "002b4a02",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa88c.md#insn-00bfa8f8) · [`00bfa8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa88c.md#insn-00bfa8bc) · [`00bfa8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa88c.md#insn-00bfa8dc)
- 新版 `00bfad20`（命令位置の公開資料なし） · `00bface4`（命令位置の公開資料なし） · `00bfad04`（命令位置の公開資料なし）

~~~diff
- 00bfa8f8 ["INT_ADD", "register:40f0:8", ["const:bfa8f8:8", "const:4:8"]]
- 00bfa8f8 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bfad20 ["INT_ADD", "register:40f0:8", ["const:bfad20:8", "const:4:8"]]
+ 00bfad20 ["CALL", null, ["callee:00c580b0:8"]]
- 00bfa8f8 bytes ee740194
+ 00bfad20 bytes e4740194
- 00bfa8bc ["INT_ADD", "register:40f0:8", ["const:bfa8bc:8", "const:4:8"]]
- 00bfa8bc ["CALL", null, ["callee:00c5d610:8"]]
+ 00bface4 ["INT_ADD", "register:40f0:8", ["const:bface4:8", "const:4:8"]]
+ 00bface4 ["CALL", null, ["callee:00c5d610:8"]]
- 00bfa8bc bytes 558a0194
+ 00bface4 bytes 4b8a0194
- 00bfa8dc ["INT_ADD", "register:40f0:8", ["const:bfa8dc:8", "const:4:8"]]
- 00bfa8dc ["CALL", null, ["callee:00c580c0:8"]]
+ 00bfad04 ["INT_ADD", "register:40f0:8", ["const:bfad04:8", "const:4:8"]]
+ 00bfad04 ["CALL", null, ["callee:00c580c0:8"]]
- 00bfa8dc bytes f9740194
+ 00bfad04 bytes ef740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d3bb88803594ec2511c511e60724be5"></a>

### [`00bfa954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa954.md) → [`00bfad7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad7c.md) _ZNSt6__ndk113random_deviceclEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md) · 呼出先 3件 [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5d250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d250.md)
- 新版 呼出元 1件 [`00c583b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c583b0.md) · 呼出先 3件 [`00c580c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580c0.md) [`00c58120`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58120.md) [`00c5d650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d650.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfadf8",
      "incomplete_value": false,
      "site": "00bfadfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:d42:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa9d0",
      "incomplete_value": false,
      "site": "00bfa9d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:d02:8"
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
      "definition_site": "00bfae04",
      "incomplete_value": false,
      "site": "00bfae0c",
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
            "const:4ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfa9dc",
      "incomplete_value": false,
      "site": "00bfa9e4",
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
            "const:46b:8"
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
      "00bfadf8",
      "PARAM",
      [
        "storage",
        "002b8d02",
        null,
        "string"
      ]
    ],
    [
      "00bfae04",
      "PARAM",
      [
        "storage",
        "002ac46b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfadf8",
      "PARAM",
      [
        "storage",
        "002b8d42",
        null,
        "string"
      ]
    ],
    [
      "00bfae04",
      "PARAM",
      [
        "storage",
        "002ac4ab",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfa9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa954.md#insn-00bfa9d4) · [`00bfa9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa954.md#insn-00bfa9e4) · [`00bfa978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa954.md#insn-00bfa978)
- 新版 `00bfadfc`（命令位置の公開資料なし） · `00bfae0c`（命令位置の公開資料なし） · `00bfada0`（命令位置の公開資料なし）

~~~diff
- 00bfa9d4 ["INT_ADD", "register:40f0:8", ["const:bfa9d4:8", "const:4:8"]]
- 00bfa9d4 ["CALL", null, ["callee:00c58120:8"]]
+ 00bfadfc ["INT_ADD", "register:40f0:8", ["const:bfadfc:8", "const:4:8"]]
+ 00bfadfc ["CALL", null, ["callee:00c58120:8"]]
- 00bfa9d4 bytes d3740194
+ 00bfadfc bytes c9740194
- 00bfa9e4 ["INT_ADD", "register:40f0:8", ["const:bfa9e4:8", "const:4:8"]]
- 00bfa9e4 ["CALL", null, ["callee:00c58120:8"]]
+ 00bfae0c ["INT_ADD", "register:40f0:8", ["const:bfae0c:8", "const:4:8"]]
+ 00bfae0c ["CALL", null, ["callee:00c58120:8"]]
- 00bfa9e4 bytes cf740194
+ 00bfae0c bytes c5740194
- 00bfa978 ["INT_ADD", "register:40f0:8", ["const:bfa978:8", "const:4:8"]]
- 00bfa978 ["CALL", null, ["callee:00c580c0:8"]]
+ 00bfada0 ["INT_ADD", "register:40f0:8", ["const:bfada0:8", "const:4:8"]]
+ 00bfada0 ["CALL", null, ["callee:00c580c0:8"]]
- 00bfa978 bytes d2740194
+ 00bfada0 bytes c8740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3414344248706c62645da7b9f5fa549"></a>

### [`00bfaac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaac4.md) → [`00bfaeec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfaeec.md) _ZNSt6__ndk117iostream_categoryEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfaf20",
      "incomplete_value": false,
      "site": "00bfaf24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfaaf8",
      "incomplete_value": false,
      "site": "00bfaafc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfaf30",
      "incomplete_value": false,
      "site": "00bfaf34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfab08",
      "incomplete_value": false,
      "site": "00bfab0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bfaf0c",
      "incomplete_value": false,
      "site": "00bfaf18",
      "value": [
        "leaf",
        "const:ca4800:8"
      ]
    },
    "old": {
      "definition_site": "00bfaae4",
      "incomplete_value": false,
      "site": "00bfaaf0",
      "value": [
        "leaf",
        "const:ca4400:8"
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
      "00bfaf00",
      "READ",
      [
        "storage",
        "01126f90",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfaf0c",
      "DATA",
      [
        "storage",
        "00ca4400",
        null,
        "pointer"
      ]
    ],
    [
      "00bfaf20",
      "PARAM",
      [
        "storage",
        "01126f90",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bfaf00",
      "READ",
      [
        "storage",
        "01127390",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfaf0c",
      "DATA",
      [
        "storage",
        "00ca4800",
        null,
        "pointer"
      ]
    ],
    [
      "00bfaf20",
      "PARAM",
      [
        "storage",
        "01127390",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfaafc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaac4.md#insn-00bfaafc) · [`00bfab0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaac4.md#insn-00bfab0c) · [`00bfaad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaac4.md#insn-00bfaad0)
- 新版 `00bfaf24`（命令位置の公開資料なし） · `00bfaf34`（命令位置の公開資料なし） · `00bfaef8`（命令位置の公開資料なし）

~~~diff
- 00bfaafc ["INT_ADD", "register:40f0:8", ["const:bfaafc:8", "const:4:8"]]
- 00bfaafc ["CALL", null, ["callee:00c57e50:8"]]
+ 00bfaf24 ["INT_ADD", "register:40f0:8", ["const:bfaf24:8", "const:4:8"]]
+ 00bfaf24 ["CALL", null, ["callee:00c57e50:8"]]
- 00bfaafc bytes d5730194
+ 00bfaf24 bytes cb730194
- 00bfab0c ["INT_ADD", "register:40f0:8", ["const:bfab0c:8", "const:4:8"]]
- 00bfab0c ["CALL", null, ["callee:00c57e70:8"]]
+ 00bfaf34 ["INT_ADD", "register:40f0:8", ["const:bfaf34:8", "const:4:8"]]
+ 00bfaf34 ["CALL", null, ["callee:00c57e70:8"]]
- 00bfab0c bytes d9730194
+ 00bfaf34 bytes cf730194
- 00bfaad0 ["COPY", "register:4040:8", ["const:1126000:8"]]
+ 00bfaef8 ["COPY", "register:4040:8", ["const:1127000:8"]]
- 00bfaad0 bytes 68290090
+ 00bfaef8 bytes 682900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2fd5e48d379b85e89b535aafbc16714"></a>

### [`00bfaccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaccc.md) → [`00bfb0f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb0f4.md) _ZNSt6__ndk18ios_base6xallocEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53880.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb108",
      "incomplete_value": true,
      "site": "00bfb10c",
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
                "const:af8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bface0",
      "incomplete_value": true,
      "site": "00bface4",
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
                "const:6f8:8"
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
      "00bfb108",
      "READ",
      [
        "storage",
        "00c9b6f8",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb108",
      "PARAM",
      [
        "storage",
        "01126f98",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bfb108",
      "READ",
      [
        "storage",
        "00c9baf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb108",
      "PARAM",
      [
        "storage",
        "01127398",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bface4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaccc.md#insn-00bface4) · [`00bface0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaccc.md#insn-00bface0)
- 新版 `00bfb10c`（命令位置の公開資料なし） · `00bfb108`（命令位置の公開資料なし）

~~~diff
- 00bface4 ["INT_ADD", "register:40f0:8", ["const:bface4:8", "const:4:8"]]
- 00bface4 ["CALL", null, ["callee:00c53ca0:8"]]
+ 00bfb10c ["INT_ADD", "register:40f0:8", ["const:bfb10c:8", "const:4:8"]]
+ 00bfb10c ["CALL", null, ["callee:00c53ca0:8"]]
- 00bface4 bytes e7620194
+ 00bfb10c bytes e5620194
- 00bface0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:6f8:8"]]
- 00bface0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfb108 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:af8:8"]]
+ 00bfb108 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bface0 bytes 217c43f9
+ 00bfb108 bytes 217c45f9
~~~


<a id="compare-ba981ce36db9966105080696433cc489"></a>

### [`00bfacf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfacf4.md) → [`00bfb11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb11c.md) _ZNSt6__ndk18ios_base5iwordEi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bfb11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bfb544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfb21c",
      "incomplete_value": false,
      "site": "00bfb21c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfadf4",
      "incomplete_value": false,
      "site": "00bfadf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:fa0:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb228",
      "incomplete_value": false,
      "site": "00bfb22c",
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
            "const:536:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfae00",
      "incomplete_value": false,
      "site": "00bfae04",
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
            "const:45a:8"
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
      "00bfb218",
      "DATA",
      [
        "storage",
        "01126fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb21c",
      "WRITE",
      [
        "storage",
        "01126fa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb228",
      "PARAM",
      [
        "storage",
        "002a745a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb218",
      "DATA",
      [
        "storage",
        "011273a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb21c",
      "WRITE",
      [
        "storage",
        "011273a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb228",
      "PARAM",
      [
        "storage",
        "002a7536",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfae04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfacf4.md#insn-00bfae04) · [`00bfad4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfacf4.md#insn-00bfad4c) · [`00bfad9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfacf4.md#insn-00bfad9c)
- 新版 `00bfb22c`（命令位置の公開資料なし） · `00bfb174`（命令位置の公開資料なし） · `00bfb1c4`（命令位置の公開資料なし）

~~~diff
- 00bfae04 ["INT_ADD", "register:40f0:8", ["const:bfae04:8", "const:4:8"]]
- 00bfae04 ["CALL", null, ["callee:00bfb544:8"]]
+ 00bfb22c ["INT_ADD", "register:40f0:8", ["const:bfb22c:8", "const:4:8"]]
+ 00bfb22c ["CALL", null, ["callee:00bfb544:8"]]
- 00bfae04 bytes c6000094
+ 00bfb22c bytes c6000094
- 00bfad4c ["INT_ADD", "register:40f0:8", ["const:bfad4c:8", "const:4:8"]]
- 00bfad4c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00bfb174 ["INT_ADD", "register:40f0:8", ["const:bfb174:8", "const:4:8"]]
+ 00bfb174 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00bfad4c bytes d57b0194
+ 00bfb174 bytes cb7b0194
- 00bfad9c ["INT_ADD", "register:40f0:8", ["const:bfad9c:8", "const:4:8"]]
- 00bfad9c ["CALL", null, ["callee:00c58090:8"]]
+ 00bfb1c4 ["INT_ADD", "register:40f0:8", ["const:bfb1c4:8", "const:4:8"]]
+ 00bfb1c4 ["CALL", null, ["callee:00c58090:8"]]
- 00bfad9c bytes bd730194
+ 00bfb1c4 bytes b3730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efbff026601455d7345132883947531d"></a>

### [`00bfae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfae08.md) → [`00bfb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb230.md) _ZNSt6__ndk18ios_base5pwordEi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bfb11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bfb544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfb330",
      "incomplete_value": false,
      "site": "00bfb330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1127000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfaf08",
      "incomplete_value": false,
      "site": "00bfaf08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb33c",
      "incomplete_value": false,
      "site": "00bfb340",
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
            "const:536:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfaf14",
      "incomplete_value": false,
      "site": "00bfaf18",
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
            "const:45a:8"
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
      "00bfb32c",
      "DATA",
      [
        "storage",
        "01126fa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb330",
      "WRITE",
      [
        "storage",
        "01126fa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb33c",
      "PARAM",
      [
        "storage",
        "002a745a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb32c",
      "DATA",
      [
        "storage",
        "011273a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb330",
      "WRITE",
      [
        "storage",
        "011273a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfb33c",
      "PARAM",
      [
        "storage",
        "002a7536",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfaf18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfae08.md#insn-00bfaf18) · [`00bfae60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfae08.md#insn-00bfae60) · [`00bfaeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfae08.md#insn-00bfaeb0)
- 新版 `00bfb340`（命令位置の公開資料なし） · `00bfb288`（命令位置の公開資料なし） · `00bfb2d8`（命令位置の公開資料なし）

~~~diff
- 00bfaf18 ["INT_ADD", "register:40f0:8", ["const:bfaf18:8", "const:4:8"]]
- 00bfaf18 ["CALL", null, ["callee:00bfb544:8"]]
+ 00bfb340 ["INT_ADD", "register:40f0:8", ["const:bfb340:8", "const:4:8"]]
+ 00bfb340 ["CALL", null, ["callee:00bfb544:8"]]
- 00bfaf18 bytes 81000094
+ 00bfb340 bytes 81000094
- 00bfae60 ["INT_ADD", "register:40f0:8", ["const:bfae60:8", "const:4:8"]]
- 00bfae60 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00bfb288 ["INT_ADD", "register:40f0:8", ["const:bfb288:8", "const:4:8"]]
+ 00bfb288 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00bfae60 bytes 907b0194
+ 00bfb288 bytes 867b0194
- 00bfaeb0 ["INT_ADD", "register:40f0:8", ["const:bfaeb0:8", "const:4:8"]]
- 00bfaeb0 ["CALL", null, ["callee:00c58090:8"]]
+ 00bfb2d8 ["INT_ADD", "register:40f0:8", ["const:bfb2d8:8", "const:4:8"]]
+ 00bfb2d8 ["CALL", null, ["callee:00c58090:8"]]
- 00bfaeb0 bytes 78730194
+ 00bfb2d8 bytes 6e730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fc752b7de7f137a85f548153d788a32"></a>

### [`00bfaf1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaf1c.md) → [`00bfb344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb344.md) _ZNSt6__ndk18ios_base17register_callbackEPFvNS0_5eventERS0_iEi

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bfb11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bfb544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md) [`00c5a0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb41c",
      "incomplete_value": false,
      "site": "00bfb420",
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
            "const:536:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfaff4",
      "incomplete_value": false,
      "site": "00bfaff8",
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
            "const:45a:8"
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
      "00bfb41c",
      "PARAM",
      [
        "storage",
        "002a745a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb41c",
      "PARAM",
      [
        "storage",
        "002a7536",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfaff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaf1c.md#insn-00bfaff8) · [`00bfaf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaf1c.md#insn-00bfaf70) · [`00bfaf9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaf1c.md#insn-00bfaf9c)
- 新版 `00bfb420`（命令位置の公開資料なし） · `00bfb398`（命令位置の公開資料なし） · `00bfb3c4`（命令位置の公開資料なし）

~~~diff
- 00bfaff8 ["INT_ADD", "register:40f0:8", ["const:bfaff8:8", "const:4:8"]]
- 00bfaff8 ["CALL", null, ["callee:00bfb544:8"]]
+ 00bfb420 ["INT_ADD", "register:40f0:8", ["const:bfb420:8", "const:4:8"]]
+ 00bfb420 ["CALL", null, ["callee:00bfb544:8"]]
- 00bfaff8 bytes 49000094
+ 00bfb420 bytes 49000094
- 00bfaf70 ["INT_ADD", "register:40f0:8", ["const:bfaf70:8", "const:4:8"]]
- 00bfaf70 ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00bfb398 ["INT_ADD", "register:40f0:8", ["const:bfb398:8", "const:4:8"]]
+ 00bfb398 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00bfaf70 bytes 4c7b0194
+ 00bfb398 bytes 427b0194
- 00bfaf9c ["INT_ADD", "register:40f0:8", ["const:bfaf9c:8", "const:4:8"]]
- 00bfaf9c ["CALL", null, ["callee:00c5a0a0:8"]]
+ 00bfb3c4 ["INT_ADD", "register:40f0:8", ["const:bfb3c4:8", "const:4:8"]]
+ 00bfb3c4 ["CALL", null, ["callee:00c5a0a0:8"]]
- 00bfaf9c bytes 417b0194
+ 00bfb3c4 bytes 377b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03728a4fe95c5cc072cddef1c0891eb1"></a>

### [`00bfaffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaffc.md) → [`00bfb424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb424.md) _ZNSt6__ndk18ios_baseD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md) [`00c5def0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5def0.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)
- 新版 呼出元 2件 [`00c5d0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0e0.md) [`00c5e2f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2f0.md) · 呼出先 2件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfb448",
      "incomplete_value": true,
      "site": "00bfb44c",
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
      "definition_site": "00bfb020",
      "incomplete_value": true,
      "site": "00bfb024",
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
      "00bfb440",
      "READ",
      [
        "storage",
        "00c9b700",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb44c",
      "DATA",
      [
        "storage",
        "00c929a8",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00bfb440",
      "READ",
      [
        "storage",
        "00c9bb00",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb44c",
      "DATA",
      [
        "storage",
        "00c92da8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaffc.md#insn-00bfb018) · [`00bfb050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaffc.md#insn-00bfb050) · [`00bfb064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaffc.md#insn-00bfb064)
- 新版 `00bfb440`（命令位置の公開資料なし） · `00bfb478`（命令位置の公開資料なし） · `00bfb48c`（命令位置の公開資料なし）

~~~diff
- 00bfb018 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:700:8"]]
- 00bfb018 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfb440 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b00:8"]]
+ 00bfb440 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfb018 bytes 088143f9
+ 00bfb440 bytes 088145f9
- 00bfb050 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bfb050 ["INT_ADD", "register:40f0:8", ["const:bfb050:8", "const:4:8"]]
- 00bfb050 ["CALLIND", null, ["register:0:8"]]
+ 00bfb478 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfb478 ["INT_ADD", "register:40f0:8", ["const:bfb478:8", "const:4:8"]]
+ 00bfb478 ["CALLIND", null, ["register:0:8"]]
- 00bfb050 bytes 00013fd6
+ 00bfb478 bytes 00013fd6
- 00bfb064 ["INT_ADD", "register:40f0:8", ["const:bfb064:8", "const:4:8"]]
- 00bfb064 ["CALL", null, ["callee:00c58290:8"]]
+ 00bfb48c ["INT_ADD", "register:40f0:8", ["const:bfb48c:8", "const:4:8"]]
+ 00bfb48c ["CALL", null, ["callee:00c58290:8"]]
- 00bfb064 bytes 8b730194
+ 00bfb48c bytes 81730194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54420962c985a2222da1dcf94c24819d"></a>

### [`00bfb0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0dc.md) → [`00bfb504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb504.md) _ZNSt6__ndk18ios_base5clearEj

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) · 呼出先 1件 [`00bfb11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md)
- 新版 呼出元 1件 [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) · 呼出先 1件 [`00bfb544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb53c",
      "incomplete_value": false,
      "site": "00bfb540",
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
            "const:536:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb114",
      "incomplete_value": false,
      "site": "00bfb118",
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
            "const:45a:8"
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
      "00bfb53c",
      "PARAM",
      [
        "storage",
        "002a745a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb53c",
      "PARAM",
      [
        "storage",
        "002a7536",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0dc.md#insn-00bfb118) · [`00bfb114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0dc.md#insn-00bfb114)
- 新版 `00bfb540`（命令位置の公開資料なし） · `00bfb53c`（命令位置の公開資料なし）

~~~diff
- 00bfb118 ["INT_ADD", "register:40f0:8", ["const:bfb118:8", "const:4:8"]]
- 00bfb118 ["CALL", null, ["callee:00bfb544:8"]]
+ 00bfb540 ["INT_ADD", "register:40f0:8", ["const:bfb540:8", "const:4:8"]]
+ 00bfb540 ["CALL", null, ["callee:00bfb544:8"]]
- 00bfb118 bytes 01000094
+ 00bfb540 bytes 01000094
- 00bfb114 ["COPY", "tmp:0:8", ["const:45a:8"]]
- 00bfb114 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bfb114 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bfb114 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bfb53c ["COPY", "tmp:0:8", ["const:536:8"]]
+ 00bfb53c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfb53c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfb53c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bfb114 bytes 00681191
+ 00bfb53c bytes 00d81491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e160668c62c12523a433ff820a781c8"></a>

### [`00bfb11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md) → [`00bfb544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb544.md) FUN_00bfb544

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00bfacf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfacf4.md) [`00bfae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfae08.md) [`00bfaf1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaf1c.md) [`00bfb0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0dc.md) · 呼出先 6件 [`00bfab94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab94.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)
- 新版 呼出元 4件 [`00bfb11c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb11c.md) [`00bfb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb230.md) [`00bfb344`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb344.md) [`00bfb504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb504.md) · 呼出先 6件 [`00bfafbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfafbc.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfb584",
      "incomplete_value": false,
      "site": "00bfb584",
      "value": [
        "leaf",
        "const:ca4800:8"
      ]
    },
    "old": {
      "definition_site": "00bfb15c",
      "incomplete_value": false,
      "site": "00bfb15c",
      "value": [
        "leaf",
        "const:ca4400:8"
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb5a4",
      "incomplete_value": true,
      "site": "00bfb5ac",
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
                "const:b08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb17c",
      "incomplete_value": true,
      "site": "00bfb184",
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
                "const:708:8"
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
      "definition_site": "00bfb5a8",
      "incomplete_value": true,
      "site": "00bfb5ac",
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
                "const:af0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb180",
      "incomplete_value": true,
      "site": "00bfb184",
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
                "const:6f0:8"
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
      "00bfb570",
      "READ",
      [
        "storage",
        "01126f90",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfb584",
      "DATA",
      [
        "storage",
        "00ca4400",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb5a4",
      "READ",
      [
        "storage",
        "00c9b708",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfb570",
      "READ",
      [
        "storage",
        "01127390",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfb584",
      "DATA",
      [
        "storage",
        "00ca4800",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb5a4",
      "READ",
      [
        "storage",
        "00c9bb08",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md#insn-00bfb184) · [`00bfb190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md#insn-00bfb190) · [`00bfb1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md#insn-00bfb1a0)
- 新版 `00bfb5ac`（命令位置の公開資料なし） · `00bfb5b8`（命令位置の公開資料なし） · `00bfb5c8`（命令位置の公開資料なし）

~~~diff
- 00bfb184 ["INT_ADD", "register:40f0:8", ["const:bfb184:8", "const:4:8"]]
- 00bfb184 ["CALL", null, ["callee:00c57f10:8"]]
+ 00bfb5ac ["INT_ADD", "register:40f0:8", ["const:bfb5ac:8", "const:4:8"]]
+ 00bfb5ac ["CALL", null, ["callee:00c57f10:8"]]
- 00bfb184 bytes 63720194
+ 00bfb5ac bytes 59720194
- 00bfb190 ["INT_ADD", "register:40f0:8", ["const:bfb190:8", "const:4:8"]]
- 00bfb190 ["CALL", null, ["callee:00c57e50:8"]]
+ 00bfb5b8 ["INT_ADD", "register:40f0:8", ["const:bfb5b8:8", "const:4:8"]]
+ 00bfb5b8 ["CALL", null, ["callee:00c57e50:8"]]
- 00bfb190 bytes 30720194
+ 00bfb5b8 bytes 26720194
- 00bfb1a0 ["INT_ADD", "register:40f0:8", ["const:bfb1a0:8", "const:4:8"]]
- 00bfb1a0 ["CALL", null, ["callee:00c57e70:8"]]
+ 00bfb5c8 ["INT_ADD", "register:40f0:8", ["const:bfb5c8:8", "const:4:8"]]
+ 00bfb5c8 ["CALL", null, ["callee:00c57e70:8"]]
- 00bfb1a0 bytes 34720194
+ 00bfb5c8 bytes 2a720194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62e37bdcaef166ebe1c8d347e50b11ee"></a>

### [`00bfb1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb1bc.md) → [`00bfb5e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb5e4.md) _ZNSt6__ndk18ios_base4initEPv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) · 呼出先 1件 [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md)
- 新版 呼出元 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md) · 呼出先 1件 [`00c5a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfb5f4",
      "incomplete_value": true,
      "site": "00bfb608",
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
                "const:30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb1cc",
      "incomplete_value": true,
      "site": "00bfb1e0",
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
                "const:ff0:8"
              ]
            ]
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
      "00bfb5f4",
      "READ",
      [
        "storage",
        "002c2ff0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfb5f4",
      "READ",
      [
        "storage",
        "002c3030",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb1bc.md#insn-00bfb1c0) · [`00bfb1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb1bc.md#insn-00bfb1cc)
- 新版 `00bfb5e8`（命令位置の公開資料なし） · `00bfb5f4`（命令位置の公開資料なし）

~~~diff
- 00bfb1c0 ["COPY", "register:4048:8", ["const:2c2000:8"]]
+ 00bfb5e8 ["COPY", "register:4048:8", ["const:2c3000:8"]]
- 00bfb1c0 bytes 29b6fff0
+ 00bfb5e8 bytes 49b6ff90
- 00bfb1cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ff0:8"]]
- 00bfb1cc ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00bfb1cc ["COPY", "register:5010:8", ["const:0:8"]]
- 00bfb1cc ["COPY", "register:5018:8", ["const:0:8"]]
+ 00bfb5f4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:30:8"]]
+ 00bfb5f4 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bfb5f4 ["COPY", "register:5010:8", ["const:0:8"]]
+ 00bfb5f4 ["COPY", "register:5018:8", ["const:0:8"]]
- 00bfb1cc bytes 20fdc33d
+ 00bfb5f4 bytes 200dc03d
~~~


<a id="compare-4ee4aec48cf21bb27c35c7a881a715ad"></a>

### [`00bfb6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6d8.md) → [`00bfbb00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbb00.md) _ZNSt6__ndk18ios_base15sync_with_stdioEb

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfbb10",
      "incomplete_value": false,
      "site": "00bfbb10",
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
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfb6e8",
      "incomplete_value": false,
      "site": "00bfb6e8",
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
            "const:408:8"
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
      "00bfbb0c",
      "READ",
      [
        "storage",
        "00ca4408",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfbb10",
      "WRITE",
      [
        "storage",
        "00ca4408",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bfbb0c",
      "READ",
      [
        "storage",
        "00ca4808",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfbb10",
      "WRITE",
      [
        "storage",
        "00ca4808",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfb6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6d8.md#insn-00bfb6e8) · [`00bfb6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6d8.md#insn-00bfb6e4)
- 新版 `00bfbb10`（命令位置の公開資料なし） · `00bfbb0c`（命令位置の公開資料なし）

~~~diff
- 00bfb6e8 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bfb6e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "const:408:8"]]
- 00bfb6e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bfbb10 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bfbb10 ["INT_ADD", "tmp:1:8", ["register:4050:8", "const:808:8"]]
+ 00bfbb10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bfb6e8 bytes 49211039
+ 00bfbb10 bytes 49212039
- 00bfb6e4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:408:8"]]
- 00bfb6e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bfb6e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bfbb0c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:808:8"]]
+ 00bfbb0c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bfbb0c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bfb6e4 bytes 48215039
+ 00bfbb0c bytes 48216039
~~~


<a id="compare-46fe0c195751705105aa8335106dbfe5"></a>

### [`00bfba74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfba74.md) → [`00bfbe9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbe9c.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md) · 呼出先 1件 [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md)
- 新版 呼出元 1件 [`00c581f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581f0.md) · 呼出先 1件 [`00c5a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfbebc",
      "incomplete_value": true,
      "site": "00bfbebc",
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
      "definition_site": "00bfba94",
      "incomplete_value": true,
      "site": "00bfba94",
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
      "00bfbeb4",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbebc",
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00bfbeb4",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbebc",
      "DATA",
      [
        "storage",
        "00c90cb0",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfba8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfba74.md#insn-00bfba8c) · [`00bfba98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfba74.md#insn-00bfba98)
- 新版 `00bfbeb4`（命令位置の公開資料なし） · `00bfbec0`（命令位置の公開資料なし）

~~~diff
- 00bfba8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
- 00bfba8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfbeb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:848:8"]]
+ 00bfbeb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfba8c bytes 082542f9
+ 00bfbeb4 bytes 082544f9
- 00bfba98 ["INT_ADD", "register:40f0:8", ["const:bfba98:8", "const:4:8"]]
- 00bfba98 ["CALL", null, ["callee:00c5a7a0:8"]]
+ 00bfbec0 ["INT_ADD", "register:40f0:8", ["const:bfbec0:8", "const:4:8"]]
+ 00bfbec0 ["CALL", null, ["callee:00c5a7a0:8"]]
- 00bfba98 bytes 427a0194
+ 00bfbec0 bytes 387a0194
~~~


<a id="compare-e48bd63a5528c3ade746e473c6f33633"></a>

### [`00bfbab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbab8.md) → [`00bfbee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbee0.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1ERKS3_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfbf08",
      "incomplete_value": true,
      "site": "00bfbf08",
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
      "definition_site": "00bfbae0",
      "incomplete_value": true,
      "site": "00bfbae0",
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
      "00bfbefc",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbf08",
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00bfbefc",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbf08",
      "DATA",
      [
        "storage",
        "00c90cb0",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfbad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbab8.md#insn-00bfbad4) · [`00bfbae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbab8.md#insn-00bfbae4)
- 新版 `00bfbefc`（命令位置の公開資料なし） · `00bfbf0c`（命令位置の公開資料なし）

~~~diff
- 00bfbad4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
- 00bfbad4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfbefc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:848:8"]]
+ 00bfbefc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfbad4 bytes 082542f9
+ 00bfbefc bytes 082544f9
- 00bfbae4 ["INT_ADD", "register:40f0:8", ["const:bfbae4:8", "const:4:8"]]
- 00bfbae4 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00bfbf0c ["INT_ADD", "register:40f0:8", ["const:bfbf0c:8", "const:4:8"]]
+ 00bfbf0c ["CALL", null, ["callee:00c5a7d0:8"]]
- 00bfbae4 bytes 3b7a0194
+ 00bfbf0c bytes 317a0194
~~~


<a id="compare-f5bfb0f544c704ecb29acdbada06cf47"></a>

### [`00bfbcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbcc0.md) → [`00bfc0e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc0e8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c581e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c581e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfc114",
      "incomplete_value": true,
      "site": "00bfc114",
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
      "definition_site": "00bfbcec",
      "incomplete_value": true,
      "site": "00bfbcec",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfc118",
      "incomplete_value": true,
      "site": "00bfc118",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfbcf0",
      "incomplete_value": true,
      "site": "00bfbcf0",
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
            "const:18:8"
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
      "00bfc104",
      "READ",
      [
        "storage",
        "00c9ae30",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc114",
      "DATA",
      [
        "storage",
        "00c92a38",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc118",
      "DATA",
      [
        "storage",
        "00c92a10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfc104",
      "READ",
      [
        "storage",
        "00c9b230",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc114",
      "DATA",
      [
        "storage",
        "00c92e38",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc118",
      "DATA",
      [
        "storage",
        "00c92e10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfbcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbcc0.md#insn-00bfbcd0) · [`00bfbcdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbcc0.md#insn-00bfbcdc) · [`00bfbcf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbcc0.md#insn-00bfbcf8)
- 新版 `00bfc0f8`（命令位置の公開資料なし） · `00bfc104`（命令位置の公開資料なし） · `00bfc120`（命令位置の公開資料なし）

~~~diff
- 00bfbcd0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00bfc0f8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00bfbcd0 bytes e80400f0
+ 00bfc0f8 bytes e80400f0
- 00bfbcdc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e30:8"]]
- 00bfbcdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfc104 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:230:8"]]
+ 00bfc104 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfbcdc bytes 081947f9
+ 00bfc104 bytes 081941f9
- 00bfbcf8 ["INT_ADD", "register:40f0:8", ["const:bfbcf8:8", "const:4:8"]]
- 00bfbcf8 ["CALL", null, ["callee:00c581e0:8"]]
+ 00bfc120 ["INT_ADD", "register:40f0:8", ["const:bfc120:8", "const:4:8"]]
+ 00bfc120 ["CALL", null, ["callee:00c581e0:8"]]
- 00bfbcf8 bytes 3a700194
+ 00bfc120 bytes 30700194
~~~


<a id="compare-6b0e3917c926e767d484ffed57c37796"></a>

### [`00bfbda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbda0.md) → [`00bfc1c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc1c8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c58af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58af0.md)
- 新版 呼出元 1件 [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c58ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc258",
      "incomplete_value": true,
      "site": "00bfc25c",
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
      "definition_site": "00bfbe30",
      "incomplete_value": true,
      "site": "00bfbe34",
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
      "00bfc258",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc258",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc258",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc258",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfbe34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbda0.md#insn-00bfbe34) · [`00bfbe00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbda0.md#insn-00bfbe00) · [`00bfbe24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbda0.md#insn-00bfbe24)
- 新版 `00bfc25c`（命令位置の公開資料なし） · `00bfc228`（命令位置の公開資料なし） · `00bfc24c`（命令位置の公開資料なし）

~~~diff
- 00bfbe34 ["INT_ADD", "register:40f0:8", ["const:bfbe34:8", "const:4:8"]]
- 00bfbe34 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfc25c ["INT_ADD", "register:40f0:8", ["const:bfc25c:8", "const:4:8"]]
+ 00bfc25c ["CALL", null, ["callee:00c58280:8"]]
- 00bfbe34 bytes 13700194
+ 00bfc25c bytes 09700194
- 00bfbe00 ["INT_ADD", "register:40f0:8", ["const:bfbe00:8", "const:4:8"]]
- 00bfbe00 ["CALL", null, ["callee:00c58ef0:8"]]
+ 00bfc228 ["INT_ADD", "register:40f0:8", ["const:bfc228:8", "const:4:8"]]
+ 00bfc228 ["CALL", null, ["callee:00c58ef0:8"]]
- 00bfbe00 bytes 3c730194
+ 00bfc228 bytes 32730194
- 00bfbe24 ["INT_ADD", "register:40f0:8", ["const:bfbe24:8", "const:4:8"]]
- 00bfbe24 ["CALL", null, ["callee:00c58270:8"]]
+ 00bfc24c ["INT_ADD", "register:40f0:8", ["const:bfc24c:8", "const:4:8"]]
+ 00bfc24c ["CALL", null, ["callee:00c58270:8"]]
- 00bfbe24 bytes 13700194
+ 00bfc24c bytes 09700194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-080a2b916952bdca1c430473a40baf2d"></a>

### [`00bfc1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc1b0.md) → [`00bfc5d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc5d8.md) FUN_00bfc5d8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfc1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc1a8.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfc5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc5d0.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc62c",
      "incomplete_value": true,
      "site": "00bfc630",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfc204",
      "incomplete_value": true,
      "site": "00bfc208",
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
                "const:710:8"
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
      "00bfc62c",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc62c",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc62c",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc62c",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc1b0.md#insn-00bfc208) · [`00bfc1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc1b0.md#insn-00bfc1dc) · [`00bfc1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc1b0.md#insn-00bfc1f8)
- 新版 `00bfc630`（命令位置の公開資料なし） · `00bfc604`（命令位置の公開資料なし） · `00bfc620`（命令位置の公開資料なし）

~~~diff
- 00bfc208 ["INT_ADD", "register:40f0:8", ["const:bfc208:8", "const:4:8"]]
- 00bfc208 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfc630 ["INT_ADD", "register:40f0:8", ["const:bfc630:8", "const:4:8"]]
+ 00bfc630 ["CALL", null, ["callee:00c58280:8"]]
- 00bfc208 bytes 1e6f0194
+ 00bfc630 bytes 146f0194
- 00bfc1dc ["INT_ADD", "register:40f0:8", ["const:bfc1dc:8", "const:4:8"]]
- 00bfc1dc ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfc604 ["INT_ADD", "register:40f0:8", ["const:bfc604:8", "const:4:8"]]
+ 00bfc604 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfc1dc bytes fd750194
+ 00bfc604 bytes f3750194
- 00bfc1f8 ["INT_ADD", "register:40f0:8", ["const:bfc1f8:8", "const:4:8"]]
- 00bfc1f8 ["CALL", null, ["callee:00c58270:8"]]
+ 00bfc620 ["INT_ADD", "register:40f0:8", ["const:bfc620:8", "const:4:8"]]
+ 00bfc620 ["CALL", null, ["callee:00c58270:8"]]
- 00bfc1f8 bytes 1e6f0194
+ 00bfc620 bytes 146f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca6534d6bd07a469a8e0ad91e37cada8"></a>

### [`00bfc2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc2e8.md) → [`00bfc710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc710.md) FUN_00bfc710

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfc2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc2e0.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfc708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc708.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.44% / 新版 98.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc764",
      "incomplete_value": true,
      "site": "00bfc768",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfc33c",
      "incomplete_value": true,
      "site": "00bfc340",
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
                "const:710:8"
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
      "00bfc764",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc764",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc764",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc764",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc2e8.md#insn-00bfc340) · [`00bfc314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc2e8.md#insn-00bfc314) · [`00bfc330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc2e8.md#insn-00bfc330)
- 新版 `00bfc768`（命令位置の公開資料なし） · `00bfc73c`（命令位置の公開資料なし） · `00bfc758`（命令位置の公開資料なし）

~~~diff
- 00bfc340 ["INT_ADD", "register:40f0:8", ["const:bfc340:8", "const:4:8"]]
- 00bfc340 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfc768 ["INT_ADD", "register:40f0:8", ["const:bfc768:8", "const:4:8"]]
+ 00bfc768 ["CALL", null, ["callee:00c58280:8"]]
- 00bfc340 bytes d06e0194
+ 00bfc768 bytes c66e0194
- 00bfc314 ["INT_ADD", "register:40f0:8", ["const:bfc314:8", "const:4:8"]]
- 00bfc314 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfc73c ["INT_ADD", "register:40f0:8", ["const:bfc73c:8", "const:4:8"]]
+ 00bfc73c ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfc314 bytes af750194
+ 00bfc73c bytes a5750194
- 00bfc330 ["INT_ADD", "register:40f0:8", ["const:bfc330:8", "const:4:8"]]
- 00bfc330 ["CALL", null, ["callee:00c58270:8"]]
+ 00bfc758 ["INT_ADD", "register:40f0:8", ["const:bfc758:8", "const:4:8"]]
+ 00bfc758 ["CALL", null, ["callee:00c58270:8"]]
- 00bfc330 bytes d06e0194
+ 00bfc758 bytes c66e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a9278a711f46463e44c53e1b7bd3f75"></a>

### [`00bfc460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc460.md) → [`00bfc888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc888.md) FUN_00bfc888

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfc458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc458.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfc880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc880.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc8dc",
      "incomplete_value": true,
      "site": "00bfc8e0",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfc4b4",
      "incomplete_value": true,
      "site": "00bfc4b8",
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
                "const:710:8"
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
      "00bfc8dc",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc8dc",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc8dc",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc8dc",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc460.md#insn-00bfc4b8) · [`00bfc48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc460.md#insn-00bfc48c) · [`00bfc4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc460.md#insn-00bfc4a8)
- 新版 `00bfc8e0`（命令位置の公開資料なし） · `00bfc8b4`（命令位置の公開資料なし） · `00bfc8d0`（命令位置の公開資料なし）

~~~diff
- 00bfc4b8 ["INT_ADD", "register:40f0:8", ["const:bfc4b8:8", "const:4:8"]]
- 00bfc4b8 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfc8e0 ["INT_ADD", "register:40f0:8", ["const:bfc8e0:8", "const:4:8"]]
+ 00bfc8e0 ["CALL", null, ["callee:00c58280:8"]]
- 00bfc4b8 bytes 726e0194
+ 00bfc8e0 bytes 686e0194
- 00bfc48c ["INT_ADD", "register:40f0:8", ["const:bfc48c:8", "const:4:8"]]
- 00bfc48c ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfc8b4 ["INT_ADD", "register:40f0:8", ["const:bfc8b4:8", "const:4:8"]]
+ 00bfc8b4 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfc48c bytes 51750194
+ 00bfc8b4 bytes 47750194
- 00bfc4a8 ["INT_ADD", "register:40f0:8", ["const:bfc4a8:8", "const:4:8"]]
- 00bfc4a8 ["CALL", null, ["callee:00c58270:8"]]
+ 00bfc8d0 ["INT_ADD", "register:40f0:8", ["const:bfc8d0:8", "const:4:8"]]
+ 00bfc8d0 ["CALL", null, ["callee:00c58270:8"]]
- 00bfc4a8 bytes 726e0194
+ 00bfc8d0 bytes 686e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7dc22440241af9af2a4163b0ecc31b2"></a>

### [`00bfc598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc598.md) → [`00bfc9c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc9c0.md) FUN_00bfc9c0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfc590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc590.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfc9b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc9b8.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfca14",
      "incomplete_value": true,
      "site": "00bfca18",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfc5ec",
      "incomplete_value": true,
      "site": "00bfc5f0",
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
                "const:710:8"
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
      "00bfca14",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfca14",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfca14",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfca14",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc598.md#insn-00bfc5f0) · [`00bfc5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc598.md#insn-00bfc5c4) · [`00bfc5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc598.md#insn-00bfc5e0)
- 新版 `00bfca18`（命令位置の公開資料なし） · `00bfc9ec`（命令位置の公開資料なし） · `00bfca08`（命令位置の公開資料なし）

~~~diff
- 00bfc5f0 ["INT_ADD", "register:40f0:8", ["const:bfc5f0:8", "const:4:8"]]
- 00bfc5f0 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfca18 ["INT_ADD", "register:40f0:8", ["const:bfca18:8", "const:4:8"]]
+ 00bfca18 ["CALL", null, ["callee:00c58280:8"]]
- 00bfc5f0 bytes 246e0194
+ 00bfca18 bytes 1a6e0194
- 00bfc5c4 ["INT_ADD", "register:40f0:8", ["const:bfc5c4:8", "const:4:8"]]
- 00bfc5c4 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfc9ec ["INT_ADD", "register:40f0:8", ["const:bfc9ec:8", "const:4:8"]]
+ 00bfc9ec ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfc5c4 bytes 03750194
+ 00bfc9ec bytes f9740194
- 00bfc5e0 ["INT_ADD", "register:40f0:8", ["const:bfc5e0:8", "const:4:8"]]
- 00bfc5e0 ["CALL", null, ["callee:00c58270:8"]]
+ 00bfca08 ["INT_ADD", "register:40f0:8", ["const:bfca08:8", "const:4:8"]]
+ 00bfca08 ["CALL", null, ["callee:00c58270:8"]]
- 00bfc5e0 bytes 246e0194
+ 00bfca08 bytes 1a6e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44e1d7dd1d89e35ac0c4061969869a13"></a>

### [`00bfc714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc714.md) → [`00bfcb3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcb3c.md) FUN_00bfcb3c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfc70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc70c.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfcb34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcb34.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfcb90",
      "incomplete_value": true,
      "site": "00bfcb94",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfc768",
      "incomplete_value": true,
      "site": "00bfc76c",
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
                "const:710:8"
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
      "00bfcb90",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcb90",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfcb90",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcb90",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc714.md#insn-00bfc76c) · [`00bfc740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc714.md#insn-00bfc740) · [`00bfc75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc714.md#insn-00bfc75c)
- 新版 `00bfcb94`（命令位置の公開資料なし） · `00bfcb68`（命令位置の公開資料なし） · `00bfcb84`（命令位置の公開資料なし）

~~~diff
- 00bfc76c ["INT_ADD", "register:40f0:8", ["const:bfc76c:8", "const:4:8"]]
- 00bfc76c ["CALL", null, ["callee:00c58280:8"]]
+ 00bfcb94 ["INT_ADD", "register:40f0:8", ["const:bfcb94:8", "const:4:8"]]
+ 00bfcb94 ["CALL", null, ["callee:00c58280:8"]]
- 00bfc76c bytes c56d0194
+ 00bfcb94 bytes bb6d0194
- 00bfc740 ["INT_ADD", "register:40f0:8", ["const:bfc740:8", "const:4:8"]]
- 00bfc740 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfcb68 ["INT_ADD", "register:40f0:8", ["const:bfcb68:8", "const:4:8"]]
+ 00bfcb68 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfc740 bytes a4740194
+ 00bfcb68 bytes 9a740194
- 00bfc75c ["INT_ADD", "register:40f0:8", ["const:bfc75c:8", "const:4:8"]]
- 00bfc75c ["CALL", null, ["callee:00c58270:8"]]
+ 00bfcb84 ["INT_ADD", "register:40f0:8", ["const:bfcb84:8", "const:4:8"]]
+ 00bfcb84 ["CALL", null, ["callee:00c58270:8"]]
- 00bfc75c bytes c56d0194
+ 00bfcb84 bytes bb6d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29a16b67d7fa98c2b0bfd39acfd5d26f"></a>

### [`00bfc84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc84c.md) → [`00bfcc74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcc74.md) FUN_00bfcc74

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfc844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc844.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfcc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcc6c.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfccc8",
      "incomplete_value": true,
      "site": "00bfcccc",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfc8a0",
      "incomplete_value": true,
      "site": "00bfc8a4",
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
                "const:710:8"
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
      "00bfccc8",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfccc8",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfccc8",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfccc8",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc84c.md#insn-00bfc8a4) · [`00bfc878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc84c.md#insn-00bfc878) · [`00bfc894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc84c.md#insn-00bfc894)
- 新版 `00bfcccc`（命令位置の公開資料なし） · `00bfcca0`（命令位置の公開資料なし） · `00bfccbc`（命令位置の公開資料なし）

~~~diff
- 00bfc8a4 ["INT_ADD", "register:40f0:8", ["const:bfc8a4:8", "const:4:8"]]
- 00bfc8a4 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfcccc ["INT_ADD", "register:40f0:8", ["const:bfcccc:8", "const:4:8"]]
+ 00bfcccc ["CALL", null, ["callee:00c58280:8"]]
- 00bfc8a4 bytes 776d0194
+ 00bfcccc bytes 6d6d0194
- 00bfc878 ["INT_ADD", "register:40f0:8", ["const:bfc878:8", "const:4:8"]]
- 00bfc878 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfcca0 ["INT_ADD", "register:40f0:8", ["const:bfcca0:8", "const:4:8"]]
+ 00bfcca0 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfc878 bytes 56740194
+ 00bfcca0 bytes 4c740194
- 00bfc894 ["INT_ADD", "register:40f0:8", ["const:bfc894:8", "const:4:8"]]
- 00bfc894 ["CALL", null, ["callee:00c58270:8"]]
+ 00bfccbc ["INT_ADD", "register:40f0:8", ["const:bfccbc:8", "const:4:8"]]
+ 00bfccbc ["CALL", null, ["callee:00c58270:8"]]
- 00bfc894 bytes 776d0194
+ 00bfccbc bytes 6d6d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2db143deb7df15f56e2a0b895a3789ed"></a>

### [`00bfc984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc984.md) → [`00bfcdac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcdac.md) FUN_00bfcdac

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfc97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc97c.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfcda4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcda4.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfce00",
      "incomplete_value": true,
      "site": "00bfce04",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfc9d8",
      "incomplete_value": true,
      "site": "00bfc9dc",
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
                "const:710:8"
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
      "00bfce00",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfce00",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfce00",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfce00",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfc9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc984.md#insn-00bfc9dc) · [`00bfc9b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc984.md#insn-00bfc9b0) · [`00bfc9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc984.md#insn-00bfc9cc)
- 新版 `00bfce04`（命令位置の公開資料なし） · `00bfcdd8`（命令位置の公開資料なし） · `00bfcdf4`（命令位置の公開資料なし）

~~~diff
- 00bfc9dc ["INT_ADD", "register:40f0:8", ["const:bfc9dc:8", "const:4:8"]]
- 00bfc9dc ["CALL", null, ["callee:00c58280:8"]]
+ 00bfce04 ["INT_ADD", "register:40f0:8", ["const:bfce04:8", "const:4:8"]]
+ 00bfce04 ["CALL", null, ["callee:00c58280:8"]]
- 00bfc9dc bytes 296d0194
+ 00bfce04 bytes 1f6d0194
- 00bfc9b0 ["INT_ADD", "register:40f0:8", ["const:bfc9b0:8", "const:4:8"]]
- 00bfc9b0 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfcdd8 ["INT_ADD", "register:40f0:8", ["const:bfcdd8:8", "const:4:8"]]
+ 00bfcdd8 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfc9b0 bytes 08740194
+ 00bfcdd8 bytes fe730194
- 00bfc9cc ["INT_ADD", "register:40f0:8", ["const:bfc9cc:8", "const:4:8"]]
- 00bfc9cc ["CALL", null, ["callee:00c58270:8"]]
+ 00bfcdf4 ["INT_ADD", "register:40f0:8", ["const:bfcdf4:8", "const:4:8"]]
+ 00bfcdf4 ["CALL", null, ["callee:00c58270:8"]]
- 00bfc9cc bytes 296d0194
+ 00bfcdf4 bytes 1f6d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bb5d03f04fce242fc269063ba306a67"></a>

### [`00bfcabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcabc.md) → [`00bfcee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcee4.md) FUN_00bfcee4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfcab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcab4.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfcedc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfcedc.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfcf38",
      "incomplete_value": true,
      "site": "00bfcf3c",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfcb10",
      "incomplete_value": true,
      "site": "00bfcb14",
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
                "const:710:8"
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
      "00bfcf38",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcf38",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfcf38",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcf38",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfcb14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcabc.md#insn-00bfcb14) · [`00bfcae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcabc.md#insn-00bfcae8) · [`00bfcb04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcabc.md#insn-00bfcb04)
- 新版 `00bfcf3c`（命令位置の公開資料なし） · `00bfcf10`（命令位置の公開資料なし） · `00bfcf2c`（命令位置の公開資料なし）

~~~diff
- 00bfcb14 ["INT_ADD", "register:40f0:8", ["const:bfcb14:8", "const:4:8"]]
- 00bfcb14 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfcf3c ["INT_ADD", "register:40f0:8", ["const:bfcf3c:8", "const:4:8"]]
+ 00bfcf3c ["CALL", null, ["callee:00c58280:8"]]
- 00bfcb14 bytes db6c0194
+ 00bfcf3c bytes d16c0194
- 00bfcae8 ["INT_ADD", "register:40f0:8", ["const:bfcae8:8", "const:4:8"]]
- 00bfcae8 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfcf10 ["INT_ADD", "register:40f0:8", ["const:bfcf10:8", "const:4:8"]]
+ 00bfcf10 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfcae8 bytes ba730194
+ 00bfcf10 bytes b0730194
- 00bfcb04 ["INT_ADD", "register:40f0:8", ["const:bfcb04:8", "const:4:8"]]
- 00bfcb04 ["CALL", null, ["callee:00c58270:8"]]
+ 00bfcf2c ["INT_ADD", "register:40f0:8", ["const:bfcf2c:8", "const:4:8"]]
+ 00bfcf2c ["CALL", null, ["callee:00c58270:8"]]
- 00bfcb04 bytes db6c0194
+ 00bfcf2c bytes d16c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20a6661b477b572dc9e1bd197e45847e"></a>

### [`00bfcbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcbf4.md) → [`00bfd01c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd01c.md) FUN_00bfd01c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfcbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcbec.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfd014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd014.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfd070",
      "incomplete_value": true,
      "site": "00bfd074",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfcc48",
      "incomplete_value": true,
      "site": "00bfcc4c",
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
                "const:710:8"
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
      "00bfd070",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd070",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfd070",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd070",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfcc4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcbf4.md#insn-00bfcc4c) · [`00bfcc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcbf4.md#insn-00bfcc20) · [`00bfcc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcbf4.md#insn-00bfcc3c)
- 新版 `00bfd074`（命令位置の公開資料なし） · `00bfd048`（命令位置の公開資料なし） · `00bfd064`（命令位置の公開資料なし）

~~~diff
- 00bfcc4c ["INT_ADD", "register:40f0:8", ["const:bfcc4c:8", "const:4:8"]]
- 00bfcc4c ["CALL", null, ["callee:00c58280:8"]]
+ 00bfd074 ["INT_ADD", "register:40f0:8", ["const:bfd074:8", "const:4:8"]]
+ 00bfd074 ["CALL", null, ["callee:00c58280:8"]]
- 00bfcc4c bytes 8d6c0194
+ 00bfd074 bytes 836c0194
- 00bfcc20 ["INT_ADD", "register:40f0:8", ["const:bfcc20:8", "const:4:8"]]
- 00bfcc20 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfd048 ["INT_ADD", "register:40f0:8", ["const:bfd048:8", "const:4:8"]]
+ 00bfd048 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfcc20 bytes 6c730194
+ 00bfd048 bytes 62730194
- 00bfcc3c ["INT_ADD", "register:40f0:8", ["const:bfcc3c:8", "const:4:8"]]
- 00bfcc3c ["CALL", null, ["callee:00c58270:8"]]
+ 00bfd064 ["INT_ADD", "register:40f0:8", ["const:bfd064:8", "const:4:8"]]
+ 00bfd064 ["CALL", null, ["callee:00c58270:8"]]
- 00bfcc3c bytes 8d6c0194
+ 00bfd064 bytes 836c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c88b2da7694fb5470aacba8fcddbf84"></a>

### [`00bfcd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcd2c.md) → [`00bfd154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd154.md) FUN_00bfd154

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfcd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcd24.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfd14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd14c.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfd1a8",
      "incomplete_value": true,
      "site": "00bfd1ac",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfcd80",
      "incomplete_value": true,
      "site": "00bfcd84",
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
                "const:710:8"
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
      "00bfd1a8",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd1a8",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfd1a8",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd1a8",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfcd84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcd2c.md#insn-00bfcd84) · [`00bfcd58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcd2c.md#insn-00bfcd58) · [`00bfcd74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcd2c.md#insn-00bfcd74)
- 新版 `00bfd1ac`（命令位置の公開資料なし） · `00bfd180`（命令位置の公開資料なし） · `00bfd19c`（命令位置の公開資料なし）

~~~diff
- 00bfcd84 ["INT_ADD", "register:40f0:8", ["const:bfcd84:8", "const:4:8"]]
- 00bfcd84 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfd1ac ["INT_ADD", "register:40f0:8", ["const:bfd1ac:8", "const:4:8"]]
+ 00bfd1ac ["CALL", null, ["callee:00c58280:8"]]
- 00bfcd84 bytes 3f6c0194
+ 00bfd1ac bytes 356c0194
- 00bfcd58 ["INT_ADD", "register:40f0:8", ["const:bfcd58:8", "const:4:8"]]
- 00bfcd58 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfd180 ["INT_ADD", "register:40f0:8", ["const:bfd180:8", "const:4:8"]]
+ 00bfd180 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfcd58 bytes 1e730194
+ 00bfd180 bytes 14730194
- 00bfcd74 ["INT_ADD", "register:40f0:8", ["const:bfcd74:8", "const:4:8"]]
- 00bfcd74 ["CALL", null, ["callee:00c58270:8"]]
+ 00bfd19c ["INT_ADD", "register:40f0:8", ["const:bfd19c:8", "const:4:8"]]
+ 00bfd19c ["CALL", null, ["callee:00c58270:8"]]
- 00bfcd74 bytes 3f6c0194
+ 00bfd19c bytes 356c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29bb57368057d085ba061175f3504e6e"></a>

### [`00bfce64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfce64.md) → [`00bfd28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd28c.md) FUN_00bfd28c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfce5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfce5c.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfd284`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd284.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfd2e0",
      "incomplete_value": true,
      "site": "00bfd2e4",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfceb8",
      "incomplete_value": true,
      "site": "00bfcebc",
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
                "const:710:8"
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
      "00bfd2e0",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd2e0",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfd2e0",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd2e0",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfcebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfce64.md#insn-00bfcebc) · [`00bfce90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfce64.md#insn-00bfce90) · [`00bfceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfce64.md#insn-00bfceac)
- 新版 `00bfd2e4`（命令位置の公開資料なし） · `00bfd2b8`（命令位置の公開資料なし） · `00bfd2d4`（命令位置の公開資料なし）

~~~diff
- 00bfcebc ["INT_ADD", "register:40f0:8", ["const:bfcebc:8", "const:4:8"]]
- 00bfcebc ["CALL", null, ["callee:00c58280:8"]]
+ 00bfd2e4 ["INT_ADD", "register:40f0:8", ["const:bfd2e4:8", "const:4:8"]]
+ 00bfd2e4 ["CALL", null, ["callee:00c58280:8"]]
- 00bfcebc bytes f16b0194
+ 00bfd2e4 bytes e76b0194
- 00bfce90 ["INT_ADD", "register:40f0:8", ["const:bfce90:8", "const:4:8"]]
- 00bfce90 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfd2b8 ["INT_ADD", "register:40f0:8", ["const:bfd2b8:8", "const:4:8"]]
+ 00bfd2b8 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfce90 bytes d0720194
+ 00bfd2b8 bytes c6720194
- 00bfceac ["INT_ADD", "register:40f0:8", ["const:bfceac:8", "const:4:8"]]
- 00bfceac ["CALL", null, ["callee:00c58270:8"]]
+ 00bfd2d4 ["INT_ADD", "register:40f0:8", ["const:bfd2d4:8", "const:4:8"]]
+ 00bfd2d4 ["CALL", null, ["callee:00c58270:8"]]
- 00bfceac bytes f16b0194
+ 00bfd2d4 bytes e76b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe661250ec935fcbf15927b9aa25b3ae"></a>

### [`00bfcf9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcf9c.md) → [`00bfd3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd3c4.md) FUN_00bfd3c4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfcf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcf94.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfd3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd3bc.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfd418",
      "incomplete_value": true,
      "site": "00bfd41c",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfcff0",
      "incomplete_value": true,
      "site": "00bfcff4",
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
                "const:710:8"
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
      "00bfd418",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd418",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfd418",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd418",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfcff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcf9c.md#insn-00bfcff4) · [`00bfcfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcf9c.md#insn-00bfcfc8) · [`00bfcfe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcf9c.md#insn-00bfcfe4)
- 新版 `00bfd41c`（命令位置の公開資料なし） · `00bfd3f0`（命令位置の公開資料なし） · `00bfd40c`（命令位置の公開資料なし）

~~~diff
- 00bfcff4 ["INT_ADD", "register:40f0:8", ["const:bfcff4:8", "const:4:8"]]
- 00bfcff4 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfd41c ["INT_ADD", "register:40f0:8", ["const:bfd41c:8", "const:4:8"]]
+ 00bfd41c ["CALL", null, ["callee:00c58280:8"]]
- 00bfcff4 bytes a36b0194
+ 00bfd41c bytes 996b0194
- 00bfcfc8 ["INT_ADD", "register:40f0:8", ["const:bfcfc8:8", "const:4:8"]]
- 00bfcfc8 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfd3f0 ["INT_ADD", "register:40f0:8", ["const:bfd3f0:8", "const:4:8"]]
+ 00bfd3f0 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfcfc8 bytes 82720194
+ 00bfd3f0 bytes 78720194
- 00bfcfe4 ["INT_ADD", "register:40f0:8", ["const:bfcfe4:8", "const:4:8"]]
- 00bfcfe4 ["CALL", null, ["callee:00c58270:8"]]
+ 00bfd40c ["INT_ADD", "register:40f0:8", ["const:bfd40c:8", "const:4:8"]]
+ 00bfd40c ["CALL", null, ["callee:00c58270:8"]]
- 00bfcfe4 bytes a36b0194
+ 00bfd40c bytes 996b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea26d83621cfa2ca42564d6aa46425e6"></a>

### [`00bfd0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd0d4.md) → [`00bfd4fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd4fc.md) FUN_00bfd4fc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bfd0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd0cc.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)
- 新版 呼出元 1件 [`00bfd4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd4f4.md) · 呼出先 5件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c582a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582a0.md) [`00c59dd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59dd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfd550",
      "incomplete_value": true,
      "site": "00bfd554",
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bfd128",
      "incomplete_value": true,
      "site": "00bfd12c",
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
                "const:710:8"
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
      "00bfd550",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd550",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfd550",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd550",
      "PARAM",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfd12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd0d4.md#insn-00bfd12c) · [`00bfd100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd0d4.md#insn-00bfd100) · [`00bfd11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd0d4.md#insn-00bfd11c)
- 新版 `00bfd554`（命令位置の公開資料なし） · `00bfd528`（命令位置の公開資料なし） · `00bfd544`（命令位置の公開資料なし）

~~~diff
- 00bfd12c ["INT_ADD", "register:40f0:8", ["const:bfd12c:8", "const:4:8"]]
- 00bfd12c ["CALL", null, ["callee:00c58280:8"]]
+ 00bfd554 ["INT_ADD", "register:40f0:8", ["const:bfd554:8", "const:4:8"]]
+ 00bfd554 ["CALL", null, ["callee:00c58280:8"]]
- 00bfd12c bytes 556b0194
+ 00bfd554 bytes 4b6b0194
- 00bfd100 ["INT_ADD", "register:40f0:8", ["const:bfd100:8", "const:4:8"]]
- 00bfd100 ["CALL", null, ["callee:00c59dd0:8"]]
+ 00bfd528 ["INT_ADD", "register:40f0:8", ["const:bfd528:8", "const:4:8"]]
+ 00bfd528 ["CALL", null, ["callee:00c59dd0:8"]]
- 00bfd100 bytes 34720194
+ 00bfd528 bytes 2a720194
- 00bfd11c ["INT_ADD", "register:40f0:8", ["const:bfd11c:8", "const:4:8"]]
- 00bfd11c ["CALL", null, ["callee:00c58270:8"]]
+ 00bfd544 ["INT_ADD", "register:40f0:8", ["const:bfd544:8", "const:4:8"]]
+ 00bfd544 ["CALL", null, ["callee:00c58270:8"]]
- 00bfd11c bytes 556b0194
+ 00bfd544 bytes 4b6b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e9a271205462472dfc9322fc2043f2c"></a>

### [`00bfd358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd358.md) → [`00bfd780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd780.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPcl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5e370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e370.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfd7c0",
      "incomplete_value": true,
      "site": "00bfd7c4",
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
      "definition_site": "00bfd398",
      "incomplete_value": true,
      "site": "00bfd39c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfd7c0",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd7c0",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfd7c0",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd7c0",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfd39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd358.md#insn-00bfd39c) · [`00bfd38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd358.md#insn-00bfd38c) · [`00bfd398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd358.md#insn-00bfd398)
- 新版 `00bfd7c4`（命令位置の公開資料なし） · `00bfd7b4`（命令位置の公開資料なし） · `00bfd7c0`（命令位置の公開資料なし）

~~~diff
- 00bfd39c ["INT_ADD", "register:40f0:8", ["const:bfd39c:8", "const:4:8"]]
- 00bfd39c ["CALL", null, ["callee:00c58280:8"]]
+ 00bfd7c4 ["INT_ADD", "register:40f0:8", ["const:bfd7c4:8", "const:4:8"]]
+ 00bfd7c4 ["CALL", null, ["callee:00c58280:8"]]
- 00bfd39c bytes b96a0194
+ 00bfd7c4 bytes af6a0194
- 00bfd38c ["INT_ADD", "register:40f0:8", ["const:bfd38c:8", "const:4:8"]]
- 00bfd38c ["CALL", null, ["callee:00c58270:8"]]
+ 00bfd7b4 ["INT_ADD", "register:40f0:8", ["const:bfd7b4:8", "const:4:8"]]
+ 00bfd7b4 ["CALL", null, ["callee:00c58270:8"]]
- 00bfd38c bytes b96a0194
+ 00bfd7b4 bytes af6a0194
- 00bfd398 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:830:8"]]
- 00bfd398 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfd7c0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:c30:8"]]
+ 00bfd7c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfd398 bytes 211844f9
+ 00bfd7c0 bytes 211846f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da021da22f17cd095e50c82bab0609b3"></a>

### [`00bfd5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd5d0.md) → [`00bfd9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd9f8.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5df80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5e380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e380.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfda30",
      "incomplete_value": true,
      "site": "00bfda34",
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
      "definition_site": "00bfd608",
      "incomplete_value": true,
      "site": "00bfd60c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfda30",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00bfda30",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfda30",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00bfda30",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfd60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd5d0.md#insn-00bfd60c) · [`00bfd5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd5d0.md#insn-00bfd5fc) · [`00bfd608`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd5d0.md#insn-00bfd608)
- 新版 `00bfda34`（命令位置の公開資料なし） · `00bfda24`（命令位置の公開資料なし） · `00bfda30`（命令位置の公開資料なし）

~~~diff
- 00bfd60c ["INT_ADD", "register:40f0:8", ["const:bfd60c:8", "const:4:8"]]
- 00bfd60c ["CALL", null, ["callee:00c58280:8"]]
+ 00bfda34 ["INT_ADD", "register:40f0:8", ["const:bfda34:8", "const:4:8"]]
+ 00bfda34 ["CALL", null, ["callee:00c58280:8"]]
- 00bfd60c bytes 1d6a0194
+ 00bfda34 bytes 136a0194
- 00bfd5fc ["INT_ADD", "register:40f0:8", ["const:bfd5fc:8", "const:4:8"]]
- 00bfd5fc ["CALL", null, ["callee:00c58270:8"]]
+ 00bfda24 ["INT_ADD", "register:40f0:8", ["const:bfda24:8", "const:4:8"]]
+ 00bfda24 ["CALL", null, ["callee:00c58270:8"]]
- 00bfd5fc bytes 1d6a0194
+ 00bfda24 bytes 136a0194
- 00bfd608 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:830:8"]]
- 00bfd608 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfda30 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:c30:8"]]
+ 00bfda30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfd608 bytes 211844f9
+ 00bfda30 bytes 211846f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82819b04d7b72f42f48a524212f61790"></a>

### [`00bfd7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd7d4.md) → [`00bfdbfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdbfc.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5df90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md) [`00c58280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58280.md) [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) [`00c5e390`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfdc3c",
      "incomplete_value": true,
      "site": "00bfdc40",
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
      "definition_site": "00bfd814",
      "incomplete_value": true,
      "site": "00bfd818",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfdc3c",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00bfdc3c",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfdc3c",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00bfdc3c",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bfd818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd7d4.md#insn-00bfd818) · [`00bfd808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd7d4.md#insn-00bfd808) · [`00bfd814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd7d4.md#insn-00bfd814)
- 新版 `00bfdc40`（命令位置の公開資料なし） · `00bfdc30`（命令位置の公開資料なし） · `00bfdc3c`（命令位置の公開資料なし）

~~~diff
- 00bfd818 ["INT_ADD", "register:40f0:8", ["const:bfd818:8", "const:4:8"]]
- 00bfd818 ["CALL", null, ["callee:00c58280:8"]]
+ 00bfdc40 ["INT_ADD", "register:40f0:8", ["const:bfdc40:8", "const:4:8"]]
+ 00bfdc40 ["CALL", null, ["callee:00c58280:8"]]
- 00bfd818 bytes 9a690194
+ 00bfdc40 bytes 90690194
- 00bfd808 ["INT_ADD", "register:40f0:8", ["const:bfd808:8", "const:4:8"]]
- 00bfd808 ["CALL", null, ["callee:00c58270:8"]]
+ 00bfdc30 ["INT_ADD", "register:40f0:8", ["const:bfdc30:8", "const:4:8"]]
+ 00bfdc30 ["CALL", null, ["callee:00c58270:8"]]
- 00bfd808 bytes 9a690194
+ 00bfdc30 bytes 90690194
- 00bfd814 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:830:8"]]
- 00bfd814 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfdc3c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:c30:8"]]
+ 00bfdc3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bfd814 bytes 211844f9
+ 00bfdc3c bytes 211846f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

