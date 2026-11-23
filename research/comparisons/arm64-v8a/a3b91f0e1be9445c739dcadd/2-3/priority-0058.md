# v15.7.4 → v16.0.0 · 最優先の変更候補 (58)

[一覧の目次](README.md)

<a id="compare-2c48fc616cff17e7d83eee6cf0c19828"></a>

### [`00aea5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea5b0.md) → [`00b4a334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a334.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a360",
      "incomplete_value": true,
      "site": "00b4a360",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea5dc",
      "incomplete_value": true,
      "site": "00aea5dc",
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
            "const:7d0:8"
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
      "definition_site": "00b4a348",
      "incomplete_value": true,
      "site": "00b4a348",
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
      "definition_site": "00aea5c4",
      "incomplete_value": true,
      "site": "00aea5c4",
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
      "definition_site": "00b4a350",
      "incomplete_value": false,
      "site": "00b4a358",
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
            "const:c36:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea5cc",
      "incomplete_value": false,
      "site": "00aea5d4",
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
            "const:172:8"
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
      "00b4a344",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a350",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00b4a360",
      "WRITE",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a344",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a350",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4a360",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea5d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea5b0.md#insn-00aea5d4) · [`00aea5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea5b0.md#insn-00aea5dc) · [`00aea5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea5b0.md#insn-00aea5bc)
- 新版 `00b4a358`（命令位置の公開資料なし） · `00b4a360`（命令位置の公開資料なし） · `00b4a340`（命令位置の公開資料なし）

~~~diff
- 00aea5d4 ["INT_ADD", "register:40f0:8", ["const:aea5d4:8", "const:4:8"]]
- 00aea5d4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a358 ["INT_ADD", "register:40f0:8", ["const:b4a358:8", "const:4:8"]]
+ 00b4a358 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea5d4 bytes afce0394
+ 00b4a358 bytes ee410494
- 00aea5dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00aea5dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a360 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
+ 00b4a360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea5dc bytes 60ea03f9
+ 00b4a360 bytes 604a03f9
- 00aea5bc ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4a340 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea5bc bytes b32d00d0
+ 00b4a340 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-244604197495f5c098ad98745773bfa1"></a>

### [`00aea5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea5f0.md) → [`00b4a374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a374.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a3a4",
      "incomplete_value": true,
      "site": "00b4a3a4",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea620",
      "incomplete_value": true,
      "site": "00aea620",
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
            "const:7d0:8"
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
      "definition_site": "00b4a388",
      "incomplete_value": true,
      "site": "00b4a388",
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
      "definition_site": "00aea604",
      "incomplete_value": true,
      "site": "00aea604",
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
      "definition_site": "00b4a394",
      "incomplete_value": false,
      "site": "00b4a39c",
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
            "const:c36:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea610",
      "incomplete_value": false,
      "site": "00aea618",
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
            "const:172:8"
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
      "00b4a384",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a394",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00b4a3a4",
      "WRITE",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a384",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a394",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4a3a4",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea5f0.md#insn-00aea618) · [`00aea620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea5f0.md#insn-00aea620) · [`00aea5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea5f0.md#insn-00aea5fc)
- 新版 `00b4a39c`（命令位置の公開資料なし） · `00b4a3a4`（命令位置の公開資料なし） · `00b4a380`（命令位置の公開資料なし）

~~~diff
- 00aea618 ["INT_ADD", "register:40f0:8", ["const:aea618:8", "const:4:8"]]
- 00aea618 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a39c ["INT_ADD", "register:40f0:8", ["const:b4a39c:8", "const:4:8"]]
+ 00b4a39c ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea618 bytes 9ece0394
+ 00b4a39c bytes dd410494
- 00aea620 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00aea620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a3a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
+ 00b4a3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea620 bytes 60ea03f9
+ 00b4a3a4 bytes 604a03f9
- 00aea5fc ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4a380 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea5fc bytes b32d00d0
+ 00b4a380 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8f6c6173b5a6918fb37dda800004264"></a>

### [`00aea634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea634.md) → [`00b4a3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a3b8.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a3e8",
      "incomplete_value": true,
      "site": "00b4a3e8",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea664",
      "incomplete_value": true,
      "site": "00aea664",
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
            "const:7d0:8"
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
      "definition_site": "00b4a3cc",
      "incomplete_value": true,
      "site": "00b4a3cc",
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
      "definition_site": "00aea648",
      "incomplete_value": true,
      "site": "00aea648",
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
      "definition_site": "00b4a3d4",
      "incomplete_value": false,
      "site": "00b4a3e0",
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
            "const:c36:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea650",
      "incomplete_value": false,
      "site": "00aea65c",
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
            "const:172:8"
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
      "00b4a3c8",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a3d4",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00b4a3e8",
      "WRITE",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a3c8",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a3d4",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4a3e8",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea634.md#insn-00aea65c) · [`00aea664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea634.md#insn-00aea664) · [`00aea640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea634.md#insn-00aea640)
- 新版 `00b4a3e0`（命令位置の公開資料なし） · `00b4a3e8`（命令位置の公開資料なし） · `00b4a3c4`（命令位置の公開資料なし）

~~~diff
- 00aea65c ["INT_ADD", "register:40f0:8", ["const:aea65c:8", "const:4:8"]]
- 00aea65c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a3e0 ["INT_ADD", "register:40f0:8", ["const:b4a3e0:8", "const:4:8"]]
+ 00b4a3e0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea65c bytes 8dce0394
+ 00b4a3e0 bytes cc410494
- 00aea664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7d0:8"]]
- 00aea664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a3e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:690:8"]]
+ 00b4a3e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea664 bytes 60ea03f9
+ 00b4a3e8 bytes 604a03f9
- 00aea640 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4a3c4 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea640 bytes b32d00d0
+ 00b4a3c4 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f34795b312b6045658891d4fe93e1578"></a>

### [`00aea684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea684.md) → [`00b4a408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a408.md) _ZN8firebase4util4file15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4a490",
      "incomplete_value": true,
      "site": "00b4a490",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea70c",
      "incomplete_value": true,
      "site": "00aea70c",
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
            "const:7d8:8"
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
      "definition_site": "00b4a43c",
      "incomplete_value": true,
      "site": "00b4a448",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:690:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea6b8",
      "incomplete_value": true,
      "site": "00aea6c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
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
      "00b4a41c",
      "READ",
      [
        "storage",
        "010a07d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a43c",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a490",
      "WRITE",
      [
        "storage",
        "010a07d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a41c",
      "READ",
      [
        "storage",
        "01125698",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a43c",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a490",
      "WRITE",
      [
        "storage",
        "01125698",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea684.md#insn-00aea6c4) · [`00aea70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea684.md#insn-00aea70c) · [`00aea694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea684.md#insn-00aea694)
- 新版 `00b4a448`（命令位置の公開資料なし） · `00b4a490`（命令位置の公開資料なし） · `00b4a418`（命令位置の公開資料なし）

~~~diff
- 00aea6c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea6c4 ["INT_ADD", "register:40f0:8", ["const:aea6c4:8", "const:4:8"]]
- 00aea6c4 ["CALLIND", null, ["register:0:8"]]
+ 00b4a448 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a448 ["INT_ADD", "register:40f0:8", ["const:b4a448:8", "const:4:8"]]
+ 00b4a448 ["CALLIND", null, ["register:0:8"]]
- 00aea6c4 bytes 00013fd6
+ 00b4a448 bytes 00013fd6
- 00aea70c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aea70c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7d8:8"]]
- 00aea70c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4a490 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4a490 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:698:8"]]
+ 00b4a490 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aea70c bytes a0621f39
+ 00b4a490 bytes a0621a39
- 00aea694 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4a418 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00aea694 bytes b52d00d0
+ 00b4a418 bytes d52e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b54c8ddddc1c18bd8ed68e388866b32"></a>

### [`00aea720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea720.md) → [`00b4a4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a4a4.md) _ZN8firebase4util4file12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00b4a4e0",
      "incomplete_value": true,
      "site": "00b4a4e0",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea75c",
      "incomplete_value": true,
      "site": "00aea75c",
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
            "const:7d8:8"
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
      "definition_site": "00b4a530",
      "incomplete_value": true,
      "site": "00b4a530",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea7ac",
      "incomplete_value": true,
      "site": "00aea7ac",
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
            "const:7d0:8"
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
      "definition_site": "00b4a4bc",
      "incomplete_value": true,
      "site": "00b4a4bc",
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
      "definition_site": "00aea738",
      "incomplete_value": true,
      "site": "00aea738",
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
      "00b4a4b8",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a4c4",
      "READ",
      [
        "storage",
        "010a07d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a4e0",
      "WRITE",
      [
        "storage",
        "010a07d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a4b8",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a4c4",
      "READ",
      [
        "storage",
        "01125698",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a4e0",
      "WRITE",
      [
        "storage",
        "01125698",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea720.md#insn-00aea75c) · [`00aea7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea720.md#insn-00aea7a8) · [`00aea7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea720.md#insn-00aea7ac)
- 新版 `00b4a4e0`（命令位置の公開資料なし） · `00b4a52c`（命令位置の公開資料なし） · `00b4a530`（命令位置の公開資料なし）

~~~diff
- 00aea75c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aea75c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aea75c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7d8:8"]]
- 00aea75c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a4e0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a4e0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a4e0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:698:8"]]
+ 00b4a4e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aea75c bytes bf621f39
+ 00b4a4e0 bytes bf621a39
- 00aea7a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aea7a8 ["INT_ADD", "register:40f0:8", ["const:aea7a8:8", "const:4:8"]]
- 00aea7a8 ["CALLIND", null, ["register:0:8"]]
+ 00b4a52c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a52c ["INT_ADD", "register:40f0:8", ["const:b4a52c:8", "const:4:8"]]
+ 00b4a52c ["CALLIND", null, ["register:0:8"]]
- 00aea7a8 bytes 00013fd6
+ 00b4a52c bytes 00013fd6
- 00aea7ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00aea7ac ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aea7ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a530 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:690:8"]]
+ 00b4a530 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a530 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aea7ac bytes 9fea03f9
+ 00b4a530 bytes 9f4a03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b697cce2bbe3bab2b9df74ad22bc7aa2"></a>

### [`00aea7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea7c0.md) → [`00b4a544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a544.md) _ZN8firebase4util4file14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a584",
      "incomplete_value": true,
      "site": "00b4a584",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea800",
      "incomplete_value": true,
      "site": "00aea800",
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
            "const:7d0:8"
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
      "definition_site": "00b4a560",
      "incomplete_value": true,
      "site": "00b4a560",
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
      "definition_site": "00aea7dc",
      "incomplete_value": true,
      "site": "00aea7dc",
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
      "definition_site": "00b4a568",
      "incomplete_value": false,
      "site": "00b4a57c",
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
            "const:c36:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea7e4",
      "incomplete_value": false,
      "site": "00aea7f8",
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
            "const:172:8"
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
      "00b4a558",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a568",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00b4a584",
      "WRITE",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a558",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a568",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4a584",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea7c0.md#insn-00aea7f8) · [`00aea800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea7c0.md#insn-00aea800) · [`00aea7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea7c0.md#insn-00aea7cc)
- 新版 `00b4a57c`（命令位置の公開資料なし） · `00b4a584`（命令位置の公開資料なし） · `00b4a550`（命令位置の公開資料なし）

~~~diff
- 00aea7f8 ["INT_ADD", "register:40f0:8", ["const:aea7f8:8", "const:4:8"]]
- 00aea7f8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a57c ["INT_ADD", "register:40f0:8", ["const:b4a57c:8", "const:4:8"]]
+ 00b4a57c ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea7f8 bytes 26ce0394
+ 00b4a57c bytes 65410494
- 00aea800 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00aea800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a584 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:690:8"]]
+ 00b4a584 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea800 bytes 80ea03f9
+ 00b4a584 bytes 804a03f9
- 00aea7cc ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4a550 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aea7cc bytes b42d00d0
+ 00b4a550 bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a3843971b525656b3a7075fedc633eb"></a>

### [`00aea830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea830.md) → [`00b4a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a5b4.md) _ZN8firebase4util4file11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde690.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b110.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b4a5d0",
      "incomplete_value": false,
      "site": "00b4a5d4",
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
      "definition_site": "00aea84c",
      "incomplete_value": false,
      "site": "00aea850",
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
      "definition_site": "00b4a5e0",
      "incomplete_value": true,
      "site": "00b4a5ec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea85c",
      "incomplete_value": true,
      "site": "00aea868",
      "value": [
        "LOAD",
        "8",
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
      "00b4a5d0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4a5e0",
      "DATA",
      [
        "storage",
        "010a07e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a5d0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4a5e0",
      "DATA",
      [
        "storage",
        "011256a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea830.md#insn-00aea850) · [`00aea848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea830.md#insn-00aea848) · [`00aea84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea830.md#insn-00aea84c)
- 新版 `00b4a5d4`（命令位置の公開資料なし） · `00b4a5cc`（命令位置の公開資料なし） · `00b4a5d0`（命令位置の公開資料なし）

~~~diff
- 00aea850 ["INT_ADD", "register:40f0:8", ["const:aea850:8", "const:4:8"]]
- 00aea850 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4a5d4 ["INT_ADD", "register:40f0:8", ["const:b4a5d4:8", "const:4:8"]]
+ 00b4a5d4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aea850 bytes 4cce0394
+ 00b4a5d4 bytes 8b410494
- 00aea848 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4a5cc ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aea848 bytes 60bdffd0
+ 00b4a5cc bytes e0baffd0
- 00aea84c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aea84c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea84c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea84c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a5d0 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4a5d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a5d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a5d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea84c bytes 001c1591
+ 00b4a5d0 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84ecdabd7438474d2719ecea1afa3379"></a>

### [`00aea86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea86c.md) → [`00b4a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a5f0.md) _ZN8firebase4util4file13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a630",
      "incomplete_value": true,
      "site": "00b4a630",
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
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea8ac",
      "incomplete_value": true,
      "site": "00aea8ac",
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
            "const:7d0:8"
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
      "definition_site": "00b4a60c",
      "incomplete_value": true,
      "site": "00b4a60c",
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
      "definition_site": "00aea888",
      "incomplete_value": true,
      "site": "00aea888",
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
      "definition_site": "00b4a614",
      "incomplete_value": false,
      "site": "00b4a628",
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
            "const:c36:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea890",
      "incomplete_value": false,
      "site": "00aea8a4",
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
            "const:172:8"
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
      "00b4a604",
      "READ",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a614",
      "PARAM",
      [
        "storage",
        "002a6172",
        null,
        "string"
      ]
    ],
    [
      "00b4a630",
      "WRITE",
      [
        "storage",
        "010a07d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a604",
      "READ",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a614",
      "PARAM",
      [
        "storage",
        "002b6c36",
        null,
        "string"
      ]
    ],
    [
      "00b4a630",
      "WRITE",
      [
        "storage",
        "01125690",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea86c.md#insn-00aea8a4) · [`00aea8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea86c.md#insn-00aea8ac) · [`00aea878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea86c.md#insn-00aea878)
- 新版 `00b4a628`（命令位置の公開資料なし） · `00b4a630`（命令位置の公開資料なし） · `00b4a5fc`（命令位置の公開資料なし）

~~~diff
- 00aea8a4 ["INT_ADD", "register:40f0:8", ["const:aea8a4:8", "const:4:8"]]
- 00aea8a4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a628 ["INT_ADD", "register:40f0:8", ["const:b4a628:8", "const:4:8"]]
+ 00b4a628 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea8a4 bytes fbcd0394
+ 00b4a628 bytes 3a410494
- 00aea8ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7d0:8"]]
- 00aea8ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a630 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:690:8"]]
+ 00b4a630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea8ac bytes 80ea03f9
+ 00b4a630 bytes 804a03f9
- 00aea878 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4a5fc ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aea878 bytes b42d00d0
+ 00b4a5fc bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15b03090b3bfafe39dec0439f8d40b5e"></a>

### [`00aea8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea8dc.md) → [`00b4a660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a660.md) _ZN8firebase4util4file10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a67c",
      "incomplete_value": false,
      "site": "00b4a680",
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
      "definition_site": "00aea8f8",
      "incomplete_value": false,
      "site": "00aea8fc",
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
      "definition_site": "00b4a68c",
      "incomplete_value": true,
      "site": "00b4a698",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aea908",
      "incomplete_value": true,
      "site": "00aea914",
      "value": [
        "LOAD",
        "8",
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
      "00b4a67c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4a68c",
      "DATA",
      [
        "storage",
        "010a0820",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a67c",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4a68c",
      "DATA",
      [
        "storage",
        "011256e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea8dc.md#insn-00aea8fc) · [`00aea8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea8dc.md#insn-00aea8f4) · [`00aea8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea8dc.md#insn-00aea8f8)
- 新版 `00b4a680`（命令位置の公開資料なし） · `00b4a678`（命令位置の公開資料なし） · `00b4a67c`（命令位置の公開資料なし）

~~~diff
- 00aea8fc ["INT_ADD", "register:40f0:8", ["const:aea8fc:8", "const:4:8"]]
- 00aea8fc ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4a680 ["INT_ADD", "register:40f0:8", ["const:b4a680:8", "const:4:8"]]
+ 00b4a680 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aea8fc bytes 21ce0394
+ 00b4a680 bytes 60410494
- 00aea8f4 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4a678 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aea8f4 bytes 60bdfff0
+ 00b4a678 bytes e0bafff0
- 00aea8f8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aea8f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aea8f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aea8f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a67c ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4a67c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a67c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a67c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aea8f8 bytes 00c81791
+ 00b4a67c bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff4a8c5e1d2244c132d27b0c315a38f1"></a>

### [`00aea918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea918.md) → [`00b4a69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a69c.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a6c8",
      "incomplete_value": true,
      "site": "00b4a6c8",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea944",
      "incomplete_value": true,
      "site": "00aea944",
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
            "const:828:8"
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
      "definition_site": "00b4a6b0",
      "incomplete_value": true,
      "site": "00b4a6b0",
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
      "definition_site": "00aea92c",
      "incomplete_value": true,
      "site": "00aea92c",
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
      "definition_site": "00b4a6bc",
      "incomplete_value": false,
      "site": "00b4a6c0",
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
            "const:4b3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea938",
      "incomplete_value": false,
      "site": "00aea93c",
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
            "const:654:8"
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
      "00b4a6ac",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a6bc",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00b4a6c8",
      "WRITE",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a6ac",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a6bc",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ],
    [
      "00b4a6c8",
      "WRITE",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea918.md#insn-00aea93c) · [`00aea944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea918.md#insn-00aea944) · [`00aea924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea918.md#insn-00aea924)
- 新版 `00b4a6c0`（命令位置の公開資料なし） · `00b4a6c8`（命令位置の公開資料なし） · `00b4a6a8`（命令位置の公開資料なし）

~~~diff
- 00aea93c ["INT_ADD", "register:40f0:8", ["const:aea93c:8", "const:4:8"]]
- 00aea93c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a6c0 ["INT_ADD", "register:40f0:8", ["const:b4a6c0:8", "const:4:8"]]
+ 00b4a6c0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea93c bytes d5cd0394
+ 00b4a6c0 bytes 14410494
- 00aea944 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00aea944 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a6c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b4a6c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea944 bytes 601604f9
+ 00b4a6c8 bytes 607603f9
- 00aea924 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4a6a8 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea924 bytes b32d00d0
+ 00b4a6a8 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf7571493b01dfbac81bbf32c13c6d25"></a>

### [`00aea958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea958.md) → [`00b4a6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a6dc.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a708",
      "incomplete_value": true,
      "site": "00b4a708",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea984",
      "incomplete_value": true,
      "site": "00aea984",
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
            "const:828:8"
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
      "definition_site": "00b4a6f0",
      "incomplete_value": true,
      "site": "00b4a6f0",
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
      "definition_site": "00aea96c",
      "incomplete_value": true,
      "site": "00aea96c",
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
      "definition_site": "00b4a6f8",
      "incomplete_value": false,
      "site": "00b4a700",
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
            "const:4b3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea974",
      "incomplete_value": false,
      "site": "00aea97c",
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
            "const:654:8"
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
      "00b4a6ec",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a6f8",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00b4a708",
      "WRITE",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a6ec",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a6f8",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ],
    [
      "00b4a708",
      "WRITE",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea958.md#insn-00aea97c) · [`00aea984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea958.md#insn-00aea984) · [`00aea964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea958.md#insn-00aea964)
- 新版 `00b4a700`（命令位置の公開資料なし） · `00b4a708`（命令位置の公開資料なし） · `00b4a6e8`（命令位置の公開資料なし）

~~~diff
- 00aea97c ["INT_ADD", "register:40f0:8", ["const:aea97c:8", "const:4:8"]]
- 00aea97c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a700 ["INT_ADD", "register:40f0:8", ["const:b4a700:8", "const:4:8"]]
+ 00b4a700 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea97c bytes c5cd0394
+ 00b4a700 bytes 04410494
- 00aea984 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00aea984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b4a708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea984 bytes 601604f9
+ 00b4a708 bytes 607603f9
- 00aea964 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4a6e8 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea964 bytes b32d00d0
+ 00b4a6e8 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67b8055460a732eb66029d3ab364a567"></a>

### [`00aea998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea998.md) → [`00b4a71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a71c.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a74c",
      "incomplete_value": true,
      "site": "00b4a74c",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea9c8",
      "incomplete_value": true,
      "site": "00aea9c8",
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
            "const:828:8"
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
      "definition_site": "00b4a730",
      "incomplete_value": true,
      "site": "00b4a730",
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
      "definition_site": "00aea9ac",
      "incomplete_value": true,
      "site": "00aea9ac",
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
      "definition_site": "00b4a73c",
      "incomplete_value": false,
      "site": "00b4a744",
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
            "const:4b3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea9b8",
      "incomplete_value": false,
      "site": "00aea9c0",
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
            "const:654:8"
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
      "00b4a72c",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a73c",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00b4a74c",
      "WRITE",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a72c",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a73c",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ],
    [
      "00b4a74c",
      "WRITE",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea998.md#insn-00aea9c0) · [`00aea9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea998.md#insn-00aea9c8) · [`00aea9a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea998.md#insn-00aea9a4)
- 新版 `00b4a744`（命令位置の公開資料なし） · `00b4a74c`（命令位置の公開資料なし） · `00b4a728`（命令位置の公開資料なし）

~~~diff
- 00aea9c0 ["INT_ADD", "register:40f0:8", ["const:aea9c0:8", "const:4:8"]]
- 00aea9c0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a744 ["INT_ADD", "register:40f0:8", ["const:b4a744:8", "const:4:8"]]
+ 00b4a744 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aea9c0 bytes b4cd0394
+ 00b4a744 bytes f3400494
- 00aea9c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00aea9c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a74c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b4a74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea9c8 bytes 601604f9
+ 00b4a74c bytes 607603f9
- 00aea9a4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4a728 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea9a4 bytes b32d00d0
+ 00b4a728 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9ab7d46cbae34ee8b165af51e003ba3"></a>

### [`00aea9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea9dc.md) → [`00b4a760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a760.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a790",
      "incomplete_value": true,
      "site": "00b4a790",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaa0c",
      "incomplete_value": true,
      "site": "00aeaa0c",
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
            "const:828:8"
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
      "definition_site": "00b4a774",
      "incomplete_value": true,
      "site": "00b4a774",
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
      "definition_site": "00aea9f0",
      "incomplete_value": true,
      "site": "00aea9f0",
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
      "definition_site": "00b4a77c",
      "incomplete_value": false,
      "site": "00b4a788",
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
            "const:4b3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea9f8",
      "incomplete_value": false,
      "site": "00aeaa04",
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
            "const:654:8"
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
      "00b4a770",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a77c",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00b4a790",
      "WRITE",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a770",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a77c",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ],
    [
      "00b4a790",
      "WRITE",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaa04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea9dc.md#insn-00aeaa04) · [`00aeaa0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea9dc.md#insn-00aeaa0c) · [`00aea9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea9dc.md#insn-00aea9e8)
- 新版 `00b4a788`（命令位置の公開資料なし） · `00b4a790`（命令位置の公開資料なし） · `00b4a76c`（命令位置の公開資料なし）

~~~diff
- 00aeaa04 ["INT_ADD", "register:40f0:8", ["const:aeaa04:8", "const:4:8"]]
- 00aeaa04 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a788 ["INT_ADD", "register:40f0:8", ["const:b4a788:8", "const:4:8"]]
+ 00b4a788 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeaa04 bytes a3cd0394
+ 00b4a788 bytes e2400494
- 00aeaa0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00aeaa0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a790 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e8:8"]]
+ 00b4a790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeaa0c bytes 601604f9
+ 00b4a790 bytes 607603f9
- 00aea9e8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4a76c ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aea9e8 bytes b32d00d0
+ 00b4a76c bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0688458f327ce364d8eaf631df2df48b"></a>

### [`00aeaa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaa2c.md) → [`00b4a7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a7b0.md) _ZN8firebase4util11float_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 50.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4a838",
      "incomplete_value": true,
      "site": "00b4a838",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaab4",
      "incomplete_value": true,
      "site": "00aeaab4",
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
            "const:830:8"
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
      "definition_site": "00b4a7e4",
      "incomplete_value": true,
      "site": "00b4a7f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:6e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaa60",
      "incomplete_value": true,
      "site": "00aeaa6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
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
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeaa80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a7c4",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aeaa60",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a838",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a7c4",
      "READ",
      [
        "storage",
        "011256f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a7e4",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a838",
      "WRITE",
      [
        "storage",
        "011256f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaa6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaa2c.md#insn-00aeaa6c) · [`00aeaa80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaa2c.md#insn-00aeaa80) · [`00aeaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaa2c.md#insn-00aeaab4)
- 新版 `00b4a7f0`（命令位置の公開資料なし） · `00b4a838`（命令位置の公開資料なし）

~~~diff
- 00aeaa6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeaa6c ["INT_ADD", "register:40f0:8", ["const:aeaa6c:8", "const:4:8"]]
- 00aeaa6c ["CALLIND", null, ["register:0:8"]]
+ 00b4a7f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a7f0 ["INT_ADD", "register:40f0:8", ["const:b4a7f0:8", "const:4:8"]]
+ 00b4a7f0 ["CALLIND", null, ["register:0:8"]]
- 00aeaa6c bytes 00013fd6
+ 00b4a7f0 bytes 00013fd6
- 00aeaa80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeaa80 ["INT_ADD", "register:40f0:8", ["const:aeaa80:8", "const:4:8"]]
- 00aeaa80 ["CALLIND", null, ["register:0:8"]]
- 00aeaa80 bytes 00013fd6
- 00aeaab4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeaab4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:830:8"]]
- 00aeaab4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4a838 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4a838 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6f0:8"]]
+ 00b4a838 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeaab4 bytes a0c22039
+ 00b4a838 bytes a0c21b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f932becfd2c2fac084861805b1ea4e44"></a>

### [`00aeaac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaac8.md) → [`00b4a84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a84c.md) _ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00b4a888",
      "incomplete_value": true,
      "site": "00b4a888",
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
            "const:6f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeab04",
      "incomplete_value": true,
      "site": "00aeab04",
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
            "const:830:8"
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
      "definition_site": "00b4a8d8",
      "incomplete_value": true,
      "site": "00b4a8d8",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeab54",
      "incomplete_value": true,
      "site": "00aeab54",
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
            "const:828:8"
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
      "definition_site": "00b4a864",
      "incomplete_value": true,
      "site": "00b4a864",
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
      "definition_site": "00aeaae0",
      "incomplete_value": true,
      "site": "00aeaae0",
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
      "00b4a860",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a86c",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a888",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a860",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a86c",
      "READ",
      [
        "storage",
        "011256f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a888",
      "WRITE",
      [
        "storage",
        "011256f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeab04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaac8.md#insn-00aeab04) · [`00aeab50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaac8.md#insn-00aeab50) · [`00aeab54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaac8.md#insn-00aeab54)
- 新版 `00b4a888`（命令位置の公開資料なし） · `00b4a8d4`（命令位置の公開資料なし） · `00b4a8d8`（命令位置の公開資料なし）

~~~diff
- 00aeab04 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeab04 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeab04 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:830:8"]]
- 00aeab04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a888 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a888 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a888 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6f0:8"]]
+ 00b4a888 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeab04 bytes bfc22039
+ 00b4a888 bytes bfc21b39
- 00aeab50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeab50 ["INT_ADD", "register:40f0:8", ["const:aeab50:8", "const:4:8"]]
- 00aeab50 ["CALLIND", null, ["register:0:8"]]
+ 00b4a8d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a8d4 ["INT_ADD", "register:40f0:8", ["const:b4a8d4:8", "const:4:8"]]
+ 00b4a8d4 ["CALLIND", null, ["register:0:8"]]
- 00aeab50 bytes 00013fd6
+ 00b4a8d4 bytes 00013fd6
- 00aeab54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00aeab54 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aeab54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a8d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00b4a8d8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a8d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aeab54 bytes 9f1604f9
+ 00b4a8d8 bytes 9f7603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23aa201db6e793c9711b445897398aef"></a>

### [`00aeab68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeab68.md) → [`00b4a8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a8ec.md) _ZN8firebase4util11float_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00aeaba8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4a92c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeab84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeab7c",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aeab84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4a930"
      ]
    ],
    [
      "unmatched:00aeab8c",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4a900",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a908",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4a930"
      ]
    ],
    [
      "00b4a910",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeab84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeab68.md#insn-00aeab84) · [`00aeaba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeab68.md#insn-00aeaba0) · [`00aeaba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeab68.md#insn-00aeaba8)
- 新版 `00b4a924`（命令位置の公開資料なし）

~~~diff
- 00aeab84 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeab84 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeab84 bytes 410100b5
- 00aeaba0 ["INT_ADD", "register:40f0:8", ["const:aeaba0:8", "const:4:8"]]
- 00aeaba0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a924 ["INT_ADD", "register:40f0:8", ["const:b4a924:8", "const:4:8"]]
+ 00b4a924 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeaba0 bytes 3ccd0394
+ 00b4a924 bytes 7b400494
- 00aeaba8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00aeaba8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeaba8 bytes 801604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6813c4e5dce56b41b032c8495df4470b"></a>

### [`00aeabd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeabd8.md) → [`00b4a95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a95c.md) _ZN8firebase4util11float_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a978",
      "incomplete_value": false,
      "site": "00b4a97c",
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
      "definition_site": "00aeabf4",
      "incomplete_value": false,
      "site": "00aeabf8",
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
      "definition_site": "00b4a988",
      "incomplete_value": true,
      "site": "00b4a994",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeac04",
      "incomplete_value": true,
      "site": "00aeac10",
      "value": [
        "LOAD",
        "8",
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
      "00b4a978",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4a988",
      "DATA",
      [
        "storage",
        "010a0838",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a978",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4a988",
      "DATA",
      [
        "storage",
        "011256f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeabf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeabd8.md#insn-00aeabf8) · [`00aeabf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeabd8.md#insn-00aeabf0) · [`00aeabf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeabd8.md#insn-00aeabf4)
- 新版 `00b4a97c`（命令位置の公開資料なし） · `00b4a974`（命令位置の公開資料なし） · `00b4a978`（命令位置の公開資料なし）

~~~diff
- 00aeabf8 ["INT_ADD", "register:40f0:8", ["const:aeabf8:8", "const:4:8"]]
- 00aeabf8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4a97c ["INT_ADD", "register:40f0:8", ["const:b4a97c:8", "const:4:8"]]
+ 00b4a97c ["CALL", null, ["callee:00c5ac00:8"]]
- 00aeabf8 bytes 62cd0394
+ 00b4a97c bytes a1400494
- 00aeabf0 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4a974 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aeabf0 bytes 60bdffd0
+ 00b4a974 bytes e0baffd0
- 00aeabf4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aeabf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeabf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeabf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a978 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4a978 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a978 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a978 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeabf4 bytes 001c1591
+ 00b4a978 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea70be64459da52550ab57d7b025d868"></a>

### [`00aeac14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac14.md) → [`00b4a998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4a998.md) _ZN8firebase4util11float_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4a9d8",
      "incomplete_value": true,
      "site": "00b4a9d8",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeac54",
      "incomplete_value": true,
      "site": "00aeac54",
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
            "const:828:8"
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
      "definition_site": "00b4a9b4",
      "incomplete_value": true,
      "site": "00b4a9b4",
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
      "definition_site": "00aeac30",
      "incomplete_value": true,
      "site": "00aeac30",
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
      "definition_site": "00b4a9bc",
      "incomplete_value": false,
      "site": "00b4a9d0",
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
            "const:4b3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeac38",
      "incomplete_value": false,
      "site": "00aeac4c",
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
            "const:654:8"
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
      "00b4a9ac",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a9bc",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00b4a9d8",
      "WRITE",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a9ac",
      "READ",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a9bc",
      "PARAM",
      [
        "storage",
        "002a94b3",
        null,
        "string"
      ]
    ],
    [
      "00b4a9d8",
      "WRITE",
      [
        "storage",
        "011256e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeac4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac14.md#insn-00aeac4c) · [`00aeac54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac14.md#insn-00aeac54) · [`00aeac20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac14.md#insn-00aeac20)
- 新版 `00b4a9d0`（命令位置の公開資料なし） · `00b4a9d8`（命令位置の公開資料なし） · `00b4a9a4`（命令位置の公開資料なし）

~~~diff
- 00aeac4c ["INT_ADD", "register:40f0:8", ["const:aeac4c:8", "const:4:8"]]
- 00aeac4c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4a9d0 ["INT_ADD", "register:40f0:8", ["const:b4a9d0:8", "const:4:8"]]
+ 00b4a9d0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeac4c bytes 11cd0394
+ 00b4a9d0 bytes 50400494
- 00aeac54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00aeac54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a9d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e8:8"]]
+ 00b4a9d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeac54 bytes 801604f9
+ 00b4a9d8 bytes 807603f9
- 00aeac20 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4a9a4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aeac20 bytes b42d00d0
+ 00b4a9a4 bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-159f7172d18672e1d0f8aa9d81ad9693"></a>

### [`00aeac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac84.md) → [`00b4aa08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa08.md) _ZN8firebase4util11float_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4aa24",
      "incomplete_value": false,
      "site": "00b4aa28",
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
      "definition_site": "00aeaca0",
      "incomplete_value": false,
      "site": "00aeaca4",
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
      "definition_site": "00b4aa34",
      "incomplete_value": true,
      "site": "00b4aa40",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeacb0",
      "incomplete_value": true,
      "site": "00aeacbc",
      "value": [
        "LOAD",
        "8",
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
      "00b4aa24",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4aa34",
      "DATA",
      [
        "storage",
        "010a0848",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4aa24",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4aa34",
      "DATA",
      [
        "storage",
        "01125708",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac84.md#insn-00aeaca4) · [`00aeac9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac84.md#insn-00aeac9c) · [`00aeaca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac84.md#insn-00aeaca0)
- 新版 `00b4aa28`（命令位置の公開資料なし） · `00b4aa20`（命令位置の公開資料なし） · `00b4aa24`（命令位置の公開資料なし）

~~~diff
- 00aeaca4 ["INT_ADD", "register:40f0:8", ["const:aeaca4:8", "const:4:8"]]
- 00aeaca4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4aa28 ["INT_ADD", "register:40f0:8", ["const:b4aa28:8", "const:4:8"]]
+ 00b4aa28 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aeaca4 bytes 37cd0394
+ 00b4aa28 bytes 76400494
- 00aeac9c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4aa20 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aeac9c bytes 60bdfff0
+ 00b4aa20 bytes e0bafff0
- 00aeaca0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aeaca0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeaca0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeaca0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4aa24 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4aa24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4aa24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4aa24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeaca0 bytes 00c81791
+ 00b4aa24 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2f4307e68836c0922400c466cf6171c"></a>

### [`00aeacc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeacc0.md) → [`00b4aa44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa44.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4aa70",
      "incomplete_value": true,
      "site": "00b4aa70",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeacec",
      "incomplete_value": true,
      "site": "00aeacec",
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
            "const:850:8"
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
      "definition_site": "00b4aa58",
      "incomplete_value": true,
      "site": "00b4aa58",
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
      "definition_site": "00aeacd4",
      "incomplete_value": true,
      "site": "00aeacd4",
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
      "definition_site": "00b4aa64",
      "incomplete_value": false,
      "site": "00b4aa68",
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
            "const:70a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeace0",
      "incomplete_value": false,
      "site": "00aeace4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:bd5:8"
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
      "00b4aa54",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aa64",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00b4aa70",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aa54",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aa64",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ],
    [
      "00b4aa70",
      "WRITE",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeace4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeacc0.md#insn-00aeace4) · [`00aeacec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeacc0.md#insn-00aeacec) · [`00aeaccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeacc0.md#insn-00aeaccc)
- 新版 `00b4aa68`（命令位置の公開資料なし） · `00b4aa70`（命令位置の公開資料なし） · `00b4aa50`（命令位置の公開資料なし）

~~~diff
- 00aeace4 ["INT_ADD", "register:40f0:8", ["const:aeace4:8", "const:4:8"]]
- 00aeace4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4aa68 ["INT_ADD", "register:40f0:8", ["const:b4aa68:8", "const:4:8"]]
+ 00b4aa68 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeace4 bytes ebcc0394
+ 00b4aa68 bytes 2a400494
- 00aeacec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aeacec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4aa70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
+ 00b4aa70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeacec bytes 602a04f9
+ 00b4aa70 bytes 608a03f9
- 00aeaccc ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4aa50 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeaccc bytes b32d00d0
+ 00b4aa50 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fc99050dee72310bafc59e829675383"></a>

### [`00aead00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead00.md) → [`00b4aa84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aa84.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aead2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4aab0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4aa98",
      "incomplete_value": true,
      "site": "00b4aa98",
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
      "definition_site": "00aead14",
      "incomplete_value": true,
      "site": "00aead14",
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
      "00b4aa94",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aa98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aead30"
      ]
    ],
    [
      "unmatched:00aead1c",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4aa94",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aa98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4aab4"
      ]
    ],
    [
      "00b4aaa0",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aead24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead00.md#insn-00aead24) · [`00aead2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead00.md#insn-00aead2c) · [`00aead3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead00.md#insn-00aead3c)

~~~diff
- 00aead24 ["INT_ADD", "register:40f0:8", ["const:aead24:8", "const:4:8"]]
- 00aead24 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aead24 bytes dbcc0394
- 00aead2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aead2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aead2c bytes 602a04f9
- 00aead3c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aead3c ["RETURN", null, ["register:0:8"]]
- 00aead3c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fc3df39654eb9f866c0da85389323e0"></a>

### [`00aead40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead40.md) → [`00b4aac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aac4.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4aaf4",
      "incomplete_value": true,
      "site": "00b4aaf4",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aead70",
      "incomplete_value": true,
      "site": "00aead70",
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
            "const:850:8"
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
      "definition_site": "00b4aad8",
      "incomplete_value": true,
      "site": "00b4aad8",
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
      "definition_site": "00aead54",
      "incomplete_value": true,
      "site": "00aead54",
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
      "definition_site": "00b4aae4",
      "incomplete_value": false,
      "site": "00b4aaec",
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
            "const:70a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aead60",
      "incomplete_value": false,
      "site": "00aead68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:bd5:8"
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
      "00b4aad4",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aae4",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00b4aaf4",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aad4",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aae4",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ],
    [
      "00b4aaf4",
      "WRITE",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aead68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead40.md#insn-00aead68) · [`00aead70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead40.md#insn-00aead70) · [`00aead4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead40.md#insn-00aead4c)
- 新版 `00b4aaec`（命令位置の公開資料なし） · `00b4aaf4`（命令位置の公開資料なし） · `00b4aad0`（命令位置の公開資料なし）

~~~diff
- 00aead68 ["INT_ADD", "register:40f0:8", ["const:aead68:8", "const:4:8"]]
- 00aead68 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4aaec ["INT_ADD", "register:40f0:8", ["const:b4aaec:8", "const:4:8"]]
+ 00b4aaec ["CALL", null, ["callee:00c5ab10:8"]]
- 00aead68 bytes cacc0394
+ 00b4aaec bytes 09400494
- 00aead70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aead70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4aaf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
+ 00b4aaf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aead70 bytes 602a04f9
+ 00b4aaf4 bytes 608a03f9
- 00aead4c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4aad0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aead4c bytes b32d00d0
+ 00b4aad0 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-598a392b61eece5db40792e639eeba89"></a>

### [`00aead84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead84.md) → [`00b4ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ab08.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4ab38",
      "incomplete_value": true,
      "site": "00b4ab38",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeadb4",
      "incomplete_value": true,
      "site": "00aeadb4",
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
            "const:850:8"
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
      "definition_site": "00b4ab1c",
      "incomplete_value": true,
      "site": "00b4ab1c",
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
      "definition_site": "00aead98",
      "incomplete_value": true,
      "site": "00aead98",
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
      "definition_site": "00b4ab24",
      "incomplete_value": false,
      "site": "00b4ab30",
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
            "const:70a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeada0",
      "incomplete_value": false,
      "site": "00aeadac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:bd5:8"
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
      "00b4ab18",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab24",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00b4ab38",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ab18",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab24",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ],
    [
      "00b4ab38",
      "WRITE",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeadac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead84.md#insn-00aeadac) · [`00aeadb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead84.md#insn-00aeadb4) · [`00aead90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead84.md#insn-00aead90)
- 新版 `00b4ab30`（命令位置の公開資料なし） · `00b4ab38`（命令位置の公開資料なし） · `00b4ab14`（命令位置の公開資料なし）

~~~diff
- 00aeadac ["INT_ADD", "register:40f0:8", ["const:aeadac:8", "const:4:8"]]
- 00aeadac ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4ab30 ["INT_ADD", "register:40f0:8", ["const:b4ab30:8", "const:4:8"]]
+ 00b4ab30 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeadac bytes b9cc0394
+ 00b4ab30 bytes f83f0494
- 00aeadb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aeadb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ab38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:710:8"]]
+ 00b4ab38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeadb4 bytes 602a04f9
+ 00b4ab38 bytes 608a03f9
- 00aead90 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4ab14 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aead90 bytes b32d00d0
+ 00b4ab14 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1845a3bad0e2d40fd46cb4cb7ede8548"></a>

### [`00aeadd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeadd4.md) → [`00b4ab58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ab58.md) _ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 50.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4abe0",
      "incomplete_value": true,
      "site": "00b4abe0",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeae5c",
      "incomplete_value": true,
      "site": "00aeae5c",
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
            "const:858:8"
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
      "site": "00aeae14"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4ab98"
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
      "00b4ab6c",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aeae08",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4abe0",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ab6c",
      "READ",
      [
        "storage",
        "01125718",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ab8c",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4abe0",
      "WRITE",
      [
        "storage",
        "01125718",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeae14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeadd4.md#insn-00aeae14) · [`00aeae5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeadd4.md#insn-00aeae5c)
- 新版 `00b4abe0`（命令位置の公開資料なし） · `00b4ab98`（命令位置の公開資料なし）

~~~diff
- 00aeae14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeae14 ["INT_ADD", "register:40f0:8", ["const:aeae14:8", "const:4:8"]]
- 00aeae14 ["CALLIND", null, ["register:0:8"]]
- 00aeae14 bytes 00013fd6
- 00aeae5c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeae5c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:858:8"]]
- 00aeae5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4abe0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4abe0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:718:8"]]
+ 00b4abe0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeae5c bytes a0622139
+ 00b4abe0 bytes a0621c39
+ 00b4ab98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4ab98 ["INT_ADD", "register:40f0:8", ["const:b4ab98:8", "const:4:8"]]
+ 00b4ab98 ["CALLIND", null, ["register:0:8"]]
+ 00b4ab98 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86f20c5ae75b3315dc426d024afc10b7"></a>

### [`00aeae70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeae70.md) → [`00b4abf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4abf4.md) _ZN8firebase4util8hash_map12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 66.67% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ac30",
      "incomplete_value": true,
      "site": "00b4ac30",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaeac",
      "incomplete_value": true,
      "site": "00aeaeac",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeaefc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4ac80"
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
      "00b4ac08",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac14",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ac30",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ac08",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac14",
      "READ",
      [
        "storage",
        "01125718",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ac30",
      "WRITE",
      [
        "storage",
        "01125718",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeae88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeae70.md#insn-00aeae88) · [`00aeaeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeae70.md#insn-00aeaeac) · [`00aeaef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeae70.md#insn-00aeaef8)
- 新版 `00b4ac0c`（命令位置の公開資料なし） · `00b4ac30`（命令位置の公開資料なし）

~~~diff
- 00aeae88 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeae88 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b4ac0c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4ac0c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00aeae88 bytes c10300b4
+ 00b4ac0c bytes c10300b4
- 00aeaeac ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeaeac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeaeac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:858:8"]]
- 00aeaeac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4ac30 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4ac30 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4ac30 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:718:8"]]
+ 00b4ac30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeaeac bytes bf622139
+ 00b4ac30 bytes bf621c39
- 00aeaef8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeaef8 ["INT_ADD", "register:40f0:8", ["const:aeaef8:8", "const:4:8"]]
- 00aeaef8 ["CALLIND", null, ["register:0:8"]]
- 00aeaef8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3e4de4c183d98bdffebaa7a37fb889c"></a>

### [`00aeaf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf10.md) → [`00b4ac94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ac94.md) _ZN8firebase4util8hash_map14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "site": "00aeaf50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4acd4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeaf2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeaf24",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aeaf2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4acd8"
      ]
    ],
    [
      "unmatched:00aeaf34",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4aca8",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4acb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4acd8"
      ]
    ],
    [
      "00b4acb8",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf10.md#insn-00aeaf2c) · [`00aeaf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf10.md#insn-00aeaf48) · [`00aeaf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf10.md#insn-00aeaf50)
- 新版 `00b4accc`（命令位置の公開資料なし）

~~~diff
- 00aeaf2c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeaf2c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeaf2c bytes 410100b5
- 00aeaf48 ["INT_ADD", "register:40f0:8", ["const:aeaf48:8", "const:4:8"]]
- 00aeaf48 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4accc ["INT_ADD", "register:40f0:8", ["const:b4accc:8", "const:4:8"]]
+ 00b4accc ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeaf48 bytes 52cc0394
+ 00b4accc bytes 913f0494
- 00aeaf50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
- 00aeaf50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeaf50 bytes 802a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b82adb7d94218b4028f324cb3a75f7a0"></a>

### [`00aeaf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf80.md) → [`00b4ad04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ad04.md) _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde130.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5abb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5abb0.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b4ad20",
      "incomplete_value": false,
      "site": "00b4ad24",
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
      "definition_site": "00aeaf9c",
      "incomplete_value": false,
      "site": "00aeafa0",
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
      "definition_site": "00b4ad30",
      "incomplete_value": true,
      "site": "00b4ad3c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeafac",
      "incomplete_value": true,
      "site": "00aeafb8",
      "value": [
        "LOAD",
        "8",
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
      "00b4ad20",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4ad30",
      "DATA",
      [
        "storage",
        "010a0860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ad20",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4ad30",
      "DATA",
      [
        "storage",
        "01125720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeafa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf80.md#insn-00aeafa0) · [`00aeaf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf80.md#insn-00aeaf98) · [`00aeaf9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf80.md#insn-00aeaf9c)
- 新版 `00b4ad24`（命令位置の公開資料なし） · `00b4ad1c`（命令位置の公開資料なし） · `00b4ad20`（命令位置の公開資料なし）

~~~diff
- 00aeafa0 ["INT_ADD", "register:40f0:8", ["const:aeafa0:8", "const:4:8"]]
- 00aeafa0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4ad24 ["INT_ADD", "register:40f0:8", ["const:b4ad24:8", "const:4:8"]]
+ 00b4ad24 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aeafa0 bytes 78cc0394
+ 00b4ad24 bytes b73f0494
- 00aeaf98 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4ad1c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aeaf98 bytes 60bdffd0
+ 00b4ad1c bytes e0baffd0
- 00aeaf9c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aeaf9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeaf9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeaf9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ad20 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4ad20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ad20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ad20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeaf9c bytes 001c1591
+ 00b4ad20 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4d1fb77ce4e6e76735ef03f62544cf6"></a>

### [`00aeafbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeafbc.md) → [`00b4ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ad40.md) _ZN8firebase4util8hash_map13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4ad80",
      "incomplete_value": true,
      "site": "00b4ad80",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaffc",
      "incomplete_value": true,
      "site": "00aeaffc",
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
            "const:850:8"
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
      "definition_site": "00b4ad5c",
      "incomplete_value": true,
      "site": "00b4ad5c",
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
      "definition_site": "00aeafd8",
      "incomplete_value": true,
      "site": "00aeafd8",
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
      "definition_site": "00b4ad64",
      "incomplete_value": false,
      "site": "00b4ad78",
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
            "const:70a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeafe0",
      "incomplete_value": false,
      "site": "00aeaff4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:bd5:8"
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
      "00b4ad54",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad64",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00b4ad80",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ad54",
      "READ",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad64",
      "PARAM",
      [
        "storage",
        "002a670a",
        null,
        "string"
      ]
    ],
    [
      "00b4ad80",
      "WRITE",
      [
        "storage",
        "01125710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeafbc.md#insn-00aeaff4) · [`00aeaffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeafbc.md#insn-00aeaffc) · [`00aeafc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeafbc.md#insn-00aeafc8)
- 新版 `00b4ad78`（命令位置の公開資料なし） · `00b4ad80`（命令位置の公開資料なし） · `00b4ad4c`（命令位置の公開資料なし）

~~~diff
- 00aeaff4 ["INT_ADD", "register:40f0:8", ["const:aeaff4:8", "const:4:8"]]
- 00aeaff4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4ad78 ["INT_ADD", "register:40f0:8", ["const:b4ad78:8", "const:4:8"]]
+ 00b4ad78 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeaff4 bytes 27cc0394
+ 00b4ad78 bytes 663f0494
- 00aeaffc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
- 00aeaffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ad80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:710:8"]]
+ 00b4ad80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeaffc bytes 802a04f9
+ 00b4ad80 bytes 808a03f9
- 00aeafc8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4ad4c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aeafc8 bytes b42d00d0
+ 00b4ad4c bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ad835a43bf2779d9696dca5227551e1"></a>

### [`00aeb02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb02c.md) → [`00b4adb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4adb0.md) _ZN8firebase4util8hash_map10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4adcc",
      "incomplete_value": false,
      "site": "00b4add0",
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
      "definition_site": "00aeb048",
      "incomplete_value": false,
      "site": "00aeb04c",
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
      "definition_site": "00b4addc",
      "incomplete_value": true,
      "site": "00b4ade8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeb058",
      "incomplete_value": true,
      "site": "00aeb064",
      "value": [
        "LOAD",
        "8",
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
      "00b4adcc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4addc",
      "DATA",
      [
        "storage",
        "010a0868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4adcc",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4addc",
      "DATA",
      [
        "storage",
        "01125728",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb04c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb02c.md#insn-00aeb04c) · [`00aeb044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb02c.md#insn-00aeb044) · [`00aeb048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb02c.md#insn-00aeb048)
- 新版 `00b4add0`（命令位置の公開資料なし） · `00b4adc8`（命令位置の公開資料なし） · `00b4adcc`（命令位置の公開資料なし）

~~~diff
- 00aeb04c ["INT_ADD", "register:40f0:8", ["const:aeb04c:8", "const:4:8"]]
- 00aeb04c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4add0 ["INT_ADD", "register:40f0:8", ["const:b4add0:8", "const:4:8"]]
+ 00b4add0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aeb04c bytes 4dcc0394
+ 00b4add0 bytes 8c3f0494
- 00aeb044 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4adc8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aeb044 bytes 60bdffd0
+ 00b4adc8 bytes e0bafff0
- 00aeb048 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aeb048 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb048 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb048 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4adcc ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4adcc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4adcc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4adcc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeb048 bytes 00c81791
+ 00b4adcc bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-535e77f32ffb00fdfa3c636f731a58b7"></a>

### [`00aeb068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb068.md) → [`00b4adec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4adec.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4ae18",
      "incomplete_value": true,
      "site": "00b4ae18",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb094",
      "incomplete_value": true,
      "site": "00aeb094",
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
            "const:870:8"
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
      "definition_site": "00b4ae00",
      "incomplete_value": true,
      "site": "00b4ae00",
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
      "definition_site": "00aeb07c",
      "incomplete_value": true,
      "site": "00aeb07c",
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
      "definition_site": "00b4ae0c",
      "incomplete_value": false,
      "site": "00b4ae10",
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
            "const:365:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb088",
      "incomplete_value": false,
      "site": "00aeb08c",
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
            "const:612:8"
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
      "00b4adfc",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae0c",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00b4ae18",
      "WRITE",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4adfc",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae0c",
      "PARAM",
      [
        "storage",
        "002a8365",
        null,
        "string"
      ]
    ],
    [
      "00b4ae18",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb068.md#insn-00aeb08c) · [`00aeb094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb068.md#insn-00aeb094) · [`00aeb074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb068.md#insn-00aeb074)
- 新版 `00b4ae10`（命令位置の公開資料なし） · `00b4ae18`（命令位置の公開資料なし） · `00b4adf8`（命令位置の公開資料なし）

~~~diff
- 00aeb08c ["INT_ADD", "register:40f0:8", ["const:aeb08c:8", "const:4:8"]]
- 00aeb08c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4ae10 ["INT_ADD", "register:40f0:8", ["const:b4ae10:8", "const:4:8"]]
+ 00b4ae10 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb08c bytes 01cc0394
+ 00b4ae10 bytes 403f0494
- 00aeb094 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
- 00aeb094 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ae18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:730:8"]]
+ 00b4ae18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb094 bytes 603a04f9
+ 00b4ae18 bytes 609a03f9
- 00aeb074 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4adf8 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeb074 bytes b32d00b0
+ 00b4adf8 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f06c0cd72bb4546ab154e66ce9fafe9"></a>

### [`00aeb0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0a8.md) → [`00b4ae2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ae2c.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4ae58",
      "incomplete_value": true,
      "site": "00b4ae58",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb0d4",
      "incomplete_value": true,
      "site": "00aeb0d4",
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
            "const:870:8"
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
      "definition_site": "00b4ae40",
      "incomplete_value": true,
      "site": "00b4ae40",
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
      "definition_site": "00aeb0bc",
      "incomplete_value": true,
      "site": "00aeb0bc",
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
      "definition_site": "00b4ae48",
      "incomplete_value": false,
      "site": "00b4ae50",
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
            "const:365:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb0c4",
      "incomplete_value": false,
      "site": "00aeb0cc",
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
            "const:612:8"
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
      "00b4ae3c",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae48",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00b4ae58",
      "WRITE",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ae3c",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae48",
      "PARAM",
      [
        "storage",
        "002a8365",
        null,
        "string"
      ]
    ],
    [
      "00b4ae58",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0a8.md#insn-00aeb0cc) · [`00aeb0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0a8.md#insn-00aeb0d4) · [`00aeb0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0a8.md#insn-00aeb0b4)
- 新版 `00b4ae50`（命令位置の公開資料なし） · `00b4ae58`（命令位置の公開資料なし） · `00b4ae38`（命令位置の公開資料なし）

~~~diff
- 00aeb0cc ["INT_ADD", "register:40f0:8", ["const:aeb0cc:8", "const:4:8"]]
- 00aeb0cc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4ae50 ["INT_ADD", "register:40f0:8", ["const:b4ae50:8", "const:4:8"]]
+ 00b4ae50 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb0cc bytes f1cb0394
+ 00b4ae50 bytes 303f0494
- 00aeb0d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
- 00aeb0d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ae58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:730:8"]]
+ 00b4ae58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb0d4 bytes 603a04f9
+ 00b4ae58 bytes 609a03f9
- 00aeb0b4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4ae38 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeb0b4 bytes b32d00b0
+ 00b4ae38 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e943645b0dd5cc482e9e1f487156ded"></a>

### [`00aeb0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0e8.md) → [`00b4ae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4ae6c.md) _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4ae9c",
      "incomplete_value": true,
      "site": "00b4ae9c",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb118",
      "incomplete_value": true,
      "site": "00aeb118",
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
            "const:870:8"
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
      "definition_site": "00b4ae80",
      "incomplete_value": true,
      "site": "00b4ae80",
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
      "definition_site": "00aeb0fc",
      "incomplete_value": true,
      "site": "00aeb0fc",
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
      "definition_site": "00b4ae8c",
      "incomplete_value": false,
      "site": "00b4ae94",
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
            "const:365:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb108",
      "incomplete_value": false,
      "site": "00aeb110",
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
            "const:612:8"
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
      "00b4ae7c",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae8c",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00b4ae9c",
      "WRITE",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ae7c",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae8c",
      "PARAM",
      [
        "storage",
        "002a8365",
        null,
        "string"
      ]
    ],
    [
      "00b4ae9c",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0e8.md#insn-00aeb110) · [`00aeb118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0e8.md#insn-00aeb118) · [`00aeb0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0e8.md#insn-00aeb0f4)
- 新版 `00b4ae94`（命令位置の公開資料なし） · `00b4ae9c`（命令位置の公開資料なし） · `00b4ae78`（命令位置の公開資料なし）

~~~diff
- 00aeb110 ["INT_ADD", "register:40f0:8", ["const:aeb110:8", "const:4:8"]]
- 00aeb110 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4ae94 ["INT_ADD", "register:40f0:8", ["const:b4ae94:8", "const:4:8"]]
+ 00b4ae94 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb110 bytes e0cb0394
+ 00b4ae94 bytes 1f3f0494
- 00aeb118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
- 00aeb118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ae9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:730:8"]]
+ 00b4ae9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb118 bytes 603a04f9
+ 00b4ae9c bytes 609a03f9
- 00aeb0f4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4ae78 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeb0f4 bytes b32d00b0
+ 00b4ae78 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a07a8921acc3f348647a5755b64b7f17"></a>

### [`00aeb12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb12c.md) → [`00b4aeb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4aeb0.md) _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4aee0",
      "incomplete_value": true,
      "site": "00b4aee0",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb15c",
      "incomplete_value": true,
      "site": "00aeb15c",
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
            "const:870:8"
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
      "definition_site": "00b4aec4",
      "incomplete_value": true,
      "site": "00b4aec4",
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
      "definition_site": "00aeb140",
      "incomplete_value": true,
      "site": "00aeb140",
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
      "definition_site": "00b4aecc",
      "incomplete_value": false,
      "site": "00b4aed8",
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
            "const:365:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb148",
      "incomplete_value": false,
      "site": "00aeb154",
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
            "const:612:8"
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
      "00b4aec0",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aecc",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00b4aee0",
      "WRITE",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aec0",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aecc",
      "PARAM",
      [
        "storage",
        "002a8365",
        null,
        "string"
      ]
    ],
    [
      "00b4aee0",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb12c.md#insn-00aeb154) · [`00aeb15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb12c.md#insn-00aeb15c) · [`00aeb138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb12c.md#insn-00aeb138)
- 新版 `00b4aed8`（命令位置の公開資料なし） · `00b4aee0`（命令位置の公開資料なし） · `00b4aebc`（命令位置の公開資料なし）

~~~diff
- 00aeb154 ["INT_ADD", "register:40f0:8", ["const:aeb154:8", "const:4:8"]]
- 00aeb154 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4aed8 ["INT_ADD", "register:40f0:8", ["const:b4aed8:8", "const:4:8"]]
+ 00b4aed8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb154 bytes cfcb0394
+ 00b4aed8 bytes 0e3f0494
- 00aeb15c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
- 00aeb15c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4aee0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:730:8"]]
+ 00b4aee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb15c bytes 603a04f9
+ 00b4aee0 bytes 609a03f9
- 00aeb138 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4aebc ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeb138 bytes b32d00b0
+ 00b4aebc bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9466ab91849267d3dd51ae959102591"></a>

### [`00aeb17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb17c.md) → [`00b4af00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4af00.md) _ZN8firebase4util13integer_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4af88",
      "incomplete_value": true,
      "site": "00b4af88",
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
            "const:738:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb204",
      "incomplete_value": true,
      "site": "00aeb204",
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
            "const:878:8"
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
      "definition_site": "00b4af34",
      "incomplete_value": true,
      "site": "00b4af40",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:730:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb1b0",
      "incomplete_value": true,
      "site": "00aeb1bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:870:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb214"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4af14",
      "READ",
      [
        "storage",
        "010a0878",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4af20",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeb208"
      ]
    ],
    [
      "00b4af34",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4af14",
      "READ",
      [
        "storage",
        "01125738",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4af20",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4af8c"
      ]
    ],
    [
      "00b4af34",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb17c.md#insn-00aeb1bc) · [`00aeb204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb17c.md#insn-00aeb204) · [`00aeb214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb17c.md#insn-00aeb214)
- 新版 `00b4af40`（命令位置の公開資料なし） · `00b4af88`（命令位置の公開資料なし）

~~~diff
- 00aeb1bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb1bc ["INT_ADD", "register:40f0:8", ["const:aeb1bc:8", "const:4:8"]]
- 00aeb1bc ["CALLIND", null, ["register:0:8"]]
+ 00b4af40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4af40 ["INT_ADD", "register:40f0:8", ["const:b4af40:8", "const:4:8"]]
+ 00b4af40 ["CALLIND", null, ["register:0:8"]]
- 00aeb1bc bytes 00013fd6
+ 00b4af40 bytes 00013fd6
- 00aeb204 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeb204 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:878:8"]]
- 00aeb204 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4af88 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4af88 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:738:8"]]
+ 00b4af88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeb204 bytes a0e22139
+ 00b4af88 bytes a0e21c39
- 00aeb214 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aeb214 ["RETURN", null, ["register:0:8"]]
- 00aeb214 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77ab377596e6a5c0eefa235391277a2d"></a>

### [`00aeb218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb218.md) → [`00b4af9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4a/00b4af9c.md) _ZN8firebase4util13integer_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 36.36% / 新版 44.44%

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
      "site": "00aeb254"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb2a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4afd8"
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
      "00b4afb0",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4afbc",
      "READ",
      [
        "storage",
        "010a0878",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aeb254",
      "WRITE",
      [
        "storage",
        "010a0878",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4afb0",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4afbc",
      "READ",
      [
        "storage",
        "01125738",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4afd8",
      "WRITE",
      [
        "storage",
        "01125738",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb218.md#insn-00aeb230) · [`00aeb250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb218.md#insn-00aeb250) · [`00aeb254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb218.md#insn-00aeb254)
- 新版 `00b4afb4`（命令位置の公開資料なし）

~~~diff
- 00aeb230 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeb230 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00b4afb4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4afb4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00aeb230 bytes c10300b4
+ 00b4afb4 bytes c10300b4
- 00aeb250 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb250 ["INT_ADD", "register:40f0:8", ["const:aeb250:8", "const:4:8"]]
- 00aeb250 ["CALLIND", null, ["register:0:8"]]
- 00aeb250 bytes 00013fd6
- 00aeb254 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeb254 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeb254 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:878:8"]]
- 00aeb254 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeb254 bytes bfe22139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed89eb7d8239eeb17babe0a4db9a4e26"></a>

### [`00aeb2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb2b8.md) → [`00b4b03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b03c.md) _ZN8firebase4util13integer_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aeb2b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb2b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb2bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeb2b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb2bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb2cc",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b03c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4b040",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4b050",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb2b8.md#insn-00aeb2b8) · [`00aeb2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb2b8.md#insn-00aeb2bc) · [`00aeb2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb2b8.md#insn-00aeb2d4)

~~~diff
- 00aeb2b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aeb2b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aeb2b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aeb2b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aeb2b8 bytes f44fbea9
- 00aeb2bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aeb2bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aeb2bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aeb2bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb2bc bytes fd7b01a9
- 00aeb2d4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeb2d4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00aeb2d4 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59bb917c82fc83b2a4413732853cddaa"></a>

### [`00aeb364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb364.md) → [`00b4b0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b0e8.md) _ZN8firebase4util13integer_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b128",
      "incomplete_value": true,
      "site": "00b4b128",
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
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb3a4",
      "incomplete_value": true,
      "site": "00aeb3a4",
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
            "const:870:8"
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
      "definition_site": "00b4b104",
      "incomplete_value": true,
      "site": "00b4b104",
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
      "definition_site": "00aeb380",
      "incomplete_value": true,
      "site": "00aeb380",
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
      "definition_site": "00b4b10c",
      "incomplete_value": false,
      "site": "00b4b120",
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
            "const:365:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb388",
      "incomplete_value": false,
      "site": "00aeb39c",
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
            "const:612:8"
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
      "00b4b0fc",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b10c",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00b4b128",
      "WRITE",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b0fc",
      "READ",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b10c",
      "PARAM",
      [
        "storage",
        "002a8365",
        null,
        "string"
      ]
    ],
    [
      "00b4b128",
      "WRITE",
      [
        "storage",
        "01125730",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb364.md#insn-00aeb39c) · [`00aeb3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb364.md#insn-00aeb3a4) · [`00aeb370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb364.md#insn-00aeb370)
- 新版 `00b4b120`（命令位置の公開資料なし） · `00b4b128`（命令位置の公開資料なし） · `00b4b0f4`（命令位置の公開資料なし）

~~~diff
- 00aeb39c ["INT_ADD", "register:40f0:8", ["const:aeb39c:8", "const:4:8"]]
- 00aeb39c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b120 ["INT_ADD", "register:40f0:8", ["const:b4b120:8", "const:4:8"]]
+ 00b4b120 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb39c bytes 3dcb0394
+ 00b4b120 bytes 7c3e0494
- 00aeb3a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
- 00aeb3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b128 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:730:8"]]
+ 00b4b128 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb3a4 bytes 803a04f9
+ 00b4b128 bytes 809a03f9
- 00aeb370 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4b0f4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aeb370 bytes b42d00b0
+ 00b4b0f4 bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc9b4eb386c47b47eb6601d6d5d9a7b6"></a>

### [`00aeb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb410.md) → [`00b4b194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b194.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b1c0",
      "incomplete_value": true,
      "site": "00b4b1c0",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb43c",
      "incomplete_value": true,
      "site": "00aeb43c",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b1a8",
      "incomplete_value": true,
      "site": "00b4b1a8",
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
      "definition_site": "00aeb424",
      "incomplete_value": true,
      "site": "00aeb424",
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
      "definition_site": "00b4b1b4",
      "incomplete_value": false,
      "site": "00b4b1b8",
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
            "const:964:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb430",
      "incomplete_value": false,
      "site": "00aeb434",
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
            "const:1fc:8"
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
      "00b4b1a4",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b1b4",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00b4b1c0",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b1a4",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b1b4",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b1c0",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb410.md#insn-00aeb434) · [`00aeb43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb410.md#insn-00aeb43c) · [`00aeb41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb410.md#insn-00aeb41c)
- 新版 `00b4b1b8`（命令位置の公開資料なし） · `00b4b1c0`（命令位置の公開資料なし） · `00b4b1a0`（命令位置の公開資料なし）

~~~diff
- 00aeb434 ["INT_ADD", "register:40f0:8", ["const:aeb434:8", "const:4:8"]]
- 00aeb434 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b1b8 ["INT_ADD", "register:40f0:8", ["const:b4b1b8:8", "const:4:8"]]
+ 00b4b1b8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb434 bytes 17cb0394
+ 00b4b1b8 bytes 563e0494
- 00aeb43c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb43c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b1c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
+ 00b4b1c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb43c bytes 604e04f9
+ 00b4b1c0 bytes 60ae03f9
- 00aeb41c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4b1a0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeb41c bytes b32d00b0
+ 00b4b1a0 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1f052c0ba200d653a8c0a9bdbe98813"></a>

### [`00aeb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb450.md) → [`00b4b1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b1d4.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b200",
      "incomplete_value": true,
      "site": "00b4b200",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb47c",
      "incomplete_value": true,
      "site": "00aeb47c",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b1e8",
      "incomplete_value": true,
      "site": "00b4b1e8",
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
      "definition_site": "00aeb464",
      "incomplete_value": true,
      "site": "00aeb464",
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
      "definition_site": "00b4b1f0",
      "incomplete_value": false,
      "site": "00b4b1f8",
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
            "const:964:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb46c",
      "incomplete_value": false,
      "site": "00aeb474",
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
            "const:1fc:8"
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
      "00b4b1e4",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b1f0",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00b4b200",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b1e4",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b1f0",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b200",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb450.md#insn-00aeb474) · [`00aeb47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb450.md#insn-00aeb47c) · [`00aeb45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb450.md#insn-00aeb45c)
- 新版 `00b4b1f8`（命令位置の公開資料なし） · `00b4b200`（命令位置の公開資料なし） · `00b4b1e0`（命令位置の公開資料なし）

~~~diff
- 00aeb474 ["INT_ADD", "register:40f0:8", ["const:aeb474:8", "const:4:8"]]
- 00aeb474 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b1f8 ["INT_ADD", "register:40f0:8", ["const:b4b1f8:8", "const:4:8"]]
+ 00b4b1f8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb474 bytes 07cb0394
+ 00b4b1f8 bytes 463e0494
- 00aeb47c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb47c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
+ 00b4b200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb47c bytes 604e04f9
+ 00b4b200 bytes 60ae03f9
- 00aeb45c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4b1e0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeb45c bytes b32d00b0
+ 00b4b1e0 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bacbee49d72b65b0037b1b0e299b158e"></a>

### [`00aeb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb490.md) → [`00b4b214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b214.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b244",
      "incomplete_value": true,
      "site": "00b4b244",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb4c0",
      "incomplete_value": true,
      "site": "00aeb4c0",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b228",
      "incomplete_value": true,
      "site": "00b4b228",
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
      "definition_site": "00aeb4a4",
      "incomplete_value": true,
      "site": "00aeb4a4",
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
      "definition_site": "00b4b234",
      "incomplete_value": false,
      "site": "00b4b23c",
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
            "const:964:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb4b0",
      "incomplete_value": false,
      "site": "00aeb4b8",
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
            "const:1fc:8"
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
      "00b4b224",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b234",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00b4b244",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b224",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b234",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b244",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb490.md#insn-00aeb4b8) · [`00aeb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb490.md#insn-00aeb4c0) · [`00aeb49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb490.md#insn-00aeb49c)
- 新版 `00b4b23c`（命令位置の公開資料なし） · `00b4b244`（命令位置の公開資料なし） · `00b4b220`（命令位置の公開資料なし）

~~~diff
- 00aeb4b8 ["INT_ADD", "register:40f0:8", ["const:aeb4b8:8", "const:4:8"]]
- 00aeb4b8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b23c ["INT_ADD", "register:40f0:8", ["const:b4b23c:8", "const:4:8"]]
+ 00b4b23c ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb4b8 bytes f6ca0394
+ 00b4b23c bytes 353e0494
- 00aeb4c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb4c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b244 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
+ 00b4b244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb4c0 bytes 604e04f9
+ 00b4b244 bytes 60ae03f9
- 00aeb49c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4b220 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeb49c bytes b32d00b0
+ 00b4b220 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccaba4e3c0fe6bfe4526f224844d4c94"></a>

### [`00aeb4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb4d4.md) → [`00b4b258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b258.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b288",
      "incomplete_value": true,
      "site": "00b4b288",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb504",
      "incomplete_value": true,
      "site": "00aeb504",
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b26c",
      "incomplete_value": true,
      "site": "00b4b26c",
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
      "definition_site": "00aeb4e8",
      "incomplete_value": true,
      "site": "00aeb4e8",
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
      "definition_site": "00b4b274",
      "incomplete_value": false,
      "site": "00b4b280",
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
            "const:964:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb4f0",
      "incomplete_value": false,
      "site": "00aeb4fc",
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
            "const:1fc:8"
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
      "00b4b268",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b274",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00b4b288",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b268",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b274",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b288",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb4fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb4d4.md#insn-00aeb4fc) · [`00aeb504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb4d4.md#insn-00aeb504) · [`00aeb4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb4d4.md#insn-00aeb4e0)
- 新版 `00b4b280`（命令位置の公開資料なし） · `00b4b288`（命令位置の公開資料なし） · `00b4b264`（命令位置の公開資料なし）

~~~diff
- 00aeb4fc ["INT_ADD", "register:40f0:8", ["const:aeb4fc:8", "const:4:8"]]
- 00aeb4fc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b280 ["INT_ADD", "register:40f0:8", ["const:b4b280:8", "const:4:8"]]
+ 00b4b280 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb4fc bytes e5ca0394
+ 00b4b280 bytes 243e0494
- 00aeb504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b288 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:758:8"]]
+ 00b4b288 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb504 bytes 604e04f9
+ 00b4b288 bytes 60ae03f9
- 00aeb4e0 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4b264 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeb4e0 bytes b32d00b0
+ 00b4b264 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c25423d188756330369f4659de9c78b2"></a>

### [`00aeb524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb524.md) → [`00b4b2a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b2a8.md) _ZN8firebase4util6intent15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb524"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb528"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb528"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeb524",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb528",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb52c",
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
      "00b4b2a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4b2ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4b2b0",
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

- 旧版 [`00aeb524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb524.md#insn-00aeb524) · [`00aeb528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb524.md#insn-00aeb528) · [`00aeb52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb524.md#insn-00aeb52c)

~~~diff
- 00aeb524 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aeb524 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aeb524 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aeb524 bytes f50f1df8
- 00aeb528 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aeb528 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aeb528 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aeb528 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb528 bytes f44f01a9
- 00aeb52c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aeb52c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aeb52c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aeb52c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb52c bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e22d978bd23c4787f756ba1e6fb999a3"></a>

### [`00aeb5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb5c0.md) → [`00b4b344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b344.md) _ZN8firebase4util6intent12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00b4b380",
      "incomplete_value": true,
      "site": "00b4b380",
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
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb5fc",
      "incomplete_value": true,
      "site": "00aeb5fc",
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
            "const:8a0:8"
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
      "definition_site": "00b4b3d0",
      "incomplete_value": true,
      "site": "00b4b3d0",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb64c",
      "incomplete_value": true,
      "site": "00aeb64c",
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b35c",
      "incomplete_value": true,
      "site": "00b4b35c",
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
      "definition_site": "00aeb5d8",
      "incomplete_value": true,
      "site": "00aeb5d8",
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
      "00b4b358",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b364",
      "READ",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b380",
      "WRITE",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b358",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b364",
      "READ",
      [
        "storage",
        "01125760",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b380",
      "WRITE",
      [
        "storage",
        "01125760",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb5c0.md#insn-00aeb5fc) · [`00aeb648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb5c0.md#insn-00aeb648) · [`00aeb64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb5c0.md#insn-00aeb64c)
- 新版 `00b4b380`（命令位置の公開資料なし） · `00b4b3cc`（命令位置の公開資料なし） · `00b4b3d0`（命令位置の公開資料なし）

~~~diff
- 00aeb5fc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeb5fc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeb5fc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8a0:8"]]
- 00aeb5fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b380 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b380 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b380 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:760:8"]]
+ 00b4b380 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeb5fc bytes bf822239
+ 00b4b380 bytes bf821d39
- 00aeb648 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb648 ["INT_ADD", "register:40f0:8", ["const:aeb648:8", "const:4:8"]]
- 00aeb648 ["CALLIND", null, ["register:0:8"]]
+ 00b4b3cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b3cc ["INT_ADD", "register:40f0:8", ["const:b4b3cc:8", "const:4:8"]]
+ 00b4b3cc ["CALLIND", null, ["register:0:8"]]
- 00aeb648 bytes 00013fd6
+ 00b4b3cc bytes 00013fd6
- 00aeb64c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
- 00aeb64c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aeb64c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4b3d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
+ 00b4b3d0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4b3d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aeb64c bytes 9f4e04f9
+ 00b4b3d0 bytes 9fae03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7de539f10f3b1bdada15a1b98015d0c"></a>

### [`00aeb660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb660.md) → [`00b4b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b3e4.md) _ZN8firebase4util6intent14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b424",
      "incomplete_value": true,
      "site": "00b4b424",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb6a0",
      "incomplete_value": true,
      "site": "00aeb6a0",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b400",
      "incomplete_value": true,
      "site": "00b4b400",
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
      "definition_site": "00aeb67c",
      "incomplete_value": true,
      "site": "00aeb67c",
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
      "definition_site": "00b4b408",
      "incomplete_value": false,
      "site": "00b4b41c",
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
            "const:964:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb684",
      "incomplete_value": false,
      "site": "00aeb698",
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
            "const:1fc:8"
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
      "00b4b3f8",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b408",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00b4b424",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b3f8",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b408",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b424",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb660.md#insn-00aeb698) · [`00aeb6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb660.md#insn-00aeb6a0) · [`00aeb66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb660.md#insn-00aeb66c)
- 新版 `00b4b41c`（命令位置の公開資料なし） · `00b4b424`（命令位置の公開資料なし） · `00b4b3f0`（命令位置の公開資料なし）

~~~diff
- 00aeb698 ["INT_ADD", "register:40f0:8", ["const:aeb698:8", "const:4:8"]]
- 00aeb698 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b41c ["INT_ADD", "register:40f0:8", ["const:b4b41c:8", "const:4:8"]]
+ 00b4b41c ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb698 bytes 7eca0394
+ 00b4b41c bytes bd3d0494
- 00aeb6a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
- 00aeb6a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b424 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
+ 00b4b424 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb6a0 bytes 804e04f9
+ 00b4b424 bytes 80ae03f9
- 00aeb66c ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4b3f0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aeb66c bytes b42d00b0
+ 00b4b3f0 bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8dedfb348b940a50b5fb2cb72a0f93f"></a>

### [`00aeb6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb6d0.md) → [`00b4b454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b454.md) _ZN8firebase4util6intent11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6b0.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b130.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b4b470",
      "incomplete_value": false,
      "site": "00b4b474",
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
      "definition_site": "00aeb6ec",
      "incomplete_value": false,
      "site": "00aeb6f0",
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
      "definition_site": "00b4b480",
      "incomplete_value": true,
      "site": "00b4b48c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeb6fc",
      "incomplete_value": true,
      "site": "00aeb708",
      "value": [
        "LOAD",
        "8",
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
      "00b4b470",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4b480",
      "DATA",
      [
        "storage",
        "010a08a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b470",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4b480",
      "DATA",
      [
        "storage",
        "01125768",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb6d0.md#insn-00aeb6f0) · [`00aeb6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb6d0.md#insn-00aeb6e8) · [`00aeb6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb6d0.md#insn-00aeb6ec)
- 新版 `00b4b474`（命令位置の公開資料なし） · `00b4b46c`（命令位置の公開資料なし） · `00b4b470`（命令位置の公開資料なし）

~~~diff
- 00aeb6f0 ["INT_ADD", "register:40f0:8", ["const:aeb6f0:8", "const:4:8"]]
- 00aeb6f0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4b474 ["INT_ADD", "register:40f0:8", ["const:b4b474:8", "const:4:8"]]
+ 00b4b474 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aeb6f0 bytes a4ca0394
+ 00b4b474 bytes e33d0494
- 00aeb6e8 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4b46c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aeb6e8 bytes 60bdffb0
+ 00b4b46c bytes e0baffb0
- 00aeb6ec ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aeb6ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb6ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb6ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b470 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4b470 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b470 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b470 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeb6ec bytes 001c1591
+ 00b4b470 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83b0376e7eadae76ed9d725a359dd09b"></a>

### [`00aeb70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb70c.md) → [`00b4b490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b490.md) _ZN8firebase4util6intent13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b4d0",
      "incomplete_value": true,
      "site": "00b4b4d0",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb74c",
      "incomplete_value": true,
      "site": "00aeb74c",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b4ac",
      "incomplete_value": true,
      "site": "00b4b4ac",
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
      "definition_site": "00aeb728",
      "incomplete_value": true,
      "site": "00aeb728",
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
      "definition_site": "00b4b4b4",
      "incomplete_value": false,
      "site": "00b4b4c8",
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
            "const:964:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb730",
      "incomplete_value": false,
      "site": "00aeb744",
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
            "const:1fc:8"
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
      "00b4b4a4",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b4b4",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00b4b4d0",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b4a4",
      "READ",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b4b4",
      "PARAM",
      [
        "storage",
        "002a2964",
        null,
        "string"
      ]
    ],
    [
      "00b4b4d0",
      "WRITE",
      [
        "storage",
        "01125758",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb70c.md#insn-00aeb744) · [`00aeb74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb70c.md#insn-00aeb74c) · [`00aeb718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb70c.md#insn-00aeb718)
- 新版 `00b4b4c8`（命令位置の公開資料なし） · `00b4b4d0`（命令位置の公開資料なし） · `00b4b49c`（命令位置の公開資料なし）

~~~diff
- 00aeb744 ["INT_ADD", "register:40f0:8", ["const:aeb744:8", "const:4:8"]]
- 00aeb744 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b4c8 ["INT_ADD", "register:40f0:8", ["const:b4b4c8:8", "const:4:8"]]
+ 00b4b4c8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb744 bytes 53ca0394
+ 00b4b4c8 bytes 923d0494
- 00aeb74c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
- 00aeb74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b4d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:758:8"]]
+ 00b4b4d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb74c bytes 804e04f9
+ 00b4b4d0 bytes 80ae03f9
- 00aeb718 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4b49c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aeb718 bytes b42d00b0
+ 00b4b49c bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-645b1acd6a52511d815feb8d37162287"></a>

### [`00aeb7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7f8.md) → [`00b4b57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b57c.md) _ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b5a8",
      "incomplete_value": true,
      "site": "00b4b5a8",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb824",
      "incomplete_value": true,
      "site": "00aeb824",
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
            "const:8d8:8"
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
      "definition_site": "00b4b590",
      "incomplete_value": true,
      "site": "00b4b590",
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
      "definition_site": "00aeb80c",
      "incomplete_value": true,
      "site": "00aeb80c",
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
      "definition_site": "00b4b598",
      "incomplete_value": false,
      "site": "00b4b5a0",
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
            "const:8a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb814",
      "incomplete_value": false,
      "site": "00aeb81c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:372:8"
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
      "00b4b58c",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b598",
      "PARAM",
      [
        "storage",
        "00290372",
        null,
        "string"
      ]
    ],
    [
      "00b4b5a8",
      "WRITE",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b58c",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b598",
      "PARAM",
      [
        "storage",
        "0029f8a9",
        null,
        "string"
      ]
    ],
    [
      "00b4b5a8",
      "WRITE",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7f8.md#insn-00aeb81c) · [`00aeb824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7f8.md#insn-00aeb824) · [`00aeb804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7f8.md#insn-00aeb804)
- 新版 `00b4b5a0`（命令位置の公開資料なし） · `00b4b5a8`（命令位置の公開資料なし） · `00b4b588`（命令位置の公開資料なし）

~~~diff
- 00aeb81c ["INT_ADD", "register:40f0:8", ["const:aeb81c:8", "const:4:8"]]
- 00aeb81c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b5a0 ["INT_ADD", "register:40f0:8", ["const:b4b5a0:8", "const:4:8"]]
+ 00b4b5a0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb81c bytes 1dca0394
+ 00b4b5a0 bytes 5c3d0494
- 00aeb824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
- 00aeb824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b5a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00b4b5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb824 bytes 606e04f9
+ 00b4b5a8 bytes 60ce03f9
- 00aeb804 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4b588 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeb804 bytes b32d00b0
+ 00b4b588 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efc402eeda43d2988628b03dc8b31bec"></a>

### [`00aeb838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb838.md) → [`00b4b5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b5bc.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b5ec",
      "incomplete_value": true,
      "site": "00b4b5ec",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb868",
      "incomplete_value": true,
      "site": "00aeb868",
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
            "const:8d8:8"
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
      "definition_site": "00b4b5d0",
      "incomplete_value": true,
      "site": "00b4b5d0",
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
      "definition_site": "00aeb84c",
      "incomplete_value": true,
      "site": "00aeb84c",
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
      "definition_site": "00b4b5dc",
      "incomplete_value": false,
      "site": "00b4b5e4",
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
            "const:8a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb858",
      "incomplete_value": false,
      "site": "00aeb860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:372:8"
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
      "00b4b5cc",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5dc",
      "PARAM",
      [
        "storage",
        "00290372",
        null,
        "string"
      ]
    ],
    [
      "00b4b5ec",
      "WRITE",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b5cc",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5dc",
      "PARAM",
      [
        "storage",
        "0029f8a9",
        null,
        "string"
      ]
    ],
    [
      "00b4b5ec",
      "WRITE",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb838.md#insn-00aeb860) · [`00aeb868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb838.md#insn-00aeb868) · [`00aeb844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb838.md#insn-00aeb844)
- 新版 `00b4b5e4`（命令位置の公開資料なし） · `00b4b5ec`（命令位置の公開資料なし） · `00b4b5c8`（命令位置の公開資料なし）

~~~diff
- 00aeb860 ["INT_ADD", "register:40f0:8", ["const:aeb860:8", "const:4:8"]]
- 00aeb860 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b5e4 ["INT_ADD", "register:40f0:8", ["const:b4b5e4:8", "const:4:8"]]
+ 00b4b5e4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb860 bytes 0cca0394
+ 00b4b5e4 bytes 4b3d0494
- 00aeb868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
- 00aeb868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b5ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00b4b5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb868 bytes 606e04f9
+ 00b4b5ec bytes 60ce03f9
- 00aeb844 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4b5c8 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeb844 bytes b32d00b0
+ 00b4b5c8 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c9e0c15cd772b410f640267ab8068ea"></a>

### [`00aeb87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb87c.md) → [`00b4b600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b600.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b630",
      "incomplete_value": true,
      "site": "00b4b630",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb8ac",
      "incomplete_value": true,
      "site": "00aeb8ac",
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
            "const:8d8:8"
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
      "definition_site": "00b4b614",
      "incomplete_value": true,
      "site": "00b4b614",
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
      "definition_site": "00aeb890",
      "incomplete_value": true,
      "site": "00aeb890",
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
      "definition_site": "00b4b61c",
      "incomplete_value": false,
      "site": "00b4b628",
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
            "const:8a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb898",
      "incomplete_value": false,
      "site": "00aeb8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:372:8"
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
      "00b4b610",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b61c",
      "PARAM",
      [
        "storage",
        "00290372",
        null,
        "string"
      ]
    ],
    [
      "00b4b630",
      "WRITE",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b610",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b61c",
      "PARAM",
      [
        "storage",
        "0029f8a9",
        null,
        "string"
      ]
    ],
    [
      "00b4b630",
      "WRITE",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb87c.md#insn-00aeb8a4) · [`00aeb8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb87c.md#insn-00aeb8ac) · [`00aeb888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb87c.md#insn-00aeb888)
- 新版 `00b4b628`（命令位置の公開資料なし） · `00b4b630`（命令位置の公開資料なし） · `00b4b60c`（命令位置の公開資料なし）

~~~diff
- 00aeb8a4 ["INT_ADD", "register:40f0:8", ["const:aeb8a4:8", "const:4:8"]]
- 00aeb8a4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b628 ["INT_ADD", "register:40f0:8", ["const:b4b628:8", "const:4:8"]]
+ 00b4b628 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeb8a4 bytes fbc90394
+ 00b4b628 bytes 3a3d0494
- 00aeb8ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
- 00aeb8ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b630 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:798:8"]]
+ 00b4b630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb8ac bytes 606e04f9
+ 00b4b630 bytes 60ce03f9
- 00aeb888 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4b60c ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeb888 bytes b32d00b0
+ 00b4b60c bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16ae94e79c43c191bca23b6e80a4bb80"></a>

### [`00aeb8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb8cc.md) → [`00b4b650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b650.md) _ZN8firebase4util8iterable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 87.18% / 新版 87.18%

CFGの説明率　旧版 50.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b6d8",
      "incomplete_value": true,
      "site": "00b4b6d8",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb954",
      "incomplete_value": true,
      "site": "00aeb954",
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
            "const:8e0:8"
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
      "site": "00aeb90c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b4b690"
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
      "00b4b664",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aeb900",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b6d8",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b664",
      "READ",
      [
        "storage",
        "011257a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b684",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b6d8",
      "WRITE",
      [
        "storage",
        "011257a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb90c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb8cc.md#insn-00aeb90c) · [`00aeb954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb8cc.md#insn-00aeb954)
- 新版 `00b4b6d8`（命令位置の公開資料なし） · `00b4b690`（命令位置の公開資料なし）

~~~diff
- 00aeb90c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb90c ["INT_ADD", "register:40f0:8", ["const:aeb90c:8", "const:4:8"]]
- 00aeb90c ["CALLIND", null, ["register:0:8"]]
- 00aeb90c bytes 00013fd6
- 00aeb954 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeb954 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8e0:8"]]
- 00aeb954 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b6d8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b6d8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7a0:8"]]
+ 00b4b6d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeb954 bytes a0822339
+ 00b4b6d8 bytes a0821e39
+ 00b4b690 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b690 ["INT_ADD", "register:40f0:8", ["const:b4b690:8", "const:4:8"]]
+ 00b4b690 ["CALLIND", null, ["register:0:8"]]
+ 00b4b690 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-747d2d1af457f93150283a88a8d21a5d"></a>

### [`00aeb968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb968.md) → [`00b4b6ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b6ec.md) _ZN8firebase4util8iterable12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.50% / 新版 72.50%

CFGの説明率　旧版 54.55% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb968"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb96c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb96c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeb968",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb96c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb970",
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
      "00b4b6ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4b6f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4b6f4",
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

- 旧版 [`00aeb968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb968.md#insn-00aeb968) · [`00aeb96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb968.md#insn-00aeb96c) · [`00aeb970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb968.md#insn-00aeb970)

~~~diff
- 00aeb968 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aeb968 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aeb968 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aeb968 bytes f50f1df8
- 00aeb96c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aeb96c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aeb96c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aeb96c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb96c bytes f44f01a9
- 00aeb970 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aeb970 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aeb970 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aeb970 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb970 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7def2b7d93490763ab48bf2548e3a37b"></a>

### [`00aeba08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba08.md) → [`00b4b78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b78c.md) _ZN8firebase4util8iterable14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b7cc",
      "incomplete_value": true,
      "site": "00b4b7cc",
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
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeba48",
      "incomplete_value": true,
      "site": "00aeba48",
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
            "const:8d8:8"
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
      "definition_site": "00b4b7a8",
      "incomplete_value": true,
      "site": "00b4b7a8",
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
      "definition_site": "00aeba24",
      "incomplete_value": true,
      "site": "00aeba24",
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
      "definition_site": "00b4b7b0",
      "incomplete_value": false,
      "site": "00b4b7c4",
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
            "const:8a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeba2c",
      "incomplete_value": false,
      "site": "00aeba40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:372:8"
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
      "00b4b7a0",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b7b0",
      "PARAM",
      [
        "storage",
        "00290372",
        null,
        "string"
      ]
    ],
    [
      "00b4b7cc",
      "WRITE",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b7a0",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b7b0",
      "PARAM",
      [
        "storage",
        "0029f8a9",
        null,
        "string"
      ]
    ],
    [
      "00b4b7cc",
      "WRITE",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeba40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba08.md#insn-00aeba40) · [`00aeba48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba08.md#insn-00aeba48) · [`00aeba14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba08.md#insn-00aeba14)
- 新版 `00b4b7c4`（命令位置の公開資料なし） · `00b4b7cc`（命令位置の公開資料なし） · `00b4b798`（命令位置の公開資料なし）

~~~diff
- 00aeba40 ["INT_ADD", "register:40f0:8", ["const:aeba40:8", "const:4:8"]]
- 00aeba40 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b7c4 ["INT_ADD", "register:40f0:8", ["const:b4b7c4:8", "const:4:8"]]
+ 00b4b7c4 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeba40 bytes 94c90394
+ 00b4b7c4 bytes d33c0494
- 00aeba48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d8:8"]]
- 00aeba48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b7cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:798:8"]]
+ 00b4b7cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeba48 bytes 806e04f9
+ 00b4b7cc bytes 80ce03f9
- 00aeba14 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4b798 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aeba14 bytes b42d00b0
+ 00b4b798 bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1ec700421a28f5ff2be74c543f568e0"></a>

### [`00aeba78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba78.md) → [`00b4b7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b7fc.md) _ZN8firebase4util8iterable11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b818",
      "incomplete_value": false,
      "site": "00b4b81c",
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
      "definition_site": "00aeba94",
      "incomplete_value": false,
      "site": "00aeba98",
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
      "definition_site": "00b4b828",
      "incomplete_value": true,
      "site": "00b4b834",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aebaa4",
      "incomplete_value": true,
      "site": "00aebab0",
      "value": [
        "LOAD",
        "8",
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
      "00b4b818",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4b828",
      "DATA",
      [
        "storage",
        "010a08e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b818",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4b828",
      "DATA",
      [
        "storage",
        "011257a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba78.md#insn-00aeba98) · [`00aeba90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba78.md#insn-00aeba90) · [`00aeba94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba78.md#insn-00aeba94)
- 新版 `00b4b81c`（命令位置の公開資料なし） · `00b4b814`（命令位置の公開資料なし） · `00b4b818`（命令位置の公開資料なし）

~~~diff
- 00aeba98 ["INT_ADD", "register:40f0:8", ["const:aeba98:8", "const:4:8"]]
- 00aeba98 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4b81c ["INT_ADD", "register:40f0:8", ["const:b4b81c:8", "const:4:8"]]
+ 00b4b81c ["CALL", null, ["callee:00c5ac00:8"]]
- 00aeba98 bytes bac90394
+ 00b4b81c bytes f93c0494
- 00aeba90 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4b814 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aeba90 bytes 60bdffb0
+ 00b4b814 bytes e0baffb0
- 00aeba94 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aeba94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeba94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeba94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b818 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4b818 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b818 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b818 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeba94 bytes 001c1591
+ 00b4b818 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35b33258954371f18a23b9621052eac0"></a>

### [`00aebab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebab4.md) → [`00b4b838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b838.md) _ZN8firebase4util8iterable13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aebab4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebab4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebab8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aebab4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aebab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aebac8",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b838",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4b83c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4b84c",
      "READ",
      [
        "storage",
        "01125798",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebab4.md#insn-00aebab4) · [`00aebab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebab4.md#insn-00aebab8) · [`00aebad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebab4.md#insn-00aebad0)

~~~diff
- 00aebab4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aebab4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aebab4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aebab4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aebab4 bytes f44fbea9
- 00aebab8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aebab8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aebab8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aebab8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aebab8 bytes fd7b01a9
- 00aebad0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aebad0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00aebad0 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baf8d048ce1f154f1bd33d6b5c2a857a"></a>

### [`00aebb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb24.md) → [`00b4b8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b8a8.md) _ZN8firebase4util8iterable10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b8c4",
      "incomplete_value": false,
      "site": "00b4b8c8",
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
      "definition_site": "00aebb40",
      "incomplete_value": false,
      "site": "00aebb44",
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
      "definition_site": "00b4b8d4",
      "incomplete_value": true,
      "site": "00b4b8e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aebb50",
      "incomplete_value": true,
      "site": "00aebb5c",
      "value": [
        "LOAD",
        "8",
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
      "00b4b8c4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4b8d4",
      "DATA",
      [
        "storage",
        "010a08f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b8c4",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4b8d4",
      "DATA",
      [
        "storage",
        "011257b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb24.md#insn-00aebb44) · [`00aebb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb24.md#insn-00aebb3c) · [`00aebb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb24.md#insn-00aebb40)
- 新版 `00b4b8c8`（命令位置の公開資料なし） · `00b4b8c0`（命令位置の公開資料なし） · `00b4b8c4`（命令位置の公開資料なし）

~~~diff
- 00aebb44 ["INT_ADD", "register:40f0:8", ["const:aebb44:8", "const:4:8"]]
- 00aebb44 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4b8c8 ["INT_ADD", "register:40f0:8", ["const:b4b8c8:8", "const:4:8"]]
+ 00b4b8c8 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aebb44 bytes 8fc90394
+ 00b4b8c8 bytes ce3c0494
- 00aebb3c ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4b8c0 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aebb3c bytes 60bdffd0
+ 00b4b8c0 bytes e0baffd0
- 00aebb40 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aebb40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aebb40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aebb40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b8c4 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4b8c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b8c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b8c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aebb40 bytes 00c81791
+ 00b4b8c4 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-232865d57a1cc1bce6893ea38a3671d9"></a>

### [`00aebb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb60.md) → [`00b4b8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b8e4.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aebb8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4b910"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b8f8",
      "incomplete_value": true,
      "site": "00b4b8f8",
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
      "definition_site": "00aebb74",
      "incomplete_value": true,
      "site": "00aebb74",
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
      "00b4b8f4",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b8f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aebb90"
      ]
    ],
    [
      "unmatched:00aebb80",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4b8f4",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b8f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4b914"
      ]
    ],
    [
      "00b4b904",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb60.md#insn-00aebb84) · [`00aebb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb60.md#insn-00aebb8c) · [`00aebb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb60.md#insn-00aebb9c)

~~~diff
- 00aebb84 ["INT_ADD", "register:40f0:8", ["const:aebb84:8", "const:4:8"]]
- 00aebb84 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aebb84 bytes 43c90394
- 00aebb8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00aebb8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebb8c bytes 607e04f9
- 00aebb9c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aebb9c ["RETURN", null, ["register:0:8"]]
- 00aebb9c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e802d441b92894cc347ff3aa4024adcc"></a>

### [`00aebba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebba0.md) → [`00b4b924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b924.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b950",
      "incomplete_value": true,
      "site": "00b4b950",
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
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebbcc",
      "incomplete_value": true,
      "site": "00aebbcc",
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
      "definition_site": "00b4b938",
      "incomplete_value": true,
      "site": "00b4b938",
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
      "definition_site": "00aebbb4",
      "incomplete_value": true,
      "site": "00aebbb4",
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
      "definition_site": "00b4b940",
      "incomplete_value": false,
      "site": "00b4b948",
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
            "const:7b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebbbc",
      "incomplete_value": false,
      "site": "00aebbc4",
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
            "const:4da:8"
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
      "00b4b934",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b940",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00b4b950",
      "WRITE",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b934",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b940",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ],
    [
      "00b4b950",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebbc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebba0.md#insn-00aebbc4) · [`00aebbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebba0.md#insn-00aebbcc) · [`00aebbac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebba0.md#insn-00aebbac)
- 新版 `00b4b948`（命令位置の公開資料なし） · `00b4b950`（命令位置の公開資料なし） · `00b4b930`（命令位置の公開資料なし）

~~~diff
- 00aebbc4 ["INT_ADD", "register:40f0:8", ["const:aebbc4:8", "const:4:8"]]
- 00aebbc4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b948 ["INT_ADD", "register:40f0:8", ["const:b4b948:8", "const:4:8"]]
+ 00b4b948 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aebbc4 bytes 33c90394
+ 00b4b948 bytes 723c0494
- 00aebbcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00aebbcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
+ 00b4b950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebbcc bytes 607e04f9
+ 00b4b950 bytes 60de03f9
- 00aebbac ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4b930 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aebbac bytes b32d00b0
+ 00b4b930 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4b8d49bc66c9e3206b381978df130a9"></a>

### [`00aebbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebbe0.md) → [`00b4b964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b964.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

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
      "site": "00aebc10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4b994"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b978",
      "incomplete_value": true,
      "site": "00b4b978",
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
      "definition_site": "00aebbf4",
      "incomplete_value": true,
      "site": "00aebbf4",
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
      "00b4b974",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aebc00",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aebc08",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b4b974",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b984",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ],
    [
      "00b4b98c",
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

- 旧版 [`00aebbf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebbe0.md#insn-00aebbf4) · [`00aebc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebbe0.md#insn-00aebc08) · [`00aebc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebbe0.md#insn-00aebc10)
- 新版 `00b4b978`（命令位置の公開資料なし）

~~~diff
- 00aebbf4 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aebbf4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4b978 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4b978 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aebbf4 bytes 080100b5
+ 00b4b978 bytes 080100b5
- 00aebc08 ["INT_ADD", "register:40f0:8", ["const:aebc08:8", "const:4:8"]]
- 00aebc08 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aebc08 bytes 22c90394
- 00aebc10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00aebc10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebc10 bytes 607e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bb37ccaa4bf7bad1110fba7c79df700"></a>

### [`00aebc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc24.md) → [`00b4b9a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b9a8.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4b9d8",
      "incomplete_value": true,
      "site": "00b4b9d8",
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
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebc54",
      "incomplete_value": true,
      "site": "00aebc54",
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
      "definition_site": "00b4b9bc",
      "incomplete_value": true,
      "site": "00b4b9bc",
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
      "definition_site": "00aebc38",
      "incomplete_value": true,
      "site": "00aebc38",
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
      "definition_site": "00b4b9c4",
      "incomplete_value": false,
      "site": "00b4b9d0",
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
            "const:7b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebc40",
      "incomplete_value": false,
      "site": "00aebc4c",
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
            "const:4da:8"
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
      "00b4b9b8",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b9c4",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00b4b9d8",
      "WRITE",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b9b8",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b9c4",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ],
    [
      "00b4b9d8",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc24.md#insn-00aebc4c) · [`00aebc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc24.md#insn-00aebc54) · [`00aebc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc24.md#insn-00aebc30)
- 新版 `00b4b9d0`（命令位置の公開資料なし） · `00b4b9d8`（命令位置の公開資料なし） · `00b4b9b4`（命令位置の公開資料なし）

~~~diff
- 00aebc4c ["INT_ADD", "register:40f0:8", ["const:aebc4c:8", "const:4:8"]]
- 00aebc4c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4b9d0 ["INT_ADD", "register:40f0:8", ["const:b4b9d0:8", "const:4:8"]]
+ 00b4b9d0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aebc4c bytes 11c90394
+ 00b4b9d0 bytes 503c0494
- 00aebc54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
- 00aebc54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b9d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7b8:8"]]
+ 00b4b9d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebc54 bytes 607e04f9
+ 00b4b9d8 bytes 60de03f9
- 00aebc30 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4b9b4 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aebc30 bytes b32d00b0
+ 00b4b9b4 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fa7897cbb61a73f385925657a07e53f"></a>

### [`00aebc74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc74.md) → [`00b4b9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b9f8.md) _ZN8firebase4util8iterator15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_return_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ba80",
      "incomplete_value": true,
      "site": "00b4ba80",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebcfc",
      "incomplete_value": true,
      "site": "00aebcfc",
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
      "definition_site": "00b4ba2c",
      "incomplete_value": true,
      "site": "00b4ba38",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
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
    "old": {
      "definition_site": "00aebca8",
      "incomplete_value": true,
      "site": "00aebcb4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebd0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ba0c",
      "READ",
      [
        "storage",
        "010a0900",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ba18",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aebd00"
      ]
    ],
    [
      "00b4ba2c",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ba0c",
      "READ",
      [
        "storage",
        "011257c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ba18",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ba84"
      ]
    ],
    [
      "00b4ba2c",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc74.md#insn-00aebcb4) · [`00aebcfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc74.md#insn-00aebcfc) · [`00aebd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc74.md#insn-00aebd0c)
- 新版 `00b4ba38`（命令位置の公開資料なし） · `00b4ba80`（命令位置の公開資料なし）

~~~diff
- 00aebcb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aebcb4 ["INT_ADD", "register:40f0:8", ["const:aebcb4:8", "const:4:8"]]
- 00aebcb4 ["CALLIND", null, ["register:0:8"]]
+ 00b4ba38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4ba38 ["INT_ADD", "register:40f0:8", ["const:b4ba38:8", "const:4:8"]]
+ 00b4ba38 ["CALLIND", null, ["register:0:8"]]
- 00aebcb4 bytes 00013fd6
+ 00b4ba38 bytes 00013fd6
- 00aebcfc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aebcfc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:900:8"]]
- 00aebcfc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4ba80 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4ba80 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7c0:8"]]
+ 00b4ba80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aebcfc bytes a0022439
+ 00b4ba80 bytes a0021f39
- 00aebd0c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aebd0c ["RETURN", null, ["register:0:8"]]
- 00aebd0c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01ad290f53971c81907f7cc52998e510"></a>

### [`00aebd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebd10.md) → [`00b4ba94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4ba94.md) _ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00b4bad0",
      "incomplete_value": true,
      "site": "00b4bad0",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebd4c",
      "incomplete_value": true,
      "site": "00aebd4c",
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
      "definition_site": "00b4bb20",
      "incomplete_value": true,
      "site": "00b4bb20",
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
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebd9c",
      "incomplete_value": true,
      "site": "00aebd9c",
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
      "definition_site": "00b4baac",
      "incomplete_value": true,
      "site": "00b4baac",
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
      "definition_site": "00aebd28",
      "incomplete_value": true,
      "site": "00aebd28",
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
      "00b4baa8",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bab4",
      "READ",
      [
        "storage",
        "010a0900",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bad0",
      "WRITE",
      [
        "storage",
        "010a0900",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4baa8",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bab4",
      "READ",
      [
        "storage",
        "011257c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bad0",
      "WRITE",
      [
        "storage",
        "011257c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebd10.md#insn-00aebd4c) · [`00aebd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebd10.md#insn-00aebd98) · [`00aebd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebd10.md#insn-00aebd9c)
- 新版 `00b4bad0`（命令位置の公開資料なし） · `00b4bb1c`（命令位置の公開資料なし） · `00b4bb20`（命令位置の公開資料なし）

~~~diff
- 00aebd4c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aebd4c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aebd4c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:900:8"]]
- 00aebd4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4bad0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4bad0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4bad0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7c0:8"]]
+ 00b4bad0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aebd4c bytes bf022439
+ 00b4bad0 bytes bf021f39
- 00aebd98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aebd98 ["INT_ADD", "register:40f0:8", ["const:aebd98:8", "const:4:8"]]
- 00aebd98 ["CALLIND", null, ["register:0:8"]]
+ 00b4bb1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4bb1c ["INT_ADD", "register:40f0:8", ["const:b4bb1c:8", "const:4:8"]]
+ 00b4bb1c ["CALLIND", null, ["register:0:8"]]
- 00aebd98 bytes 00013fd6
+ 00b4bb1c bytes 00013fd6
- 00aebd9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
- 00aebd9c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aebd9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4bb20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
+ 00b4bb20 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4bb20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aebd9c bytes 9f7e04f9
+ 00b4bb20 bytes 9fde03f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e546cc5e3aceef02fa6b408b91bffef7"></a>

### [`00aebdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebdb0.md) → [`00b4bb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bb34.md) _ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4bb74",
      "incomplete_value": true,
      "site": "00b4bb74",
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
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebdf0",
      "incomplete_value": true,
      "site": "00aebdf0",
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
      "definition_site": "00b4bb50",
      "incomplete_value": true,
      "site": "00b4bb50",
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
      "definition_site": "00aebdcc",
      "incomplete_value": true,
      "site": "00aebdcc",
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
      "definition_site": "00b4bb58",
      "incomplete_value": false,
      "site": "00b4bb6c",
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
            "const:7b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebdd4",
      "incomplete_value": false,
      "site": "00aebde8",
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
            "const:4da:8"
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
      "00b4bb48",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bb58",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00b4bb74",
      "WRITE",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bb48",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bb58",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ],
    [
      "00b4bb74",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebdb0.md#insn-00aebde8) · [`00aebdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebdb0.md#insn-00aebdf0) · [`00aebdbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebdb0.md#insn-00aebdbc)
- 新版 `00b4bb6c`（命令位置の公開資料なし） · `00b4bb74`（命令位置の公開資料なし） · `00b4bb40`（命令位置の公開資料なし）

~~~diff
- 00aebde8 ["INT_ADD", "register:40f0:8", ["const:aebde8:8", "const:4:8"]]
- 00aebde8 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4bb6c ["INT_ADD", "register:40f0:8", ["const:b4bb6c:8", "const:4:8"]]
+ 00b4bb6c ["CALL", null, ["callee:00c5ab10:8"]]
- 00aebde8 bytes aac80394
+ 00b4bb6c bytes e93b0494
- 00aebdf0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
- 00aebdf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bb74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
+ 00b4bb74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebdf0 bytes 807e04f9
+ 00b4bb74 bytes 80de03f9
- 00aebdbc ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4bb40 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aebdbc bytes b42d00b0
+ 00b4bb40 bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e68199aa00f19f9e6400b06b4660ad48"></a>

### [`00aebe20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe20.md) → [`00b4bba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bba4.md) _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6e0.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b160.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b4bbc0",
      "incomplete_value": false,
      "site": "00b4bbc4",
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
      "definition_site": "00aebe3c",
      "incomplete_value": false,
      "site": "00aebe40",
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
      "definition_site": "00b4bbd0",
      "incomplete_value": true,
      "site": "00b4bbdc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aebe4c",
      "incomplete_value": true,
      "site": "00aebe58",
      "value": [
        "LOAD",
        "8",
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
      "00b4bbc0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4bbd0",
      "DATA",
      [
        "storage",
        "010a0908",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bbc0",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4bbd0",
      "DATA",
      [
        "storage",
        "011257c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebe40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe20.md#insn-00aebe40) · [`00aebe38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe20.md#insn-00aebe38) · [`00aebe3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe20.md#insn-00aebe3c)
- 新版 `00b4bbc4`（命令位置の公開資料なし） · `00b4bbbc`（命令位置の公開資料なし） · `00b4bbc0`（命令位置の公開資料なし）

~~~diff
- 00aebe40 ["INT_ADD", "register:40f0:8", ["const:aebe40:8", "const:4:8"]]
- 00aebe40 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4bbc4 ["INT_ADD", "register:40f0:8", ["const:b4bbc4:8", "const:4:8"]]
+ 00b4bbc4 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aebe40 bytes d0c80394
+ 00b4bbc4 bytes 0f3c0494
- 00aebe38 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4bbbc ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aebe38 bytes 60bdffb0
+ 00b4bbbc bytes e0baffb0
- 00aebe3c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aebe3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aebe3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aebe3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4bbc0 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4bbc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bbc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bbc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aebe3c bytes 001c1591
+ 00b4bbc0 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6db8e169846c4442ff9d6bd81155938a"></a>

### [`00aebe5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe5c.md) → [`00b4bbe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bbe0.md) _ZN8firebase4util8iterator13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4bc20",
      "incomplete_value": true,
      "site": "00b4bc20",
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
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebe9c",
      "incomplete_value": true,
      "site": "00aebe9c",
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
      "definition_site": "00b4bbfc",
      "incomplete_value": true,
      "site": "00b4bbfc",
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
      "definition_site": "00aebe78",
      "incomplete_value": true,
      "site": "00aebe78",
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
      "definition_site": "00b4bc04",
      "incomplete_value": false,
      "site": "00b4bc18",
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
            "const:7b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebe80",
      "incomplete_value": false,
      "site": "00aebe94",
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
            "const:4da:8"
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
      "00b4bbf4",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bc04",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00b4bc20",
      "WRITE",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bbf4",
      "READ",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bc04",
      "PARAM",
      [
        "storage",
        "002a707b",
        null,
        "string"
      ]
    ],
    [
      "00b4bc20",
      "WRITE",
      [
        "storage",
        "011257b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebe94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe5c.md#insn-00aebe94) · [`00aebe9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe5c.md#insn-00aebe9c) · [`00aebe68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe5c.md#insn-00aebe68)
- 新版 `00b4bc18`（命令位置の公開資料なし） · `00b4bc20`（命令位置の公開資料なし） · `00b4bbec`（命令位置の公開資料なし）

~~~diff
- 00aebe94 ["INT_ADD", "register:40f0:8", ["const:aebe94:8", "const:4:8"]]
- 00aebe94 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4bc18 ["INT_ADD", "register:40f0:8", ["const:b4bc18:8", "const:4:8"]]
+ 00b4bc18 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aebe94 bytes 7fc80394
+ 00b4bc18 bytes be3b0494
- 00aebe9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
- 00aebe9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bc20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
+ 00b4bc20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebe9c bytes 807e04f9
+ 00b4bc20 bytes 80de03f9
- 00aebe68 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4bbec ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aebe68 bytes b42d00b0
+ 00b4bbec bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a54398f05b0b9120e7d8cfb4a922939e"></a>

### [`00aebf08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf08.md) → [`00b4bc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bc8c.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4bcb8",
      "incomplete_value": true,
      "site": "00b4bcb8",
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
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebf34",
      "incomplete_value": true,
      "site": "00aebf34",
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
            "const:920:8"
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
      "definition_site": "00b4bca0",
      "incomplete_value": true,
      "site": "00b4bca0",
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
      "definition_site": "00aebf1c",
      "incomplete_value": true,
      "site": "00aebf1c",
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
      "definition_site": "00b4bcac",
      "incomplete_value": false,
      "site": "00b4bcb0",
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
            "const:8bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebf28",
      "incomplete_value": false,
      "site": "00aebf2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:385:8"
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
      "00b4bc9c",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bcac",
      "PARAM",
      [
        "storage",
        "00290385",
        null,
        "string"
      ]
    ],
    [
      "00b4bcb8",
      "WRITE",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bc9c",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bcac",
      "PARAM",
      [
        "storage",
        "0029f8bc",
        null,
        "string"
      ]
    ],
    [
      "00b4bcb8",
      "WRITE",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf08.md#insn-00aebf2c) · [`00aebf34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf08.md#insn-00aebf34) · [`00aebf14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf08.md#insn-00aebf14)
- 新版 `00b4bcb0`（命令位置の公開資料なし） · `00b4bcb8`（命令位置の公開資料なし） · `00b4bc98`（命令位置の公開資料なし）

~~~diff
- 00aebf2c ["INT_ADD", "register:40f0:8", ["const:aebf2c:8", "const:4:8"]]
- 00aebf2c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4bcb0 ["INT_ADD", "register:40f0:8", ["const:b4bcb0:8", "const:4:8"]]
+ 00b4bcb0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aebf2c bytes 59c80394
+ 00b4bcb0 bytes 983b0494
- 00aebf34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00aebf34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bcb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b4bcb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebf34 bytes 609204f9
+ 00b4bcb8 bytes 60f203f9
- 00aebf14 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4bc98 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aebf14 bytes b32d00b0
+ 00b4bc98 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ba74b1c76a58cb131f89f999dd0803a"></a>

### [`00aebf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf48.md) → [`00b4bccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bccc.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aebf48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebf4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebf4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aebf48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aebf4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4bcdc",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bccc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4bcd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b4bcdc",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf48.md#insn-00aebf48) · [`00aebf4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf48.md#insn-00aebf4c) · [`00aebf5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf48.md#insn-00aebf5c)
- 新版 `00b4bce0`（命令位置の公開資料なし）

~~~diff
- 00aebf48 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00aebf48 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aebf48 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aebf48 bytes f30f1ef8
- 00aebf4c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aebf4c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aebf4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aebf4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aebf4c bytes fd7b01a9
- 00aebf5c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aebf5c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b4bce0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4bce0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aebf5c bytes e80000b5
+ 00b4bce0 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dfdb82e9b248a31d8e1ba90b8973f52"></a>

### [`00aebf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf88.md) → [`00b4bd0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bd0c.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4bd3c",
      "incomplete_value": true,
      "site": "00b4bd3c",
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
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebfb8",
      "incomplete_value": true,
      "site": "00aebfb8",
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
            "const:920:8"
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
      "definition_site": "00b4bd20",
      "incomplete_value": true,
      "site": "00b4bd20",
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
      "definition_site": "00aebf9c",
      "incomplete_value": true,
      "site": "00aebf9c",
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
      "definition_site": "00b4bd2c",
      "incomplete_value": false,
      "site": "00b4bd34",
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
            "const:8bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebfa8",
      "incomplete_value": false,
      "site": "00aebfb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:385:8"
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
      "00b4bd1c",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd2c",
      "PARAM",
      [
        "storage",
        "00290385",
        null,
        "string"
      ]
    ],
    [
      "00b4bd3c",
      "WRITE",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bd1c",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd2c",
      "PARAM",
      [
        "storage",
        "0029f8bc",
        null,
        "string"
      ]
    ],
    [
      "00b4bd3c",
      "WRITE",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf88.md#insn-00aebfb0) · [`00aebfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf88.md#insn-00aebfb8) · [`00aebf94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf88.md#insn-00aebf94)
- 新版 `00b4bd34`（命令位置の公開資料なし） · `00b4bd3c`（命令位置の公開資料なし） · `00b4bd18`（命令位置の公開資料なし）

~~~diff
- 00aebfb0 ["INT_ADD", "register:40f0:8", ["const:aebfb0:8", "const:4:8"]]
- 00aebfb0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4bd34 ["INT_ADD", "register:40f0:8", ["const:b4bd34:8", "const:4:8"]]
+ 00b4bd34 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aebfb0 bytes 38c80394
+ 00b4bd34 bytes 773b0494
- 00aebfb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00aebfb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bd3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b4bd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebfb8 bytes 609204f9
+ 00b4bd3c bytes 60f203f9
- 00aebf94 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4bd18 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aebf94 bytes b32d00b0
+ 00b4bd18 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-887f5a5a7a3911e6599c23bafb94442d"></a>

### [`00aebfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebfcc.md) → [`00b4bd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bd50.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4bd80",
      "incomplete_value": true,
      "site": "00b4bd80",
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
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebffc",
      "incomplete_value": true,
      "site": "00aebffc",
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
            "const:920:8"
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
      "definition_site": "00b4bd64",
      "incomplete_value": true,
      "site": "00b4bd64",
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
      "definition_site": "00aebfe0",
      "incomplete_value": true,
      "site": "00aebfe0",
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
      "definition_site": "00b4bd6c",
      "incomplete_value": false,
      "site": "00b4bd78",
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
            "const:8bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebfe8",
      "incomplete_value": false,
      "site": "00aebff4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:290000:8"
          ],
          [
            "leaf",
            "const:385:8"
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
      "00b4bd60",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd6c",
      "PARAM",
      [
        "storage",
        "00290385",
        null,
        "string"
      ]
    ],
    [
      "00b4bd80",
      "WRITE",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bd60",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd6c",
      "PARAM",
      [
        "storage",
        "0029f8bc",
        null,
        "string"
      ]
    ],
    [
      "00b4bd80",
      "WRITE",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebfcc.md#insn-00aebff4) · [`00aebffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebfcc.md#insn-00aebffc) · [`00aebfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebfcc.md#insn-00aebfd8)
- 新版 `00b4bd78`（命令位置の公開資料なし） · `00b4bd80`（命令位置の公開資料なし） · `00b4bd5c`（命令位置の公開資料なし）

~~~diff
- 00aebff4 ["INT_ADD", "register:40f0:8", ["const:aebff4:8", "const:4:8"]]
- 00aebff4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4bd78 ["INT_ADD", "register:40f0:8", ["const:b4bd78:8", "const:4:8"]]
+ 00b4bd78 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aebff4 bytes 27c80394
+ 00b4bd78 bytes 663b0494
- 00aebffc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
- 00aebffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bd80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b4bd80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebffc bytes 609204f9
+ 00b4bd80 bytes 60f203f9
- 00aebfd8 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4bd5c ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aebfd8 bytes b32d00b0
+ 00b4bd5c bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40da2208ae2475c67b08224f0df50066"></a>

### [`00aec01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec01c.md) → [`00b4bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bda0.md) _ZN8firebase4util4list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4be28",
      "incomplete_value": true,
      "site": "00b4be28",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec0a4",
      "incomplete_value": true,
      "site": "00aec0a4",
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
            "const:928:8"
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
      "definition_site": "00b4bdd4",
      "incomplete_value": true,
      "site": "00b4bde0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
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
      "definition_site": "00aec050",
      "incomplete_value": true,
      "site": "00aec05c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
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
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec088"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4bdb4",
      "READ",
      [
        "storage",
        "010a0928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bdd4",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be28",
      "WRITE",
      [
        "storage",
        "010a0928",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4bdb4",
      "READ",
      [
        "storage",
        "011257e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bdd4",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be28",
      "WRITE",
      [
        "storage",
        "011257e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec01c.md#insn-00aec05c) · [`00aec088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec01c.md#insn-00aec088) · [`00aec0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec01c.md#insn-00aec0a4)
- 新版 `00b4bde0`（命令位置の公開資料なし） · `00b4be28`（命令位置の公開資料なし）

~~~diff
- 00aec05c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec05c ["INT_ADD", "register:40f0:8", ["const:aec05c:8", "const:4:8"]]
- 00aec05c ["CALLIND", null, ["register:0:8"]]
+ 00b4bde0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4bde0 ["INT_ADD", "register:40f0:8", ["const:b4bde0:8", "const:4:8"]]
+ 00b4bde0 ["CALLIND", null, ["register:0:8"]]
- 00aec05c bytes 00013fd6
+ 00b4bde0 bytes 00013fd6
- 00aec088 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec088 ["INT_ADD", "register:40f0:8", ["const:aec088:8", "const:4:8"]]
- 00aec088 ["CALLIND", null, ["register:0:8"]]
- 00aec088 bytes 00013fd6
- 00aec0a4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aec0a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:928:8"]]
- 00aec0a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4be28 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4be28 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7e8:8"]]
+ 00b4be28 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aec0a4 bytes a0a22439
+ 00b4be28 bytes a0a21f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7c012a0510516ea70b907c00496208f"></a>

### [`00aec0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec0b8.md) → [`00b4be3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4be3c.md) _ZN8firebase4util4list12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00b4be78",
      "incomplete_value": true,
      "site": "00b4be78",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec0f4",
      "incomplete_value": true,
      "site": "00aec0f4",
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
            "const:928:8"
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
      "definition_site": "00b4bec8",
      "incomplete_value": true,
      "site": "00b4bec8",
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
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec144",
      "incomplete_value": true,
      "site": "00aec144",
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
            "const:920:8"
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
      "definition_site": "00b4be54",
      "incomplete_value": true,
      "site": "00b4be54",
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
      "definition_site": "00aec0d0",
      "incomplete_value": true,
      "site": "00aec0d0",
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
      "00b4be50",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be5c",
      "READ",
      [
        "storage",
        "010a0928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4be78",
      "WRITE",
      [
        "storage",
        "010a0928",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4be50",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be5c",
      "READ",
      [
        "storage",
        "011257e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4be78",
      "WRITE",
      [
        "storage",
        "011257e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec0b8.md#insn-00aec0f4) · [`00aec140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec0b8.md#insn-00aec140) · [`00aec144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec0b8.md#insn-00aec144)
- 新版 `00b4be78`（命令位置の公開資料なし） · `00b4bec4`（命令位置の公開資料なし） · `00b4bec8`（命令位置の公開資料なし）

~~~diff
- 00aec0f4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aec0f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aec0f4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:928:8"]]
- 00aec0f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4be78 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4be78 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4be78 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7e8:8"]]
+ 00b4be78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aec0f4 bytes bfa22439
+ 00b4be78 bytes bfa21f39
- 00aec140 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec140 ["INT_ADD", "register:40f0:8", ["const:aec140:8", "const:4:8"]]
- 00aec140 ["CALLIND", null, ["register:0:8"]]
+ 00b4bec4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4bec4 ["INT_ADD", "register:40f0:8", ["const:b4bec4:8", "const:4:8"]]
+ 00b4bec4 ["CALLIND", null, ["register:0:8"]]
- 00aec140 bytes 00013fd6
+ 00b4bec4 bytes 00013fd6
- 00aec144 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00aec144 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aec144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4bec8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
+ 00b4bec8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4bec8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aec144 bytes 9f9204f9
+ 00b4bec8 bytes 9ff203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-027a560a193e0d40bd7cbcb519521e75"></a>

### [`00aec158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec158.md) → [`00b4bedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bedc.md) _ZN8firebase4util4list14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aec198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4bf1c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec174"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec16c",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aec174",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4bf20"
      ]
    ],
    [
      "unmatched:00aec17c",
      "PARAM",
      [
        "storage",
        "00290385",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4bef0",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bef8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4bf20"
      ]
    ],
    [
      "00b4bf00",
      "PARAM",
      [
        "storage",
        "0029f8bc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec158.md#insn-00aec174) · [`00aec190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec158.md#insn-00aec190) · [`00aec198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec158.md#insn-00aec198)
- 新版 `00b4bf14`（命令位置の公開資料なし）

~~~diff
- 00aec174 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aec174 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00aec174 bytes 410100b5
- 00aec190 ["INT_ADD", "register:40f0:8", ["const:aec190:8", "const:4:8"]]
- 00aec190 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4bf14 ["INT_ADD", "register:40f0:8", ["const:b4bf14:8", "const:4:8"]]
+ 00b4bf14 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec190 bytes c0c70394
+ 00b4bf14 bytes ff3a0494
- 00aec198 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00aec198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec198 bytes 809204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b055fb9ae4561a1d51ebcb08156b05d3"></a>

### [`00aec1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec1c8.md) → [`00b4bf4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bf4c.md) _ZN8firebase4util4list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6a0.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5b120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b120.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b4bf68",
      "incomplete_value": false,
      "site": "00b4bf6c",
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
      "definition_site": "00aec1e4",
      "incomplete_value": false,
      "site": "00aec1e8",
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
      "definition_site": "00b4bf78",
      "incomplete_value": true,
      "site": "00b4bf84",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec1f4",
      "incomplete_value": true,
      "site": "00aec200",
      "value": [
        "LOAD",
        "8",
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
      "00b4bf68",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4bf78",
      "DATA",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bf68",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4bf78",
      "DATA",
      [
        "storage",
        "011257f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec1c8.md#insn-00aec1e8) · [`00aec1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec1c8.md#insn-00aec1e0) · [`00aec1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec1c8.md#insn-00aec1e4)
- 新版 `00b4bf6c`（命令位置の公開資料なし） · `00b4bf64`（命令位置の公開資料なし） · `00b4bf68`（命令位置の公開資料なし）

~~~diff
- 00aec1e8 ["INT_ADD", "register:40f0:8", ["const:aec1e8:8", "const:4:8"]]
- 00aec1e8 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4bf6c ["INT_ADD", "register:40f0:8", ["const:b4bf6c:8", "const:4:8"]]
+ 00b4bf6c ["CALL", null, ["callee:00c5ac00:8"]]
- 00aec1e8 bytes e6c70394
+ 00b4bf6c bytes 253b0494
- 00aec1e0 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4bf64 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aec1e0 bytes 60bdff90
+ 00b4bf64 bytes e0baffb0
- 00aec1e4 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aec1e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec1e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec1e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4bf68 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4bf68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bf68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bf68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec1e4 bytes 001c1591
+ 00b4bf68 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44e8c6210fc36fc9cf591870d7db09f6"></a>

### [`00aec204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec204.md) → [`00b4bf88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4bf88.md) _ZN8firebase4util4list13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aec244"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4bfc8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec220"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec218",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aec220",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4bfcc"
      ]
    ],
    [
      "unmatched:00aec228",
      "PARAM",
      [
        "storage",
        "00290385",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4bf9c",
      "READ",
      [
        "storage",
        "011257e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bfa4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4bfcc"
      ]
    ],
    [
      "00b4bfac",
      "PARAM",
      [
        "storage",
        "0029f8bc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec204.md#insn-00aec220) · [`00aec23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec204.md#insn-00aec23c) · [`00aec244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec204.md#insn-00aec244)
- 新版 `00b4bfc0`（命令位置の公開資料なし）

~~~diff
- 00aec220 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aec220 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aec220 bytes 410100b5
- 00aec23c ["INT_ADD", "register:40f0:8", ["const:aec23c:8", "const:4:8"]]
- 00aec23c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4bfc0 ["INT_ADD", "register:40f0:8", ["const:b4bfc0:8", "const:4:8"]]
+ 00b4bfc0 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec23c bytes 95c70394
+ 00b4bfc0 bytes d43a0494
- 00aec244 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
- 00aec244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec244 bytes 809204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-575cd41e6edce4f75de0801897211b03"></a>

### [`00aec2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2b0.md) → [`00b4c034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c034.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c060",
      "incomplete_value": true,
      "site": "00b4c060",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec2dc",
      "incomplete_value": true,
      "site": "00aec2dc",
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
            "const:950:8"
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
      "definition_site": "00b4c048",
      "incomplete_value": true,
      "site": "00b4c048",
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
      "definition_site": "00aec2c4",
      "incomplete_value": true,
      "site": "00aec2c4",
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
      "definition_site": "00b4c054",
      "incomplete_value": false,
      "site": "00b4c058",
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
            "const:a6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec2d0",
      "incomplete_value": false,
      "site": "00aec2d4",
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
            "const:df0:8"
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
      "00b4c044",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c054",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ],
    [
      "00b4c060",
      "WRITE",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c044",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c054",
      "PARAM",
      [
        "storage",
        "002b8a6c",
        null,
        "string"
      ]
    ],
    [
      "00b4c060",
      "WRITE",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2b0.md#insn-00aec2d4) · [`00aec2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2b0.md#insn-00aec2dc) · [`00aec2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2b0.md#insn-00aec2bc)
- 新版 `00b4c058`（命令位置の公開資料なし） · `00b4c060`（命令位置の公開資料なし） · `00b4c040`（命令位置の公開資料なし）

~~~diff
- 00aec2d4 ["INT_ADD", "register:40f0:8", ["const:aec2d4:8", "const:4:8"]]
- 00aec2d4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c058 ["INT_ADD", "register:40f0:8", ["const:b4c058:8", "const:4:8"]]
+ 00b4c058 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec2d4 bytes 6fc70394
+ 00b4c058 bytes ae3a0494
- 00aec2dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
- 00aec2dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c060 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00b4c060 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec2dc bytes 60aa04f9
+ 00b4c060 bytes 600a04f9
- 00aec2bc ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4c040 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aec2bc bytes b32d0090
+ 00b4c040 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e33fd1bdc81794c1fb74b7cfc4139d95"></a>

### [`00aec2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2f0.md) → [`00b4c074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c074.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c0a0",
      "incomplete_value": true,
      "site": "00b4c0a0",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec31c",
      "incomplete_value": true,
      "site": "00aec31c",
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
            "const:950:8"
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
      "definition_site": "00b4c088",
      "incomplete_value": true,
      "site": "00b4c088",
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
      "definition_site": "00aec304",
      "incomplete_value": true,
      "site": "00aec304",
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
      "definition_site": "00b4c090",
      "incomplete_value": false,
      "site": "00b4c098",
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
            "const:a6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec30c",
      "incomplete_value": false,
      "site": "00aec314",
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
            "const:df0:8"
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
      "00b4c084",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c090",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ],
    [
      "00b4c0a0",
      "WRITE",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c084",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c090",
      "PARAM",
      [
        "storage",
        "002b8a6c",
        null,
        "string"
      ]
    ],
    [
      "00b4c0a0",
      "WRITE",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2f0.md#insn-00aec314) · [`00aec31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2f0.md#insn-00aec31c) · [`00aec2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2f0.md#insn-00aec2fc)
- 新版 `00b4c098`（命令位置の公開資料なし） · `00b4c0a0`（命令位置の公開資料なし） · `00b4c080`（命令位置の公開資料なし）

~~~diff
- 00aec314 ["INT_ADD", "register:40f0:8", ["const:aec314:8", "const:4:8"]]
- 00aec314 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c098 ["INT_ADD", "register:40f0:8", ["const:b4c098:8", "const:4:8"]]
+ 00b4c098 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec314 bytes 5fc70394
+ 00b4c098 bytes 9e3a0494
- 00aec31c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
- 00aec31c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00b4c0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec31c bytes 60aa04f9
+ 00b4c0a0 bytes 600a04f9
- 00aec2fc ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4c080 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aec2fc bytes b32d0090
+ 00b4c080 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a40fe5fcf666a2d25036874a8170d498"></a>

### [`00aec330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec330.md) → [`00b4c0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c0b4.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c0e4",
      "incomplete_value": true,
      "site": "00b4c0e4",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec360",
      "incomplete_value": true,
      "site": "00aec360",
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
            "const:950:8"
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
      "definition_site": "00b4c0c8",
      "incomplete_value": true,
      "site": "00b4c0c8",
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
      "definition_site": "00aec344",
      "incomplete_value": true,
      "site": "00aec344",
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
      "definition_site": "00b4c0d4",
      "incomplete_value": false,
      "site": "00b4c0dc",
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
            "const:a6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec350",
      "incomplete_value": false,
      "site": "00aec358",
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
            "const:df0:8"
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
      "00b4c0c4",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c0d4",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ],
    [
      "00b4c0e4",
      "WRITE",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c0c4",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c0d4",
      "PARAM",
      [
        "storage",
        "002b8a6c",
        null,
        "string"
      ]
    ],
    [
      "00b4c0e4",
      "WRITE",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec330.md#insn-00aec358) · [`00aec360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec330.md#insn-00aec360) · [`00aec33c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec330.md#insn-00aec33c)
- 新版 `00b4c0dc`（命令位置の公開資料なし） · `00b4c0e4`（命令位置の公開資料なし） · `00b4c0c0`（命令位置の公開資料なし）

~~~diff
- 00aec358 ["INT_ADD", "register:40f0:8", ["const:aec358:8", "const:4:8"]]
- 00aec358 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c0dc ["INT_ADD", "register:40f0:8", ["const:b4c0dc:8", "const:4:8"]]
+ 00b4c0dc ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec358 bytes 4ec70394
+ 00b4c0dc bytes 8d3a0494
- 00aec360 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
- 00aec360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c0e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00b4c0e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec360 bytes 60aa04f9
+ 00b4c0e4 bytes 600a04f9
- 00aec33c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4c0c0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aec33c bytes b32d0090
+ 00b4c0c0 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f30893e780a91c821c5da952f3142add"></a>

### [`00aec374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec374.md) → [`00b4c0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c0f8.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c128",
      "incomplete_value": true,
      "site": "00b4c128",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec3a4",
      "incomplete_value": true,
      "site": "00aec3a4",
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
            "const:950:8"
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
      "definition_site": "00b4c10c",
      "incomplete_value": true,
      "site": "00b4c10c",
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
      "definition_site": "00aec388",
      "incomplete_value": true,
      "site": "00aec388",
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
      "definition_site": "00b4c114",
      "incomplete_value": false,
      "site": "00b4c120",
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
            "const:a6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec390",
      "incomplete_value": false,
      "site": "00aec39c",
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
            "const:df0:8"
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
      "00b4c108",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c114",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ],
    [
      "00b4c128",
      "WRITE",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c108",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c114",
      "PARAM",
      [
        "storage",
        "002b8a6c",
        null,
        "string"
      ]
    ],
    [
      "00b4c128",
      "WRITE",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec374.md#insn-00aec39c) · [`00aec3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec374.md#insn-00aec3a4) · [`00aec380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec374.md#insn-00aec380)
- 新版 `00b4c120`（命令位置の公開資料なし） · `00b4c128`（命令位置の公開資料なし） · `00b4c104`（命令位置の公開資料なし）

~~~diff
- 00aec39c ["INT_ADD", "register:40f0:8", ["const:aec39c:8", "const:4:8"]]
- 00aec39c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c120 ["INT_ADD", "register:40f0:8", ["const:b4c120:8", "const:4:8"]]
+ 00b4c120 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec39c bytes 3dc70394
+ 00b4c120 bytes 7c3a0494
- 00aec3a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
- 00aec3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c128 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00b4c128 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec3a4 bytes 60aa04f9
+ 00b4c128 bytes 600a04f9
- 00aec380 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4c104 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aec380 bytes b32d0090
+ 00b4c104 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c64e254b4a3a9a0da54dfda4842e0e42"></a>

### [`00aec3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec3c4.md) → [`00b4c148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c148.md) _ZN8firebase4util10long_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4c1d0",
      "incomplete_value": true,
      "site": "00b4c1d0",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec44c",
      "incomplete_value": true,
      "site": "00aec44c",
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
            "const:958:8"
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
      "definition_site": "00b4c17c",
      "incomplete_value": true,
      "site": "00b4c188",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
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
    "old": {
      "definition_site": "00aec3f8",
      "incomplete_value": true,
      "site": "00aec404",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:950:8"
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
      "00b4c15c",
      "READ",
      [
        "storage",
        "010a0958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c17c",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c1d0",
      "WRITE",
      [
        "storage",
        "010a0958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c15c",
      "READ",
      [
        "storage",
        "01125818",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c17c",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c1d0",
      "WRITE",
      [
        "storage",
        "01125818",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec3c4.md#insn-00aec404) · [`00aec44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec3c4.md#insn-00aec44c) · [`00aec3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec3c4.md#insn-00aec3d4)
- 新版 `00b4c188`（命令位置の公開資料なし） · `00b4c1d0`（命令位置の公開資料なし） · `00b4c158`（命令位置の公開資料なし）

~~~diff
- 00aec404 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec404 ["INT_ADD", "register:40f0:8", ["const:aec404:8", "const:4:8"]]
- 00aec404 ["CALLIND", null, ["register:0:8"]]
+ 00b4c188 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c188 ["INT_ADD", "register:40f0:8", ["const:b4c188:8", "const:4:8"]]
+ 00b4c188 ["CALLIND", null, ["register:0:8"]]
- 00aec404 bytes 00013fd6
+ 00b4c188 bytes 00013fd6
- 00aec44c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aec44c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:958:8"]]
- 00aec44c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4c1d0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4c1d0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:818:8"]]
+ 00b4c1d0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aec44c bytes a0622539
+ 00b4c1d0 bytes a0622039
- 00aec3d4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4c158 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00aec3d4 bytes b52d0090
+ 00b4c158 bytes d52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a4d02207846f23103868c4d593d79e3"></a>

### [`00aec460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec460.md) → [`00b4c1e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c1e4.md) _ZN8firebase4util10long_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4c220",
      "incomplete_value": true,
      "site": "00b4c220",
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
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec49c",
      "incomplete_value": true,
      "site": "00aec49c",
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
            "const:958:8"
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
      "definition_site": "00b4c270",
      "incomplete_value": true,
      "site": "00b4c270",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec4ec",
      "incomplete_value": true,
      "site": "00aec4ec",
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
            "const:950:8"
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
      "definition_site": "00b4c1fc",
      "incomplete_value": true,
      "site": "00b4c1fc",
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
      "definition_site": "00aec478",
      "incomplete_value": true,
      "site": "00aec478",
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
      "00b4c1f8",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c204",
      "READ",
      [
        "storage",
        "010a0958",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c220",
      "WRITE",
      [
        "storage",
        "010a0958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c1f8",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c204",
      "READ",
      [
        "storage",
        "01125818",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c220",
      "WRITE",
      [
        "storage",
        "01125818",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec460.md#insn-00aec478) · [`00aec49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec460.md#insn-00aec49c) · [`00aec4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec460.md#insn-00aec4e8)
- 新版 `00b4c1fc`（命令位置の公開資料なし） · `00b4c220`（命令位置の公開資料なし） · `00b4c26c`（命令位置の公開資料なし）

~~~diff
- 00aec478 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aec478 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b4c1fc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b4c1fc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00aec478 bytes c10300b4
+ 00b4c1fc bytes c10300b4
- 00aec49c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aec49c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aec49c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:958:8"]]
- 00aec49c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4c220 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4c220 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4c220 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:818:8"]]
+ 00b4c220 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aec49c bytes bf622539
+ 00b4c220 bytes bf622039
- 00aec4e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec4e8 ["INT_ADD", "register:40f0:8", ["const:aec4e8:8", "const:4:8"]]
- 00aec4e8 ["CALLIND", null, ["register:0:8"]]
+ 00b4c26c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c26c ["INT_ADD", "register:40f0:8", ["const:b4c26c:8", "const:4:8"]]
+ 00b4c26c ["CALLIND", null, ["register:0:8"]]
- 00aec4e8 bytes 00013fd6
+ 00b4c26c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad47c79469b566e24816bd7f7720114c"></a>

### [`00aec500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec500.md) → [`00b4c284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c284.md) _ZN8firebase4util10long_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aec540"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4c2c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec51c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec514",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aec51c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c2c8"
      ]
    ],
    [
      "unmatched:00aec524",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4c298",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c2a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c2c8"
      ]
    ],
    [
      "00b4c2a8",
      "PARAM",
      [
        "storage",
        "002b8a6c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec500.md#insn-00aec51c) · [`00aec538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec500.md#insn-00aec538) · [`00aec540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec500.md#insn-00aec540)
- 新版 `00b4c2bc`（命令位置の公開資料なし）

~~~diff
- 00aec51c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aec51c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aec51c bytes 410100b5
- 00aec538 ["INT_ADD", "register:40f0:8", ["const:aec538:8", "const:4:8"]]
- 00aec538 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c2bc ["INT_ADD", "register:40f0:8", ["const:b4c2bc:8", "const:4:8"]]
+ 00b4c2bc ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec538 bytes d6c60394
+ 00b4c2bc bytes 153a0494
- 00aec540 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:950:8"]]
- 00aec540 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec540 bytes 80aa04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cabb945003553e841b42e3e9858e9f3d"></a>

### [`00aec570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec570.md) → [`00b4c2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c2f4.md) _ZN8firebase4util10long_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3f0.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5ae70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ae70.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b4c310",
      "incomplete_value": false,
      "site": "00b4c314",
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
      "definition_site": "00aec58c",
      "incomplete_value": false,
      "site": "00aec590",
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
      "definition_site": "00b4c320",
      "incomplete_value": true,
      "site": "00b4c32c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec59c",
      "incomplete_value": true,
      "site": "00aec5a8",
      "value": [
        "LOAD",
        "8",
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
      "00b4c310",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4c320",
      "DATA",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c310",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4c320",
      "DATA",
      [
        "storage",
        "01125820",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec570.md#insn-00aec590) · [`00aec588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec570.md#insn-00aec588) · [`00aec58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec570.md#insn-00aec58c)
- 新版 `00b4c314`（命令位置の公開資料なし） · `00b4c30c`（命令位置の公開資料なし） · `00b4c310`（命令位置の公開資料なし）

~~~diff
- 00aec590 ["INT_ADD", "register:40f0:8", ["const:aec590:8", "const:4:8"]]
- 00aec590 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4c314 ["INT_ADD", "register:40f0:8", ["const:b4c314:8", "const:4:8"]]
+ 00b4c314 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aec590 bytes fcc60394
+ 00b4c314 bytes 3b3a0494
- 00aec588 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4c30c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aec588 bytes 60bdff90
+ 00b4c30c bytes e0baff90
- 00aec58c ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aec58c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec58c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec58c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c310 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4c310 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c310 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c310 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec58c bytes 001c1591
+ 00b4c310 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f09b63e75f6883fdef067fc36aa4120a"></a>

### [`00aec5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec5ac.md) → [`00b4c330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c330.md) _ZN8firebase4util10long_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c370",
      "incomplete_value": true,
      "site": "00b4c370",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec5ec",
      "incomplete_value": true,
      "site": "00aec5ec",
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
            "const:950:8"
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
      "definition_site": "00b4c34c",
      "incomplete_value": true,
      "site": "00b4c34c",
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
      "definition_site": "00aec5c8",
      "incomplete_value": true,
      "site": "00aec5c8",
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
      "definition_site": "00b4c354",
      "incomplete_value": false,
      "site": "00b4c368",
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
            "const:a6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec5d0",
      "incomplete_value": false,
      "site": "00aec5e4",
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
            "const:df0:8"
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
      "00b4c344",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c354",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ],
    [
      "00b4c370",
      "WRITE",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c344",
      "READ",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c354",
      "PARAM",
      [
        "storage",
        "002b8a6c",
        null,
        "string"
      ]
    ],
    [
      "00b4c370",
      "WRITE",
      [
        "storage",
        "01125810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec5ac.md#insn-00aec5e4) · [`00aec5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec5ac.md#insn-00aec5ec) · [`00aec5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec5ac.md#insn-00aec5b8)
- 新版 `00b4c368`（命令位置の公開資料なし） · `00b4c370`（命令位置の公開資料なし） · `00b4c33c`（命令位置の公開資料なし）

~~~diff
- 00aec5e4 ["INT_ADD", "register:40f0:8", ["const:aec5e4:8", "const:4:8"]]
- 00aec5e4 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c368 ["INT_ADD", "register:40f0:8", ["const:b4c368:8", "const:4:8"]]
+ 00b4c368 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec5e4 bytes abc60394
+ 00b4c368 bytes ea390494
- 00aec5ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:950:8"]]
- 00aec5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
+ 00b4c370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec5ec bytes 80aa04f9
+ 00b4c370 bytes 800a04f9
- 00aec5b8 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4c33c ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aec5b8 bytes b42d0090
+ 00b4c33c bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58c18b431b158fd84698b1731c2e7526"></a>

### [`00aec61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec61c.md) → [`00b4c3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c3a0.md) _ZN8firebase4util10long_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c3bc",
      "incomplete_value": false,
      "site": "00b4c3c0",
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
      "definition_site": "00aec638",
      "incomplete_value": false,
      "site": "00aec63c",
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
      "definition_site": "00b4c3cc",
      "incomplete_value": true,
      "site": "00b4c3d8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec648",
      "incomplete_value": true,
      "site": "00aec654",
      "value": [
        "LOAD",
        "8",
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
      "00b4c3bc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4c3cc",
      "DATA",
      [
        "storage",
        "010a0970",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4c3bc",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4c3cc",
      "DATA",
      [
        "storage",
        "01125830",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec61c.md#insn-00aec63c) · [`00aec634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec61c.md#insn-00aec634) · [`00aec638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec61c.md#insn-00aec638)
- 新版 `00b4c3c0`（命令位置の公開資料なし） · `00b4c3b8`（命令位置の公開資料なし） · `00b4c3bc`（命令位置の公開資料なし）

~~~diff
- 00aec63c ["INT_ADD", "register:40f0:8", ["const:aec63c:8", "const:4:8"]]
- 00aec63c ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4c3c0 ["INT_ADD", "register:40f0:8", ["const:b4c3c0:8", "const:4:8"]]
+ 00b4c3c0 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aec63c bytes d1c60394
+ 00b4c3c0 bytes 103a0494
- 00aec634 ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4c3b8 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aec634 bytes 60bdffb0
+ 00b4c3b8 bytes e0baffb0
- 00aec638 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aec638 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec638 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec638 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c3bc ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4c3bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c3bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c3bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec638 bytes 00c81791
+ 00b4c3bc bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4779efff5234cabdded22d3a18f7b095"></a>

### [`00aec658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec658.md) → [`00b4c3dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c3dc.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c408",
      "incomplete_value": true,
      "site": "00b4c408",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec684",
      "incomplete_value": true,
      "site": "00aec684",
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
            "const:978:8"
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
      "definition_site": "00b4c3f0",
      "incomplete_value": true,
      "site": "00b4c3f0",
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
      "definition_site": "00aec66c",
      "incomplete_value": true,
      "site": "00aec66c",
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
      "definition_site": "00b4c3fc",
      "incomplete_value": false,
      "site": "00b4c400",
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
            "const:59a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec678",
      "incomplete_value": false,
      "site": "00aec67c",
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
            "const:f85:8"
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
      "00b4c3ec",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c3fc",
      "PARAM",
      [
        "storage",
        "002a0f85",
        null,
        "string"
      ]
    ],
    [
      "00b4c408",
      "WRITE",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c3ec",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c3fc",
      "PARAM",
      [
        "storage",
        "002b159a",
        null,
        "string"
      ]
    ],
    [
      "00b4c408",
      "WRITE",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec658.md#insn-00aec67c) · [`00aec684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec658.md#insn-00aec684) · [`00aec664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec658.md#insn-00aec664)
- 新版 `00b4c400`（命令位置の公開資料なし） · `00b4c408`（命令位置の公開資料なし） · `00b4c3e8`（命令位置の公開資料なし）

~~~diff
- 00aec67c ["INT_ADD", "register:40f0:8", ["const:aec67c:8", "const:4:8"]]
- 00aec67c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c400 ["INT_ADD", "register:40f0:8", ["const:b4c400:8", "const:4:8"]]
+ 00b4c400 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec67c bytes 85c60394
+ 00b4c400 bytes c4390494
- 00aec684 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
- 00aec684 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c408 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:838:8"]]
+ 00b4c408 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec684 bytes 60be04f9
+ 00b4c408 bytes 601e04f9
- 00aec664 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4c3e8 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aec664 bytes b32d0090
+ 00b4c3e8 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e19acd5b03a03437f2d9646cece8e0e9"></a>

### [`00aec698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec698.md) → [`00b4c41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c41c.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c448",
      "incomplete_value": true,
      "site": "00b4c448",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec6c4",
      "incomplete_value": true,
      "site": "00aec6c4",
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
            "const:978:8"
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
      "definition_site": "00b4c430",
      "incomplete_value": true,
      "site": "00b4c430",
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
      "definition_site": "00aec6ac",
      "incomplete_value": true,
      "site": "00aec6ac",
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
      "definition_site": "00b4c438",
      "incomplete_value": false,
      "site": "00b4c440",
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
            "const:59a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec6b4",
      "incomplete_value": false,
      "site": "00aec6bc",
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
            "const:f85:8"
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
      "00b4c42c",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c438",
      "PARAM",
      [
        "storage",
        "002a0f85",
        null,
        "string"
      ]
    ],
    [
      "00b4c448",
      "WRITE",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c42c",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c438",
      "PARAM",
      [
        "storage",
        "002b159a",
        null,
        "string"
      ]
    ],
    [
      "00b4c448",
      "WRITE",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec698.md#insn-00aec6bc) · [`00aec6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec698.md#insn-00aec6c4) · [`00aec6a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec698.md#insn-00aec6a4)
- 新版 `00b4c440`（命令位置の公開資料なし） · `00b4c448`（命令位置の公開資料なし） · `00b4c428`（命令位置の公開資料なし）

~~~diff
- 00aec6bc ["INT_ADD", "register:40f0:8", ["const:aec6bc:8", "const:4:8"]]
- 00aec6bc ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c440 ["INT_ADD", "register:40f0:8", ["const:b4c440:8", "const:4:8"]]
+ 00b4c440 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec6bc bytes 75c60394
+ 00b4c440 bytes b4390494
- 00aec6c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
- 00aec6c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c448 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:838:8"]]
+ 00b4c448 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec6c4 bytes 60be04f9
+ 00b4c448 bytes 601e04f9
- 00aec6a4 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4c428 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aec6a4 bytes b32d0090
+ 00b4c428 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-114446069e3118e52f851d648c22889b"></a>

### [`00aec71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec71c.md) → [`00b4c4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c4a0.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c4d0",
      "incomplete_value": true,
      "site": "00b4c4d0",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec74c",
      "incomplete_value": true,
      "site": "00aec74c",
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
            "const:978:8"
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
      "definition_site": "00b4c4b4",
      "incomplete_value": true,
      "site": "00b4c4b4",
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
      "definition_site": "00aec730",
      "incomplete_value": true,
      "site": "00aec730",
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
      "definition_site": "00b4c4bc",
      "incomplete_value": false,
      "site": "00b4c4c8",
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
            "const:59a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec738",
      "incomplete_value": false,
      "site": "00aec744",
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
            "const:f85:8"
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
      "00b4c4b0",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c4bc",
      "PARAM",
      [
        "storage",
        "002a0f85",
        null,
        "string"
      ]
    ],
    [
      "00b4c4d0",
      "WRITE",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c4b0",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c4bc",
      "PARAM",
      [
        "storage",
        "002b159a",
        null,
        "string"
      ]
    ],
    [
      "00b4c4d0",
      "WRITE",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec71c.md#insn-00aec744) · [`00aec74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec71c.md#insn-00aec74c) · [`00aec728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec71c.md#insn-00aec728)
- 新版 `00b4c4c8`（命令位置の公開資料なし） · `00b4c4d0`（命令位置の公開資料なし） · `00b4c4ac`（命令位置の公開資料なし）

~~~diff
- 00aec744 ["INT_ADD", "register:40f0:8", ["const:aec744:8", "const:4:8"]]
- 00aec744 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c4c8 ["INT_ADD", "register:40f0:8", ["const:b4c4c8:8", "const:4:8"]]
+ 00b4c4c8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec744 bytes 53c60394
+ 00b4c4c8 bytes 92390494
- 00aec74c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
- 00aec74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c4d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:838:8"]]
+ 00b4c4d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec74c bytes 60be04f9
+ 00b4c4d0 bytes 601e04f9
- 00aec728 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4c4ac ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aec728 bytes b32d0090
+ 00b4c4ac bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96388a4f963c643280c038be71e9ad6b"></a>

### [`00aec76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec76c.md) → [`00b4c4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c4f0.md) _ZN8firebase4util3map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4c578",
      "incomplete_value": true,
      "site": "00b4c578",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec7f4",
      "incomplete_value": true,
      "site": "00aec7f4",
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
            "const:980:8"
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
      "site": "00aec7ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec7d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c504",
      "READ",
      [
        "storage",
        "010a0980",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aec7a0",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c578",
      "WRITE",
      [
        "storage",
        "010a0980",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c504",
      "READ",
      [
        "storage",
        "01125840",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c524",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c578",
      "WRITE",
      [
        "storage",
        "01125840",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec76c.md#insn-00aec7ac) · [`00aec7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec76c.md#insn-00aec7d8) · [`00aec7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec76c.md#insn-00aec7f4)
- 新版 `00b4c578`（命令位置の公開資料なし）

~~~diff
- 00aec7ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec7ac ["INT_ADD", "register:40f0:8", ["const:aec7ac:8", "const:4:8"]]
- 00aec7ac ["CALLIND", null, ["register:0:8"]]
- 00aec7ac bytes 00013fd6
- 00aec7d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec7d8 ["INT_ADD", "register:40f0:8", ["const:aec7d8:8", "const:4:8"]]
- 00aec7d8 ["CALLIND", null, ["register:0:8"]]
- 00aec7d8 bytes 00013fd6
- 00aec7f4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aec7f4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:980:8"]]
- 00aec7f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4c578 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4c578 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:840:8"]]
+ 00b4c578 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aec7f4 bytes a0022639
+ 00b4c578 bytes a0022139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d62ac27df7a34f2abace74856d25a07"></a>

### [`00aec808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec808.md) → [`00b4c58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c58c.md) _ZN8firebase4util3map12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec80c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec80c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec808",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec80c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec810",
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
      "00b4c58c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4c590",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4c594",
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

- 旧版 [`00aec808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec808.md#insn-00aec808) · [`00aec80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec808.md#insn-00aec80c) · [`00aec810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec808.md#insn-00aec810)

~~~diff
- 00aec808 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aec808 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aec808 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aec808 bytes f50f1df8
- 00aec80c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aec80c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aec80c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aec80c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec80c bytes f44f01a9
- 00aec810 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aec810 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aec810 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aec810 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec810 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eade8f15a35eb9f84ab68baefbb567cc"></a>

### [`00aec8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec8a8.md) → [`00b4c62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c62c.md) _ZN8firebase4util3map14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

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
      "definition_site": "00b4c66c",
      "incomplete_value": true,
      "site": "00b4c66c",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec8e8",
      "incomplete_value": true,
      "site": "00aec8e8",
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
            "const:978:8"
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
      "definition_site": "00b4c648",
      "incomplete_value": true,
      "site": "00b4c648",
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
      "definition_site": "00aec8c4",
      "incomplete_value": true,
      "site": "00aec8c4",
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
      "definition_site": "00b4c650",
      "incomplete_value": false,
      "site": "00b4c664",
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
            "const:59a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec8cc",
      "incomplete_value": false,
      "site": "00aec8e0",
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
            "const:f85:8"
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
      "00b4c640",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c650",
      "PARAM",
      [
        "storage",
        "002a0f85",
        null,
        "string"
      ]
    ],
    [
      "00b4c66c",
      "WRITE",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c640",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c650",
      "PARAM",
      [
        "storage",
        "002b159a",
        null,
        "string"
      ]
    ],
    [
      "00b4c66c",
      "WRITE",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec8a8.md#insn-00aec8e0) · [`00aec8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec8a8.md#insn-00aec8e8) · [`00aec8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec8a8.md#insn-00aec8b4)
- 新版 `00b4c664`（命令位置の公開資料なし） · `00b4c66c`（命令位置の公開資料なし） · `00b4c638`（命令位置の公開資料なし）

~~~diff
- 00aec8e0 ["INT_ADD", "register:40f0:8", ["const:aec8e0:8", "const:4:8"]]
- 00aec8e0 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c664 ["INT_ADD", "register:40f0:8", ["const:b4c664:8", "const:4:8"]]
+ 00b4c664 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec8e0 bytes ecc50394
+ 00b4c664 bytes 2b390494
- 00aec8e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:978:8"]]
- 00aec8e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c66c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:838:8"]]
+ 00b4c66c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec8e8 bytes 80be04f9
+ 00b4c66c bytes 801e04f9
- 00aec8b4 ["COPY", "register:40a0:8", ["const:10a0000:8"]]
+ 00b4c638 ["COPY", "register:40a0:8", ["const:1125000:8"]]
- 00aec8b4 bytes b42d0090
+ 00b4c638 bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79194b7e4be843c577d0ca43a093e2f3"></a>

### [`00aec918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec918.md) → [`00b4c69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c69c.md) _ZN8firebase4util3map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde100.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)
- 新版 呼出元 1件 [`00c5ab80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab80.md) · 呼出先 1件 [`00c5ac00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ac00.md)

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
      "definition_site": "00b4c6b8",
      "incomplete_value": false,
      "site": "00b4c6bc",
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
      "definition_site": "00aec934",
      "incomplete_value": false,
      "site": "00aec938",
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
      "definition_site": "00b4c6c8",
      "incomplete_value": true,
      "site": "00b4c6d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec944",
      "incomplete_value": true,
      "site": "00aec950",
      "value": [
        "LOAD",
        "8",
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
      "00b4c6b8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4c6c8",
      "DATA",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c6b8",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4c6c8",
      "DATA",
      [
        "storage",
        "01125848",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec918.md#insn-00aec938) · [`00aec930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec918.md#insn-00aec930) · [`00aec934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec918.md#insn-00aec934)
- 新版 `00b4c6bc`（命令位置の公開資料なし） · `00b4c6b4`（命令位置の公開資料なし） · `00b4c6b8`（命令位置の公開資料なし）

~~~diff
- 00aec938 ["INT_ADD", "register:40f0:8", ["const:aec938:8", "const:4:8"]]
- 00aec938 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4c6bc ["INT_ADD", "register:40f0:8", ["const:b4c6bc:8", "const:4:8"]]
+ 00b4c6bc ["CALL", null, ["callee:00c5ac00:8"]]
- 00aec938 bytes 12c60394
+ 00b4c6bc bytes 51390494
- 00aec930 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4c6b4 ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aec930 bytes 60bdff90
+ 00b4c6b4 bytes e0baff90
- 00aec934 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aec934 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec934 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec934 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c6b8 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4c6b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c6b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c6b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec934 bytes 001c1591
+ 00b4c6b8 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0440aaae79b2b6556498ebf069e82824"></a>

### [`00aec954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec954.md) → [`00b4c6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c6d8.md) _ZN8firebase4util3map13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00aec994"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4c718"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec970"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec968",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aec970",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c71c"
      ]
    ],
    [
      "unmatched:00aec978",
      "PARAM",
      [
        "storage",
        "002a0f85",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4c6ec",
      "READ",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c6f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4c71c"
      ]
    ],
    [
      "00b4c6fc",
      "PARAM",
      [
        "storage",
        "002b159a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec954.md#insn-00aec970) · [`00aec98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec954.md#insn-00aec98c) · [`00aec994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec954.md#insn-00aec994)
- 新版 `00b4c710`（命令位置の公開資料なし）

~~~diff
- 00aec970 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aec970 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aec970 bytes 410100b5
- 00aec98c ["INT_ADD", "register:40f0:8", ["const:aec98c:8", "const:4:8"]]
- 00aec98c ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c710 ["INT_ADD", "register:40f0:8", ["const:b4c710:8", "const:4:8"]]
+ 00b4c710 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aec98c bytes c1c50394
+ 00b4c710 bytes 00390494
- 00aec994 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:978:8"]]
- 00aec994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec994 bytes 80be04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24983d4dff4f2890d4ed7faf19ff1245"></a>

### [`00aec9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec9c4.md) → [`00b4c748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c748.md) _ZN8firebase4util3map10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c764",
      "incomplete_value": false,
      "site": "00b4c768",
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
      "definition_site": "00aec9e0",
      "incomplete_value": false,
      "site": "00aec9e4",
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
      "definition_site": "00b4c774",
      "incomplete_value": true,
      "site": "00b4c780",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec9f0",
      "incomplete_value": true,
      "site": "00aec9fc",
      "value": [
        "LOAD",
        "8",
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
      "00b4c764",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4c774",
      "DATA",
      [
        "storage",
        "010a09a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4c764",
      "PARAM",
      [
        "storage",
        "002a9451",
        null,
        "string"
      ]
    ],
    [
      "00b4c774",
      "DATA",
      [
        "storage",
        "01125860",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec9c4.md#insn-00aec9e4) · [`00aec9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec9c4.md#insn-00aec9dc) · [`00aec9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec9c4.md#insn-00aec9e0)
- 新版 `00b4c768`（命令位置の公開資料なし） · `00b4c760`（命令位置の公開資料なし） · `00b4c764`（命令位置の公開資料なし）

~~~diff
- 00aec9e4 ["INT_ADD", "register:40f0:8", ["const:aec9e4:8", "const:4:8"]]
- 00aec9e4 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4c768 ["INT_ADD", "register:40f0:8", ["const:b4c768:8", "const:4:8"]]
+ 00b4c768 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aec9e4 bytes e7c50394
+ 00b4c768 bytes 26390494
- 00aec9dc ["COPY", "register:4000:8", ["const:299000:8"]]
+ 00b4c760 ["COPY", "register:4000:8", ["const:2a9000:8"]]
- 00aec9dc bytes 60bdffb0
+ 00b4c760 bytes e0baffb0
- 00aec9e0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aec9e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec9e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec9e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c764 ["COPY", "tmp:0:8", ["const:451:8"]]
+ 00b4c764 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c764 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c764 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec9e0 bytes 00c81791
+ 00b4c764 bytes 00441191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03cef5fe84235f18e2249ed65c2c32fa"></a>

### [`00aeca00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca00.md) → [`00b4c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c784.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c7b0",
      "incomplete_value": true,
      "site": "00b4c7b0",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeca2c",
      "incomplete_value": true,
      "site": "00aeca2c",
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
            "const:9a8:8"
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
      "definition_site": "00b4c798",
      "incomplete_value": true,
      "site": "00b4c798",
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
      "definition_site": "00aeca14",
      "incomplete_value": true,
      "site": "00aeca14",
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
      "definition_site": "00b4c7a4",
      "incomplete_value": false,
      "site": "00b4c7a8",
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
            "const:a62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeca20",
      "incomplete_value": false,
      "site": "00aeca24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:1d3:8"
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
      "00b4c794",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c7a4",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "00b4c7b0",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c794",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c7a4",
      "PARAM",
      [
        "storage",
        "002a3a62",
        null,
        "string"
      ]
    ],
    [
      "00b4c7b0",
      "WRITE",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeca24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca00.md#insn-00aeca24) · [`00aeca2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca00.md#insn-00aeca2c) · [`00aeca0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca00.md#insn-00aeca0c)
- 新版 `00b4c7a8`（命令位置の公開資料なし） · `00b4c7b0`（命令位置の公開資料なし） · `00b4c790`（命令位置の公開資料なし）

~~~diff
- 00aeca24 ["INT_ADD", "register:40f0:8", ["const:aeca24:8", "const:4:8"]]
- 00aeca24 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c7a8 ["INT_ADD", "register:40f0:8", ["const:b4c7a8:8", "const:4:8"]]
+ 00b4c7a8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeca24 bytes 9bc50394
+ 00b4c7a8 bytes da380494
- 00aeca2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aeca2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c7b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
+ 00b4c7b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeca2c bytes 60d604f9
+ 00b4c7b0 bytes 603604f9
- 00aeca0c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4c790 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeca0c bytes b32d0090
+ 00b4c790 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd8ba624b94c5b451633234ffd8adf97"></a>

### [`00aeca40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca40.md) → [`00b4c7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c7c4.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c7f0",
      "incomplete_value": true,
      "site": "00b4c7f0",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeca6c",
      "incomplete_value": true,
      "site": "00aeca6c",
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
            "const:9a8:8"
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
      "definition_site": "00b4c7d8",
      "incomplete_value": true,
      "site": "00b4c7d8",
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
      "definition_site": "00aeca54",
      "incomplete_value": true,
      "site": "00aeca54",
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
      "definition_site": "00b4c7e0",
      "incomplete_value": false,
      "site": "00b4c7e8",
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
            "const:a62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeca5c",
      "incomplete_value": false,
      "site": "00aeca64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:1d3:8"
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
      "00b4c7d4",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c7e0",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "00b4c7f0",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c7d4",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c7e0",
      "PARAM",
      [
        "storage",
        "002a3a62",
        null,
        "string"
      ]
    ],
    [
      "00b4c7f0",
      "WRITE",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeca64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca40.md#insn-00aeca64) · [`00aeca6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca40.md#insn-00aeca6c) · [`00aeca4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca40.md#insn-00aeca4c)
- 新版 `00b4c7e8`（命令位置の公開資料なし） · `00b4c7f0`（命令位置の公開資料なし） · `00b4c7d0`（命令位置の公開資料なし）

~~~diff
- 00aeca64 ["INT_ADD", "register:40f0:8", ["const:aeca64:8", "const:4:8"]]
- 00aeca64 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c7e8 ["INT_ADD", "register:40f0:8", ["const:b4c7e8:8", "const:4:8"]]
+ 00b4c7e8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aeca64 bytes 8bc50394
+ 00b4c7e8 bytes ca380494
- 00aeca6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aeca6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c7f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
+ 00b4c7f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeca6c bytes 60d604f9
+ 00b4c7f0 bytes 603604f9
- 00aeca4c ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4c7d0 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aeca4c bytes b32d0090
+ 00b4c7d0 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-789154d7fdc9dc82a1534c4decd5e554"></a>

### [`00aeca80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca80.md) → [`00b4c804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c804.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

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
      "site": "00aecab0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4c834"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4c818",
      "incomplete_value": true,
      "site": "00b4c818",
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
      "definition_site": "00aeca94",
      "incomplete_value": true,
      "site": "00aeca94",
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
      "00b4c814",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aecaa0",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aecaa8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5ab10"
      ]
    ]
  ],
  "added": [
    [
      "00b4c814",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c824",
      "PARAM",
      [
        "storage",
        "002a3a62",
        null,
        "string"
      ]
    ],
    [
      "00b4c82c",
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

- 旧版 [`00aeca94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca80.md#insn-00aeca94) · [`00aecaa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca80.md#insn-00aecaa8) · [`00aecab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca80.md#insn-00aecab0)
- 新版 `00b4c818`（命令位置の公開資料なし）

~~~diff
- 00aeca94 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aeca94 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00b4c818 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b4c818 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeca94 bytes 080100b5
+ 00b4c818 bytes 080100b5
- 00aecaa8 ["INT_ADD", "register:40f0:8", ["const:aecaa8:8", "const:4:8"]]
- 00aecaa8 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aecaa8 bytes 7ac50394
- 00aecab0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aecab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecab0 bytes 60d604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dea1f423a830737a6fbefb020d17a777"></a>

### [`00aecac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecac4.md) → [`00b4c848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c848.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4c878",
      "incomplete_value": true,
      "site": "00b4c878",
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
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecaf4",
      "incomplete_value": true,
      "site": "00aecaf4",
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
            "const:9a8:8"
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
      "definition_site": "00b4c85c",
      "incomplete_value": true,
      "site": "00b4c85c",
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
      "definition_site": "00aecad8",
      "incomplete_value": true,
      "site": "00aecad8",
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
      "definition_site": "00b4c864",
      "incomplete_value": false,
      "site": "00b4c870",
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
            "const:a62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecae0",
      "incomplete_value": false,
      "site": "00aecaec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:1d3:8"
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
      "00b4c858",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c864",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "00b4c878",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c858",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c864",
      "PARAM",
      [
        "storage",
        "002a3a62",
        null,
        "string"
      ]
    ],
    [
      "00b4c878",
      "WRITE",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecaec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecac4.md#insn-00aecaec) · [`00aecaf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecac4.md#insn-00aecaf4) · [`00aecad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecac4.md#insn-00aecad0)
- 新版 `00b4c870`（命令位置の公開資料なし） · `00b4c878`（命令位置の公開資料なし） · `00b4c854`（命令位置の公開資料なし）

~~~diff
- 00aecaec ["INT_ADD", "register:40f0:8", ["const:aecaec:8", "const:4:8"]]
- 00aecaec ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4c870 ["INT_ADD", "register:40f0:8", ["const:b4c870:8", "const:4:8"]]
+ 00b4c870 ["CALL", null, ["callee:00c5ab10:8"]]
- 00aecaec bytes 69c50394
+ 00b4c870 bytes a8380494
- 00aecaf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00aecaf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c878 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
+ 00b4c878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecaf4 bytes 60d604f9
+ 00b4c878 bytes 603604f9
- 00aecad0 ["COPY", "register:4098:8", ["const:10a0000:8"]]
+ 00b4c854 ["COPY", "register:4098:8", ["const:1125000:8"]]
- 00aecad0 bytes b32d0090
+ 00b4c854 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03c6e3e892310376afa4a8e687241a67"></a>

### [`00aecb14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecb14.md) → [`00b4c898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c898.md) _ZN8firebase4util22parcel_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 62.50% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4c920",
      "incomplete_value": true,
      "site": "00b4c920",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecb9c",
      "incomplete_value": true,
      "site": "00aecb9c",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c8cc",
      "incomplete_value": true,
      "site": "00b4c8d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:868:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecb48",
      "incomplete_value": true,
      "site": "00aecb54",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:9a8:8"
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
      "00b4c8ac",
      "READ",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c8cc",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c920",
      "WRITE",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c8ac",
      "READ",
      [
        "storage",
        "01125870",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c8cc",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c920",
      "WRITE",
      [
        "storage",
        "01125870",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecb54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecb14.md#insn-00aecb54) · [`00aecb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecb14.md#insn-00aecb9c) · [`00aecb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecb14.md#insn-00aecb24)
- 新版 `00b4c8d8`（命令位置の公開資料なし） · `00b4c920`（命令位置の公開資料なし） · `00b4c8a8`（命令位置の公開資料なし）

~~~diff
- 00aecb54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aecb54 ["INT_ADD", "register:40f0:8", ["const:aecb54:8", "const:4:8"]]
- 00aecb54 ["CALLIND", null, ["register:0:8"]]
+ 00b4c8d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c8d8 ["INT_ADD", "register:40f0:8", ["const:b4c8d8:8", "const:4:8"]]
+ 00b4c8d8 ["CALLIND", null, ["register:0:8"]]
- 00aecb54 bytes 00013fd6
+ 00b4c8d8 bytes 00013fd6
- 00aecb9c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aecb9c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b0:8"]]
- 00aecb9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4c920 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4c920 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:870:8"]]
+ 00b4c920 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aecb9c bytes a0c22639
+ 00b4c920 bytes a0c22139
- 00aecb24 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4c8a8 ["COPY", "register:40a8:8", ["const:1125000:8"]]
- 00aecb24 bytes b52d0090
+ 00b4c8a8 bytes d52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b3de6611464f07478e9882884bb6a5b"></a>

### [`00aecbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecbb0.md) → [`00b4c934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c934.md) _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.50% / 新版 67.50%

CFGの説明率　旧版 10.00% / 新版 8.33%

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
      "site": "00aecbb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecbb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecbb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aecbb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aecbb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aecbb8",
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
      "00b4c934",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b4c938",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b4c93c",
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

- 旧版 [`00aecbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecbb0.md#insn-00aecbb0) · [`00aecbb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecbb0.md#insn-00aecbb4) · [`00aecbb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecbb0.md#insn-00aecbb8)

~~~diff
- 00aecbb0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aecbb0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aecbb0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aecbb0 bytes f50f1df8
- 00aecbb4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aecbb4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aecbb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aecbb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aecbb4 bytes f44f01a9
- 00aecbb8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aecbb8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aecbb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aecbb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aecbb8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a79c8fb471ca1758c1560242f6842b11"></a>

### [`00aecc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecc50.md) → [`00b4c9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4c9d4.md) _ZN8firebase4util22parcel_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5ab10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab10.md) [`00c5ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ab30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

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
      "site": "00aecc90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b4ca14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecc6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aecc64",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aecc6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ca18"
      ]
    ],
    [
      "unmatched:00aecc74",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4c9e8",
      "READ",
      [
        "storage",
        "01125868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c9f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b4ca18"
      ]
    ],
    [
      "00b4c9f8",
      "PARAM",
      [
        "storage",
        "002a3a62",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecc50.md#insn-00aecc6c) · [`00aecc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecc50.md#insn-00aecc88) · [`00aecc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecc50.md#insn-00aecc90)
- 新版 `00b4ca0c`（命令位置の公開資料なし）

~~~diff
- 00aecc6c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aecc6c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aecc6c bytes 410100b5
- 00aecc88 ["INT_ADD", "register:40f0:8", ["const:aecc88:8", "const:4:8"]]
- 00aecc88 ["CALL", null, ["callee:00c5ab10:8"]]
+ 00b4ca0c ["INT_ADD", "register:40f0:8", ["const:b4ca0c:8", "const:4:8"]]
+ 00b4ca0c ["CALL", null, ["callee:00c5ab10:8"]]
- 00aecc88 bytes 02c50394
+ 00b4ca0c bytes 41380494
- 00aecc90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00aecc90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecc90 bytes 80d604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64564501ac75ad13d75d496127138458"></a>

### [`00aeccc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccc0.md) → [`00b4ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4ca44.md) _ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x5fd84` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "00b4ca60",
      "incomplete_value": false,
      "site": "00b4ca64",
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
      "definition_site": "00aeccdc",
      "incomplete_value": false,
      "site": "00aecce0",
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
      "definition_site": "00b4ca70",
      "incomplete_value": true,
      "site": "00b4ca7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeccec",
      "incomplete_value": true,
      "site": "00aeccf8",
      "value": [
        "LOAD",
        "8",
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
      "00b4ca60",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4ca70",
      "DATA",
      [
        "storage",
        "010a09b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ca60",
      "PARAM",
      [
        "storage",
        "002a829a",
        null,
        "string"
      ]
    ],
    [
      "00b4ca70",
      "DATA",
      [
        "storage",
        "01125878",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccc0.md#insn-00aecce0) · [`00aeccd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccc0.md#insn-00aeccd8) · [`00aeccdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccc0.md#insn-00aeccdc)
- 新版 `00b4ca64`（命令位置の公開資料なし） · `00b4ca5c`（命令位置の公開資料なし） · `00b4ca60`（命令位置の公開資料なし）

~~~diff
- 00aecce0 ["INT_ADD", "register:40f0:8", ["const:aecce0:8", "const:4:8"]]
- 00aecce0 ["CALL", null, ["callee:00c5ac00:8"]]
+ 00b4ca64 ["INT_ADD", "register:40f0:8", ["const:b4ca64:8", "const:4:8"]]
+ 00b4ca64 ["CALL", null, ["callee:00c5ac00:8"]]
- 00aecce0 bytes 28c50394
+ 00b4ca64 bytes 67380494
- 00aeccd8 ["COPY", "register:4000:8", ["const:298000:8"]]
+ 00b4ca5c ["COPY", "register:4000:8", ["const:2a8000:8"]]
- 00aeccd8 bytes 60bdff90
+ 00b4ca5c bytes e0baff90
- 00aeccdc ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aeccdc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeccdc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeccdc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ca60 ["COPY", "tmp:0:8", ["const:29a:8"]]
+ 00b4ca60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ca60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ca60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeccdc bytes 001c1591
+ 00b4ca60 bytes 00680a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

