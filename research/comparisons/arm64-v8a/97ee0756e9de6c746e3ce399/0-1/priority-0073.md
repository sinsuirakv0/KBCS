# v15.7.2 → v15.7.3 · 最優先の変更候補 (73)

[一覧の目次](README.md)

<a id="compare-e2b5cf4cdc207778bffced25570e497a"></a>

### [`00b6ab00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ab00.md) → [`00b6abc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6abc8.md) _ZN8firebase4auth22GameCenterAuthProvider23GetCredentialLastResultEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00848b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00848/00848b34.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00848b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848b34.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ac38",
      "incomplete_value": true,
      "site": "00b6ac40",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 6,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ab78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ab00.md#insn-00b6ab78) · [`00b6ab24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ab00.md#insn-00b6ab24) · [`00b6ab34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ab00.md#insn-00b6ab34)
- 新版 [`00b6ac40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6abc8.md#insn-00b6ac40) · [`00b6abec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6abc8.md#insn-00b6abec) · [`00b6abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6abc8.md#insn-00b6abfc)

~~~diff
- 00b6ab78 ["INT_ADD", "register:40f0:8", ["const:b6ab78:8", "const:4:8"]]
- 00b6ab78 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b6ac40 ["INT_ADD", "register:40f0:8", ["const:b6ac40:8", "const:4:8"]]
+ 00b6ac40 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b6ab78 bytes 66cc0194
+ 00b6ac40 bytes 60cc0194
- 00b6ab24 ["INT_ADD", "register:40f0:8", ["const:b6ab24:8", "const:4:8"]]
- 00b6ab24 ["CALL", null, ["callee:00be0b00:8"]]
+ 00b6abec ["INT_ADD", "register:40f0:8", ["const:b6abec:8", "const:4:8"]]
+ 00b6abec ["CALL", null, ["callee:00be0b00:8"]]
- 00b6ab24 bytes cbd70194
+ 00b6abec bytes c5d70194
- 00b6ab34 ["INT_ADD", "register:40f0:8", ["const:b6ab34:8", "const:4:8"]]
- 00b6ab34 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b6abfc ["INT_ADD", "register:40f0:8", ["const:b6abfc:8", "const:4:8"]]
+ 00b6abfc ["CALL", null, ["callee:00bddbd0:8"]]
- 00b6ab34 bytes fbcb0194
+ 00b6abfc bytes f5cb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-373a0d71ae47290e750a11d0a6e3aca6"></a>

### [`00b6ac24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ac24.md) → [`00b6acec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6acec.md) _ZN8firebase4auth22GameCenterAuthProvider21IsPlayerAuthenticatedEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6acf8",
      "incomplete_value": false,
      "site": "00b6acfc",
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
            "const:fef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ac30",
      "incomplete_value": false,
      "site": "00b6ac34",
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
            "const:ff6:8"
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
      "00b6acf8",
      "PARAM",
      [
        "storage",
        "002a3ff6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6acf8",
      "PARAM",
      [
        "storage",
        "002a3fef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ac34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ac24.md#insn-00b6ac34) · [`00b6ac30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ac24.md#insn-00b6ac30)
- 新版 [`00b6acfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6acec.md#insn-00b6acfc) · [`00b6acf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6acec.md#insn-00b6acf8)

~~~diff
- 00b6ac34 ["INT_ADD", "register:40f0:8", ["const:b6ac34:8", "const:4:8"]]
- 00b6ac34 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6acfc ["INT_ADD", "register:40f0:8", ["const:b6acfc:8", "const:4:8"]]
+ 00b6acfc ["CALL", null, ["callee:00bde130:8"]]
- 00b6ac34 bytes 13cd0194
+ 00b6acfc bytes 0dcd0194
- 00b6ac30 ["COPY", "tmp:0:8", ["const:ff6:8"]]
- 00b6ac30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ac30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ac30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6acf8 ["COPY", "tmp:0:8", ["const:fef:8"]]
+ 00b6acf8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6acf8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6acf8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6ac30 bytes 00d83f91
+ 00b6acf8 bytes 00bc3f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fa9daa24745795875ce8fb10e3cc0fb"></a>

### [`00b6ac70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ac70.md) → [`00b6ad38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad38.md) _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ad64",
      "incomplete_value": false,
      "site": "00b6ad68",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ac9c",
      "incomplete_value": false,
      "site": "00b6aca0",
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
            "const:dbf:8"
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
      "00b6ad64",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6ad64",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6aca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ac70.md#insn-00b6aca0) · [`00b6ac8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ac70.md#insn-00b6ac8c) · [`00b6ac9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ac70.md#insn-00b6ac9c)
- 新版 [`00b6ad68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad38.md#insn-00b6ad68) · [`00b6ad54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad38.md#insn-00b6ad54) · [`00b6ad64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6ad38.md#insn-00b6ad64)

~~~diff
- 00b6aca0 ["INT_ADD", "register:40f0:8", ["const:b6aca0:8", "const:4:8"]]
- 00b6aca0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6ad68 ["INT_ADD", "register:40f0:8", ["const:b6ad68:8", "const:4:8"]]
+ 00b6ad68 ["CALL", null, ["callee:00bde130:8"]]
- 00b6aca0 bytes f8cc0194
+ 00b6ad68 bytes f2cc0194
- 00b6ac8c ["INT_ADD", "register:40f0:8", ["const:b6ac8c:8", "const:4:8"]]
- 00b6ac8c ["CALL", null, ["callee:00bde390:8"]]
+ 00b6ad54 ["INT_ADD", "register:40f0:8", ["const:b6ad54:8", "const:4:8"]]
+ 00b6ad54 ["CALL", null, ["callee:00bde390:8"]]
- 00b6ac8c bytes 95cd0194
+ 00b6ad54 bytes 8fcd0194
- 00b6ac9c ["COPY", "tmp:0:8", ["const:dbf:8"]]
- 00b6ac9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ac9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ac9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6ad64 ["COPY", "tmp:0:8", ["const:e4c:8"]]
+ 00b6ad64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6ad64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6ad64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6ac9c bytes 00fc3691
+ 00b6ad64 bytes 00303991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98e9c4f2f5e485c6ff2e29b1bb47d532"></a>

### [`00b6ad14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ad14.md) → [`00b6addc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6addc.md) _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d40.md) · 呼出先 3件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 1件 [`00be0df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0df0.md) · 呼出先 3件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ae0c",
      "incomplete_value": false,
      "site": "00b6ae10",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ad44",
      "incomplete_value": false,
      "site": "00b6ad48",
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
            "const:dbf:8"
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
      "definition_site": "00b6ae40",
      "incomplete_value": false,
      "site": "00b6ae44",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ad78",
      "incomplete_value": false,
      "site": "00b6ad7c",
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
            "const:dbf:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6ae0c",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ],
    [
      "00b6ae40",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6ae0c",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ],
    [
      "00b6ae40",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ad48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ad14.md#insn-00b6ad48) · [`00b6ad7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ad14.md#insn-00b6ad7c) · [`00b6ad34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ad14.md#insn-00b6ad34)
- 新版 [`00b6ae10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6addc.md#insn-00b6ae10) · [`00b6ae44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6addc.md#insn-00b6ae44) · [`00b6adfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6addc.md#insn-00b6adfc)

~~~diff
- 00b6ad48 ["INT_ADD", "register:40f0:8", ["const:b6ad48:8", "const:4:8"]]
- 00b6ad48 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6ae10 ["INT_ADD", "register:40f0:8", ["const:b6ae10:8", "const:4:8"]]
+ 00b6ae10 ["CALL", null, ["callee:00bde130:8"]]
- 00b6ad48 bytes cecc0194
+ 00b6ae10 bytes c8cc0194
- 00b6ad7c ["INT_ADD", "register:40f0:8", ["const:b6ad7c:8", "const:4:8"]]
- 00b6ad7c ["CALL", null, ["callee:00bde130:8"]]
+ 00b6ae44 ["INT_ADD", "register:40f0:8", ["const:b6ae44:8", "const:4:8"]]
+ 00b6ae44 ["CALL", null, ["callee:00bde130:8"]]
- 00b6ad7c bytes c1cc0194
+ 00b6ae44 bytes bbcc0194
- 00b6ad34 ["INT_ADD", "register:40f0:8", ["const:b6ad34:8", "const:4:8"]]
- 00b6ad34 ["CALL", null, ["callee:00bde390:8"]]
+ 00b6adfc ["INT_ADD", "register:40f0:8", ["const:b6adfc:8", "const:4:8"]]
+ 00b6adfc ["CALL", null, ["callee:00bde390:8"]]
- 00b6ad34 bytes 6bcd0194
+ 00b6adfc bytes 65cd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92aa13a19fcd44ce2fb33d0c76d20bc7"></a>

### [`00b6ade8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ade8.md) → [`00b6aeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aeb0.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokeneqERKS2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6aed8",
      "incomplete_value": false,
      "site": "00b6aedc",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ae10",
      "incomplete_value": false,
      "site": "00b6ae14",
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
            "const:dbf:8"
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
      "00b6aed8",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6aed8",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ae14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ade8.md#insn-00b6ae14) · [`00b6ae00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ade8.md#insn-00b6ae00) · [`00b6ae10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ade8.md#insn-00b6ae10)
- 新版 [`00b6aedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aeb0.md#insn-00b6aedc) · [`00b6aec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aeb0.md#insn-00b6aec8) · [`00b6aed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6aeb0.md#insn-00b6aed8)

~~~diff
- 00b6ae14 ["INT_ADD", "register:40f0:8", ["const:b6ae14:8", "const:4:8"]]
- 00b6ae14 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6aedc ["INT_ADD", "register:40f0:8", ["const:b6aedc:8", "const:4:8"]]
+ 00b6aedc ["CALL", null, ["callee:00bde130:8"]]
- 00b6ae14 bytes 9bcc0194
+ 00b6aedc bytes 95cc0194
- 00b6ae00 ["INT_ADD", "register:40f0:8", ["const:b6ae00:8", "const:4:8"]]
- 00b6ae00 ["CALL", null, ["callee:00bde390:8"]]
+ 00b6aec8 ["INT_ADD", "register:40f0:8", ["const:b6aec8:8", "const:4:8"]]
+ 00b6aec8 ["CALL", null, ["callee:00bde390:8"]]
- 00b6ae00 bytes 38cd0194
+ 00b6aec8 bytes 32cd0194
- 00b6ae10 ["COPY", "tmp:0:8", ["const:dbf:8"]]
- 00b6ae10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ae10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ae10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6aed8 ["COPY", "tmp:0:8", ["const:e4c:8"]]
+ 00b6aed8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6aed8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6aed8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6ae10 bytes 00fc3691
+ 00b6aed8 bytes 00303991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a74c41bb50f010ffd8177018c25946a"></a>

### [`00b6ae54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ae54.md) → [`00b6af1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af1c.md) _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokenneERKS2_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6af44",
      "incomplete_value": false,
      "site": "00b6af48",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ae7c",
      "incomplete_value": false,
      "site": "00b6ae80",
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
            "const:dbf:8"
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
      "00b6af44",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6af44",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ae80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ae54.md#insn-00b6ae80) · [`00b6ae6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ae54.md#insn-00b6ae6c) · [`00b6ae7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ae54.md#insn-00b6ae7c)
- 新版 [`00b6af48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af1c.md#insn-00b6af48) · [`00b6af34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af1c.md#insn-00b6af34) · [`00b6af44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af1c.md#insn-00b6af44)

~~~diff
- 00b6ae80 ["INT_ADD", "register:40f0:8", ["const:b6ae80:8", "const:4:8"]]
- 00b6ae80 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6af48 ["INT_ADD", "register:40f0:8", ["const:b6af48:8", "const:4:8"]]
+ 00b6af48 ["CALL", null, ["callee:00bde130:8"]]
- 00b6ae80 bytes 80cc0194
+ 00b6af48 bytes 7acc0194
- 00b6ae6c ["INT_ADD", "register:40f0:8", ["const:b6ae6c:8", "const:4:8"]]
- 00b6ae6c ["CALL", null, ["callee:00bde390:8"]]
+ 00b6af34 ["INT_ADD", "register:40f0:8", ["const:b6af34:8", "const:4:8"]]
+ 00b6af34 ["CALL", null, ["callee:00bde390:8"]]
- 00b6ae6c bytes 1dcd0194
+ 00b6af34 bytes 17cd0194
- 00b6ae7c ["COPY", "tmp:0:8", ["const:dbf:8"]]
- 00b6ae7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ae7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6ae7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6af44 ["COPY", "tmp:0:8", ["const:e4c:8"]]
+ 00b6af44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6af44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6af44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6ae7c bytes 00fc3691
+ 00b6af44 bytes 00303991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a66c38ed7c8a493084d611c385173562"></a>

### [`00b6aec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6aec8.md) → [`00b6af90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af90.md) _ZN8firebase4auth17PhoneAuthProviderD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be08c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be08c0.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 1件 [`00be0970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0970.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6afb8",
      "incomplete_value": false,
      "site": "00b6afbc",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6aef0",
      "incomplete_value": false,
      "site": "00b6aef4",
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
            "const:dbf:8"
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
      "00b6afb8",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6afb8",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6aef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6aec8.md#insn-00b6aef4) · [`00b6aee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6aec8.md#insn-00b6aee0) · [`00b6aef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6aec8.md#insn-00b6aef0)
- 新版 [`00b6afbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af90.md#insn-00b6afbc) · [`00b6afa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af90.md#insn-00b6afa8) · [`00b6afb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6a/00b6af90.md#insn-00b6afb8)

~~~diff
- 00b6aef4 ["INT_ADD", "register:40f0:8", ["const:b6aef4:8", "const:4:8"]]
- 00b6aef4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6afbc ["INT_ADD", "register:40f0:8", ["const:b6afbc:8", "const:4:8"]]
+ 00b6afbc ["CALL", null, ["callee:00bde130:8"]]
- 00b6aef4 bytes 63cc0194
+ 00b6afbc bytes 5dcc0194
- 00b6aee0 ["INT_ADD", "register:40f0:8", ["const:b6aee0:8", "const:4:8"]]
- 00b6aee0 ["CALL", null, ["callee:00bde390:8"]]
+ 00b6afa8 ["INT_ADD", "register:40f0:8", ["const:b6afa8:8", "const:4:8"]]
+ 00b6afa8 ["CALL", null, ["callee:00bde390:8"]]
- 00b6aee0 bytes 00cd0194
+ 00b6afa8 bytes facc0194
- 00b6aef0 ["COPY", "tmp:0:8", ["const:dbf:8"]]
- 00b6aef0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6aef0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6aef0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6afb8 ["COPY", "tmp:0:8", ["const:e4c:8"]]
+ 00b6afb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6afb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6afb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6aef0 bytes 00fc3691
+ 00b6afb8 bytes 00303991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6d43c3da23ff98f21759ed06111789e"></a>

### [`00b6af38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6af38.md) → [`00b6b000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b000.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerC2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6b018",
      "incomplete_value": true,
      "site": "00b6b01c",
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
      "definition_site": "00b6af50",
      "incomplete_value": true,
      "site": "00b6af54",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b040",
      "incomplete_value": false,
      "site": "00b6b044",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6af78",
      "incomplete_value": false,
      "site": "00b6af7c",
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
            "const:dbf:8"
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
    "new": {
      "definition_site": "00b6b058",
      "incomplete_value": true,
      "site": "00b6b068",
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
                "const:968:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6af90",
      "incomplete_value": true,
      "site": "00b6afa0",
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
                "const:8a8:8"
              ]
            ]
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
      "00b6b010",
      "READ",
      [
        "storage",
        "00c1bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00b6b01c",
      "DATA",
      [
        "storage",
        "00c12698",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00b6b040",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6b010",
      "READ",
      [
        "storage",
        "00c1bbc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b6b01c",
      "DATA",
      [
        "storage",
        "00c12748",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00b6b040",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6af7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6af38.md#insn-00b6af7c) · [`00b6afa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6af38.md#insn-00b6afa0) · [`00b6af48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6af38.md#insn-00b6af48)
- 新版 [`00b6b044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b000.md#insn-00b6b044) · [`00b6b068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b000.md#insn-00b6b068) · [`00b6b010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b000.md#insn-00b6b010)

~~~diff
- 00b6af7c ["INT_ADD", "register:40f0:8", ["const:b6af7c:8", "const:4:8"]]
- 00b6af7c ["CALL", null, ["callee:00bde130:8"]]
+ 00b6b044 ["INT_ADD", "register:40f0:8", ["const:b6b044:8", "const:4:8"]]
+ 00b6b044 ["CALL", null, ["callee:00bde130:8"]]
- 00b6af7c bytes 41cc0194
+ 00b6b044 bytes 3bcc0194
- 00b6afa0 ["INT_ADD", "register:40f0:8", ["const:b6afa0:8", "const:4:8"]]
- 00b6afa0 ["CALL", null, ["callee:0056681c:8"]]
+ 00b6b068 ["INT_ADD", "register:40f0:8", ["const:b6b068:8", "const:4:8"]]
+ 00b6b068 ["CALL", null, ["callee:0056681c:8"]]
- 00b6afa0 bytes 1feee797
+ 00b6b068 bytes edede797
- 00b6af48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b10:8"]]
- 00b6af48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6b010 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bc0:8"]]
+ 00b6b010 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6af48 bytes 088945f9
+ 00b6b010 bytes 08e145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94472ea2a0c8b8aa8c2a5647d07f8c59"></a>

### [`00b6afcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6afcc.md) → [`00b6b094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b094.md) _ZN8firebase4auth17PhoneAuthProvider8ListenerD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6b0ac",
      "incomplete_value": true,
      "site": "00b6b0b0",
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
      "definition_site": "00b6afe4",
      "incomplete_value": true,
      "site": "00b6afe8",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b0c4",
      "incomplete_value": false,
      "site": "00b6b0c8",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6affc",
      "incomplete_value": false,
      "site": "00b6b000",
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
            "const:dbf:8"
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
      "definition_site": "00b6b0dc",
      "incomplete_value": true,
      "site": "00b6b0e8",
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
                "const:980:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b014",
      "incomplete_value": true,
      "site": "00b6b020",
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
                "const:8c0:8"
              ]
            ]
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
      "00b6b0a4",
      "READ",
      [
        "storage",
        "00c1bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00b6b0b0",
      "DATA",
      [
        "storage",
        "00c12698",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00b6b0c4",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6b0a4",
      "READ",
      [
        "storage",
        "00c1bbc0",
        null,
        "pointer"
      ]
    ],
    [
      "00b6b0b0",
      "DATA",
      [
        "storage",
        "00c12748",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00b6b0c4",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6afcc.md#insn-00b6b000) · [`00b6b020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6afcc.md#insn-00b6b020) · [`00b6afdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6afcc.md#insn-00b6afdc)
- 新版 [`00b6b0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b094.md#insn-00b6b0c8) · [`00b6b0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b094.md#insn-00b6b0e8) · [`00b6b0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b094.md#insn-00b6b0a4)

~~~diff
- 00b6b000 ["INT_ADD", "register:40f0:8", ["const:b6b000:8", "const:4:8"]]
- 00b6b000 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6b0c8 ["INT_ADD", "register:40f0:8", ["const:b6b0c8:8", "const:4:8"]]
+ 00b6b0c8 ["CALL", null, ["callee:00bde130:8"]]
- 00b6b000 bytes 20cc0194
+ 00b6b0c8 bytes 1acc0194
- 00b6b020 ["INT_ADD", "register:40f0:8", ["const:b6b020:8", "const:4:8"]]
- 00b6b020 ["CALL", null, ["callee:00551e14:8"]]
+ 00b6b0e8 ["INT_ADD", "register:40f0:8", ["const:b6b0e8:8", "const:4:8"]]
+ 00b6b0e8 ["CALL", null, ["callee:00551e14:8"]]
- 00b6b020 bytes 7d9be797
+ 00b6b0e8 bytes 4b9be797
- 00b6afdc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b10:8"]]
- 00b6afdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6b0a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bc0:8"]]
+ 00b6b0a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6afdc bytes 088945f9
+ 00b6b0a4 bytes 08e145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-612a2d0e8679db6a91928fd43488458a"></a>

### [`00b6b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b064.md) → [`00b6b12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b12c.md) _ZN8firebase4auth17PhoneAuthProvider17VerifyPhoneNumberERKNS0_16PhoneAuthOptionsEPNS1_8ListenerE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件

アドレスに依存する影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b198",
      "incomplete_value": true,
      "site": "00b6b1b0",
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b0d0",
      "incomplete_value": true,
      "site": "00b6b0e8",
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
                "const:770:8"
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
      "definition_site": "00b6b1a4",
      "incomplete_value": true,
      "site": "00b6b1b0",
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
                "const:840:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b0dc",
      "incomplete_value": true,
      "site": "00b6b0e8",
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
                "const:780:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b1c8",
      "incomplete_value": false,
      "site": "00b6b1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:5b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b100",
      "incomplete_value": false,
      "site": "00b6b108",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "00b6b198",
      "READ",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b1a4",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b1c8",
      "PARAM",
      [
        "storage",
        "002ad5c0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6b198",
      "READ",
      [
        "storage",
        "010a1830",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b1a4",
      "READ",
      [
        "storage",
        "010a1840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b1c8",
      "PARAM",
      [
        "storage",
        "002ad5b7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b064.md#insn-00b6b0e8) · [`00b6b108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b064.md#insn-00b6b108) · [`00b6b140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b064.md#insn-00b6b140)
- 新版 [`00b6b1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b12c.md#insn-00b6b1b0) · [`00b6b1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b12c.md#insn-00b6b1d0) · [`00b6b208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b12c.md#insn-00b6b208)

~~~diff
- 00b6b0e8 ["INT_ADD", "register:40f0:8", ["const:b6b0e8:8", "const:4:8"]]
- 00b6b0e8 ["CALL", null, ["callee:0056681c:8"]]
+ 00b6b1b0 ["INT_ADD", "register:40f0:8", ["const:b6b1b0:8", "const:4:8"]]
+ 00b6b1b0 ["CALL", null, ["callee:0056681c:8"]]
- 00b6b0e8 bytes cdede797
+ 00b6b1b0 bytes 9bede797
- 00b6b108 ["INT_ADD", "register:40f0:8", ["const:b6b108:8", "const:4:8"]]
- 00b6b108 ["CALL", null, ["callee:00bde6f0:8"]]
+ 00b6b1d0 ["INT_ADD", "register:40f0:8", ["const:b6b1d0:8", "const:4:8"]]
+ 00b6b1d0 ["CALL", null, ["callee:00bde6f0:8"]]
- 00b6b108 bytes 4ecd0194
+ 00b6b1d0 bytes 48cd0194
- 00b6b140 ["INT_ADD", "register:40f0:8", ["const:b6b140:8", "const:4:8"]]
- 00b6b140 ["CALL", null, ["callee:00bde6f0:8"]]
+ 00b6b208 ["INT_ADD", "register:40f0:8", ["const:b6b208:8", "const:4:8"]]
+ 00b6b208 ["CALL", null, ["callee:00bde6f0:8"]]
- 00b6b140 bytes 40cd0194
+ 00b6b208 bytes 3acd0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88e2b6435f30897eff693deefba217e0"></a>

### [`00b6b584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b584.md) → [`00b6b64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b64c.md) _ZN8firebase4auth17PhoneAuthProvider13GetCredentialEPKcS3_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.79% / 新版 95.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b6c4",
      "incomplete_value": true,
      "site": "00b6b6dc",
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
                "const:888:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b5fc",
      "incomplete_value": true,
      "site": "00b6b614",
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
                "const:7c8:8"
              ]
            ]
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
    "new": {
      "definition_site": "00b6b6c8",
      "incomplete_value": true,
      "site": "00b6b6dc",
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
                "const:8a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b600",
      "incomplete_value": true,
      "site": "00b6b614",
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
                "const:7e0:8"
              ]
            ]
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
    "new": {
      "definition_site": "00b6b734",
      "incomplete_value": false,
      "site": "00b6b738",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b66c",
      "incomplete_value": false,
      "site": "00b6b670",
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
            "const:dbf:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6b674",
      "READ",
      [
        "storage",
        "010a18f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6b6c4",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b6c8",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6b674",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6b6c4",
      "READ",
      [
        "storage",
        "010a1888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6b6c8",
      "READ",
      [
        "storage",
        "010a18a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b584.md#insn-00b6b614) · [`00b6b670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b584.md#insn-00b6b670) · [`00b6b6d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b584.md#insn-00b6b6d8)
- 新版 [`00b6b6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b64c.md#insn-00b6b6dc) · [`00b6b738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b64c.md#insn-00b6b738) · [`00b6b7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b64c.md#insn-00b6b7a0)

~~~diff
- 00b6b614 ["INT_ADD", "register:40f0:8", ["const:b6b614:8", "const:4:8"]]
- 00b6b614 ["CALL", null, ["callee:00bddcf0:8"]]
+ 00b6b6dc ["INT_ADD", "register:40f0:8", ["const:b6b6dc:8", "const:4:8"]]
+ 00b6b6dc ["CALL", null, ["callee:00bddcf0:8"]]
- 00b6b614 bytes 8bc90194
+ 00b6b6dc bytes 85c90194
- 00b6b670 ["INT_ADD", "register:40f0:8", ["const:b6b670:8", "const:4:8"]]
- 00b6b670 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6b738 ["INT_ADD", "register:40f0:8", ["const:b6b738:8", "const:4:8"]]
+ 00b6b738 ["CALL", null, ["callee:00bde130:8"]]
- 00b6b670 bytes 84ca0194
+ 00b6b738 bytes 7eca0194
- 00b6b6d8 ["INT_ADD", "register:40f0:8", ["const:b6b6d8:8", "const:4:8"]]
- 00b6b6d8 ["CALL", null, ["callee:00bdddf0:8"]]
+ 00b6b7a0 ["INT_ADD", "register:40f0:8", ["const:b6b7a0:8", "const:4:8"]]
+ 00b6b7a0 ["CALL", null, ["callee:00bdddf0:8"]]
- 00b6b6d8 bytes 9ac90194
+ 00b6b7a0 bytes 94c90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dfd2881a5a05fb57d5cd7dd55d5aed6"></a>

### [`00b6b7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b7a0.md) → [`00b6b868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b868.md) _ZN8firebase4auth20JniAuthPhoneListener29nativeOnVerificationCompletedEP7_JNIEnvP8_jobjectlS5_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2e0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde390.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 83.33% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6b8a8",
      "incomplete_value": false,
      "site": "00b6b8ac",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6b7e0",
      "incomplete_value": false,
      "site": "00b6b7e4",
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
            "const:dbf:8"
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
      "definition_site": "00b6b84c",
      "incomplete_value": true,
      "site": "00b6b850",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6b8a8",
      "PARAM",
      [
        "storage",
        "002a1dbf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6b8a8",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6b7e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b7a0.md#insn-00b6b7e4) · [`00b6b850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b7a0.md#insn-00b6b850) · [`00b6b7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b7a0.md#insn-00b6b7d0)
- 新版 [`00b6b8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b868.md#insn-00b6b8ac) · [`00b6b918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b868.md#insn-00b6b918) · [`00b6b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6b868.md#insn-00b6b898)

~~~diff
- 00b6b7e4 ["INT_ADD", "register:40f0:8", ["const:b6b7e4:8", "const:4:8"]]
- 00b6b7e4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6b8ac ["INT_ADD", "register:40f0:8", ["const:b6b8ac:8", "const:4:8"]]
+ 00b6b8ac ["CALL", null, ["callee:00bde130:8"]]
- 00b6b7e4 bytes 27ca0194
+ 00b6b8ac bytes 21ca0194
- 00b6b850 ["INT_ADD", "register:40f0:8", ["const:b6b850:8", "const:4:8"]]
- 00b6b850 ["CALL", null, ["callee:00bdb010:8"]]
+ 00b6b918 ["INT_ADD", "register:40f0:8", ["const:b6b918:8", "const:4:8"]]
+ 00b6b918 ["CALL", null, ["callee:00bdb010:8"]]
- 00b6b850 bytes c4bd0194
+ 00b6b918 bytes bebd0194
- 00b6b7d0 ["INT_ADD", "register:40f0:8", ["const:b6b7d0:8", "const:4:8"]]
- 00b6b7d0 ["CALL", null, ["callee:00bde390:8"]]
+ 00b6b898 ["INT_ADD", "register:40f0:8", ["const:b6b898:8", "const:4:8"]]
+ 00b6b898 ["CALL", null, ["callee:00bde390:8"]]
- 00b6b7d0 bytes c4ca0194
+ 00b6b898 bytes beca0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-554ef65929c35ab6fdb4eee4e0484118"></a>

### [`00b6b93c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b93c.md) → [`00b6ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6ba04.md) _ZN8firebase4auth20JniAuthPhoneListener16nativeOnCodeSentEP7_JNIEnvP8_jobjectlP8_jstringS5_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.30% / 新版 87.30%

CFGの説明率　旧版 73.33% / 新版 57.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b940"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b940"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6b944"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6b940",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6b944",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6b948",
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
      "00b6ba08",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b6ba0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6ba10",
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

- 旧版 [`00b6b940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b93c.md#insn-00b6b940) · [`00b6b944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b93c.md#insn-00b6b944) · [`00b6b948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6b93c.md#insn-00b6b948)

~~~diff
- 00b6b940 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b6b940 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b6b940 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b6b940 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6b940 bytes f85f03a9
- 00b6b944 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b6b944 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b6b944 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b6b944 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6b944 bytes f65704a9
- 00b6b948 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6b948 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6b948 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b6b948 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6b948 bytes f44f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88840cef018b3c89b22a17ceaf65c448"></a>

### [`00b6bb80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bb80.md) → [`00b6bc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bc48.md) _ZN8firebase4auth22FederatedOAuthProviderC1ERKNS0_26FederatedOAuthProviderDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddc20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc20.md) · 呼出先 3件 [`005188a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00518/005188a4.md) [`00bde130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde130.md) [`00bdff90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdf/00bdff90.md)
- 新版 呼出元 1件 [`00bddcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcd0.md) · 呼出先 3件 [`005188a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00518/005188a4.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00be0040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0040.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6bc6c",
      "incomplete_value": true,
      "site": "00b6bc70",
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
      "definition_site": "00b6bba4",
      "incomplete_value": true,
      "site": "00b6bba8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bbc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6bc90"
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
      "00b6bc60",
      "READ",
      [
        "storage",
        "00c1bb18",
        null,
        "pointer"
      ]
    ],
    [
      "00b6bc70",
      "DATA",
      [
        "storage",
        "00c126d8",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "unmatched:00b6bbcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bcdc"
      ]
    ]
  ],
  "added": [
    [
      "00b6bc60",
      "READ",
      [
        "storage",
        "00c1bbc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b6bc70",
      "DATA",
      [
        "storage",
        "00c12788",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00b6bc94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bcdc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6bbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bb80.md#insn-00b6bbc8) · [`00b6bbcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bb80.md#insn-00b6bbcc) · [`00b6bbec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bb80.md#insn-00b6bbec)

~~~diff
- 00b6bbc8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:38:8"]]
- 00b6bbc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b6bbc8 bytes 081c00f9
- 00b6bbcc ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00b6bbcc bytes 40020054
- 00b6bbec ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00b6bbec ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b6bbec ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00b6bbec ["COPY", "register:4010:8", ["tmp:0:8"]]
- 00b6bbec bytes 62018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49bed0c6f85d580d167f125c8ee6e075"></a>

### [`00b6bca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bca4.md) → [`00b6bd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bd6c.md) _ZN8firebase4auth22FederatedOAuthProviderD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 28.57% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bcc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6bd90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bcf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6bd80",
      "READ",
      [
        "storage",
        "00c1bb18",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b6bcc8",
      "DATA",
      [
        "storage",
        "00c126d8",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "unmatched:00b6bcf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bdd8"
      ]
    ]
  ],
  "added": [
    [
      "00b6bd80",
      "READ",
      [
        "storage",
        "00c1bbc8",
        null,
        "pointer"
      ]
    ],
    [
      "00b6bd90",
      "DATA",
      [
        "storage",
        "00c12788",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00b6bdc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6bdd8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6bcc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bca4.md#insn-00b6bcc8) · [`00b6bccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bca4.md#insn-00b6bccc) · [`00b6bcf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bca4.md#insn-00b6bcf8)
- 新版 [`00b6bd94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bd6c.md#insn-00b6bd94)

~~~diff
- 00b6bcc8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b6bcc8 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b6bcc8 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:38:8"]]
- 00b6bcc8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b6bcc8 bytes 088403f8
- 00b6bccc ["INT_ADD", "register:40f0:8", ["const:b6bccc:8", "const:4:8"]]
- 00b6bccc ["CALL", null, ["callee:0044a5b8:8"]]
+ 00b6bd94 ["INT_ADD", "register:40f0:8", ["const:b6bd94:8", "const:4:8"]]
+ 00b6bd94 ["CALL", null, ["callee:0044a5b8:8"]]
- 00b6bccc bytes 3b7ae397
+ 00b6bd94 bytes 097ae397
- 00b6bcf8 ["CBRANCH", null, ["local:b10:8", "register:101:1"]]
- 00b6bcf8 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f8af11c22069e23b6bcac30f265d7d7"></a>

### [`00b6bd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bd50.md) → [`00b6be18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6be18.md) _ZN8firebase4auth22FederatedOAuthProviderD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044a5b8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 57.89% / 新版 55.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bd50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bd54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6bd54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6bd50",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6bd54",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6be2c",
      "READ",
      [
        "storage",
        "00c1bb18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b6be18",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6be1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6be2c",
      "READ",
      [
        "storage",
        "00c1bbc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6bd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bd50.md#insn-00b6bd50) · [`00b6bd54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bd50.md#insn-00b6bd54) · [`00b6bd78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6bd50.md#insn-00b6bd78)
- 新版 [`00b6be40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6be18.md#insn-00b6be40)

~~~diff
- 00b6bd50 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b6bd50 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b6bd50 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6bd50 bytes f50f1df8
- 00b6bd54 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6bd54 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6bd54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6bd54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6bd54 bytes f44f01a9
- 00b6bd78 ["INT_ADD", "register:40f0:8", ["const:b6bd78:8", "const:4:8"]]
- 00b6bd78 ["CALL", null, ["callee:0044a5b8:8"]]
+ 00b6be40 ["INT_ADD", "register:40f0:8", ["const:b6be40:8", "const:4:8"]]
+ 00b6be40 ["CALL", null, ["callee:0044a5b8:8"]]
- 00b6bd78 bytes 107ae397
+ 00b6be40 bytes de79e397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d78873483dcba15111a514fd66065aa6"></a>

### [`00b6be60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6be60.md) → [`00b6bf28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bf28.md) _ZN8firebase4auth22FederatedOAuthProvider6SignInEPNS0_8AuthDataE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b64df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md) [`00b6c204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c204.md) [`00b6d148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d148.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) [`00b6c2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c2cc.md) [`00b6d210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d210.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 20.00% / 新版 22.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6be74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6be74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6be78"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6be74",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6be78",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6be94",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6bf3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6bf40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6bf5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6be74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6be60.md#insn-00b6be74) · [`00b6be78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6be60.md#insn-00b6be78) · [`00b6be94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6be60.md#insn-00b6be94)

~~~diff
- 00b6be74 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6be74 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6be74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1b0:8"]]
- 00b6be74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6be74 bytes f44f1ba9
- 00b6be78 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6be78 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6be78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1c0:8"]]
- 00b6be78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6be78 bytes fd7b1ca9
- 00b6be94 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b6be94 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00b6be94 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b6be94 bytes a9031af8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61dfa0b42b444bd3cbc1ff8ce93e1fe2"></a>

### [`00b6c204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c204.md) → [`00b6c2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c2cc.md) FUN_00b6c2cc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00b6be60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6be60.md) [`00b6c444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c444.md) [`00b6c71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c71c.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc40.md) [`00bde030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde030.md)
- 新版 呼出元 3件 [`00b6bf28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bf28.md) [`00b6c50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c50c.md) [`00b6c7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c7e4.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bde0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.61% / 新版 98.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6c328",
      "incomplete_value": true,
      "site": "00b6c340",
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
                "const:7e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6c260",
      "incomplete_value": true,
      "site": "00b6c278",
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
                "const:720:8"
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
      "definition_site": "00b6c32c",
      "incomplete_value": true,
      "site": "00b6c340",
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
                "const:7f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6c264",
      "incomplete_value": true,
      "site": "00b6c278",
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
                "const:738:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6c3a0",
      "incomplete_value": true,
      "site": "00b6c3b0",
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
                "const:8d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6c2d8",
      "incomplete_value": true,
      "site": "00b6c2e8",
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
                "const:810:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6c328",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6c32c",
      "READ",
      [
        "storage",
        "010a1738",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6c3a0",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6c328",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6c32c",
      "READ",
      [
        "storage",
        "010a17f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6c3a0",
      "READ",
      [
        "storage",
        "010a18d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6c278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c204.md#insn-00b6c278) · [`00b6c2e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c204.md#insn-00b6c2e8) · [`00b6c378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c204.md#insn-00b6c378)
- 新版 [`00b6c340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c2cc.md#insn-00b6c340) · [`00b6c3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c2cc.md#insn-00b6c3b0) · [`00b6c440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c2cc.md#insn-00b6c440)

~~~diff
- 00b6c278 ["INT_ADD", "register:40f0:8", ["const:b6c278:8", "const:4:8"]]
- 00b6c278 ["CALL", null, ["callee:00bddcf0:8"]]
+ 00b6c340 ["INT_ADD", "register:40f0:8", ["const:b6c340:8", "const:4:8"]]
+ 00b6c340 ["CALL", null, ["callee:00bddcf0:8"]]
- 00b6c278 bytes 72c60194
+ 00b6c340 bytes 6cc60194
- 00b6c2e8 ["INT_ADD", "register:40f0:8", ["const:b6c2e8:8", "const:4:8"]]
- 00b6c2e8 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6c3b0 ["INT_ADD", "register:40f0:8", ["const:b6c3b0:8", "const:4:8"]]
+ 00b6c3b0 ["CALL", null, ["callee:0047495c:8"]]
- 00b6c2e8 bytes 9d21e497
+ 00b6c3b0 bytes 6b21e497
- 00b6c378 ["INT_ADD", "register:40f0:8", ["const:b6c378:8", "const:4:8"]]
- 00b6c378 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6c440 ["INT_ADD", "register:40f0:8", ["const:b6c440:8", "const:4:8"]]
+ 00b6c440 ["CALL", null, ["callee:0047495c:8"]]
- 00b6c378 bytes 7921e497
+ 00b6c440 bytes 4721e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1abd77c3808a17261dfb32ceeb3b8b97"></a>

### [`00b6ca20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6ca20.md) → [`00b6cae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cae8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10CredentialEEEvRKNS_12FutureHandleEiPKcEUlPvE_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0cd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0cd0.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d80.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6cb4c",
      "incomplete_value": false,
      "site": "00b6cb50",
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
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ca84",
      "incomplete_value": false,
      "site": "00b6ca88",
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
      "00b6cb4c",
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
      "00b6cb4c",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ca88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6ca20.md#insn-00b6ca88) · [`00b6ca4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6ca20.md#insn-00b6ca4c) · [`00b6ca58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6ca20.md#insn-00b6ca58)
- 新版 [`00b6cb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cae8.md#insn-00b6cb50) · [`00b6cb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cae8.md#insn-00b6cb14) · [`00b6cb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cae8.md#insn-00b6cb20)

~~~diff
- 00b6ca88 ["INT_ADD", "register:40f0:8", ["const:b6ca88:8", "const:4:8"]]
- 00b6ca88 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6cb50 ["INT_ADD", "register:40f0:8", ["const:b6cb50:8", "const:4:8"]]
+ 00b6cb50 ["CALL", null, ["callee:00bde130:8"]]
- 00b6ca88 bytes 7ec50194
+ 00b6cb50 bytes 78c50194
- 00b6ca4c ["INT_ADD", "register:40f0:8", ["const:b6ca4c:8", "const:4:8"]]
- 00b6ca4c ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b6cb14 ["INT_ADD", "register:40f0:8", ["const:b6cb14:8", "const:4:8"]]
+ 00b6cb14 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b6ca4c bytes 35c40194
+ 00b6cb14 bytes 2fc40194
- 00b6ca58 ["INT_ADD", "register:40f0:8", ["const:b6ca58:8", "const:4:8"]]
- 00b6ca58 ["CALL", null, ["callee:00bddfb0:8"]]
+ 00b6cb20 ["INT_ADD", "register:40f0:8", ["const:b6cb20:8", "const:4:8"]]
+ 00b6cb20 ["CALL", null, ["callee:00bddfb0:8"]]
- 00b6ca58 bytes 2ac50194
+ 00b6cb20 bytes 24c50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f4ed38fefb27388d2c4dc1dd1dbd1c5"></a>

### [`00b6ce08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6ce08.md) → [`00b6ced0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6ced0.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE30__emp

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0d70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d70.md) · 呼出先 5件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdd9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd9a0.md) [`00bde660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde660.md) [`00be0d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d60.md)
- 新版 呼出元 1件 [`00be0e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e20.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdda50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00be0e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.48% / 新版 84.48%

CFGの説明率　旧版 20.00% / 新版 11.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ce3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ce60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6cf04"
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
      "unmatched:00b6ce3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6cecc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cfb4"
      ]
    ]
  ],
  "added": [
    [
      "00b6cf04",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b6cf94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6cfb4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ce3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6ce08.md#insn-00b6ce3c) · [`00b6ce40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6ce08.md#insn-00b6ce40) · [`00b6ce60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6ce08.md#insn-00b6ce60)
- 新版 [`00b6cf08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6ced0.md#insn-00b6cf08)

~~~diff
- 00b6ce3c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00b6ce3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b6ce3c bytes e80f00f9
- 00b6ce40 ["INT_ADD", "register:40f0:8", ["const:b6ce40:8", "const:4:8"]]
- 00b6ce40 ["CALL", null, ["callee:00be0e10:8"]]
+ 00b6cf08 ["INT_ADD", "register:40f0:8", ["const:b6cf08:8", "const:4:8"]]
+ 00b6cf08 ["CALL", null, ["callee:00be0e10:8"]]
- 00b6ce40 bytes c8cf0194
+ 00b6cf08 bytes c2cf0194
- 00b6ce60 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6ce60 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6ce60 ["INT_ADD", "register:40b8:8", ["register:40b8:8", "const:20:8"]]
- 00b6ce60 ["STORE", null, ["const:1b1:8", "register:40b8:8", "tmp:1:4"]]
- 00b6ce60 bytes ff0e02b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48af54c3cf46ff9d5bec63d48df2d4e0"></a>

### [`00b6cf1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cf1c.md) → [`00b6cfe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6cfe4.md) _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__fin

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d60.md) · 呼出先 1件 [`00bde620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde620.md)
- 新版 呼出元 1件 [`00be0e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e10.md) · 呼出先 1件 [`00bde6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.21% / 新版 89.21%

CFGの説明率　旧版 48.75% / 新版 49.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cf1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cf20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6cf20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6cf1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6cf20",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6cf24",
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
      "00b6cfe4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b6cfe8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b6cfec",
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

- 旧版 [`00b6cf1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cf1c.md#insn-00b6cf1c) · [`00b6cf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cf1c.md#insn-00b6cf20) · [`00b6cf24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6cf1c.md#insn-00b6cf24)

~~~diff
- 00b6cf1c ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 00b6cf1c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00b6cf1c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6cf1c bytes f90f1bf8
- 00b6cf20 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b6cf20 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b6cf20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6cf20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6cf20 bytes f85f01a9
- 00b6cf24 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b6cf24 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b6cf24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6cf24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6cf24 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1721ef77a7366fc4b73509575f7eecb"></a>

### [`00b6d148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d148.md) → [`00b6d210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d210.md) _ZN8firebase4auth35FederatedAuthProviderFutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00b6be60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6b/00b6be60.md) [`00b6c444`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c444.md) [`00b6c71c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6c/00b6c71c.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00be0c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c20.md)
- 新版 呼出元 3件 [`00b6bf28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6b/00b6bf28.md) [`00b6c50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c50c.md) [`00b6c7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6c/00b6c7e4.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cd0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d178"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d17c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6d240"
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
      "unmatched:00b6d178",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6d17c",
      "WRITE",
      [
        "storage",
        "Stack[-0x4c]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6d240",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00b6d244",
      "WRITE",
      [
        "storage",
        "Stack[-0x4c]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d148.md#insn-00b6d178) · [`00b6d17c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d148.md#insn-00b6d17c) · [`00b6d180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d148.md#insn-00b6d180)
- 新版 [`00b6d248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d210.md#insn-00b6d248)

~~~diff
- 00b6d178 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b6d178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b6d178 bytes e81f00f9
- 00b6d17c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6d17c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6d17c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:34:8"]]
- 00b6d17c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6d17c bytes ffd30039
- 00b6d180 ["INT_ADD", "register:40f0:8", ["const:b6d180:8", "const:4:8"]]
- 00b6d180 ["CALL", null, ["callee:00be0cd0:8"]]
+ 00b6d248 ["INT_ADD", "register:40f0:8", ["const:b6d248:8", "const:4:8"]]
+ 00b6d248 ["CALL", null, ["callee:00be0cd0:8"]]
- 00b6d180 bytes a8ce0194
+ 00b6d248 bytes a2ce0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f21a4cb917713dc1f266838373bade2e"></a>

### [`00b6d224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d224.md) → [`00b6d2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d2ec.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0cc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0cc0.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d70.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

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
      "definition_site": "00b6d358",
      "incomplete_value": false,
      "site": "00b6d35c",
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
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d290",
      "incomplete_value": false,
      "site": "00b6d294",
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
      "00b6d358",
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
      "00b6d358",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d224.md#insn-00b6d294) · [`00b6d258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d224.md#insn-00b6d258) · [`00b6d264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d224.md#insn-00b6d264)
- 新版 [`00b6d35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d2ec.md#insn-00b6d35c) · [`00b6d320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d2ec.md#insn-00b6d320) · [`00b6d32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d2ec.md#insn-00b6d32c)

~~~diff
- 00b6d294 ["INT_ADD", "register:40f0:8", ["const:b6d294:8", "const:4:8"]]
- 00b6d294 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6d35c ["INT_ADD", "register:40f0:8", ["const:b6d35c:8", "const:4:8"]]
+ 00b6d35c ["CALL", null, ["callee:00bde130:8"]]
- 00b6d294 bytes 7bc30194
+ 00b6d35c bytes 75c30194
- 00b6d258 ["INT_ADD", "register:40f0:8", ["const:b6d258:8", "const:4:8"]]
- 00b6d258 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b6d320 ["INT_ADD", "register:40f0:8", ["const:b6d320:8", "const:4:8"]]
+ 00b6d320 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b6d258 bytes 32c20194
+ 00b6d320 bytes 2cc20194
- 00b6d264 ["INT_ADD", "register:40f0:8", ["const:b6d264:8", "const:4:8"]]
- 00b6d264 ["CALL", null, ["callee:00bddfb0:8"]]
+ 00b6d32c ["INT_ADD", "register:40f0:8", ["const:b6d32c:8", "const:4:8"]]
+ 00b6d32c ["CALL", null, ["callee:00bddfb0:8"]]
- 00b6d264 bytes 27c30194
+ 00b6d32c bytes 21c30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2b22d26088f7db080de2dd200bd7ce2"></a>

### [`00b6d3e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d3e4.md) → [`00b6d4ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ac.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b6d4d8",
      "incomplete_value": true,
      "site": "00b6d4d8",
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
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d410",
      "incomplete_value": true,
      "site": "00b6d410",
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
            "const:8f8:8"
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
      "definition_site": "00b6d4c0",
      "incomplete_value": true,
      "site": "00b6d4c0",
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
      "definition_site": "00b6d3f8",
      "incomplete_value": true,
      "site": "00b6d3f8",
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
      "definition_site": "00b6d4cc",
      "incomplete_value": false,
      "site": "00b6d4d0",
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
            "const:2ed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d404",
      "incomplete_value": false,
      "site": "00b6d408",
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
            "const:2e7:8"
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
      "00b6d4bc",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d4cc",
      "PARAM",
      [
        "storage",
        "002ab2e7",
        null,
        "string"
      ]
    ],
    [
      "00b6d4d8",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d4bc",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d4cc",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ],
    [
      "00b6d4d8",
      "WRITE",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d3e4.md#insn-00b6d408) · [`00b6d410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d3e4.md#insn-00b6d410) · [`00b6d3f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d3e4.md#insn-00b6d3f4)
- 新版 [`00b6d4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ac.md#insn-00b6d4d0) · [`00b6d4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ac.md#insn-00b6d4d8) · [`00b6d4bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ac.md#insn-00b6d4bc)

~~~diff
- 00b6d408 ["INT_ADD", "register:40f0:8", ["const:b6d408:8", "const:4:8"]]
- 00b6d408 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6d4d0 ["INT_ADD", "register:40f0:8", ["const:b6d4d0:8", "const:4:8"]]
+ 00b6d4d0 ["CALL", null, ["callee:00bde040:8"]]
- 00b6d408 bytes e2c20194
+ 00b6d4d0 bytes dcc20194
- 00b6d410 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00b6d410 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d4d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
+ 00b6d4d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d410 bytes 607e04f9
+ 00b6d4d8 bytes 60de04f9
- 00b6d3f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00b6d3f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d4bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
+ 00b6d4bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d3f4 bytes 687e44f9
+ 00b6d4bc bytes 68de44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b201cf09a3d00fd344840764c745d88"></a>

### [`00b6d424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d424.md) → [`00b6d4ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ec.md) _ZN8firebase4auth11tokenresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b6d424"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d428"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d428"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d424",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6d428",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6d4fc",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d4ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6d4f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6d4fc",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d424.md#insn-00b6d424) · [`00b6d428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d424.md#insn-00b6d428) · [`00b6d438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d424.md#insn-00b6d438)
- 新版 [`00b6d500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d4ec.md#insn-00b6d500)

~~~diff
- 00b6d424 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b6d424 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6d424 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6d424 bytes f30f1ef8
- 00b6d428 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6d428 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6d428 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6d428 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6d428 bytes fd7b01a9
- 00b6d438 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6d438 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b6d500 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b6d500 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6d438 bytes e80000b5
+ 00b6d500 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b48ce167aff2ddcf992d50293f69d1a"></a>

### [`00b6d464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d464.md) → [`00b6d52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d52c.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b6d55c",
      "incomplete_value": true,
      "site": "00b6d55c",
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
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d494",
      "incomplete_value": true,
      "site": "00b6d494",
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
            "const:8f8:8"
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
      "definition_site": "00b6d540",
      "incomplete_value": true,
      "site": "00b6d540",
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
      "definition_site": "00b6d478",
      "incomplete_value": true,
      "site": "00b6d478",
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
      "definition_site": "00b6d54c",
      "incomplete_value": false,
      "site": "00b6d554",
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
            "const:2ed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d484",
      "incomplete_value": false,
      "site": "00b6d48c",
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
            "const:2e7:8"
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
      "00b6d53c",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d54c",
      "PARAM",
      [
        "storage",
        "002ab2e7",
        null,
        "string"
      ]
    ],
    [
      "00b6d55c",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d53c",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d54c",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ],
    [
      "00b6d55c",
      "WRITE",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d48c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d464.md#insn-00b6d48c) · [`00b6d494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d464.md#insn-00b6d494) · [`00b6d474`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d464.md#insn-00b6d474)
- 新版 [`00b6d554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d52c.md#insn-00b6d554) · [`00b6d55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d52c.md#insn-00b6d55c) · [`00b6d53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d52c.md#insn-00b6d53c)

~~~diff
- 00b6d48c ["INT_ADD", "register:40f0:8", ["const:b6d48c:8", "const:4:8"]]
- 00b6d48c ["CALL", null, ["callee:00bde040:8"]]
+ 00b6d554 ["INT_ADD", "register:40f0:8", ["const:b6d554:8", "const:4:8"]]
+ 00b6d554 ["CALL", null, ["callee:00bde040:8"]]
- 00b6d48c bytes c1c20194
+ 00b6d554 bytes bbc20194
- 00b6d494 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00b6d494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d55c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
+ 00b6d55c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d494 bytes 607e04f9
+ 00b6d55c bytes 60de04f9
- 00b6d474 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00b6d474 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d53c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
+ 00b6d53c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d474 bytes 687e44f9
+ 00b6d53c bytes 68de44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e979411a6f7b5f387c658bfe70a82933"></a>

### [`00b6d4a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d4a8.md) → [`00b6d570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d570.md) _ZN8firebase4auth11tokenresult10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b6d5a0",
      "incomplete_value": true,
      "site": "00b6d5a0",
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
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d4d8",
      "incomplete_value": true,
      "site": "00b6d4d8",
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
            "const:8f8:8"
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
      "definition_site": "00b6d584",
      "incomplete_value": true,
      "site": "00b6d584",
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
      "definition_site": "00b6d4bc",
      "incomplete_value": true,
      "site": "00b6d4bc",
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
      "definition_site": "00b6d58c",
      "incomplete_value": false,
      "site": "00b6d598",
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
            "const:2ed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d4c4",
      "incomplete_value": false,
      "site": "00b6d4d0",
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
            "const:2e7:8"
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
      "00b6d580",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d58c",
      "PARAM",
      [
        "storage",
        "002ab2e7",
        null,
        "string"
      ]
    ],
    [
      "00b6d5a0",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d580",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d58c",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ],
    [
      "00b6d5a0",
      "WRITE",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d4d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d4a8.md#insn-00b6d4d0) · [`00b6d4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d4a8.md#insn-00b6d4d8) · [`00b6d4b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d4a8.md#insn-00b6d4b8)
- 新版 [`00b6d598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d570.md#insn-00b6d598) · [`00b6d5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d570.md#insn-00b6d5a0) · [`00b6d580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d570.md#insn-00b6d580)

~~~diff
- 00b6d4d0 ["INT_ADD", "register:40f0:8", ["const:b6d4d0:8", "const:4:8"]]
- 00b6d4d0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6d598 ["INT_ADD", "register:40f0:8", ["const:b6d598:8", "const:4:8"]]
+ 00b6d598 ["CALL", null, ["callee:00bde040:8"]]
- 00b6d4d0 bytes b0c20194
+ 00b6d598 bytes aac20194
- 00b6d4d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00b6d4d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d5a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
+ 00b6d5a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d4d8 bytes 607e04f9
+ 00b6d5a0 bytes 60de04f9
- 00b6d4b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00b6d4b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d580 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9b8:8"]]
+ 00b6d580 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d4b8 bytes 687e44f9
+ 00b6d580 bytes 68de44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-970ad82fe3f64ceaa80953457ba0a510"></a>

### [`00b6d4f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d4f8.md) → [`00b6d5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d5c0.md) _ZN8firebase4auth11tokenresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b6d618",
      "incomplete_value": true,
      "site": "00b6d618",
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
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d550",
      "incomplete_value": true,
      "site": "00b6d550",
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
            "const:900:8"
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
      "definition_site": "00b6d5f4",
      "incomplete_value": true,
      "site": "00b6d600",
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
                "const:9b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d52c",
      "incomplete_value": true,
      "site": "00b6d538",
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
                "const:8f8:8"
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
      "00b6d5d4",
      "READ",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d5f4",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d618",
      "WRITE",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6d5d4",
      "READ",
      [
        "storage",
        "010a19c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d5f4",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d618",
      "WRITE",
      [
        "storage",
        "010a19c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d4f8.md#insn-00b6d538) · [`00b6d550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d4f8.md#insn-00b6d550) · [`00b6d50c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d4f8.md#insn-00b6d50c)
- 新版 [`00b6d600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d5c0.md#insn-00b6d600) · [`00b6d618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d5c0.md#insn-00b6d618) · [`00b6d5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d5c0.md#insn-00b6d5d4)

~~~diff
- 00b6d538 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d538 ["INT_ADD", "register:40f0:8", ["const:b6d538:8", "const:4:8"]]
- 00b6d538 ["CALLIND", null, ["register:0:8"]]
+ 00b6d600 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6d600 ["INT_ADD", "register:40f0:8", ["const:b6d600:8", "const:4:8"]]
+ 00b6d600 ["CALLIND", null, ["register:0:8"]]
- 00b6d538 bytes 00013fd6
+ 00b6d600 bytes 00013fd6
- 00b6d550 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6d550 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:900:8"]]
- 00b6d550 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6d618 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6d618 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9c0:8"]]
+ 00b6d618 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6d550 bytes a0022439
+ 00b6d618 bytes a0022739
- 00b6d50c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:900:8"]]
- 00b6d50c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6d50c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6d5d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9c0:8"]]
+ 00b6d5d4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d5d4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6d50c bytes a8026439
+ 00b6d5d4 bytes a8026739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc4b51fdef213747855f4e3b9f355d2b"></a>

### [`00b6d564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d564.md) → [`00b6d62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d62c.md) _ZN8firebase4auth11tokenresult12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b6d668",
      "incomplete_value": true,
      "site": "00b6d668",
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
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d5a0",
      "incomplete_value": true,
      "site": "00b6d5a0",
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
            "const:900:8"
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
      "definition_site": "00b6d688",
      "incomplete_value": true,
      "site": "00b6d688",
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
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d5c0",
      "incomplete_value": true,
      "site": "00b6d5c0",
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
            "const:8f8:8"
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
      "definition_site": "00b6d644",
      "incomplete_value": true,
      "site": "00b6d644",
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
      "definition_site": "00b6d57c",
      "incomplete_value": true,
      "site": "00b6d57c",
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
      "00b6d640",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d64c",
      "READ",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d668",
      "WRITE",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6d640",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d64c",
      "READ",
      [
        "storage",
        "010a19c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d668",
      "WRITE",
      [
        "storage",
        "010a19c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d564.md#insn-00b6d5a0) · [`00b6d5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d564.md#insn-00b6d5bc) · [`00b6d5c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d564.md#insn-00b6d5c0)
- 新版 [`00b6d668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d62c.md#insn-00b6d668) · [`00b6d684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d62c.md#insn-00b6d684) · [`00b6d688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d62c.md#insn-00b6d688)

~~~diff
- 00b6d5a0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6d5a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6d5a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:900:8"]]
- 00b6d5a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6d668 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6d668 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6d668 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9c0:8"]]
+ 00b6d668 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6d5a0 bytes bf022439
+ 00b6d668 bytes bf022739
- 00b6d5bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d5bc ["INT_ADD", "register:40f0:8", ["const:b6d5bc:8", "const:4:8"]]
- 00b6d5bc ["CALLIND", null, ["register:0:8"]]
+ 00b6d684 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6d684 ["INT_ADD", "register:40f0:8", ["const:b6d684:8", "const:4:8"]]
+ 00b6d684 ["CALLIND", null, ["register:0:8"]]
- 00b6d5bc bytes 00013fd6
+ 00b6d684 bytes 00013fd6
- 00b6d5c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
- 00b6d5c0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6d5c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b6d688 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
+ 00b6d688 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b6d688 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6d5c0 bytes 9f7e04f9
+ 00b6d688 bytes 9fde04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6947dfdbad0a96847069139b1113ac73"></a>

### [`00b6d5d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d5d4.md) → [`00b6d69c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d69c.md) _ZN8firebase4auth11tokenresult14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6d6dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d5f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d5e8",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6d5f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d6e0"
      ]
    ],
    [
      "unmatched:00b6d5f8",
      "PARAM",
      [
        "storage",
        "002ab2e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6d6b0",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d6b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6d6e0"
      ]
    ],
    [
      "00b6d6c0",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d5d4.md#insn-00b6d5f0) · [`00b6d60c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d5d4.md#insn-00b6d60c) · [`00b6d614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d5d4.md#insn-00b6d614)
- 新版 [`00b6d6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d69c.md#insn-00b6d6d4)

~~~diff
- 00b6d5f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d5f0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6d5f0 bytes 410100b5
- 00b6d60c ["INT_ADD", "register:40f0:8", ["const:b6d60c:8", "const:4:8"]]
- 00b6d60c ["CALL", null, ["callee:00bde040:8"]]
+ 00b6d6d4 ["INT_ADD", "register:40f0:8", ["const:b6d6d4:8", "const:4:8"]]
+ 00b6d6d4 ["CALL", null, ["callee:00bde040:8"]]
- 00b6d60c bytes 61c20194
+ 00b6d6d4 bytes 5bc20194
- 00b6d614 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
- 00b6d614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d614 bytes 807e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-258fc366c58c860261738ce413f454d7"></a>

### [`00b6d680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d680.md) → [`00b6d748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d748.md) _ZN8firebase4auth11tokenresult13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_destination

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
      "definition_site": "00b6d788",
      "incomplete_value": true,
      "site": "00b6d788",
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
            "const:9b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d6c0",
      "incomplete_value": true,
      "site": "00b6d6c0",
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
            "const:8f8:8"
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
      "definition_site": "00b6d764",
      "incomplete_value": true,
      "site": "00b6d764",
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
      "definition_site": "00b6d69c",
      "incomplete_value": true,
      "site": "00b6d69c",
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
      "definition_site": "00b6d76c",
      "incomplete_value": false,
      "site": "00b6d780",
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
            "const:2ed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d6a4",
      "incomplete_value": false,
      "site": "00b6d6b8",
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
            "const:2e7:8"
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
      "00b6d75c",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d76c",
      "PARAM",
      [
        "storage",
        "002ab2e7",
        null,
        "string"
      ]
    ],
    [
      "00b6d788",
      "WRITE",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d75c",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d76c",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ],
    [
      "00b6d788",
      "WRITE",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d6b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d680.md#insn-00b6d6b8) · [`00b6d6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d680.md#insn-00b6d6c0) · [`00b6d694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d680.md#insn-00b6d694)
- 新版 [`00b6d780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d748.md#insn-00b6d780) · [`00b6d788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d748.md#insn-00b6d788) · [`00b6d75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d748.md#insn-00b6d75c)

~~~diff
- 00b6d6b8 ["INT_ADD", "register:40f0:8", ["const:b6d6b8:8", "const:4:8"]]
- 00b6d6b8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6d780 ["INT_ADD", "register:40f0:8", ["const:b6d780:8", "const:4:8"]]
+ 00b6d780 ["CALL", null, ["callee:00bde040:8"]]
- 00b6d6b8 bytes 36c20194
+ 00b6d780 bytes 30c20194
- 00b6d6c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
- 00b6d6c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d788 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
+ 00b6d788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d6c0 bytes 807e04f9
+ 00b6d788 bytes 80de04f9
- 00b6d694 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
- 00b6d694 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d75c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
+ 00b6d75c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d694 bytes 817e44f9
+ 00b6d75c bytes 81de44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a14aea8d187629da752b5dafb46377f"></a>

### [`00b6d6f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d6f0.md) → [`00b6d7b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7b8.md) _ZN8firebase4auth11tokenresult10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b6d7d4",
      "incomplete_value": false,
      "site": "00b6d7d8",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d70c",
      "incomplete_value": false,
      "site": "00b6d710",
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
      "definition_site": "00b6d7e4",
      "incomplete_value": true,
      "site": "00b6d7f0",
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
      "definition_site": "00b6d71c",
      "incomplete_value": true,
      "site": "00b6d728",
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
      "00b6d7d4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6d7e4",
      "DATA",
      [
        "storage",
        "010a1910",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6d7d4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6d7e4",
      "DATA",
      [
        "storage",
        "010a19d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d6f0.md#insn-00b6d710) · [`00b6d70c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d6f0.md#insn-00b6d70c) · [`00b6d718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d6f0.md#insn-00b6d718)
- 新版 [`00b6d7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7b8.md#insn-00b6d7d8) · [`00b6d7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7b8.md#insn-00b6d7d4) · [`00b6d7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7b8.md#insn-00b6d7e0)

~~~diff
- 00b6d710 ["INT_ADD", "register:40f0:8", ["const:b6d710:8", "const:4:8"]]
- 00b6d710 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6d7d8 ["INT_ADD", "register:40f0:8", ["const:b6d7d8:8", "const:4:8"]]
+ 00b6d7d8 ["CALL", null, ["callee:00bde130:8"]]
- 00b6d710 bytes 5cc20194
+ 00b6d7d8 bytes 56c20194
- 00b6d70c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b6d70c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6d70c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6d70c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6d7d4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b6d7d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6d7d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6d7d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6d70c bytes 00c81791
+ 00b6d7d4 bytes 00fc1991
- 00b6d718 ["COPY", "tmp:0:8", ["const:910:8"]]
- 00b6d718 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6d718 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6d718 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6d7e0 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 00b6d7e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6d7e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6d7e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6d718 bytes 08412491
+ 00b6d7e0 bytes 08412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dda12824cd8260ef4a20d7ce160a8855"></a>

### [`00b6d72c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d72c.md) → [`00b6d7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7f4.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b6d820",
      "incomplete_value": true,
      "site": "00b6d820",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d758",
      "incomplete_value": true,
      "site": "00b6d758",
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
            "const:918:8"
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
      "definition_site": "00b6d808",
      "incomplete_value": true,
      "site": "00b6d808",
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
      "definition_site": "00b6d740",
      "incomplete_value": true,
      "site": "00b6d740",
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
      "definition_site": "00b6d814",
      "incomplete_value": false,
      "site": "00b6d818",
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
            "const:96e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d74c",
      "incomplete_value": false,
      "site": "00b6d750",
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
            "const:8e1:8"
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
      "00b6d804",
      "READ",
      [
        "storage",
        "010a1918",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d814",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b6d820",
      "WRITE",
      [
        "storage",
        "010a1918",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d804",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d814",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b6d820",
      "WRITE",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d72c.md#insn-00b6d750) · [`00b6d758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d72c.md#insn-00b6d758) · [`00b6d73c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d72c.md#insn-00b6d73c)
- 新版 [`00b6d818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7f4.md#insn-00b6d818) · [`00b6d820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7f4.md#insn-00b6d820) · [`00b6d804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d7f4.md#insn-00b6d804)

~~~diff
- 00b6d750 ["INT_ADD", "register:40f0:8", ["const:b6d750:8", "const:4:8"]]
- 00b6d750 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6d818 ["INT_ADD", "register:40f0:8", ["const:b6d818:8", "const:4:8"]]
+ 00b6d818 ["CALL", null, ["callee:00bde040:8"]]
- 00b6d750 bytes 10c20194
+ 00b6d818 bytes 0ac20194
- 00b6d758 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:918:8"]]
- 00b6d758 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d820 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b6d820 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d758 bytes 608e04f9
+ 00b6d820 bytes 60ee04f9
- 00b6d73c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:918:8"]]
- 00b6d73c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d804 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b6d804 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d73c bytes 688e44f9
+ 00b6d804 bytes 68ee44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4865d457f5181ff2c96019e2778ec562"></a>

### [`00b6d76c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d76c.md) → [`00b6d834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d834.md) _ZN8firebase4auth4user19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b6d860",
      "incomplete_value": true,
      "site": "00b6d860",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d798",
      "incomplete_value": true,
      "site": "00b6d798",
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
            "const:918:8"
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
      "definition_site": "00b6d848",
      "incomplete_value": true,
      "site": "00b6d848",
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
      "definition_site": "00b6d780",
      "incomplete_value": true,
      "site": "00b6d780",
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
      "definition_site": "00b6d850",
      "incomplete_value": false,
      "site": "00b6d858",
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
            "const:96e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d788",
      "incomplete_value": false,
      "site": "00b6d790",
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
            "const:8e1:8"
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
      "00b6d844",
      "READ",
      [
        "storage",
        "010a1918",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d850",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b6d860",
      "WRITE",
      [
        "storage",
        "010a1918",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d844",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d850",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b6d860",
      "WRITE",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d76c.md#insn-00b6d790) · [`00b6d798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d76c.md#insn-00b6d798) · [`00b6d77c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d76c.md#insn-00b6d77c)
- 新版 [`00b6d858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d834.md#insn-00b6d858) · [`00b6d860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d834.md#insn-00b6d860) · [`00b6d844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d834.md#insn-00b6d844)

~~~diff
- 00b6d790 ["INT_ADD", "register:40f0:8", ["const:b6d790:8", "const:4:8"]]
- 00b6d790 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6d858 ["INT_ADD", "register:40f0:8", ["const:b6d858:8", "const:4:8"]]
+ 00b6d858 ["CALL", null, ["callee:00bde040:8"]]
- 00b6d790 bytes 00c20194
+ 00b6d858 bytes fac10194
- 00b6d798 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:918:8"]]
- 00b6d798 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d860 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b6d860 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d798 bytes 608e04f9
+ 00b6d860 bytes 60ee04f9
- 00b6d77c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:918:8"]]
- 00b6d77c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d844 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b6d844 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d77c bytes 688e44f9
+ 00b6d844 bytes 68ee44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45aaaa992e64f66f25dfd9f18b92eb95"></a>

### [`00b6d7ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d7ac.md) → [`00b6d874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d874.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

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
      "site": "00b6d7ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d7b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d7b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d7ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6d7b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6d884",
      "READ",
      [
        "storage",
        "010a1918",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d874",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6d878",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6d884",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d7ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d7ac.md#insn-00b6d7ac) · [`00b6d7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d7ac.md#insn-00b6d7b0) · [`00b6d7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d7ac.md#insn-00b6d7c0)
- 新版 [`00b6d888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d874.md#insn-00b6d888)

~~~diff
- 00b6d7ac ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b6d7ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6d7ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6d7ac bytes f30f1ef8
- 00b6d7b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6d7b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6d7b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6d7b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6d7b0 bytes fd7b01a9
- 00b6d7c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6d7c0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b6d888 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b6d888 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6d7c0 bytes 080100b5
+ 00b6d888 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0bce7d629f5be64a04d1635b263c8c8"></a>

### [`00b6d7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d7f0.md) → [`00b6d8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d8b8.md) _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b6d8e8",
      "incomplete_value": true,
      "site": "00b6d8e8",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d820",
      "incomplete_value": true,
      "site": "00b6d820",
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
            "const:918:8"
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
      "definition_site": "00b6d8cc",
      "incomplete_value": true,
      "site": "00b6d8cc",
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
      "definition_site": "00b6d804",
      "incomplete_value": true,
      "site": "00b6d804",
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
      "definition_site": "00b6d8d4",
      "incomplete_value": false,
      "site": "00b6d8e0",
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
            "const:96e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d80c",
      "incomplete_value": false,
      "site": "00b6d818",
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
            "const:8e1:8"
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
      "00b6d8c8",
      "READ",
      [
        "storage",
        "010a1918",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d8d4",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ],
    [
      "00b6d8e8",
      "WRITE",
      [
        "storage",
        "010a1918",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6d8c8",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d8d4",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ],
    [
      "00b6d8e8",
      "WRITE",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d7f0.md#insn-00b6d818) · [`00b6d820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d7f0.md#insn-00b6d820) · [`00b6d800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d7f0.md#insn-00b6d800)
- 新版 [`00b6d8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d8b8.md#insn-00b6d8e0) · [`00b6d8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d8b8.md#insn-00b6d8e8) · [`00b6d8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d8b8.md#insn-00b6d8c8)

~~~diff
- 00b6d818 ["INT_ADD", "register:40f0:8", ["const:b6d818:8", "const:4:8"]]
- 00b6d818 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6d8e0 ["INT_ADD", "register:40f0:8", ["const:b6d8e0:8", "const:4:8"]]
+ 00b6d8e0 ["CALL", null, ["callee:00bde040:8"]]
- 00b6d818 bytes dec10194
+ 00b6d8e0 bytes d8c10194
- 00b6d820 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:918:8"]]
- 00b6d820 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6d8e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b6d8e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d820 bytes 608e04f9
+ 00b6d8e8 bytes 60ee04f9
- 00b6d800 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:918:8"]]
- 00b6d800 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d8c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d8:8"]]
+ 00b6d8c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6d800 bytes 688e44f9
+ 00b6d8c8 bytes 68ee44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ad40b177c8987710786242f6b6731ef"></a>

### [`00b6d840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d840.md) → [`00b6d908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d908.md) _ZN8firebase4auth4user15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b6d960",
      "incomplete_value": true,
      "site": "00b6d960",
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
            "const:9e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d898",
      "incomplete_value": true,
      "site": "00b6d898",
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
            "const:920:8"
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
      "definition_site": "00b6d93c",
      "incomplete_value": true,
      "site": "00b6d948",
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
                "const:9d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6d874",
      "incomplete_value": true,
      "site": "00b6d880",
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
                "const:918:8"
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
      "00b6d91c",
      "READ",
      [
        "storage",
        "010a1920",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d93c",
      "READ",
      [
        "storage",
        "010a1918",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d960",
      "WRITE",
      [
        "storage",
        "010a1920",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6d91c",
      "READ",
      [
        "storage",
        "010a19e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6d93c",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6d960",
      "WRITE",
      [
        "storage",
        "010a19e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d840.md#insn-00b6d880) · [`00b6d898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d840.md#insn-00b6d898) · [`00b6d854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d840.md#insn-00b6d854)
- 新版 [`00b6d948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d908.md#insn-00b6d948) · [`00b6d960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d908.md#insn-00b6d960) · [`00b6d91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d908.md#insn-00b6d91c)

~~~diff
- 00b6d880 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6d880 ["INT_ADD", "register:40f0:8", ["const:b6d880:8", "const:4:8"]]
- 00b6d880 ["CALLIND", null, ["register:0:8"]]
+ 00b6d948 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6d948 ["INT_ADD", "register:40f0:8", ["const:b6d948:8", "const:4:8"]]
+ 00b6d948 ["CALLIND", null, ["register:0:8"]]
- 00b6d880 bytes 00013fd6
+ 00b6d948 bytes 00013fd6
- 00b6d898 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6d898 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:920:8"]]
- 00b6d898 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6d960 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6d960 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9e0:8"]]
+ 00b6d960 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6d898 bytes a0822439
+ 00b6d960 bytes a0822739
- 00b6d854 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:920:8"]]
- 00b6d854 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6d854 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6d91c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9e0:8"]]
+ 00b6d91c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6d91c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6d854 bytes a8826439
+ 00b6d91c bytes a8826739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adeba59ef80ffab3f9a13572f93a0701"></a>

### [`00b6d91c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d91c.md) → [`00b6d9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d9e4.md) _ZN8firebase4auth4user14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "site": "00b6d95c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6da24"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d938"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d930",
      "READ",
      [
        "storage",
        "010a1918",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6d938",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6da28"
      ]
    ],
    [
      "unmatched:00b6d940",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6d9f8",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6da00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6da28"
      ]
    ],
    [
      "00b6da08",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d91c.md#insn-00b6d938) · [`00b6d954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d91c.md#insn-00b6d954) · [`00b6d95c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d91c.md#insn-00b6d95c)
- 新版 [`00b6da1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6d9e4.md#insn-00b6da1c)

~~~diff
- 00b6d938 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d938 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6d938 bytes 410100b5
- 00b6d954 ["INT_ADD", "register:40f0:8", ["const:b6d954:8", "const:4:8"]]
- 00b6d954 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6da1c ["INT_ADD", "register:40f0:8", ["const:b6da1c:8", "const:4:8"]]
+ 00b6da1c ["CALL", null, ["callee:00bde040:8"]]
- 00b6d954 bytes 8fc10194
+ 00b6da1c bytes 89c10194
- 00b6d95c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:918:8"]]
- 00b6d95c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6d95c bytes 808e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f596883edc8c96dd351dd5506e9ca70"></a>

### [`00b6d9c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d9c8.md) → [`00b6da90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6da90.md) _ZN8firebase4auth4user13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00b6da08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6dad0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6d9e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6d9dc",
      "READ",
      [
        "storage",
        "010a1918",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6d9e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6dad4"
      ]
    ],
    [
      "unmatched:00b6d9ec",
      "PARAM",
      [
        "storage",
        "002998e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6daa4",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6daac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6dad4"
      ]
    ],
    [
      "00b6dab4",
      "PARAM",
      [
        "storage",
        "0029996e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6d9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d9c8.md#insn-00b6d9e4) · [`00b6da00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d9c8.md#insn-00b6da00) · [`00b6da08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6d9c8.md#insn-00b6da08)
- 新版 [`00b6dac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6da90.md#insn-00b6dac8)

~~~diff
- 00b6d9e4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6d9e4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6d9e4 bytes 410100b5
- 00b6da00 ["INT_ADD", "register:40f0:8", ["const:b6da00:8", "const:4:8"]]
- 00b6da00 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6dac8 ["INT_ADD", "register:40f0:8", ["const:b6dac8:8", "const:4:8"]]
+ 00b6dac8 ["CALL", null, ["callee:00bde040:8"]]
- 00b6da00 bytes 64c10194
+ 00b6dac8 bytes 5ec10194
- 00b6da08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:918:8"]]
- 00b6da08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6da08 bytes 808e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5913090584f36bbd3f2dc21f5c3c2ebe"></a>

### [`00b6dab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dab4.md) → [`00b6db7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db7c.md) _ZN8firebase4auth8userinfo19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

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
      "site": "00b6dae0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6dba8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6db90",
      "incomplete_value": true,
      "site": "00b6db90",
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
      "definition_site": "00b6dac8",
      "incomplete_value": true,
      "site": "00b6dac8",
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
      "00b6db8c",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6dad0",
      "PARAM",
      [
        "storage",
        "002a0fd8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6dad8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b6db8c",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6db98",
      "PARAM",
      [
        "storage",
        "002a1065",
        null,
        "string"
      ]
    ],
    [
      "00b6dba0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dab4.md#insn-00b6dad8) · [`00b6dae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dab4.md#insn-00b6dae0)
- 新版 [`00b6dba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6db7c.md#insn-00b6dba0)

~~~diff
- 00b6dad8 ["INT_ADD", "register:40f0:8", ["const:b6dad8:8", "const:4:8"]]
- 00b6dad8 ["CALL", null, ["callee:00bde040:8"]]
- 00b6dad8 bytes 2ec10194
- 00b6dae0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b6dae0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dae0 bytes 60d604f9
+ 00b6dba0 ["INT_ADD", "register:40f0:8", ["const:b6dba0:8", "const:4:8"]]
+ 00b6dba0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6dba0 bytes 28c10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85b8f659da47039c15486e4bc768a2c3"></a>

### [`00b6daf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6daf4.md) → [`00b6dbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dbbc.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

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
      "site": "00b6daf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6daf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6daf8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6daf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6daf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6dbcc",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6dbbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6dbc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6dbcc",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6daf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6daf4.md#insn-00b6daf4) · [`00b6daf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6daf4.md#insn-00b6daf8) · [`00b6db08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6daf4.md#insn-00b6db08)
- 新版 [`00b6dbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dbbc.md#insn-00b6dbd0)

~~~diff
- 00b6daf4 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b6daf4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6daf4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6daf4 bytes f30f1ef8
- 00b6daf8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6daf8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6daf8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6daf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6daf8 bytes fd7b01a9
- 00b6db08 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6db08 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b6dbd0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b6dbd0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6db08 bytes 080100b5
+ 00b6dbd0 bytes 080100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9920d8189e0a4ff2ebb063c4bfb4460d"></a>

### [`00b6db38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6db38.md) → [`00b6dc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc00.md) _ZN8firebase4auth8userinfo10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b6db68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6dc30"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6dc14",
      "incomplete_value": true,
      "site": "00b6dc14",
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
      "definition_site": "00b6db4c",
      "incomplete_value": true,
      "site": "00b6db4c",
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
      "00b6dc10",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dc14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6db6c"
      ]
    ],
    [
      "unmatched:00b6db54",
      "PARAM",
      [
        "storage",
        "002a0fd8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6dc10",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dc14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6dc34"
      ]
    ],
    [
      "00b6dc1c",
      "PARAM",
      [
        "storage",
        "002a1065",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6db60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6db38.md#insn-00b6db60) · [`00b6db68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6db38.md#insn-00b6db68) · [`00b6db78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6db38.md#insn-00b6db78)
- 新版 [`00b6dc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dc00.md#insn-00b6dc28)

~~~diff
- 00b6db60 ["INT_ADD", "register:40f0:8", ["const:b6db60:8", "const:4:8"]]
- 00b6db60 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6dc28 ["INT_ADD", "register:40f0:8", ["const:b6dc28:8", "const:4:8"]]
+ 00b6dc28 ["CALL", null, ["callee:00bde040:8"]]
- 00b6db60 bytes 0cc10194
+ 00b6dc28 bytes 06c10194
- 00b6db68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b6db68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6db68 bytes 60d604f9
- 00b6db78 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6db78 ["RETURN", null, ["register:0:8"]]
- 00b6db78 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac83b75dbe0d5eb9890714a839ec9bb2"></a>

### [`00b6dbf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dbf4.md) → [`00b6dcbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dcbc.md) _ZN8firebase4auth8userinfo12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b6dcf8",
      "incomplete_value": true,
      "site": "00b6dcf8",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc30",
      "incomplete_value": true,
      "site": "00b6dc30",
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
            "const:9b0:8"
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
      "definition_site": "00b6dd18",
      "incomplete_value": true,
      "site": "00b6dd18",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dc50",
      "incomplete_value": true,
      "site": "00b6dc50",
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
            "const:9a8:8"
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
      "definition_site": "00b6dcd4",
      "incomplete_value": true,
      "site": "00b6dcd4",
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
      "definition_site": "00b6dc0c",
      "incomplete_value": true,
      "site": "00b6dc0c",
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
      "00b6dcd0",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dcdc",
      "READ",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6dcf8",
      "WRITE",
      [
        "storage",
        "010a19b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6dcd0",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dcdc",
      "READ",
      [
        "storage",
        "010a1a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6dcf8",
      "WRITE",
      [
        "storage",
        "010a1a70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dbf4.md#insn-00b6dc30) · [`00b6dc4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dbf4.md#insn-00b6dc4c) · [`00b6dc50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dbf4.md#insn-00b6dc50)
- 新版 [`00b6dcf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dcbc.md#insn-00b6dcf8) · [`00b6dd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dcbc.md#insn-00b6dd14) · [`00b6dd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dcbc.md#insn-00b6dd18)

~~~diff
- 00b6dc30 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6dc30 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6dc30 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b0:8"]]
- 00b6dc30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6dcf8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6dcf8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6dcf8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a70:8"]]
+ 00b6dcf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6dc30 bytes bfc22639
+ 00b6dcf8 bytes bfc22939
- 00b6dc4c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6dc4c ["INT_ADD", "register:40f0:8", ["const:b6dc4c:8", "const:4:8"]]
- 00b6dc4c ["CALLIND", null, ["register:0:8"]]
+ 00b6dd14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6dd14 ["INT_ADD", "register:40f0:8", ["const:b6dd14:8", "const:4:8"]]
+ 00b6dd14 ["CALLIND", null, ["register:0:8"]]
- 00b6dc4c bytes 00013fd6
+ 00b6dd14 bytes 00013fd6
- 00b6dc50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b6dc50 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6dc50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b6dd18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
+ 00b6dd18 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b6dd18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6dc50 bytes 9fd604f9
+ 00b6dd18 bytes 9f3605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db1621acf17bb36c7c663595d02261c2"></a>

### [`00b6dc64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dc64.md) → [`00b6dd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd2c.md) _ZN8firebase4auth8userinfo14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6dca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6dd6c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6dd48",
      "incomplete_value": true,
      "site": "00b6dd48",
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
      "definition_site": "00b6dc80",
      "incomplete_value": true,
      "site": "00b6dc80",
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
      "00b6dd40",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dd50",
      "PARAM",
      [
        "storage",
        "002a0fd8",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6dca4",
      "WRITE",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6dd40",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dd50",
      "PARAM",
      [
        "storage",
        "002a1065",
        null,
        "string"
      ]
    ],
    [
      "00b6dd6c",
      "WRITE",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dc9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dc64.md#insn-00b6dc9c) · [`00b6dca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dc64.md#insn-00b6dca4)
- 新版 [`00b6dd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd2c.md#insn-00b6dd64) · [`00b6dd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dd2c.md#insn-00b6dd6c)

~~~diff
- 00b6dc9c ["INT_ADD", "register:40f0:8", ["const:b6dc9c:8", "const:4:8"]]
- 00b6dc9c ["CALL", null, ["callee:00bde040:8"]]
+ 00b6dd64 ["INT_ADD", "register:40f0:8", ["const:b6dd64:8", "const:4:8"]]
+ 00b6dd64 ["CALL", null, ["callee:00bde040:8"]]
- 00b6dc9c bytes bdc00194
+ 00b6dd64 bytes b7c00194
- 00b6dca4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b6dca4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dca4 bytes 80d604f9
+ 00b6dd6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
+ 00b6dd6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6dd6c bytes 803605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6410b4e408ed4a16320f18e508647e7"></a>

### [`00b6dd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dd10.md) → [`00b6ddd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6ddd8.md) _ZN8firebase4auth8userinfo13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00b6dd50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6de18"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6dd2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6dd24",
      "READ",
      [
        "storage",
        "010a19a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6dd2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6de1c"
      ]
    ],
    [
      "unmatched:00b6dd34",
      "PARAM",
      [
        "storage",
        "002a0fd8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6ddec",
      "READ",
      [
        "storage",
        "010a1a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6ddf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6de1c"
      ]
    ],
    [
      "00b6ddfc",
      "PARAM",
      [
        "storage",
        "002a1065",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dd2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dd10.md#insn-00b6dd2c) · [`00b6dd48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dd10.md#insn-00b6dd48) · [`00b6dd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dd10.md#insn-00b6dd50)
- 新版 [`00b6de10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6ddd8.md#insn-00b6de10)

~~~diff
- 00b6dd2c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6dd2c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6dd2c bytes 410100b5
- 00b6dd48 ["INT_ADD", "register:40f0:8", ["const:b6dd48:8", "const:4:8"]]
- 00b6dd48 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6de10 ["INT_ADD", "register:40f0:8", ["const:b6de10:8", "const:4:8"]]
+ 00b6de10 ["CALL", null, ["callee:00bde040:8"]]
- 00b6dd48 bytes 92c00194
+ 00b6de10 bytes 8cc00194
- 00b6dd50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b6dd50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dd50 bytes 80d604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24caa9af633e0a254bee50e64a4a930d"></a>

### [`00b6ddbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ddbc.md) → [`00b6de84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de84.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

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
      "site": "00b6ddbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ddc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ddc0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6ddbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6ddc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6de94",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6de84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6de88",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b6de94",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ddbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ddbc.md#insn-00b6ddbc) · [`00b6ddc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ddbc.md#insn-00b6ddc0) · [`00b6ddd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ddbc.md#insn-00b6ddd0)
- 新版 [`00b6de98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de84.md#insn-00b6de98)

~~~diff
- 00b6ddbc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b6ddbc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6ddbc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6ddbc bytes f30f1ef8
- 00b6ddc0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6ddc0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6ddc0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6ddc0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6ddc0 bytes fd7b01a9
- 00b6ddd0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6ddd0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b6de98 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b6de98 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6ddd0 bytes e80000b5
+ 00b6de98 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7ca8e1beb4f500cd906328435ef304f"></a>

### [`00b6ddfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ddfc.md) → [`00b6dec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dec4.md) _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

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
      "site": "00b6de28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6def0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6ded8",
      "incomplete_value": true,
      "site": "00b6ded8",
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
      "definition_site": "00b6de10",
      "incomplete_value": true,
      "site": "00b6de10",
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
      "00b6ded4",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6de18",
      "PARAM",
      [
        "storage",
        "002ad650",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6de20",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00b6ded4",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dee0",
      "PARAM",
      [
        "storage",
        "002ad647",
        null,
        "string"
      ]
    ],
    [
      "00b6dee8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6de10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ddfc.md#insn-00b6de10) · [`00b6de20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ddfc.md#insn-00b6de20) · [`00b6de28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ddfc.md#insn-00b6de28)
- 新版 [`00b6ded8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6dec4.md#insn-00b6ded8)

~~~diff
- 00b6de10 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6de10 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b6ded8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b6ded8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6de10 bytes e80000b5
+ 00b6ded8 bytes e80000b5
- 00b6de20 ["INT_ADD", "register:40f0:8", ["const:b6de20:8", "const:4:8"]]
- 00b6de20 ["CALL", null, ["callee:00bde040:8"]]
- 00b6de20 bytes 5cc00194
- 00b6de28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
- 00b6de28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6de28 bytes 60fe04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebff15756d0b3c2565086f77cd460c40"></a>

### [`00b6de3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6de3c.md) → [`00b6df04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df04.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b6df34",
      "incomplete_value": true,
      "site": "00b6df34",
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
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6de6c",
      "incomplete_value": true,
      "site": "00b6de6c",
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
            "const:9f8:8"
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
      "definition_site": "00b6df18",
      "incomplete_value": true,
      "site": "00b6df18",
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
      "definition_site": "00b6de50",
      "incomplete_value": true,
      "site": "00b6de50",
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
      "definition_site": "00b6df24",
      "incomplete_value": false,
      "site": "00b6df2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:647:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6de5c",
      "incomplete_value": false,
      "site": "00b6de64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:650:8"
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
      "00b6df14",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6df24",
      "PARAM",
      [
        "storage",
        "002ad650",
        null,
        "string"
      ]
    ],
    [
      "00b6df34",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6df14",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6df24",
      "PARAM",
      [
        "storage",
        "002ad647",
        null,
        "string"
      ]
    ],
    [
      "00b6df34",
      "WRITE",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6de64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6de3c.md#insn-00b6de64) · [`00b6de6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6de3c.md#insn-00b6de6c) · [`00b6de4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6de3c.md#insn-00b6de4c)
- 新版 [`00b6df2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df04.md#insn-00b6df2c) · [`00b6df34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df04.md#insn-00b6df34) · [`00b6df14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df04.md#insn-00b6df14)

~~~diff
- 00b6de64 ["INT_ADD", "register:40f0:8", ["const:b6de64:8", "const:4:8"]]
- 00b6de64 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6df2c ["INT_ADD", "register:40f0:8", ["const:b6df2c:8", "const:4:8"]]
+ 00b6df2c ["CALL", null, ["callee:00bde040:8"]]
- 00b6de64 bytes 4bc00194
+ 00b6df2c bytes 45c00194
- 00b6de6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
- 00b6de6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6df34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
+ 00b6df34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6de6c bytes 60fe04f9
+ 00b6df34 bytes 605e05f9
- 00b6de4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
- 00b6de4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6df14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
+ 00b6df14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6de4c bytes 68fe44f9
+ 00b6df14 bytes 685e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55ca86d48a1e8db3d6721ff66e3aa901"></a>

### [`00b6de80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6de80.md) → [`00b6df48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df48.md) _ZN8firebase4auth8metadata10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b6df78",
      "incomplete_value": true,
      "site": "00b6df78",
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
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6deb0",
      "incomplete_value": true,
      "site": "00b6deb0",
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
            "const:9f8:8"
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
      "definition_site": "00b6df5c",
      "incomplete_value": true,
      "site": "00b6df5c",
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
      "definition_site": "00b6de94",
      "incomplete_value": true,
      "site": "00b6de94",
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
      "definition_site": "00b6df64",
      "incomplete_value": false,
      "site": "00b6df70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:647:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6de9c",
      "incomplete_value": false,
      "site": "00b6dea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:650:8"
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
      "00b6df58",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6df64",
      "PARAM",
      [
        "storage",
        "002ad650",
        null,
        "string"
      ]
    ],
    [
      "00b6df78",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6df58",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6df64",
      "PARAM",
      [
        "storage",
        "002ad647",
        null,
        "string"
      ]
    ],
    [
      "00b6df78",
      "WRITE",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6de80.md#insn-00b6dea8) · [`00b6deb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6de80.md#insn-00b6deb0) · [`00b6de90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6de80.md#insn-00b6de90)
- 新版 [`00b6df70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df48.md#insn-00b6df70) · [`00b6df78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df48.md#insn-00b6df78) · [`00b6df58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df48.md#insn-00b6df58)

~~~diff
- 00b6dea8 ["INT_ADD", "register:40f0:8", ["const:b6dea8:8", "const:4:8"]]
- 00b6dea8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6df70 ["INT_ADD", "register:40f0:8", ["const:b6df70:8", "const:4:8"]]
+ 00b6df70 ["CALL", null, ["callee:00bde040:8"]]
- 00b6dea8 bytes 3ac00194
+ 00b6df70 bytes 34c00194
- 00b6deb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
- 00b6deb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6df78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
+ 00b6df78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6deb0 bytes 60fe04f9
+ 00b6df78 bytes 605e05f9
- 00b6de90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f8:8"]]
- 00b6de90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6df58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
+ 00b6df58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6de90 bytes 68fe44f9
+ 00b6df58 bytes 685e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad986a9e7a9fe9200409abaced83e761"></a>

### [`00b6ded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ded0.md) → [`00b6df98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df98.md) _ZN8firebase4auth8metadata15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b6dff0",
      "incomplete_value": true,
      "site": "00b6dff0",
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
            "const:ac0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df28",
      "incomplete_value": true,
      "site": "00b6df28",
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
            "const:a00:8"
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
      "definition_site": "00b6dfcc",
      "incomplete_value": true,
      "site": "00b6dfd8",
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6df04",
      "incomplete_value": true,
      "site": "00b6df10",
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
                "const:9f8:8"
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
      "00b6dfac",
      "READ",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6dfcc",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dff0",
      "WRITE",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6dfac",
      "READ",
      [
        "storage",
        "010a1ac0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6dfcc",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6dff0",
      "WRITE",
      [
        "storage",
        "010a1ac0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6df10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ded0.md#insn-00b6df10) · [`00b6df28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ded0.md#insn-00b6df28) · [`00b6dee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6ded0.md#insn-00b6dee4)
- 新版 [`00b6dfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df98.md#insn-00b6dfd8) · [`00b6dff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df98.md#insn-00b6dff0) · [`00b6dfac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6df98.md#insn-00b6dfac)

~~~diff
- 00b6df10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6df10 ["INT_ADD", "register:40f0:8", ["const:b6df10:8", "const:4:8"]]
- 00b6df10 ["CALLIND", null, ["register:0:8"]]
+ 00b6dfd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6dfd8 ["INT_ADD", "register:40f0:8", ["const:b6dfd8:8", "const:4:8"]]
+ 00b6dfd8 ["CALLIND", null, ["register:0:8"]]
- 00b6df10 bytes 00013fd6
+ 00b6dfd8 bytes 00013fd6
- 00b6df28 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6df28 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a00:8"]]
- 00b6df28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6dff0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6dff0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ac0:8"]]
+ 00b6dff0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6df28 bytes a0022839
+ 00b6dff0 bytes a0022b39
- 00b6dee4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a00:8"]]
- 00b6dee4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b6dee4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6dfac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ac0:8"]]
+ 00b6dfac ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6dfac ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b6dee4 bytes a8026839
+ 00b6dfac bytes a8026b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd0d47b20ad13834e03fca01a784aa16"></a>

### [`00b6df3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6df3c.md) → [`00b6e004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e004.md) _ZN8firebase4auth8metadata12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 16.67% / 新版 14.29%

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
      "site": "00b6df78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6df98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6e040"
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
      "00b6e018",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e01c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6df9c"
      ]
    ],
    [
      "00b6e024",
      "READ",
      [
        "storage",
        "010a1a00",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6e018",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e01c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e064"
      ]
    ],
    [
      "00b6e024",
      "READ",
      [
        "storage",
        "010a1ac0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6df78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6df3c.md#insn-00b6df78) · [`00b6df80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6df3c.md#insn-00b6df80) · [`00b6df94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6df3c.md#insn-00b6df94)

~~~diff
- 00b6df78 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6df78 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6df78 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a00:8"]]
- 00b6df78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6df78 bytes bf022839
- 00b6df80 ["INT_ADD", "register:40f0:8", ["const:b6df80:8", "const:4:8"]]
- 00b6df80 ["CALL", null, ["callee:00bde090:8"]]
- 00b6df80 bytes 18c00194
- 00b6df94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6df94 ["INT_ADD", "register:40f0:8", ["const:b6df94:8", "const:4:8"]]
- 00b6df94 ["CALLIND", null, ["register:0:8"]]
- 00b6df94 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63cfbcaa0ce3526331e4df64da0eed3e"></a>

### [`00b6dfac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dfac.md) → [`00b6e074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e074.md) _ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b6e0b4",
      "incomplete_value": true,
      "site": "00b6e0b4",
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
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dfec",
      "incomplete_value": true,
      "site": "00b6dfec",
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
            "const:9f8:8"
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
      "definition_site": "00b6e090",
      "incomplete_value": true,
      "site": "00b6e090",
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
      "definition_site": "00b6dfc8",
      "incomplete_value": true,
      "site": "00b6dfc8",
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
      "definition_site": "00b6e098",
      "incomplete_value": false,
      "site": "00b6e0ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:647:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6dfd0",
      "incomplete_value": false,
      "site": "00b6dfe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:650:8"
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
      "00b6e088",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e098",
      "PARAM",
      [
        "storage",
        "002ad650",
        null,
        "string"
      ]
    ],
    [
      "00b6e0b4",
      "WRITE",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e088",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e098",
      "PARAM",
      [
        "storage",
        "002ad647",
        null,
        "string"
      ]
    ],
    [
      "00b6e0b4",
      "WRITE",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6dfe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dfac.md#insn-00b6dfe4) · [`00b6dfec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dfac.md#insn-00b6dfec) · [`00b6dfc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6d/00b6dfac.md#insn-00b6dfc0)
- 新版 [`00b6e0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e074.md#insn-00b6e0ac) · [`00b6e0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e074.md#insn-00b6e0b4) · [`00b6e088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e074.md#insn-00b6e088)

~~~diff
- 00b6dfe4 ["INT_ADD", "register:40f0:8", ["const:b6dfe4:8", "const:4:8"]]
- 00b6dfe4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6e0ac ["INT_ADD", "register:40f0:8", ["const:b6e0ac:8", "const:4:8"]]
+ 00b6e0ac ["CALL", null, ["callee:00bde040:8"]]
- 00b6dfe4 bytes ebbf0194
+ 00b6e0ac bytes e5bf0194
- 00b6dfec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
- 00b6dfec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e0b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ab8:8"]]
+ 00b6e0b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6dfec bytes 80fe04f9
+ 00b6e0b4 bytes 805e05f9
- 00b6dfc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
- 00b6dfc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e088 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ab8:8"]]
+ 00b6e088 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6dfc0 bytes 81fe44f9
+ 00b6e088 bytes 815e45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6b5332e6544f0a3de6ca5d53cd343a6"></a>

### [`00b6e01c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e01c.md) → [`00b6e0e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e0e4.md) _ZN8firebase4auth8metadata11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b6e100",
      "incomplete_value": false,
      "site": "00b6e104",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e038",
      "incomplete_value": false,
      "site": "00b6e03c",
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
      "definition_site": "00b6e110",
      "incomplete_value": true,
      "site": "00b6e11c",
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
      "definition_site": "00b6e048",
      "incomplete_value": true,
      "site": "00b6e054",
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
      "00b6e100",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6e110",
      "DATA",
      [
        "storage",
        "010a1a08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e100",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6e110",
      "DATA",
      [
        "storage",
        "010a1ac8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e03c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e01c.md#insn-00b6e03c) · [`00b6e038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e01c.md#insn-00b6e038) · [`00b6e044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e01c.md#insn-00b6e044)
- 新版 [`00b6e104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e0e4.md#insn-00b6e104) · [`00b6e100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e0e4.md#insn-00b6e100) · [`00b6e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e0e4.md#insn-00b6e10c)

~~~diff
- 00b6e03c ["INT_ADD", "register:40f0:8", ["const:b6e03c:8", "const:4:8"]]
- 00b6e03c ["CALL", null, ["callee:00bde130:8"]]
+ 00b6e104 ["INT_ADD", "register:40f0:8", ["const:b6e104:8", "const:4:8"]]
+ 00b6e104 ["CALL", null, ["callee:00bde130:8"]]
- 00b6e03c bytes 11c00194
+ 00b6e104 bytes 0bc00194
- 00b6e038 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b6e038 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e038 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e038 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6e100 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b6e100 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e100 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e100 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6e038 bytes 001c1591
+ 00b6e100 bytes 00501791
- 00b6e044 ["COPY", "tmp:0:8", ["const:a08:8"]]
- 00b6e044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6e10c ["COPY", "tmp:0:8", ["const:ac8:8"]]
+ 00b6e10c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e10c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e10c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6e044 bytes 08212891
+ 00b6e10c bytes 08212b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8804497072be9b7c664efcb70a0a52cf"></a>

### [`00b6e058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e058.md) → [`00b6e120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e120.md) _ZN8firebase4auth8metadata13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00b6e098"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6e160"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e074"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6e06c",
      "READ",
      [
        "storage",
        "010a19f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6e074",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e164"
      ]
    ],
    [
      "unmatched:00b6e07c",
      "PARAM",
      [
        "storage",
        "002ad650",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6e134",
      "READ",
      [
        "storage",
        "010a1ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e13c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e164"
      ]
    ],
    [
      "00b6e144",
      "PARAM",
      [
        "storage",
        "002ad647",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e058.md#insn-00b6e074) · [`00b6e090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e058.md#insn-00b6e090) · [`00b6e098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e058.md#insn-00b6e098)
- 新版 [`00b6e158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e120.md#insn-00b6e158)

~~~diff
- 00b6e074 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6e074 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6e074 bytes 410100b5
- 00b6e090 ["INT_ADD", "register:40f0:8", ["const:b6e090:8", "const:4:8"]]
- 00b6e090 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6e158 ["INT_ADD", "register:40f0:8", ["const:b6e158:8", "const:4:8"]]
+ 00b6e158 ["CALL", null, ["callee:00bde040:8"]]
- 00b6e090 bytes c0bf0194
+ 00b6e158 bytes babf0194
- 00b6e098 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f8:8"]]
- 00b6e098 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e098 bytes 80fe04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a05737699be37efbab8019b1e896d581"></a>

### [`00b6e104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e104.md) → [`00b6e1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e1cc.md) _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b6e1f8",
      "incomplete_value": true,
      "site": "00b6e1f8",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e130",
      "incomplete_value": true,
      "site": "00b6e130",
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
            "const:a20:8"
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
      "definition_site": "00b6e1e0",
      "incomplete_value": true,
      "site": "00b6e1e0",
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
      "definition_site": "00b6e118",
      "incomplete_value": true,
      "site": "00b6e118",
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
      "definition_site": "00b6e1ec",
      "incomplete_value": false,
      "site": "00b6e1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:133:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e124",
      "incomplete_value": false,
      "site": "00b6e128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:a6:8"
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
      "00b6e1dc",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e1ec",
      "PARAM",
      [
        "storage",
        "0029d0a6",
        null,
        "string"
      ]
    ],
    [
      "00b6e1f8",
      "WRITE",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e1dc",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e1ec",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ],
    [
      "00b6e1f8",
      "WRITE",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e104.md#insn-00b6e128) · [`00b6e130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e104.md#insn-00b6e130) · [`00b6e114`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e104.md#insn-00b6e114)
- 新版 [`00b6e1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e1cc.md#insn-00b6e1f0) · [`00b6e1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e1cc.md#insn-00b6e1f8) · [`00b6e1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e1cc.md#insn-00b6e1dc)

~~~diff
- 00b6e128 ["INT_ADD", "register:40f0:8", ["const:b6e128:8", "const:4:8"]]
- 00b6e128 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6e1f0 ["INT_ADD", "register:40f0:8", ["const:b6e1f0:8", "const:4:8"]]
+ 00b6e1f0 ["CALL", null, ["callee:00bde040:8"]]
- 00b6e128 bytes 9abf0194
+ 00b6e1f0 bytes 94bf0194
- 00b6e130 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00b6e130 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e1f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
+ 00b6e1f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e130 bytes 601205f9
+ 00b6e1f8 bytes 607205f9
- 00b6e114 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00b6e114 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e1dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
+ 00b6e1dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e114 bytes 681245f9
+ 00b6e1dc bytes 687245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2075cfab2922a0595bfbed401635556"></a>

### [`00b6e144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e144.md) → [`00b6e20c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e20c.md) _ZN8firebase4auth18userprofilebuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b6e170"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6e238"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e220",
      "incomplete_value": true,
      "site": "00b6e220",
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
      "definition_site": "00b6e158",
      "incomplete_value": true,
      "site": "00b6e158",
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
      "00b6e21c",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e220",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e174"
      ]
    ],
    [
      "unmatched:00b6e160",
      "PARAM",
      [
        "storage",
        "0029d0a6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6e21c",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e220",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e23c"
      ]
    ],
    [
      "00b6e228",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e144.md#insn-00b6e168) · [`00b6e170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e144.md#insn-00b6e170) · [`00b6e180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e144.md#insn-00b6e180)

~~~diff
- 00b6e168 ["INT_ADD", "register:40f0:8", ["const:b6e168:8", "const:4:8"]]
- 00b6e168 ["CALL", null, ["callee:00bde040:8"]]
- 00b6e168 bytes 8abf0194
- 00b6e170 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00b6e170 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e170 bytes 601205f9
- 00b6e180 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6e180 ["RETURN", null, ["register:0:8"]]
- 00b6e180 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c32f66ad1496f82c7127b8d963a426ea"></a>

### [`00b6e184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e184.md) → [`00b6e24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e24c.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "site": "00b6e1b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6e27c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e260",
      "incomplete_value": true,
      "site": "00b6e260",
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
      "definition_site": "00b6e198",
      "incomplete_value": true,
      "site": "00b6e198",
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
      "00b6e25c",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e260",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e1b8"
      ]
    ],
    [
      "unmatched:00b6e1a4",
      "PARAM",
      [
        "storage",
        "0029d0a6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6e25c",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e260",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e280"
      ]
    ],
    [
      "00b6e26c",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e184.md#insn-00b6e1ac) · [`00b6e1b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e184.md#insn-00b6e1b4) · [`00b6e1c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e184.md#insn-00b6e1c4)

~~~diff
- 00b6e1ac ["INT_ADD", "register:40f0:8", ["const:b6e1ac:8", "const:4:8"]]
- 00b6e1ac ["CALL", null, ["callee:00bde040:8"]]
- 00b6e1ac bytes 79bf0194
- 00b6e1b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00b6e1b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e1b4 bytes 601205f9
- 00b6e1c4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6e1c4 ["RETURN", null, ["register:0:8"]]
- 00b6e1c4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5ec1b7c3a5b8cb1e3c6c2dd027a6dfc"></a>

### [`00b6e1c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e1c8.md) → [`00b6e290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e290.md) _ZN8firebase4auth18userprofilebuilder10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b6e2c0",
      "incomplete_value": true,
      "site": "00b6e2c0",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e1f8",
      "incomplete_value": true,
      "site": "00b6e1f8",
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
            "const:a20:8"
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
      "definition_site": "00b6e2a4",
      "incomplete_value": true,
      "site": "00b6e2a4",
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
      "definition_site": "00b6e1dc",
      "incomplete_value": true,
      "site": "00b6e1dc",
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
      "definition_site": "00b6e2ac",
      "incomplete_value": false,
      "site": "00b6e2b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:133:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e1e4",
      "incomplete_value": false,
      "site": "00b6e1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:a6:8"
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
      "00b6e2a0",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e2ac",
      "PARAM",
      [
        "storage",
        "0029d0a6",
        null,
        "string"
      ]
    ],
    [
      "00b6e2c0",
      "WRITE",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e2a0",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e2ac",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ],
    [
      "00b6e2c0",
      "WRITE",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e1c8.md#insn-00b6e1f0) · [`00b6e1f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e1c8.md#insn-00b6e1f8) · [`00b6e1d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e1c8.md#insn-00b6e1d8)
- 新版 [`00b6e2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e290.md#insn-00b6e2b8) · [`00b6e2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e290.md#insn-00b6e2c0) · [`00b6e2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e290.md#insn-00b6e2a0)

~~~diff
- 00b6e1f0 ["INT_ADD", "register:40f0:8", ["const:b6e1f0:8", "const:4:8"]]
- 00b6e1f0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6e2b8 ["INT_ADD", "register:40f0:8", ["const:b6e2b8:8", "const:4:8"]]
+ 00b6e2b8 ["CALL", null, ["callee:00bde040:8"]]
- 00b6e1f0 bytes 68bf0194
+ 00b6e2b8 bytes 62bf0194
- 00b6e1f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00b6e1f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e2c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
+ 00b6e2c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e1f8 bytes 601205f9
+ 00b6e2c0 bytes 607205f9
- 00b6e1d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
- 00b6e1d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e2a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ae0:8"]]
+ 00b6e2a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e1d8 bytes 681245f9
+ 00b6e2a0 bytes 687245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f01935a00d0fcde4e1bfa03d504fd62"></a>

### [`00b6e218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e218.md) → [`00b6e2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e2e0.md) _ZN8firebase4auth18userprofilebuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call, call_argument_candidate, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b6e338",
      "incomplete_value": true,
      "site": "00b6e338",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e270",
      "incomplete_value": true,
      "site": "00b6e270",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e258"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6e260",
      "incomplete_value": true,
      "site": "00b6e264",
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
      "00b6e2f4",
      "READ",
      [
        "storage",
        "010a1a28",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b6e24c",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e338",
      "WRITE",
      [
        "storage",
        "010a1a28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6e2f4",
      "READ",
      [
        "storage",
        "010a1ae8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e314",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e338",
      "WRITE",
      [
        "storage",
        "010a1ae8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e218.md#insn-00b6e258) · [`00b6e264`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e218.md#insn-00b6e264) · [`00b6e270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e218.md#insn-00b6e270)
- 新版 [`00b6e32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e2e0.md#insn-00b6e32c) · [`00b6e338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e2e0.md#insn-00b6e338)

~~~diff
- 00b6e258 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e258 ["INT_ADD", "register:40f0:8", ["const:b6e258:8", "const:4:8"]]
- 00b6e258 ["CALLIND", null, ["register:0:8"]]
- 00b6e258 bytes 00013fd6
- 00b6e264 ["INT_ADD", "register:40f0:8", ["const:b6e264:8", "const:4:8"]]
- 00b6e264 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6e32c ["INT_ADD", "register:40f0:8", ["const:b6e32c:8", "const:4:8"]]
+ 00b6e32c ["CALL", null, ["callee:00bde090:8"]]
- 00b6e264 bytes 5fbf0194
+ 00b6e32c bytes 59bf0194
- 00b6e270 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6e270 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a28:8"]]
- 00b6e270 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b6e338 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b6e338 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ae8:8"]]
+ 00b6e338 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6e270 bytes a0a22839
+ 00b6e338 bytes a0a22b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-304eaac8b78ffadeb3366b2f3c24a8c0"></a>

### [`00b6e284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e284.md) → [`00b6e34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e34c.md) _ZN8firebase4auth18userprofilebuilder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b6e388",
      "incomplete_value": true,
      "site": "00b6e388",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e2c0",
      "incomplete_value": true,
      "site": "00b6e2c0",
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
            "const:a28:8"
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
      "definition_site": "00b6e3a8",
      "incomplete_value": true,
      "site": "00b6e3a8",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e2e0",
      "incomplete_value": true,
      "site": "00b6e2e0",
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
            "const:a20:8"
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
      "definition_site": "00b6e364",
      "incomplete_value": true,
      "site": "00b6e364",
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
      "definition_site": "00b6e29c",
      "incomplete_value": true,
      "site": "00b6e29c",
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
      "00b6e360",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e36c",
      "READ",
      [
        "storage",
        "010a1a28",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e388",
      "WRITE",
      [
        "storage",
        "010a1a28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6e360",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e36c",
      "READ",
      [
        "storage",
        "010a1ae8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6e388",
      "WRITE",
      [
        "storage",
        "010a1ae8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e284.md#insn-00b6e2c0) · [`00b6e2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e284.md#insn-00b6e2dc) · [`00b6e2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e284.md#insn-00b6e2e0)
- 新版 [`00b6e388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e34c.md#insn-00b6e388) · [`00b6e3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e34c.md#insn-00b6e3a4) · [`00b6e3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e34c.md#insn-00b6e3a8)

~~~diff
- 00b6e2c0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6e2c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6e2c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a28:8"]]
- 00b6e2c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b6e388 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b6e388 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b6e388 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ae8:8"]]
+ 00b6e388 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6e2c0 bytes bfa22839
+ 00b6e388 bytes bfa22b39
- 00b6e2dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6e2dc ["INT_ADD", "register:40f0:8", ["const:b6e2dc:8", "const:4:8"]]
- 00b6e2dc ["CALLIND", null, ["register:0:8"]]
+ 00b6e3a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6e3a4 ["INT_ADD", "register:40f0:8", ["const:b6e3a4:8", "const:4:8"]]
+ 00b6e3a4 ["CALLIND", null, ["register:0:8"]]
- 00b6e2dc bytes 00013fd6
+ 00b6e3a4 bytes 00013fd6
- 00b6e2e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
- 00b6e2e0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6e2e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b6e3a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae0:8"]]
+ 00b6e3a8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b6e3a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6e2e0 bytes 9f1205f9
+ 00b6e3a8 bytes 9f7205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e7f57e8bcc458ecf16e383b1ae9c75c"></a>

### [`00b6e2f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e2f4.md) → [`00b6e3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e3bc.md) _ZN8firebase4auth18userprofilebuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e334"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6e3fc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6e3d8",
      "incomplete_value": true,
      "site": "00b6e3d8",
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
      "definition_site": "00b6e310",
      "incomplete_value": true,
      "site": "00b6e310",
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
      "00b6e3d0",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e3e0",
      "PARAM",
      [
        "storage",
        "0029d0a6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b6e334",
      "WRITE",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e3d0",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e3e0",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ],
    [
      "00b6e3fc",
      "WRITE",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e32c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e2f4.md#insn-00b6e32c) · [`00b6e334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e2f4.md#insn-00b6e334)
- 新版 [`00b6e3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e3bc.md#insn-00b6e3f4) · [`00b6e3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e3bc.md#insn-00b6e3fc)

~~~diff
- 00b6e32c ["INT_ADD", "register:40f0:8", ["const:b6e32c:8", "const:4:8"]]
- 00b6e32c ["CALL", null, ["callee:00bde040:8"]]
+ 00b6e3f4 ["INT_ADD", "register:40f0:8", ["const:b6e3f4:8", "const:4:8"]]
+ 00b6e3f4 ["CALL", null, ["callee:00bde040:8"]]
- 00b6e32c bytes 19bf0194
+ 00b6e3f4 bytes 13bf0194
- 00b6e334 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
- 00b6e334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e334 bytes 801205f9
+ 00b6e3fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ae0:8"]]
+ 00b6e3fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6e3fc bytes 807205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0efdd5194774e6ee7b5c1ab75f8873a3"></a>

### [`00b6e364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e364.md) → [`00b6e42c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e42c.md) _ZN8firebase4auth18userprofilebuilder11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b6e448",
      "incomplete_value": false,
      "site": "00b6e44c",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e380",
      "incomplete_value": false,
      "site": "00b6e384",
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
      "definition_site": "00b6e458",
      "incomplete_value": true,
      "site": "00b6e464",
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
      "definition_site": "00b6e390",
      "incomplete_value": true,
      "site": "00b6e39c",
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
      "00b6e448",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b6e458",
      "DATA",
      [
        "storage",
        "010a1a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6e448",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b6e458",
      "DATA",
      [
        "storage",
        "010a1af0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e364.md#insn-00b6e384) · [`00b6e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e364.md#insn-00b6e380) · [`00b6e38c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e364.md#insn-00b6e38c)
- 新版 [`00b6e44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e42c.md#insn-00b6e44c) · [`00b6e448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e42c.md#insn-00b6e448) · [`00b6e454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e42c.md#insn-00b6e454)

~~~diff
- 00b6e384 ["INT_ADD", "register:40f0:8", ["const:b6e384:8", "const:4:8"]]
- 00b6e384 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6e44c ["INT_ADD", "register:40f0:8", ["const:b6e44c:8", "const:4:8"]]
+ 00b6e44c ["CALL", null, ["callee:00bde130:8"]]
- 00b6e384 bytes 3fbf0194
+ 00b6e44c bytes 39bf0194
- 00b6e380 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b6e380 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e380 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e380 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6e448 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b6e448 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e448 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e448 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6e380 bytes 001c1591
+ 00b6e448 bytes 00501791
- 00b6e38c ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00b6e38c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e38c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e38c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6e454 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00b6e454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6e38c bytes 08c12891
+ 00b6e454 bytes 08c12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ede08ec7dc0f9edf798abb82bca5a05"></a>

### [`00b6e3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e3a0.md) → [`00b6e468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e468.md) _ZN8firebase4auth18userprofilebuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00b6e3e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6e4a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e3bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6e3b4",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6e3bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e4ac"
      ]
    ],
    [
      "unmatched:00b6e3c4",
      "PARAM",
      [
        "storage",
        "0029d0a6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6e47c",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e484",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e4ac"
      ]
    ],
    [
      "00b6e48c",
      "PARAM",
      [
        "storage",
        "0029d133",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e3bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e3a0.md#insn-00b6e3bc) · [`00b6e3d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e3a0.md#insn-00b6e3d8) · [`00b6e3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e3a0.md#insn-00b6e3e0)
- 新版 [`00b6e4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e468.md#insn-00b6e4a0)

~~~diff
- 00b6e3bc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6e3bc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6e3bc bytes 410100b5
- 00b6e3d8 ["INT_ADD", "register:40f0:8", ["const:b6e3d8:8", "const:4:8"]]
- 00b6e3d8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6e4a0 ["INT_ADD", "register:40f0:8", ["const:b6e4a0:8", "const:4:8"]]
+ 00b6e4a0 ["CALL", null, ["callee:00bde040:8"]]
- 00b6e3d8 bytes eebe0194
+ 00b6e4a0 bytes e8be0194
- 00b6e3e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
- 00b6e3e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e3e0 bytes 801205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06efd6b7080a8340bd1c86baf5408078"></a>

### [`00b6e410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e410.md) → [`00b6e4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e4d8.md) _ZN8firebase4auth18userprofilebuilder10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b6e4f4",
      "incomplete_value": false,
      "site": "00b6e4f8",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e42c",
      "incomplete_value": false,
      "site": "00b6e430",
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
      "definition_site": "00b6e504",
      "incomplete_value": true,
      "site": "00b6e510",
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
      "definition_site": "00b6e43c",
      "incomplete_value": true,
      "site": "00b6e448",
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
      "00b6e4f4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6e504",
      "DATA",
      [
        "storage",
        "010a1a50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6e4f4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6e504",
      "DATA",
      [
        "storage",
        "010a1b10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e410.md#insn-00b6e430) · [`00b6e42c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e410.md#insn-00b6e42c) · [`00b6e438`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e410.md#insn-00b6e438)
- 新版 [`00b6e4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e4d8.md#insn-00b6e4f8) · [`00b6e4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e4d8.md#insn-00b6e4f4) · [`00b6e500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e4d8.md#insn-00b6e500)

~~~diff
- 00b6e430 ["INT_ADD", "register:40f0:8", ["const:b6e430:8", "const:4:8"]]
- 00b6e430 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6e4f8 ["INT_ADD", "register:40f0:8", ["const:b6e4f8:8", "const:4:8"]]
+ 00b6e4f8 ["CALL", null, ["callee:00bde130:8"]]
- 00b6e430 bytes 14bf0194
+ 00b6e4f8 bytes 0ebf0194
- 00b6e42c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b6e42c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e42c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6e42c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6e4f4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b6e4f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e4f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6e4f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6e42c bytes 00c81791
+ 00b6e4f4 bytes 00fc1991
- 00b6e438 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 00b6e438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b6e438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6e500 ["COPY", "tmp:0:8", ["const:b10:8"]]
+ 00b6e500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6e500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b6e438 bytes 08412991
+ 00b6e500 bytes 08412c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e171ea267a818ae3a16eb06566f74094"></a>

### [`00b6e44c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e44c.md) → [`00b6e514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e514.md) _ZN8firebase4auth18CacheUserMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0b50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b50.md) · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 1件 [`00be0c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c00.md) · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 29.27% / 新版 29.27%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e490"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e4e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e540"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6e464",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6e46c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e494"
      ]
    ],
    [
      "unmatched:00b6e474",
      "PARAM",
      [
        "storage",
        "002ab2e7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b6e52c",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e534",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e55c"
      ]
    ],
    [
      "00b6e53c",
      "PARAM",
      [
        "storage",
        "002ab2ed",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e44c.md#insn-00b6e46c) · [`00b6e488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e44c.md#insn-00b6e488) · [`00b6e490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e44c.md#insn-00b6e490)

~~~diff
- 00b6e46c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6e46c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b6e46c bytes 410100b5
- 00b6e488 ["INT_ADD", "register:40f0:8", ["const:b6e488:8", "const:4:8"]]
- 00b6e488 ["CALL", null, ["callee:00bde040:8"]]
- 00b6e488 bytes c2be0194
- 00b6e490 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8f8:8"]]
- 00b6e490 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6e490 bytes a07e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd79334d3fe40ce8f863d8f1a03d8273"></a>

### [`00b6e638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e638.md) → [`00b6e700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e700.md) _ZN8firebase4auth18ReleaseUserClassesEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b70.md) · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00be0c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c20.md) · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 13.46% / 新版 13.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e674"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e694"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e6c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6e714",
      "READ",
      [
        "storage",
        "010a18f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e71c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6e698"
      ]
    ],
    [
      "00b6e724",
      "READ",
      [
        "storage",
        "010a1900",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6e714",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6e71c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6e760"
      ]
    ],
    [
      "00b6e724",
      "READ",
      [
        "storage",
        "010a19c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e638.md#insn-00b6e660) · [`00b6e674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e638.md#insn-00b6e674) · [`00b6e694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e638.md#insn-00b6e694)

~~~diff
- 00b6e660 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b6e660 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6e660 bytes c8000034
- 00b6e674 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b6e674 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b6e674 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:900:8"]]
- 00b6e674 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b6e674 bytes bf022439
- 00b6e694 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
- 00b6e694 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6e694 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6e694 bytes 9f7e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d716321245b454f744f1c928305c176"></a>

### [`00b6e840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e840.md) → [`00b6e908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e908.md) _ZN8firebase4auth4UserD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b30.md)

変更の種類 constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b6e924",
      "incomplete_value": true,
      "site": "00b6e928",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e85c",
      "incomplete_value": true,
      "site": "00b6e860",
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
      "unmatched:00b6e850",
      "READ",
      [
        "storage",
        "00c1ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00b6e928",
      "DATA",
      [
        "storage",
        "00c12a00",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00b6e918",
      "READ",
      [
        "storage",
        "00c1bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00b6e928",
      "DATA",
      [
        "storage",
        "00c12ab0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e840.md#insn-00b6e850) · [`00b6e864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e840.md#insn-00b6e864)
- 新版 [`00b6e92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e908.md#insn-00b6e92c) · [`00b6e918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e908.md#insn-00b6e918)

~~~diff
- 00b6e850 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
- 00b6e850 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6e850 bytes 084945f9
- 00b6e864 ["INT_ADD", "register:40f0:8", ["const:b6e864:8", "const:4:8"]]
- 00b6e864 ["CALL", null, ["callee:00be0b30:8"]]
+ 00b6e92c ["INT_ADD", "register:40f0:8", ["const:b6e92c:8", "const:4:8"]]
+ 00b6e92c ["CALL", null, ["callee:00be0b30:8"]]
- 00b6e864 bytes 87c80194
+ 00b6e92c bytes 81c80194
+ 00b6e918 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b40:8"]]
+ 00b6e918 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6e918 bytes 08a145f9
~~~


<a id="compare-8a1eedefbadbcd2d905a0eb32ab1d2e5"></a>

### [`00b6e93c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e93c.md) → [`00b6ea04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ea04.md) _ZNK8firebase4auth4User5emailEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md) [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md) [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 87.50% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6ea34",
      "incomplete_value": true,
      "site": "00b6ea40",
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
                "const:aa0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6e96c",
      "incomplete_value": true,
      "site": "00b6e978",
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
                "const:9e0:8"
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
      "00b6ea34",
      "READ",
      [
        "storage",
        "010a19e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6ea84",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6ea34",
      "READ",
      [
        "storage",
        "010a1aa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6ea84",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6e978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e93c.md#insn-00b6e978) · [`00b6e954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e93c.md#insn-00b6e954) · [`00b6e95c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e93c.md#insn-00b6e95c)
- 新版 [`00b6ea40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ea04.md#insn-00b6ea40) · [`00b6ea1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ea04.md#insn-00b6ea1c) · [`00b6ea24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ea04.md#insn-00b6ea24)

~~~diff
- 00b6e978 ["INT_ADD", "register:40f0:8", ["const:b6e978:8", "const:4:8"]]
- 00b6e978 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6ea40 ["INT_ADD", "register:40f0:8", ["const:b6ea40:8", "const:4:8"]]
+ 00b6ea40 ["CALL", null, ["callee:0047495c:8"]]
- 00b6e978 bytes f917e497
+ 00b6ea40 bytes c717e497
- 00b6e954 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b6e954 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b6ea1c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b6ea1c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b6e954 bytes c90200b4
+ 00b6ea1c bytes c90200b4
- 00b6e95c ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b6e95c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b6ea24 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b6ea24 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b6e95c bytes 950200b4
+ 00b6ea24 bytes 950200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aa6b0478bfcfdb475071fa8668b862b"></a>

### [`00b6e9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e9e0.md) → [`00b6eaa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6eaa8.md) _ZNK8firebase4auth4User12display_nameEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md) [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md) [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 16.67% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e9e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e9e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6e9e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6e9e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6e9e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6e9e8",
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
      "00b6eaa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6eaac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6eab0",
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

- 旧版 [`00b6e9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e9e0.md#insn-00b6e9e0) · [`00b6e9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e9e0.md#insn-00b6e9e4) · [`00b6e9e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6e9e0.md#insn-00b6e9e8)

~~~diff
- 00b6e9e0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b6e9e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b6e9e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6e9e0 bytes f50f1df8
- 00b6e9e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6e9e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6e9e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6e9e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6e9e4 bytes f44f01a9
- 00b6e9e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b6e9e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b6e9e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6e9e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6e9e8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f797367e73f57ae1cd914469e451aa42"></a>

### [`00b6eb28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6eb28.md) → [`00b6ebf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ebf0.md) _ZNK8firebase4auth4User9photo_urlEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde370.md) [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde420.md) [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 44.44% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6eb28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6eb2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6eb2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6eb28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6eb2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6eb48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ec60"
      ]
    ]
  ],
  "added": [
    [
      "00b6ebf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b6ebf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b6ec10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ec60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6eb28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6eb28.md#insn-00b6eb28) · [`00b6eb2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6eb28.md#insn-00b6eb2c) · [`00b6eb48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6eb28.md#insn-00b6eb48)

~~~diff
- 00b6eb28 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b6eb28 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b6eb28 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6eb28 bytes f50f1df8
- 00b6eb2c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6eb2c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6eb2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6eb2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6eb2c bytes f44f01a9
- 00b6eb48 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b6eb48 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00b6eb48 bytes 950200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c492790b916368013936f55a40120f3a"></a>

### [`00b6ebcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ebcc.md) → [`00b6ec94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ec94.md) _ZNK8firebase4auth4User11provider_idEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md) [`00bde640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde640.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md) [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6ebf0",
      "incomplete_value": true,
      "site": "00b6ebf4",
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
            "register:4048:8"
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
      "definition_site": "00b6ecc4",
      "incomplete_value": true,
      "site": "00b6ecd0",
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
                "const:a80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6ebfc",
      "incomplete_value": true,
      "site": "00b6ec08",
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
                "const:9c0:8"
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
      "00b6ecc4",
      "READ",
      [
        "storage",
        "010a19c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6ed14",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6ecc4",
      "READ",
      [
        "storage",
        "010a1a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6ed14",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ebf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ebcc.md#insn-00b6ebf4) · [`00b6ec08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ebcc.md#insn-00b6ec08) · [`00b6ebfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ebcc.md#insn-00b6ebfc)
- 新版 [`00b6ecbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ec94.md#insn-00b6ecbc) · [`00b6ecd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ec94.md#insn-00b6ecd0) · [`00b6ecc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ec94.md#insn-00b6ecc4)

~~~diff
- 00b6ebf4 ["INT_ADD", "register:40f0:8", ["const:b6ebf4:8", "const:4:8"]]
- 00b6ebf4 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b6ecbc ["INT_ADD", "register:40f0:8", ["const:b6ecbc:8", "const:4:8"]]
+ 00b6ecbc ["CALL", null, ["callee:00bde1b0:8"]]
- 00b6ebf4 bytes 43bd0194
+ 00b6ecbc bytes 3dbd0194
- 00b6ec08 ["INT_ADD", "register:40f0:8", ["const:b6ec08:8", "const:4:8"]]
- 00b6ec08 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6ecd0 ["INT_ADD", "register:40f0:8", ["const:b6ecd0:8", "const:4:8"]]
+ 00b6ecd0 ["CALL", null, ["callee:0047495c:8"]]
- 00b6ec08 bytes 5517e497
+ 00b6ecd0 bytes 2317e497
- 00b6ebfc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9c0:8"]]
- 00b6ebfc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6ecc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a80:8"]]
+ 00b6ecc4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6ebfc bytes 02e144f9
+ 00b6ecc4 bytes 024145f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9afb793152205101d9bd4f1c33359ca6"></a>

### [`00b6ec70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ec70.md) → [`00b6ed38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ed38.md) _ZN8firebase4auth15ReadTokenResultEP8_jobjectPNS0_18FutureCallbackDataINSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b6ede4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ede4.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md)
- 新版 呼出元 1件 [`00b6eeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6eeac.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.13% / 新版 89.13%

CFGの説明率　旧版 29.63% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ed54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ed8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6eda8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b6edbc",
      "PARAM",
      [
        "storage",
        "002a632b",
        null,
        "string"
      ]
    ],
    [
      "00b6edc8",
      "READ",
      [
        "storage",
        "010a1908",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6ed58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ee30"
      ]
    ]
  ],
  "added": [
    [
      "00b6edbc",
      "PARAM",
      [
        "storage",
        "002a6324",
        null,
        "string"
      ]
    ],
    [
      "00b6edc8",
      "READ",
      [
        "storage",
        "010a19c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6ee20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6ee30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6eccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ec70.md#insn-00b6eccc) · [`00b6ecdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ec70.md#insn-00b6ecdc) · [`00b6ece0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ec70.md#insn-00b6ece0)
- 新版 [`00b6ed94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ed38.md#insn-00b6ed94) · [`00b6eda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ed38.md#insn-00b6eda4) · [`00b6eda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ed38.md#insn-00b6eda8)

~~~diff
- 00b6eccc ["INT_ADD", "register:40f0:8", ["const:b6eccc:8", "const:4:8"]]
- 00b6eccc ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b6ed94 ["INT_ADD", "register:40f0:8", ["const:b6ed94:8", "const:4:8"]]
+ 00b6ed94 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b6eccc bytes 95bb0194
+ 00b6ed94 bytes 8fbb0194
- 00b6ecdc ["INT_ADD", "register:40f0:8", ["const:b6ecdc:8", "const:4:8"]]
- 00b6ecdc ["CALL", null, ["callee:00bddbe0:8"]]
+ 00b6eda4 ["INT_ADD", "register:40f0:8", ["const:b6eda4:8", "const:4:8"]]
+ 00b6eda4 ["CALL", null, ["callee:00bddbe0:8"]]
- 00b6ecdc bytes 95bb0194
+ 00b6eda4 bytes 8fbb0194
- 00b6ece0 ["INT_EQUAL", "tmp:0:1", ["register:40c8:4", "const:0:4"]]
- 00b6ece0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b6eda8 ["INT_EQUAL", "tmp:0:1", ["register:40c8:4", "const:0:4"]]
+ 00b6eda8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00b6ece0 bytes 79000034
+ 00b6eda8 bytes 79000034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08c4f9b5755264390e2d80d1ec981e7b"></a>

### [`00b6ede4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ede4.md) → [`00b6eeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6eeac.md) _ZN8firebase4auth4User8GetTokenEb

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb00.md) · 呼出先 17件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00ae3d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae3/00ae3d00.md) [`00b6ec70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ec70.md) [`00b71980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71980.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00bddbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbb0.md) · 呼出先 17件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00ae3dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3dc8.md) [`00b6ed38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6ed38.md) [`00b71a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71a48.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 28.57% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ede8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ede8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6edec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6ede8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6edec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6edf0",
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
      "00b6eeb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b6eeb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b6eeb8",
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

- 旧版 [`00b6ede8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ede4.md#insn-00b6ede8) · [`00b6edec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ede4.md#insn-00b6edec) · [`00b6edf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ede4.md#insn-00b6edf0)

~~~diff
- 00b6ede8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b6ede8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b6ede8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b6ede8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6ede8 bytes fa6704a9
- 00b6edec ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b6edec ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b6edec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b6edec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6edec bytes f85f05a9
- 00b6edf0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b6edf0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b6edf0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b6edf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6edf0 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b515d981631c0533eaedfe838bffdbd9"></a>

### [`00b6f148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f148.md) → [`00b6f210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f210.md) _ZNK8firebase4auth4User13provider_dataEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb60.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00553/005533e0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00bddc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc10.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.03% / 新版 89.03%

CFGの説明率　旧版 73.68% / 新版 73.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 16件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f148"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f148"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f14c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6f148",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6f14c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6f150",
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
      "00b6f210",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b6f214",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b6f218",
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

- 旧版 [`00b6f148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f148.md#insn-00b6f148) · [`00b6f14c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f148.md#insn-00b6f14c) · [`00b6f150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f148.md#insn-00b6f150)

~~~diff
- 00b6f148 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b6f148 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b6f148 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00b6f148 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6f148 bytes fc6fbaa9
- 00b6f14c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b6f14c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b6f14c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b6f14c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6f14c bytes fa6701a9
- 00b6f150 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b6f150 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b6f150 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b6f150 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6f150 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa8b7a7199f667c892ff5d75955e867e"></a>

### [`00b6f854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f854.md) → [`00b6f91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f91c.md) _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE7reserveEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0dd0.md) · 呼出先 4件 [`00ae03b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae0/00ae03b4.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0da0.md)
- 新版 呼出元 1件 [`00be0e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e80.md) · 呼出先 4件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e50.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.86% / 新版 72.86%

CFGの説明率　旧版 16.67% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f908"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6f9d0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6f894"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6f894",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6fa10"
      ]
    ],
    [
      "unmatched:00b6f8ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6fa28"
      ]
    ],
    [
      "unmatched:00b6f90c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6f9f0"
      ]
    ]
  ],
  "added": [
    [
      "00b6f95c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6fa10"
      ]
    ],
    [
      "00b6f974",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6fa28"
      ]
    ],
    [
      "00b6f9d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6f9f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f854.md#insn-00b6f894) · [`00b6f8ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f854.md#insn-00b6f8ac) · [`00b6f8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f854.md#insn-00b6f8c4)
- 新版 [`00b6f98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6f91c.md#insn-00b6f98c)

~~~diff
- 00b6f894 ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
- 00b6f894 bytes a2050054
- 00b6f8ac ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 00b6f8ac bytes a2050054
- 00b6f8c4 ["INT_ADD", "register:40f0:8", ["const:b6f8c4:8", "const:4:8"]]
- 00b6f8c4 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00b6f98c ["INT_ADD", "register:40f0:8", ["const:b6f98c:8", "const:4:8"]]
+ 00b6f98c ["CALL", null, ["callee:00bdaff0:8"]]
- 00b6f8c4 bytes 9fad0194
+ 00b6f98c bytes 99ad0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c351aed5793687db78cc02c100d85f1"></a>

### [`00b6f9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f9a0.md) → [`00b6fa68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fa68.md) _ZNK8firebase4auth22AndroidWrappedUserInfo3uidEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 37.50% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6fa94",
      "incomplete_value": true,
      "site": "00b6faa0",
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
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6f9cc",
      "incomplete_value": true,
      "site": "00b6f9d8",
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
                "const:9b8:8"
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
      "00b6fa94",
      "READ",
      [
        "storage",
        "010a19b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6fa94",
      "READ",
      [
        "storage",
        "010a1a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6f9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f9a0.md#insn-00b6f9d8) · [`00b6f9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f9a0.md#insn-00b6f9bc) · [`00b6f9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6f9a0.md#insn-00b6f9cc)
- 新版 [`00b6faa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fa68.md#insn-00b6faa0) · [`00b6fa84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fa68.md#insn-00b6fa84) · [`00b6fa94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fa68.md#insn-00b6fa94)

~~~diff
- 00b6f9d8 ["INT_ADD", "register:40f0:8", ["const:b6f9d8:8", "const:4:8"]]
- 00b6f9d8 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6faa0 ["INT_ADD", "register:40f0:8", ["const:b6faa0:8", "const:4:8"]]
+ 00b6faa0 ["CALL", null, ["callee:0047495c:8"]]
- 00b6f9d8 bytes e113e497
+ 00b6faa0 bytes af13e497
- 00b6f9bc ["INT_ADD", "register:40f0:8", ["const:b6f9bc:8", "const:4:8"]]
- 00b6f9bc ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b6fa84 ["INT_ADD", "register:40f0:8", ["const:b6fa84:8", "const:4:8"]]
+ 00b6fa84 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b6f9bc bytes d1b90194
+ 00b6fa84 bytes cbb90194
- 00b6f9cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00b6f9cc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6fa94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00b6fa94 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6f9cc bytes 02dd44f9
+ 00b6fa94 bytes 023d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-799c31edfc37a95c8fb42d58704f7b4b"></a>

### [`00b6faa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6faa8.md) → [`00b6fb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fb70.md) _ZNK8firebase4auth22AndroidWrappedUserInfo12display_nameEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 71.43% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6fac0",
      "incomplete_value": true,
      "site": "00b6fac4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
      "definition_site": "00b6fb9c",
      "incomplete_value": true,
      "site": "00b6fba8",
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
                "const:a88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6fad4",
      "incomplete_value": true,
      "site": "00b6fae0",
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
                "const:9c8:8"
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
      "00b6fb9c",
      "READ",
      [
        "storage",
        "010a19c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6fb9c",
      "READ",
      [
        "storage",
        "010a1a88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6fac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6faa8.md#insn-00b6fac4) · [`00b6fae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6faa8.md#insn-00b6fae0) · [`00b6facc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6faa8.md#insn-00b6facc)
- 新版 [`00b6fb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fb70.md#insn-00b6fb8c) · [`00b6fba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fb70.md#insn-00b6fba8) · [`00b6fb94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fb70.md#insn-00b6fb94)

~~~diff
- 00b6fac4 ["INT_ADD", "register:40f0:8", ["const:b6fac4:8", "const:4:8"]]
- 00b6fac4 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b6fb8c ["INT_ADD", "register:40f0:8", ["const:b6fb8c:8", "const:4:8"]]
+ 00b6fb8c ["CALL", null, ["callee:00bde1b0:8"]]
- 00b6fac4 bytes 8fb90194
+ 00b6fb8c bytes 89b90194
- 00b6fae0 ["INT_ADD", "register:40f0:8", ["const:b6fae0:8", "const:4:8"]]
- 00b6fae0 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6fba8 ["INT_ADD", "register:40f0:8", ["const:b6fba8:8", "const:4:8"]]
+ 00b6fba8 ["CALL", null, ["callee:0047495c:8"]]
- 00b6fae0 bytes 9f13e497
+ 00b6fba8 bytes 6d13e497
- 00b6facc ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b6facc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b6fb94 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b6fb94 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6facc bytes f50000b4
+ 00b6fb94 bytes f50000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24a1b31bb56d4f47a808c17af93960b7"></a>

### [`00b6fb2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fb2c.md) → [`00b6fbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fbf4.md) _ZNK8firebase4auth22AndroidWrappedUserInfo9photo_urlEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde370.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde420.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6fb58",
      "incomplete_value": true,
      "site": "00b6fb64",
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
                "const:9d8:8"
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
      "00b6fc20",
      "READ",
      [
        "storage",
        "010a19d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6fc20",
      "READ",
      [
        "storage",
        "010a1a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6fb64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fb2c.md#insn-00b6fb64) · [`00b6fb48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fb2c.md#insn-00b6fb48) · [`00b6fb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fb2c.md#insn-00b6fb50)
- 新版 [`00b6fc2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fbf4.md#insn-00b6fc2c) · [`00b6fc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fbf4.md#insn-00b6fc10) · [`00b6fc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fbf4.md#insn-00b6fc18)

~~~diff
- 00b6fb64 ["INT_ADD", "register:40f0:8", ["const:b6fb64:8", "const:4:8"]]
- 00b6fb64 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6fc2c ["INT_ADD", "register:40f0:8", ["const:b6fc2c:8", "const:4:8"]]
+ 00b6fc2c ["CALL", null, ["callee:0047495c:8"]]
- 00b6fb64 bytes 7e13e497
+ 00b6fc2c bytes 4c13e497
- 00b6fb48 ["INT_ADD", "register:40f0:8", ["const:b6fb48:8", "const:4:8"]]
- 00b6fb48 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b6fc10 ["INT_ADD", "register:40f0:8", ["const:b6fc10:8", "const:4:8"]]
+ 00b6fc10 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b6fb48 bytes 6eb90194
+ 00b6fc10 bytes 68b90194
- 00b6fb50 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b6fb50 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b6fc18 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b6fc18 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6fb50 bytes f50000b4
+ 00b6fc18 bytes f50000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-918e9d84e5bf31e1b8178ab259aafdca"></a>

### [`00b6fbb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fbb0.md) → [`00b6fc78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fc78.md) _ZNK8firebase4auth22AndroidWrappedUserInfo11provider_idEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b6fbc8",
      "incomplete_value": true,
      "site": "00b6fbcc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
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
      "definition_site": "00b6fca4",
      "incomplete_value": true,
      "site": "00b6fcb0",
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
                "const:a80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6fbdc",
      "incomplete_value": true,
      "site": "00b6fbe8",
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
                "const:9c0:8"
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
      "00b6fca4",
      "READ",
      [
        "storage",
        "010a19c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6fca4",
      "READ",
      [
        "storage",
        "010a1a80",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6fbcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fbb0.md#insn-00b6fbcc) · [`00b6fbe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fbb0.md#insn-00b6fbe8) · [`00b6fbd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fbb0.md#insn-00b6fbd4)
- 新版 [`00b6fc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fc78.md#insn-00b6fc94) · [`00b6fcb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fc78.md#insn-00b6fcb0) · [`00b6fc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fc78.md#insn-00b6fc9c)

~~~diff
- 00b6fbcc ["INT_ADD", "register:40f0:8", ["const:b6fbcc:8", "const:4:8"]]
- 00b6fbcc ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b6fc94 ["INT_ADD", "register:40f0:8", ["const:b6fc94:8", "const:4:8"]]
+ 00b6fc94 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b6fbcc bytes 4db90194
+ 00b6fc94 bytes 47b90194
- 00b6fbe8 ["INT_ADD", "register:40f0:8", ["const:b6fbe8:8", "const:4:8"]]
- 00b6fbe8 ["CALL", null, ["callee:0047495c:8"]]
+ 00b6fcb0 ["INT_ADD", "register:40f0:8", ["const:b6fcb0:8", "const:4:8"]]
+ 00b6fcb0 ["CALL", null, ["callee:0047495c:8"]]
- 00b6fbe8 bytes 5d13e497
+ 00b6fcb0 bytes 2b13e497
- 00b6fbd4 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 00b6fbd4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b6fc9c ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 00b6fc9c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b6fbd4 bytes f50000b4
+ 00b6fc9c bytes f50000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2606aa999f2f3dcc3aa2a2b3e7b7b8a"></a>

### [`00b6fc34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fc34.md) → [`00b6fcfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fcfc.md) _ZNK8firebase4auth22AndroidWrappedUserInfo12phone_numberEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00bde410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde410.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4c0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 22.22% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6fd28",
      "incomplete_value": true,
      "site": "00b6fd34",
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
                "const:a90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6fc60",
      "incomplete_value": true,
      "site": "00b6fc6c",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:9d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6fcb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00b6fd7c"
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
      "unmatched:00b6fc60",
      "READ",
      [
        "storage",
        "010a19d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6fd28",
      "READ",
      [
        "storage",
        "010a1a90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6fc6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fc34.md#insn-00b6fc6c) · [`00b6fcb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fc34.md#insn-00b6fcb4)
- 新版 [`00b6fd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fcfc.md#insn-00b6fd34) · [`00b6fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fcfc.md#insn-00b6fd7c)

~~~diff
- 00b6fc6c ["INT_ADD", "register:40f0:8", ["const:b6fc6c:8", "const:4:8"]]
- 00b6fc6c ["CALL", null, ["callee:0047495c:8"]]
+ 00b6fd34 ["INT_ADD", "register:40f0:8", ["const:b6fd34:8", "const:4:8"]]
+ 00b6fd34 ["CALL", null, ["callee:0047495c:8"]]
- 00b6fc6c bytes 3c13e497
+ 00b6fd34 bytes 0a13e497
- 00b6fcb4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b6fcb4 ["RETURN", null, ["register:0:8"]]
- 00b6fcb4 bytes c0035fd6
+ 00b6fd7c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00b6fd7c ["RETURN", null, ["register:0:8"]]
+ 00b6fd7c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d8e83cc45b15faec5f897b8cb95e6df"></a>

### [`00b6fcb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fcb8.md) → [`00b6fd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fd80.md) _ZN8firebase4auth22AndroidWrappedUserInfoD2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00be0a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0a80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00be0b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b30.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6fcd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6fda0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6fda4",
      "incomplete_value": true,
      "site": "00b6fda8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6fccc",
      "READ",
      [
        "storage",
        "00c1bb30",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b6fcd8",
      "DATA",
      [
        "storage",
        "00c12a68",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00b6fd94",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00b6fda0",
      "DATA",
      [
        "storage",
        "00c12b18",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6fcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fcb8.md#insn-00b6fcd8) · [`00b6fce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fcb8.md#insn-00b6fce0)
- 新版 [`00b6fda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fd80.md#insn-00b6fda8) · [`00b6fda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fd80.md#insn-00b6fda0)

~~~diff
- 00b6fcd8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b6fcd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b6fcd8 bytes 090000f9
- 00b6fce0 ["INT_ADD", "register:40f0:8", ["const:b6fce0:8", "const:4:8"]]
- 00b6fce0 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b6fda8 ["INT_ADD", "register:40f0:8", ["const:b6fda8:8", "const:4:8"]]
+ 00b6fda8 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b6fce0 bytes 08b90194
+ 00b6fda8 bytes 02b90194
+ 00b6fda0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00b6fda0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00b6fda0 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-718bf1fc98b099ce643d230acb798278"></a>

### [`00b6fd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fd1c.md) → [`00b6fde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6f/00b6fde4.md) _ZN8firebase4auth4User14UpdatePasswordEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60a8c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.09% / 新版 86.09%

CFGの説明率　旧版 23.81% / 新版 26.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6fd20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6fd20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6fd24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6fd20",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6fd24",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b6fd28",
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
      "00b6fde8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b6fdec",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b6fdf0",
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

- 旧版 [`00b6fd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fd1c.md#insn-00b6fd20) · [`00b6fd24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fd1c.md#insn-00b6fd24) · [`00b6fd28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6fd1c.md#insn-00b6fd28)

~~~diff
- 00b6fd20 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b6fd20 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b6fd20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b6fd20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6fd20 bytes fa6704a9
- 00b6fd24 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b6fd24 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b6fd24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b6fd24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6fd24 bytes f85f05a9
- 00b6fd28 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b6fd28 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b6fd28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b6fd28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b6fd28 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c68c027f271a98620f362babfa21488"></a>

### [`00b6ff44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6ff44.md) → [`00b7000c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7000c.md) _ZN8firebase4auth4User17UpdateUserProfileERKNS1_11UserProfileE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00b60a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60a8c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 95.18% / 新版 95.18%

CFGの説明率　旧版 66.04% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6ff80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70060"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70068"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6ff80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70150"
      ]
    ],
    [
      "unmatched:00b6ffd0",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b6ffd4",
      "READ",
      [
        "storage",
        "010a1a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b70048",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b70150"
      ]
    ],
    [
      "00b70098",
      "READ",
      [
        "storage",
        "010a1ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b7009c",
      "READ",
      [
        "storage",
        "010a1af0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6ff80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6ff44.md#insn-00b6ff80) · [`00b6ffa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6ff44.md#insn-00b6ffa4) · [`00b6ffb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6f/00b6ff44.md#insn-00b6ffb0)
- 新版 [`00b7006c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7000c.md#insn-00b7006c) · [`00b70078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7000c.md#insn-00b70078)

~~~diff
- 00b6ff80 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6ff80 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 00b6ff80 bytes 480800b4
- 00b6ffa4 ["INT_ADD", "register:40f0:8", ["const:b6ffa4:8", "const:4:8"]]
- 00b6ffa4 ["CALL", null, ["callee:00bddf70:8"]]
+ 00b7006c ["INT_ADD", "register:40f0:8", ["const:b7006c:8", "const:4:8"]]
+ 00b7006c ["CALL", null, ["callee:00bddf70:8"]]
- 00b6ffa4 bytes c7b70194
+ 00b7006c bytes c1b70194
- 00b6ffb0 ["INT_ADD", "register:40f0:8", ["const:b6ffb0:8", "const:4:8"]]
- 00b6ffb0 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b70078 ["INT_ADD", "register:40f0:8", ["const:b70078:8", "const:4:8"]]
+ 00b70078 ["CALL", null, ["callee:00bddf30:8"]]
- 00b6ffb0 bytes b4b70194
+ 00b70078 bytes aeb70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f59c57a42c7529f2a1aaed683bea093c"></a>

### [`00b70544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70544.md) → [`00b7060c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7060c.md) _ZNK8firebase4auth4User16LinkWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b70648",
      "incomplete_value": false,
      "site": "00b7064c",
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
            "const:c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b70580",
      "incomplete_value": false,
      "site": "00b70584",
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
            "const:d0:8"
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
      "00b70648",
      "PARAM",
      [
        "storage",
        "002a50d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b70648",
      "PARAM",
      [
        "storage",
        "002a50c9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b70584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70544.md#insn-00b70584) · [`00b70580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70544.md#insn-00b70580) · [`00b70590`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70544.md#insn-00b70590)
- 新版 [`00b7064c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7060c.md#insn-00b7064c) · [`00b70648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7060c.md#insn-00b70648) · [`00b70658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b7060c.md#insn-00b70658)

~~~diff
- 00b70584 ["INT_ADD", "register:40f0:8", ["const:b70584:8", "const:4:8"]]
- 00b70584 ["CALL", null, ["callee:00bde130:8"]]
+ 00b7064c ["INT_ADD", "register:40f0:8", ["const:b7064c:8", "const:4:8"]]
+ 00b7064c ["CALL", null, ["callee:00bde130:8"]]
- 00b70584 bytes bfb60194
+ 00b7064c bytes b9b60194
- 00b70580 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 00b70580 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b70580 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b70580 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b70648 ["COPY", "tmp:0:8", ["const:c9:8"]]
+ 00b70648 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b70648 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b70648 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b70580 bytes 00400391
+ 00b70648 bytes 00240391
- 00b70590 ["INT_ADD", "register:40f0:8", ["const:b70590:8", "const:4:8"]]
- 00b70590 ["CALL", null, ["callee:00bdddc0:8"]]
+ 00b70658 ["INT_ADD", "register:40f0:8", ["const:b70658:8", "const:4:8"]]
+ 00b70658 ["CALL", null, ["callee:00bdddc0:8"]]
- 00b70590 bytes e0b50194
+ 00b70658 bytes dab50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-830a160be5798ad78e1dc3c52875062b"></a>

### [`00b705c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b705c8.md) → [`00b70690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70690.md) _ZN8firebase4auth4User6UnlinkEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60310.md) [`00b64df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b603d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md) [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.55% / 新版 74.55%

CFGの説明率　旧版 9.30% / 新版 7.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b705f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b706c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b706c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b705f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b705f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b707a4"
      ]
    ],
    [
      "unmatched:00b70648",
      "READ",
      [
        "storage",
        "010a1960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b706b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00b706c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b707a4"
      ]
    ],
    [
      "00b70710",
      "READ",
      [
        "storage",
        "010a1a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b705f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b705c8.md#insn-00b705f0) · [`00b705f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b705c8.md#insn-00b705f8) · [`00b7061c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b705c8.md#insn-00b7061c)
- 新版 [`00b706e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70690.md#insn-00b706e4)

~~~diff
- 00b705f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00b705f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b705f0 bytes e91700f9
- 00b705f8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b705f8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00b705f8 bytes 290700b4
- 00b7061c ["INT_ADD", "register:40f0:8", ["const:b7061c:8", "const:4:8"]]
- 00b7061c ["CALL", null, ["callee:00be0bb0:8"]]
+ 00b706e4 ["INT_ADD", "register:40f0:8", ["const:b706e4:8", "const:4:8"]]
+ 00b706e4 ["CALL", null, ["callee:00be0bb0:8"]]
- 00b7061c bytes 39c10194
+ 00b706e4 bytes 33c10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-617214581c467860c4dac9edd733c373"></a>

### [`00b707d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b707d0.md) → [`00b70898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70898.md) _ZN8firebase4auth4User27UpdatePhoneNumberCredentialERKNS0_19PhoneAuthCredentialE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b606d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b606d8.md) [`00b65208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65208.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b607a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b607a0.md) [`00b652d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b652d0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.37% / 新版 85.37%

CFGの説明率　旧版 28.57% / 新版 42.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b707d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b707d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b707d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b707d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b707d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b707dc",
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
      "00b7089c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b708a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b708a4",
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

- 旧版 [`00b707d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b707d0.md#insn-00b707d4) · [`00b707d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b707d0.md#insn-00b707d8) · [`00b707dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b707d0.md#insn-00b707dc)

~~~diff
- 00b707d4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b707d4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b707d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b707d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b707d4 bytes fa6704a9
- 00b707d8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b707d8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b707d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b707d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b707d8 bytes f85f05a9
- 00b707dc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b707dc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b707dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b707dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b707dc bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da587a7fe93054e8ef71eaa4821ce5e2"></a>

### [`00b70a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70a1c.md) → [`00b70ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70ae4.md) _ZN8firebase4auth4User6ReloadEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60a8c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 56.25% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b70b40",
      "incomplete_value": true,
      "site": "00b70b48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00b70b44",
      "incomplete_value": true,
      "site": "00b70b48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:8:8"
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b70b68",
      "incomplete_value": true,
      "site": "00b70b74",
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
                "const:a30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b70aa0",
      "incomplete_value": true,
      "site": "00b70aac",
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
                "const:970:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b70b68",
      "READ",
      [
        "storage",
        "010a1970",
        null,
        "undefined8"
      ]
    ],
    [
      "00b70c04",
      "READ",
      [
        "storage",
        "00c1bae8",
        null,
        "pointer"
      ]
    ],
    [
      "00b70c04",
      "PARAM",
      [
        "storage",
        "00b60a8c",
        "_ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b70b68",
      "READ",
      [
        "storage",
        "010a1a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b70c04",
      "READ",
      [
        "storage",
        "00c1bb98",
        null,
        "pointer"
      ]
    ],
    [
      "00b70c04",
      "PARAM",
      [
        "storage",
        "00b60b54",
        "_ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b70a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70a1c.md#insn-00b70a80) · [`00b70aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70a1c.md#insn-00b70aac) · [`00b70b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70a1c.md#insn-00b70b4c)
- 新版 [`00b70b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70ae4.md#insn-00b70b48) · [`00b70b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70ae4.md#insn-00b70b74) · [`00b70c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70ae4.md#insn-00b70c14)

~~~diff
- 00b70a80 ["INT_ADD", "register:40f0:8", ["const:b70a80:8", "const:4:8"]]
- 00b70a80 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b70b48 ["INT_ADD", "register:40f0:8", ["const:b70b48:8", "const:4:8"]]
+ 00b70b48 ["CALL", null, ["callee:00bddf30:8"]]
- 00b70a80 bytes 00b50194
+ 00b70b48 bytes fab40194
- 00b70aac ["INT_ADD", "register:40f0:8", ["const:b70aac:8", "const:4:8"]]
- 00b70aac ["CALL", null, ["callee:0047495c:8"]]
+ 00b70b74 ["INT_ADD", "register:40f0:8", ["const:b70b74:8", "const:4:8"]]
+ 00b70b74 ["CALL", null, ["callee:0047495c:8"]]
- 00b70aac bytes ac0fe497
+ 00b70b74 bytes 7a0fe497
- 00b70b4c ["INT_ADD", "register:40f0:8", ["const:b70b4c:8", "const:4:8"]]
- 00b70b4c ["CALL", null, ["callee:00bde070:8"]]
+ 00b70c14 ["INT_ADD", "register:40f0:8", ["const:b70c14:8", "const:4:8"]]
+ 00b70c14 ["CALL", null, ["callee:00bde070:8"]]
- 00b70b4c bytes 1db50194
+ 00b70c14 bytes 17b50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-313456e1e2e91b4f16a3558767543376"></a>

### [`00b70c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70c0c.md) → [`00b70cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70cd4.md) _ZN8firebase4auth4User14ReauthenticateERKNS0_10CredentialE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60a8c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 55.56% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 11件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70c10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70c10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70c14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b70c10",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b70c14",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b70c18",
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
      "00b70cd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b70cdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b70ce0",
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

- 旧版 [`00b70c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70c0c.md#insn-00b70c10) · [`00b70c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70c0c.md#insn-00b70c14) · [`00b70c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70c0c.md#insn-00b70c18)

~~~diff
- 00b70c10 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b70c10 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b70c10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b70c10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b70c10 bytes fa6704a9
- 00b70c14 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b70c14 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b70c14 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b70c14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b70c14 bytes f85f05a9
- 00b70c18 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b70c18 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b70c18 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b70c18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b70c18 bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b826421550f34865f8e369ee23e81874"></a>

### [`00b70e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70e04.md) → [`00b70ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70ecc.md) _ZN8firebase4auth4User29ReauthenticateAndRetrieveDataERKNS0_10CredentialE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60310`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60310.md) [`00b64df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b603d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md) [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.99% / 新版 98.99%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b70f9c",
      "incomplete_value": true,
      "site": "00b70f9c",
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
                "const:ba0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b70ed4",
      "incomplete_value": true,
      "site": "00b70ed4",
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
                "const:af0:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b70f38",
      "incomplete_value": true,
      "site": "00b70f48",
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b70e70",
      "incomplete_value": true,
      "site": "00b70e80",
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
                "const:980:8"
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
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b70f18",
      "incomplete_value": true,
      "site": "00b70f28",
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
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b70f38",
      "READ",
      [
        "storage",
        "010a1980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b70f98",
      "READ",
      [
        "storage",
        "00c1baf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b70f9c",
      "DATA",
      [
        "storage",
        "00b64df8",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b70f38",
      "READ",
      [
        "storage",
        "010a1a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b70f98",
      "READ",
      [
        "storage",
        "00c1bba0",
        null,
        "pointer"
      ]
    ],
    [
      "00b70f9c",
      "DATA",
      [
        "storage",
        "00b64ec0",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b70e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70e04.md#insn-00b70e80) · [`00b70f28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70e04.md#insn-00b70f28) · [`00b70e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70e04.md#insn-00b70e34)
- 新版 [`00b70f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70ecc.md#insn-00b70f48) · [`00b70ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70ecc.md#insn-00b70ff0) · [`00b70efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70ecc.md#insn-00b70efc)

~~~diff
- 00b70e80 ["INT_ADD", "register:40f0:8", ["const:b70e80:8", "const:4:8"]]
- 00b70e80 ["CALL", null, ["callee:0047495c:8"]]
+ 00b70f48 ["INT_ADD", "register:40f0:8", ["const:b70f48:8", "const:4:8"]]
+ 00b70f48 ["CALL", null, ["callee:0047495c:8"]]
- 00b70e80 bytes b70ee497
+ 00b70f48 bytes 850ee497
- 00b70f28 ["INT_ADD", "register:40f0:8", ["const:b70f28:8", "const:4:8"]]
- 00b70f28 ["CALL", null, ["callee:00bde070:8"]]
+ 00b70ff0 ["INT_ADD", "register:40f0:8", ["const:b70ff0:8", "const:4:8"]]
+ 00b70ff0 ["CALL", null, ["callee:00bde070:8"]]
- 00b70f28 bytes 26b40194
+ 00b70ff0 bytes 20b40194
- 00b70e34 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00b70e34 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b70efc ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
+ 00b70efc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b70e34 bytes c90500b4
+ 00b70efc bytes c90500b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cafb9e13c86df60d199a6a83b467a5d1"></a>

### [`00b70fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70fdc.md) → [`00b710a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b710a4.md) _ZNK8firebase4auth4User26ReauthenticateWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bddc80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc80.md) [`00bddd10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd10.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b70fe0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b70fdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b70fe0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71018",
      "PARAM",
      [
        "storage",
        "002a50d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b710a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b710a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b710e0",
      "PARAM",
      [
        "storage",
        "002a50c9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b70fdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70fdc.md#insn-00b70fdc) · [`00b70fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70fdc.md#insn-00b70fe0) · [`00b7101c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b70fdc.md#insn-00b7101c)
- 新版 [`00b710e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b710a4.md#insn-00b710e4)

~~~diff
- 00b70fdc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b70fdc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b70fdc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b70fdc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b70fdc bytes f44fbea9
- 00b70fe0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b70fe0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b70fe0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b70fe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b70fe0 bytes fd7b01a9
- 00b7101c ["INT_ADD", "register:40f0:8", ["const:b7101c:8", "const:4:8"]]
- 00b7101c ["CALL", null, ["callee:00bde130:8"]]
+ 00b710e4 ["INT_ADD", "register:40f0:8", ["const:b710e4:8", "const:4:8"]]
+ 00b710e4 ["CALL", null, ["callee:00bde130:8"]]
- 00b7101c bytes 19b40194
+ 00b710e4 bytes 13b40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c03518d640d59fdb85d59d211648fa84"></a>

### [`00b71060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71060.md) → [`00b71128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71128.md) _ZN8firebase4auth4User21SendEmailVerificationEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60a8c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 80.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b711ac",
      "incomplete_value": true,
      "site": "00b711b8",
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
                "const:a50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b710e4",
      "incomplete_value": true,
      "site": "00b710f0",
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b71248",
      "incomplete_value": true,
      "site": "00b71258",
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b71180",
      "incomplete_value": true,
      "site": "00b71190",
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
                "const:ae8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b711ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b711ac",
      "READ",
      [
        "storage",
        "010a1990",
        null,
        "undefined8"
      ]
    ],
    [
      "00b71248",
      "READ",
      [
        "storage",
        "00c1bae8",
        null,
        "pointer"
      ]
    ],
    [
      "00b71248",
      "PARAM",
      [
        "storage",
        "00b60a8c",
        "_ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b711ac",
      "READ",
      [
        "storage",
        "010a1a50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b71248",
      "READ",
      [
        "storage",
        "00c1bb98",
        null,
        "pointer"
      ]
    ],
    [
      "00b71248",
      "PARAM",
      [
        "storage",
        "00b60b54",
        "_ZN8firebase4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b710e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71060.md#insn-00b710e4) · [`00b710f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71060.md#insn-00b710f0) · [`00b71190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71060.md#insn-00b71190)
- 新版 [`00b711ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71128.md#insn-00b711ac) · [`00b711b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71128.md#insn-00b711b8) · [`00b71258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71128.md#insn-00b71258)

~~~diff
- 00b710e4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:990:8"]]
- 00b710e4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b711ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a50:8"]]
+ 00b711ac ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b710e4 bytes 22c944f9
+ 00b711ac bytes 222945f9
- 00b710f0 ["INT_ADD", "register:40f0:8", ["const:b710f0:8", "const:4:8"]]
- 00b710f0 ["CALL", null, ["callee:0047495c:8"]]
+ 00b711b8 ["INT_ADD", "register:40f0:8", ["const:b711b8:8", "const:4:8"]]
+ 00b711b8 ["CALL", null, ["callee:0047495c:8"]]
- 00b710f0 bytes 1b0ee497
+ 00b711b8 bytes e90de497
- 00b71190 ["INT_ADD", "register:40f0:8", ["const:b71190:8", "const:4:8"]]
- 00b71190 ["CALL", null, ["callee:00bde070:8"]]
+ 00b71258 ["INT_ADD", "register:40f0:8", ["const:b71258:8", "const:4:8"]]
+ 00b71258 ["CALL", null, ["callee:00bde070:8"]]
- 00b71190 bytes 8cb30194
+ 00b71258 bytes 86b30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-229b0f1d82a345769e1fabbc6444e395"></a>

### [`00b71250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71250.md) → [`00b71318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71318.md) _ZN8firebase4auth4User40SendEmailVerificationBeforeUpdatingEmailEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60a8c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.09% / 新版 86.09%

CFGの説明率　旧版 9.09% / 新版 8.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71254"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71254"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71258"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b71254",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b71258",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7125c",
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
      "00b7131c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b71320",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00b71324",
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

- 旧版 [`00b71254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71250.md#insn-00b71254) · [`00b71258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71250.md#insn-00b71258) · [`00b7125c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71250.md#insn-00b7125c)

~~~diff
- 00b71254 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b71254 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b71254 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00b71254 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b71254 bytes fa6704a9
- 00b71258 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b71258 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b71258 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00b71258 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b71258 bytes f85f05a9
- 00b7125c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b7125c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b7125c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00b7125c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7125c bytes f65706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61dbc07f50adbee1b0e6dc9bbe365679"></a>

### [`00b71478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71478.md) → [`00b71540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71540.md) _ZN8firebase4auth4User6DeleteEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddb10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb10.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00b60a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b60/00b60a8c.md) [`00b71868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71868.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bddbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbc0.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) [`00b71930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71930.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 14.29% / 新版 15.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7148c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b71488",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7148c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b714a0",
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
      "00b71550",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b71554",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b71568",
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

- 旧版 [`00b71488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71478.md#insn-00b71488) · [`00b7148c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71478.md#insn-00b7148c) · [`00b714a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71478.md#insn-00b714a0)

~~~diff
- 00b71488 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b71488 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b71488 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00b71488 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b71488 bytes f44f07a9
- 00b7148c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7148c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7148c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00b7148c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7148c bytes fd7b08a9
- 00b714a0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b714a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b714a0 bytes e91f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a744d470654b7452033f327871af9b42"></a>

### [`00b71670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71670.md) → [`00b71738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71738.md) _ZNK8firebase4auth4User8metadataEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`0056c6c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c6c4.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c6c4.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

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
      "definition_site": "00b7176c",
      "incomplete_value": true,
      "site": "00b71778",
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
                "const:a58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b716a4",
      "incomplete_value": true,
      "site": "00b716b0",
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
                "const:998:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b71794",
      "incomplete_value": true,
      "site": "00b717a0",
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
                "const:ac8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b716cc",
      "incomplete_value": true,
      "site": "00b716d8",
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
                "const:a08:8"
              ]
            ]
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
      "00b7176c",
      "READ",
      [
        "storage",
        "010a1998",
        null,
        "undefined8"
      ]
    ],
    [
      "00b71794",
      "READ",
      [
        "storage",
        "010a1a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b717a4",
      "READ",
      [
        "storage",
        "010a1a10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b7176c",
      "READ",
      [
        "storage",
        "010a1a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b71794",
      "READ",
      [
        "storage",
        "010a1ac8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b717a4",
      "READ",
      [
        "storage",
        "010a1ad0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b716b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71670.md#insn-00b716b0) · [`00b716d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71670.md#insn-00b716d8) · [`00b71698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71670.md#insn-00b71698)
- 新版 [`00b71778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71738.md#insn-00b71778) · [`00b717a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71738.md#insn-00b717a0) · [`00b71760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71738.md#insn-00b71760)

~~~diff
- 00b716b0 ["INT_ADD", "register:40f0:8", ["const:b716b0:8", "const:4:8"]]
- 00b716b0 ["CALL", null, ["callee:0047495c:8"]]
+ 00b71778 ["INT_ADD", "register:40f0:8", ["const:b71778:8", "const:4:8"]]
+ 00b71778 ["CALL", null, ["callee:0047495c:8"]]
- 00b716b0 bytes ab0ce497
+ 00b71778 bytes 790ce497
- 00b716d8 ["INT_ADD", "register:40f0:8", ["const:b716d8:8", "const:4:8"]]
- 00b716d8 ["CALL", null, ["callee:0056c6c4:8"]]
+ 00b717a0 ["INT_ADD", "register:40f0:8", ["const:b717a0:8", "const:4:8"]]
+ 00b717a0 ["CALL", null, ["callee:0056c6c4:8"]]
- 00b716d8 bytes fbebe797
+ 00b717a0 bytes c9ebe797
- 00b71698 ["INT_ADD", "register:40f0:8", ["const:b71698:8", "const:4:8"]]
- 00b71698 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b71760 ["INT_ADD", "register:40f0:8", ["const:b71760:8", "const:4:8"]]
+ 00b71760 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b71698 bytes 9ab20194
+ 00b71760 bytes 94b20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd93f0119fa1de6e2717d1b2e9633223"></a>

### [`00b717fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b717fc.md) → [`00b718c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b718c4.md) _ZN8firebase4auth22AndroidWrappedUserInfoD0Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde100.md) [`00be0a80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0a80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00be0b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b30.md)

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
      "definition_site": "00b718e0",
      "incomplete_value": true,
      "site": "00b718e4",
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
      "definition_site": "00b71818",
      "incomplete_value": true,
      "site": "00b7181c",
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
      "00b718d8",
      "READ",
      [
        "storage",
        "00c1bb30",
        null,
        "pointer"
      ]
    ],
    [
      "00b718e4",
      "DATA",
      [
        "storage",
        "00c12a68",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00b718d8",
      "READ",
      [
        "storage",
        "00c1bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00b718e4",
      "DATA",
      [
        "storage",
        "00c12b18",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b717fc.md#insn-00b71810) · [`00b71824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b717fc.md#insn-00b71824) · [`00b71834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b717fc.md#insn-00b71834)
- 新版 [`00b718d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b718c4.md#insn-00b718d8) · [`00b718ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b718c4.md#insn-00b718ec) · [`00b718fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b718c4.md#insn-00b718fc)

~~~diff
- 00b71810 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b30:8"]]
- 00b71810 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b718d8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:be0:8"]]
+ 00b718d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b71810 bytes 299945f9
+ 00b718d8 bytes 29f145f9
- 00b71824 ["INT_ADD", "register:40f0:8", ["const:b71824:8", "const:4:8"]]
- 00b71824 ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b718ec ["INT_ADD", "register:40f0:8", ["const:b718ec:8", "const:4:8"]]
+ 00b718ec ["CALL", null, ["callee:00bde1b0:8"]]
- 00b71824 bytes 37b20194
+ 00b718ec bytes 31b20194
- 00b71834 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b71834 ["INT_ADD", "register:40f0:8", ["const:b71834:8", "const:4:8"]]
- 00b71834 ["CALLIND", null, ["register:0:8"]]
+ 00b718fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b718fc ["INT_ADD", "register:40f0:8", ["const:b718fc:8", "const:4:8"]]
+ 00b718fc ["CALLIND", null, ["register:0:8"]]
- 00b71834 bytes 00013fd6
+ 00b718fc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-512f145346947706b430cd5b3b3483cf"></a>

### [`00b71878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71878.md) → [`00b71940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71940.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allo

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d90.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e40.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b719a4",
      "incomplete_value": false,
      "site": "00b719a8",
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
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b718dc",
      "incomplete_value": false,
      "site": "00b718e0",
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
      "00b719a4",
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
      "00b719a4",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b718e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71878.md#insn-00b718e0) · [`00b718a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71878.md#insn-00b718a4) · [`00b718b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71878.md#insn-00b718b0)
- 新版 [`00b719a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71940.md#insn-00b719a8) · [`00b7196c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71940.md#insn-00b7196c) · [`00b71978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71940.md#insn-00b71978)

~~~diff
- 00b718e0 ["INT_ADD", "register:40f0:8", ["const:b718e0:8", "const:4:8"]]
- 00b718e0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b719a8 ["INT_ADD", "register:40f0:8", ["const:b719a8:8", "const:4:8"]]
+ 00b719a8 ["CALL", null, ["callee:00bde130:8"]]
- 00b718e0 bytes e8b10194
+ 00b719a8 bytes e2b10194
- 00b718a4 ["INT_ADD", "register:40f0:8", ["const:b718a4:8", "const:4:8"]]
- 00b718a4 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b7196c ["INT_ADD", "register:40f0:8", ["const:b7196c:8", "const:4:8"]]
+ 00b7196c ["CALL", null, ["callee:00bddbd0:8"]]
- 00b718a4 bytes 9fb00194
+ 00b7196c bytes 99b00194
- 00b718b0 ["INT_ADD", "register:40f0:8", ["const:b718b0:8", "const:4:8"]]
- 00b718b0 ["CALL", null, ["callee:00bddfb0:8"]]
+ 00b71978 ["INT_ADD", "register:40f0:8", ["const:b71978:8", "const:4:8"]]
+ 00b71978 ["CALL", null, ["callee:00bddfb0:8"]]
- 00b718b0 bytes 94b10194
+ 00b71978 bytes 8eb10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a570875c4b3e7ea8f1844ee1458b524b"></a>

### [`00b71980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71980.md) → [`00b71a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71a48.md) _ZN8firebase4auth14FutureCallbackINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvP7_JNIEnvP8_jobjectNS_4util12FutureR

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00b6ede4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6e/00b6ede4.md) · 呼出先 6件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddb40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb40.md) [`00bdde80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde80.md) [`00be0c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c20.md)
- 新版 呼出元 1件 [`00b6eeac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6eeac.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00be0cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0cd0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b719b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71980.md#insn-00b719b8) · [`00b719d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71980.md#insn-00b719d0) · [`00b719f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71980.md#insn-00b719f8)
- 新版 [`00b71a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71a48.md#insn-00b71a80) · [`00b71a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71a48.md#insn-00b71a98) · [`00b71ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71a48.md#insn-00b71ac0)

~~~diff
- 00b719b8 ["INT_ADD", "register:40f0:8", ["const:b719b8:8", "const:4:8"]]
- 00b719b8 ["CALL", null, ["callee:00be0cd0:8"]]
+ 00b71a80 ["INT_ADD", "register:40f0:8", ["const:b71a80:8", "const:4:8"]]
+ 00b71a80 ["CALL", null, ["callee:00be0cd0:8"]]
- 00b719b8 bytes 9abc0194
+ 00b71a80 bytes 94bc0194
- 00b719d0 ["INT_ADD", "register:40f0:8", ["const:b719d0:8", "const:4:8"]]
- 00b719d0 ["CALL", null, ["callee:00bddf30:8"]]
+ 00b71a98 ["INT_ADD", "register:40f0:8", ["const:b71a98:8", "const:4:8"]]
+ 00b71a98 ["CALL", null, ["callee:00bddf30:8"]]
- 00b719d0 bytes 2cb10194
+ 00b71a98 bytes 26b10194
- 00b719f8 ["INT_ADD", "register:40f0:8", ["const:b719f8:8", "const:4:8"]]
- 00b719f8 ["CALL", null, ["callee:00be0e30:8"]]
+ 00b71ac0 ["INT_ADD", "register:40f0:8", ["const:b71ac0:8", "const:4:8"]]
+ 00b71ac0 ["CALL", null, ["callee:00be0e30:8"]]
- 00b719f8 bytes e2bc0194
+ 00b71ac0 bytes dcbc0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c76a32fa8f21bf3b639f229fc88ac3de"></a>

### [`00b71a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71a54.md) → [`00b71b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71b1c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS_4auth14Fut

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0d80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0d80.md) · 呼出先 10件 [`00bddb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb20.md) [`00bddb30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddb30.md) [`00bddeb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddeb0.md) [`00bdded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdded0.md) [`00bddee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddee0.md)
- 新版 呼出元 1件 [`00be0e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e30.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)

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
      "definition_site": "00b71b88",
      "incomplete_value": false,
      "site": "00b71b8c",
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
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b71ac0",
      "incomplete_value": false,
      "site": "00b71ac4",
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
      "00b71b88",
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
      "00b71b88",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71a54.md#insn-00b71ac4) · [`00b71a88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71a54.md#insn-00b71a88) · [`00b71a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71a54.md#insn-00b71a94)
- 新版 [`00b71b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71b1c.md#insn-00b71b8c) · [`00b71b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71b1c.md#insn-00b71b50) · [`00b71b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71b1c.md#insn-00b71b5c)

~~~diff
- 00b71ac4 ["INT_ADD", "register:40f0:8", ["const:b71ac4:8", "const:4:8"]]
- 00b71ac4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b71b8c ["INT_ADD", "register:40f0:8", ["const:b71b8c:8", "const:4:8"]]
+ 00b71b8c ["CALL", null, ["callee:00bde130:8"]]
- 00b71ac4 bytes 6fb10194
+ 00b71b8c bytes 69b10194
- 00b71a88 ["INT_ADD", "register:40f0:8", ["const:b71a88:8", "const:4:8"]]
- 00b71a88 ["CALL", null, ["callee:00bddbd0:8"]]
+ 00b71b50 ["INT_ADD", "register:40f0:8", ["const:b71b50:8", "const:4:8"]]
+ 00b71b50 ["CALL", null, ["callee:00bddbd0:8"]]
- 00b71a88 bytes 26b00194
+ 00b71b50 bytes 20b00194
- 00b71a94 ["INT_ADD", "register:40f0:8", ["const:b71a94:8", "const:4:8"]]
- 00b71a94 ["CALL", null, ["callee:00bddfb0:8"]]
+ 00b71b5c ["INT_ADD", "register:40f0:8", ["const:b71b5c:8", "const:4:8"]]
+ 00b71b5c ["CALL", null, ["callee:00bddfb0:8"]]
- 00b71a94 bytes 1bb10194
+ 00b71b5c bytes 15b10194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85c17ad0c51882c9aa5fcc75a1e6b92e"></a>

### [`00b71b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71b8c.md) → [`00b71c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71c54.md) _ZN8firebase4auth17UserInfoInterfaceC2ERKS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0da0.md) · 呼出先 1件 [`00bde630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde630.md)
- 新版 呼出元 1件 [`00be0e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e50.md) · 呼出先 1件 [`00bde6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6e0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71bc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b71c90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b71bc4",
      "incomplete_value": true,
      "site": "00b71bcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "00b71c70",
      "READ",
      [
        "storage",
        "00c1ba98",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b71bc8",
      "DATA",
      [
        "storage",
        "00c12ad0",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00b71c70",
      "READ",
      [
        "storage",
        "00c1bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00b71c90",
      "DATA",
      [
        "storage",
        "00c12b80",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71b8c.md#insn-00b71bc8) · [`00b71bcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71b8c.md#insn-00b71bcc) · [`00b71be8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71b8c.md#insn-00b71be8)
- 新版 [`00b71c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71c54.md#insn-00b71c94) · [`00b71cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71c54.md#insn-00b71cb0)

~~~diff
- 00b71bc8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b71bc8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b71bc8 ["INT_ADD", "register:40a8:8", ["register:40a8:8", "const:20:8"]]
- 00b71bc8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b71bc8 bytes a80602f8
- 00b71bcc ["INT_ADD", "register:40f0:8", ["const:b71bcc:8", "const:4:8"]]
- 00b71bcc ["CALL", null, ["callee:00bde6e0:8"]]
+ 00b71c94 ["INT_ADD", "register:40f0:8", ["const:b71c94:8", "const:4:8"]]
+ 00b71c94 ["CALL", null, ["callee:00bde6e0:8"]]
- 00b71bcc bytes 99b20194
+ 00b71c94 bytes 93b20194
- 00b71be8 ["INT_ADD", "register:40f0:8", ["const:b71be8:8", "const:4:8"]]
- 00b71be8 ["CALL", null, ["callee:00bde6e0:8"]]
+ 00b71cb0 ["INT_ADD", "register:40f0:8", ["const:b71cb0:8", "const:4:8"]]
+ 00b71cb0 ["CALL", null, ["callee:00bde6e0:8"]]
- 00b71be8 bytes 92b20194
+ 00b71cb0 bytes 8cb20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19b3c48a52928a48fac3d9419c031dcc"></a>

### [`00b71cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71cf4.md) → [`00b71dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71dbc.md) _ZNSt6__ndk16vectorIN8firebase4auth17UserInfoInterfaceENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEvOT_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0dc0.md) · 呼出先 4件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdddb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdddb0.md) [`00be0da0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0da0.md)
- 新版 呼出元 1件 [`00be0e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e70.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md) [`00be0e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 84.27% / 新版 84.27%

CFGの説明率　旧版 47.83% / 新版 47.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b71d48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00b71e10"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00b71dbc",
      "incomplete_value": true,
      "site": "00b71dc8",
      "value": [
        "INT_SUB",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "unmatched:00b71d48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71f18"
      ]
    ]
  ],
  "added": [
    [
      "00b71e10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b71f18"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b71d48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71cf4.md#insn-00b71d48) · [`00b71dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71cf4.md#insn-00b71dc8) · [`00b71e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b71/00b71cf4.md#insn-00b71e10)
- 新版 [`00b71e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71dbc.md#insn-00b71e90) · [`00b71ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b71/00b71dbc.md#insn-00b71ed8)

~~~diff
- 00b71d48 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00b71d48 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00b71d48 ["CBRANCH", null, ["local:b17:8", "tmp:1:1"]]
- 00b71d48 bytes 48080054
- 00b71dc8 ["INT_ADD", "register:40f0:8", ["const:b71dc8:8", "const:4:8"]]
- 00b71dc8 ["CALL", null, ["callee:00be0e50:8"]]
+ 00b71e90 ["INT_ADD", "register:40f0:8", ["const:b71e90:8", "const:4:8"]]
+ 00b71e90 ["CALL", null, ["callee:00be0e50:8"]]
- 00b71dc8 bytes f6bb0194
+ 00b71e90 bytes f0bb0194
- 00b71e10 ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
- 00b71e10 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00b71ed8 ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
+ 00b71ed8 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00b71e10 bytes 180100b4
+ 00b71ed8 bytes 180100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

