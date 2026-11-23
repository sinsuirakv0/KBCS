# v15.7.2 → v15.7.3 · 最優先の変更候補 (47)

[一覧の目次](README.md)

<a id="compare-a357cd360c3759c0fc3929eeec9b6f07"></a>

### [`008ed544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed544.md) → [`008ed544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed544.md) FUN_008ed544

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008ed568",
      "incomplete_value": false,
      "site": "008ed568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed568",
      "incomplete_value": false,
      "site": "008ed568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "008ed568",
      "DATA",
      [
        "storage",
        "00c07bb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed568",
      "DATA",
      [
        "storage",
        "00c07c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed544.md#insn-008ed564)
- 新版 [`008ed564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed544.md#insn-008ed564)

~~~diff
- 008ed564 ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 008ed564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ed564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ed564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ed564 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 008ed564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ed564 bytes 08e12e91
+ 008ed564 bytes 08a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77d24d65539a992a6dd5debbedc7d870"></a>

### [`008ed578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed578.md) → [`008ed578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed578.md) FUN_008ed578

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ed584",
      "incomplete_value": false,
      "site": "008ed584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed584",
      "incomplete_value": false,
      "site": "008ed584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "008ed584",
      "DATA",
      [
        "storage",
        "00c07bb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed584",
      "DATA",
      [
        "storage",
        "00c07c68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed578.md#insn-008ed580)
- 新版 [`008ed580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed578.md#insn-008ed580)

~~~diff
- 008ed580 ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 008ed580 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ed580 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ed580 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ed580 ["COPY", "tmp:0:8", ["const:c68:8"]]
+ 008ed580 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ed580 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ed580 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ed580 bytes 29e12e91
+ 008ed580 bytes 29a13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43562bb61c6603d2d8db0dcb149fa1e4"></a>

### [`008ed5dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed5dc.md) → [`008ed5dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed5dc.md) FUN_008ed5dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008ed600",
      "incomplete_value": false,
      "site": "008ed600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed600",
      "incomplete_value": false,
      "site": "008ed600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "008ed600",
      "DATA",
      [
        "storage",
        "00c07c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed600",
      "DATA",
      [
        "storage",
        "00c07ce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed5fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed5dc.md#insn-008ed5fc)
- 新版 [`008ed5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed5dc.md#insn-008ed5fc)

~~~diff
- 008ed5fc ["COPY", "tmp:0:8", ["const:c38:8"]]
- 008ed5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ed5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ed5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ed5fc ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 008ed5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ed5fc bytes 08e13091
+ 008ed5fc bytes 08a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9371d4afddd5b3a62ca18c3469a7abf4"></a>

### [`008ed610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed610.md) → [`008ed610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed610.md) FUN_008ed610

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ed61c",
      "incomplete_value": false,
      "site": "008ed61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed61c",
      "incomplete_value": false,
      "site": "008ed61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "008ed61c",
      "DATA",
      [
        "storage",
        "00c07c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed61c",
      "DATA",
      [
        "storage",
        "00c07ce8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed618`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed610.md#insn-008ed618)
- 新版 [`008ed618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed610.md#insn-008ed618)

~~~diff
- 008ed618 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 008ed618 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ed618 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ed618 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ed618 ["COPY", "tmp:0:8", ["const:ce8:8"]]
+ 008ed618 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ed618 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ed618 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ed618 bytes 29e13091
+ 008ed618 bytes 29a13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b51e8bd02bbf949208c54d4adddd3b74"></a>

### [`008ed668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed668.md) → [`008ed668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed668.md) FUN_008ed668

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008ed67c",
      "incomplete_value": false,
      "site": "008ed680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed67c",
      "incomplete_value": false,
      "site": "008ed680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
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
      "008ed680",
      "DATA",
      [
        "storage",
        "00c07cb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed680",
      "DATA",
      [
        "storage",
        "00c07d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed668.md#insn-008ed67c)
- 新版 [`008ed67c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed668.md#insn-008ed67c)

~~~diff
- 008ed67c ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 008ed67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ed67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ed67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ed67c ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 008ed67c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed67c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed67c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ed67c bytes 08e13291
+ 008ed67c bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59cbd8f7e703b27055d32f338cba986e"></a>

### [`008ed68c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed68c.md) → [`008ed68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed68c.md) FUN_008ed68c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ed690",
      "incomplete_value": false,
      "site": "008ed694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed690",
      "incomplete_value": false,
      "site": "008ed694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
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
      "008ed694",
      "DATA",
      [
        "storage",
        "00c07cb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed694",
      "DATA",
      [
        "storage",
        "00c07d68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed68c.md#insn-008ed690)
- 新版 [`008ed690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed68c.md#insn-008ed690)

~~~diff
- 008ed690 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 008ed690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ed690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ed690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ed690 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 008ed690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ed690 bytes 08e13291
+ 008ed690 bytes 08a13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-056ba13d9123990fd4693e1adebbff33"></a>

### [`008ed718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed718.md) → [`008ed718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed718.md) FUN_008ed718

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008ed72c",
      "incomplete_value": false,
      "site": "008ed730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed72c",
      "incomplete_value": false,
      "site": "008ed730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "008ed730",
      "DATA",
      [
        "storage",
        "00c07d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed730",
      "DATA",
      [
        "storage",
        "00c07de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed72c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed718.md#insn-008ed72c)
- 新版 [`008ed72c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed718.md#insn-008ed72c)

~~~diff
- 008ed72c ["COPY", "tmp:0:8", ["const:d38:8"]]
- 008ed72c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ed72c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ed72c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ed72c ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 008ed72c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed72c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed72c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ed72c bytes 08e13491
+ 008ed72c bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7776054d4a3c07d72ef30dbb16a12df5"></a>

### [`008ed73c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed73c.md) → [`008ed73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed73c.md) FUN_008ed73c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ed740",
      "incomplete_value": false,
      "site": "008ed744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed740",
      "incomplete_value": false,
      "site": "008ed744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "008ed744",
      "DATA",
      [
        "storage",
        "00c07d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed744",
      "DATA",
      [
        "storage",
        "00c07de8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed73c.md#insn-008ed740)
- 新版 [`008ed740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed73c.md#insn-008ed740)

~~~diff
- 008ed740 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 008ed740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ed740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ed740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ed740 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 008ed740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ed740 bytes 08e13491
+ 008ed740 bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00382858092061ec61d470ad2174f4c7"></a>

### [`008ed7cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed7cc.md) → [`008ed7cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed7cc.md) FUN_008ed7cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008ed7e0",
      "incomplete_value": false,
      "site": "008ed7e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed7e0",
      "incomplete_value": false,
      "site": "008ed7e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "008ed7e4",
      "DATA",
      [
        "storage",
        "00c07db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed7e4",
      "DATA",
      [
        "storage",
        "00c07e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed7e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed7cc.md#insn-008ed7e0)
- 新版 [`008ed7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed7cc.md#insn-008ed7e0)

~~~diff
- 008ed7e0 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 008ed7e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ed7e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ed7e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ed7e0 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 008ed7e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed7e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed7e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ed7e0 bytes 08e13691
+ 008ed7e0 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-483a944556bcf1df847dfb705730b8a0"></a>

### [`008ed7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed7f0.md) → [`008ed7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed7f0.md) FUN_008ed7f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ed7f4",
      "incomplete_value": false,
      "site": "008ed7f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed7f4",
      "incomplete_value": false,
      "site": "008ed7f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "008ed7f8",
      "DATA",
      [
        "storage",
        "00c07db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed7f8",
      "DATA",
      [
        "storage",
        "00c07e68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed7f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed7f0.md#insn-008ed7f4)
- 新版 [`008ed7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed7f0.md#insn-008ed7f4)

~~~diff
- 008ed7f4 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 008ed7f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ed7f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ed7f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ed7f4 ["COPY", "tmp:0:8", ["const:e68:8"]]
+ 008ed7f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed7f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed7f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ed7f4 bytes 08e13691
+ 008ed7f4 bytes 08a13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a3b341849218e99758dca2e347dcee8"></a>

### [`008ed880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed880.md) → [`008ed880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed880.md) FUN_008ed880

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008ed894",
      "incomplete_value": false,
      "site": "008ed898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed894",
      "incomplete_value": false,
      "site": "008ed898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "008ed898",
      "DATA",
      [
        "storage",
        "00c07e38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed898",
      "DATA",
      [
        "storage",
        "00c07ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed880.md#insn-008ed894)
- 新版 [`008ed894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed880.md#insn-008ed894)

~~~diff
- 008ed894 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 008ed894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ed894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ed894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ed894 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 008ed894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ed894 bytes 08e13891
+ 008ed894 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f870b13e3df8d34dff118023798cd925"></a>

### [`008ed8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed8a4.md) → [`008ed8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed8a4.md) FUN_008ed8a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ed8a8",
      "incomplete_value": false,
      "site": "008ed8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ed8a8",
      "incomplete_value": false,
      "site": "008ed8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "008ed8ac",
      "DATA",
      [
        "storage",
        "00c07e38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ed8ac",
      "DATA",
      [
        "storage",
        "00c07ee8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ed8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008ed8a4.md#insn-008ed8a8)
- 新版 [`008ed8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008ed8a4.md#insn-008ed8a8)

~~~diff
- 008ed8a8 ["COPY", "tmp:0:8", ["const:e38:8"]]
- 008ed8a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ed8a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ed8a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ed8a8 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 008ed8a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed8a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ed8a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ed8a8 bytes 08e13891
+ 008ed8a8 bytes 08a13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a53d240319955181271952895e79a33"></a>

### [`008edb3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008edb3c.md) → [`008edb3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008edb3c.md) FUN_008edb3c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008edb60",
      "incomplete_value": false,
      "site": "008edb60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008edb60",
      "incomplete_value": false,
      "site": "008edb60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "008edb60",
      "DATA",
      [
        "storage",
        "00c07eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008edb60",
      "DATA",
      [
        "storage",
        "00c07f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008edb5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008edb3c.md#insn-008edb5c)
- 新版 [`008edb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008edb3c.md#insn-008edb5c)

~~~diff
- 008edb5c ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 008edb5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008edb5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008edb5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008edb5c ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 008edb5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008edb5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008edb5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008edb5c bytes 08e13a91
+ 008edb5c bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7458e94a6eea776689cca837360e02ff"></a>

### [`008edb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008edb70.md) → [`008edb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008edb70.md) FUN_008edb70

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008edb7c",
      "incomplete_value": false,
      "site": "008edb7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008edb7c",
      "incomplete_value": false,
      "site": "008edb7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "008edb7c",
      "DATA",
      [
        "storage",
        "00c07eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008edb7c",
      "DATA",
      [
        "storage",
        "00c07f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008edb78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008edb70.md#insn-008edb78)
- 新版 [`008edb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008edb70.md#insn-008edb78)

~~~diff
- 008edb78 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 008edb78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008edb78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008edb78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008edb78 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 008edb78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008edb78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008edb78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008edb78 bytes 29e13a91
+ 008edb78 bytes 29a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47526f0c091b5788ed9d31c3e982d405"></a>

### [`008edbe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008edbe8.md) → [`008edbe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008edbe8.md) FUN_008edbe8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008edc0c",
      "incomplete_value": false,
      "site": "008edc0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008edc0c",
      "incomplete_value": false,
      "site": "008edc0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "008edc0c",
      "DATA",
      [
        "storage",
        "00c07f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008edc0c",
      "DATA",
      [
        "storage",
        "00c07fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008edc08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008edbe8.md#insn-008edc08)
- 新版 [`008edc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008edbe8.md#insn-008edc08)

~~~diff
- 008edc08 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 008edc08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008edc08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008edc08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008edc08 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 008edc08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008edc08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008edc08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008edc08 bytes 08e13c91
+ 008edc08 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ca8369c1f76101deb7d2c4b024232f3"></a>

### [`008edc1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008edc1c.md) → [`008edc1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008edc1c.md) FUN_008edc1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008edc28",
      "incomplete_value": false,
      "site": "008edc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008edc28",
      "incomplete_value": false,
      "site": "008edc28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "008edc28",
      "DATA",
      [
        "storage",
        "00c07f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008edc28",
      "DATA",
      [
        "storage",
        "00c07fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008edc24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008edc1c.md#insn-008edc24)
- 新版 [`008edc24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008edc1c.md#insn-008edc24)

~~~diff
- 008edc24 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 008edc24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008edc24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008edc24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008edc24 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 008edc24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008edc24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008edc24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008edc24 bytes 29e13c91
+ 008edc24 bytes 29a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff4cc5687ea8e7216d1b5e12f7620852"></a>

### [`008edc38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008edc38.md) → [`008edc38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008edc38.md) FUN_008edc38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 17件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00886014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/00886014.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00886014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/00886014.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008edcd8",
      "incomplete_value": true,
      "site": "008edce8",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:a02:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008edcd8",
      "incomplete_value": true,
      "site": "008edce8",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:975:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008edd08",
      "incomplete_value": false,
      "site": "008edd08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008edd08",
      "incomplete_value": false,
      "site": "008edd08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008ede28"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008edcd8",
      "READ",
      [
        "storage",
        "0029d975",
        null,
        "string"
      ]
    ],
    [
      "008edd08",
      "DATA",
      [
        "storage",
        "00c07fa8",
        null,
        "undefined *"
      ]
    ],
    [
      "008edd68",
      "READ",
      [
        "storage",
        "00c07fc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008edcd8",
      "READ",
      [
        "storage",
        "0029da02",
        null,
        "string"
      ]
    ],
    [
      "008edd08",
      "DATA",
      [
        "storage",
        "00c08058",
        null,
        "undefined *"
      ]
    ],
    [
      "008edd68",
      "READ",
      [
        "storage",
        "00c08078",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ede28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008edc38.md#insn-008ede28) · [`008ede60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ed/008edc38.md#insn-008ede60)
- 新版 [`008ede28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ed/008edc38.md#insn-008ede28)

~~~diff
- 008ede28 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 008ede28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008ede28 bytes 140800f9
+ 008ede28 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
+ 008ede28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008ede28 bytes 140800f9
- 008ede60 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 008ede60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008ede60 bytes 140800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1786a0274b282af9304570048f42b9b"></a>

### [`008ee03c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee03c.md) → [`008ee03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee03c.md) FUN_008ee03c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008ee05c",
      "incomplete_value": false,
      "site": "008ee060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee05c",
      "incomplete_value": false,
      "site": "008ee060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "008ee060",
      "DATA",
      [
        "storage",
        "00c07fa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ee060",
      "DATA",
      [
        "storage",
        "00c08058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ee058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee03c.md#insn-008ee058) · [`008ee05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee03c.md#insn-008ee05c)
- 新版 [`008ee058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee03c.md#insn-008ee058) · [`008ee05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee03c.md#insn-008ee05c)

~~~diff
- 008ee058 ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008ee058 ["COPY", "register:4040:8", ["const:c08000:8"]]
- 008ee058 bytes c81800b0
+ 008ee058 bytes c81800d0
- 008ee05c ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 008ee05c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ee05c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ee05c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ee05c ["COPY", "tmp:0:8", ["const:58:8"]]
+ 008ee05c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee05c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee05c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ee05c bytes 08a13e91
+ 008ee05c bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64d42787250af7938592d0a5257609fd"></a>

### [`008ee074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee074.md) → [`008ee074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee074.md) FUN_008ee074

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ee078",
      "incomplete_value": false,
      "site": "008ee07c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee078",
      "incomplete_value": false,
      "site": "008ee07c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "008ee07c",
      "DATA",
      [
        "storage",
        "00c07fa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ee07c",
      "DATA",
      [
        "storage",
        "00c08058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ee074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee074.md#insn-008ee074) · [`008ee078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee074.md#insn-008ee078)
- 新版 [`008ee074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee074.md#insn-008ee074) · [`008ee078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee074.md#insn-008ee078)

~~~diff
- 008ee074 ["COPY", "register:4040:8", ["const:c07000:8"]]
+ 008ee074 ["COPY", "register:4040:8", ["const:c08000:8"]]
- 008ee074 bytes c81800b0
+ 008ee074 bytes c81800d0
- 008ee078 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 008ee078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ee078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ee078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ee078 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 008ee078 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee078 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee078 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ee078 bytes 08a13e91
+ 008ee078 bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a64884971a97bd169bba7efddb9d0dae"></a>

### [`008ee21c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee21c.md) → [`008ee21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee21c.md) FUN_008ee21c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008ee240",
      "incomplete_value": false,
      "site": "008ee240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee240",
      "incomplete_value": false,
      "site": "008ee240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "008ee240",
      "DATA",
      [
        "storage",
        "00c08018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ee240",
      "DATA",
      [
        "storage",
        "00c080c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ee23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee21c.md#insn-008ee23c)
- 新版 [`008ee23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee21c.md#insn-008ee23c)

~~~diff
- 008ee23c ["COPY", "tmp:0:8", ["const:18:8"]]
- 008ee23c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ee23c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ee23c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ee23c ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 008ee23c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee23c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee23c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ee23c bytes 08610091
+ 008ee23c bytes 08210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64cb446647df4dfd5e349847ab424108"></a>

### [`008ee250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee250.md) → [`008ee250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee250.md) FUN_008ee250

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ee25c",
      "incomplete_value": false,
      "site": "008ee25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee25c",
      "incomplete_value": false,
      "site": "008ee25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:18:8"
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
      "008ee25c",
      "DATA",
      [
        "storage",
        "00c08018",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ee25c",
      "DATA",
      [
        "storage",
        "00c080c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ee258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee250.md#insn-008ee258)
- 新版 [`008ee258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee250.md#insn-008ee258)

~~~diff
- 008ee258 ["COPY", "tmp:0:8", ["const:18:8"]]
- 008ee258 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ee258 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ee258 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ee258 ["COPY", "tmp:0:8", ["const:c8:8"]]
+ 008ee258 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ee258 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ee258 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ee258 bytes 29610091
+ 008ee258 bytes 29210391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fa650b175f47dc0708237e779328718"></a>

### [`008ee26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee26c.md) → [`008ee26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee26c.md) FUN_008ee26c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00701e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00701/00701e0c.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00883d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883d34.md) [`008847e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00884/008847e4.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00701e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00701/00701e0c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d34.md) [`008847e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008847e4.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008ee38c",
      "incomplete_value": true,
      "site": "008ee3a0",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:394:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee38c",
      "incomplete_value": true,
      "site": "008ee3a0",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:428:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ee3b8",
      "incomplete_value": false,
      "site": "008ee3c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee3b8",
      "incomplete_value": false,
      "site": "008ee3c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008ee38c",
      "READ",
      [
        "storage",
        "002a8428",
        null,
        "string"
      ]
    ],
    [
      "008ee3c0",
      "DATA",
      [
        "storage",
        "00c08088",
        null,
        "undefined *"
      ]
    ],
    [
      "008ee418",
      "READ",
      [
        "storage",
        "00c080a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008ee38c",
      "READ",
      [
        "storage",
        "002a8394",
        null,
        "string"
      ]
    ],
    [
      "008ee3c0",
      "DATA",
      [
        "storage",
        "00c08138",
        null,
        "undefined *"
      ]
    ],
    [
      "008ee418",
      "READ",
      [
        "storage",
        "00c08158",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ee384`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee26c.md#insn-008ee384) · [`008ee3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee26c.md#insn-008ee3b8) · [`008ee3bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee26c.md#insn-008ee3bc)
- 新版 [`008ee384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee26c.md#insn-008ee384) · [`008ee3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee26c.md#insn-008ee3b8)

~~~diff
- 008ee384 ["COPY", "tmp:0:8", ["const:428:8"]]
- 008ee384 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ee384 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ee384 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ee384 ["COPY", "tmp:0:8", ["const:394:8"]]
+ 008ee384 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ee384 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ee384 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ee384 bytes 29a11091
+ 008ee384 bytes 29510e91
- 008ee3b8 ["COPY", "tmp:0:8", ["const:88:8"]]
- 008ee3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ee3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ee3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ee3b8 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 008ee3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ee3b8 bytes 08210291
+ 008ee3b8 bytes 08e10491
- 008ee3bc ["COPY", "tmp:0:8", ["const:30:8"]]
- 008ee3bc ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 008ee3bc ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 008ee3bc ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 008ee3bc bytes f5c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5233956e2e5ff0c44a12ceceb66fccc"></a>

### [`008ee52c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee52c.md) → [`008ee52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee52c.md) FUN_008ee52c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008ee540",
      "incomplete_value": false,
      "site": "008ee544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee540",
      "incomplete_value": false,
      "site": "008ee544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "008ee544",
      "DATA",
      [
        "storage",
        "00c08088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ee544",
      "DATA",
      [
        "storage",
        "00c08138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ee540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee52c.md#insn-008ee540)
- 新版 [`008ee540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee52c.md#insn-008ee540)

~~~diff
- 008ee540 ["COPY", "tmp:0:8", ["const:88:8"]]
- 008ee540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ee540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ee540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ee540 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 008ee540 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee540 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee540 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ee540 bytes 08210291
+ 008ee540 bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bceeaf71664db8ba068e2bcc26296624"></a>

### [`008ee550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee550.md) → [`008ee550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee550.md) FUN_008ee550

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ee554",
      "incomplete_value": false,
      "site": "008ee558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee554",
      "incomplete_value": false,
      "site": "008ee558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "008ee558",
      "DATA",
      [
        "storage",
        "00c08088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ee558",
      "DATA",
      [
        "storage",
        "00c08138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ee554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee550.md#insn-008ee554)
- 新版 [`008ee554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee550.md#insn-008ee554)

~~~diff
- 008ee554 ["COPY", "tmp:0:8", ["const:88:8"]]
- 008ee554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ee554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ee554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ee554 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 008ee554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ee554 bytes 08210291
+ 008ee554 bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff9e5716c0ed0c7a9b6146d428078900"></a>

### [`008ee61c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee61c.md) → [`008ee61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee61c.md) FUN_008ee61c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008ee620",
      "incomplete_value": true,
      "site": "008ee624",
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
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee620",
      "incomplete_value": true,
      "site": "008ee624",
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
            "const:128:8"
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
      "008ee624",
      "DATA",
      [
        "storage",
        "00c08128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ee624",
      "DATA",
      [
        "storage",
        "00c081d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ee620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee61c.md#insn-008ee620)
- 新版 [`008ee620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee61c.md#insn-008ee620)

~~~diff
- 008ee620 ["COPY", "tmp:0:8", ["const:128:8"]]
- 008ee620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ee620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ee620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ee620 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 008ee620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ee620 bytes 08a10491
+ 008ee620 bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a5317627aac1792adcc0a1bfee44670"></a>

### [`008ee72c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee72c.md) → [`008ee72c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee72c.md) FUN_008ee72c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008ee750",
      "incomplete_value": false,
      "site": "008ee754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee750",
      "incomplete_value": false,
      "site": "008ee754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "008ee754",
      "DATA",
      [
        "storage",
        "00c081a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ee754",
      "DATA",
      [
        "storage",
        "00c08258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ee750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee72c.md#insn-008ee750)
- 新版 [`008ee750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee72c.md#insn-008ee750)

~~~diff
- 008ee750 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 008ee750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ee750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ee750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ee750 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 008ee750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ee750 bytes 08a10691
+ 008ee750 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04bfdc8b6086aaff27bd1944b040b372"></a>

### [`008ee76c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee76c.md) → [`008ee76c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee76c.md) FUN_008ee76c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008ee770",
      "incomplete_value": false,
      "site": "008ee774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee770",
      "incomplete_value": false,
      "site": "008ee774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:1a8:8"
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
      "008ee774",
      "DATA",
      [
        "storage",
        "00c081a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008ee774",
      "DATA",
      [
        "storage",
        "00c08258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ee770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee76c.md#insn-008ee770)
- 新版 [`008ee770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee76c.md#insn-008ee770)

~~~diff
- 008ee770 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 008ee770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ee770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ee770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ee770 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 008ee770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ee770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ee770 bytes 08a10691
+ 008ee770 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0bcf5f31b3bcee9fa3abe1ef0b9be01"></a>

### [`008ee810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee810.md) → [`008ee810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee810.md) _INIT_174

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008ee84c",
      "incomplete_value": true,
      "site": "008ee868",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee84c",
      "incomplete_value": true,
      "site": "008ee868",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2e4:8"
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
      "definition_site": "008ee870",
      "incomplete_value": true,
      "site": "008ee88c",
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
                "const:2a7000:8"
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
      "definition_site": "008ee870",
      "incomplete_value": true,
      "site": "008ee88c",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f7:8"
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
      "definition_site": "008ee890",
      "incomplete_value": true,
      "site": "008ee8ac",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ee890",
      "incomplete_value": true,
      "site": "008ee8ac",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:da:8"
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
      "008ee84c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008ee870",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008ee890",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008ee84c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008ee870",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008ee890",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ee83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee810.md#insn-008ee83c) · [`008ee844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008ee810.md#insn-008ee844)
- 新版 [`008ee83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee810.md#insn-008ee83c) · [`008ee844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008ee810.md#insn-008ee844)

~~~diff
- 008ee83c ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 008ee83c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008ee83c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008ee83c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008ee83c ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 008ee83c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008ee83c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008ee83c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008ee83c bytes 73a21b91
+ 008ee83c bytes 73a21e91
- 008ee844 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008ee844 bytes c9cdffb0
+ 008ee844 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008ee844 bytes c9cdffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccfa57086b5c0ca575f8655f8d826116"></a>

### [`008eeba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008eeba0.md) → [`008eeba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008eeba0.md) FUN_008eeba0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0081fa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081fa64.md) · 呼出先 48件 [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c120.md) [`0041c8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8f8.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md)
- 新版 呼出元 1件 [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) · 呼出先 48件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.66% / 新版 92.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 19件, `store_destination` 12件, `store_value` 17件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008eebe8",
      "incomplete_value": false,
      "site": "008eebe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eebe8",
      "incomplete_value": false,
      "site": "008eebe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008eebe0",
      "incomplete_value": true,
      "site": "008eebe8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
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
      "definition_site": "008eebe0",
      "incomplete_value": true,
      "site": "008eebe8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008eebec",
      "incomplete_value": false,
      "site": "008eebec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008eebec",
      "incomplete_value": false,
      "site": "008eebec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "008eebe0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008eebe4",
      "READ",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ],
    [
      "008eebe8",
      "WRITE",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008eebe0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008eebe4",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "008eebe8",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008eebe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008eeba0.md#insn-008eebe8) · [`008eebec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008eeba0.md#insn-008eebec) · [`008eec08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008eeba0.md#insn-008eec08)
- 新版 [`008eebe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008eeba0.md#insn-008eebe8) · [`008eebec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008eeba0.md#insn-008eebec) · [`008eec08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008eeba0.md#insn-008eec08)

~~~diff
- 008eebe8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a8:8"]]
- 008eebe8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008eebe8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
+ 008eebe8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008eebe8 bytes 09d504f9
+ 008eebe8 bytes 093505f9
- 008eebec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b8:8"]]
- 008eebec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008eebec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
+ 008eebec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008eebec bytes aade04f9
+ 008eebec bytes aa3e05f9
- 008eec08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b8:8"]]
- 008eec08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008eec08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
+ 008eec08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008eec08 bytes b4de04f9
+ 008eec08 bytes b43e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16043d46b30583da612441a984b3474c"></a>

### [`008f1308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f1/008f1308.md) → [`008f1308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f1/008f1308.md) FUN_008f1308

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00695904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00695/00695904.md) [`008f06a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f0/008f06a0.md) · 呼出先 15件 [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00574fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574fe4.md) [`0081fa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081fa64.md) [`008865b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/008865b0.md) [`00887e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00887/00887e18.md)
- 新版 呼出元 2件 [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`008f06a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f0/008f06a0.md) · 呼出先 15件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md) [`00887e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/00887e18.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.63% / 新版 97.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f13b8",
      "incomplete_value": true,
      "site": "008f13b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d7c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f13b8",
      "incomplete_value": true,
      "site": "008f13b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d83:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008f1454",
      "incomplete_value": false,
      "site": "008f145c",
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
            "const:85b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f1454",
      "incomplete_value": false,
      "site": "008f145c",
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
            "const:855:8"
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
      "008f13a4",
      "READ",
      [
        "storage",
        "002a5d83",
        null,
        "string"
      ]
    ],
    [
      "008f1454",
      "PARAM",
      [
        "storage",
        "002ab855",
        null,
        null
      ]
    ],
    [
      "008f14ec",
      "DATA",
      [
        "storage",
        "00c08270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f13a4",
      "READ",
      [
        "storage",
        "002a5d7c",
        null,
        "string"
      ]
    ],
    [
      "008f1454",
      "PARAM",
      [
        "storage",
        "002ab85b",
        null,
        null
      ]
    ],
    [
      "008f14ec",
      "DATA",
      [
        "storage",
        "00c08320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f139c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f1/008f1308.md#insn-008f139c) · [`008f1454`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f1/008f1308.md#insn-008f1454) · [`008f14dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f1/008f1308.md#insn-008f14dc)
- 新版 [`008f139c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f1/008f1308.md#insn-008f139c) · [`008f1454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f1/008f1308.md#insn-008f1454) · [`008f14dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f1/008f1308.md#insn-008f14dc)

~~~diff
- 008f139c ["COPY", "tmp:0:8", ["const:d83:8"]]
- 008f139c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f139c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f139c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f139c ["COPY", "tmp:0:8", ["const:d7c:8"]]
+ 008f139c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f139c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f139c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f139c bytes 290d3691
+ 008f139c bytes 29f13591
- 008f1454 ["COPY", "tmp:0:8", ["const:855:8"]]
- 008f1454 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008f1454 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008f1454 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008f1454 ["COPY", "tmp:0:8", ["const:85b:8"]]
+ 008f1454 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008f1454 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008f1454 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008f1454 bytes 21542191
+ 008f1454 bytes 216c2191
- 008f14dc ["COPY", "tmp:0:8", ["const:270:8"]]
- 008f14dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f14dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f14dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f14dc ["COPY", "tmp:0:8", ["const:320:8"]]
+ 008f14dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f14dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f14dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f14dc bytes 08c10991
+ 008f14dc bytes 08810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee8f8af1d9e0d7d6882c2654831043c2"></a>

### [`008f17a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f1/008f17a8.md) → [`008f17a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f1/008f17a8.md) FUN_008f17a8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 28件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00444c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444fcc.md) [`00445044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445044.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 28件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00444c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444fcc.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.63% / 新版 97.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008f17f0",
      "incomplete_value": true,
      "site": "008f17f0",
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
      "definition_site": "008f17f0",
      "incomplete_value": true,
      "site": "008f17f0",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008f206c",
      "incomplete_value": true,
      "site": "008f2070",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
      "definition_site": "008f206c",
      "incomplete_value": true,
      "site": "008f2070",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:c78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 73,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008f21a0",
      "incomplete_value": true,
      "site": "008f21a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
      "definition_site": "008f21a0",
      "incomplete_value": true,
      "site": "008f21a4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:c78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 77,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f17ec",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008f17f8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f1800",
      "PARAM",
      [
        "storage",
        "00c08228",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f17ec",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008f17f8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f1800",
      "PARAM",
      [
        "storage",
        "00c082d8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f17ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f1/008f17a8.md#insn-008f17ec) · [`008f17f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f1/008f17a8.md#insn-008f17f8) · [`008f1800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f1/008f17a8.md#insn-008f1800)
- 新版 [`008f17ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f1/008f17a8.md#insn-008f17ec) · [`008f17f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f1/008f17a8.md#insn-008f17f8) · [`008f1800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f1/008f17a8.md#insn-008f1800)

~~~diff
- 008f17ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008f17ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008f17ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008f17ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008f17ec bytes 08dd44f9
+ 008f17ec bytes 083d45f9
- 008f17f8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008f17f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008f17f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008f17f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008f17f8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008f17f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008f17f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008f17f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008f17f8 bytes 21603691
+ 008f17f8 bytes 21203991
- 008f1800 ["COPY", "tmp:0:8", ["const:228:8"]]
- 008f1800 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008f1800 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008f1800 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008f1800 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 008f1800 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008f1800 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008f1800 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008f1800 bytes 42a00891
+ 008f1800 bytes 42600b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47ae35d7b86cb326857d98c1796d5f4b"></a>

### [`008f2388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2388.md) → [`008f2388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2388.md) FUN_008f2388

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008eeba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ee/008eeba0.md) · 呼出先 25件 [`0044b8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8a8.md) [`0044b8ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b8ec.md) [`0044ba98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044ba98.md) [`0044c020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c020.md) [`0044c1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c1dc.md)
- 新版 呼出元 1件 [`008eeba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008eeba0.md) · 呼出先 25件 [`0044b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md) [`0044b8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8ec.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md) [`0044c020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c020.md) [`0044c1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c1dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.92% / 新版 86.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 3件, `store_value` 16件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008f23c4",
      "incomplete_value": false,
      "site": "008f23d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f23c4",
      "incomplete_value": false,
      "site": "008f23d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "definition_site": "008f2470",
      "incomplete_value": true,
      "site": "008f2470",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:8bd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f2470",
      "incomplete_value": true,
      "site": "008f2470",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:951:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f2474",
      "incomplete_value": true,
      "site": "008f2474",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008f2474",
      "incomplete_value": true,
      "site": "008f2474",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f23d0",
      "DATA",
      [
        "storage",
        "00c08250",
        null,
        "pointer"
      ]
    ],
    [
      "008f2460",
      "READ",
      [
        "storage",
        "002a8951",
        null,
        "string"
      ]
    ],
    [
      "008f2464",
      "READ",
      [
        "storage",
        "002a8957",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008f23d0",
      "DATA",
      [
        "storage",
        "00c08300",
        null,
        "pointer"
      ]
    ],
    [
      "008f2460",
      "READ",
      [
        "storage",
        "002a88bd",
        null,
        "string"
      ]
    ],
    [
      "008f2464",
      "READ",
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

- 旧版 [`008f23c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2388.md#insn-008f23c4) · [`008f2458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2388.md#insn-008f2458) · [`008f248c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2388.md#insn-008f248c)
- 新版 [`008f23c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2388.md#insn-008f23c4) · [`008f2458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2388.md#insn-008f2458) · [`008f248c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2388.md#insn-008f248c)

~~~diff
- 008f23c4 ["COPY", "tmp:0:8", ["const:250:8"]]
- 008f23c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f23c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f23c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f23c4 ["COPY", "tmp:0:8", ["const:300:8"]]
+ 008f23c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f23c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f23c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f23c4 bytes 08410991
+ 008f23c4 bytes 08010c91
- 008f2458 ["COPY", "tmp:0:8", ["const:951:8"]]
- 008f2458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f2458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f2458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f2458 ["COPY", "tmp:0:8", ["const:8bd:8"]]
+ 008f2458 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f2458 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f2458 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f2458 bytes 29452591
+ 008f2458 bytes 29f52291
- 008f248c ["COPY", "tmp:0:8", ["const:18b:8"]]
- 008f248c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f248c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f248c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f248c ["COPY", "tmp:0:8", ["const:218:8"]]
+ 008f248c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f248c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f248c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f248c bytes 292d0691
+ 008f248c bytes 29610891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41af2b586a21b59dfb47c703ab1ebdbe"></a>

### [`008f2c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2c38.md) → [`008f2c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2c38.md) FUN_008f2c38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008f2e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2e74.md) · 呼出先 6件 [`0044b9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044c/0044c104.md) [`0064c828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0064c/0064c828.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`008f2e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2e74.md) · 呼出先 6件 [`0044b9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b9cc.md) [`0044c104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c104.md) [`0064c828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c828.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.60% / 新版 98.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008f2c54",
      "incomplete_value": false,
      "site": "008f2c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f2c54",
      "incomplete_value": false,
      "site": "008f2c58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:250:8"
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
      "008f2c58",
      "DATA",
      [
        "storage",
        "00c08250",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008f2c58",
      "DATA",
      [
        "storage",
        "00c08300",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f2c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2c38.md#insn-008f2c54)
- 新版 [`008f2c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2c38.md#insn-008f2c54)

~~~diff
- 008f2c54 ["COPY", "tmp:0:8", ["const:250:8"]]
- 008f2c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f2c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f2c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f2c54 ["COPY", "tmp:0:8", ["const:300:8"]]
+ 008f2c54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f2c54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f2c54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f2c54 bytes 08410991
+ 008f2c54 bytes 08010c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09d9cc012052e873a7b91e2a70eba4e8"></a>

### [`008f2e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2e9c.md) → [`008f2e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2e9c.md) FUN_008f2e9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008f2ebc",
      "incomplete_value": false,
      "site": "008f2ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f2ebc",
      "incomplete_value": false,
      "site": "008f2ec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "008f2ec0",
      "DATA",
      [
        "storage",
        "00c08270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f2ec0",
      "DATA",
      [
        "storage",
        "00c08320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f2ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2e9c.md#insn-008f2ebc)
- 新版 [`008f2ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2e9c.md#insn-008f2ebc)

~~~diff
- 008f2ebc ["COPY", "tmp:0:8", ["const:270:8"]]
- 008f2ebc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f2ebc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f2ebc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f2ebc ["COPY", "tmp:0:8", ["const:320:8"]]
+ 008f2ebc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f2ebc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f2ebc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f2ebc bytes 08c10991
+ 008f2ebc bytes 08810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fb194b44ad281cc972e6eb7c60c1803"></a>

### [`008f2ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2ed4.md) → [`008f2ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2ed4.md) FUN_008f2ed4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008f2ed8",
      "incomplete_value": false,
      "site": "008f2edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:320:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f2ed8",
      "incomplete_value": false,
      "site": "008f2edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "008f2edc",
      "DATA",
      [
        "storage",
        "00c08270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f2edc",
      "DATA",
      [
        "storage",
        "00c08320",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f2ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2ed4.md#insn-008f2ed8)
- 新版 [`008f2ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2ed4.md#insn-008f2ed8)

~~~diff
- 008f2ed8 ["COPY", "tmp:0:8", ["const:270:8"]]
- 008f2ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f2ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f2ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f2ed8 ["COPY", "tmp:0:8", ["const:320:8"]]
+ 008f2ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f2ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f2ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f2ed8 bytes 08c10991
+ 008f2ed8 bytes 08810c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbc5e25749eeb68bae8f3494ef255d6c"></a>

### [`008f2fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2fbc.md) → [`008f2fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2fbc.md) _INIT_175

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f301c",
      "incomplete_value": true,
      "site": "008f3038",
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
                "live",
                "register:4050:8"
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
      "definition_site": "008f301c",
      "incomplete_value": true,
      "site": "008f3038",
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
                "live",
                "register:4050:8"
              ],
              [
                "leaf",
                "const:2f7:8"
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
      "definition_site": "008f305c",
      "incomplete_value": true,
      "site": "008f3074",
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
                "const:293000:8"
              ],
              [
                "leaf",
                "const:73b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f305c",
      "incomplete_value": true,
      "site": "008f3074",
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
                "const:293000:8"
              ],
              [
                "leaf",
                "const:6ae:8"
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
      "definition_site": "008f3078",
      "incomplete_value": true,
      "site": "008f3094",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:36e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f3078",
      "incomplete_value": true,
      "site": "008f3094",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:2e1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f2ff8",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008f301c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008f303c",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008f2ff8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008f301c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008f303c",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f2fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2fbc.md#insn-008f2fe8) · [`008f2ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f2/008f2fbc.md#insn-008f2ff0)
- 新版 [`008f2fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2fbc.md#insn-008f2fe8) · [`008f2ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f2/008f2fbc.md#insn-008f2ff0)

~~~diff
- 008f2fe8 ["COPY", "tmp:0:8", ["const:700:8"]]
- 008f2fe8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008f2fe8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008f2fe8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008f2fe8 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 008f2fe8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008f2fe8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008f2fe8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008f2fe8 bytes 73021c91
+ 008f2fe8 bytes 73021f91
- 008f2ff0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008f2ff0 bytes a9cdffb0
+ 008f2ff0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008f2ff0 bytes a9cdffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd63fcb421148b61c2e9bd21d1226c4a"></a>

### [`008f334c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f3/008f334c.md) → [`008f334c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f3/008f334c.md) _INIT_176

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f3388",
      "incomplete_value": true,
      "site": "008f33a4",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f3388",
      "incomplete_value": true,
      "site": "008f33a4",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2e4:8"
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
      "definition_site": "008f33ac",
      "incomplete_value": true,
      "site": "008f33c8",
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
                "const:2a7000:8"
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
      "definition_site": "008f33ac",
      "incomplete_value": true,
      "site": "008f33c8",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f7:8"
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
      "definition_site": "008f33cc",
      "incomplete_value": true,
      "site": "008f33e8",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f33cc",
      "incomplete_value": true,
      "site": "008f33e8",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:da:8"
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
      "008f3388",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008f33ac",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008f33cc",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008f3388",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008f33ac",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008f33cc",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f3378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f3/008f334c.md#insn-008f3378) · [`008f3380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f3/008f334c.md#insn-008f3380)
- 新版 [`008f3378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f3/008f334c.md#insn-008f3378) · [`008f3380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f3/008f334c.md#insn-008f3380)

~~~diff
- 008f3378 ["COPY", "tmp:0:8", ["const:720:8"]]
- 008f3378 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008f3378 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008f3378 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008f3378 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 008f3378 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008f3378 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008f3378 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008f3378 bytes 73821c91
+ 008f3378 bytes 73821f91
- 008f3380 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008f3380 bytes a9cdff90
+ 008f3380 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008f3380 bytes a9cdff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fbc302d37474b5f69e8522d8495e235"></a>

### [`008f36dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f3/008f36dc.md) → [`008f36dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f3/008f36dc.md) _INIT_177

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f373c",
      "incomplete_value": true,
      "site": "008f3758",
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
                "const:2a7000:8"
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
      "definition_site": "008f373c",
      "incomplete_value": true,
      "site": "008f3758",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f7:8"
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
      "definition_site": "008f375c",
      "incomplete_value": true,
      "site": "008f3778",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f375c",
      "incomplete_value": true,
      "site": "008f3778",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:da:8"
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
      "definition_site": "008f3798",
      "incomplete_value": true,
      "site": "008f37b4",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:36e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f3798",
      "incomplete_value": true,
      "site": "008f37b4",
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
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:2e1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f3718",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008f373c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008f375c",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008f3718",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008f373c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008f375c",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f3708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f3/008f36dc.md#insn-008f3708) · [`008f3714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f3/008f36dc.md#insn-008f3714) · [`008f3730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f3/008f36dc.md#insn-008f3730)
- 新版 [`008f3708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f3/008f36dc.md#insn-008f3708) · [`008f3714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f3/008f36dc.md#insn-008f3714) · [`008f3730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f3/008f36dc.md#insn-008f3730)

~~~diff
- 008f3708 ["COPY", "tmp:0:8", ["const:738:8"]]
- 008f3708 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008f3708 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008f3708 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008f3708 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 008f3708 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008f3708 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008f3708 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008f3708 bytes 73e21c91
+ 008f3708 bytes 73e21f91
- 008f3714 ["COPY", "tmp:0:8", ["const:2e4:8"]]
- 008f3714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f3714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f3714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f3714 ["COPY", "tmp:0:8", ["const:2dd:8"]]
+ 008f3714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f3714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f3714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f3714 bytes 29910b91
+ 008f3714 bytes 29750b91
- 008f3730 ["COPY", "tmp:0:8", ["const:2f7:8"]]
- 008f3730 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008f3730 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008f3730 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008f3730 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 008f3730 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008f3730 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008f3730 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008f3730 bytes 4add0b91
+ 008f3730 bytes 4ac10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be4299b2e03c5c467ea492677195715a"></a>

### [`008f40f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f4/008f40f0.md) → [`008f40f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f4/008f40f0.md) FUN_008f40f0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008f3f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f3/008f3f78.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00464a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`008f3f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f3/008f3f78.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.73% / 新版 93.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008f4144",
      "incomplete_value": false,
      "site": "008f4150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f4144",
      "incomplete_value": false,
      "site": "008f4150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "definition_site": "008f4168",
      "incomplete_value": true,
      "site": "008f4168",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d87:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f4168",
      "incomplete_value": true,
      "site": "008f4168",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d8e:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "008f416c",
      "incomplete_value": true,
      "site": "008f416c",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f416c",
      "incomplete_value": true,
      "site": "008f416c",
      "value": [
        "LOAD",
        "8",
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
                "const:5:8"
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
      "008f4150",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "008f4158",
      "READ",
      [
        "storage",
        "002a5d8e",
        null,
        null
      ]
    ],
    [
      "008f4160",
      "READ",
      [
        "storage",
        "002a5d93",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008f4150",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008f4158",
      "READ",
      [
        "storage",
        "002a5d87",
        null,
        null
      ]
    ],
    [
      "008f4160",
      "READ",
      [
        "storage",
        "002a5d8c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f4144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f4/008f40f0.md#insn-008f4144) · [`008f4148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f4/008f40f0.md#insn-008f4148)
- 新版 [`008f4144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f4/008f40f0.md#insn-008f4144) · [`008f4148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f4/008f40f0.md#insn-008f4148)

~~~diff
- 008f4144 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 008f4144 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f4144 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f4144 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f4144 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 008f4144 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f4144 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f4144 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f4144 bytes 08e13191
+ 008f4144 bytes 08a13491
- 008f4148 ["COPY", "register:4048:8", ["const:2a5000:8"]]
- 008f4148 bytes 89cdffb0
+ 008f4148 ["COPY", "register:4048:8", ["const:2a5000:8"]]
+ 008f4148 bytes 89cdffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3e8b2ef4449cec6719548cb558f2e18"></a>

### [`008f45ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f4/008f45ac.md) → [`008f45ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f4/008f45ac.md) FUN_008f45ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008f3f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f3/008f3f78.md) [`008f4f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f4/008f4f50.md) [`008f5270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5270.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md)
- 新版 呼出元 3件 [`008f3f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f3/008f3f78.md) [`008f4f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f4/008f4f50.md) [`008f5270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5270.md) · 呼出先 29件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.83% / 新版 96.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008f49d8",
      "incomplete_value": false,
      "site": "008f49d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f49d8",
      "incomplete_value": false,
      "site": "008f49d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008f4bec",
      "incomplete_value": false,
      "site": "008f4bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f4bec",
      "incomplete_value": false,
      "site": "008f4bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008f45e4",
      "incomplete_value": true,
      "site": "008f45e4",
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
      "definition_site": "008f45e4",
      "incomplete_value": true,
      "site": "008f45e4",
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
      "008f45e0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "008f45ec",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f45f4",
      "PARAM",
      [
        "storage",
        "00bfa3e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008f45e0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008f45ec",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008f45f4",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f45e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f4/008f45ac.md#insn-008f45e0) · [`008f45ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f4/008f45ac.md#insn-008f45ec) · [`008f45f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f4/008f45ac.md#insn-008f45f4)
- 新版 [`008f45e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f4/008f45ac.md#insn-008f45e0) · [`008f45ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f4/008f45ac.md#insn-008f45ec) · [`008f45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f4/008f45ac.md#insn-008f45f4)

~~~diff
- 008f45e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 008f45e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008f45e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 008f45e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008f45e0 bytes 08dd44f9
+ 008f45e0 bytes 083d45f9
- 008f45ec ["COPY", "tmp:0:8", ["const:d98:8"]]
- 008f45ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008f45ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008f45ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008f45ec ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 008f45ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008f45ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008f45ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008f45ec bytes 21603691
+ 008f45ec bytes 21203991
- 008f45f4 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 008f45f4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008f45f4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008f45f4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008f45f4 ["COPY", "tmp:0:8", ["const:490:8"]]
+ 008f45f4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008f45f4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008f45f4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008f45f4 bytes 42800f91
+ 008f45f4 bytes 42401291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffa8af4ba3ea968ac23eea8b2071dd38"></a>

### [`008f5020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5020.md) → [`008f5020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5020.md) FUN_008f5020

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00821cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00821/00821cbc.md) [`008226b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00822/008226b4.md) [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) [`008f45ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f4/008f45ac.md) [`008f5270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5270.md) · 呼出先 14件 [`0052dad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dad8.md) [`00678b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0067c/0067c9c4.md)
- 新版 呼出元 5件 [`00821cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cbc.md) [`008226b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00822/008226b4.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`008f45ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f4/008f45ac.md) [`008f5270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5270.md) · 呼出先 14件 [`0052dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dad8.md) [`00678b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c7f0.md) [`0067c9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c0.md) [`0067c9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0067c/0067c9c4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008f5054",
      "incomplete_value": false,
      "site": "008f505c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5054",
      "incomplete_value": false,
      "site": "008f505c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008f5164",
      "incomplete_value": false,
      "site": "008f516c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5164",
      "incomplete_value": false,
      "site": "008f516c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "008f505c",
      "DATA",
      [
        "storage",
        "00c084f0",
        null,
        "undefined *"
      ]
    ],
    [
      "008f516c",
      "DATA",
      [
        "storage",
        "00c08570",
        null,
        "undefined *"
      ]
    ],
    [
      "008f51b0",
      "READ",
      [
        "storage",
        "00c08510",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008f505c",
      "DATA",
      [
        "storage",
        "00c085a0",
        null,
        "undefined *"
      ]
    ],
    [
      "008f516c",
      "DATA",
      [
        "storage",
        "00c08620",
        null,
        "undefined *"
      ]
    ],
    [
      "008f51b0",
      "READ",
      [
        "storage",
        "00c085c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5020.md#insn-008f5054) · [`008f5164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5020.md#insn-008f5164)
- 新版 [`008f5054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5020.md#insn-008f5054) · [`008f5164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5020.md#insn-008f5164)

~~~diff
- 008f5054 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 008f5054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f5054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f5054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f5054 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 008f5054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f5054 bytes 08c11391
+ 008f5054 bytes 08811691
- 008f5164 ["COPY", "tmp:0:8", ["const:570:8"]]
- 008f5164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f5164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f5164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f5164 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 008f5164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f5164 bytes 08c11591
+ 008f5164 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fae56fbf23d27bfdab837d843788bd74"></a>

### [`008f5270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5270.md) → [`008f5270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5270.md) FUN_008f5270

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008f5a88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5a88.md) [`008f5b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5b5c.md) · 呼出先 27件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fac.md)
- 新版 呼出元 2件 [`008f5a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5a88.md) [`008f5b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5b5c.md) · 呼出先 27件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f5394",
      "incomplete_value": true,
      "site": "008f5394",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:236:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5394",
      "incomplete_value": true,
      "site": "008f5394",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:1a9:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008f53d8",
      "incomplete_value": false,
      "site": "008f53d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f53d8",
      "incomplete_value": false,
      "site": "008f53d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "definition_site": "008f548c",
      "incomplete_value": true,
      "site": "008f548c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:236:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f548c",
      "incomplete_value": true,
      "site": "008f548c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:1a9:8"
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
      "008f537c",
      "READ",
      [
        "storage",
        "002961a9",
        null,
        "string"
      ]
    ],
    [
      "008f53d8",
      "DATA",
      [
        "storage",
        "00c083f0",
        null,
        "undefined *"
      ]
    ],
    [
      "008f5474",
      "READ",
      [
        "storage",
        "002961a9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008f537c",
      "READ",
      [
        "storage",
        "00296236",
        null,
        "string"
      ]
    ],
    [
      "008f53d8",
      "DATA",
      [
        "storage",
        "00c084a0",
        null,
        "undefined *"
      ]
    ],
    [
      "008f5474",
      "READ",
      [
        "storage",
        "00296236",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5270.md#insn-008f5374) · [`008f53d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5270.md#insn-008f53d0) · [`008f53d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5270.md#insn-008f53d4)
- 新版 [`008f5374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5270.md#insn-008f5374) · [`008f53d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5270.md#insn-008f53d0)

~~~diff
- 008f5374 ["COPY", "tmp:0:8", ["const:1a9:8"]]
- 008f5374 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f5374 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f5374 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f5374 ["COPY", "tmp:0:8", ["const:236:8"]]
+ 008f5374 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5374 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5374 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f5374 bytes 29a50691
+ 008f5374 bytes 29d90891
- 008f53d0 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 008f53d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f53d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f53d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f53d0 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 008f53d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f53d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f53d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f53d0 bytes 08c10f91
+ 008f53d0 bytes 08811291
- 008f53d4 ["INT_SUB", "register:40b8:8", ["register:40e8:8", "const:40:8"]]
- 008f53d4 bytes b70301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fccec16c7cc283c894cfaecd3a2456f2"></a>

### [`008f5a38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5a38.md) → [`008f5a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5a38.md) FUN_008f5a38

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008f5a5c",
      "incomplete_value": false,
      "site": "008f5a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5a5c",
      "incomplete_value": false,
      "site": "008f5a5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "008f5a5c",
      "DATA",
      [
        "storage",
        "00c082f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f5a5c",
      "DATA",
      [
        "storage",
        "00c083a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5a58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5a38.md#insn-008f5a58)
- 新版 [`008f5a58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5a38.md#insn-008f5a58)

~~~diff
- 008f5a58 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 008f5a58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f5a58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f5a58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f5a58 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 008f5a58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5a58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5a58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f5a58 bytes 08c10b91
+ 008f5a58 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e472756328d2eb813978e9f77de36ee"></a>

### [`008f5a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5a6c.md) → [`008f5a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5a6c.md) FUN_008f5a6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008f5a78",
      "incomplete_value": false,
      "site": "008f5a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5a78",
      "incomplete_value": false,
      "site": "008f5a78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
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
      "008f5a78",
      "DATA",
      [
        "storage",
        "00c082f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f5a78",
      "DATA",
      [
        "storage",
        "00c083a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5a6c.md#insn-008f5a74)
- 新版 [`008f5a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5a6c.md#insn-008f5a74)

~~~diff
- 008f5a74 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 008f5a74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f5a74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f5a74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f5a74 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 008f5a74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5a74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5a74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f5a74 bytes 29c10b91
+ 008f5a74 bytes 29810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0338144fb9cf967b046c32734ade23ea"></a>

### [`008f5b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5b0c.md) → [`008f5b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5b0c.md) FUN_008f5b0c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008f5b30",
      "incomplete_value": false,
      "site": "008f5b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5b30",
      "incomplete_value": false,
      "site": "008f5b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "008f5b30",
      "DATA",
      [
        "storage",
        "00c08370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f5b30",
      "DATA",
      [
        "storage",
        "00c08420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5b0c.md#insn-008f5b2c)
- 新版 [`008f5b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5b0c.md#insn-008f5b2c)

~~~diff
- 008f5b2c ["COPY", "tmp:0:8", ["const:370:8"]]
- 008f5b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f5b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f5b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f5b2c ["COPY", "tmp:0:8", ["const:420:8"]]
+ 008f5b2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5b2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5b2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f5b2c bytes 08c10d91
+ 008f5b2c bytes 08811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ab874ba0e22e7f605d2b5aabc3e45d8"></a>

### [`008f5b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5b40.md) → [`008f5b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5b40.md) FUN_008f5b40

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008f5b4c",
      "incomplete_value": false,
      "site": "008f5b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5b4c",
      "incomplete_value": false,
      "site": "008f5b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "008f5b4c",
      "DATA",
      [
        "storage",
        "00c08370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f5b4c",
      "DATA",
      [
        "storage",
        "00c08420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5b40.md#insn-008f5b48)
- 新版 [`008f5b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5b40.md#insn-008f5b48)

~~~diff
- 008f5b48 ["COPY", "tmp:0:8", ["const:370:8"]]
- 008f5b48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f5b48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f5b48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f5b48 ["COPY", "tmp:0:8", ["const:420:8"]]
+ 008f5b48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5b48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5b48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f5b48 bytes 29c10d91
+ 008f5b48 bytes 29811091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29c4fce608c60c28ace155d4baf8f99f"></a>

### [`008f5be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5be0.md) → [`008f5be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5be0.md) FUN_008f5be0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008f5c04",
      "incomplete_value": false,
      "site": "008f5c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5c04",
      "incomplete_value": false,
      "site": "008f5c04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "008f5c04",
      "DATA",
      [
        "storage",
        "00c083f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f5c04",
      "DATA",
      [
        "storage",
        "00c084a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5c00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5be0.md#insn-008f5c00)
- 新版 [`008f5c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5be0.md#insn-008f5c00)

~~~diff
- 008f5c00 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 008f5c00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f5c00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f5c00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f5c00 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 008f5c00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5c00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5c00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f5c00 bytes 08c10f91
+ 008f5c00 bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30e02d8fcf19e64e4dec687afe7bfd37"></a>

### [`008f5c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5c14.md) → [`008f5c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5c14.md) FUN_008f5c14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008f5c20",
      "incomplete_value": false,
      "site": "008f5c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5c20",
      "incomplete_value": false,
      "site": "008f5c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "008f5c20",
      "DATA",
      [
        "storage",
        "00c083f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f5c20",
      "DATA",
      [
        "storage",
        "00c084a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5c1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5c14.md#insn-008f5c1c)
- 新版 [`008f5c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5c14.md#insn-008f5c1c)

~~~diff
- 008f5c1c ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 008f5c1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f5c1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f5c1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f5c1c ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 008f5c1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5c1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5c1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f5c1c bytes 29c10f91
+ 008f5c1c bytes 29811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5121ff5aa782d15ce30503c25e0eca"></a>

### [`008f5cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5cb8.md) → [`008f5cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5cb8.md) FUN_008f5cb8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008f5cdc",
      "incomplete_value": false,
      "site": "008f5cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5cdc",
      "incomplete_value": false,
      "site": "008f5cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "008f5cdc",
      "DATA",
      [
        "storage",
        "00c08470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f5cdc",
      "DATA",
      [
        "storage",
        "00c08520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5cd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5cb8.md#insn-008f5cd8)
- 新版 [`008f5cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5cb8.md#insn-008f5cd8)

~~~diff
- 008f5cd8 ["COPY", "tmp:0:8", ["const:470:8"]]
- 008f5cd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f5cd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f5cd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f5cd8 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 008f5cd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5cd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5cd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f5cd8 bytes 08c11191
+ 008f5cd8 bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b41c278b591a8774e4334157be4bae3d"></a>

### [`008f5cec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5cec.md) → [`008f5cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5cec.md) FUN_008f5cec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008f5cf8",
      "incomplete_value": false,
      "site": "008f5cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5cf8",
      "incomplete_value": false,
      "site": "008f5cf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "008f5cf8",
      "DATA",
      [
        "storage",
        "00c08470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f5cf8",
      "DATA",
      [
        "storage",
        "00c08520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5cec.md#insn-008f5cf4)
- 新版 [`008f5cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5cec.md#insn-008f5cf4)

~~~diff
- 008f5cf4 ["COPY", "tmp:0:8", ["const:470:8"]]
- 008f5cf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f5cf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f5cf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f5cf4 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 008f5cf4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5cf4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5cf4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f5cf4 bytes 29c11191
+ 008f5cf4 bytes 29811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cf28428cb2c8e67184b5b0cb6479297"></a>

### [`008f5d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5d90.md) → [`008f5d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5d90.md) FUN_008f5d90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008f5db0",
      "incomplete_value": false,
      "site": "008f5db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5db0",
      "incomplete_value": false,
      "site": "008f5db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "008f5db4",
      "DATA",
      [
        "storage",
        "00c084f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f5db4",
      "DATA",
      [
        "storage",
        "00c085a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5d90.md#insn-008f5db0)
- 新版 [`008f5db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5d90.md#insn-008f5db0)

~~~diff
- 008f5db0 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 008f5db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f5db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f5db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f5db0 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 008f5db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f5db0 bytes 08c11391
+ 008f5db0 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd34cf727fb9c5688ed88940a851b9ab"></a>

### [`008f5dc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5dc8.md) → [`008f5dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5dc8.md) FUN_008f5dc8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008f5dcc",
      "incomplete_value": false,
      "site": "008f5dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5dcc",
      "incomplete_value": false,
      "site": "008f5dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "008f5dd0",
      "DATA",
      [
        "storage",
        "00c084f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f5dd0",
      "DATA",
      [
        "storage",
        "00c085a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5dc8.md#insn-008f5dcc)
- 新版 [`008f5dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5dc8.md#insn-008f5dcc)

~~~diff
- 008f5dcc ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 008f5dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f5dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f5dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f5dcc ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 008f5dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f5dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f5dcc bytes 08c11391
+ 008f5dcc bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4995bb27b7248578c96f9d4be8768bf6"></a>

### [`008f5e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5e28.md) → [`008f5e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5e28.md) FUN_008f5e28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008f5de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5de8.md) [`008f61ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f61ac.md) · 呼出先 10件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fac.md) [`0052dae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dae4.md) [`00574ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574ff0.md)
- 新版 呼出元 2件 [`008f5de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5de8.md) [`008f61ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f61ac.md) · 呼出先 10件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`0052dae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dae4.md) [`00574ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.21% / 新版 96.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f5ed8",
      "incomplete_value": true,
      "site": "008f5ed8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:b78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f5ed8",
      "incomplete_value": true,
      "site": "008f5ed8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:aeb:8"
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
      "definition_site": "008f5edc",
      "incomplete_value": true,
      "site": "008f5edc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008f5edc",
      "incomplete_value": true,
      "site": "008f5edc",
      "value": [
        "LOAD",
        "8",
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
      "008f5ec8",
      "READ",
      [
        "storage",
        "0029eaeb",
        null,
        "string"
      ]
    ],
    [
      "008f5ecc",
      "READ",
      [
        "storage",
        "0029eaf1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008f5ec8",
      "READ",
      [
        "storage",
        "0029eb78",
        null,
        "string"
      ]
    ],
    [
      "008f5ecc",
      "READ",
      [
        "storage",
        "0029eb7e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f5ec0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f5/008f5e28.md#insn-008f5ec0)
- 新版 [`008f5ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f5/008f5e28.md#insn-008f5ec0)

~~~diff
- 008f5ec0 ["COPY", "tmp:0:8", ["const:aeb:8"]]
- 008f5ec0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f5ec0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f5ec0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f5ec0 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 008f5ec0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5ec0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f5ec0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f5ec0 bytes 29ad2b91
+ 008f5ec0 bytes 29e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07cd70172516ef59a94edd81eed5eaa5"></a>

### [`008f6154`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f6154.md) → [`008f6154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f6154.md) FUN_008f6154

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008f6174",
      "incomplete_value": false,
      "site": "008f6178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f6174",
      "incomplete_value": false,
      "site": "008f6178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "008f6178",
      "DATA",
      [
        "storage",
        "00c08570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f6178",
      "DATA",
      [
        "storage",
        "00c08620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f6174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f6154.md#insn-008f6174)
- 新版 [`008f6174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f6154.md#insn-008f6174)

~~~diff
- 008f6174 ["COPY", "tmp:0:8", ["const:570:8"]]
- 008f6174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f6174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f6174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f6174 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 008f6174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f6174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f6174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f6174 bytes 08c11591
+ 008f6174 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b8a926298b45fb3cce9d79234ebc9b5"></a>

### [`008f618c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f618c.md) → [`008f618c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f618c.md) FUN_008f618c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008f6190",
      "incomplete_value": false,
      "site": "008f6194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f6190",
      "incomplete_value": false,
      "site": "008f6194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "008f6194",
      "DATA",
      [
        "storage",
        "00c08570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008f6194",
      "DATA",
      [
        "storage",
        "00c08620",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f6190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f618c.md#insn-008f6190)
- 新版 [`008f6190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f618c.md#insn-008f6190)

~~~diff
- 008f6190 ["COPY", "tmp:0:8", ["const:570:8"]]
- 008f6190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008f6190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008f6190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008f6190 ["COPY", "tmp:0:8", ["const:620:8"]]
+ 008f6190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008f6190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008f6190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008f6190 bytes 08c11591
+ 008f6190 bytes 08811891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fe9b5be545368726319e92e382d8c04"></a>

### [`008f61ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f61ec.md) → [`008f61ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f61ec.md) _INIT_178

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.57% / 新版 87.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f6228",
      "incomplete_value": true,
      "site": "008f6244",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2dd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f6228",
      "incomplete_value": true,
      "site": "008f6244",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2e4:8"
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
      "definition_site": "008f624c",
      "incomplete_value": true,
      "site": "008f6268",
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
                "const:2a7000:8"
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
      "definition_site": "008f624c",
      "incomplete_value": true,
      "site": "008f6268",
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
                "const:2a7000:8"
              ],
              [
                "leaf",
                "const:2f7:8"
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
      "definition_site": "008f626c",
      "incomplete_value": true,
      "site": "008f6288",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f626c",
      "incomplete_value": true,
      "site": "008f6288",
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
                "const:2a8000:8"
              ],
              [
                "leaf",
                "const:da:8"
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
      "008f6228",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "008f624c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "008f626c",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008f6228",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008f624c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008f626c",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f6218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f61ec.md#insn-008f6218) · [`008f6220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f61ec.md#insn-008f6220)
- 新版 [`008f6218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f61ec.md#insn-008f6218) · [`008f6220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f61ec.md#insn-008f6220)

~~~diff
- 008f6218 ["COPY", "tmp:0:8", ["const:750:8"]]
- 008f6218 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008f6218 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008f6218 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008f6218 ["COPY", "tmp:0:8", ["const:810:8"]]
+ 008f6218 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008f6218 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008f6218 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008f6218 bytes 73421d91
+ 008f6218 bytes 73422091
- 008f6220 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008f6220 bytes 89cdffb0
+ 008f6220 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008f6220 bytes 89cdffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fcde85dcc2382528af7d63717f17a59"></a>

### [`008f657c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f657c.md) → [`008f657c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f657c.md) FUN_008f657c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`008f95c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f9/008f95c0.md) [`008fbbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fb/008fbbc8.md) [`00900188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900188.md) · 呼出先 53件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`0045a1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a1f0.md) [`0045a1f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a1f8.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md)
- 新版 呼出元 3件 [`008f95c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f9/008f95c0.md) [`008fbbc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fb/008fbbc8.md) [`00900188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900188.md) · 呼出先 53件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`0045a1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a1f0.md) [`0045a1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a1f8.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 20件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008f6840",
      "incomplete_value": false,
      "site": "008f6840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f6840",
      "incomplete_value": false,
      "site": "008f6840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008f6abc",
      "incomplete_value": false,
      "site": "008f6abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f6abc",
      "incomplete_value": false,
      "site": "008f6abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "definition_site": "008f6ea4",
      "incomplete_value": true,
      "site": "008f6ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f6ea4",
      "incomplete_value": true,
      "site": "008f6ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:6f0:8"
          ]
        ]
      ]
    },
    "ordinal": 79,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f66dc",
      "READ",
      [
        "storage",
        "00c1b470",
        null,
        "pointer"
      ]
    ],
    [
      "008f66f0",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ],
    [
      "008f6708",
      "READ",
      [
        "storage",
        "00c1b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008f66dc",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "008f66f0",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "008f6708",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f66dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f657c.md#insn-008f66dc) · [`008f6708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f657c.md#insn-008f6708) · [`008f6838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f657c.md#insn-008f6838)
- 新版 [`008f66dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f657c.md#insn-008f66dc) · [`008f6708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f657c.md#insn-008f6708) · [`008f6838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f657c.md#insn-008f6838)

~~~diff
- 008f66dc ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:470:8"]]
- 008f66dc ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 008f66dc ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:520:8"]]
+ 008f66dc ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 008f66dc bytes 7b3b42f9
+ 008f66dc bytes 7b9342f9
- 008f6708 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:478:8"]]
- 008f6708 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 008f6708 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:528:8"]]
+ 008f6708 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 008f6708 bytes 5a3f42f9
+ 008f6708 bytes 5a9742f9
- 008f6838 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 008f6838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f6838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f6838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f6838 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 008f6838 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f6838 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f6838 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f6838 bytes 29c11791
+ 008f6838 bytes 29811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a1d996090275a35d900169f2a02dff6"></a>

### [`008f93f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f9/008f93f0.md) → [`008f93f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f9/008f93f0.md) FUN_008f93f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`008f657c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f6/008f657c.md) [`008f9e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f9/008f9e20.md) [`008fe98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe98c.md) [`008feab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008feab4.md) [`008ff260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff260.md) · 呼出先 4件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`009019f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/009019f4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 6件 [`008f657c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f6/008f657c.md) [`008f9e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f9/008f9e20.md) [`008fe98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe98c.md) [`008feab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008feab4.md) [`008ff260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff260.md) · 呼出先 4件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009019f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/009019f4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.88% / 新版 93.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008f9494",
      "incomplete_value": true,
      "site": "008f94ac",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:f32:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f9494",
      "incomplete_value": true,
      "site": "008f94ac",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:ea5:8"
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
      "definition_site": "008f9500",
      "incomplete_value": true,
      "site": "008f9518",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:4f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008f9500",
      "incomplete_value": true,
      "site": "008f9518",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:463:8"
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
      "008f9494",
      "READ",
      [
        "storage",
        "00292ea5",
        null,
        "string"
      ]
    ],
    [
      "008f9500",
      "READ",
      [
        "storage",
        "00299463",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008f9494",
      "READ",
      [
        "storage",
        "00292f32",
        null,
        "string"
      ]
    ],
    [
      "008f9500",
      "READ",
      [
        "storage",
        "002994f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f948c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f9/008f93f0.md#insn-008f948c) · [`008f94f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f9/008f93f0.md#insn-008f94f8)
- 新版 [`008f948c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f9/008f93f0.md#insn-008f948c) · [`008f94f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f9/008f93f0.md#insn-008f94f8)

~~~diff
- 008f948c ["COPY", "tmp:0:8", ["const:ea5:8"]]
- 008f948c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f948c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f948c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f948c ["COPY", "tmp:0:8", ["const:f32:8"]]
+ 008f948c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f948c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f948c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f948c bytes 29953a91
+ 008f948c bytes 29c93c91
- 008f94f8 ["COPY", "tmp:0:8", ["const:463:8"]]
- 008f94f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008f94f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008f94f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008f94f8 ["COPY", "tmp:0:8", ["const:4f0:8"]]
+ 008f94f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008f94f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008f94f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008f94f8 bytes 298d1191
+ 008f94f8 bytes 29c11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3027f3b0fe6beebd4dda829c7f9be951"></a>

### [`008f9e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f9/008f9e20.md) → [`008f9e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f9/008f9e20.md) FUN_008f9e20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008fbbc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fb/008fbbc8.md) [`00900188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00900/00900188.md) · 呼出先 39件 [`00449aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`0045a1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a1f0.md) [`0045a1f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a1f8.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md)
- 新版 呼出元 2件 [`008fbbc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fb/008fbbc8.md) [`00900188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/00900188.md) · 呼出先 39件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`0045a1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a1f0.md) [`0045a1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a1f8.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.13% / 新版 98.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fa128",
      "incomplete_value": false,
      "site": "008fa128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fa128",
      "incomplete_value": false,
      "site": "008fa128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:2f0:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fa53c",
      "incomplete_value": false,
      "site": "008fa53c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fa53c",
      "incomplete_value": false,
      "site": "008fa53c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fa700",
      "incomplete_value": false,
      "site": "008fa700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:4a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fa700",
      "incomplete_value": false,
      "site": "008fa700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c09000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "ordinal": 79,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008f9fc4",
      "READ",
      [
        "storage",
        "00c1b470",
        null,
        "pointer"
      ]
    ],
    [
      "008f9fd8",
      "DATA",
      [
        "storage",
        "00c0bc38",
        null,
        "undefined *"
      ]
    ],
    [
      "008f9ff0",
      "READ",
      [
        "storage",
        "00c1b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008f9fc4",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ],
    [
      "008f9fd8",
      "DATA",
      [
        "storage",
        "00c0bce8",
        null,
        "undefined *"
      ]
    ],
    [
      "008f9ff0",
      "READ",
      [
        "storage",
        "00c1b528",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008f9fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f9/008f9e20.md#insn-008f9fc4) · [`008f9ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f9/008f9e20.md#insn-008f9ff0) · [`008fa120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008f9/008f9e20.md#insn-008fa120)
- 新版 [`008f9fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f9/008f9e20.md#insn-008f9fc4) · [`008f9ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f9/008f9e20.md#insn-008f9ff0) · [`008fa120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008f9/008f9e20.md#insn-008fa120)

~~~diff
- 008f9fc4 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:470:8"]]
- 008f9fc4 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 008f9fc4 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:520:8"]]
+ 008f9fc4 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 008f9fc4 bytes 7b3b42f9
+ 008f9fc4 bytes 7b9342f9
- 008f9ff0 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:478:8"]]
- 008f9ff0 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
+ 008f9ff0 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:528:8"]]
+ 008f9ff0 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
- 008f9ff0 bytes 9c3f42f9
+ 008f9ff0 bytes 9c9742f9
- 008fa120 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 008fa120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008fa120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008fa120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008fa120 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 008fa120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008fa120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008fa120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008fa120 bytes 29c10b91
+ 008fa120 bytes 29810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68c88e7e52f10181c4fc8b67ef867268"></a>

### [`008fbce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fb/008fbce8.md) → [`008fbce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fb/008fbce8.md) FUN_008fbce8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`008fe98c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe98c.md) [`008feab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008feab4.md) [`008ff260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff260.md) [`008ff388`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008ff/008ff388.md) · 呼出先 4件 [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`009019f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00901/009019f4.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 4件 [`008fe98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe98c.md) [`008feab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008feab4.md) [`008ff260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff260.md) [`008ff388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ff/008ff388.md) · 呼出先 4件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009019f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/009019f4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.40% / 新版 91.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008fbd60",
      "incomplete_value": true,
      "site": "008fbd78",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:f32:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fbd60",
      "incomplete_value": true,
      "site": "008fbd78",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:ea5:8"
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
      "definition_site": "008fbda4",
      "incomplete_value": true,
      "site": "008fbdbc",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:4f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fbda4",
      "incomplete_value": true,
      "site": "008fbdbc",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:463:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008fbd60",
      "READ",
      [
        "storage",
        "00292ea5",
        null,
        "string"
      ]
    ],
    [
      "008fbda4",
      "READ",
      [
        "storage",
        "00299463",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008fbd60",
      "READ",
      [
        "storage",
        "00292f32",
        null,
        "string"
      ]
    ],
    [
      "008fbda4",
      "READ",
      [
        "storage",
        "002994f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fbd58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fb/008fbce8.md#insn-008fbd58) · [`008fbd5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fb/008fbce8.md#insn-008fbd5c)
- 新版 [`008fbd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fb/008fbce8.md#insn-008fbd58) · [`008fbd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fb/008fbce8.md#insn-008fbd5c)

~~~diff
- 008fbd58 ["COPY", "tmp:0:8", ["const:ea5:8"]]
- 008fbd58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008fbd58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008fbd58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008fbd58 ["COPY", "tmp:0:8", ["const:f32:8"]]
+ 008fbd58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008fbd58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008fbd58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008fbd58 bytes 29953a91
+ 008fbd58 bytes 29c93c91
- 008fbd5c ["COPY", "register:4050:8", ["const:6567:8"]]
- 008fbd5c bytes eaac8c52
+ 008fbd5c ["COPY", "register:4050:8", ["const:6567:8"]]
+ 008fbd5c bytes eaac8c52
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c25dc4bf563fe6b185574df50428f5ae"></a>

### [`008fbee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fb/008fbee0.md) → [`008fbee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fb/008fbee0.md) FUN_008fbee0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fbef4",
      "incomplete_value": false,
      "site": "008fbef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fbef4",
      "incomplete_value": false,
      "site": "008fbef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "008fbef8",
      "DATA",
      [
        "storage",
        "00c085f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fbef8",
      "DATA",
      [
        "storage",
        "00c086a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fbef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fb/008fbee0.md#insn-008fbef4)
- 新版 [`008fbef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fb/008fbee0.md#insn-008fbef4)

~~~diff
- 008fbef4 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 008fbef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fbef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fbef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fbef4 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 008fbef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fbef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fbef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fbef4 bytes 08c11791
+ 008fbef4 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-183bf3d5d13324c9c9f6b50d67d844e8"></a>

### [`008fbf04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fb/008fbf04.md) → [`008fbf04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fb/008fbf04.md) FUN_008fbf04

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fbf08",
      "incomplete_value": false,
      "site": "008fbf0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fbf08",
      "incomplete_value": false,
      "site": "008fbf0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "008fbf0c",
      "DATA",
      [
        "storage",
        "00c085f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fbf0c",
      "DATA",
      [
        "storage",
        "00c086a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fbf08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fb/008fbf04.md#insn-008fbf08)
- 新版 [`008fbf08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fb/008fbf04.md#insn-008fbf08)

~~~diff
- 008fbf08 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 008fbf08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fbf08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fbf08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fbf08 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 008fbf08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fbf08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fbf08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fbf08 bytes 08c11791
+ 008fbf08 bytes 08811a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2e7fbf041c7413449f32f9b15ea6bba"></a>

### [`008fc04c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc04c.md) → [`008fc04c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc04c.md) FUN_008fc04c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fc060",
      "incomplete_value": false,
      "site": "008fc064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc060",
      "incomplete_value": false,
      "site": "008fc064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "008fc064",
      "DATA",
      [
        "storage",
        "00c08670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fc064",
      "DATA",
      [
        "storage",
        "00c08720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fc060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc04c.md#insn-008fc060)
- 新版 [`008fc060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc04c.md#insn-008fc060)

~~~diff
- 008fc060 ["COPY", "tmp:0:8", ["const:670:8"]]
- 008fc060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fc060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fc060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fc060 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 008fc060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fc060 bytes 08c11991
+ 008fc060 bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81ec42985c9d845a9bd0acba1859bf91"></a>

### [`008fc070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc070.md) → [`008fc070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc070.md) FUN_008fc070

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fc074",
      "incomplete_value": false,
      "site": "008fc078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc074",
      "incomplete_value": false,
      "site": "008fc078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "008fc078",
      "DATA",
      [
        "storage",
        "00c08670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fc078",
      "DATA",
      [
        "storage",
        "00c08720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fc074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc070.md#insn-008fc074)
- 新版 [`008fc074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc070.md#insn-008fc074)

~~~diff
- 008fc074 ["COPY", "tmp:0:8", ["const:670:8"]]
- 008fc074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fc074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fc074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fc074 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 008fc074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fc074 bytes 08c11991
+ 008fc074 bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96804691b9c71a9486c60e54ec62ec63"></a>

### [`008fc1b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc1b4.md) → [`008fc1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc1b4.md) FUN_008fc1b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fc1c8",
      "incomplete_value": false,
      "site": "008fc1cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc1c8",
      "incomplete_value": false,
      "site": "008fc1cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "008fc1cc",
      "DATA",
      [
        "storage",
        "00c086f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fc1cc",
      "DATA",
      [
        "storage",
        "00c087a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fc1c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc1b4.md#insn-008fc1c8)
- 新版 [`008fc1c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc1b4.md#insn-008fc1c8)

~~~diff
- 008fc1c8 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 008fc1c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fc1c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fc1c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fc1c8 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 008fc1c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc1c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc1c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fc1c8 bytes 08c11b91
+ 008fc1c8 bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6192f9103ef5199db7bfc6b639dc1e00"></a>

### [`008fc1d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc1d8.md) → [`008fc1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc1d8.md) FUN_008fc1d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fc1dc",
      "incomplete_value": false,
      "site": "008fc1e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc1dc",
      "incomplete_value": false,
      "site": "008fc1e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "008fc1e0",
      "DATA",
      [
        "storage",
        "00c086f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fc1e0",
      "DATA",
      [
        "storage",
        "00c087a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fc1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc1d8.md#insn-008fc1dc)
- 新版 [`008fc1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc1d8.md#insn-008fc1dc)

~~~diff
- 008fc1dc ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 008fc1dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fc1dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fc1dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fc1dc ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 008fc1dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc1dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc1dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fc1dc bytes 08c11b91
+ 008fc1dc bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3246ab55a425ce55115254c0242e2414"></a>

### [`008fc320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc320.md) → [`008fc320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc320.md) FUN_008fc320

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fc334",
      "incomplete_value": false,
      "site": "008fc338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc334",
      "incomplete_value": false,
      "site": "008fc338",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "008fc338",
      "DATA",
      [
        "storage",
        "00c08770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fc338",
      "DATA",
      [
        "storage",
        "00c08820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fc334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc320.md#insn-008fc334)
- 新版 [`008fc334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc320.md#insn-008fc334)

~~~diff
- 008fc334 ["COPY", "tmp:0:8", ["const:770:8"]]
- 008fc334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fc334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fc334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fc334 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 008fc334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fc334 bytes 08c11d91
+ 008fc334 bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-106feb8c7d4efd563b22d88766bb384a"></a>

### [`008fc344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc344.md) → [`008fc344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc344.md) FUN_008fc344

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fc348",
      "incomplete_value": false,
      "site": "008fc34c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc348",
      "incomplete_value": false,
      "site": "008fc34c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "008fc34c",
      "DATA",
      [
        "storage",
        "00c08770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fc34c",
      "DATA",
      [
        "storage",
        "00c08820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fc348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc344.md#insn-008fc348)
- 新版 [`008fc348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc344.md#insn-008fc348)

~~~diff
- 008fc348 ["COPY", "tmp:0:8", ["const:770:8"]]
- 008fc348 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fc348 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fc348 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fc348 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 008fc348 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc348 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc348 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fc348 bytes 08c11d91
+ 008fc348 bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2235a3981c8b8877b565d87ea716d2c4"></a>

### [`008fc35c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc35c.md) → [`008fc35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc35c.md) FUN_008fc35c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fff8.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md)
- 新版 呼出元 0件  · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fff8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.11% / 新版 97.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fc6ac",
      "incomplete_value": false,
      "site": "008fc6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc6ac",
      "incomplete_value": false,
      "site": "008fc6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "definition_site": "008fc6e4",
      "incomplete_value": false,
      "site": "008fc6e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc6e4",
      "incomplete_value": false,
      "site": "008fc6e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "008fc514",
      "PARAM",
      [
        "storage",
        "002a7b7f",
        null,
        "string"
      ]
    ],
    [
      "008fc514",
      "PARAM",
      [
        "storage",
        "002a293a",
        null,
        "string"
      ]
    ],
    [
      "008fc6ac",
      "DATA",
      [
        "storage",
        "00c087e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fc514",
      "PARAM",
      [
        "storage",
        "002a7aeb",
        null,
        "string"
      ]
    ],
    [
      "008fc514",
      "PARAM",
      [
        "storage",
        "002a2933",
        null,
        "string"
      ]
    ],
    [
      "008fc6ac",
      "DATA",
      [
        "storage",
        "00c08890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fc500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc35c.md#insn-008fc500) · [`008fc508`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc35c.md#insn-008fc508)
- 新版 [`008fc500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc35c.md#insn-008fc500) · [`008fc508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc35c.md#insn-008fc508)

~~~diff
- 008fc500 ["COPY", "tmp:0:8", ["const:b7f:8"]]
- 008fc500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fc500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fc500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fc500 ["COPY", "tmp:0:8", ["const:aeb:8"]]
+ 008fc500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fc500 bytes 08fd2d91
+ 008fc500 bytes 08ad2b91
- 008fc508 ["COPY", "register:4050:8", ["const:2a2000:8"]]
- 008fc508 bytes 2acdffd0
+ 008fc508 ["COPY", "register:4050:8", ["const:2a2000:8"]]
+ 008fc508 bytes 2acdffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e89a26384fd9756480a3090c1a55faa0"></a>

### [`008fc8dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc8dc.md) → [`008fc8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc8dc.md) FUN_008fc8dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fc8f0",
      "incomplete_value": false,
      "site": "008fc8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc8f0",
      "incomplete_value": false,
      "site": "008fc8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "008fc8f4",
      "DATA",
      [
        "storage",
        "00c087e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fc8f4",
      "DATA",
      [
        "storage",
        "00c08890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fc8f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc8dc.md#insn-008fc8f0)
- 新版 [`008fc8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc8dc.md#insn-008fc8f0)

~~~diff
- 008fc8f0 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 008fc8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fc8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fc8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fc8f0 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 008fc8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fc8f0 bytes 08811f91
+ 008fc8f0 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1ad2e428634f54e580651167385d7a7"></a>

### [`008fc900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc900.md) → [`008fc900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc900.md) FUN_008fc900

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fc904",
      "incomplete_value": false,
      "site": "008fc908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc904",
      "incomplete_value": false,
      "site": "008fc908",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
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
      "008fc908",
      "DATA",
      [
        "storage",
        "00c087e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fc908",
      "DATA",
      [
        "storage",
        "00c08890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fc904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc900.md#insn-008fc904)
- 新版 [`008fc904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc900.md#insn-008fc904)

~~~diff
- 008fc904 ["COPY", "tmp:0:8", ["const:7e0:8"]]
- 008fc904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fc904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fc904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fc904 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 008fc904 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc904 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc904 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fc904 bytes 08811f91
+ 008fc904 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b171284e8c4d0eaa76ca24d51a6b23c"></a>

### [`008fc9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc9c0.md) → [`008fc9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc9c0.md) FUN_008fc9c0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fc9d4",
      "incomplete_value": false,
      "site": "008fc9d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc9d4",
      "incomplete_value": false,
      "site": "008fc9d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "008fc9d8",
      "DATA",
      [
        "storage",
        "00c08860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fc9d8",
      "DATA",
      [
        "storage",
        "00c08910",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fc9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc9c0.md#insn-008fc9d4)
- 新版 [`008fc9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc9c0.md#insn-008fc9d4)

~~~diff
- 008fc9d4 ["COPY", "tmp:0:8", ["const:860:8"]]
- 008fc9d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fc9d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fc9d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fc9d4 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 008fc9d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc9d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc9d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fc9d4 bytes 08812191
+ 008fc9d4 bytes 08412491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0d1e22d3017f4190c3e5189a9561562"></a>

### [`008fc9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc9e4.md) → [`008fc9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc9e4.md) FUN_008fc9e4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fc9e8",
      "incomplete_value": false,
      "site": "008fc9ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:910:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fc9e8",
      "incomplete_value": false,
      "site": "008fc9ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "008fc9ec",
      "DATA",
      [
        "storage",
        "00c08860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fc9ec",
      "DATA",
      [
        "storage",
        "00c08910",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fc9e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fc9e4.md#insn-008fc9e8)
- 新版 [`008fc9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc9e4.md#insn-008fc9e8)

~~~diff
- 008fc9e8 ["COPY", "tmp:0:8", ["const:860:8"]]
- 008fc9e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fc9e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fc9e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fc9e8 ["COPY", "tmp:0:8", ["const:910:8"]]
+ 008fc9e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc9e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fc9e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fc9e8 bytes 08812191
+ 008fc9e8 bytes 08412491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f0b0aa0336f9f8d2f6d49470c5c5976"></a>

### [`008fcaa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcaa4.md) → [`008fcaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcaa4.md) FUN_008fcaa4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fcac8",
      "incomplete_value": false,
      "site": "008fcac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fcac8",
      "incomplete_value": false,
      "site": "008fcac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "008fcac8",
      "DATA",
      [
        "storage",
        "00c088f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fcac8",
      "DATA",
      [
        "storage",
        "00c089a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fcac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcaa4.md#insn-008fcac4)
- 新版 [`008fcac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcaa4.md#insn-008fcac4)

~~~diff
- 008fcac4 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 008fcac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fcac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fcac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fcac4 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 008fcac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fcac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fcac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fcac4 bytes 08c12391
+ 008fcac4 bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe0546bd39b0de11aeb91e8bbc8c757f"></a>

### [`008fcad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcad8.md) → [`008fcad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcad8.md) FUN_008fcad8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fcae4",
      "incomplete_value": false,
      "site": "008fcae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fcae4",
      "incomplete_value": false,
      "site": "008fcae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "008fcae4",
      "DATA",
      [
        "storage",
        "00c088f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fcae4",
      "DATA",
      [
        "storage",
        "00c089a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fcae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcad8.md#insn-008fcae0)
- 新版 [`008fcae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcad8.md#insn-008fcae0)

~~~diff
- 008fcae0 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 008fcae0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008fcae0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008fcae0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008fcae0 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 008fcae0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008fcae0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008fcae0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008fcae0 bytes 29c12391
+ 008fcae0 bytes 29812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7aed6806511986fe01b620ab4ece3952"></a>

### [`008fcaf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcaf4.md) → [`008fcaf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcaf4.md) FUN_008fcaf4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`0053d984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d984.md) [`0073e258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e258.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0053d984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d984.md) [`0073e258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e258.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.94% / 新版 97.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fcce8",
      "incomplete_value": false,
      "site": "008fccf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fcce8",
      "incomplete_value": false,
      "site": "008fccf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fcd20",
      "incomplete_value": false,
      "site": "008fcd30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fcd20",
      "incomplete_value": false,
      "site": "008fcd30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "008fccf8",
      "DATA",
      [
        "storage",
        "00c08960",
        null,
        "undefined *"
      ]
    ],
    [
      "008fcd30",
      "DATA",
      [
        "storage",
        "00c089e0",
        null,
        "undefined *"
      ]
    ],
    [
      "008fcd6c",
      "READ",
      [
        "storage",
        "00c08980",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008fccf8",
      "DATA",
      [
        "storage",
        "00c08a10",
        null,
        "undefined *"
      ]
    ],
    [
      "008fcd30",
      "DATA",
      [
        "storage",
        "00c08a90",
        null,
        "undefined *"
      ]
    ],
    [
      "008fcd6c",
      "READ",
      [
        "storage",
        "00c08a30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fcce8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcaf4.md#insn-008fcce8) · [`008fcd20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcaf4.md#insn-008fcd20)
- 新版 [`008fcce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcaf4.md#insn-008fcce8) · [`008fcd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcaf4.md#insn-008fcd20)

~~~diff
- 008fcce8 ["COPY", "tmp:0:8", ["const:960:8"]]
- 008fcce8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fcce8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fcce8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fcce8 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 008fcce8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fcce8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fcce8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fcce8 bytes 08812591
+ 008fcce8 bytes 08412891
- 008fcd20 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 008fcd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fcd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fcd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fcd20 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 008fcd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fcd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fcd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fcd20 bytes 08812791
+ 008fcd20 bytes 08412a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87d84caec671dd2d243d2129a85b8b55"></a>

### [`008fce88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fce88.md) → [`008fce88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fce88.md) FUN_008fce88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fce9c",
      "incomplete_value": false,
      "site": "008fcea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fce9c",
      "incomplete_value": false,
      "site": "008fcea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "008fcea0",
      "DATA",
      [
        "storage",
        "00c08960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fcea0",
      "DATA",
      [
        "storage",
        "00c08a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fce9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fce88.md#insn-008fce9c)
- 新版 [`008fce9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fce88.md#insn-008fce9c)

~~~diff
- 008fce9c ["COPY", "tmp:0:8", ["const:960:8"]]
- 008fce9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fce9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fce9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fce9c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 008fce9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fce9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fce9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fce9c bytes 08812591
+ 008fce9c bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8098120e1ce2960eb2badc886d17ca0"></a>

### [`008fceac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fceac.md) → [`008fceac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fceac.md) FUN_008fceac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fceb0",
      "incomplete_value": false,
      "site": "008fceb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fceb0",
      "incomplete_value": false,
      "site": "008fceb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "008fceb4",
      "DATA",
      [
        "storage",
        "00c08960",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fceb4",
      "DATA",
      [
        "storage",
        "00c08a10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fceb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fceac.md#insn-008fceb0)
- 新版 [`008fceb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fceac.md#insn-008fceb0)

~~~diff
- 008fceb0 ["COPY", "tmp:0:8", ["const:960:8"]]
- 008fceb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fceb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fceb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fceb0 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 008fceb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fceb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fceb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fceb0 bytes 08812591
+ 008fceb0 bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3824a4cdcb7b130c82eb8a6e28aee2a"></a>

### [`008fcf6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcf6c.md) → [`008fcf6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcf6c.md) FUN_008fcf6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fcf80",
      "incomplete_value": false,
      "site": "008fcf84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fcf80",
      "incomplete_value": false,
      "site": "008fcf84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "008fcf84",
      "DATA",
      [
        "storage",
        "00c089e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fcf84",
      "DATA",
      [
        "storage",
        "00c08a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fcf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcf6c.md#insn-008fcf80)
- 新版 [`008fcf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcf6c.md#insn-008fcf80)

~~~diff
- 008fcf80 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 008fcf80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fcf80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fcf80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fcf80 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 008fcf80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fcf80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fcf80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fcf80 bytes 08812791
+ 008fcf80 bytes 08412a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b4c43af22daec13264636f670b745e0"></a>

### [`008fcf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcf90.md) → [`008fcf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcf90.md) FUN_008fcf90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fcf94",
      "incomplete_value": false,
      "site": "008fcf98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:a90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fcf94",
      "incomplete_value": false,
      "site": "008fcf98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "008fcf98",
      "DATA",
      [
        "storage",
        "00c089e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fcf98",
      "DATA",
      [
        "storage",
        "00c08a90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fcf94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fc/008fcf90.md#insn-008fcf94)
- 新版 [`008fcf94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcf90.md#insn-008fcf94)

~~~diff
- 008fcf94 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 008fcf94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fcf94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fcf94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fcf94 ["COPY", "tmp:0:8", ["const:a90:8"]]
+ 008fcf94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fcf94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fcf94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fcf94 bytes 08812791
+ 008fcf94 bytes 08412a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b24b4044816897206fbba9a08b92a01"></a>

### [`008fd050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd050.md) → [`008fd050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd050.md) FUN_008fd050

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fd074",
      "incomplete_value": false,
      "site": "008fd074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd074",
      "incomplete_value": false,
      "site": "008fd074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "008fd074",
      "DATA",
      [
        "storage",
        "00c08a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fd074",
      "DATA",
      [
        "storage",
        "00c08b20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd050.md#insn-008fd070)
- 新版 [`008fd070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd050.md#insn-008fd070)

~~~diff
- 008fd070 ["COPY", "tmp:0:8", ["const:a70:8"]]
- 008fd070 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd070 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd070 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd070 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 008fd070 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd070 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd070 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd070 bytes 08c12991
+ 008fd070 bytes 08812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b2d77bfbb1ba0b5fa38d2e716bfa47d"></a>

### [`008fd084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd084.md) → [`008fd084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd084.md) FUN_008fd084

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fd090",
      "incomplete_value": false,
      "site": "008fd090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd090",
      "incomplete_value": false,
      "site": "008fd090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:a70:8"
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
      "008fd090",
      "DATA",
      [
        "storage",
        "00c08a70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fd090",
      "DATA",
      [
        "storage",
        "00c08b20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd084.md#insn-008fd08c)
- 新版 [`008fd08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd084.md#insn-008fd08c)

~~~diff
- 008fd08c ["COPY", "tmp:0:8", ["const:a70:8"]]
- 008fd08c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008fd08c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008fd08c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008fd08c ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 008fd08c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008fd08c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008fd08c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008fd08c bytes 29c12991
+ 008fd08c bytes 29812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76a14d7d4f906cca6ea4e7b964154f9f"></a>

### [`008fd0a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd0a0.md) → [`008fd0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd0a0.md) FUN_008fd0a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`0053d984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d984.md) [`0073e258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e258.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 17件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0053d984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d984.md) [`0073e258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e258.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fd2b8",
      "incomplete_value": false,
      "site": "008fd2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd2b8",
      "incomplete_value": false,
      "site": "008fd2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "008fd2f0",
      "incomplete_value": false,
      "site": "008fd300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd2f0",
      "incomplete_value": false,
      "site": "008fd300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008fd2c8",
      "DATA",
      [
        "storage",
        "00c08ae0",
        null,
        "undefined *"
      ]
    ],
    [
      "008fd300",
      "DATA",
      [
        "storage",
        "00c08b60",
        null,
        "undefined *"
      ]
    ],
    [
      "008fd33c",
      "READ",
      [
        "storage",
        "00c08b00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008fd2c8",
      "DATA",
      [
        "storage",
        "00c08b90",
        null,
        "undefined *"
      ]
    ],
    [
      "008fd300",
      "DATA",
      [
        "storage",
        "00c08c10",
        null,
        "undefined *"
      ]
    ],
    [
      "008fd33c",
      "READ",
      [
        "storage",
        "00c08bb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd2b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd0a0.md#insn-008fd2b8) · [`008fd2f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd0a0.md#insn-008fd2f0)
- 新版 [`008fd2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd0a0.md#insn-008fd2b8) · [`008fd2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd0a0.md#insn-008fd2f0)

~~~diff
- 008fd2b8 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 008fd2b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd2b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd2b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd2b8 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 008fd2b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd2b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd2b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd2b8 bytes 08812b91
+ 008fd2b8 bytes 08412e91
- 008fd2f0 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 008fd2f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd2f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd2f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd2f0 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 008fd2f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd2f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd2f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd2f0 bytes 08812d91
+ 008fd2f0 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5013e6bd18482cfe3ff6d0f8581d42c3"></a>

### [`008fd458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd458.md) → [`008fd458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd458.md) FUN_008fd458

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fd46c",
      "incomplete_value": false,
      "site": "008fd470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd46c",
      "incomplete_value": false,
      "site": "008fd470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "008fd470",
      "DATA",
      [
        "storage",
        "00c08ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fd470",
      "DATA",
      [
        "storage",
        "00c08b90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd458.md#insn-008fd46c)
- 新版 [`008fd46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd458.md#insn-008fd46c)

~~~diff
- 008fd46c ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 008fd46c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd46c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd46c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd46c ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 008fd46c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd46c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd46c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd46c bytes 08812b91
+ 008fd46c bytes 08412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dedea8aa41d15db5933b6a8f54b565c9"></a>

### [`008fd47c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd47c.md) → [`008fd47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd47c.md) FUN_008fd47c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fd480",
      "incomplete_value": false,
      "site": "008fd484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd480",
      "incomplete_value": false,
      "site": "008fd484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "008fd484",
      "DATA",
      [
        "storage",
        "00c08ae0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fd484",
      "DATA",
      [
        "storage",
        "00c08b90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd47c.md#insn-008fd480)
- 新版 [`008fd480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd47c.md#insn-008fd480)

~~~diff
- 008fd480 ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 008fd480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd480 ["COPY", "tmp:0:8", ["const:b90:8"]]
+ 008fd480 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd480 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd480 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd480 bytes 08812b91
+ 008fd480 bytes 08412e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37bf987e6118142209ee162a9da097dd"></a>

### [`008fd53c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd53c.md) → [`008fd53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd53c.md) FUN_008fd53c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fd550",
      "incomplete_value": false,
      "site": "008fd554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd550",
      "incomplete_value": false,
      "site": "008fd554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "008fd554",
      "DATA",
      [
        "storage",
        "00c08b60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fd554",
      "DATA",
      [
        "storage",
        "00c08c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd53c.md#insn-008fd550)
- 新版 [`008fd550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd53c.md#insn-008fd550)

~~~diff
- 008fd550 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 008fd550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd550 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 008fd550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd550 bytes 08812d91
+ 008fd550 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11f439b7af256a5a49c0b580307874a8"></a>

### [`008fd560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd560.md) → [`008fd560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd560.md) FUN_008fd560

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fd564",
      "incomplete_value": false,
      "site": "008fd568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd564",
      "incomplete_value": false,
      "site": "008fd568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:b60:8"
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
      "008fd568",
      "DATA",
      [
        "storage",
        "00c08b60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fd568",
      "DATA",
      [
        "storage",
        "00c08c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd560.md#insn-008fd564)
- 新版 [`008fd564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd560.md#insn-008fd564)

~~~diff
- 008fd564 ["COPY", "tmp:0:8", ["const:b60:8"]]
- 008fd564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd564 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 008fd564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd564 bytes 08812d91
+ 008fd564 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdb8ca96bcd99809a079574a8f0eae6f"></a>

### [`008fd620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd620.md) → [`008fd620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd620.md) FUN_008fd620

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fd634",
      "incomplete_value": false,
      "site": "008fd638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd634",
      "incomplete_value": false,
      "site": "008fd638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "008fd638",
      "DATA",
      [
        "storage",
        "00c08bf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fd638",
      "DATA",
      [
        "storage",
        "00c08ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd620.md#insn-008fd634)
- 新版 [`008fd634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd620.md#insn-008fd634)

~~~diff
- 008fd634 ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 008fd634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd634 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 008fd634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd634 bytes 08c12f91
+ 008fd634 bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-457e758a7941dd3a1d8602989ed6fe12"></a>

### [`008fd644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd644.md) → [`008fd644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd644.md) FUN_008fd644

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fd648",
      "incomplete_value": false,
      "site": "008fd64c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd648",
      "incomplete_value": false,
      "site": "008fd64c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "008fd64c",
      "DATA",
      [
        "storage",
        "00c08bf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fd64c",
      "DATA",
      [
        "storage",
        "00c08ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd644.md#insn-008fd648)
- 新版 [`008fd648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd644.md#insn-008fd648)

~~~diff
- 008fd648 ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 008fd648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd648 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 008fd648 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd648 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd648 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd648 bytes 08c12f91
+ 008fd648 bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-260e0fab3c478fe7f86a4b8de72dce72"></a>

### [`008fd65c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd65c.md) → [`008fd65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd65c.md) FUN_008fd65c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 16件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`0053d984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053d/0053d984.md) [`0073e258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e258.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0053d984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d984.md) [`0073e258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e258.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.71% / 新版 97.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fd804",
      "incomplete_value": false,
      "site": "008fd814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd804",
      "incomplete_value": false,
      "site": "008fd814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fd83c",
      "incomplete_value": false,
      "site": "008fd84c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd83c",
      "incomplete_value": false,
      "site": "008fd84c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "008fd814",
      "DATA",
      [
        "storage",
        "00c08c60",
        null,
        "undefined *"
      ]
    ],
    [
      "008fd84c",
      "DATA",
      [
        "storage",
        "00c08ce0",
        null,
        "undefined *"
      ]
    ],
    [
      "008fd888",
      "READ",
      [
        "storage",
        "00c08c80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008fd814",
      "DATA",
      [
        "storage",
        "00c08d10",
        null,
        "undefined *"
      ]
    ],
    [
      "008fd84c",
      "DATA",
      [
        "storage",
        "00c08d90",
        null,
        "undefined *"
      ]
    ],
    [
      "008fd888",
      "READ",
      [
        "storage",
        "00c08d30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd65c.md#insn-008fd804) · [`008fd83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd65c.md#insn-008fd83c)
- 新版 [`008fd804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd65c.md#insn-008fd804) · [`008fd83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd65c.md#insn-008fd83c)

~~~diff
- 008fd804 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 008fd804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd804 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 008fd804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd804 bytes 08813191
+ 008fd804 bytes 08413491
- 008fd83c ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 008fd83c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd83c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd83c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd83c ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 008fd83c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd83c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd83c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd83c bytes 08813391
+ 008fd83c bytes 08413691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12c07772abe7bc6d415cb856460aaae7"></a>

### [`008fd9a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd9a4.md) → [`008fd9a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd9a4.md) FUN_008fd9a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fd9b8",
      "incomplete_value": false,
      "site": "008fd9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd9b8",
      "incomplete_value": false,
      "site": "008fd9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "008fd9bc",
      "DATA",
      [
        "storage",
        "00c08c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fd9bc",
      "DATA",
      [
        "storage",
        "00c08d10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd9a4.md#insn-008fd9b8)
- 新版 [`008fd9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd9a4.md#insn-008fd9b8)

~~~diff
- 008fd9b8 ["COPY", "tmp:0:8", ["const:c60:8"]]
- 008fd9b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd9b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd9b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd9b8 ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 008fd9b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd9b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd9b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd9b8 bytes 08813191
+ 008fd9b8 bytes 08413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253b1b0908a57e10f80037bdaf98be0d"></a>

### [`008fd9c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd9c8.md) → [`008fd9c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd9c8.md) FUN_008fd9c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fd9cc",
      "incomplete_value": false,
      "site": "008fd9d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fd9cc",
      "incomplete_value": false,
      "site": "008fd9d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "008fd9d0",
      "DATA",
      [
        "storage",
        "00c08c60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fd9d0",
      "DATA",
      [
        "storage",
        "00c08d10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fd9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fd9c8.md#insn-008fd9cc)
- 新版 [`008fd9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fd9c8.md#insn-008fd9cc)

~~~diff
- 008fd9cc ["COPY", "tmp:0:8", ["const:c60:8"]]
- 008fd9cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fd9cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fd9cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fd9cc ["COPY", "tmp:0:8", ["const:d10:8"]]
+ 008fd9cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd9cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fd9cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fd9cc bytes 08813191
+ 008fd9cc bytes 08413491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ee74c6e0e5264b92bb3b5f3e334c838"></a>

### [`008fda88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fda88.md) → [`008fda88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fda88.md) FUN_008fda88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fda9c",
      "incomplete_value": false,
      "site": "008fdaa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fda9c",
      "incomplete_value": false,
      "site": "008fdaa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "008fdaa0",
      "DATA",
      [
        "storage",
        "00c08ce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fdaa0",
      "DATA",
      [
        "storage",
        "00c08d90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fda9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fda88.md#insn-008fda9c)
- 新版 [`008fda9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fda88.md#insn-008fda9c)

~~~diff
- 008fda9c ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 008fda9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fda9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fda9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fda9c ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 008fda9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fda9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fda9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fda9c bytes 08813391
+ 008fda9c bytes 08413691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f209dc787645a833bb493c81f95798c"></a>

### [`008fdaac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdaac.md) → [`008fdaac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdaac.md) FUN_008fdaac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fdab0",
      "incomplete_value": false,
      "site": "008fdab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fdab0",
      "incomplete_value": false,
      "site": "008fdab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "008fdab4",
      "DATA",
      [
        "storage",
        "00c08ce0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fdab4",
      "DATA",
      [
        "storage",
        "00c08d90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fdab0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdaac.md#insn-008fdab0)
- 新版 [`008fdab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdaac.md#insn-008fdab0)

~~~diff
- 008fdab0 ["COPY", "tmp:0:8", ["const:ce0:8"]]
- 008fdab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fdab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fdab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fdab0 ["COPY", "tmp:0:8", ["const:d90:8"]]
+ 008fdab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fdab0 bytes 08813391
+ 008fdab0 bytes 08413691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03d2b10c57c5f592e26dc07b69805685"></a>

### [`008fdb6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdb6c.md) → [`008fdb6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdb6c.md) FUN_008fdb6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fdb80",
      "incomplete_value": false,
      "site": "008fdb84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fdb80",
      "incomplete_value": false,
      "site": "008fdb84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "008fdb84",
      "DATA",
      [
        "storage",
        "00c08d70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fdb84",
      "DATA",
      [
        "storage",
        "00c08e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fdb80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdb6c.md#insn-008fdb80)
- 新版 [`008fdb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdb6c.md#insn-008fdb80)

~~~diff
- 008fdb80 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 008fdb80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fdb80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fdb80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fdb80 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 008fdb80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdb80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdb80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fdb80 bytes 08c13591
+ 008fdb80 bytes 08813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19c5f8c5cc91baadec376cda6cb81bb7"></a>

### [`008fdb90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdb90.md) → [`008fdb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdb90.md) FUN_008fdb90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fdb94",
      "incomplete_value": false,
      "site": "008fdb98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fdb94",
      "incomplete_value": false,
      "site": "008fdb98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "008fdb98",
      "DATA",
      [
        "storage",
        "00c08d70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fdb98",
      "DATA",
      [
        "storage",
        "00c08e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fdb94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdb90.md#insn-008fdb94)
- 新版 [`008fdb94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdb90.md#insn-008fdb94)

~~~diff
- 008fdb94 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 008fdb94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fdb94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fdb94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fdb94 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 008fdb94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdb94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdb94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fdb94 bytes 08c13591
+ 008fdb94 bytes 08813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0218dd81cc6021da6e5a16ed20b04f8d"></a>

### [`008fdd04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdd04.md) → [`008fdd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdd04.md) FUN_008fdd04

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fdd18",
      "incomplete_value": false,
      "site": "008fdd1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fdd18",
      "incomplete_value": false,
      "site": "008fdd1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "008fdd1c",
      "DATA",
      [
        "storage",
        "00c08df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fdd1c",
      "DATA",
      [
        "storage",
        "00c08ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fdd18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdd04.md#insn-008fdd18)
- 新版 [`008fdd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdd04.md#insn-008fdd18)

~~~diff
- 008fdd18 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 008fdd18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fdd18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fdd18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fdd18 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 008fdd18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdd18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdd18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fdd18 bytes 08c13791
+ 008fdd18 bytes 08813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4837dcfc5a240638670054486fc1e9aa"></a>

### [`008fdd28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdd28.md) → [`008fdd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdd28.md) FUN_008fdd28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008fdd2c",
      "incomplete_value": false,
      "site": "008fdd30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fdd2c",
      "incomplete_value": false,
      "site": "008fdd30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:df0:8"
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
      "008fdd30",
      "DATA",
      [
        "storage",
        "00c08df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fdd30",
      "DATA",
      [
        "storage",
        "00c08ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fdd2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdd28.md#insn-008fdd2c)
- 新版 [`008fdd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdd28.md#insn-008fdd2c)

~~~diff
- 008fdd2c ["COPY", "tmp:0:8", ["const:df0:8"]]
- 008fdd2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fdd2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fdd2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fdd2c ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 008fdd2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdd2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdd2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fdd2c bytes 08c13791
+ 008fdd2c bytes 08813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-909df71f18a91d6964db0ec925c1b169"></a>

### [`008fdd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdd40.md) → [`008fdd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdd40.md) FUN_008fdd40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 22件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 22件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.60% / 新版 96.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008fdf00",
      "incomplete_value": false,
      "site": "008fdf10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fdf00",
      "incomplete_value": false,
      "site": "008fdf10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "definition_site": "008fdf38",
      "incomplete_value": false,
      "site": "008fdf48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fdf38",
      "incomplete_value": false,
      "site": "008fdf48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "definition_site": "008fdffc",
      "incomplete_value": true,
      "site": "008fe010",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:272:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fdffc",
      "incomplete_value": true,
      "site": "008fe010",
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
                "const:2a4000:8"
              ],
              [
                "leaf",
                "const:279:8"
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
      "008fdf10",
      "DATA",
      [
        "storage",
        "00c08e60",
        null,
        "undefined *"
      ]
    ],
    [
      "008fdf48",
      "DATA",
      [
        "storage",
        "00c08ee0",
        null,
        "undefined *"
      ]
    ],
    [
      "008fdf84",
      "READ",
      [
        "storage",
        "00c08e80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008fdf10",
      "DATA",
      [
        "storage",
        "00c08f10",
        null,
        "undefined *"
      ]
    ],
    [
      "008fdf48",
      "DATA",
      [
        "storage",
        "00c08f90",
        null,
        "undefined *"
      ]
    ],
    [
      "008fdf84",
      "READ",
      [
        "storage",
        "00c08f30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fdf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdd40.md#insn-008fdf00) · [`008fdf38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdd40.md#insn-008fdf38) · [`008fdff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fd/008fdd40.md#insn-008fdff4)
- 新版 [`008fdf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdd40.md#insn-008fdf00) · [`008fdf38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdd40.md#insn-008fdf38) · [`008fdff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fd/008fdd40.md#insn-008fdff4)

~~~diff
- 008fdf00 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 008fdf00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fdf00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fdf00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fdf00 ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 008fdf00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdf00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdf00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fdf00 bytes 08813991
+ 008fdf00 bytes 08413c91
- 008fdf38 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 008fdf38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fdf38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fdf38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fdf38 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 008fdf38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdf38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fdf38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fdf38 bytes 08813b91
+ 008fdf38 bytes 08413e91
- 008fdff4 ["COPY", "tmp:0:8", ["const:279:8"]]
- 008fdff4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008fdff4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008fdff4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008fdff4 ["COPY", "tmp:0:8", ["const:272:8"]]
+ 008fdff4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008fdff4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008fdff4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008fdff4 bytes 29e50991
+ 008fdff4 bytes 29c90991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-446d10e2a22e061acec08f9713b094ae"></a>

### [`008fe148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe148.md) → [`008fe148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe148.md) FUN_008fe148

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "008fe15c",
      "incomplete_value": false,
      "site": "008fe160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008fe15c",
      "incomplete_value": false,
      "site": "008fe160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c08000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "008fe160",
      "DATA",
      [
        "storage",
        "00c08e60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008fe160",
      "DATA",
      [
        "storage",
        "00c08f10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008fe15c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008fe/008fe148.md#insn-008fe15c)
- 新版 [`008fe15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fe/008fe148.md#insn-008fe15c)

~~~diff
- 008fe15c ["COPY", "tmp:0:8", ["const:e60:8"]]
- 008fe15c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008fe15c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008fe15c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008fe15c ["COPY", "tmp:0:8", ["const:f10:8"]]
+ 008fe15c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe15c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008fe15c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008fe15c bytes 08813991
+ 008fe15c bytes 08413c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

