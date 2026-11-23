# v16.0.0 → v16.0.1 · 最優先の変更候補 (88)

[一覧の目次](README.md)

<a id="compare-15b8e9e4a9549664b1927042cb01aa29"></a>

### [`00c16c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16c70.md) → [`00c17098`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17098.md) _ZNKSt6__ndk110__time_put8__do_putEPwRS1_PK2tmcc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e270.md) · 呼出先 5件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c5dbb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbb0.md) [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e260.md) [`00c5e280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e280.md)
- 新版 呼出元 1件 [`00c5e670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e670.md) · 呼出先 5件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c5dfb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfb0.md) [`00c5e570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e570.md) [`00c5e660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e660.md) [`00c5e680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e680.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c17170",
      "incomplete_value": false,
      "site": "00c17174",
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
            "const:de5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16d48",
      "incomplete_value": false,
      "site": "00c16d4c",
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
            "const:d18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c17170",
      "PARAM",
      [
        "storage",
        "0029fd18",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c17170",
      "PARAM",
      [
        "storage",
        "0029fde5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c16d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16c70.md#insn-00c16d4c) · [`00c16cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16c70.md#insn-00c16cd0) · [`00c16ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16c70.md#insn-00c16ce8)
- 新版 `00c17174`（命令位置の公開資料なし） · `00c170f8`（命令位置の公開資料なし） · `00c17110`（命令位置の公開資料なし）

~~~diff
- 00c16d4c ["INT_ADD", "register:40f0:8", ["const:c16d4c:8", "const:4:8"]]
- 00c16d4c ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c17174 ["INT_ADD", "register:40f0:8", ["const:c17174:8", "const:4:8"]]
+ 00c17174 ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c16d4c bytes 991b0194
+ 00c17174 bytes 8f1b0194
- 00c16cd0 ["INT_ADD", "register:40f0:8", ["const:c16cd0:8", "const:4:8"]]
- 00c16cd0 ["CALL", null, ["callee:00c5e660:8"]]
+ 00c170f8 ["INT_ADD", "register:40f0:8", ["const:c170f8:8", "const:4:8"]]
+ 00c170f8 ["CALL", null, ["callee:00c5e660:8"]]
- 00c16cd0 bytes 641d0194
+ 00c170f8 bytes 5a1d0194
- 00c16ce8 ["INT_ADD", "register:40f0:8", ["const:c16ce8:8", "const:4:8"]]
- 00c16ce8 ["CALL", null, ["callee:00c5e570:8"]]
+ 00c17110 ["INT_ADD", "register:40f0:8", ["const:c17110:8", "const:4:8"]]
+ 00c17110 ["CALL", null, ["callee:00c5e570:8"]]
- 00c16ce8 bytes 221d0194
+ 00c17110 bytes 181d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cad72f4e7e0667b211fa2284ba0ee645"></a>

### [`00c16ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16ec0.md) → [`00c172e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c172e8.md) _ZNKSt6__ndk110moneypunctIwLb0EE16do_negative_signEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c172f4",
      "incomplete_value": true,
      "site": "00c172fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16ecc",
      "incomplete_value": true,
      "site": "00c16ed4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f80:8"
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
      "00c172f4",
      "READ",
      [
        "storage",
        "002c3f80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c172f4",
      "READ",
      [
        "storage",
        "002c3fc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c16ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16ec0.md#insn-00c16ecc)
- 新版 `00c172f4`（命令位置の公開資料なし）

~~~diff
- 00c16ecc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f80:8"]]
- 00c16ecc ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c16ecc ["COPY", "register:5008:8", ["const:0:8"]]
- 00c16ecc ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c172f4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc0:8"]]
+ 00c172f4 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c172f4 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c172f4 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c16ecc bytes 20c147fd
+ 00c172f4 bytes 20e147fd
~~~


<a id="compare-d5e4d14258ed6717f6cc89da85c5c702"></a>

### [`00c16f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16f50.md) → [`00c17378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17378.md) _ZNKSt6__ndk110moneypunctIwLb1EE16do_negative_signEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c17384",
      "incomplete_value": true,
      "site": "00c1738c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c16f5c",
      "incomplete_value": true,
      "site": "00c16f64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f80:8"
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
      "00c17384",
      "READ",
      [
        "storage",
        "002c3f80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c17384",
      "READ",
      [
        "storage",
        "002c3fc0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c16f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16f50.md#insn-00c16f5c)
- 新版 `00c17384`（命令位置の公開資料なし）

~~~diff
- 00c16f5c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f80:8"]]
- 00c16f5c ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
- 00c16f5c ["COPY", "register:5008:8", ["const:0:8"]]
- 00c16f5c ["COPY", "register:5010:8", ["const:0:8"]]
+ 00c17384 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc0:8"]]
+ 00c17384 ["LOAD", "register:5000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c17384 ["COPY", "register:5008:8", ["const:0:8"]]
+ 00c17384 ["COPY", "register:5010:8", ["const:0:8"]]
- 00c16f5c bytes 20c147fd
+ 00c17384 bytes 20e147fd
~~~


<a id="compare-4e983f0895adbae1f900c121385e5b8b"></a>

### [`00c17388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17388.md) → [`00c177b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c177b0.md) _ZNKSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_bRNS_8ios_baseERjRe

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bd0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c17af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17af4.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1780c",
      "incomplete_value": true,
      "site": "00c17814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c173e4",
      "incomplete_value": true,
      "site": "00c173ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c178b8",
      "incomplete_value": true,
      "site": "00c178c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:d8c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17490",
      "incomplete_value": true,
      "site": "00c1749c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:cbf:8"
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c17840",
      "incomplete_value": true,
      "site": "00c17848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c17418",
      "incomplete_value": true,
      "site": "00c17420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c177e0",
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c177f8",
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c1780c",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c177e0",
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c177f8",
      "DATA",
      [
        "storage",
        "00c17af4",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c1780c",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c17420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17388.md#insn-00c17420) · [`00c1754c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17388.md#insn-00c1754c) · [`00c17664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17388.md#insn-00c17664)
- 新版 `00c17848`（命令位置の公開資料なし） · `00c17974`（命令位置の公開資料なし） · `00c17a8c`（命令位置の公開資料なし）

~~~diff
- 00c17420 ["INT_ADD", "register:40f0:8", ["const:c17420:8", "const:4:8"]]
- 00c17420 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c17848 ["INT_ADD", "register:40f0:8", ["const:c17848:8", "const:4:8"]]
+ 00c17848 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c17420 bytes b0190194
+ 00c17848 bytes a6190194
- 00c1754c ["INT_ADD", "register:40f0:8", ["const:c1754c:8", "const:4:8"]]
- 00c1754c ["CALL", null, ["callee:00c5e6a0:8"]]
+ 00c17974 ["INT_ADD", "register:40f0:8", ["const:c17974:8", "const:4:8"]]
+ 00c17974 ["CALL", null, ["callee:00c5e6a0:8"]]
- 00c1754c bytes 551b0194
+ 00c17974 bytes 4b1b0194
- 00c17664 ["INT_ADD", "register:40f0:8", ["const:c17664:8", "const:4:8"]]
- 00c17664 ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c17a8c ["INT_ADD", "register:40f0:8", ["const:c17a8c:8", "const:4:8"]]
+ 00c17a8c ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c17664 bytes 53190194
+ 00c17a8c bytes 49190194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd34db1149d516d8e0aa79051b871db8"></a>

### [`00c176d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176d4.md) → [`00c17afc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17afc.md) _ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE8__do_getERS4_S4_bRKNS_6localeEjRjRbRKNS_5ctypeIcEERNS_10unique_ptr

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e290.md) · 呼出先 11件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md)
- 新版 呼出元 1件 [`00c5e690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e690.md) · 呼出先 11件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c17af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17af4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_value` 3件

アドレスに依存する影響 `branch_value` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c17c68",
      "incomplete_value": true,
      "site": "00c17c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17840",
      "incomplete_value": true,
      "site": "00c17848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c17f44",
      "incomplete_value": true,
      "site": "00c17f48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17b1c",
      "incomplete_value": true,
      "site": "00c17b20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:928:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c17f7c",
      "incomplete_value": true,
      "site": "00c17f80",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4050:8"
              ],
              [
                "leaf",
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c17b54",
      "incomplete_value": true,
      "site": "00c17b58",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4050:8"
              ],
              [
                "leaf",
                "const:928:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 51,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c17c68",
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c17c70",
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c17e8c",
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c17c68",
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c17c70",
      "DATA",
      [
        "storage",
        "00c17af4",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c17e8c",
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c17748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176d4.md#insn-00c17748) · [`00c177e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176d4.md#insn-00c177e4) · [`00c17840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176d4.md#insn-00c17840)
- 新版 `00c17b70`（命令位置の公開資料なし） · `00c17c0c`（命令位置の公開資料なし） · `00c17c68`（命令位置の公開資料なし）

~~~diff
- 00c17748 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c17748 ["INT_ADD", "register:40f0:8", ["const:c17748:8", "const:4:8"]]
- 00c17748 ["CALLIND", null, ["register:0:8"]]
+ 00c17b70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c17b70 ["INT_ADD", "register:40f0:8", ["const:c17b70:8", "const:4:8"]]
+ 00c17b70 ["CALLIND", null, ["register:0:8"]]
- 00c17748 bytes 00013fd6
+ 00c17b70 bytes 00013fd6
- 00c177e4 ["INT_ADD", "register:40f0:8", ["const:c177e4:8", "const:4:8"]]
- 00c177e4 ["CALL", null, ["callee:00c5e6b0:8"]]
+ 00c17c0c ["INT_ADD", "register:40f0:8", ["const:c17c0c:8", "const:4:8"]]
+ 00c17c0c ["CALL", null, ["callee:00c5e6b0:8"]]
- 00c177e4 bytes b31a0194
+ 00c17c0c bytes a91a0194
- 00c17840 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7d0:8"]]
- 00c17840 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c17c68 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bd0:8"]]
+ 00c17c68 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c17840 bytes 29e943f9
+ 00c17c68 bytes 29e945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c569ccdc7f9a694b78c52b8589bc0fb"></a>

### [`00c188dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c188dc.md) → [`00c18d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18d04.md) _ZNKSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_getES4_S4_bRNS_8ios_baseERjRNS_12basic_stringIcS3_NS_9allocato

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c18b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c18b9c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c17af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17af4.md) [`00c18fc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c18/00c18fc4.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 98.09% / 新版 98.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c18d4c",
      "incomplete_value": true,
      "site": "00c18d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c18924",
      "incomplete_value": true,
      "site": "00c18924",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
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
      "definition_site": "00c18d68",
      "incomplete_value": true,
      "site": "00c18d68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c18940",
      "incomplete_value": true,
      "site": "00c18940",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c18d70",
      "incomplete_value": true,
      "site": "00c18d74",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c18948",
      "incomplete_value": true,
      "site": "00c1894c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "00c18d34",
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c18d4c",
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c18d60",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c18d34",
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c18d4c",
      "DATA",
      [
        "storage",
        "00c17af4",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c18d60",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c18974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c188dc.md#insn-00c18974) · [`00c1890c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c188dc.md#insn-00c1890c) · [`00c18930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c18/00c188dc.md#insn-00c18930)
- 新版 `00c18d9c`（命令位置の公開資料なし） · `00c18d34`（命令位置の公開資料なし） · `00c18d58`（命令位置の公開資料なし）

~~~diff
- 00c18974 ["INT_ADD", "register:40f0:8", ["const:c18974:8", "const:4:8"]]
- 00c18974 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c18d9c ["INT_ADD", "register:40f0:8", ["const:c18d9c:8", "const:4:8"]]
+ 00c18d9c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c18974 bytes 5b140194
+ 00c18d9c bytes 51140194
- 00c1890c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:7d0:8"]]
- 00c1890c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c18d34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd0:8"]]
+ 00c18d34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1890c bytes 08e943f9
+ 00c18d34 bytes 08e945f9
- 00c18930 ["INT_ADD", "register:40f0:8", ["const:c18930:8", "const:4:8"]]
- 00c18930 ["CALL", null, ["callee:00c58270:8"]]
+ 00c18d58 ["INT_ADD", "register:40f0:8", ["const:c18d58:8", "const:4:8"]]
+ 00c18d58 ["CALL", null, ["callee:00c58270:8"]]
- 00c18930 bytes 50fd0094
+ 00c18d58 bytes 46fd0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f8033787f2a8f6325d7a51c8da8fb6e"></a>

### [`00c19224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c19224.md) → [`00c1964c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c19/00c1964c.md) _ZNKSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_getES4_S4_bRNS_8ios_baseERjRe

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c17af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17af4.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 95.94% / 新版 95.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c19694",
      "incomplete_value": true,
      "site": "00c19694",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1926c",
      "incomplete_value": true,
      "site": "00c1926c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c196a8",
      "incomplete_value": true,
      "site": "00c196b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c19280",
      "incomplete_value": true,
      "site": "00c19288",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
      "definition_site": "00c19754",
      "incomplete_value": true,
      "site": "00c19760",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:d8c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1932c",
      "incomplete_value": true,
      "site": "00c19338",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:cbf:8"
              ]
            ]
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
      "00c1967c",
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c19694",
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c196a8",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c1967c",
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c19694",
      "DATA",
      [
        "storage",
        "00c17af4",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c196a8",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c192bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c19224.md#insn-00c192bc) · [`00c193f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c19224.md#insn-00c193f0) · [`00c19504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c19224.md#insn-00c19504)
- 新版 `00c196e4`（命令位置の公開資料なし） · `00c19818`（命令位置の公開資料なし） · `00c1992c`（命令位置の公開資料なし）

~~~diff
- 00c192bc ["INT_ADD", "register:40f0:8", ["const:c192bc:8", "const:4:8"]]
- 00c192bc ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c196e4 ["INT_ADD", "register:40f0:8", ["const:c196e4:8", "const:4:8"]]
+ 00c196e4 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c192bc bytes 09120194
+ 00c196e4 bytes ff110194
- 00c193f0 ["INT_ADD", "register:40f0:8", ["const:c193f0:8", "const:4:8"]]
- 00c193f0 ["CALL", null, ["callee:00c5e6a0:8"]]
+ 00c19818 ["INT_ADD", "register:40f0:8", ["const:c19818:8", "const:4:8"]]
+ 00c19818 ["CALL", null, ["callee:00c5e6a0:8"]]
- 00c193f0 bytes ac130194
+ 00c19818 bytes a2130194
- 00c19504 ["INT_ADD", "register:40f0:8", ["const:c19504:8", "const:4:8"]]
- 00c19504 ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c1992c ["INT_ADD", "register:40f0:8", ["const:c1992c:8", "const:4:8"]]
+ 00c1992c ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c19504 bytes ab110194
+ 00c1992c bytes a1110194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c4419f5880fe9a326e2579516643339"></a>

### [`00c1956c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c1956c.md) → [`00c19994`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c19/00c19994.md) _ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE8__do_getERS4_S4_bRKNS_6localeEjRjRbRKNS_5ctypeIwEERNS_10unique_ptr

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5e2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e2c0.md) · 呼出先 11件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c176cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c176cc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)
- 新版 呼出元 1件 [`00c5e6c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e6c0.md) · 呼出先 11件 [`00440c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440c3c.md) [`00c17af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c17/00c17af4.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c5a020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.97% / 新版 98.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c19b24",
      "incomplete_value": true,
      "site": "00c19b2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c196fc",
      "incomplete_value": true,
      "site": "00c19704",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c19de8",
      "incomplete_value": true,
      "site": "00c19df0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c199c0",
      "incomplete_value": true,
      "site": "00c199c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:928:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c19e3c",
      "incomplete_value": true,
      "site": "00c19e40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c19a14",
      "incomplete_value": true,
      "site": "00c19a18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:928:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c19b24",
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c19b2c",
      "DATA",
      [
        "storage",
        "00c176cc",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c19d30",
      "READ",
      [
        "storage",
        "00c9b7d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c19b24",
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ],
    [
      "00c19b2c",
      "DATA",
      [
        "storage",
        "00c17af4",
        "_ZNSt6__ndk112__do_nothingEPv",
        null
      ]
    ],
    [
      "00c19d30",
      "READ",
      [
        "storage",
        "00c9bbd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c195f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c1956c.md#insn-00c195f4) · [`00c1962c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c1956c.md#insn-00c1962c) · [`00c196a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c19/00c1956c.md#insn-00c196a8)
- 新版 `00c19a1c`（命令位置の公開資料なし） · `00c19a54`（命令位置の公開資料なし） · `00c19ad0`（命令位置の公開資料なし）

~~~diff
- 00c195f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c195f4 ["INT_ADD", "register:40f0:8", ["const:c195f4:8", "const:4:8"]]
- 00c195f4 ["CALLIND", null, ["register:0:8"]]
+ 00c19a1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c19a1c ["INT_ADD", "register:40f0:8", ["const:c19a1c:8", "const:4:8"]]
+ 00c19a1c ["CALLIND", null, ["register:0:8"]]
- 00c195f4 bytes 00013fd6
+ 00c19a1c bytes 00013fd6
- 00c1962c ["COPY", "register:0:8", ["register:4040:8"]]
- 00c1962c ["INT_ADD", "register:40f0:8", ["const:c1962c:8", "const:4:8"]]
- 00c1962c ["CALLIND", null, ["register:0:8"]]
+ 00c19a54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c19a54 ["INT_ADD", "register:40f0:8", ["const:c19a54:8", "const:4:8"]]
+ 00c19a54 ["CALLIND", null, ["register:0:8"]]
- 00c1962c bytes 00013fd6
+ 00c19a54 bytes 00013fd6
- 00c196a8 ["INT_ADD", "register:40f0:8", ["const:c196a8:8", "const:4:8"]]
- 00c196a8 ["CALL", null, ["callee:00c5e6d0:8"]]
+ 00c19ad0 ["INT_ADD", "register:40f0:8", ["const:c19ad0:8", "const:4:8"]]
+ 00c19ad0 ["CALL", null, ["callee:00c5e6d0:8"]]
- 00c196a8 bytes 0a130194
+ 00c19ad0 bytes 00130194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68f539f5a811a9171b721ea6f734efe7"></a>

### [`00c1b10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b10c.md) → [`00c1b534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b534.md) _ZNKSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_bRNS_8ios_baseEce

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c1b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 95.14% / 新版 95.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1b60c",
      "incomplete_value": true,
      "site": "00c1b614",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c1b1e4",
      "incomplete_value": true,
      "site": "00c1b1ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c1b8d4",
      "incomplete_value": true,
      "site": "00c1b8d4",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1b4ac",
      "incomplete_value": true,
      "site": "00c1b4ac",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1b61c",
      "incomplete_value": true,
      "site": "00c1b620",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1b1f4",
      "incomplete_value": true,
      "site": "00c1b1f8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00c1b568",
      "PARAM",
      [
        "storage",
        "002b1770",
        null,
        "string"
      ]
    ],
    [
      "00c1b59c",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1b5a4",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1b568",
      "PARAM",
      [
        "storage",
        "002b17b0",
        null,
        "string"
      ]
    ],
    [
      "00c1b59c",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1b5a4",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1b220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b10c.md#insn-00c1b220) · [`00c1b490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b10c.md#insn-00c1b490) · [`00c1b4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b10c.md#insn-00c1b4a8)
- 新版 `00c1b648`（命令位置の公開資料なし） · `00c1b8b8`（命令位置の公開資料なし） · `00c1b8d0`（命令位置の公開資料なし）

~~~diff
- 00c1b220 ["INT_ADD", "register:40f0:8", ["const:c1b220:8", "const:4:8"]]
- 00c1b220 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c1b648 ["INT_ADD", "register:40f0:8", ["const:c1b648:8", "const:4:8"]]
+ 00c1b648 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1b220 bytes 300a0194
+ 00c1b648 bytes 260a0194
- 00c1b490 ["INT_ADD", "register:40f0:8", ["const:c1b490:8", "const:4:8"]]
- 00c1b490 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c1b8b8 ["INT_ADD", "register:40f0:8", ["const:c1b8b8:8", "const:4:8"]]
+ 00c1b8b8 ["CALL", null, ["callee:00c57e50:8"]]
- 00c1b490 bytes 70f10094
+ 00c1b8b8 bytes 66f10094
- 00c1b4a8 ["INT_ADD", "register:40f0:8", ["const:c1b4a8:8", "const:4:8"]]
- 00c1b4a8 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c1b8d0 ["INT_ADD", "register:40f0:8", ["const:c1b8d0:8", "const:4:8"]]
+ 00c1b8d0 ["CALL", null, ["callee:00c5d220:8"]]
- 00c1b4a8 bytes 5e060194
+ 00c1b8d0 bytes 54060194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e6b48bca31930d300444eccaf6be0b4"></a>

### [`00c1bd04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1bd04.md) → [`00c1c12c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1c12c.md) _ZNKSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE6do_putES4_bRNS_8ios_baseEcRKNS_12basic_stringIcS3_NS_9allocatorIc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00459628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459628.md) [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00459668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459668.md) [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 99.47% / 新版 99.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1c17c",
      "incomplete_value": true,
      "site": "00c1c17c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c1bd54",
      "incomplete_value": true,
      "site": "00c1bd54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1c184",
      "incomplete_value": true,
      "site": "00c1c188",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1bd5c",
      "incomplete_value": true,
      "site": "00c1bd60",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1c1a8",
      "incomplete_value": true,
      "site": "00c1c1b0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
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
      "definition_site": "00c1bd80",
      "incomplete_value": true,
      "site": "00c1bd88",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
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
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1c174",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c1c17c",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1c180",
      "READ",
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
      "00c1c174",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c1c17c",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1c180",
      "READ",
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

- 旧版 [`00c1bd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1bd04.md#insn-00c1bd88) · [`00c1bd44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1bd04.md#insn-00c1bd44) · [`00c1bd4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1bd04.md#insn-00c1bd4c)
- 新版 `00c1c1b0`（命令位置の公開資料なし） · `00c1c16c`（命令位置の公開資料なし） · `00c1c174`（命令位置の公開資料なし）

~~~diff
- 00c1bd88 ["INT_ADD", "register:40f0:8", ["const:c1bd88:8", "const:4:8"]]
- 00c1bd88 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c1c1b0 ["INT_ADD", "register:40f0:8", ["const:c1c1b0:8", "const:4:8"]]
+ 00c1c1b0 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1bd88 bytes 56070194
+ 00c1c1b0 bytes 4c070194
- 00c1bd44 ["INT_ADD", "register:40f0:8", ["const:c1bd44:8", "const:4:8"]]
- 00c1bd44 ["CALL", null, ["callee:00c58270:8"]]
+ 00c1c16c ["INT_ADD", "register:40f0:8", ["const:c1c16c:8", "const:4:8"]]
+ 00c1c16c ["CALL", null, ["callee:00c58270:8"]]
- 00c1bd44 bytes 4bf00094
+ 00c1c16c bytes 41f00094
- 00c1bd4c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:830:8"]]
- 00c1bd4c ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c1c174 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c30:8"]]
+ 00c1c174 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1bd4c bytes f71a44f9
+ 00c1c174 bytes f71a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-483d963e777b9fc76ac58e1aee77fc8c"></a>

### [`00c1c088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c088.md) → [`00c1c4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1c/00c1c4b0.md) _ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwe

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c118e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c1b9e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1b/00c1b9e0.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 95.20% / 新版 95.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1c588",
      "incomplete_value": true,
      "site": "00c1c590",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1c160",
      "incomplete_value": true,
      "site": "00c1c168",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c1c85c",
      "incomplete_value": true,
      "site": "00c1c85c",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1c434",
      "incomplete_value": true,
      "site": "00c1c434",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1c598",
      "incomplete_value": true,
      "site": "00c1c59c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1c170",
      "incomplete_value": true,
      "site": "00c1c174",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
      "00c1c4e4",
      "PARAM",
      [
        "storage",
        "002b1770",
        null,
        "string"
      ]
    ],
    [
      "00c1c518",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1c520",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1c4e4",
      "PARAM",
      [
        "storage",
        "002b17b0",
        null,
        "string"
      ]
    ],
    [
      "00c1c518",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1c520",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1c0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c088.md#insn-00c1c0d8) · [`00c1c110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c088.md#insn-00c1c110) · [`00c1c19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c088.md#insn-00c1c19c)
- 新版 `00c1c500`（命令位置の公開資料なし） · `00c1c538`（命令位置の公開資料なし） · `00c1c5c4`（命令位置の公開資料なし）

~~~diff
- 00c1c0d8 ["INT_ADD", "register:40f0:8", ["const:c1c0d8:8", "const:4:8"]]
- 00c1c0d8 ["CALL", null, ["callee:00c5e100:8"]]
+ 00c1c500 ["INT_ADD", "register:40f0:8", ["const:c1c500:8", "const:4:8"]]
+ 00c1c500 ["CALL", null, ["callee:00c5e100:8"]]
- 00c1c0d8 bytes 0a070194
+ 00c1c500 bytes 00070194
- 00c1c110 ["INT_ADD", "register:40f0:8", ["const:c1c110:8", "const:4:8"]]
- 00c1c110 ["CALL", null, ["callee:00c1b9e0:8"]]
+ 00c1c538 ["INT_ADD", "register:40f0:8", ["const:c1c538:8", "const:4:8"]]
+ 00c1c538 ["CALL", null, ["callee:00c1b9e0:8"]]
- 00c1c110 bytes 2afdff97
+ 00c1c538 bytes 2afdff97
- 00c1c19c ["INT_ADD", "register:40f0:8", ["const:c1c19c:8", "const:4:8"]]
- 00c1c19c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c1c5c4 ["INT_ADD", "register:40f0:8", ["const:c1c5c4:8", "const:4:8"]]
+ 00c1c5c4 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1c19c bytes 51060194
+ 00c1c5c4 bytes 47060194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7f1ddc9e2ec8693bfc71888d47c6245"></a>

### [`00c1cbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1cbec.md) → [`00c1d014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d014.md) _ZNKSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE6do_putES4_bRNS_8ios_baseEwRKNS_12basic_stringIwS3_NS_9allocatorIw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c114bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c11/00c114bc.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c118e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c11/00c118e4.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.48% / 新版 99.48%

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
      "definition_site": "00c1d064",
      "incomplete_value": true,
      "site": "00c1d064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1cc3c",
      "incomplete_value": true,
      "site": "00c1cc3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
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
      "definition_site": "00c1d090",
      "incomplete_value": true,
      "site": "00c1d098",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1cc68",
      "incomplete_value": true,
      "site": "00c1cc70",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
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
      "definition_site": "00c1d08c",
      "incomplete_value": false,
      "site": "00c1d098",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c1cc64",
      "incomplete_value": false,
      "site": "00c1cc70",
      "value": [
        "leaf",
        "const:c35b90:8"
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
      "00c1d05c",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c1d064",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1d068",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1d05c",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c1d064",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1d068",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1cc70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1cbec.md#insn-00c1cc70) · [`00c1cc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1cbec.md#insn-00c1cc2c) · [`00c1cc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1cbec.md#insn-00c1cc34)
- 新版 `00c1d098`（命令位置の公開資料なし） · `00c1d054`（命令位置の公開資料なし） · `00c1d05c`（命令位置の公開資料なし）

~~~diff
- 00c1cc70 ["INT_ADD", "register:40f0:8", ["const:c1cc70:8", "const:4:8"]]
- 00c1cc70 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c1d098 ["INT_ADD", "register:40f0:8", ["const:c1d098:8", "const:4:8"]]
+ 00c1d098 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1cc70 bytes 9c030194
+ 00c1d098 bytes 92030194
- 00c1cc2c ["INT_ADD", "register:40f0:8", ["const:c1cc2c:8", "const:4:8"]]
- 00c1cc2c ["CALL", null, ["callee:00c58270:8"]]
+ 00c1d054 ["INT_ADD", "register:40f0:8", ["const:c1d054:8", "const:4:8"]]
+ 00c1d054 ["CALL", null, ["callee:00c58270:8"]]
- 00c1cc2c bytes 91ec0094
+ 00c1d054 bytes 87ec0094
- 00c1cc34 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:740:8"]]
- 00c1cc34 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c1d05c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:b40:8"]]
+ 00c1d05c ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1cc34 bytes f7a243f9
+ 00c1d05c bytes f7a245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-386d736e2b5a7b53d3cfe9df98018149"></a>

### [`00c1d274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md) → [`00c1d69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d69c.md) FUN_00c1d69c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c1f71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f71c.md) · 呼出先 12件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c1fb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fb44.md) · 呼出先 12件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 83.10% / 新版 83.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 13件, `call_argument_candidate` 57件, `store_condition` 26件, `store_destination` 43件, `store_value` 42件

アドレスに依存する影響 `call_argument_candidate` 25件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1d6d8",
      "incomplete_value": false,
      "site": "00c1d6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1d2b0",
      "incomplete_value": false,
      "site": "00c1d2b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "definition_site": "00c1d750",
      "incomplete_value": true,
      "site": "00c1d75c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1d328",
      "incomplete_value": true,
      "site": "00c1d334",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:f78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1d820",
      "incomplete_value": true,
      "site": "00c1d834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1d3f8",
      "incomplete_value": true,
      "site": "00c1d40c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 42,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1d6d8",
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c1d748",
      "READ",
      [
        "storage",
        "00c9b7f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c1d750",
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c1d6d8",
      "DATA",
      [
        "storage",
        "00c936c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c1d748",
      "READ",
      [
        "storage",
        "00c9bbf8",
        null,
        "pointer"
      ]
    ],
    [
      "00c1d750",
      "READ",
      [
        "storage",
        "00c9b378",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1dd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md#insn-00c1dd60) · [`00c1de3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md#insn-00c1de3c) · [`00c1d2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md#insn-00c1d2a4)
- 新版 `00c1e188`（命令位置の公開資料なし） · `00c1e264`（命令位置の公開資料なし） · `00c1d6cc`（命令位置の公開資料なし）

~~~diff
- 00c1dd60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:860:8"]]
- 00c1dd60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c1e188 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c60:8"]]
+ 00c1e188 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1dd60 bytes 293144f9
+ 00c1e188 bytes 293146f9
- 00c1de3c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:868:8"]]
- 00c1de3c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c1e264 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c68:8"]]
+ 00c1e264 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1de3c bytes 293544f9
+ 00c1e264 bytes 293546f9
- 00c1d2a4 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00c1d2a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c1d2a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c1d2a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c1d6cc ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00c1d6cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c1d6cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c1d6cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c1d2a4 bytes 29010b91
+ 00c1d6cc bytes 29011b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6baef01a1ce60f0dde5f83635314f0ab"></a>

### [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) → [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) FUN_00c1f48c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c24ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ad4.md) [`00c24c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c0c.md) · 呼出先 43件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c1d274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md) [`00c1f7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md) [`00c1f8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) [`00c1fa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md)
- 新版 呼出元 2件 [`00c24efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24efc.md) [`00c25034`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25034.md) · 呼出先 43件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c1d69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d69c.md) [`00c1fbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fbd0.md) [`00c1fcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fcfc.md) [`00c1fe28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fe28.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 87.68% / 新版 87.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件, `store_value` 10件

アドレスに依存する影響 `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1f4bc",
      "incomplete_value": false,
      "site": "00c1f4bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f094",
      "incomplete_value": false,
      "site": "00c1f094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1f668",
      "incomplete_value": true,
      "site": "00c1f668",
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
      "definition_site": "00c1f240",
      "incomplete_value": true,
      "site": "00c1f240",
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1f6a4",
      "incomplete_value": true,
      "site": "00c1f6a8",
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
      "definition_site": "00c1f27c",
      "incomplete_value": true,
      "site": "00c1f280",
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
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c1f4bc",
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c1f54c",
      "READ",
      [
        "storage",
        "011279e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1f554",
      "READ",
      [
        "storage",
        "011279e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1f4bc",
      "DATA",
      [
        "storage",
        "00c936c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c1f54c",
      "READ",
      [
        "storage",
        "01127de8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1f554",
      "READ",
      [
        "storage",
        "01127de0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1f198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md#insn-00c1f198) · [`00c1f1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md#insn-00c1f1a8) · [`00c1f4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md#insn-00c1f4bc)
- 新版 `00c1f5c0`（命令位置の公開資料なし） · `00c1f5d0`（命令位置の公開資料なし） · `00c1f8e4`（命令位置の公開資料なし）

~~~diff
- 00c1f198 ["INT_ADD", "register:40f0:8", ["const:c1f198:8", "const:4:8"]]
- 00c1f198 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c1f5c0 ["INT_ADD", "register:40f0:8", ["const:c1f5c0:8", "const:4:8"]]
+ 00c1f5c0 ["CALL", null, ["callee:00c57e90:8"]]
- 00c1f198 bytes 3ee20094
+ 00c1f5c0 bytes 34e20094
- 00c1f1a8 ["INT_ADD", "register:40f0:8", ["const:c1f1a8:8", "const:4:8"]]
- 00c1f1a8 ["CALL", null, ["callee:00c5e820:8"]]
+ 00c1f5d0 ["INT_ADD", "register:40f0:8", ["const:c1f5d0:8", "const:4:8"]]
+ 00c1f5d0 ["CALL", null, ["callee:00c5e820:8"]]
- 00c1f1a8 bytes 9efc0094
+ 00c1f5d0 bytes 94fc0094
- 00c1f4bc ["INT_ADD", "register:40f0:8", ["const:c1f4bc:8", "const:4:8"]]
- 00c1f4bc ["CALL", null, ["callee:00c57e90:8"]]
+ 00c1f8e4 ["INT_ADD", "register:40f0:8", ["const:c1f8e4:8", "const:4:8"]]
+ 00c1f8e4 ["CALL", null, ["callee:00c57e90:8"]]
- 00c1f4bc bytes 75e10094
+ 00c1f8e4 bytes 6be10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-019b05d49e261558c8004ddfa7689360"></a>

### [`00c1f71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f71c.md) → [`00c1fb44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fb44.md) _ZNSt6__ndk16locale7classicEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5e4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4c0.md) · 呼出先 3件 [`00c1d274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 1件 [`00c5e8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8c0.md) · 呼出先 3件 [`00c1d69c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d69c.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 68.97% / 新版 68.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c1fbac",
      "incomplete_value": true,
      "site": "00c1fbac",
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
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f784",
      "incomplete_value": true,
      "site": "00c1f784",
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
            "const:9e0:8"
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
      "definition_site": "00c1fb80",
      "incomplete_value": false,
      "site": "00c1fb84",
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
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f758",
      "incomplete_value": false,
      "site": "00c1f75c",
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
            "const:9e8:8"
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
      "definition_site": "00c1fb98",
      "incomplete_value": false,
      "site": "00c1fb9c",
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
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f770",
      "incomplete_value": false,
      "site": "00c1f774",
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
            "const:8a8:8"
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
      "00c1fb5c",
      "READ",
      [
        "storage",
        "011279e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1fb68",
      "DATA",
      [
        "storage",
        "011279e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c1fb80",
      "PARAM",
      [
        "storage",
        "011279e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c1fb5c",
      "READ",
      [
        "storage",
        "01127de8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c1fb68",
      "DATA",
      [
        "storage",
        "01127de0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c1fb80",
      "PARAM",
      [
        "storage",
        "01127de8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1f75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f71c.md#insn-00c1f75c) · [`00c1f774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f71c.md#insn-00c1f774) · [`00c1f784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f71c.md#insn-00c1f784)
- 新版 `00c1fb84`（命令位置の公開資料なし） · `00c1fb9c`（命令位置の公開資料なし） · `00c1fbac`（命令位置の公開資料なし）

~~~diff
- 00c1f75c ["INT_ADD", "register:40f0:8", ["const:c1f75c:8", "const:4:8"]]
- 00c1f75c ["CALL", null, ["callee:00c57e50:8"]]
+ 00c1fb84 ["INT_ADD", "register:40f0:8", ["const:c1fb84:8", "const:4:8"]]
+ 00c1fb84 ["CALL", null, ["callee:00c57e50:8"]]
- 00c1f75c bytes bde00094
+ 00c1fb84 bytes b3e00094
- 00c1f774 ["INT_ADD", "register:40f0:8", ["const:c1f774:8", "const:4:8"]]
- 00c1f774 ["CALL", null, ["callee:00c1d69c:8"]]
+ 00c1fb9c ["INT_ADD", "register:40f0:8", ["const:c1fb9c:8", "const:4:8"]]
+ 00c1fb9c ["CALL", null, ["callee:00c1d69c:8"]]
- 00c1f774 bytes c0f6ff97
+ 00c1fb9c bytes c0f6ff97
- 00c1f784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9e0:8"]]
- 00c1f784 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00c1fbac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 00c1fbac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00c1f784 bytes 13f104f9
+ 00c1fbac bytes 13f106f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e4c70f44f35bb6b3404b29baea43905"></a>

### [`00c1f7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md) → [`00c1fbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fbd0.md) FUN_00c1fbd0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1fbf4",
      "incomplete_value": true,
      "site": "00c1fbf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f7cc",
      "incomplete_value": true,
      "site": "00c1f7d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1fc00",
      "incomplete_value": true,
      "site": "00c1fc04",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1f7d8",
      "incomplete_value": true,
      "site": "00c1f7dc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1fc28",
      "incomplete_value": true,
      "site": "00c1fc2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f800",
      "incomplete_value": true,
      "site": "00c1f804",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
              ]
            ]
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
      "00c1fbf4",
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ],
    [
      "00c1fbf8",
      "DATA",
      [
        "storage",
        "01127758",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1fbfc",
      "READ",
      [
        "storage",
        "01127758",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1fbf4",
      "READ",
      [
        "storage",
        "00c9b378",
        null,
        "pointer"
      ]
    ],
    [
      "00c1fbf8",
      "DATA",
      [
        "storage",
        "01127b58",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1fbfc",
      "READ",
      [
        "storage",
        "01127b58",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1f804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md#insn-00c1f804) · [`00c1f7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md#insn-00c1f7c0) · [`00c1f7cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md#insn-00c1f7cc)
- 新版 `00c1fc2c`（命令位置の公開資料なし） · `00c1fbe8`（命令位置の公開資料なし） · `00c1fbf4`（命令位置の公開資料なし）

~~~diff
- 00c1f804 ["INT_ADD", "register:40f0:8", ["const:c1f804:8", "const:4:8"]]
- 00c1f804 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c1fc2c ["INT_ADD", "register:40f0:8", ["const:c1fc2c:8", "const:4:8"]]
+ 00c1fc2c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1f804 bytes b7f80094
+ 00c1fc2c bytes adf80094
- 00c1f7c0 ["COPY", "register:40a0:8", ["const:c9a000:8"]]
+ 00c1fbe8 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00c1f7c0 bytes d40300f0
+ 00c1fbe8 bytes f4030090
- 00c1f7cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f78:8"]]
- 00c1f7cc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c1fbf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
+ 00c1fbf4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1f7cc bytes 94be47f9
+ 00c1fbf4 bytes 94be41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2019e6ac6e5ba206e105495fc00e530"></a>

### [`00c1f8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) → [`00c1fcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fcfc.md) FUN_00c1fcfc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1fd20",
      "incomplete_value": true,
      "site": "00c1fd24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f8f8",
      "incomplete_value": true,
      "site": "00c1f8fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1fd2c",
      "incomplete_value": true,
      "site": "00c1fd30",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1f904",
      "incomplete_value": true,
      "site": "00c1f908",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1fd54",
      "incomplete_value": true,
      "site": "00c1fd58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1f92c",
      "incomplete_value": true,
      "site": "00c1f930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
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
      "00c1fd20",
      "READ",
      [
        "storage",
        "00c9b808",
        null,
        "pointer"
      ]
    ],
    [
      "00c1fd24",
      "DATA",
      [
        "storage",
        "01127768",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1fd28",
      "READ",
      [
        "storage",
        "01127768",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1fd20",
      "READ",
      [
        "storage",
        "00c9bc08",
        null,
        "pointer"
      ]
    ],
    [
      "00c1fd24",
      "DATA",
      [
        "storage",
        "01127b68",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1fd28",
      "READ",
      [
        "storage",
        "01127b68",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1f930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md#insn-00c1f930) · [`00c1f8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md#insn-00c1f8f8) · [`00c1f920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md#insn-00c1f920)
- 新版 `00c1fd58`（命令位置の公開資料なし） · `00c1fd20`（命令位置の公開資料なし） · `00c1fd48`（命令位置の公開資料なし）

~~~diff
- 00c1f930 ["INT_ADD", "register:40f0:8", ["const:c1f930:8", "const:4:8"]]
- 00c1f930 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c1fd58 ["INT_ADD", "register:40f0:8", ["const:c1fd58:8", "const:4:8"]]
+ 00c1fd58 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1f930 bytes 6cf80094
+ 00c1fd58 bytes 62f80094
- 00c1f8f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:808:8"]]
- 00c1f8f8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c1fd20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c08:8"]]
+ 00c1fd20 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1f8f8 bytes 940644f9
+ 00c1fd20 bytes 940646f9
- 00c1f920 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c1fd48 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1f920 bytes 82130b10
+ 00c1fd48 bytes 82130b10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e71bae1be064b7182f563fe9605a30f1"></a>

### [`00c1fa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md) → [`00c1fe28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fe28.md) FUN_00c1fe28

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1fe4c",
      "incomplete_value": true,
      "site": "00c1fe50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c1fa24",
      "incomplete_value": true,
      "site": "00c1fa28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1fe58",
      "incomplete_value": true,
      "site": "00c1fe5c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1fa30",
      "incomplete_value": true,
      "site": "00c1fa34",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1fe80",
      "incomplete_value": true,
      "site": "00c1fe84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c1fa58",
      "incomplete_value": true,
      "site": "00c1fa5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00c1fe4c",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c1fe50",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1fe54",
      "READ",
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
      "00c1fe4c",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c1fe50",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1fe54",
      "READ",
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

- 旧版 [`00c1fa5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md#insn-00c1fa5c) · [`00c1fa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md#insn-00c1fa24) · [`00c1fa4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md#insn-00c1fa4c)
- 新版 `00c1fe84`（命令位置の公開資料なし） · `00c1fe4c`（命令位置の公開資料なし） · `00c1fe74`（命令位置の公開資料なし）

~~~diff
- 00c1fa5c ["INT_ADD", "register:40f0:8", ["const:c1fa5c:8", "const:4:8"]]
- 00c1fa5c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c1fe84 ["INT_ADD", "register:40f0:8", ["const:c1fe84:8", "const:4:8"]]
+ 00c1fe84 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1fa5c bytes 21f80094
+ 00c1fe84 bytes 17f80094
- 00c1fa24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00c1fa24 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c1fe4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
+ 00c1fe4c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1fa24 bytes 941a44f9
+ 00c1fe4c bytes 941a46f9
- 00c1fa4c ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c1fe74 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1fa4c bytes 220a0b10
+ 00c1fe74 bytes 220a0b10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14db37820a17fb0f0642f6fc50593045"></a>

### [`00c1fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fb2c.md) → [`00c1ff54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1ff54.md) FUN_00c1ff54

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c1ff78",
      "incomplete_value": true,
      "site": "00c1ff7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fb50",
      "incomplete_value": true,
      "site": "00c1fb54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c1ff84",
      "incomplete_value": true,
      "site": "00c1ff88",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1fb5c",
      "incomplete_value": true,
      "site": "00c1fb60",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1ffac",
      "incomplete_value": true,
      "site": "00c1ffb0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fb84",
      "incomplete_value": true,
      "site": "00c1fb88",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
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
      "00c1ff78",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c1ff7c",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1ff80",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c1ff78",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c1ff7c",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c1ff80",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1fb88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fb2c.md#insn-00c1fb88) · [`00c1fb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fb2c.md#insn-00c1fb50) · [`00c1fb78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fb2c.md#insn-00c1fb78)
- 新版 `00c1ffb0`（命令位置の公開資料なし） · `00c1ff78`（命令位置の公開資料なし） · `00c1ffa0`（命令位置の公開資料なし）

~~~diff
- 00c1fb88 ["INT_ADD", "register:40f0:8", ["const:c1fb88:8", "const:4:8"]]
- 00c1fb88 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c1ffb0 ["INT_ADD", "register:40f0:8", ["const:c1ffb0:8", "const:4:8"]]
+ 00c1ffb0 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1fb88 bytes d6f70094
+ 00c1ffb0 bytes ccf70094
- 00c1fb50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00c1fb50 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c1ff78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b40:8"]]
+ 00c1ff78 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1fb50 bytes 94a243f9
+ 00c1ff78 bytes 94a245f9
- 00c1fb78 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c1ffa0 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1fb78 bytes c2000b10
+ 00c1ffa0 bytes c2000b10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-417bde6ef5e9ae60f02eabb75c14965e"></a>

### [`00c1fc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fc58.md) → [`00c20080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20080.md) FUN_00c20080

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c200a4",
      "incomplete_value": true,
      "site": "00c200a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fc7c",
      "incomplete_value": true,
      "site": "00c1fc80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c200b0",
      "incomplete_value": true,
      "site": "00c200b4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1fc88",
      "incomplete_value": true,
      "site": "00c1fc8c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c200d8",
      "incomplete_value": true,
      "site": "00c200dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fcb0",
      "incomplete_value": true,
      "site": "00c1fcb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
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
      "00c200a4",
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c200a8",
      "DATA",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c200ac",
      "READ",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c200a4",
      "READ",
      [
        "storage",
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c200a8",
      "DATA",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c200ac",
      "READ",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1fcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fc58.md#insn-00c1fcb4) · [`00c1fc7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fc58.md#insn-00c1fc7c) · [`00c1fca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fc58.md#insn-00c1fca4)
- 新版 `00c200dc`（命令位置の公開資料なし） · `00c200a4`（命令位置の公開資料なし） · `00c200cc`（命令位置の公開資料なし）

~~~diff
- 00c1fcb4 ["INT_ADD", "register:40f0:8", ["const:c1fcb4:8", "const:4:8"]]
- 00c1fcb4 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c200dc ["INT_ADD", "register:40f0:8", ["const:c200dc:8", "const:4:8"]]
+ 00c200dc ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1fcb4 bytes 8bf70094
+ 00c200dc bytes 81f70094
- 00c1fc7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4b8:8"]]
- 00c1fc7c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c200a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
+ 00c200a4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1fc7c bytes 945e42f9
+ 00c200a4 bytes 945e44f9
- 00c1fca4 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c200cc ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1fca4 bytes 62f70a10
+ 00c200cc bytes 62f70a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f582eb4862c9117536c7ecf91114b62"></a>

### [`00c1fd84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fd84.md) → [`00c201ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c201ac.md) FUN_00c201ac

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c201d0",
      "incomplete_value": true,
      "site": "00c201d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fda8",
      "incomplete_value": true,
      "site": "00c1fdac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c201dc",
      "incomplete_value": true,
      "site": "00c201e0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1fdb4",
      "incomplete_value": true,
      "site": "00c1fdb8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c20204",
      "incomplete_value": true,
      "site": "00c20208",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fddc",
      "incomplete_value": true,
      "site": "00c1fde0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
              ]
            ]
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
      "00c201d0",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c201d4",
      "DATA",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c201d8",
      "READ",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c201d0",
      "READ",
      [
        "storage",
        "00c9bba8",
        null,
        "pointer"
      ]
    ],
    [
      "00c201d4",
      "DATA",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c201d8",
      "READ",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1fde0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fd84.md#insn-00c1fde0) · [`00c1fda8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fd84.md#insn-00c1fda8) · [`00c1fdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fd84.md#insn-00c1fdd0)
- 新版 `00c20208`（命令位置の公開資料なし） · `00c201d0`（命令位置の公開資料なし） · `00c201f8`（命令位置の公開資料なし）

~~~diff
- 00c1fde0 ["INT_ADD", "register:40f0:8", ["const:c1fde0:8", "const:4:8"]]
- 00c1fde0 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c20208 ["INT_ADD", "register:40f0:8", ["const:c20208:8", "const:4:8"]]
+ 00c20208 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1fde0 bytes 40f70094
+ 00c20208 bytes 36f70094
- 00c1fda8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
- 00c1fda8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c201d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ba8:8"]]
+ 00c201d0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1fda8 bytes 94d643f9
+ 00c201d0 bytes 94d645f9
- 00c1fdd0 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c201f8 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1fdd0 bytes 02ee0a10
+ 00c201f8 bytes 02ee0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6683326da5e78a5d0a28757e5c0cc8bb"></a>

### [`00c1feb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1feb0.md) → [`00c202d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c202d8.md) FUN_00c202d8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c202fc",
      "incomplete_value": true,
      "site": "00c20300",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1fed4",
      "incomplete_value": true,
      "site": "00c1fed8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:828:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c20308",
      "incomplete_value": true,
      "site": "00c2030c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c1fee0",
      "incomplete_value": true,
      "site": "00c1fee4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c20330",
      "incomplete_value": true,
      "site": "00c20334",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c1ff08",
      "incomplete_value": true,
      "site": "00c1ff0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:828:8"
              ]
            ]
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
      "00c202fc",
      "READ",
      [
        "storage",
        "00c9b828",
        null,
        "pointer"
      ]
    ],
    [
      "00c20300",
      "DATA",
      [
        "storage",
        "01127a48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20304",
      "READ",
      [
        "storage",
        "01127a48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c202fc",
      "READ",
      [
        "storage",
        "00c9bc28",
        null,
        "pointer"
      ]
    ],
    [
      "00c20300",
      "DATA",
      [
        "storage",
        "01127e48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20304",
      "READ",
      [
        "storage",
        "01127e48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c1ff0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1feb0.md#insn-00c1ff0c) · [`00c1fed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1feb0.md#insn-00c1fed4) · [`00c1fefc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1feb0.md#insn-00c1fefc)
- 新版 `00c20334`（命令位置の公開資料なし） · `00c202fc`（命令位置の公開資料なし） · `00c20324`（命令位置の公開資料なし）

~~~diff
- 00c1ff0c ["INT_ADD", "register:40f0:8", ["const:c1ff0c:8", "const:4:8"]]
- 00c1ff0c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c20334 ["INT_ADD", "register:40f0:8", ["const:c20334:8", "const:4:8"]]
+ 00c20334 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c1ff0c bytes f5f60094
+ 00c20334 bytes ebf60094
- 00c1fed4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00c1fed4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c202fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c28:8"]]
+ 00c202fc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c1fed4 bytes 941644f9
+ 00c202fc bytes 941646f9
- 00c1fefc ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20324 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c1fefc bytes a2e40a10
+ 00c20324 bytes a2e40a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d6487685452acdc31f7507bb955c987"></a>

### [`00c1ffdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1ffdc.md) → [`00c20404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20404.md) FUN_00c20404

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20428",
      "incomplete_value": true,
      "site": "00c2042c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20000",
      "incomplete_value": true,
      "site": "00c20004",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c20434",
      "incomplete_value": true,
      "site": "00c20438",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c2000c",
      "incomplete_value": true,
      "site": "00c20010",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c2045c",
      "incomplete_value": true,
      "site": "00c20460",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20034",
      "incomplete_value": true,
      "site": "00c20038",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:838:8"
              ]
            ]
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
      "00c20428",
      "READ",
      [
        "storage",
        "00c9b838",
        null,
        "pointer"
      ]
    ],
    [
      "00c2042c",
      "DATA",
      [
        "storage",
        "01127a68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20430",
      "READ",
      [
        "storage",
        "01127a68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c20428",
      "READ",
      [
        "storage",
        "00c9bc38",
        null,
        "pointer"
      ]
    ],
    [
      "00c2042c",
      "DATA",
      [
        "storage",
        "01127e68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20430",
      "READ",
      [
        "storage",
        "01127e68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1ffdc.md#insn-00c20038) · [`00c20000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1ffdc.md#insn-00c20000) · [`00c20028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1ffdc.md#insn-00c20028)
- 新版 `00c20460`（命令位置の公開資料なし） · `00c20428`（命令位置の公開資料なし） · `00c20450`（命令位置の公開資料なし）

~~~diff
- 00c20038 ["INT_ADD", "register:40f0:8", ["const:c20038:8", "const:4:8"]]
- 00c20038 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c20460 ["INT_ADD", "register:40f0:8", ["const:c20460:8", "const:4:8"]]
+ 00c20460 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c20038 bytes aaf60094
+ 00c20460 bytes a0f60094
- 00c20000 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:838:8"]]
- 00c20000 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20428 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c38:8"]]
+ 00c20428 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20000 bytes 941e44f9
+ 00c20428 bytes 941e46f9
- 00c20028 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20450 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20028 bytes 42db0a10
+ 00c20450 bytes 42db0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41781c41f6b3b1dafc3b92005615d1c9"></a>

### [`00c20108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20108.md) → [`00c20530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20530.md) FUN_00c20530

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20554",
      "incomplete_value": true,
      "site": "00c20558",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2012c",
      "incomplete_value": true,
      "site": "00c20130",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:848:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c20560",
      "incomplete_value": true,
      "site": "00c20564",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c20138",
      "incomplete_value": true,
      "site": "00c2013c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c20588",
      "incomplete_value": true,
      "site": "00c2058c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20160",
      "incomplete_value": true,
      "site": "00c20164",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:848:8"
              ]
            ]
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
      "00c20554",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00c20558",
      "DATA",
      [
        "storage",
        "01127a58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2055c",
      "READ",
      [
        "storage",
        "01127a58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c20554",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c20558",
      "DATA",
      [
        "storage",
        "01127e58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2055c",
      "READ",
      [
        "storage",
        "01127e58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20108.md#insn-00c20164) · [`00c2012c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20108.md#insn-00c2012c) · [`00c20154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20108.md#insn-00c20154)
- 新版 `00c2058c`（命令位置の公開資料なし） · `00c20554`（命令位置の公開資料なし） · `00c2057c`（命令位置の公開資料なし）

~~~diff
- 00c20164 ["INT_ADD", "register:40f0:8", ["const:c20164:8", "const:4:8"]]
- 00c20164 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c2058c ["INT_ADD", "register:40f0:8", ["const:c2058c:8", "const:4:8"]]
+ 00c2058c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c20164 bytes 5ff60094
+ 00c2058c bytes 55f60094
- 00c2012c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:848:8"]]
- 00c2012c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20554 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c48:8"]]
+ 00c20554 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2012c bytes 942644f9
+ 00c20554 bytes 942646f9
- 00c20154 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c2057c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20154 bytes e2d10a10
+ 00c2057c bytes e2d10a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb2f9f944bd2a2662343dc075fdd71a4"></a>

### [`00c20234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20234.md) → [`00c2065c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c2065c.md) FUN_00c2065c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20680",
      "incomplete_value": true,
      "site": "00c20684",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20258",
      "incomplete_value": true,
      "site": "00c2025c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:858:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c2068c",
      "incomplete_value": true,
      "site": "00c20690",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c20264",
      "incomplete_value": true,
      "site": "00c20268",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c206b4",
      "incomplete_value": true,
      "site": "00c206b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2028c",
      "incomplete_value": true,
      "site": "00c20290",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:858:8"
              ]
            ]
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
      "00c20680",
      "READ",
      [
        "storage",
        "00c9b858",
        null,
        "pointer"
      ]
    ],
    [
      "00c20684",
      "DATA",
      [
        "storage",
        "01127a78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20688",
      "READ",
      [
        "storage",
        "01127a78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c20680",
      "READ",
      [
        "storage",
        "00c9bc58",
        null,
        "pointer"
      ]
    ],
    [
      "00c20684",
      "DATA",
      [
        "storage",
        "01127e78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20688",
      "READ",
      [
        "storage",
        "01127e78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20234.md#insn-00c20290) · [`00c20258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20234.md#insn-00c20258) · [`00c20280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20234.md#insn-00c20280)
- 新版 `00c206b8`（命令位置の公開資料なし） · `00c20680`（命令位置の公開資料なし） · `00c206a8`（命令位置の公開資料なし）

~~~diff
- 00c20290 ["INT_ADD", "register:40f0:8", ["const:c20290:8", "const:4:8"]]
- 00c20290 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c206b8 ["INT_ADD", "register:40f0:8", ["const:c206b8:8", "const:4:8"]]
+ 00c206b8 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c20290 bytes 14f60094
+ 00c206b8 bytes 0af60094
- 00c20258 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
- 00c20258 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20680 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00c20680 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20258 bytes 942e44f9
+ 00c20680 bytes 942e46f9
- 00c20280 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c206a8 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20280 bytes 82c80a10
+ 00c206a8 bytes 82c80a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68bf4f6966162fc175c857beb14a1e9d"></a>

### [`00c20360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20360.md) → [`00c20788`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20788.md) FUN_00c20788

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c207ac",
      "incomplete_value": true,
      "site": "00c207b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20384",
      "incomplete_value": true,
      "site": "00c20388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c207b8",
      "incomplete_value": true,
      "site": "00c207bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c20390",
      "incomplete_value": true,
      "site": "00c20394",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c207e0",
      "incomplete_value": true,
      "site": "00c207e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c203b8",
      "incomplete_value": true,
      "site": "00c203bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
              ]
            ]
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
      "00c207ac",
      "READ",
      [
        "storage",
        "00c9b7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c207b0",
      "DATA",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c207b4",
      "READ",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c207ac",
      "READ",
      [
        "storage",
        "00c9bbb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c207b0",
      "DATA",
      [
        "storage",
        "01127e88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c207b4",
      "READ",
      [
        "storage",
        "01127e88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c203bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20360.md#insn-00c203bc) · [`00c20384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20360.md#insn-00c20384) · [`00c203ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20360.md#insn-00c203ac)
- 新版 `00c207e4`（命令位置の公開資料なし） · `00c207ac`（命令位置の公開資料なし） · `00c207d4`（命令位置の公開資料なし）

~~~diff
- 00c203bc ["INT_ADD", "register:40f0:8", ["const:c203bc:8", "const:4:8"]]
- 00c203bc ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c207e4 ["INT_ADD", "register:40f0:8", ["const:c207e4:8", "const:4:8"]]
+ 00c207e4 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c203bc bytes c9f50094
+ 00c207e4 bytes bff50094
- 00c20384 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
- 00c20384 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c207ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
+ 00c207ac ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20384 bytes 94de43f9
+ 00c207ac bytes 94de45f9
- 00c203ac ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c207d4 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c203ac bytes 22bf0a10
+ 00c207d4 bytes 22bf0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f68c28a61d2fcf91ac281bc04850147e"></a>

### [`00c2048c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c2048c.md) → [`00c208b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c208b4.md) FUN_00c208b4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c208d8",
      "incomplete_value": true,
      "site": "00c208dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c204b0",
      "incomplete_value": true,
      "site": "00c204b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c208e4",
      "incomplete_value": true,
      "site": "00c208e8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c204bc",
      "incomplete_value": true,
      "site": "00c204c0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c2090c",
      "incomplete_value": true,
      "site": "00c20910",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c204e4",
      "incomplete_value": true,
      "site": "00c204e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
              ]
            ]
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
      "00c208d8",
      "READ",
      [
        "storage",
        "00c9b7c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c208dc",
      "DATA",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c208e0",
      "READ",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c208d8",
      "READ",
      [
        "storage",
        "00c9bbc8",
        null,
        "pointer"
      ]
    ],
    [
      "00c208dc",
      "DATA",
      [
        "storage",
        "01127e98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c208e0",
      "READ",
      [
        "storage",
        "01127e98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c204e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c2048c.md#insn-00c204e8) · [`00c204b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c2048c.md#insn-00c204b0) · [`00c204d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c2048c.md#insn-00c204d8)
- 新版 `00c20910`（命令位置の公開資料なし） · `00c208d8`（命令位置の公開資料なし） · `00c20900`（命令位置の公開資料なし）

~~~diff
- 00c204e8 ["INT_ADD", "register:40f0:8", ["const:c204e8:8", "const:4:8"]]
- 00c204e8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c20910 ["INT_ADD", "register:40f0:8", ["const:c20910:8", "const:4:8"]]
+ 00c20910 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c204e8 bytes 7ef50094
+ 00c20910 bytes 74f50094
- 00c204b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00c204b0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c208d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bc8:8"]]
+ 00c208d8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c204b0 bytes 94e643f9
+ 00c208d8 bytes 94e645f9
- 00c204d8 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20900 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c204d8 bytes c2b50a10
+ 00c20900 bytes c2b50a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81ec86d5e94e60fa3e188484fe5d1e7b"></a>

### [`00c205b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c205b8.md) → [`00c209e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c209e0.md) FUN_00c209e0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20a04",
      "incomplete_value": true,
      "site": "00c20a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c205dc",
      "incomplete_value": true,
      "site": "00c205e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c20a10",
      "incomplete_value": true,
      "site": "00c20a14",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c205e8",
      "incomplete_value": true,
      "site": "00c205ec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c20a38",
      "incomplete_value": true,
      "site": "00c20a3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20610",
      "incomplete_value": true,
      "site": "00c20614",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e0:8"
              ]
            ]
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
      "00c20a04",
      "READ",
      [
        "storage",
        "00c9b7e0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20a08",
      "DATA",
      [
        "storage",
        "011277f8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20a0c",
      "READ",
      [
        "storage",
        "011277f8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c20a04",
      "READ",
      [
        "storage",
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20a08",
      "DATA",
      [
        "storage",
        "01127bf8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20a0c",
      "READ",
      [
        "storage",
        "01127bf8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c205b8.md#insn-00c20614) · [`00c205dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c205b8.md#insn-00c205dc) · [`00c20604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c205b8.md#insn-00c20604)
- 新版 `00c20a3c`（命令位置の公開資料なし） · `00c20a04`（命令位置の公開資料なし） · `00c20a2c`（命令位置の公開資料なし）

~~~diff
- 00c20614 ["INT_ADD", "register:40f0:8", ["const:c20614:8", "const:4:8"]]
- 00c20614 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c20a3c ["INT_ADD", "register:40f0:8", ["const:c20a3c:8", "const:4:8"]]
+ 00c20a3c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c20614 bytes 33f50094
+ 00c20a3c bytes 29f50094
- 00c205dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00c205dc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20a04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
+ 00c20a04 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c205dc bytes 94f243f9
+ 00c20a04 bytes 94f245f9
- 00c20604 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20a2c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20604 bytes 62ac0a10
+ 00c20a2c bytes 62ac0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd32408aba7b531ba7b4d944d14e832f"></a>

### [`00c206e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c206e4.md) → [`00c20b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20b0c.md) FUN_00c20b0c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4d0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 1件 [`00c5e8d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20b3c",
      "incomplete_value": true,
      "site": "00c20b3c",
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
      "definition_site": "00c20714",
      "incomplete_value": true,
      "site": "00c20714",
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
      "00c20b2c",
      "READ",
      [
        "storage",
        "00c9b998",
        null,
        "pointer"
      ]
    ],
    [
      "00c20b3c",
      "DATA",
      [
        "storage",
        "00c95000",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c20b2c",
      "READ",
      [
        "storage",
        "00c9bd98",
        null,
        "pointer"
      ]
    ],
    [
      "00c20b3c",
      "DATA",
      [
        "storage",
        "00c95400",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c206e4.md#insn-00c20704) · [`00c20708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c206e4.md#insn-00c20708) · [`00c2070c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c206e4.md#insn-00c2070c)
- 新版 `00c20b2c`（命令位置の公開資料なし）

~~~diff
- 00c20704 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:998:8"]]
- 00c20704 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20b2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d98:8"]]
+ 00c20b2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20704 bytes 08cd44f9
+ 00c20b2c bytes 08cd46f9
- 00c20708 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00c20708 bytes f50300aa
- 00c2070c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00c2070c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44f5adee8ee6b0cfb583e6b6e13e77ba"></a>

### [`00c207c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c207c8.md) → [`00c20bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20bf0.md) FUN_00c20bf0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20c14",
      "incomplete_value": true,
      "site": "00c20c18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c207ec",
      "incomplete_value": true,
      "site": "00c207f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c20c20",
      "incomplete_value": true,
      "site": "00c20c24",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c207f8",
      "incomplete_value": true,
      "site": "00c207fc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c20c48",
      "incomplete_value": true,
      "site": "00c20c4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20820",
      "incomplete_value": true,
      "site": "00c20824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
              ]
            ]
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
      "00c20c14",
      "READ",
      [
        "storage",
        "00c9b7d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c20c18",
      "DATA",
      [
        "storage",
        "01127808",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20c1c",
      "READ",
      [
        "storage",
        "01127808",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c20c14",
      "READ",
      [
        "storage",
        "00c9bbd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c20c18",
      "DATA",
      [
        "storage",
        "01127c08",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20c1c",
      "READ",
      [
        "storage",
        "01127c08",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c207c8.md#insn-00c20824) · [`00c207ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c207c8.md#insn-00c207ec) · [`00c20814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c207c8.md#insn-00c20814)
- 新版 `00c20c4c`（命令位置の公開資料なし） · `00c20c14`（命令位置の公開資料なし） · `00c20c3c`（命令位置の公開資料なし）

~~~diff
- 00c20824 ["INT_ADD", "register:40f0:8", ["const:c20824:8", "const:4:8"]]
- 00c20824 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c20c4c ["INT_ADD", "register:40f0:8", ["const:c20c4c:8", "const:4:8"]]
+ 00c20c4c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c20824 bytes aff40094
+ 00c20c4c bytes a5f40094
- 00c207ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d8:8"]]
- 00c207ec ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20c14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bd8:8"]]
+ 00c20c14 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c207ec bytes 94ee43f9
+ 00c20c14 bytes 94ee45f9
- 00c20814 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20c3c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20814 bytes e29b0a10
+ 00c20c3c bytes e29b0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e0cebc35198ec46f84c0b2f9ccb4174"></a>

### [`00c208f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c208f4.md) → [`00c20d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20d1c.md) FUN_00c20d1c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4e0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 1件 [`00c5e8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20d4c",
      "incomplete_value": true,
      "site": "00c20d4c",
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
      "definition_site": "00c20924",
      "incomplete_value": true,
      "site": "00c20924",
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
      "00c20d3c",
      "READ",
      [
        "storage",
        "00c9b9a0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20d4c",
      "DATA",
      [
        "storage",
        "00c95088",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c20d3c",
      "READ",
      [
        "storage",
        "00c9bda0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20d4c",
      "DATA",
      [
        "storage",
        "00c95488",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c208f4.md#insn-00c20914) · [`00c20918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c208f4.md#insn-00c20918) · [`00c2091c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c208f4.md#insn-00c2091c)
- 新版 `00c20d3c`（命令位置の公開資料なし）

~~~diff
- 00c20914 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a0:8"]]
- 00c20914 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20d3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da0:8"]]
+ 00c20d3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20914 bytes 08d144f9
+ 00c20d3c bytes 08d146f9
- 00c20918 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00c20918 bytes f50300aa
- 00c2091c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00c2091c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4f7c44925986c74a7f0715742d41104"></a>

### [`00c209d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c209d8.md) → [`00c20e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20e00.md) FUN_00c20e00

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.65% / 新版 93.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20e24",
      "incomplete_value": true,
      "site": "00c20e28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c209fc",
      "incomplete_value": true,
      "site": "00c20a00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c20e58",
      "incomplete_value": true,
      "site": "00c20e5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20a30",
      "incomplete_value": true,
      "site": "00c20a34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f0:8"
              ]
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
      "definition_site": "00c20e4c",
      "incomplete_value": false,
      "site": "00c20e5c",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c20a24",
      "incomplete_value": false,
      "site": "00c20a34",
      "value": [
        "leaf",
        "const:c35b90:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c20e24",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20e28",
      "DATA",
      [
        "storage",
        "01127818",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20e2c",
      "READ",
      [
        "storage",
        "01127818",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c20e24",
      "READ",
      [
        "storage",
        "00c9bbf0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20e28",
      "DATA",
      [
        "storage",
        "01127c18",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c20e2c",
      "READ",
      [
        "storage",
        "01127c18",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c209d8.md#insn-00c20a34) · [`00c209fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c209d8.md#insn-00c209fc) · [`00c20a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c209d8.md#insn-00c20a24)
- 新版 `00c20e5c`（命令位置の公開資料なし） · `00c20e24`（命令位置の公開資料なし） · `00c20e4c`（命令位置の公開資料なし）

~~~diff
- 00c20a34 ["INT_ADD", "register:40f0:8", ["const:c20a34:8", "const:4:8"]]
- 00c20a34 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c20e5c ["INT_ADD", "register:40f0:8", ["const:c20e5c:8", "const:4:8"]]
+ 00c20e5c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c20a34 bytes 2bf40094
+ 00c20e5c bytes 21f40094
- 00c209fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f0:8"]]
- 00c209fc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20e24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bf0:8"]]
+ 00c20e24 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c209fc bytes 94fa43f9
+ 00c20e24 bytes 94fa45f9
- 00c20a24 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c20e4c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20a24 bytes 628b0a10
+ 00c20e4c bytes 628b0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea9d6f50d71d952b23c9e88c8b000d3f"></a>

### [`00c20b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20b04.md) → [`00c20f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c20/00c20f2c.md) FUN_00c20f2c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4f0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 1件 [`00c5e8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c20f5c",
      "incomplete_value": true,
      "site": "00c20f5c",
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
      "definition_site": "00c20b34",
      "incomplete_value": true,
      "site": "00c20b34",
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
      "00c20f4c",
      "READ",
      [
        "storage",
        "00c9b9a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c20f5c",
      "DATA",
      [
        "storage",
        "00c95110",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c20f4c",
      "READ",
      [
        "storage",
        "00c9bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00c20f5c",
      "DATA",
      [
        "storage",
        "00c95510",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20b04.md#insn-00c20b24) · [`00c20b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20b04.md#insn-00c20b28) · [`00c20b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20b04.md#insn-00c20b2c)
- 新版 `00c20f4c`（命令位置の公開資料なし）

~~~diff
- 00c20b24 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 00c20b24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c20f4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:da8:8"]]
+ 00c20f4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20b24 bytes 08d544f9
+ 00c20f4c bytes 08d546f9
- 00c20b28 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00c20b28 bytes f50300aa
- 00c20b2c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00c20b2c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e73cf31ea5e43f9001e06a88f5e48170"></a>

### [`00c20be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20be8.md) → [`00c21010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21010.md) FUN_00c21010

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21034",
      "incomplete_value": true,
      "site": "00c21038",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20c0c",
      "incomplete_value": true,
      "site": "00c20c10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c21040",
      "incomplete_value": true,
      "site": "00c21044",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c20c18",
      "incomplete_value": true,
      "site": "00c20c1c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c21068",
      "incomplete_value": true,
      "site": "00c2106c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20c40",
      "incomplete_value": true,
      "site": "00c20c44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e8:8"
              ]
            ]
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
      "00c21034",
      "READ",
      [
        "storage",
        "00c9b7e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c21038",
      "DATA",
      [
        "storage",
        "01127828",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2103c",
      "READ",
      [
        "storage",
        "01127828",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21034",
      "READ",
      [
        "storage",
        "00c9bbe8",
        null,
        "pointer"
      ]
    ],
    [
      "00c21038",
      "DATA",
      [
        "storage",
        "01127c28",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2103c",
      "READ",
      [
        "storage",
        "01127c28",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20be8.md#insn-00c20c44) · [`00c20c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20be8.md#insn-00c20c0c) · [`00c20c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20be8.md#insn-00c20c34)
- 新版 `00c2106c`（命令位置の公開資料なし） · `00c21034`（命令位置の公開資料なし） · `00c2105c`（命令位置の公開資料なし）

~~~diff
- 00c20c44 ["INT_ADD", "register:40f0:8", ["const:c20c44:8", "const:4:8"]]
- 00c20c44 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c2106c ["INT_ADD", "register:40f0:8", ["const:c2106c:8", "const:4:8"]]
+ 00c2106c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c20c44 bytes a7f30094
+ 00c2106c bytes 9df30094
- 00c20c0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
- 00c20c0c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21034 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
+ 00c21034 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20c0c bytes 94f643f9
+ 00c21034 bytes 94f645f9
- 00c20c34 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c2105c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20c34 bytes e27a0a10
+ 00c2105c bytes e27a0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7885610c1adc5e8dc276bcc4d9928cc2"></a>

### [`00c20d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20d14.md) → [`00c2113c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c2113c.md) FUN_00c2113c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e500.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 1件 [`00c5e900`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e900.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2116c",
      "incomplete_value": true,
      "site": "00c2116c",
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
      "definition_site": "00c20d44",
      "incomplete_value": true,
      "site": "00c20d44",
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
      "00c2115c",
      "READ",
      [
        "storage",
        "00c9b9b0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2116c",
      "DATA",
      [
        "storage",
        "00c95198",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c2115c",
      "READ",
      [
        "storage",
        "00c9bdb0",
        null,
        "pointer"
      ]
    ],
    [
      "00c2116c",
      "DATA",
      [
        "storage",
        "00c95598",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20d14.md#insn-00c20d34) · [`00c20d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20d14.md#insn-00c20d38) · [`00c20d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20d14.md#insn-00c20d3c)
- 新版 `00c2115c`（命令位置の公開資料なし）

~~~diff
- 00c20d34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b0:8"]]
- 00c20d34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2115c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db0:8"]]
+ 00c2115c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20d34 bytes 08d944f9
+ 00c2115c bytes 08d946f9
- 00c20d38 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00c20d38 bytes f50300aa
- 00c20d3c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00c20d3c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7ae3bea8c49a55a004798104925332d"></a>

### [`00c20df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20df8.md) → [`00c21220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21220.md) FUN_00c21220

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21244",
      "incomplete_value": true,
      "site": "00c21248",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20e1c",
      "incomplete_value": true,
      "site": "00c20e20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c21250",
      "incomplete_value": true,
      "site": "00c21254",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c20e28",
      "incomplete_value": true,
      "site": "00c20e2c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c21278",
      "incomplete_value": true,
      "site": "00c2127c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20e50",
      "incomplete_value": true,
      "site": "00c20e54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
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
      "00c21244",
      "READ",
      [
        "storage",
        "00c9aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00c21248",
      "DATA",
      [
        "storage",
        "011277b8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2124c",
      "READ",
      [
        "storage",
        "011277b8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21244",
      "READ",
      [
        "storage",
        "00c9b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c21248",
      "DATA",
      [
        "storage",
        "01127bb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2124c",
      "READ",
      [
        "storage",
        "01127bb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20df8.md#insn-00c20e54) · [`00c20e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20df8.md#insn-00c20e10) · [`00c20e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20df8.md#insn-00c20e1c)
- 新版 `00c2127c`（命令位置の公開資料なし） · `00c21238`（命令位置の公開資料なし） · `00c21244`（命令位置の公開資料なし）

~~~diff
- 00c20e54 ["INT_ADD", "register:40f0:8", ["const:c20e54:8", "const:4:8"]]
- 00c20e54 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c2127c ["INT_ADD", "register:40f0:8", ["const:c2127c:8", "const:4:8"]]
+ 00c2127c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c20e54 bytes 23f30094
+ 00c2127c bytes 19f30094
- 00c20e10 ["COPY", "register:40a0:8", ["const:c9a000:8"]]
+ 00c21238 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00c20e10 bytes d40300d0
+ 00c21238 bytes d40300d0
- 00c20e1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ef0:8"]]
- 00c20e1c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21244 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
+ 00c21244 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20e1c bytes 947a47f9
+ 00c21244 bytes 947a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92269dfb11892209104efcc68a43010f"></a>

### [`00c20f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20f24.md) → [`00c2134c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c2134c.md) FUN_00c2134c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.83% / 新版 96.83%

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
      "definition_site": "00c213a4",
      "incomplete_value": true,
      "site": "00c213a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c20f7c",
      "incomplete_value": true,
      "site": "00c20f80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f0:8"
              ]
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
      "definition_site": "00c21398",
      "incomplete_value": false,
      "site": "00c213a8",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c20f70",
      "incomplete_value": false,
      "site": "00c20f80",
      "value": [
        "leaf",
        "const:c35b90:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c21370",
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c21374",
      "DATA",
      [
        "storage",
        "011277c8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21378",
      "READ",
      [
        "storage",
        "011277c8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21370",
      "READ",
      [
        "storage",
        "00c9bcf0",
        null,
        "pointer"
      ]
    ],
    [
      "00c21374",
      "DATA",
      [
        "storage",
        "01127bc8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21378",
      "READ",
      [
        "storage",
        "01127bc8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c20f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20f24.md#insn-00c20f80) · [`00c20f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20f24.md#insn-00c20f48) · [`00c20f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c20f24.md#insn-00c20f70)
- 新版 `00c213a8`（命令位置の公開資料なし） · `00c21370`（命令位置の公開資料なし） · `00c21398`（命令位置の公開資料なし）

~~~diff
- 00c20f80 ["INT_ADD", "register:40f0:8", ["const:c20f80:8", "const:4:8"]]
- 00c20f80 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c213a8 ["INT_ADD", "register:40f0:8", ["const:c213a8:8", "const:4:8"]]
+ 00c213a8 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c20f80 bytes d8f20094
+ 00c213a8 bytes cef20094
- 00c20f48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
- 00c20f48 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
+ 00c21370 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c20f48 bytes 947a44f9
+ 00c21370 bytes 947a46f9
- 00c20f70 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c21398 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c20f70 bytes 02610a10
+ 00c21398 bytes 02610a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e341185ce6560b0ccaff138d518f2a44"></a>

### [`00c21050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21050.md) → [`00c21478`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21478.md) FUN_00c21478

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2149c",
      "incomplete_value": true,
      "site": "00c214a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21074",
      "incomplete_value": true,
      "site": "00c21078",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c214a8",
      "incomplete_value": true,
      "site": "00c214ac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c21080",
      "incomplete_value": true,
      "site": "00c21084",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c214d0",
      "incomplete_value": true,
      "site": "00c214d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c210a8",
      "incomplete_value": true,
      "site": "00c210ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
              ]
            ]
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
      "00c2149c",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ],
    [
      "00c214a0",
      "DATA",
      [
        "storage",
        "011277d8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c214a4",
      "READ",
      [
        "storage",
        "011277d8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c2149c",
      "READ",
      [
        "storage",
        "00c9b2f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c214a0",
      "DATA",
      [
        "storage",
        "01127bd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c214a4",
      "READ",
      [
        "storage",
        "01127bd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c210ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21050.md#insn-00c210ac) · [`00c21068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21050.md#insn-00c21068) · [`00c21074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21050.md#insn-00c21074)
- 新版 `00c214d4`（命令位置の公開資料なし） · `00c21490`（命令位置の公開資料なし） · `00c2149c`（命令位置の公開資料なし）

~~~diff
- 00c210ac ["INT_ADD", "register:40f0:8", ["const:c210ac:8", "const:4:8"]]
- 00c210ac ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c214d4 ["INT_ADD", "register:40f0:8", ["const:c214d4:8", "const:4:8"]]
+ 00c214d4 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c210ac bytes 8df20094
+ 00c214d4 bytes 83f20094
- 00c21068 ["COPY", "register:40a0:8", ["const:c9a000:8"]]
+ 00c21490 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00c21068 bytes d40300b0
+ 00c21490 bytes d40300d0
- 00c21074 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ef8:8"]]
- 00c21074 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2149c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
+ 00c2149c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c21074 bytes 947e47f9
+ 00c2149c bytes 947e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85d48dcc5531271d68bd2a5f8495250b"></a>

### [`00c2117c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c2117c.md) → [`00c215a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c215a4.md) FUN_00c215a4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c215c8",
      "incomplete_value": true,
      "site": "00c215cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c211a0",
      "incomplete_value": true,
      "site": "00c211a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c215d4",
      "incomplete_value": true,
      "site": "00c215d8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c211ac",
      "incomplete_value": true,
      "site": "00c211b0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c215fc",
      "incomplete_value": true,
      "site": "00c21600",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c211d4",
      "incomplete_value": true,
      "site": "00c211d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
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
      "00c215c8",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00c215cc",
      "DATA",
      [
        "storage",
        "011277e8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c215d0",
      "READ",
      [
        "storage",
        "011277e8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c215c8",
      "READ",
      [
        "storage",
        "00c9bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00c215cc",
      "DATA",
      [
        "storage",
        "01127be8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c215d0",
      "READ",
      [
        "storage",
        "01127be8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c211d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c2117c.md#insn-00c211d8) · [`00c211a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c2117c.md#insn-00c211a0) · [`00c211c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c2117c.md#insn-00c211c8)
- 新版 `00c21600`（命令位置の公開資料なし） · `00c215c8`（命令位置の公開資料なし） · `00c215f0`（命令位置の公開資料なし）

~~~diff
- 00c211d8 ["INT_ADD", "register:40f0:8", ["const:c211d8:8", "const:4:8"]]
- 00c211d8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c21600 ["INT_ADD", "register:40f0:8", ["const:c21600:8", "const:4:8"]]
+ 00c21600 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c211d8 bytes 42f20094
+ 00c21600 bytes 38f20094
- 00c211a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00c211a0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c215c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
+ 00c215c8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c211a0 bytes 948a44f9
+ 00c215c8 bytes 948a46f9
- 00c211c8 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c215f0 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c211c8 bytes 424e0a10
+ 00c215f0 bytes 424e0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68588db2ae2cf526960e0bbb65d13ee1"></a>

### [`00c212a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c212a8.md) → [`00c216d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c216d0.md) FUN_00c216d0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.65% / 新版 93.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c216f4",
      "incomplete_value": true,
      "site": "00c216f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c212cc",
      "incomplete_value": true,
      "site": "00c212d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c21728",
      "incomplete_value": true,
      "site": "00c2172c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21300",
      "incomplete_value": true,
      "site": "00c21304",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
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
      "definition_site": "00c2171c",
      "incomplete_value": false,
      "site": "00c2172c",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c212f4",
      "incomplete_value": false,
      "site": "00c21304",
      "value": [
        "leaf",
        "const:c35b90:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c216f4",
      "READ",
      [
        "storage",
        "00c9b920",
        null,
        "pointer"
      ]
    ],
    [
      "00c216f8",
      "DATA",
      [
        "storage",
        "01127878",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c216fc",
      "READ",
      [
        "storage",
        "01127878",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c216f4",
      "READ",
      [
        "storage",
        "00c9bd20",
        null,
        "pointer"
      ]
    ],
    [
      "00c216f8",
      "DATA",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c216fc",
      "READ",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c21304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c212a8.md#insn-00c21304) · [`00c212cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c212a8.md#insn-00c212cc) · [`00c212f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c212a8.md#insn-00c212f4)
- 新版 `00c2172c`（命令位置の公開資料なし） · `00c216f4`（命令位置の公開資料なし） · `00c2171c`（命令位置の公開資料なし）

~~~diff
- 00c21304 ["INT_ADD", "register:40f0:8", ["const:c21304:8", "const:4:8"]]
- 00c21304 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c2172c ["INT_ADD", "register:40f0:8", ["const:c2172c:8", "const:4:8"]]
+ 00c2172c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c21304 bytes f7f10094
+ 00c2172c bytes edf10094
- 00c212cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00c212cc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c216f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00c216f4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c212cc bytes 949244f9
+ 00c216f4 bytes 949246f9
- 00c212f4 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c2171c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c212f4 bytes e2440a10
+ 00c2171c bytes e2440a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b6a39041adba1f5efa8e5ad5a70fbdc"></a>

### [`00c213d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c213d4.md) → [`00c217fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c217fc.md) FUN_00c217fc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 5件 [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5dae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dae0.md)
- 新版 呼出元 2件 [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) · 呼出先 5件 [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c5dee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21820",
      "incomplete_value": true,
      "site": "00c21824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c213f8",
      "incomplete_value": true,
      "site": "00c213fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c2182c",
      "incomplete_value": true,
      "site": "00c21830",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c21404",
      "incomplete_value": true,
      "site": "00c21408",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c21854",
      "incomplete_value": true,
      "site": "00c21858",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2142c",
      "incomplete_value": true,
      "site": "00c21430",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
            ]
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
      "00c21820",
      "READ",
      [
        "storage",
        "00c9b930",
        null,
        "pointer"
      ]
    ],
    [
      "00c21824",
      "DATA",
      [
        "storage",
        "01127888",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21828",
      "READ",
      [
        "storage",
        "01127888",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c21820",
      "READ",
      [
        "storage",
        "00c9bd30",
        null,
        "pointer"
      ]
    ],
    [
      "00c21824",
      "DATA",
      [
        "storage",
        "01127c88",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c21828",
      "READ",
      [
        "storage",
        "01127c88",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c21430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c213d4.md#insn-00c21430) · [`00c213f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c213d4.md#insn-00c213f8) · [`00c21420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c213d4.md#insn-00c21420)
- 新版 `00c21858`（命令位置の公開資料なし） · `00c21820`（命令位置の公開資料なし） · `00c21848`（命令位置の公開資料なし）

~~~diff
- 00c21430 ["INT_ADD", "register:40f0:8", ["const:c21430:8", "const:4:8"]]
- 00c21430 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c21858 ["INT_ADD", "register:40f0:8", ["const:c21858:8", "const:4:8"]]
+ 00c21858 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c21430 bytes acf10094
+ 00c21858 bytes a2f10094
- 00c213f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
- 00c213f8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c21820 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d30:8"]]
+ 00c21820 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c213f8 bytes 949a44f9
+ 00c21820 bytes 949a46f9
- 00c21420 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c21848 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c21420 bytes 823b0a10
+ 00c21848 bytes 823b0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fc1425c5dc7a766c494c877de5be32c"></a>

### [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) → [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) FUN_00c21928

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00c24c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c78.md) [`00c24dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24dc8.md) · 呼出先 40件 [`00c1d138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d138.md) [`00c1f7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md) [`00c1f8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) [`00c1fa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md) [`00c1fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fb2c.md)
- 新版 呼出元 2件 [`00c250a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c250a0.md) [`00c251f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c251f0.md) · 呼出先 40件 [`00c1d560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d560.md) [`00c1fbd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fbd0.md) [`00c1fcfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fcfc.md) [`00c1fe28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1fe28.md) [`00c1ff54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1ff54.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.59% / 新版 88.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 13件

アドレスに依存する影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2195c",
      "incomplete_value": false,
      "site": "00c2195c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21534",
      "incomplete_value": false,
      "site": "00c21534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "definition_site": "00c21aec",
      "incomplete_value": true,
      "site": "00c21aec",
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
      "definition_site": "00c216c4",
      "incomplete_value": true,
      "site": "00c216c4",
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21b24",
      "incomplete_value": true,
      "site": "00c21b28",
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
      "definition_site": "00c216fc",
      "incomplete_value": true,
      "site": "00c21700",
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
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c2195c",
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c21ae4",
      "READ",
      [
        "storage",
        "00c9b938",
        null,
        "pointer"
      ]
    ],
    [
      "00c21aec",
      "DATA",
      [
        "storage",
        "00c955d0",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00c2195c",
      "DATA",
      [
        "storage",
        "00c936c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00c21ae4",
      "READ",
      [
        "storage",
        "00c9bd38",
        null,
        "pointer"
      ]
    ],
    [
      "00c21aec",
      "DATA",
      [
        "storage",
        "00c959d0",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c21528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md#insn-00c21528) · [`00c215a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md#insn-00c215a8) · [`00c215c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md#insn-00c215c4)
- 新版 `00c21950`（命令位置の公開資料なし） · `00c219d0`（命令位置の公開資料なし） · `00c219ec`（命令位置の公開資料なし）

~~~diff
- 00c21528 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00c21528 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c21528 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c21528 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c21950 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00c21950 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c21950 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c21950 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c21528 bytes 29010b91
+ 00c21950 bytes 29011b91
- 00c215a8 ["INT_ADD", "register:40f0:8", ["const:c215a8:8", "const:4:8"]]
- 00c215a8 ["CALL", null, ["callee:00c1d560:8"]]
+ 00c219d0 ["INT_ADD", "register:40f0:8", ["const:c219d0:8", "const:4:8"]]
+ 00c219d0 ["CALL", null, ["callee:00c1d560:8"]]
- 00c215a8 bytes e4eeff97
+ 00c219d0 bytes e4eeff97
- 00c215c4 ["INT_ADD", "register:40f0:8", ["const:c215c4:8", "const:4:8"]]
- 00c215c4 ["CALL", null, ["callee:00c358e8:8"]]
+ 00c219ec ["INT_ADD", "register:40f0:8", ["const:c219ec:8", "const:4:8"]]
+ 00c219ec ["CALL", null, ["callee:00c358e8:8"]]
- 00c215c4 bytes bf4f0094
+ 00c219ec bytes bf4f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1114e81b62fcfee8567632e98538bf0"></a>

### [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) → [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) FUN_00c21f78

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c24e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24e40.md) · 呼出先 33件 [`00c1d138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d138.md) [`00c21eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21eb4.md) [`00c21ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21ff8.md) [`00c2213c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2213c.md) [`00c22280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22280.md)
- 新版 呼出元 1件 [`00c25268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25268.md) · 呼出先 33件 [`00c1d560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1d/00c1d560.md) [`00c222dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c222dc.md) [`00c22420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22420.md) [`00c22564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22564.md) [`00c226a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c226a8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c21fa8",
      "incomplete_value": false,
      "site": "00c21fa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21b80",
      "incomplete_value": false,
      "site": "00c21b80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c21fa8",
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c21fa8",
      "DATA",
      [
        "storage",
        "00c936c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c21b74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md#insn-00c21b74) · [`00c21bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md#insn-00c21bf4) · [`00c21c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md#insn-00c21c10)
- 新版 `00c21f9c`（命令位置の公開資料なし） · `00c2201c`（命令位置の公開資料なし） · `00c22038`（命令位置の公開資料なし）

~~~diff
- 00c21b74 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00c21b74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c21b74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c21b74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c21f9c ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00c21f9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c21f9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c21f9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c21b74 bytes 29010b91
+ 00c21f9c bytes 29011b91
- 00c21bf4 ["INT_ADD", "register:40f0:8", ["const:c21bf4:8", "const:4:8"]]
- 00c21bf4 ["CALL", null, ["callee:00c1d560:8"]]
+ 00c2201c ["INT_ADD", "register:40f0:8", ["const:c2201c:8", "const:4:8"]]
+ 00c2201c ["CALL", null, ["callee:00c1d560:8"]]
- 00c21bf4 bytes 51edff97
+ 00c2201c bytes 51edff97
- 00c21c10 ["INT_ADD", "register:40f0:8", ["const:c21c10:8", "const:4:8"]]
- 00c21c10 ["CALL", null, ["callee:00c358e8:8"]]
+ 00c22038 ["INT_ADD", "register:40f0:8", ["const:c22038:8", "const:4:8"]]
+ 00c22038 ["CALL", null, ["callee:00c358e8:8"]]
- 00c21c10 bytes 2c4e0094
+ 00c22038 bytes 2c4e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c29b939fbff670064591560b840f657c"></a>

### [`00c21eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21eb4.md) → [`00c222dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c222dc.md) FUN_00c222dc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22300",
      "incomplete_value": true,
      "site": "00c22304",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21ed8",
      "incomplete_value": true,
      "site": "00c21edc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c2230c",
      "incomplete_value": true,
      "site": "00c22310",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c21ee4",
      "incomplete_value": true,
      "site": "00c21ee8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22334",
      "incomplete_value": true,
      "site": "00c22338",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c21f0c",
      "incomplete_value": true,
      "site": "00c21f10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
              ]
            ]
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
      "00c22300",
      "READ",
      [
        "storage",
        "00c9af78",
        null,
        "pointer"
      ]
    ],
    [
      "00c22304",
      "DATA",
      [
        "storage",
        "01127758",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22308",
      "READ",
      [
        "storage",
        "01127758",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22300",
      "READ",
      [
        "storage",
        "00c9b378",
        null,
        "pointer"
      ]
    ],
    [
      "00c22304",
      "DATA",
      [
        "storage",
        "01127b58",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22308",
      "READ",
      [
        "storage",
        "01127b58",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c21f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21eb4.md#insn-00c21f10) · [`00c21ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21eb4.md#insn-00c21ecc) · [`00c21ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21eb4.md#insn-00c21ed8)
- 新版 `00c22338`（命令位置の公開資料なし） · `00c222f4`（命令位置の公開資料なし） · `00c22300`（命令位置の公開資料なし）

~~~diff
- 00c21f10 ["INT_ADD", "register:40f0:8", ["const:c21f10:8", "const:4:8"]]
- 00c21f10 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c22338 ["INT_ADD", "register:40f0:8", ["const:c22338:8", "const:4:8"]]
+ 00c22338 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c21f10 bytes f4ee0094
+ 00c22338 bytes eaee0094
- 00c21ecc ["COPY", "register:40a0:8", ["const:c9a000:8"]]
+ 00c222f4 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00c21ecc bytes d40300b0
+ 00c222f4 bytes d40300b0
- 00c21ed8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f78:8"]]
- 00c21ed8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22300 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
+ 00c22300 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c21ed8 bytes 94be47f9
+ 00c22300 bytes 94be41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60b6067852e8dd526ccb6b2c48c867d5"></a>

### [`00c21ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21ff8.md) → [`00c22420`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22420.md) FUN_00c22420

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22444",
      "incomplete_value": true,
      "site": "00c22448",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2201c",
      "incomplete_value": true,
      "site": "00c22020",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c22450",
      "incomplete_value": true,
      "site": "00c22454",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22028",
      "incomplete_value": true,
      "site": "00c2202c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22478",
      "incomplete_value": true,
      "site": "00c2247c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22050",
      "incomplete_value": true,
      "site": "00c22054",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:808:8"
              ]
            ]
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
      "00c22444",
      "READ",
      [
        "storage",
        "00c9b808",
        null,
        "pointer"
      ]
    ],
    [
      "00c22448",
      "DATA",
      [
        "storage",
        "01127768",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2244c",
      "READ",
      [
        "storage",
        "01127768",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22444",
      "READ",
      [
        "storage",
        "00c9bc08",
        null,
        "pointer"
      ]
    ],
    [
      "00c22448",
      "DATA",
      [
        "storage",
        "01127b68",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2244c",
      "READ",
      [
        "storage",
        "01127b68",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21ff8.md#insn-00c22054) · [`00c2201c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21ff8.md#insn-00c2201c) · [`00c22044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21ff8.md#insn-00c22044)
- 新版 `00c2247c`（命令位置の公開資料なし） · `00c22444`（命令位置の公開資料なし） · `00c2246c`（命令位置の公開資料なし）

~~~diff
- 00c22054 ["INT_ADD", "register:40f0:8", ["const:c22054:8", "const:4:8"]]
- 00c22054 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c2247c ["INT_ADD", "register:40f0:8", ["const:c2247c:8", "const:4:8"]]
+ 00c2247c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c22054 bytes a3ee0094
+ 00c2247c bytes 99ee0094
- 00c2201c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:808:8"]]
- 00c2201c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22444 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c08:8"]]
+ 00c22444 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2201c bytes 940644f9
+ 00c22444 bytes 940646f9
- 00c22044 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c2246c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c22044 bytes 62da0910
+ 00c2246c bytes 62da0910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bba30d0e0be5beefc8538aeb224b3c1d"></a>

### [`00c2213c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2213c.md) → [`00c22564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22564.md) FUN_00c22564

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22588",
      "incomplete_value": true,
      "site": "00c2258c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c22160",
      "incomplete_value": true,
      "site": "00c22164",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c22594",
      "incomplete_value": true,
      "site": "00c22598",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c2216c",
      "incomplete_value": true,
      "site": "00c22170",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c225bc",
      "incomplete_value": true,
      "site": "00c225c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
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
      "definition_site": "00c22194",
      "incomplete_value": true,
      "site": "00c22198",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
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
      "00c22588",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00c2258c",
      "DATA",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22590",
      "READ",
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
      "00c22588",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "00c2258c",
      "DATA",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22590",
      "READ",
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

- 旧版 [`00c22198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2213c.md#insn-00c22198) · [`00c22160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2213c.md#insn-00c22160) · [`00c22188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2213c.md#insn-00c22188)
- 新版 `00c225c0`（命令位置の公開資料なし） · `00c22588`（命令位置の公開資料なし） · `00c225b0`（命令位置の公開資料なし）

~~~diff
- 00c22198 ["INT_ADD", "register:40f0:8", ["const:c22198:8", "const:4:8"]]
- 00c22198 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c225c0 ["INT_ADD", "register:40f0:8", ["const:c225c0:8", "const:4:8"]]
+ 00c225c0 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c22198 bytes 52ee0094
+ 00c225c0 bytes 48ee0094
- 00c22160 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00c22160 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22588 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
+ 00c22588 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22160 bytes 941a44f9
+ 00c22588 bytes 941a46f9
- 00c22188 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c225b0 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c22188 bytes 42d00910
+ 00c225b0 bytes 42d00910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34a449af5b6bddd01b8cb8d962cc4611"></a>

### [`00c22280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22280.md) → [`00c226a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c226a8.md) FUN_00c226a8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c226cc",
      "incomplete_value": true,
      "site": "00c226d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c222a4",
      "incomplete_value": true,
      "site": "00c222a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c226d8",
      "incomplete_value": true,
      "site": "00c226dc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c222b0",
      "incomplete_value": true,
      "site": "00c222b4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22700",
      "incomplete_value": true,
      "site": "00c22704",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c222d8",
      "incomplete_value": true,
      "site": "00c222dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
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
      "00c226cc",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00c226d0",
      "DATA",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c226d4",
      "READ",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c226cc",
      "READ",
      [
        "storage",
        "00c9bb40",
        null,
        "pointer"
      ]
    ],
    [
      "00c226d0",
      "DATA",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c226d4",
      "READ",
      [
        "storage",
        "01127e08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c222dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22280.md#insn-00c222dc) · [`00c222a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22280.md#insn-00c222a4) · [`00c222cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22280.md#insn-00c222cc)
- 新版 `00c22704`（命令位置の公開資料なし） · `00c226cc`（命令位置の公開資料なし） · `00c226f4`（命令位置の公開資料なし）

~~~diff
- 00c222dc ["INT_ADD", "register:40f0:8", ["const:c222dc:8", "const:4:8"]]
- 00c222dc ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c22704 ["INT_ADD", "register:40f0:8", ["const:c22704:8", "const:4:8"]]
+ 00c22704 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c222dc bytes 01ee0094
+ 00c22704 bytes f7ed0094
- 00c222a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
- 00c222a4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c226cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b40:8"]]
+ 00c226cc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c222a4 bytes 94a243f9
+ 00c226cc bytes 94a245f9
- 00c222cc ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c226f4 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c222cc bytes 22c60910
+ 00c226f4 bytes 22c60910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91618e2a8fb2d62914ceff80008a44a0"></a>

### [`00c223c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c223c4.md) → [`00c227ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c227ec.md) FUN_00c227ec

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22810",
      "incomplete_value": true,
      "site": "00c22814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c223e8",
      "incomplete_value": true,
      "site": "00c223ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c2281c",
      "incomplete_value": true,
      "site": "00c22820",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c223f4",
      "incomplete_value": true,
      "site": "00c223f8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22844",
      "incomplete_value": true,
      "site": "00c22848",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2241c",
      "incomplete_value": true,
      "site": "00c22420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
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
      "00c22810",
      "READ",
      [
        "storage",
        "00c9b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c22814",
      "DATA",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22818",
      "READ",
      [
        "storage",
        "01127a28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22810",
      "READ",
      [
        "storage",
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c22814",
      "DATA",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22818",
      "READ",
      [
        "storage",
        "01127e28",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c223c4.md#insn-00c22420) · [`00c223e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c223c4.md#insn-00c223e8) · [`00c22410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c223c4.md#insn-00c22410)
- 新版 `00c22848`（命令位置の公開資料なし） · `00c22810`（命令位置の公開資料なし） · `00c22838`（命令位置の公開資料なし）

~~~diff
- 00c22420 ["INT_ADD", "register:40f0:8", ["const:c22420:8", "const:4:8"]]
- 00c22420 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c22848 ["INT_ADD", "register:40f0:8", ["const:c22848:8", "const:4:8"]]
+ 00c22848 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c22420 bytes b0ed0094
+ 00c22848 bytes a6ed0094
- 00c223e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4b8:8"]]
- 00c223e8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22810 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
+ 00c22810 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c223e8 bytes 945e42f9
+ 00c22810 bytes 945e44f9
- 00c22410 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c22838 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c22410 bytes 02bc0910
+ 00c22838 bytes 02bc0910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f2383cce8037404c0e7d94faeba02f1"></a>

### [`00c22508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22508.md) → [`00c22930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22930.md) FUN_00c22930

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22954",
      "incomplete_value": true,
      "site": "00c22958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2252c",
      "incomplete_value": true,
      "site": "00c22530",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:828:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c22960",
      "incomplete_value": true,
      "site": "00c22964",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22538",
      "incomplete_value": true,
      "site": "00c2253c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22988",
      "incomplete_value": true,
      "site": "00c2298c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22560",
      "incomplete_value": true,
      "site": "00c22564",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:828:8"
              ]
            ]
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
      "00c22954",
      "READ",
      [
        "storage",
        "00c9b828",
        null,
        "pointer"
      ]
    ],
    [
      "00c22958",
      "DATA",
      [
        "storage",
        "01127a48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2295c",
      "READ",
      [
        "storage",
        "01127a48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22954",
      "READ",
      [
        "storage",
        "00c9bc28",
        null,
        "pointer"
      ]
    ],
    [
      "00c22958",
      "DATA",
      [
        "storage",
        "01127e48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2295c",
      "READ",
      [
        "storage",
        "01127e48",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22508.md#insn-00c22564) · [`00c2252c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22508.md#insn-00c2252c) · [`00c22554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22508.md#insn-00c22554)
- 新版 `00c2298c`（命令位置の公開資料なし） · `00c22954`（命令位置の公開資料なし） · `00c2297c`（命令位置の公開資料なし）

~~~diff
- 00c22564 ["INT_ADD", "register:40f0:8", ["const:c22564:8", "const:4:8"]]
- 00c22564 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c2298c ["INT_ADD", "register:40f0:8", ["const:c2298c:8", "const:4:8"]]
+ 00c2298c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c22564 bytes 5fed0094
+ 00c2298c bytes 55ed0094
- 00c2252c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00c2252c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22954 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c28:8"]]
+ 00c22954 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2252c bytes 941644f9
+ 00c22954 bytes 941646f9
- 00c22554 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c2297c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c22554 bytes e2b10910
+ 00c2297c bytes e2b10910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-548057c03f14ffa17f275841874b0562"></a>

### [`00c2264c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2264c.md) → [`00c22a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22a74.md) FUN_00c22a74

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22a98",
      "incomplete_value": true,
      "site": "00c22a9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22670",
      "incomplete_value": true,
      "site": "00c22674",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c22aa4",
      "incomplete_value": true,
      "site": "00c22aa8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c2267c",
      "incomplete_value": true,
      "site": "00c22680",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22acc",
      "incomplete_value": true,
      "site": "00c22ad0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c226a4",
      "incomplete_value": true,
      "site": "00c226a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:838:8"
              ]
            ]
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
      "00c22a98",
      "READ",
      [
        "storage",
        "00c9b838",
        null,
        "pointer"
      ]
    ],
    [
      "00c22a9c",
      "DATA",
      [
        "storage",
        "01127a68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22aa0",
      "READ",
      [
        "storage",
        "01127a68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22a98",
      "READ",
      [
        "storage",
        "00c9bc38",
        null,
        "pointer"
      ]
    ],
    [
      "00c22a9c",
      "DATA",
      [
        "storage",
        "01127e68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22aa0",
      "READ",
      [
        "storage",
        "01127e68",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c226a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2264c.md#insn-00c226a8) · [`00c22670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2264c.md#insn-00c22670) · [`00c22698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c2264c.md#insn-00c22698)
- 新版 `00c22ad0`（命令位置の公開資料なし） · `00c22a98`（命令位置の公開資料なし） · `00c22ac0`（命令位置の公開資料なし）

~~~diff
- 00c226a8 ["INT_ADD", "register:40f0:8", ["const:c226a8:8", "const:4:8"]]
- 00c226a8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c22ad0 ["INT_ADD", "register:40f0:8", ["const:c22ad0:8", "const:4:8"]]
+ 00c22ad0 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c226a8 bytes 0eed0094
+ 00c22ad0 bytes 04ed0094
- 00c22670 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:838:8"]]
- 00c22670 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22a98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c38:8"]]
+ 00c22a98 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22670 bytes 941e44f9
+ 00c22a98 bytes 941e46f9
- 00c22698 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c22ac0 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c22698 bytes c2a70910
+ 00c22ac0 bytes c2a70910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85d6f58e342b575040f32bf1b8dcfdd9"></a>

### [`00c22790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22790.md) → [`00c22bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22bb8.md) FUN_00c22bb8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22bdc",
      "incomplete_value": true,
      "site": "00c22be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c227b4",
      "incomplete_value": true,
      "site": "00c227b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:848:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c22be8",
      "incomplete_value": true,
      "site": "00c22bec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c227c0",
      "incomplete_value": true,
      "site": "00c227c4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22c10",
      "incomplete_value": true,
      "site": "00c22c14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c227e8",
      "incomplete_value": true,
      "site": "00c227ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:848:8"
              ]
            ]
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
      "00c22bdc",
      "READ",
      [
        "storage",
        "00c9b848",
        null,
        "pointer"
      ]
    ],
    [
      "00c22be0",
      "DATA",
      [
        "storage",
        "01127a58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22be4",
      "READ",
      [
        "storage",
        "01127a58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22bdc",
      "READ",
      [
        "storage",
        "00c9bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00c22be0",
      "DATA",
      [
        "storage",
        "01127e58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22be4",
      "READ",
      [
        "storage",
        "01127e58",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c227ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22790.md#insn-00c227ec) · [`00c227b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22790.md#insn-00c227b4) · [`00c227dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22790.md#insn-00c227dc)
- 新版 `00c22c14`（命令位置の公開資料なし） · `00c22bdc`（命令位置の公開資料なし） · `00c22c04`（命令位置の公開資料なし）

~~~diff
- 00c227ec ["INT_ADD", "register:40f0:8", ["const:c227ec:8", "const:4:8"]]
- 00c227ec ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c22c14 ["INT_ADD", "register:40f0:8", ["const:c22c14:8", "const:4:8"]]
+ 00c22c14 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c227ec bytes bdec0094
+ 00c22c14 bytes b3ec0094
- 00c227b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:848:8"]]
- 00c227b4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22bdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c48:8"]]
+ 00c22bdc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c227b4 bytes 942644f9
+ 00c22bdc bytes 942646f9
- 00c227dc ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c22c04 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c227dc bytes a29d0910
+ 00c22c04 bytes a29d0910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d56bb6bcd82a1c3499561d47e79ec622"></a>

### [`00c228d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c228d4.md) → [`00c22cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22cfc.md) FUN_00c22cfc

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22d20",
      "incomplete_value": true,
      "site": "00c22d24",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c228f8",
      "incomplete_value": true,
      "site": "00c228fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:858:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c22d2c",
      "incomplete_value": true,
      "site": "00c22d30",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22904",
      "incomplete_value": true,
      "site": "00c22908",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22d54",
      "incomplete_value": true,
      "site": "00c22d58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2292c",
      "incomplete_value": true,
      "site": "00c22930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:858:8"
              ]
            ]
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
      "00c22d20",
      "READ",
      [
        "storage",
        "00c9b858",
        null,
        "pointer"
      ]
    ],
    [
      "00c22d24",
      "DATA",
      [
        "storage",
        "01127a78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22d28",
      "READ",
      [
        "storage",
        "01127a78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22d20",
      "READ",
      [
        "storage",
        "00c9bc58",
        null,
        "pointer"
      ]
    ],
    [
      "00c22d24",
      "DATA",
      [
        "storage",
        "01127e78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22d28",
      "READ",
      [
        "storage",
        "01127e78",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c228d4.md#insn-00c22930) · [`00c228f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c228d4.md#insn-00c228f8) · [`00c22920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c228d4.md#insn-00c22920)
- 新版 `00c22d58`（命令位置の公開資料なし） · `00c22d20`（命令位置の公開資料なし） · `00c22d48`（命令位置の公開資料なし）

~~~diff
- 00c22930 ["INT_ADD", "register:40f0:8", ["const:c22930:8", "const:4:8"]]
- 00c22930 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c22d58 ["INT_ADD", "register:40f0:8", ["const:c22d58:8", "const:4:8"]]
+ 00c22d58 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c22930 bytes 6cec0094
+ 00c22d58 bytes 62ec0094
- 00c228f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
- 00c228f8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22d20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00c22d20 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c228f8 bytes 942e44f9
+ 00c22d20 bytes 942e46f9
- 00c22920 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c22d48 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c22920 bytes 82930910
+ 00c22d48 bytes 82930910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-487ea7cf3e2e8b64fa9421cc4a475da4"></a>

### [`00c22a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22a18.md) → [`00c22e40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22e40.md) FUN_00c22e40

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22e64",
      "incomplete_value": true,
      "site": "00c22e68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22a3c",
      "incomplete_value": true,
      "site": "00c22a40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c22e70",
      "incomplete_value": true,
      "site": "00c22e74",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22a48",
      "incomplete_value": true,
      "site": "00c22a4c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22e98",
      "incomplete_value": true,
      "site": "00c22e9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22a70",
      "incomplete_value": true,
      "site": "00c22a74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a8:8"
              ]
            ]
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
      "00c22e64",
      "READ",
      [
        "storage",
        "00c9b7a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c22e68",
      "DATA",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22e6c",
      "READ",
      [
        "storage",
        "01127a38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22e64",
      "READ",
      [
        "storage",
        "00c9bba8",
        null,
        "pointer"
      ]
    ],
    [
      "00c22e68",
      "DATA",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22e6c",
      "READ",
      [
        "storage",
        "01127e38",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22a18.md#insn-00c22a74) · [`00c22a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22a18.md#insn-00c22a3c) · [`00c22a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22a18.md#insn-00c22a64)
- 新版 `00c22e9c`（命令位置の公開資料なし） · `00c22e64`（命令位置の公開資料なし） · `00c22e8c`（命令位置の公開資料なし）

~~~diff
- 00c22a74 ["INT_ADD", "register:40f0:8", ["const:c22a74:8", "const:4:8"]]
- 00c22a74 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c22e9c ["INT_ADD", "register:40f0:8", ["const:c22e9c:8", "const:4:8"]]
+ 00c22e9c ["CALL", null, ["callee:00c5dee0:8"]]
- 00c22a74 bytes 1bec0094
+ 00c22e9c bytes 11ec0094
- 00c22a3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a8:8"]]
- 00c22a3c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22e64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ba8:8"]]
+ 00c22e64 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22a3c bytes 94d643f9
+ 00c22e64 bytes 94d645f9
- 00c22a64 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c22e8c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c22a64 bytes 62890910
+ 00c22e8c bytes 62890910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2ef195cd572add8c19a7a6f43309c37"></a>

### [`00c22b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22b5c.md) → [`00c22f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c22/00c22f84.md) FUN_00c22f84

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c22fa8",
      "incomplete_value": true,
      "site": "00c22fac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22b80",
      "incomplete_value": true,
      "site": "00c22b84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c22fb4",
      "incomplete_value": true,
      "site": "00c22fb8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22b8c",
      "incomplete_value": true,
      "site": "00c22b90",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22fdc",
      "incomplete_value": true,
      "site": "00c22fe0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22bb4",
      "incomplete_value": true,
      "site": "00c22bb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e0:8"
              ]
            ]
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
      "00c22fa8",
      "READ",
      [
        "storage",
        "00c9b7e0",
        null,
        "pointer"
      ]
    ],
    [
      "00c22fac",
      "DATA",
      [
        "storage",
        "011277f8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22fb0",
      "READ",
      [
        "storage",
        "011277f8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c22fa8",
      "READ",
      [
        "storage",
        "00c9bbe0",
        null,
        "pointer"
      ]
    ],
    [
      "00c22fac",
      "DATA",
      [
        "storage",
        "01127bf8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c22fb0",
      "READ",
      [
        "storage",
        "01127bf8",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22b5c.md#insn-00c22bb8) · [`00c22b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22b5c.md#insn-00c22b80) · [`00c22ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22b5c.md#insn-00c22ba8)
- 新版 `00c22fe0`（命令位置の公開資料なし） · `00c22fa8`（命令位置の公開資料なし） · `00c22fd0`（命令位置の公開資料なし）

~~~diff
- 00c22bb8 ["INT_ADD", "register:40f0:8", ["const:c22bb8:8", "const:4:8"]]
- 00c22bb8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c22fe0 ["INT_ADD", "register:40f0:8", ["const:c22fe0:8", "const:4:8"]]
+ 00c22fe0 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c22bb8 bytes caeb0094
+ 00c22fe0 bytes c0eb0094
- 00c22b80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
- 00c22b80 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c22fa8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be0:8"]]
+ 00c22fa8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22b80 bytes 94f243f9
+ 00c22fa8 bytes 94f245f9
- 00c22ba8 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c22fd0 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c22ba8 bytes 427f0910
+ 00c22fd0 bytes 427f0910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f700d71b00a279fd3f3279a06aed5d4"></a>

### [`00c22ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22ca0.md) → [`00c230c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c230c8.md) FUN_00c230c8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c230ec",
      "incomplete_value": true,
      "site": "00c230f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22cc4",
      "incomplete_value": true,
      "site": "00c22cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c230f8",
      "incomplete_value": true,
      "site": "00c230fc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22cd0",
      "incomplete_value": true,
      "site": "00c22cd4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23120",
      "incomplete_value": true,
      "site": "00c23124",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22cf8",
      "incomplete_value": true,
      "site": "00c22cfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7d8:8"
              ]
            ]
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
      "00c230ec",
      "READ",
      [
        "storage",
        "00c9b7d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c230f0",
      "DATA",
      [
        "storage",
        "01127808",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c230f4",
      "READ",
      [
        "storage",
        "01127808",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c230ec",
      "READ",
      [
        "storage",
        "00c9bbd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c230f0",
      "DATA",
      [
        "storage",
        "01127c08",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c230f4",
      "READ",
      [
        "storage",
        "01127c08",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22ca0.md#insn-00c22cfc) · [`00c22cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22ca0.md#insn-00c22cc4) · [`00c22cec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22ca0.md#insn-00c22cec)
- 新版 `00c23124`（命令位置の公開資料なし） · `00c230ec`（命令位置の公開資料なし） · `00c23114`（命令位置の公開資料なし）

~~~diff
- 00c22cfc ["INT_ADD", "register:40f0:8", ["const:c22cfc:8", "const:4:8"]]
- 00c22cfc ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c23124 ["INT_ADD", "register:40f0:8", ["const:c23124:8", "const:4:8"]]
+ 00c23124 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c22cfc bytes 79eb0094
+ 00c23124 bytes 6feb0094
- 00c22cc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d8:8"]]
- 00c22cc4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c230ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bd8:8"]]
+ 00c230ec ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22cc4 bytes 94ee43f9
+ 00c230ec bytes 94ee45f9
- 00c22cec ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c23114 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c22cec bytes 22750910
+ 00c23114 bytes 22750910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8d7e3a8031ee29f0a3557e0a5d9473e"></a>

### [`00c22de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22de4.md) → [`00c2320c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c2320c.md) FUN_00c2320c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23230",
      "incomplete_value": true,
      "site": "00c23234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22e08",
      "incomplete_value": true,
      "site": "00c22e0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c2323c",
      "incomplete_value": true,
      "site": "00c23240",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22e14",
      "incomplete_value": true,
      "site": "00c22e18",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23264",
      "incomplete_value": true,
      "site": "00c23268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22e3c",
      "incomplete_value": true,
      "site": "00c22e40",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7f0:8"
              ]
            ]
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
      "00c23230",
      "READ",
      [
        "storage",
        "00c9b7f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c23234",
      "DATA",
      [
        "storage",
        "01127818",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23238",
      "READ",
      [
        "storage",
        "01127818",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23230",
      "READ",
      [
        "storage",
        "00c9bbf0",
        null,
        "pointer"
      ]
    ],
    [
      "00c23234",
      "DATA",
      [
        "storage",
        "01127c18",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23238",
      "READ",
      [
        "storage",
        "01127c18",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22de4.md#insn-00c22e40) · [`00c22e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22de4.md#insn-00c22e08) · [`00c22e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22de4.md#insn-00c22e30)
- 新版 `00c23268`（命令位置の公開資料なし） · `00c23230`（命令位置の公開資料なし） · `00c23258`（命令位置の公開資料なし）

~~~diff
- 00c22e40 ["INT_ADD", "register:40f0:8", ["const:c22e40:8", "const:4:8"]]
- 00c22e40 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c23268 ["INT_ADD", "register:40f0:8", ["const:c23268:8", "const:4:8"]]
+ 00c23268 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c22e40 bytes 28eb0094
+ 00c23268 bytes 1eeb0094
- 00c22e08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f0:8"]]
- 00c22e08 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23230 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bf0:8"]]
+ 00c23230 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22e08 bytes 94fa43f9
+ 00c23230 bytes 94fa45f9
- 00c22e30 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c23258 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c22e30 bytes 026b0910
+ 00c23258 bytes 026b0910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca6d176bced75029b2b40e0a1159e142"></a>

### [`00c22f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22f28.md) → [`00c23350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c23350.md) FUN_00c23350

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23374",
      "incomplete_value": true,
      "site": "00c23378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22f4c",
      "incomplete_value": true,
      "site": "00c22f50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c23380",
      "incomplete_value": true,
      "site": "00c23384",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c22f58",
      "incomplete_value": true,
      "site": "00c22f5c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c233a8",
      "incomplete_value": true,
      "site": "00c233ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c22f80",
      "incomplete_value": true,
      "site": "00c22f84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e8:8"
              ]
            ]
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
      "00c23374",
      "READ",
      [
        "storage",
        "00c9b7e8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23378",
      "DATA",
      [
        "storage",
        "01127828",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2337c",
      "READ",
      [
        "storage",
        "01127828",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23374",
      "READ",
      [
        "storage",
        "00c9bbe8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23378",
      "DATA",
      [
        "storage",
        "01127c28",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2337c",
      "READ",
      [
        "storage",
        "01127c28",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c22f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22f28.md#insn-00c22f84) · [`00c22f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22f28.md#insn-00c22f4c) · [`00c22f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c22/00c22f28.md#insn-00c22f74)
- 新版 `00c233ac`（命令位置の公開資料なし） · `00c23374`（命令位置の公開資料なし） · `00c2339c`（命令位置の公開資料なし）

~~~diff
- 00c22f84 ["INT_ADD", "register:40f0:8", ["const:c22f84:8", "const:4:8"]]
- 00c22f84 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c233ac ["INT_ADD", "register:40f0:8", ["const:c233ac:8", "const:4:8"]]
+ 00c233ac ["CALL", null, ["callee:00c5dee0:8"]]
- 00c22f84 bytes d7ea0094
+ 00c233ac bytes cdea0094
- 00c22f4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
- 00c22f4c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23374 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
+ 00c23374 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c22f4c bytes 94f643f9
+ 00c23374 bytes 94f645f9
- 00c22f74 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c2339c ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c22f74 bytes e2600910
+ 00c2339c bytes e2600910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-924535e82685a2c26fedc4fe6194f7de"></a>

### [`00c2306c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c2306c.md) → [`00c23494`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c23494.md) FUN_00c23494

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c234b8",
      "incomplete_value": true,
      "site": "00c234bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23090",
      "incomplete_value": true,
      "site": "00c23094",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c234c4",
      "incomplete_value": true,
      "site": "00c234c8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c2309c",
      "incomplete_value": true,
      "site": "00c230a0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c234ec",
      "incomplete_value": true,
      "site": "00c234f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c230c4",
      "incomplete_value": true,
      "site": "00c230c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8a8:8"
              ]
            ]
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
      "00c234b8",
      "READ",
      [
        "storage",
        "00c9b8a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c234bc",
      "DATA",
      [
        "storage",
        "01127838",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c234c0",
      "READ",
      [
        "storage",
        "01127838",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c234b8",
      "READ",
      [
        "storage",
        "00c9bca8",
        null,
        "pointer"
      ]
    ],
    [
      "00c234bc",
      "DATA",
      [
        "storage",
        "01127c38",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c234c0",
      "READ",
      [
        "storage",
        "01127c38",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c230c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c2306c.md#insn-00c230c8) · [`00c23090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c2306c.md#insn-00c23090) · [`00c230b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c2306c.md#insn-00c230b8)
- 新版 `00c234f0`（命令位置の公開資料なし） · `00c234b8`（命令位置の公開資料なし） · `00c234e0`（命令位置の公開資料なし）

~~~diff
- 00c230c8 ["INT_ADD", "register:40f0:8", ["const:c230c8:8", "const:4:8"]]
- 00c230c8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c234f0 ["INT_ADD", "register:40f0:8", ["const:c234f0:8", "const:4:8"]]
+ 00c234f0 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c230c8 bytes 86ea0094
+ 00c234f0 bytes 7cea0094
- 00c23090 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00c23090 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c234b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca8:8"]]
+ 00c234b8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23090 bytes 945644f9
+ 00c234b8 bytes 945646f9
- 00c230b8 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c234e0 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c230b8 bytes c2560910
+ 00c234e0 bytes c2560910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e031684ea6509652570fb75dc5459391"></a>

### [`00c231b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c231b0.md) → [`00c235d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c235d8.md) FUN_00c235d8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c235fc",
      "incomplete_value": true,
      "site": "00c23600",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c231d4",
      "incomplete_value": true,
      "site": "00c231d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c23608",
      "incomplete_value": true,
      "site": "00c2360c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c231e0",
      "incomplete_value": true,
      "site": "00c231e4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23630",
      "incomplete_value": true,
      "site": "00c23634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23208",
      "incomplete_value": true,
      "site": "00c2320c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
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
      "00c235fc",
      "READ",
      [
        "storage",
        "00c9b8b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23600",
      "DATA",
      [
        "storage",
        "01127848",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23604",
      "READ",
      [
        "storage",
        "01127848",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c235fc",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23600",
      "DATA",
      [
        "storage",
        "01127c48",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23604",
      "READ",
      [
        "storage",
        "01127c48",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2320c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c231b0.md#insn-00c2320c) · [`00c231d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c231b0.md#insn-00c231d4) · [`00c231fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c231b0.md#insn-00c231fc)
- 新版 `00c23634`（命令位置の公開資料なし） · `00c235fc`（命令位置の公開資料なし） · `00c23624`（命令位置の公開資料なし）

~~~diff
- 00c2320c ["INT_ADD", "register:40f0:8", ["const:c2320c:8", "const:4:8"]]
- 00c2320c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c23634 ["INT_ADD", "register:40f0:8", ["const:c23634:8", "const:4:8"]]
+ 00c23634 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c2320c bytes 35ea0094
+ 00c23634 bytes 2bea0094
- 00c231d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00c231d4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c235fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
+ 00c235fc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c231d4 bytes 945e44f9
+ 00c235fc bytes 945e46f9
- 00c231fc ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c23624 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c231fc bytes a24c0910
+ 00c23624 bytes a24c0910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cc86f5f123dcf1e7a7fcd68b285392d"></a>

### [`00c232f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c232f4.md) → [`00c2371c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c2371c.md) FUN_00c2371c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23740",
      "incomplete_value": true,
      "site": "00c23744",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23318",
      "incomplete_value": true,
      "site": "00c2331c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c2374c",
      "incomplete_value": true,
      "site": "00c23750",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23324",
      "incomplete_value": true,
      "site": "00c23328",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23774",
      "incomplete_value": true,
      "site": "00c23778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2334c",
      "incomplete_value": true,
      "site": "00c23350",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c8:8"
              ]
            ]
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
      "00c23740",
      "READ",
      [
        "storage",
        "00c9b8c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23744",
      "DATA",
      [
        "storage",
        "01127858",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23748",
      "READ",
      [
        "storage",
        "01127858",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23740",
      "READ",
      [
        "storage",
        "00c9bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23744",
      "DATA",
      [
        "storage",
        "01127c58",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23748",
      "READ",
      [
        "storage",
        "01127c58",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c232f4.md#insn-00c23350) · [`00c23318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c232f4.md#insn-00c23318) · [`00c23340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c232f4.md#insn-00c23340)
- 新版 `00c23778`（命令位置の公開資料なし） · `00c23740`（命令位置の公開資料なし） · `00c23768`（命令位置の公開資料なし）

~~~diff
- 00c23350 ["INT_ADD", "register:40f0:8", ["const:c23350:8", "const:4:8"]]
- 00c23350 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c23778 ["INT_ADD", "register:40f0:8", ["const:c23778:8", "const:4:8"]]
+ 00c23778 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c23350 bytes e4e90094
+ 00c23778 bytes dae90094
- 00c23318 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00c23318 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23740 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc8:8"]]
+ 00c23740 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23318 bytes 946644f9
+ 00c23740 bytes 946646f9
- 00c23340 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c23768 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c23340 bytes 82420910
+ 00c23768 bytes 82420910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e546c7dfa4a097959249c624fe54a7e5"></a>

### [`00c23438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23438.md) → [`00c23860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c23860.md) FUN_00c23860

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23884",
      "incomplete_value": true,
      "site": "00c23888",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2345c",
      "incomplete_value": true,
      "site": "00c23460",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c23890",
      "incomplete_value": true,
      "site": "00c23894",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23468",
      "incomplete_value": true,
      "site": "00c2346c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c238b8",
      "incomplete_value": true,
      "site": "00c238bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23490",
      "incomplete_value": true,
      "site": "00c23494",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8d8:8"
              ]
            ]
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
      "00c23884",
      "READ",
      [
        "storage",
        "00c9b8d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23888",
      "DATA",
      [
        "storage",
        "01127868",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2388c",
      "READ",
      [
        "storage",
        "01127868",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23884",
      "READ",
      [
        "storage",
        "00c9bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23888",
      "DATA",
      [
        "storage",
        "01127c68",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c2388c",
      "READ",
      [
        "storage",
        "01127c68",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23438.md#insn-00c23494) · [`00c2345c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23438.md#insn-00c2345c) · [`00c23484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23438.md#insn-00c23484)
- 新版 `00c238bc`（命令位置の公開資料なし） · `00c23884`（命令位置の公開資料なし） · `00c238ac`（命令位置の公開資料なし）

~~~diff
- 00c23494 ["INT_ADD", "register:40f0:8", ["const:c23494:8", "const:4:8"]]
- 00c23494 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c238bc ["INT_ADD", "register:40f0:8", ["const:c238bc:8", "const:4:8"]]
+ 00c238bc ["CALL", null, ["callee:00c5dee0:8"]]
- 00c23494 bytes 93e90094
+ 00c238bc bytes 89e90094
- 00c2345c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d8:8"]]
- 00c2345c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23884 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd8:8"]]
+ 00c23884 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2345c bytes 946e44f9
+ 00c23884 bytes 946e46f9
- 00c23484 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c238ac ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c23484 bytes 62380910
+ 00c238ac bytes 62380910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e84338e545e821e722a274a8d1278507"></a>

### [`00c2357c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c2357c.md) → [`00c239a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c239a4.md) FUN_00c239a4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c239c8",
      "incomplete_value": true,
      "site": "00c239cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c235a0",
      "incomplete_value": true,
      "site": "00c235a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c239fc",
      "incomplete_value": true,
      "site": "00c23a00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c235d4",
      "incomplete_value": true,
      "site": "00c235d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b8:8"
              ]
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
      "definition_site": "00c239f0",
      "incomplete_value": false,
      "site": "00c23a00",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c235c8",
      "incomplete_value": false,
      "site": "00c235d8",
      "value": [
        "leaf",
        "const:c35b90:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c239c8",
      "READ",
      [
        "storage",
        "00c9b7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c239cc",
      "DATA",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c239d0",
      "READ",
      [
        "storage",
        "01127a88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c239c8",
      "READ",
      [
        "storage",
        "00c9bbb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c239cc",
      "DATA",
      [
        "storage",
        "01127e88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c239d0",
      "READ",
      [
        "storage",
        "01127e88",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c235d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c2357c.md#insn-00c235d8) · [`00c235a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c2357c.md#insn-00c235a0) · [`00c235c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c2357c.md#insn-00c235c8)
- 新版 `00c23a00`（命令位置の公開資料なし） · `00c239c8`（命令位置の公開資料なし） · `00c239f0`（命令位置の公開資料なし）

~~~diff
- 00c235d8 ["INT_ADD", "register:40f0:8", ["const:c235d8:8", "const:4:8"]]
- 00c235d8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c23a00 ["INT_ADD", "register:40f0:8", ["const:c23a00:8", "const:4:8"]]
+ 00c23a00 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c235d8 bytes 42e90094
+ 00c23a00 bytes 38e90094
- 00c235a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
- 00c235a0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c239c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bb8:8"]]
+ 00c239c8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c235a0 bytes 94de43f9
+ 00c239c8 bytes 94de45f9
- 00c235c8 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c239f0 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c235c8 bytes 422e0910
+ 00c239f0 bytes 422e0910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-423eb097948990ae3d474ea034e47f49"></a>

### [`00c236c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c236c0.md) → [`00c23ae8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c23ae8.md) FUN_00c23ae8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23b0c",
      "incomplete_value": true,
      "site": "00c23b10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c236e4",
      "incomplete_value": true,
      "site": "00c236e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c23b18",
      "incomplete_value": true,
      "site": "00c23b1c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c236f0",
      "incomplete_value": true,
      "site": "00c236f4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23b40",
      "incomplete_value": true,
      "site": "00c23b44",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
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
    "old": {
      "definition_site": "00c23718",
      "incomplete_value": true,
      "site": "00c2371c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
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
      "00c23b0c",
      "READ",
      [
        "storage",
        "00c9b7c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23b10",
      "DATA",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23b14",
      "READ",
      [
        "storage",
        "01127a98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23b0c",
      "READ",
      [
        "storage",
        "00c9bbc8",
        null,
        "pointer"
      ]
    ],
    [
      "00c23b10",
      "DATA",
      [
        "storage",
        "01127e98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23b14",
      "READ",
      [
        "storage",
        "01127e98",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2371c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c236c0.md#insn-00c2371c) · [`00c236e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c236c0.md#insn-00c236e4) · [`00c2370c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c236c0.md#insn-00c2370c)
- 新版 `00c23b44`（命令位置の公開資料なし） · `00c23b0c`（命令位置の公開資料なし） · `00c23b34`（命令位置の公開資料なし）

~~~diff
- 00c2371c ["INT_ADD", "register:40f0:8", ["const:c2371c:8", "const:4:8"]]
- 00c2371c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c23b44 ["INT_ADD", "register:40f0:8", ["const:c23b44:8", "const:4:8"]]
+ 00c23b44 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c2371c bytes f1e80094
+ 00c23b44 bytes e7e80094
- 00c236e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c8:8"]]
- 00c236e4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23b0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bc8:8"]]
+ 00c23b0c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c236e4 bytes 94e643f9
+ 00c23b0c bytes 94e645f9
- 00c2370c ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c23b34 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c2370c bytes 22240910
+ 00c23b34 bytes 22240910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-234f535704169a5cee4d8e24f0306acd"></a>

### [`00c23804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23804.md) → [`00c23c2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c23c2c.md) FUN_00c23c2c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23c50",
      "incomplete_value": true,
      "site": "00c23c54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c23828",
      "incomplete_value": true,
      "site": "00c2382c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c23c84",
      "incomplete_value": true,
      "site": "00c23c88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00c2385c",
      "incomplete_value": true,
      "site": "00c23860",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c23c78",
      "incomplete_value": false,
      "site": "00c23c88",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c23850",
      "incomplete_value": false,
      "site": "00c23860",
      "value": [
        "leaf",
        "const:c35b90:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c23c50",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00c23c54",
      "DATA",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23c58",
      "READ",
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
      "00c23c50",
      "READ",
      [
        "storage",
        "00c9bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00c23c54",
      "DATA",
      [
        "storage",
        "01127b78",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23c58",
      "READ",
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

- 旧版 [`00c23860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23804.md#insn-00c23860) · [`00c23828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23804.md#insn-00c23828) · [`00c23850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23804.md#insn-00c23850)
- 新版 `00c23c88`（命令位置の公開資料なし） · `00c23c50`（命令位置の公開資料なし） · `00c23c78`（命令位置の公開資料なし）

~~~diff
- 00c23860 ["INT_ADD", "register:40f0:8", ["const:c23860:8", "const:4:8"]]
- 00c23860 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c23c88 ["INT_ADD", "register:40f0:8", ["const:c23c88:8", "const:4:8"]]
+ 00c23c88 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c23860 bytes a0e80094
+ 00c23c88 bytes 96e80094
- 00c23828 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
- 00c23828 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23c50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
+ 00c23c50 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23828 bytes 948a43f9
+ 00c23c50 bytes 948a45f9
- 00c23850 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c23c78 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c23850 bytes 021a0910
+ 00c23c78 bytes 021a0910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a77a901a7360ecd546d29e0becfb69f4"></a>

### [`00c23948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23948.md) → [`00c23d70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c23d70.md) FUN_00c23d70

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23d94",
      "incomplete_value": true,
      "site": "00c23d98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2396c",
      "incomplete_value": true,
      "site": "00c23970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c23da0",
      "incomplete_value": true,
      "site": "00c23da4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23978",
      "incomplete_value": true,
      "site": "00c2397c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23dc8",
      "incomplete_value": true,
      "site": "00c23dcc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c239a0",
      "incomplete_value": true,
      "site": "00c239a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:748:8"
              ]
            ]
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
      "00c23d94",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c23d98",
      "DATA",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23d9c",
      "READ",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23d94",
      "READ",
      [
        "storage",
        "00c9bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00c23d98",
      "DATA",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23d9c",
      "READ",
      [
        "storage",
        "01127b88",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c239a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23948.md#insn-00c239a4) · [`00c2396c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23948.md#insn-00c2396c) · [`00c23994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23948.md#insn-00c23994)
- 新版 `00c23dcc`（命令位置の公開資料なし） · `00c23d94`（命令位置の公開資料なし） · `00c23dbc`（命令位置の公開資料なし）

~~~diff
- 00c239a4 ["INT_ADD", "register:40f0:8", ["const:c239a4:8", "const:4:8"]]
- 00c239a4 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c23dcc ["INT_ADD", "register:40f0:8", ["const:c23dcc:8", "const:4:8"]]
+ 00c23dcc ["CALL", null, ["callee:00c5dee0:8"]]
- 00c239a4 bytes 4fe80094
+ 00c23dcc bytes 45e80094
- 00c2396c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:748:8"]]
- 00c2396c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23d94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b48:8"]]
+ 00c23d94 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2396c bytes 94a643f9
+ 00c23d94 bytes 94a645f9
- 00c23994 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c23dbc ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c23994 bytes e20f0910
+ 00c23dbc bytes e20f0910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d87483af5db8553d10cfc7b2012af7ab"></a>

### [`00c23a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23a8c.md) → [`00c23eb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c23eb4.md) FUN_00c23eb4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c23ed8",
      "incomplete_value": true,
      "site": "00c23edc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23ab0",
      "incomplete_value": true,
      "site": "00c23ab4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:438:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c23ee4",
      "incomplete_value": true,
      "site": "00c23ee8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23abc",
      "incomplete_value": true,
      "site": "00c23ac0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23f0c",
      "incomplete_value": true,
      "site": "00c23f10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:838:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23ae4",
      "incomplete_value": true,
      "site": "00c23ae8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:438:8"
              ]
            ]
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
      "00c23ed8",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00c23edc",
      "DATA",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23ee0",
      "READ",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c23ed8",
      "READ",
      [
        "storage",
        "00c9b838",
        null,
        "pointer"
      ]
    ],
    [
      "00c23edc",
      "DATA",
      [
        "storage",
        "01127b98",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c23ee0",
      "READ",
      [
        "storage",
        "01127b98",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23a8c.md#insn-00c23ae8) · [`00c23ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23a8c.md#insn-00c23ab0) · [`00c23ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23a8c.md#insn-00c23ad8)
- 新版 `00c23f10`（命令位置の公開資料なし） · `00c23ed8`（命令位置の公開資料なし） · `00c23f00`（命令位置の公開資料なし）

~~~diff
- 00c23ae8 ["INT_ADD", "register:40f0:8", ["const:c23ae8:8", "const:4:8"]]
- 00c23ae8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c23f10 ["INT_ADD", "register:40f0:8", ["const:c23f10:8", "const:4:8"]]
+ 00c23f10 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c23ae8 bytes fee70094
+ 00c23f10 bytes f4e70094
- 00c23ab0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
- 00c23ab0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c23ed8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:838:8"]]
+ 00c23ed8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23ab0 bytes 941e42f9
+ 00c23ed8 bytes 941e44f9
- 00c23ad8 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c23f00 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c23ad8 bytes c2050910
+ 00c23f00 bytes c2050910
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a34e6c2a3d775cc0e12ee03fd760b999"></a>

### [`00c23bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23bd0.md) → [`00c23ff8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c23/00c23ff8.md) FUN_00c23ff8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2401c",
      "incomplete_value": true,
      "site": "00c24020",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23bf4",
      "incomplete_value": true,
      "site": "00c23bf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:758:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c24028",
      "incomplete_value": true,
      "site": "00c2402c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23c00",
      "incomplete_value": true,
      "site": "00c23c04",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c24050",
      "incomplete_value": true,
      "site": "00c24054",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23c28",
      "incomplete_value": true,
      "site": "00c23c2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:758:8"
              ]
            ]
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
      "00c2401c",
      "READ",
      [
        "storage",
        "00c9b758",
        null,
        "pointer"
      ]
    ],
    [
      "00c24020",
      "DATA",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24024",
      "READ",
      [
        "storage",
        "011277a8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c2401c",
      "READ",
      [
        "storage",
        "00c9bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00c24020",
      "DATA",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24024",
      "READ",
      [
        "storage",
        "01127ba8",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23bd0.md#insn-00c23c2c) · [`00c23bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23bd0.md#insn-00c23bf4) · [`00c23c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23bd0.md#insn-00c23c1c)
- 新版 `00c24054`（命令位置の公開資料なし） · `00c2401c`（命令位置の公開資料なし） · `00c24044`（命令位置の公開資料なし）

~~~diff
- 00c23c2c ["INT_ADD", "register:40f0:8", ["const:c23c2c:8", "const:4:8"]]
- 00c23c2c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c24054 ["INT_ADD", "register:40f0:8", ["const:c24054:8", "const:4:8"]]
+ 00c24054 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c23c2c bytes ade70094
+ 00c24054 bytes a3e70094
- 00c23bf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
- 00c23bf4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2401c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b58:8"]]
+ 00c2401c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23bf4 bytes 94ae43f9
+ 00c2401c bytes 94ae45f9
- 00c23c1c ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c24044 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c23c1c bytes a2fb0810
+ 00c24044 bytes a2fb0810
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb192b41367c7fe5a56e5aada2868109"></a>

### [`00c23d14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23d14.md) → [`00c2413c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c2413c.md) FUN_00c2413c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24160",
      "incomplete_value": true,
      "site": "00c24164",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23d38",
      "incomplete_value": true,
      "site": "00c23d3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c2416c",
      "incomplete_value": true,
      "site": "00c24170",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23d44",
      "incomplete_value": true,
      "site": "00c23d48",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c24194",
      "incomplete_value": true,
      "site": "00c24198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23d6c",
      "incomplete_value": true,
      "site": "00c23d70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
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
      "00c24160",
      "READ",
      [
        "storage",
        "00c9aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00c24164",
      "DATA",
      [
        "storage",
        "011277b8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24168",
      "READ",
      [
        "storage",
        "011277b8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c24160",
      "READ",
      [
        "storage",
        "00c9b2f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c24164",
      "DATA",
      [
        "storage",
        "01127bb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24168",
      "READ",
      [
        "storage",
        "01127bb8",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23d14.md#insn-00c23d70) · [`00c23d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23d14.md#insn-00c23d2c) · [`00c23d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23d14.md#insn-00c23d38)
- 新版 `00c24198`（命令位置の公開資料なし） · `00c24154`（命令位置の公開資料なし） · `00c24160`（命令位置の公開資料なし）

~~~diff
- 00c23d70 ["INT_ADD", "register:40f0:8", ["const:c23d70:8", "const:4:8"]]
- 00c23d70 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c24198 ["INT_ADD", "register:40f0:8", ["const:c24198:8", "const:4:8"]]
+ 00c24198 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c23d70 bytes 5ce70094
+ 00c24198 bytes 52e70094
- 00c23d2c ["COPY", "register:40a0:8", ["const:c9a000:8"]]
+ 00c24154 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00c23d2c bytes b40300f0
+ 00c24154 bytes b40300f0
- 00c23d38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ef0:8"]]
- 00c23d38 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c24160 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
+ 00c24160 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23d38 bytes 947a47f9
+ 00c24160 bytes 947a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-728bf67968b8b9a7286ce661b62d4762"></a>

### [`00c23e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23e58.md) → [`00c24280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24280.md) FUN_00c24280

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c242a4",
      "incomplete_value": true,
      "site": "00c242a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23e7c",
      "incomplete_value": true,
      "site": "00c23e80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c242b0",
      "incomplete_value": true,
      "site": "00c242b4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23e88",
      "incomplete_value": true,
      "site": "00c23e8c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c242d8",
      "incomplete_value": true,
      "site": "00c242dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23eb0",
      "incomplete_value": true,
      "site": "00c23eb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f0:8"
              ]
            ]
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
      "00c242a4",
      "READ",
      [
        "storage",
        "00c9b8f0",
        null,
        "pointer"
      ]
    ],
    [
      "00c242a8",
      "DATA",
      [
        "storage",
        "011277c8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c242ac",
      "READ",
      [
        "storage",
        "011277c8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c242a4",
      "READ",
      [
        "storage",
        "00c9bcf0",
        null,
        "pointer"
      ]
    ],
    [
      "00c242a8",
      "DATA",
      [
        "storage",
        "01127bc8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c242ac",
      "READ",
      [
        "storage",
        "01127bc8",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23e58.md#insn-00c23eb4) · [`00c23e7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23e58.md#insn-00c23e7c) · [`00c23ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23e58.md#insn-00c23ea4)
- 新版 `00c242dc`（命令位置の公開資料なし） · `00c242a4`（命令位置の公開資料なし） · `00c242cc`（命令位置の公開資料なし）

~~~diff
- 00c23eb4 ["INT_ADD", "register:40f0:8", ["const:c23eb4:8", "const:4:8"]]
- 00c23eb4 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c242dc ["INT_ADD", "register:40f0:8", ["const:c242dc:8", "const:4:8"]]
+ 00c242dc ["CALL", null, ["callee:00c5dee0:8"]]
- 00c23eb4 bytes 0be70094
+ 00c242dc bytes 01e70094
- 00c23e7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
- 00c23e7c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c242a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf0:8"]]
+ 00c242a4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23e7c bytes 947a44f9
+ 00c242a4 bytes 947a46f9
- 00c23ea4 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c242cc ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c23ea4 bytes 62e70810
+ 00c242cc bytes 62e70810
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-152d7bf999f875cb27e6e7e2fbcc8205"></a>

### [`00c23f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23f9c.md) → [`00c243c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c243c4.md) FUN_00c243c4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c243e8",
      "incomplete_value": true,
      "site": "00c243ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23fc0",
      "incomplete_value": true,
      "site": "00c23fc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c243f4",
      "incomplete_value": true,
      "site": "00c243f8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c23fcc",
      "incomplete_value": true,
      "site": "00c23fd0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c2441c",
      "incomplete_value": true,
      "site": "00c24420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c23ff4",
      "incomplete_value": true,
      "site": "00c23ff8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
              ]
            ]
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
      "00c243e8",
      "READ",
      [
        "storage",
        "00c9aef8",
        null,
        "pointer"
      ]
    ],
    [
      "00c243ec",
      "DATA",
      [
        "storage",
        "011277d8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c243f0",
      "READ",
      [
        "storage",
        "011277d8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c243e8",
      "READ",
      [
        "storage",
        "00c9b2f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c243ec",
      "DATA",
      [
        "storage",
        "01127bd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c243f0",
      "READ",
      [
        "storage",
        "01127bd8",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c23ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23f9c.md#insn-00c23ff8) · [`00c23fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23f9c.md#insn-00c23fb4) · [`00c23fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c23/00c23f9c.md#insn-00c23fc0)
- 新版 `00c24420`（命令位置の公開資料なし） · `00c243dc`（命令位置の公開資料なし） · `00c243e8`（命令位置の公開資料なし）

~~~diff
- 00c23ff8 ["INT_ADD", "register:40f0:8", ["const:c23ff8:8", "const:4:8"]]
- 00c23ff8 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c24420 ["INT_ADD", "register:40f0:8", ["const:c24420:8", "const:4:8"]]
+ 00c24420 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c23ff8 bytes bae60094
+ 00c24420 bytes b0e60094
- 00c23fb4 ["COPY", "register:40a0:8", ["const:c9a000:8"]]
+ 00c243dc ["COPY", "register:40a0:8", ["const:c9b000:8"]]
- 00c23fb4 bytes b40300f0
+ 00c243dc bytes b40300f0
- 00c23fc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ef8:8"]]
- 00c23fc0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c243e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
+ 00c243e8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c23fc0 bytes 947e47f9
+ 00c243e8 bytes 947e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-062fe0c03b473a32e6457d760ce10554"></a>

### [`00c240e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c240e0.md) → [`00c24508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24508.md) FUN_00c24508

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2452c",
      "incomplete_value": true,
      "site": "00c24530",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24104",
      "incomplete_value": true,
      "site": "00c24108",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c24538",
      "incomplete_value": true,
      "site": "00c2453c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c24110",
      "incomplete_value": true,
      "site": "00c24114",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c24560",
      "incomplete_value": true,
      "site": "00c24564",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24138",
      "incomplete_value": true,
      "site": "00c2413c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
              ]
            ]
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
      "00c2452c",
      "READ",
      [
        "storage",
        "00c9b910",
        null,
        "pointer"
      ]
    ],
    [
      "00c24530",
      "DATA",
      [
        "storage",
        "011277e8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24534",
      "READ",
      [
        "storage",
        "011277e8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c2452c",
      "READ",
      [
        "storage",
        "00c9bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00c24530",
      "DATA",
      [
        "storage",
        "01127be8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24534",
      "READ",
      [
        "storage",
        "01127be8",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2413c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c240e0.md#insn-00c2413c) · [`00c24104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c240e0.md#insn-00c24104) · [`00c2412c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c240e0.md#insn-00c2412c)
- 新版 `00c24564`（命令位置の公開資料なし） · `00c2452c`（命令位置の公開資料なし） · `00c24554`（命令位置の公開資料なし）

~~~diff
- 00c2413c ["INT_ADD", "register:40f0:8", ["const:c2413c:8", "const:4:8"]]
- 00c2413c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c24564 ["INT_ADD", "register:40f0:8", ["const:c24564:8", "const:4:8"]]
+ 00c24564 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c2413c bytes 69e60094
+ 00c24564 bytes 5fe60094
- 00c24104 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00c24104 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2452c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
+ 00c2452c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c24104 bytes 948a44f9
+ 00c2452c bytes 948a46f9
- 00c2412c ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c24554 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c2412c bytes 22d30810
+ 00c24554 bytes 22d30810
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a34222f352583ac8013548c587a36124"></a>

### [`00c24224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24224.md) → [`00c2464c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c2464c.md) FUN_00c2464c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24670",
      "incomplete_value": true,
      "site": "00c24674",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24248",
      "incomplete_value": true,
      "site": "00c2424c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c2467c",
      "incomplete_value": true,
      "site": "00c24680",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c24254",
      "incomplete_value": true,
      "site": "00c24258",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00c246a4",
      "incomplete_value": true,
      "site": "00c246a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2427c",
      "incomplete_value": true,
      "site": "00c24280",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
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
      "00c24670",
      "READ",
      [
        "storage",
        "00c9b920",
        null,
        "pointer"
      ]
    ],
    [
      "00c24674",
      "DATA",
      [
        "storage",
        "01127878",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24678",
      "READ",
      [
        "storage",
        "01127878",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c24670",
      "READ",
      [
        "storage",
        "00c9bd20",
        null,
        "pointer"
      ]
    ],
    [
      "00c24674",
      "DATA",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00c24678",
      "READ",
      [
        "storage",
        "01127c78",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24224.md#insn-00c24280) · [`00c24248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24224.md#insn-00c24248) · [`00c24270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24224.md#insn-00c24270)
- 新版 `00c246a8`（命令位置の公開資料なし） · `00c24670`（命令位置の公開資料なし） · `00c24698`（命令位置の公開資料なし）

~~~diff
- 00c24280 ["INT_ADD", "register:40f0:8", ["const:c24280:8", "const:4:8"]]
- 00c24280 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c246a8 ["INT_ADD", "register:40f0:8", ["const:c246a8:8", "const:4:8"]]
+ 00c246a8 ["CALL", null, ["callee:00c5dee0:8"]]
- 00c24280 bytes 18e60094
+ 00c246a8 bytes 0ee60094
- 00c24248 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00c24248 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c24670 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d20:8"]]
+ 00c24670 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c24248 bytes 949244f9
+ 00c24670 bytes 949246f9
- 00c24270 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c24698 ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c24270 bytes 02c90810
+ 00c24698 bytes 02c90810
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e85668222404d858d5af76423898e4cf"></a>

### [`00c24368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24368.md) → [`00c24790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24790.md) FUN_00c24790

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 6件 [`00c05b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c05/00c05b30.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c35b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35b90.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c21f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21f78.md) · 呼出先 6件 [`00c05f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05f58.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c35fb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35fb8.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c247b4",
      "incomplete_value": true,
      "site": "00c247b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2438c",
      "incomplete_value": true,
      "site": "00c24390",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40a0:8"
              ],
              [
                "leaf",
                "const:930:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c247e8",
      "incomplete_value": true,
      "site": "00c247ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c243c0",
      "incomplete_value": true,
      "site": "00c243c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
              ]
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
      "definition_site": "00c247dc",
      "incomplete_value": false,
      "site": "00c247ec",
      "value": [
        "leaf",
        "const:c35fb8:8"
      ]
    },
    "old": {
      "definition_site": "00c243b4",
      "incomplete_value": false,
      "site": "00c243c4",
      "value": [
        "leaf",
        "const:c35b90:8"
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c247b4",
      "READ",
      [
        "storage",
        "00c9b930",
        null,
        "pointer"
      ]
    ],
    [
      "00c247b8",
      "DATA",
      [
        "storage",
        "01127888",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c247bc",
      "READ",
      [
        "storage",
        "01127888",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c247b4",
      "READ",
      [
        "storage",
        "00c9bd30",
        null,
        "pointer"
      ]
    ],
    [
      "00c247b8",
      "DATA",
      [
        "storage",
        "01127c88",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00c247bc",
      "READ",
      [
        "storage",
        "01127c88",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c243c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24368.md#insn-00c243c4) · [`00c2438c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24368.md#insn-00c2438c) · [`00c243b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24368.md#insn-00c243b4)
- 新版 `00c247ec`（命令位置の公開資料なし） · `00c247b4`（命令位置の公開資料なし） · `00c247dc`（命令位置の公開資料なし）

~~~diff
- 00c243c4 ["INT_ADD", "register:40f0:8", ["const:c243c4:8", "const:4:8"]]
- 00c243c4 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00c247ec ["INT_ADD", "register:40f0:8", ["const:c247ec:8", "const:4:8"]]
+ 00c247ec ["CALL", null, ["callee:00c5dee0:8"]]
- 00c243c4 bytes c7e50094
+ 00c247ec bytes bde50094
- 00c2438c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
- 00c2438c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c247b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d30:8"]]
+ 00c247b4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2438c bytes 949a44f9
+ 00c247b4 bytes 949a46f9
- 00c243b4 ["COPY", "register:4010:8", ["const:c35b90:8"]]
+ 00c247dc ["COPY", "register:4010:8", ["const:c35fb8:8"]]
- 00c243b4 bytes e2be0810
+ 00c247dc bytes e2be0810
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8bba984d0db67c393374af451a7b0c2"></a>

### [`00c244ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c244ac.md) → [`00c248d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c248d4.md) FUN_00c248d4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c24ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ee8.md) · 呼出先 10件 [`00c354a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354a8.md) [`00c354c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354c0.md) [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c25310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25310.md) · 呼出先 10件 [`00c358d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358d0.md) [`00c358e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c358e8.md) [`00c35a44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c35/00c35a44.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24904",
      "incomplete_value": false,
      "site": "00c24904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c244dc",
      "incomplete_value": false,
      "site": "00c244dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "00c24904",
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c24904",
      "DATA",
      [
        "storage",
        "00c936c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c244d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c244ac.md#insn-00c244d4) · [`00c244d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c244ac.md#insn-00c244d8) · [`00c24540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c244ac.md#insn-00c24540)
- 新版 `00c248fc`（命令位置の公開資料なし） · `00c24968`（命令位置の公開資料なし）

~~~diff
- 00c244d4 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00c244d4 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00c244d4 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00c244d4 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00c248fc ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00c248fc ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00c248fc ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00c248fc ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00c244d4 bytes 6b010b91
+ 00c248fc bytes 6b011b91
- 00c244d8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00c244d8 bytes f30300aa
- 00c24540 ["INT_ADD", "register:40f0:8", ["const:c24540:8", "const:4:8"]]
- 00c24540 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c24968 ["INT_ADD", "register:40f0:8", ["const:c24968:8", "const:4:8"]]
+ 00c24968 ["CALL", null, ["callee:00c57e90:8"]]
- 00c24540 bytes 54cd0094
+ 00c24968 bytes 4acd0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-520621447f82d5aed40b36ecd6e032af"></a>

### [`00c24780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24780.md) → [`00c24ba8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24ba8.md) FUN_00c24ba8

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c24854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24854.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 1件 [`00c24c7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24c7c.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24bc8",
      "incomplete_value": false,
      "site": "00c24bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c247a0",
      "incomplete_value": false,
      "site": "00c247a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c93000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "00c24bd0",
      "DATA",
      [
        "storage",
        "00c932c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c24bd0",
      "DATA",
      [
        "storage",
        "00c936c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c247a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24780.md#insn-00c247a0) · [`00c247ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24780.md#insn-00c247ec) · [`00c24800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24780.md#insn-00c24800)
- 新版 `00c24bc8`（命令位置の公開資料なし） · `00c24c14`（命令位置の公開資料なし） · `00c24c28`（命令位置の公開資料なし）

~~~diff
- 00c247a0 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 00c247a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c247a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c247a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c24bc8 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00c24bc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c24bc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c24bc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c247a0 bytes 08010b91
+ 00c24bc8 bytes 08011b91
- 00c247ec ["INT_ADD", "register:40f0:8", ["const:c247ec:8", "const:4:8"]]
- 00c247ec ["CALL", null, ["callee:00c53d00:8"]]
+ 00c24c14 ["INT_ADD", "register:40f0:8", ["const:c24c14:8", "const:4:8"]]
+ 00c24c14 ["CALL", null, ["callee:00c53d00:8"]]
- 00c247ec bytes 3dbc0094
+ 00c24c14 bytes 3bbc0094
- 00c24800 ["COPY", "register:0:8", ["register:4040:8"]]
- 00c24800 ["INT_ADD", "register:40f0:8", ["const:c24800:8", "const:4:8"]]
- 00c24800 ["CALLIND", null, ["register:0:8"]]
+ 00c24c28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c24c28 ["INT_ADD", "register:40f0:8", ["const:c24c28:8", "const:4:8"]]
+ 00c24c28 ["CALLIND", null, ["register:0:8"]]
- 00c24800 bytes 00013fd6
+ 00c24c28 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64ec59561e3fc94d556f87112a9ffc09"></a>

### [`00c24880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24880.md) → [`00c24ca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24ca8.md) _ZNSt6__ndk16locale8__globalEv

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5e4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c24cfc",
      "incomplete_value": false,
      "site": "00c24d00",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c248d4",
      "incomplete_value": false,
      "site": "00c248d8",
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
            "const:9f0:8"
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
      "definition_site": "00c24d08",
      "incomplete_value": false,
      "site": "00c24d0c",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c248e0",
      "incomplete_value": false,
      "site": "00c248e4",
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
            "const:9f8:8"
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
      "00c24cc0",
      "READ",
      [
        "storage",
        "011279f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c24ccc",
      "DATA",
      [
        "storage",
        "011279f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c24ce4",
      "PARAM",
      [
        "storage",
        "011279f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c24cc0",
      "READ",
      [
        "storage",
        "01127df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c24ccc",
      "DATA",
      [
        "storage",
        "01127df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c24ce4",
      "PARAM",
      [
        "storage",
        "01127df8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c248d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24880.md#insn-00c248d8) · [`00c248e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24880.md#insn-00c248e4) · [`00c24894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24880.md#insn-00c24894)
- 新版 `00c24d00`（命令位置の公開資料なし） · `00c24d0c`（命令位置の公開資料なし） · `00c24cbc`（命令位置の公開資料なし）

~~~diff
- 00c248d8 ["INT_ADD", "register:40f0:8", ["const:c248d8:8", "const:4:8"]]
- 00c248d8 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00c24d00 ["INT_ADD", "register:40f0:8", ["const:c24d00:8", "const:4:8"]]
+ 00c24d00 ["CALL", null, ["callee:00c5a7d0:8"]]
- 00c248d8 bytes bed60094
+ 00c24d00 bytes b4d60094
- 00c248e4 ["INT_ADD", "register:40f0:8", ["const:c248e4:8", "const:4:8"]]
- 00c248e4 ["CALL", null, ["callee:00c57e70:8"]]
+ 00c24d0c ["INT_ADD", "register:40f0:8", ["const:c24d0c:8", "const:4:8"]]
+ 00c24d0c ["CALL", null, ["callee:00c57e70:8"]]
- 00c248e4 bytes 63cc0094
+ 00c24d0c bytes 59cc0094
- 00c24894 ["COPY", "tmp:0:8", ["const:9f8:8"]]
- 00c24894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c24894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c24894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c24cbc ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 00c24cbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c24cbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c24cbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c24894 bytes 08e12791
+ 00c24cbc bytes 08e13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0236e0d2fbfdf6a7771a9778eafc24a9"></a>

### [`00c24904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24904.md) → [`00c24d2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24d2c.md) _ZNSt6__ndk16localeC2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md) · 呼出先 5件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5e4c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4c0.md)
- 新版 呼出元 1件 [`00c5a7a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7a0.md) · 呼出先 5件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) [`00c5e8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e8c0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 63.89% / 新版 63.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c24d5c",
      "incomplete_value": true,
      "site": "00c24d64",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
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
      "definition_site": "00c24934",
      "incomplete_value": true,
      "site": "00c2493c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1127000:8"
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c24d60",
      "incomplete_value": true,
      "site": "00c24d68",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00c24938",
      "incomplete_value": true,
      "site": "00c24940",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c24d8c",
      "incomplete_value": false,
      "site": "00c24d90",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24964",
      "incomplete_value": false,
      "site": "00c24968",
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
            "const:9f8:8"
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
      "00c24d48",
      "READ",
      [
        "storage",
        "011279f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c24d5c",
      "READ",
      [
        "storage",
        "011279f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c24d8c",
      "PARAM",
      [
        "storage",
        "011279f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c24d48",
      "READ",
      [
        "storage",
        "01127df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c24d5c",
      "READ",
      [
        "storage",
        "01127df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c24d8c",
      "PARAM",
      [
        "storage",
        "01127df8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24904.md#insn-00c24968) · [`00c24980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24904.md#insn-00c24980) · [`00c2498c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24904.md#insn-00c2498c)
- 新版 `00c24d90`（命令位置の公開資料なし） · `00c24da8`（命令位置の公開資料なし） · `00c24db4`（命令位置の公開資料なし）

~~~diff
- 00c24968 ["INT_ADD", "register:40f0:8", ["const:c24968:8", "const:4:8"]]
- 00c24968 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c24d90 ["INT_ADD", "register:40f0:8", ["const:c24d90:8", "const:4:8"]]
+ 00c24d90 ["CALL", null, ["callee:00c57e50:8"]]
- 00c24968 bytes 3acc0094
+ 00c24d90 bytes 30cc0094
- 00c24980 ["INT_ADD", "register:40f0:8", ["const:c24980:8", "const:4:8"]]
- 00c24980 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00c24da8 ["INT_ADD", "register:40f0:8", ["const:c24da8:8", "const:4:8"]]
+ 00c24da8 ["CALL", null, ["callee:00c5a7d0:8"]]
- 00c24980 bytes 94d60094
+ 00c24da8 bytes 8ad60094
- 00c2498c ["INT_ADD", "register:40f0:8", ["const:c2498c:8", "const:4:8"]]
- 00c2498c ["CALL", null, ["callee:00c57e70:8"]]
+ 00c24db4 ["INT_ADD", "register:40f0:8", ["const:c24db4:8", "const:4:8"]]
+ 00c24db4 ["CALL", null, ["callee:00c57e70:8"]]
- 00c2498c bytes 39cc0094
+ 00c24db4 bytes 2fcc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddc75dd2e83d27022b836b1420cd36c4"></a>

### [`00c249ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c249ac.md) → [`00c24dd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24dd4.md) _ZNSt6__ndk16localeC1ERKS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)
- 新版 呼出元 1件 [`00c5a7d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a7d0.md) · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c24de4",
      "incomplete_value": true,
      "site": "00c24dec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00c249bc",
      "incomplete_value": true,
      "site": "00c249c4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00c249c4"
      ],
      [
        "FALL_THROUGH",
        "00c24dec"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00c24de4",
      "incomplete_value": true,
      "site": "00c24df4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00c249bc",
      "incomplete_value": true,
      "site": "00c249cc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00c249c4"
      ],
      [
        "FALL_THROUGH",
        "00c24dec"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00c24de4",
      "incomplete_value": true,
      "site": "00c24df4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00c249bc",
      "incomplete_value": true,
      "site": "00c249cc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 2,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00c249b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c249ac.md#insn-00c249b8) · [`00c249dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c249ac.md#insn-00c249dc)
- 新版 `00c24de0`（命令位置の公開資料なし） · `00c24e04`（命令位置の公開資料なし）

~~~diff
- 00c249b8 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 00c249b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00c249b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00c249b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c24de0 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00c24de0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c24de0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c24de0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00c249b8 bytes 29a12291
+ 00c24de0 bytes 29a13291
- 00c249dc ["INT_ADD", "register:40f0:8", ["const:c249dc:8", "const:4:8"]]
- 00c249dc ["CALL", null, ["callee:00c53cd0:8"]]
+ 00c24e04 ["INT_ADD", "register:40f0:8", ["const:c24e04:8", "const:4:8"]]
+ 00c24e04 ["CALL", null, ["callee:00c53cd0:8"]]
- 00c249dc bytes b5bb0094
+ 00c24e04 bytes b3bb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9406cd43221bbdca1623481d17f7c4b1"></a>

### [`00c249ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c249ec.md) → [`00c24e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24e14.md) _ZNSt6__ndk16localeD1Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c58290`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58290.md) · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c24e30",
      "incomplete_value": true,
      "site": "00c24e34",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00c24a08",
      "incomplete_value": true,
      "site": "00c24a0c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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


#### 変更候補の命令位置

- 旧版 [`00c24a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c249ec.md#insn-00c24a04) · [`00c24a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c249ec.md#insn-00c24a18)
- 新版 `00c24e2c`（命令位置の公開資料なし） · `00c24e40`（命令位置の公開資料なし）

~~~diff
- 00c24a04 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 00c24a04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c24a04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c24a04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c24e2c ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00c24e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c24e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c24e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c24a04 bytes 08a12291
+ 00c24e2c bytes 08a13291
- 00c24a18 ["INT_ADD", "register:40f0:8", ["const:c24a18:8", "const:4:8"]]
- 00c24a18 ["CALL", null, ["callee:00c53d00:8"]]
+ 00c24e40 ["INT_ADD", "register:40f0:8", ["const:c24e40:8", "const:4:8"]]
+ 00c24e40 ["CALL", null, ["callee:00c53d00:8"]]
- 00c24a18 bytes b2bb0094
+ 00c24e40 bytes b0bb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6faa79b325338180487834eb4185c792"></a>

### [`00c24a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24a4c.md) → [`00c24e74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24e74.md) _ZNSt6__ndk16localeaSERKS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md) · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00c5e2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e2e0.md) · 呼出先 2件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c24e9c",
      "incomplete_value": true,
      "site": "00c24ea0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00c24a74",
      "incomplete_value": true,
      "site": "00c24a78",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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


#### 変更候補の命令位置

- 旧版 [`00c24a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24a4c.md#insn-00c24a68) · [`00c24a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24a4c.md#insn-00c24a84) · [`00c24a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24a4c.md#insn-00c24a9c)
- 新版 `00c24e90`（命令位置の公開資料なし） · `00c24eac`（命令位置の公開資料なし） · `00c24ec4`（命令位置の公開資料なし）

~~~diff
- 00c24a68 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 00c24a68 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00c24a68 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00c24a68 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00c24e90 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00c24e90 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00c24e90 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00c24e90 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00c24a68 bytes d6a22291
+ 00c24e90 bytes d6a23291
- 00c24a84 ["INT_ADD", "register:40f0:8", ["const:c24a84:8", "const:4:8"]]
- 00c24a84 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00c24eac ["INT_ADD", "register:40f0:8", ["const:c24eac:8", "const:4:8"]]
+ 00c24eac ["CALL", null, ["callee:00c53cd0:8"]]
- 00c24a84 bytes 8bbb0094
+ 00c24eac bytes 89bb0094
- 00c24a9c ["INT_ADD", "register:40f0:8", ["const:c24a9c:8", "const:4:8"]]
- 00c24a9c ["CALL", null, ["callee:00c53d00:8"]]
+ 00c24ec4 ["INT_ADD", "register:40f0:8", ["const:c24ec4:8", "const:4:8"]]
+ 00c24ec4 ["CALL", null, ["callee:00c53d00:8"]]
- 00c24a9c bytes 91bb0094
+ 00c24ec4 bytes 8fbb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c6743a4374e344b58566c4fe4307e54"></a>

### [`00c24ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ad4.md) → [`00c24efc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c24efc.md) _ZNSt6__ndk16localeC1EPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c1f48c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c1f/00c1f48c.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c24ff8",
      "incomplete_value": false,
      "site": "00c24ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:d5d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24bd0",
      "incomplete_value": false,
      "site": "00c24bd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:d1d:8"
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
      "00c24ff8",
      "PARAM",
      [
        "storage",
        "002b5d1d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c24ff8",
      "PARAM",
      [
        "storage",
        "002b5d5d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24bd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ad4.md#insn-00c24bd4) · [`00c24b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ad4.md#insn-00c24b00) · [`00c24b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ad4.md#insn-00c24b0c)
- 新版 `00c24ffc`（命令位置の公開資料なし） · `00c24f28`（命令位置の公開資料なし） · `00c24f34`（命令位置の公開資料なし）

~~~diff
- 00c24bd4 ["INT_ADD", "register:40f0:8", ["const:c24bd4:8", "const:4:8"]]
- 00c24bd4 ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c24ffc ["INT_ADD", "register:40f0:8", ["const:c24ffc:8", "const:4:8"]]
+ 00c24ffc ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c24bd4 bytes f7e30094
+ 00c24ffc bytes ede30094
- 00c24b00 ["INT_ADD", "register:40f0:8", ["const:c24b00:8", "const:4:8"]]
- 00c24b00 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c24f28 ["INT_ADD", "register:40f0:8", ["const:c24f28:8", "const:4:8"]]
+ 00c24f28 ["CALL", null, ["callee:00c57e90:8"]]
- 00c24b00 bytes e4cb0094
+ 00c24f28 bytes dacb0094
- 00c24b0c ["INT_ADD", "register:40f0:8", ["const:c24b0c:8", "const:4:8"]]
- 00c24b0c ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c24f34 ["INT_ADD", "register:40f0:8", ["const:c24f34:8", "const:4:8"]]
+ 00c24f34 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c24b0c bytes 35cc0094
+ 00c24f34 bytes 2bcc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a427c6816b6bb4e0d8b35833c7d37f4"></a>

### [`00c24c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c78.md) → [`00c250a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c250a0.md) _ZNSt6__ndk16localeC1ERKS0_PKci

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c21928`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c21/00c21928.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c251b4",
      "incomplete_value": false,
      "site": "00c251b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:d5d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24d8c",
      "incomplete_value": false,
      "site": "00c24d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:d1d:8"
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
      "00c251b4",
      "PARAM",
      [
        "storage",
        "002b5d1d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c251b4",
      "PARAM",
      [
        "storage",
        "002b5d5d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c78.md#insn-00c24d90) · [`00c24cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c78.md#insn-00c24cb0) · [`00c24cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c78.md#insn-00c24cc0)
- 新版 `00c251b8`（命令位置の公開資料なし） · `00c250d8`（命令位置の公開資料なし） · `00c250e8`（命令位置の公開資料なし）

~~~diff
- 00c24d90 ["INT_ADD", "register:40f0:8", ["const:c24d90:8", "const:4:8"]]
- 00c24d90 ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00c251b8 ["INT_ADD", "register:40f0:8", ["const:c251b8:8", "const:4:8"]]
+ 00c251b8 ["CALL", null, ["callee:00c5dfb0:8"]]
- 00c24d90 bytes 88e30094
+ 00c251b8 bytes 7ee30094
- 00c24cb0 ["INT_ADD", "register:40f0:8", ["const:c24cb0:8", "const:4:8"]]
- 00c24cb0 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c250d8 ["INT_ADD", "register:40f0:8", ["const:c250d8:8", "const:4:8"]]
+ 00c250d8 ["CALL", null, ["callee:00c57e90:8"]]
- 00c24cb0 bytes 78cb0094
+ 00c250d8 bytes 6ecb0094
- 00c24cc0 ["INT_ADD", "register:40f0:8", ["const:c24cc0:8", "const:4:8"]]
- 00c24cc0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 00c250e8 ["INT_ADD", "register:40f0:8", ["const:c250e8:8", "const:4:8"]]
+ 00c250e8 ["CALL", null, ["callee:00c57fe0:8"]]
- 00c24cc0 bytes c8cb0094
+ 00c250e8 bytes becb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5829b83ce3b0677387f0aade532e910"></a>

### [`00c24ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ee8.md) → [`00c25310`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25310.md) _ZNSt6__ndk16locale14__install_ctorERKS0_PNS0_5facetEl

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c244ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c244ac.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c248d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c24/00c248d4.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c25368",
      "incomplete_value": true,
      "site": "00c25370",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4098:8"
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
      "definition_site": "00c24f40",
      "incomplete_value": true,
      "site": "00c24f48",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4098:8"
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
    "ordinal": 1,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00c24f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ee8.md#insn-00c24f14) · [`00c24f28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ee8.md#insn-00c24f28) · [`00c24f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ee8.md#insn-00c24f3c)
- 新版 `00c2533c`（命令位置の公開資料なし） · `00c25350`（命令位置の公開資料なし） · `00c25364`（命令位置の公開資料なし）

~~~diff
- 00c24f14 ["INT_ADD", "register:40f0:8", ["const:c24f14:8", "const:4:8"]]
- 00c24f14 ["CALL", null, ["callee:00c57e90:8"]]
+ 00c2533c ["INT_ADD", "register:40f0:8", ["const:c2533c:8", "const:4:8"]]
+ 00c2533c ["CALL", null, ["callee:00c57e90:8"]]
- 00c24f14 bytes dfca0094
+ 00c2533c bytes d5ca0094
- 00c24f28 ["INT_ADD", "register:40f0:8", ["const:c24f28:8", "const:4:8"]]
- 00c24f28 ["CALL", null, ["callee:00c248d4:8"]]
+ 00c25350 ["INT_ADD", "register:40f0:8", ["const:c25350:8", "const:4:8"]]
+ 00c25350 ["CALL", null, ["callee:00c248d4:8"]]
- 00c24f28 bytes 61fdff97
+ 00c25350 bytes 61fdff97
- 00c24f3c ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 00c24f3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c24f3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c24f3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c25364 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00c25364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c25364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c25364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c24f3c bytes 08a12291
+ 00c25364 bytes 08a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d2672a647aba4c9924bc1626ad4d7e1"></a>

### [`00c24f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24f80.md) → [`00c253a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c253a8.md) _ZNSt6__ndk16locale6globalERKS0_

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c25444",
      "incomplete_value": true,
      "site": "00c25444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2501c",
      "incomplete_value": true,
      "site": "00c2501c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c25414",
      "incomplete_value": true,
      "site": "00c25418",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40b8:8"
              ]
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
      "definition_site": "00c24fec",
      "incomplete_value": true,
      "site": "00c24ff0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40b8:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c253e0",
      "incomplete_value": false,
      "site": "00c253e8",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c24fb8",
      "incomplete_value": false,
      "site": "00c24fc0",
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
            "const:9f0:8"
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
      "00c253d0",
      "READ",
      [
        "storage",
        "011279f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c253e0",
      "PARAM",
      [
        "storage",
        "011279f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c25410",
      "READ",
      [
        "storage",
        "011279f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c253d0",
      "READ",
      [
        "storage",
        "01127df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c253e0",
      "PARAM",
      [
        "storage",
        "01127df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00c25410",
      "READ",
      [
        "storage",
        "01127df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c24fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24f80.md#insn-00c24fc0) · [`00c2501c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24f80.md#insn-00c2501c) · [`00c25114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24f80.md#insn-00c25114)
- 新版 `00c253e8`（命令位置の公開資料なし） · `00c25444`（命令位置の公開資料なし） · `00c2553c`（命令位置の公開資料なし）

~~~diff
- 00c24fc0 ["INT_ADD", "register:40f0:8", ["const:c24fc0:8", "const:4:8"]]
- 00c24fc0 ["CALL", null, ["callee:00c5a7d0:8"]]
+ 00c253e8 ["INT_ADD", "register:40f0:8", ["const:c253e8:8", "const:4:8"]]
+ 00c253e8 ["CALL", null, ["callee:00c5a7d0:8"]]
- 00c24fc0 bytes 04d50094
+ 00c253e8 bytes fad40094
- 00c2501c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:9f0:8"]]
- 00c2501c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c25444 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:df0:8"]]
+ 00c25444 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00c2501c bytes c8fa04f9
+ 00c25444 bytes c8fa06f9
- 00c25114 ["INT_ADD", "register:40f0:8", ["const:c25114:8", "const:4:8"]]
- 00c25114 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c2553c ["INT_ADD", "register:40f0:8", ["const:c2553c:8", "const:4:8"]]
+ 00c2553c ["CALL", null, ["callee:00c57e50:8"]]
- 00c25114 bytes 4fca0094
+ 00c2553c bytes 45ca0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fbc9dbb67bba273feaff4f4f76062ab"></a>

### [`00c25434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25434.md) → [`00c2585c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c2585c.md) _ZNSt6__ndk114collate_bynameIcEC1EPKcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c25888",
      "incomplete_value": true,
      "site": "00c25888",
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
      "definition_site": "00c25460",
      "incomplete_value": true,
      "site": "00c25460",
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
      "definition_site": "00c258c4",
      "incomplete_value": false,
      "site": "00c258d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:acd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2549c",
      "incomplete_value": false,
      "site": "00c254ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "00c2587c",
      "READ",
      [
        "storage",
        "00c9b9b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c25888",
      "DATA",
      [
        "storage",
        "00c932e8",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c258c4",
      "PARAM",
      [
        "storage",
        "002aaa00",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c2587c",
      "READ",
      [
        "storage",
        "00c9bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c25888",
      "DATA",
      [
        "storage",
        "00c936e8",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c258c4",
      "PARAM",
      [
        "storage",
        "002aaacd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c254ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25434.md#insn-00c254ac) · [`00c25454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25434.md#insn-00c25454) · [`00c2546c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25434.md#insn-00c2546c)
- 新版 `00c258d4`（命令位置の公開資料なし） · `00c2587c`（命令位置の公開資料なし） · `00c25894`（命令位置の公開資料なし）

~~~diff
- 00c254ac ["INT_ADD", "register:40f0:8", ["const:c254ac:8", "const:4:8"]]
- 00c254ac ["CALL", null, ["callee:00c25934:8"]]
+ 00c258d4 ["INT_ADD", "register:40f0:8", ["const:c258d4:8", "const:4:8"]]
+ 00c258d4 ["CALL", null, ["callee:00c25934:8"]]
- 00c254ac bytes 18000094
+ 00c258d4 bytes 18000094
- 00c25454 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00c25454 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c2587c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
+ 00c2587c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c25454 bytes 08dd44f9
+ 00c2587c bytes 08dd46f9
- 00c2546c ["INT_ADD", "register:40f0:8", ["const:c2546c:8", "const:4:8"]]
- 00c2546c ["CALL", null, ["callee:00c5d220:8"]]
+ 00c25894 ["INT_ADD", "register:40f0:8", ["const:c25894:8", "const:4:8"]]
+ 00c25894 ["CALL", null, ["callee:00c5d220:8"]]
- 00c2546c bytes 6dde0094
+ 00c25894 bytes 63de0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-041e3aeafe180a6db56cc12cf9e0b71e"></a>

### [`00c25570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25570.md) → [`00c25998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25998.md) _ZNSt6__ndk114collate_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e420.md) · 呼出先 6件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 1件 [`00c5e820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e820.md) · 呼出先 6件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c259c4",
      "incomplete_value": true,
      "site": "00c259c4",
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
      "definition_site": "00c2559c",
      "incomplete_value": true,
      "site": "00c2559c",
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
      "definition_site": "00c25a04",
      "incomplete_value": false,
      "site": "00c25a14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:acd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c255dc",
      "incomplete_value": false,
      "site": "00c255ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:a00:8"
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
      "00c259b8",
      "READ",
      [
        "storage",
        "00c9b9b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c259c4",
      "DATA",
      [
        "storage",
        "00c932e8",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c25a04",
      "PARAM",
      [
        "storage",
        "002aaa00",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c259b8",
      "READ",
      [
        "storage",
        "00c9bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c259c4",
      "DATA",
      [
        "storage",
        "00c936e8",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c25a04",
      "PARAM",
      [
        "storage",
        "002aaacd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c255ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25570.md#insn-00c255ec) · [`00c25590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25570.md#insn-00c25590) · [`00c255b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25570.md#insn-00c255b8)
- 新版 `00c25a14`（命令位置の公開資料なし） · `00c259b8`（命令位置の公開資料なし） · `00c259e0`（命令位置の公開資料なし）

~~~diff
- 00c255ec ["INT_ADD", "register:40f0:8", ["const:c255ec:8", "const:4:8"]]
- 00c255ec ["CALL", null, ["callee:00c580b0:8"]]
+ 00c25a14 ["INT_ADD", "register:40f0:8", ["const:c25a14:8", "const:4:8"]]
+ 00c25a14 ["CALL", null, ["callee:00c580b0:8"]]
- 00c255ec bytes b1c90094
+ 00c25a14 bytes a7c90094
- 00c25590 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00c25590 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c259b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
+ 00c259b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c25590 bytes 08dd44f9
+ 00c259b8 bytes 08dd46f9
- 00c255b8 ["INT_ADD", "register:40f0:8", ["const:c255b8:8", "const:4:8"]]
- 00c255b8 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c259e0 ["INT_ADD", "register:40f0:8", ["const:c259e0:8", "const:4:8"]]
+ 00c259e0 ["CALL", null, ["callee:00c5d220:8"]]
- 00c255b8 bytes 1ade0094
+ 00c259e0 bytes 10de0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83b7ba867dd8a6bf7720315ea7e22780"></a>

### [`00c25634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25634.md) → [`00c25a5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25a5c.md) _ZNSt6__ndk114collate_bynameIcED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e520.md) · 呼出先 2件 [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md)
- 新版 呼出元 1件 [`00c5e920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e920.md) · 呼出先 2件 [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c25a7c",
      "incomplete_value": true,
      "site": "00c25a80",
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
      "definition_site": "00c25654",
      "incomplete_value": true,
      "site": "00c25658",
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
      "00c25a74",
      "READ",
      [
        "storage",
        "00c9b9b8",
        null,
        "pointer"
      ]
    ],
    [
      "00c25a80",
      "DATA",
      [
        "storage",
        "00c932e8",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00c25a74",
      "READ",
      [
        "storage",
        "00c9bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "00c25a80",
      "DATA",
      [
        "storage",
        "00c936e8",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2564c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25634.md#insn-00c2564c) · [`00c2565c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25634.md#insn-00c2565c)
- 新版 `00c25a74`（命令位置の公開資料なし） · `00c25a84`（命令位置の公開資料なし）

~~~diff
- 00c2564c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00c2564c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c25a74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
+ 00c25a74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c2564c bytes 08dd44f9
+ 00c25a74 bytes 08dd46f9
- 00c2565c ["INT_ADD", "register:40f0:8", ["const:c2565c:8", "const:4:8"]]
- 00c2565c ["CALL", null, ["callee:00c5d1d0:8"]]
+ 00c25a84 ["INT_ADD", "register:40f0:8", ["const:c25a84:8", "const:4:8"]]
+ 00c25a84 ["CALL", null, ["callee:00c5d1d0:8"]]
- 00c2565c bytes dddd0094
+ 00c25a84 bytes d3dd0094
~~~


<a id="compare-1d5540234da1bb8fbbe41047d693647a"></a>

### [`00c25a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25a78.md) → [`00c25ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25ea0.md) _ZNSt6__ndk114collate_bynameIwEC1EPKcm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00c25934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25934.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c25f08",
      "incomplete_value": false,
      "site": "00c25f18",
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
            "const:d97:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c25ae0",
      "incomplete_value": false,
      "site": "00c25af0",
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
            "const:cca:8"
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
      "00c25ec0",
      "READ",
      [
        "storage",
        "00c9b9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c25ecc",
      "DATA",
      [
        "storage",
        "00c93328",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c25f08",
      "PARAM",
      [
        "storage",
        "0029fcca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c25ec0",
      "READ",
      [
        "storage",
        "00c9bdc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c25ecc",
      "DATA",
      [
        "storage",
        "00c93728",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c25f08",
      "PARAM",
      [
        "storage",
        "0029fd97",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c25af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25a78.md#insn-00c25af0) · [`00c25a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25a78.md#insn-00c25a98) · [`00c25ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25a78.md#insn-00c25ab0)
- 新版 `00c25f18`（命令位置の公開資料なし） · `00c25ec0`（命令位置の公開資料なし） · `00c25ed8`（命令位置の公開資料なし）

~~~diff
- 00c25af0 ["INT_ADD", "register:40f0:8", ["const:c25af0:8", "const:4:8"]]
- 00c25af0 ["CALL", null, ["callee:00c25934:8"]]
+ 00c25f18 ["INT_ADD", "register:40f0:8", ["const:c25f18:8", "const:4:8"]]
+ 00c25f18 ["CALL", null, ["callee:00c25934:8"]]
- 00c25af0 bytes 87feff97
+ 00c25f18 bytes 87feff97
- 00c25a98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9c0:8"]]
- 00c25a98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c25ec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00c25ec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c25a98 bytes 08e144f9
+ 00c25ec0 bytes 08e146f9
- 00c25ab0 ["INT_ADD", "register:40f0:8", ["const:c25ab0:8", "const:4:8"]]
- 00c25ab0 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c25ed8 ["INT_ADD", "register:40f0:8", ["const:c25ed8:8", "const:4:8"]]
+ 00c25ed8 ["CALL", null, ["callee:00c5d220:8"]]
- 00c25ab0 bytes dcdc0094
+ 00c25ed8 bytes d2dc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2258a6a870af16c966f8474c8302a257"></a>

### [`00c25b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25b50.md) → [`00c25f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c25/00c25f78.md) _ZNSt6__ndk114collate_bynameIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e430.md) · 呼出先 6件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 1件 [`00c5e830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e830.md) · 呼出先 6件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c25fa4",
      "incomplete_value": true,
      "site": "00c25fa4",
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
      "definition_site": "00c25b7c",
      "incomplete_value": true,
      "site": "00c25b7c",
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
      "definition_site": "00c25fe4",
      "incomplete_value": true,
      "site": "00c25ff4",
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
            "const:d97:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c25bbc",
      "incomplete_value": true,
      "site": "00c25bcc",
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
            "const:cca:8"
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
      "00c25f98",
      "READ",
      [
        "storage",
        "00c9b9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c25fa4",
      "DATA",
      [
        "storage",
        "00c93328",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c25fe4",
      "PARAM",
      [
        "storage",
        "0029fcca",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c25f98",
      "READ",
      [
        "storage",
        "00c9bdc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c25fa4",
      "DATA",
      [
        "storage",
        "00c93728",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00c25fe4",
      "PARAM",
      [
        "storage",
        "0029fd97",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c25bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25b50.md#insn-00c25bcc) · [`00c25b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25b50.md#insn-00c25b70) · [`00c25b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25b50.md#insn-00c25b98)
- 新版 `00c25ff4`（命令位置の公開資料なし） · `00c25f98`（命令位置の公開資料なし） · `00c25fc0`（命令位置の公開資料なし）

~~~diff
- 00c25bcc ["INT_ADD", "register:40f0:8", ["const:c25bcc:8", "const:4:8"]]
- 00c25bcc ["CALL", null, ["callee:00c580b0:8"]]
+ 00c25ff4 ["INT_ADD", "register:40f0:8", ["const:c25ff4:8", "const:4:8"]]
+ 00c25ff4 ["CALL", null, ["callee:00c580b0:8"]]
- 00c25bcc bytes 39c80094
+ 00c25ff4 bytes 2fc80094
- 00c25b70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9c0:8"]]
- 00c25b70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c25f98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00c25f98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c25b70 bytes 08e144f9
+ 00c25f98 bytes 08e146f9
- 00c25b98 ["INT_ADD", "register:40f0:8", ["const:c25b98:8", "const:4:8"]]
- 00c25b98 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c25fc0 ["INT_ADD", "register:40f0:8", ["const:c25fc0:8", "const:4:8"]]
+ 00c25fc0 ["CALL", null, ["callee:00c5d220:8"]]
- 00c25b98 bytes a2dc0094
+ 00c25fc0 bytes 98dc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a39a4aeec3cae7635e086997138bbe6"></a>

### [`00c25c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c14.md) → [`00c2603c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c2603c.md) _ZNSt6__ndk114collate_bynameIwED2Ev

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e550.md) · 呼出先 2件 [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md)
- 新版 呼出元 1件 [`00c5e950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e950.md) · 呼出先 2件 [`00c58300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58300.md) [`00c5d1d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d1d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c2605c",
      "incomplete_value": true,
      "site": "00c26060",
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
      "definition_site": "00c25c34",
      "incomplete_value": true,
      "site": "00c25c38",
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
      "00c26054",
      "READ",
      [
        "storage",
        "00c9b9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00c26060",
      "DATA",
      [
        "storage",
        "00c93328",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00c26054",
      "READ",
      [
        "storage",
        "00c9bdc0",
        null,
        "pointer"
      ]
    ],
    [
      "00c26060",
      "DATA",
      [
        "storage",
        "00c93728",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c25c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c14.md#insn-00c25c2c) · [`00c25c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c14.md#insn-00c25c3c)
- 新版 `00c26054`（命令位置の公開資料なし） · `00c26064`（命令位置の公開資料なし）

~~~diff
- 00c25c2c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9c0:8"]]
- 00c25c2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c26054 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00c26054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c25c2c bytes 08e144f9
+ 00c26054 bytes 08e146f9
- 00c25c3c ["INT_ADD", "register:40f0:8", ["const:c25c3c:8", "const:4:8"]]
- 00c25c3c ["CALL", null, ["callee:00c5d1d0:8"]]
+ 00c26064 ["INT_ADD", "register:40f0:8", ["const:c26064:8", "const:4:8"]]
+ 00c26064 ["CALL", null, ["callee:00c5d1d0:8"]]
- 00c25c3c bytes 65dc0094
+ 00c26064 bytes 5bdc0094
~~~


<a id="compare-39f920ffc4174ba6650b42eaaff2867b"></a>

### [`00c260fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c260fc.md) → [`00c26524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26524.md) _ZNKSt6__ndk15ctypeIwE5do_isEmw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c26548",
      "incomplete_value": true,
      "site": "00c2654c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26120",
      "incomplete_value": true,
      "site": "00c26124",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_EQUAL"
            ]
          ]
        ]
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
      "00c26540",
      "DATA",
      [
        "storage",
        "00310f58",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26540",
      "DATA",
      [
        "storage",
        "00310f98",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c260fc.md#insn-00c26114)
- 新版 `00c2653c`（命令位置の公開資料なし）

~~~diff
- 00c26114 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00c26114 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c26114 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c26114 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c2653c ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00c2653c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c2653c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c2653c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c26114 bytes 08613d91
+ 00c2653c bytes 08613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebb8343a8d8622047733874a08d44ee1"></a>

### [`00c26214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26214.md) → [`00c2663c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c2663c.md) _ZNKSt6__ndk15ctypeIwE10do_toupperEw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md) [`00c5e590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e590.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md) [`00c5e990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e990.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c266bc",
      "incomplete_value": true,
      "site": "00c266bc",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26294",
      "incomplete_value": true,
      "site": "00c26294",
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
            "const:898:8"
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
      "definition_site": "00c2669c",
      "incomplete_value": false,
      "site": "00c266a0",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26274",
      "incomplete_value": false,
      "site": "00c26278",
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
            "const:8a0:8"
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
      "definition_site": "00c266ac",
      "incomplete_value": false,
      "site": "00c266b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26284",
      "incomplete_value": false,
      "site": "00c26290",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:13c:8"
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
      "00c26664",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2666c",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2669c",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c26664",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c2666c",
      "READ",
      [
        "storage",
        "01127c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00c2669c",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26214.md#insn-00c26278) · [`00c26290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26214.md#insn-00c26290) · [`00c26294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26214.md#insn-00c26294)
- 新版 `00c266a0`（命令位置の公開資料なし） · `00c266b8`（命令位置の公開資料なし） · `00c266bc`（命令位置の公開資料なし）

~~~diff
- 00c26278 ["INT_ADD", "register:40f0:8", ["const:c26278:8", "const:4:8"]]
- 00c26278 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c266a0 ["INT_ADD", "register:40f0:8", ["const:c266a0:8", "const:4:8"]]
+ 00c266a0 ["CALL", null, ["callee:00c57e50:8"]]
- 00c26278 bytes f6c50094
+ 00c266a0 bytes ecc50094
- 00c26290 ["INT_ADD", "register:40f0:8", ["const:c26290:8", "const:4:8"]]
- 00c26290 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c266b8 ["INT_ADD", "register:40f0:8", ["const:c266b8:8", "const:4:8"]]
+ 00c266b8 ["CALL", null, ["callee:00c5d220:8"]]
- 00c26290 bytes e4da0094
+ 00c266b8 bytes dada0094
- 00c26294 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
- 00c26294 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c266bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
+ 00c266bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26294 bytes 804e04f9
+ 00c266bc bytes 804e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-677bff1c7bedfcf875d3a535b9a63b6b"></a>

### [`00c262c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c262c0.md) → [`00c266e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c266e8.md) _ZNKSt6__ndk15ctypeIwE10do_toupperEPwPKw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26774",
      "incomplete_value": true,
      "site": "00c26774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2634c",
      "incomplete_value": true,
      "site": "00c2634c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00c2674c",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26754",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26760",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2674c",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26754",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26760",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c2634c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c262c0.md#insn-00c2634c) · [`00c262ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c262c0.md#insn-00c262ec) · [`00c26330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c262c0.md#insn-00c26330)
- 新版 `00c26774`（命令位置の公開資料なし） · `00c26714`（命令位置の公開資料なし） · `00c26758`（命令位置の公開資料なし）

~~~diff
- 00c2634c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:898:8"]]
- 00c2634c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26774 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
+ 00c26774 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c2634c bytes c04e04f9
+ 00c26774 bytes c04e06f9
- 00c262ec ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00c262ec ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c262ec ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c262ec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c26714 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00c26714 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26714 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26714 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c262ec bytes b5822291
+ 00c26714 bytes b5823291
- 00c26330 ["INT_ADD", "register:40f0:8", ["const:c26330:8", "const:4:8"]]
- 00c26330 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c26758 ["INT_ADD", "register:40f0:8", ["const:c26758:8", "const:4:8"]]
+ 00c26758 ["CALL", null, ["callee:00c57e50:8"]]
- 00c26330 bytes c8c50094
+ 00c26758 bytes bec50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd9ab6c2a13914d44f791cf1509acab8"></a>

### [`00c26394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26394.md) → [`00c267bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c267bc.md) _ZNKSt6__ndk15ctypeIwE10do_tolowerEw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26834",
      "incomplete_value": false,
      "site": "00c26834",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2640c",
      "incomplete_value": false,
      "site": "00c2640c",
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
            "const:898:8"
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
      "definition_site": "00c26810",
      "incomplete_value": false,
      "site": "00c26814",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c263e8",
      "incomplete_value": false,
      "site": "00c263ec",
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
            "const:8a0:8"
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
      "definition_site": "00c26820",
      "incomplete_value": false,
      "site": "00c2682c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c263f8",
      "incomplete_value": false,
      "site": "00c26404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:13c:8"
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
      "00c267e0",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26810",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26820",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c267e0",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26810",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26820",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c263ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26394.md#insn-00c263ec) · [`00c26404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26394.md#insn-00c26404) · [`00c2640c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26394.md#insn-00c2640c)
- 新版 `00c26814`（命令位置の公開資料なし） · `00c2682c`（命令位置の公開資料なし） · `00c26834`（命令位置の公開資料なし）

~~~diff
- 00c263ec ["INT_ADD", "register:40f0:8", ["const:c263ec:8", "const:4:8"]]
- 00c263ec ["CALL", null, ["callee:00c57e50:8"]]
+ 00c26814 ["INT_ADD", "register:40f0:8", ["const:c26814:8", "const:4:8"]]
+ 00c26814 ["CALL", null, ["callee:00c57e50:8"]]
- 00c263ec bytes 99c50094
+ 00c26814 bytes 8fc50094
- 00c26404 ["INT_ADD", "register:40f0:8", ["const:c26404:8", "const:4:8"]]
- 00c26404 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c2682c ["INT_ADD", "register:40f0:8", ["const:c2682c:8", "const:4:8"]]
+ 00c2682c ["CALL", null, ["callee:00c5d220:8"]]
- 00c26404 bytes 87da0094
+ 00c2682c bytes 7dda0094
- 00c2640c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:898:8"]]
- 00c2640c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26834 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
+ 00c26834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c2640c bytes 004d04f9
+ 00c26834 bytes 004d06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9dfc851abe1a403593e646ca919815e"></a>

### [`00c26438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26438.md) → [`00c26860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26860.md) _ZNKSt6__ndk15ctypeIwE10do_tolowerEPwPKw

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c268ec",
      "incomplete_value": true,
      "site": "00c268ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c264c4",
      "incomplete_value": true,
      "site": "00c264c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00c268c4",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c268cc",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c268d8",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c268c4",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c268cc",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c268d8",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c264c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26438.md#insn-00c264c4) · [`00c26464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26438.md#insn-00c26464) · [`00c264a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26438.md#insn-00c264a8)
- 新版 `00c268ec`（命令位置の公開資料なし） · `00c2688c`（命令位置の公開資料なし） · `00c268d0`（命令位置の公開資料なし）

~~~diff
- 00c264c4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:898:8"]]
- 00c264c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c268ec ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
+ 00c268ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c264c4 bytes c04e04f9
+ 00c268ec bytes c04e06f9
- 00c26464 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00c26464 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26464 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26464 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c2688c ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00c2688c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c2688c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c2688c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c26464 bytes b5822291
+ 00c2688c bytes b5823291
- 00c264a8 ["INT_ADD", "register:40f0:8", ["const:c264a8:8", "const:4:8"]]
- 00c264a8 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c268d0 ["INT_ADD", "register:40f0:8", ["const:c268d0:8", "const:4:8"]]
+ 00c268d0 ["CALL", null, ["callee:00c57e50:8"]]
- 00c264a8 bytes 6ac50094
+ 00c268d0 bytes 60c50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79090ac018a0eb0fa9c1ffa0f6c67485"></a>

### [`00c267e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c267e0.md) → [`00c26c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26c08.md) _ZNSt6__ndk15ctypeIcEC1EPKmbm

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5e3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e3e0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e7e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e7e0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c26c20",
      "incomplete_value": true,
      "site": "00c26c24",
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
      "definition_site": "00c267f8",
      "incomplete_value": true,
      "site": "00c267fc",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c26c34",
      "incomplete_value": true,
      "site": "00c26c38",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c2680c",
      "incomplete_value": true,
      "site": "00c26810",
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
            "const:f58:8"
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
      "00c26c14",
      "READ",
      [
        "storage",
        "00c9b9c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c26c24",
      "DATA",
      [
        "storage",
        "00c93368",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c26c38",
      "DATA",
      [
        "storage",
        "00310f58",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26c14",
      "READ",
      [
        "storage",
        "00c9bdc8",
        null,
        "pointer"
      ]
    ],
    [
      "00c26c24",
      "DATA",
      [
        "storage",
        "00c93768",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c26c38",
      "DATA",
      [
        "storage",
        "00310f98",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c267ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c267e0.md#insn-00c267ec) · [`00c2680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c267e0.md#insn-00c2680c)
- 新版 `00c26c14`（命令位置の公開資料なし） · `00c26c34`（命令位置の公開資料なし）

~~~diff
- 00c267ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9c8:8"]]
- 00c267ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00c26c14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc8:8"]]
+ 00c26c14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00c267ec bytes 08e544f9
+ 00c26c14 bytes 08e546f9
- 00c2680c ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00c2680c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00c2680c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00c2680c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c26c34 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00c26c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c26c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c26c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00c2680c bytes 08613d91
+ 00c26c34 bytes 08613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd6e34730707ee26c42db23853361424"></a>

### [`00c26898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26898.md) → [`00c26cc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26cc0.md) _ZNKSt6__ndk15ctypeIcE10do_toupperEc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26d38",
      "incomplete_value": false,
      "site": "00c26d38",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26910",
      "incomplete_value": false,
      "site": "00c26910",
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
            "const:898:8"
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
      "definition_site": "00c26d14",
      "incomplete_value": false,
      "site": "00c26d18",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c268ec",
      "incomplete_value": false,
      "site": "00c268f0",
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
            "const:8a0:8"
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
      "definition_site": "00c26d24",
      "incomplete_value": false,
      "site": "00c26d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c268fc",
      "incomplete_value": false,
      "site": "00c26908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:13c:8"
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
      "00c26ce0",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26d14",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26d24",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26ce0",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26d14",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26d24",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c268f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26898.md#insn-00c268f0) · [`00c26908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26898.md#insn-00c26908) · [`00c26910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26898.md#insn-00c26910)
- 新版 `00c26d18`（命令位置の公開資料なし） · `00c26d30`（命令位置の公開資料なし） · `00c26d38`（命令位置の公開資料なし）

~~~diff
- 00c268f0 ["INT_ADD", "register:40f0:8", ["const:c268f0:8", "const:4:8"]]
- 00c268f0 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c26d18 ["INT_ADD", "register:40f0:8", ["const:c26d18:8", "const:4:8"]]
+ 00c26d18 ["CALL", null, ["callee:00c57e50:8"]]
- 00c268f0 bytes 58c40094
+ 00c26d18 bytes 4ec40094
- 00c26908 ["INT_ADD", "register:40f0:8", ["const:c26908:8", "const:4:8"]]
- 00c26908 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c26d30 ["INT_ADD", "register:40f0:8", ["const:c26d30:8", "const:4:8"]]
+ 00c26d30 ["CALL", null, ["callee:00c5d220:8"]]
- 00c26908 bytes 46d90094
+ 00c26d30 bytes 3cd90094
- 00c26910 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:898:8"]]
- 00c26910 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26d38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
+ 00c26d38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26910 bytes 004d04f9
+ 00c26d38 bytes 004d06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e528ffcbdc3dd173c19e4d5a5bc0a314"></a>

### [`00c2693c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c2693c.md) → [`00c26d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26d64.md) _ZNKSt6__ndk15ctypeIcE10do_toupperEPcPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26df0",
      "incomplete_value": true,
      "site": "00c26df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c269c8",
      "incomplete_value": true,
      "site": "00c269c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00c26dc8",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26dd0",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26ddc",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26dc8",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26dd0",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26ddc",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c269c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c2693c.md#insn-00c269c8) · [`00c26968`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c2693c.md#insn-00c26968) · [`00c269ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c2693c.md#insn-00c269ac)
- 新版 `00c26df0`（命令位置の公開資料なし） · `00c26d90`（命令位置の公開資料なし） · `00c26dd4`（命令位置の公開資料なし）

~~~diff
- 00c269c8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:898:8"]]
- 00c269c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26df0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
+ 00c26df0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c269c8 bytes c04e04f9
+ 00c26df0 bytes c04e06f9
- 00c26968 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00c26968 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26968 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26968 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c26d90 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00c26d90 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26d90 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26d90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c26968 bytes b5822291
+ 00c26d90 bytes b5823291
- 00c269ac ["INT_ADD", "register:40f0:8", ["const:c269ac:8", "const:4:8"]]
- 00c269ac ["CALL", null, ["callee:00c57e50:8"]]
+ 00c26dd4 ["INT_ADD", "register:40f0:8", ["const:c26dd4:8", "const:4:8"]]
+ 00c26dd4 ["CALL", null, ["callee:00c57e50:8"]]
- 00c269ac bytes 29c40094
+ 00c26dd4 bytes 1fc40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3dd0dff244cef661f9c7cda7d8f93e5"></a>

### [`00c26a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26a10.md) → [`00c26e38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26e38.md) _ZNKSt6__ndk15ctypeIcE10do_tolowerEc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26eb0",
      "incomplete_value": false,
      "site": "00c26eb0",
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
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26a88",
      "incomplete_value": false,
      "site": "00c26a88",
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
            "const:898:8"
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
      "definition_site": "00c26e8c",
      "incomplete_value": false,
      "site": "00c26e90",
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
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26a64",
      "incomplete_value": false,
      "site": "00c26a68",
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
            "const:8a0:8"
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
      "definition_site": "00c26e9c",
      "incomplete_value": true,
      "site": "00c26ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26a74",
      "incomplete_value": true,
      "site": "00c26a80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:13c:8"
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
      "00c26e58",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26e8c",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26e9c",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26e58",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26e8c",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26e9c",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26a10.md#insn-00c26a68) · [`00c26a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26a10.md#insn-00c26a80) · [`00c26a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26a10.md#insn-00c26a88)
- 新版 `00c26e90`（命令位置の公開資料なし） · `00c26ea8`（命令位置の公開資料なし） · `00c26eb0`（命令位置の公開資料なし）

~~~diff
- 00c26a68 ["INT_ADD", "register:40f0:8", ["const:c26a68:8", "const:4:8"]]
- 00c26a68 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c26e90 ["INT_ADD", "register:40f0:8", ["const:c26e90:8", "const:4:8"]]
+ 00c26e90 ["CALL", null, ["callee:00c57e50:8"]]
- 00c26a68 bytes fac30094
+ 00c26e90 bytes f0c30094
- 00c26a80 ["INT_ADD", "register:40f0:8", ["const:c26a80:8", "const:4:8"]]
- 00c26a80 ["CALL", null, ["callee:00c5d220:8"]]
+ 00c26ea8 ["INT_ADD", "register:40f0:8", ["const:c26ea8:8", "const:4:8"]]
+ 00c26ea8 ["CALL", null, ["callee:00c5d220:8"]]
- 00c26a80 bytes e8d80094
+ 00c26ea8 bytes ded80094
- 00c26a88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:898:8"]]
- 00c26a88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26eb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c98:8"]]
+ 00c26eb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26a88 bytes 004d04f9
+ 00c26eb0 bytes 004d06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d77a5c59158ac729659e017a839e64d6"></a>

### [`00c26ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26ab4.md) → [`00c26edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c26/00c26edc.md) _ZNKSt6__ndk15ctypeIcE10do_tolowerEPcPKc

採用 · 移動量 `+0x428` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c5d220`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d220.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c26f68",
      "incomplete_value": true,
      "site": "00c26f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c26b40",
      "incomplete_value": true,
      "site": "00c26b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00c26f40",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26f48",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26f54",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26f40",
      "READ",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26f48",
      "PARAM",
      [
        "storage",
        "01127ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26f54",
      "PARAM",
      [
        "storage",
        "002b617c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00c26b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26ab4.md#insn-00c26b40) · [`00c26ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26ab4.md#insn-00c26ae0) · [`00c26b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26ab4.md#insn-00c26b24)
- 新版 `00c26f68`（命令位置の公開資料なし） · `00c26f08`（命令位置の公開資料なし） · `00c26f4c`（命令位置の公開資料なし）

~~~diff
- 00c26b40 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:898:8"]]
- 00c26b40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26f68 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:c98:8"]]
+ 00c26f68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00c26b40 bytes c04e04f9
+ 00c26f68 bytes c04e06f9
- 00c26ae0 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00c26ae0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26ae0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00c26ae0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00c26f08 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00c26f08 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26f08 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00c26f08 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00c26ae0 bytes b5822291
+ 00c26f08 bytes b5823291
- 00c26b24 ["INT_ADD", "register:40f0:8", ["const:c26b24:8", "const:4:8"]]
- 00c26b24 ["CALL", null, ["callee:00c57e50:8"]]
+ 00c26f4c ["INT_ADD", "register:40f0:8", ["const:c26f4c:8", "const:4:8"]]
+ 00c26f4c ["CALL", null, ["callee:00c57e50:8"]]
- 00c26b24 bytes cbc30094
+ 00c26f4c bytes c1c30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

