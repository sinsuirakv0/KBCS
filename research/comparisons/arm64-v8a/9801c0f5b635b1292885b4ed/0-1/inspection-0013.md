# v15.7.4 → v16.0.0 · 要調査の変更候補 (13)

[一覧の目次](README.md)

<a id="compare-5a262717aef0fc1aaf4fefc2d60a50b8"></a>

### [`00570bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570bd0.md) → [`00593a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593a68.md) FUN_00593a68

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd620.md) [`00bdd800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd800.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a070.md) [`00c5a250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a250.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00570c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570bd0.md#insn-00570c34)
- 新版 [`00593acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593a68.md#insn-00593acc)

~~~diff
- 00570c34 ["INT_ADD", "register:40f0:8", ["const:570c34:8", "const:4:8"]]
- 00570c34 ["CALL", null, ["callee:00c5a070:8"]]
+ 00593acc ["INT_ADD", "register:40f0:8", ["const:593acc:8", "const:4:8"]]
+ 00593acc ["CALL", null, ["callee:00c5a070:8"]]
- 00570c34 bytes 7bb21994
+ 00593acc bytes 69191b94
~~~


<a id="compare-0a981ef23fb9a89acfda0399cef43af6"></a>

### [`00570c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570c50.md) → [`00593ae8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593ae8.md) FUN_00593ae8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd620.md) [`00bdd810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd810.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a070.md) [`00c5a260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a260.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00570cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570c50.md#insn-00570cb8)
- 新版 [`00593b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593ae8.md#insn-00593b50)

~~~diff
- 00570cb8 ["INT_ADD", "register:40f0:8", ["const:570cb8:8", "const:4:8"]]
- 00570cb8 ["CALL", null, ["callee:00c5a070:8"]]
+ 00593b50 ["INT_ADD", "register:40f0:8", ["const:593b50:8", "const:4:8"]]
+ 00593b50 ["CALL", null, ["callee:00c5a070:8"]]
- 00570cb8 bytes 5ab21994
+ 00593b50 bytes 48191b94
~~~


<a id="compare-6c08f2320eea0bb76150ea6ebf821ade"></a>

### [`00570cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570cd8.md) → [`00593b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593b70.md) FUN_00593b70

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd620.md) [`00bdd820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd820.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a070.md) [`00c5a270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a270.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00570d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570cd8.md#insn-00570d34)
- 新版 [`00593bcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593b70.md#insn-00593bcc)

~~~diff
- 00570d34 ["INT_ADD", "register:40f0:8", ["const:570d34:8", "const:4:8"]]
- 00570d34 ["CALL", null, ["callee:00c5a070:8"]]
+ 00593bcc ["INT_ADD", "register:40f0:8", ["const:593bcc:8", "const:4:8"]]
+ 00593bcc ["CALL", null, ["callee:00c5a070:8"]]
- 00570d34 bytes 3bb21994
+ 00593bcc bytes 29191b94
~~~


<a id="compare-55f38501d2a9da7c14c62f87aae4f1fc"></a>

### [`00570d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570d50.md) → [`00593be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593be8.md) FUN_00593be8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd620.md) [`00bdd830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd830.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a070.md) [`00c5a280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a280.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00570dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/00570d50.md#insn-00570dac)
- 新版 [`00593c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593be8.md#insn-00593c44)

~~~diff
- 00570dac ["INT_ADD", "register:40f0:8", ["const:570dac:8", "const:4:8"]]
- 00570dac ["CALL", null, ["callee:00c5a070:8"]]
+ 00593c44 ["INT_ADD", "register:40f0:8", ["const:593c44:8", "const:4:8"]]
+ 00593c44 ["CALL", null, ["callee:00c5a070:8"]]
- 00570dac bytes 1db21994
+ 00593c44 bytes 0b191b94
~~~


<a id="compare-1704ceb29eaa11b74b518807067c4420"></a>

### [`00571468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571468.md) → [`00594300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md) FUN_00594300

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00571468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571468.md) [`00571a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571a08.md) · 呼出先 2件 [`00571468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571468.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00594300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md) [`005948a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/005948a0.md) · 呼出先 2件 [`00594300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00571488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571468.md#insn-00571488) · [`00571494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571468.md#insn-00571494)
- 新版 [`00594320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md#insn-00594320) · [`0059432c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594300.md#insn-0059432c)

~~~diff
- 00571488 ["INT_ADD", "register:40f0:8", ["const:571488:8", "const:4:8"]]
- 00571488 ["CALL", null, ["local:b0:8"]]
+ 00594320 ["INT_ADD", "register:40f0:8", ["const:594320:8", "const:4:8"]]
+ 00594320 ["CALL", null, ["local:b0:8"]]
- 00571488 bytes f8ffff97
+ 00594320 bytes f8ffff97
- 00571494 ["INT_ADD", "register:40f0:8", ["const:571494:8", "const:4:8"]]
- 00571494 ["CALL", null, ["local:b0:8"]]
+ 0059432c ["INT_ADD", "register:40f0:8", ["const:59432c:8", "const:4:8"]]
+ 0059432c ["CALL", null, ["local:b0:8"]]
- 00571494 bytes f5ffff97
+ 0059432c bytes f5ffff97
~~~


<a id="compare-19c20e0239ca7c2dd372cca1f6eda006"></a>

### [`005714ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005714ac.md) → [`00594344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594344.md) FUN_00594344

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005704a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005704a8.md) [`00aa7b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa7/00aa7b28.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`005715d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005715d8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00593340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593340.md) [`00b075a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b07/00b075a0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00594470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594470.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005714e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005714ac.md#insn-005714e4) · [`00571504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005714ac.md#insn-00571504) · [`00571538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005714ac.md#insn-00571538)
- 新版 [`0059437c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594344.md#insn-0059437c) · [`0059439c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594344.md#insn-0059439c) · [`005943d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594344.md#insn-005943d0)

~~~diff
- 005714e4 ["INT_ADD", "register:40f0:8", ["const:5714e4:8", "const:4:8"]]
- 005714e4 ["CALL", null, ["callee:00594470:8"]]
+ 0059437c ["INT_ADD", "register:40f0:8", ["const:59437c:8", "const:4:8"]]
+ 0059437c ["CALL", null, ["callee:00594470:8"]]
- 005714e4 bytes 3d000094
+ 0059437c bytes 3d000094
- 00571504 ["INT_ADD", "register:40f0:8", ["const:571504:8", "const:4:8"]]
- 00571504 ["CALL", null, ["callee:00c57a90:8"]]
+ 0059439c ["INT_ADD", "register:40f0:8", ["const:59439c:8", "const:4:8"]]
+ 0059439c ["CALL", null, ["callee:00c57a90:8"]]
- 00571504 bytes cfa61994
+ 0059439c bytes bd0d1b94
- 00571538 ["INT_ADD", "register:40f0:8", ["const:571538:8", "const:4:8"]]
- 00571538 ["CALL", null, ["callee:0043bae0:8"]]
+ 005943d0 ["INT_ADD", "register:40f0:8", ["const:5943d0:8", "const:4:8"]]
+ 005943d0 ["CALL", null, ["callee:0043bae0:8"]]
- 00571538 bytes aa9efa97
+ 005943d0 bytes c49dfa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5bc1c733dff9f89d2b2f1e9af697602"></a>

### [`005715d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005715d8.md) → [`00594470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594470.md) FUN_00594470

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005714ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005714ac.md) · 呼出先 2件 [`0042818c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/0042818c.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00594344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594344.md) · 呼出先 2件 [`0044ac8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044a/0044ac8c.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00571660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005715d8.md#insn-00571660) · [`005716b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005715d8.md#insn-005716b4) · [`00571750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005715d8.md#insn-00571750)
- 新版 [`005944f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594470.md#insn-005944f8) · [`0059454c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594470.md#insn-0059454c) · [`005945e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594470.md#insn-005945e8)

~~~diff
- 00571660 ["INT_ADD", "register:40f0:8", ["const:571660:8", "const:4:8"]]
- 00571660 ["CALL", null, ["callee:00c57c50:8"]]
+ 005944f8 ["INT_ADD", "register:40f0:8", ["const:5944f8:8", "const:4:8"]]
+ 005944f8 ["CALL", null, ["callee:00c57c50:8"]]
- 00571660 bytes e8a61994
+ 005944f8 bytes d60d1b94
- 005716b4 ["INT_ADD", "register:40f0:8", ["const:5716b4:8", "const:4:8"]]
- 005716b4 ["CALL", null, ["callee:00c57c50:8"]]
+ 0059454c ["INT_ADD", "register:40f0:8", ["const:59454c:8", "const:4:8"]]
+ 0059454c ["CALL", null, ["callee:00c57c50:8"]]
- 005716b4 bytes d3a61994
+ 0059454c bytes c10d1b94
- 00571750 ["INT_ADD", "register:40f0:8", ["const:571750:8", "const:4:8"]]
- 00571750 ["CALL", null, ["callee:00c57c50:8"]]
+ 005945e8 ["INT_ADD", "register:40f0:8", ["const:5945e8:8", "const:4:8"]]
+ 005945e8 ["CALL", null, ["callee:00c57c50:8"]]
- 00571750 bytes aca61994
+ 005945e8 bytes 9a0d1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d24698257e501ad7e61fb7b7278974d"></a>

### [`00571874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571874.md) → [`0059470c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/0059470c.md) FUN_0059470c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005718ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571874.md#insn-005718ac)
- 新版 [`00594744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/0059470c.md#insn-00594744)

~~~diff
- 005718ac ["INT_ADD", "register:40f0:8", ["const:5718ac:8", "const:4:8"]]
- 005718ac ["CALL", null, ["callee:00c57ab0:8"]]
+ 00594744 ["INT_ADD", "register:40f0:8", ["const:594744:8", "const:4:8"]]
+ 00594744 ["CALL", null, ["callee:00c57ab0:8"]]
- 005718ac bytes eda51994
+ 00594744 bytes db0c1b94
~~~


<a id="compare-59877fcda47c0220e8efcc705cc50891"></a>

### [`005718c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005718c4.md) → [`0059475c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/0059475c.md) FUN_0059475c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005704a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00570/005704a8.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00593340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00593/00593340.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00571930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005718c4.md#insn-00571930) · [`0057198c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/005718c4.md#insn-0057198c)
- 新版 [`005947c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/0059475c.md#insn-005947c8) · [`00594824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/0059475c.md#insn-00594824)

~~~diff
- 00571930 ["INT_ADD", "register:40f0:8", ["const:571930:8", "const:4:8"]]
- 00571930 ["CALL", null, ["callee:00c57c50:8"]]
+ 005947c8 ["INT_ADD", "register:40f0:8", ["const:5947c8:8", "const:4:8"]]
+ 005947c8 ["CALL", null, ["callee:00c57c50:8"]]
- 00571930 bytes 34a61994
+ 005947c8 bytes 220d1b94
- 0057198c ["INT_ADD", "register:40f0:8", ["const:57198c:8", "const:4:8"]]
- 0057198c ["CALL", null, ["callee:00c57c50:8"]]
+ 00594824 ["INT_ADD", "register:40f0:8", ["const:594824:8", "const:4:8"]]
+ 00594824 ["CALL", null, ["callee:00c57c50:8"]]
- 0057198c bytes 1da61994
+ 00594824 bytes 0b0d1b94
~~~


<a id="compare-df4c505992ff70008335c78c5599c44e"></a>

### [`00572150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572150.md) → [`00594fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594fe8.md) FUN_00594fe8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00565e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565e14.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00588cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588cac.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00572184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572150.md#insn-00572184) · [`005721b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572150.md#insn-005721b8)
- 新版 [`0059501c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594fe8.md#insn-0059501c) · [`00595050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594fe8.md#insn-00595050)

~~~diff
- 00572184 ["COPY", "register:0:8", ["register:4048:8"]]
- 00572184 ["INT_ADD", "register:40f0:8", ["const:572184:8", "const:4:8"]]
- 00572184 ["CALLIND", null, ["register:0:8"]]
+ 0059501c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0059501c ["INT_ADD", "register:40f0:8", ["const:59501c:8", "const:4:8"]]
+ 0059501c ["CALLIND", null, ["register:0:8"]]
- 00572184 bytes 20013fd6
+ 0059501c bytes 20013fd6
- 005721b8 ["INT_ADD", "register:40f0:8", ["const:5721b8:8", "const:4:8"]]
- 005721b8 ["CALL", null, ["callee:00588cac:8"]]
+ 00595050 ["INT_ADD", "register:40f0:8", ["const:595050:8", "const:4:8"]]
+ 00595050 ["CALL", null, ["callee:00588cac:8"]]
- 005721b8 bytes 17cfff97
+ 00595050 bytes 17cfff97
~~~


<a id="compare-de59665807ade3530c679e36e73ec5ba"></a>

### [`005722b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005722b8.md) → [`00595150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595150.md) FUN_00595150

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00571c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571c94.md) · 呼出先 2件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c668.md)
- 新版 呼出元 1件 [`00594b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594b2c.md) · 呼出先 2件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f500.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005722d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005722b8.md#insn-005722d0)
- 新版 [`00595168`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595150.md#insn-00595168)

~~~diff
- 005722d0 ["INT_ADD", "register:40f0:8", ["const:5722d0:8", "const:4:8"]]
- 005722d0 ["CALL", null, ["callee:0055f484:8"]]
+ 00595168 ["INT_ADD", "register:40f0:8", ["const:595168:8", "const:4:8"]]
+ 00595168 ["CALL", null, ["callee:0055f484:8"]]
- 005722d0 bytes c728ff97
+ 00595168 bytes c728ff97
~~~


<a id="compare-b63ddb03a50f1dfbd84930f7bd739972"></a>

### [`005722f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005722f8.md) → [`00595190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595190.md) FUN_00595190

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00571c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00571/00571c94.md) · 呼出先 2件 [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) [`0053c690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c690.md)
- 新版 呼出元 1件 [`00594b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00594/00594b2c.md) · 呼出先 2件 [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) [`0055f528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f528.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00572310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/005722f8.md#insn-00572310)
- 新版 [`005951a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595190.md#insn-005951a8)

~~~diff
- 00572310 ["INT_ADD", "register:40f0:8", ["const:572310:8", "const:4:8"]]
- 00572310 ["CALL", null, ["callee:0055f484:8"]]
+ 005951a8 ["INT_ADD", "register:40f0:8", ["const:5951a8:8", "const:4:8"]]
+ 005951a8 ["CALL", null, ["callee:0055f484:8"]]
- 00572310 bytes b728ff97
+ 005951a8 bytes b728ff97
~~~


<a id="compare-10e884126f51be4ce2e9b31cccf65796"></a>

### [`005732fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005732fc.md) → [`00596194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596194.md) FUN_00596194

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) · 呼出先 2件 [`00574358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574358.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 2件 [`005971f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971f0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00573378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005732fc.md#insn-00573378) · [`005733d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005732fc.md#insn-005733d4) · [`00573410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005732fc.md#insn-00573410)
- 新版 [`00596210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596194.md#insn-00596210) · [`0059626c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596194.md#insn-0059626c) · [`005962a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596194.md#insn-005962a8)

~~~diff
- 00573378 ["INT_ADD", "register:40f0:8", ["const:573378:8", "const:4:8"]]
- 00573378 ["CALL", null, ["callee:00c57c50:8"]]
+ 00596210 ["INT_ADD", "register:40f0:8", ["const:596210:8", "const:4:8"]]
+ 00596210 ["CALL", null, ["callee:00c57c50:8"]]
- 00573378 bytes a29f1994
+ 00596210 bytes 90061b94
- 005733d4 ["INT_ADD", "register:40f0:8", ["const:5733d4:8", "const:4:8"]]
- 005733d4 ["CALL", null, ["callee:00c57c50:8"]]
+ 0059626c ["INT_ADD", "register:40f0:8", ["const:59626c:8", "const:4:8"]]
+ 0059626c ["CALL", null, ["callee:00c57c50:8"]]
- 005733d4 bytes 8b9f1994
+ 0059626c bytes 79061b94
- 00573410 ["COPY", "register:0:8", ["register:4040:8"]]
- 00573410 ["INT_ADD", "register:40f0:8", ["const:573410:8", "const:4:8"]]
- 00573410 ["CALLIND", null, ["register:0:8"]]
+ 005962a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005962a8 ["INT_ADD", "register:40f0:8", ["const:5962a8:8", "const:4:8"]]
+ 005962a8 ["CALLIND", null, ["register:0:8"]]
- 00573410 bytes 00013fd6
+ 005962a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62a69925a6dd020adbe626158ce1cf95"></a>

### [`00573464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573464.md) → [`005962fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005962fc.md) FUN_005962fc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) · 呼出先 2件 [`00574494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574494.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`00595cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00595/00595cdc.md) · 呼出先 2件 [`0059732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059732c.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005734e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573464.md#insn-005734e0) · [`0057353c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573464.md#insn-0057353c) · [`00573578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573464.md#insn-00573578)
- 新版 [`00596378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005962fc.md#insn-00596378) · [`005963d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005962fc.md#insn-005963d4) · [`00596410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005962fc.md#insn-00596410)

~~~diff
- 005734e0 ["INT_ADD", "register:40f0:8", ["const:5734e0:8", "const:4:8"]]
- 005734e0 ["CALL", null, ["callee:00c57c50:8"]]
+ 00596378 ["INT_ADD", "register:40f0:8", ["const:596378:8", "const:4:8"]]
+ 00596378 ["CALL", null, ["callee:00c57c50:8"]]
- 005734e0 bytes 489f1994
+ 00596378 bytes 36061b94
- 0057353c ["INT_ADD", "register:40f0:8", ["const:57353c:8", "const:4:8"]]
- 0057353c ["CALL", null, ["callee:00c57c50:8"]]
+ 005963d4 ["INT_ADD", "register:40f0:8", ["const:5963d4:8", "const:4:8"]]
+ 005963d4 ["CALL", null, ["callee:00c57c50:8"]]
- 0057353c bytes 319f1994
+ 005963d4 bytes 1f061b94
- 00573578 ["COPY", "register:0:8", ["register:4040:8"]]
- 00573578 ["INT_ADD", "register:40f0:8", ["const:573578:8", "const:4:8"]]
- 00573578 ["CALLIND", null, ["register:0:8"]]
+ 00596410 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00596410 ["INT_ADD", "register:40f0:8", ["const:596410:8", "const:4:8"]]
+ 00596410 ["CALLIND", null, ["register:0:8"]]
- 00573578 bytes 00013fd6
+ 00596410 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d090b583823a2194e65e65ff7afc752"></a>

### [`00573f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573f44.md) → [`00596ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596ddc.md) FUN_00596ddc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00574144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574144.md) · 呼出先 5件 [`0052dccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dccc.md) [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00596fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596fdc.md) · 呼出先 5件 [`00550b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550b64.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00573f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573f44.md#insn-00573f6c) · [`00573f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573f44.md#insn-00573f84) · [`00573f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573f44.md#insn-00573f90)
- 新版 [`00596e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596ddc.md#insn-00596e04) · [`00596e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596ddc.md#insn-00596e1c) · [`00596e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596ddc.md#insn-00596e28)

~~~diff
- 00573f6c ["INT_ADD", "register:40f0:8", ["const:573f6c:8", "const:4:8"]]
- 00573f6c ["CALL", null, ["callee:00550b64:8"]]
+ 00596e04 ["INT_ADD", "register:40f0:8", ["const:596e04:8", "const:4:8"]]
+ 00596e04 ["CALL", null, ["callee:00550b64:8"]]
- 00573f6c bytes 58e7fe97
+ 00596e04 bytes 58e7fe97
- 00573f84 ["COPY", "register:0:8", ["register:4048:8"]]
- 00573f84 ["INT_ADD", "register:40f0:8", ["const:573f84:8", "const:4:8"]]
- 00573f84 ["CALLIND", null, ["register:0:8"]]
+ 00596e1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00596e1c ["INT_ADD", "register:40f0:8", ["const:596e1c:8", "const:4:8"]]
+ 00596e1c ["CALLIND", null, ["register:0:8"]]
- 00573f84 bytes 20013fd6
+ 00596e1c bytes 20013fd6
- 00573f90 ["INT_ADD", "register:40f0:8", ["const:573f90:8", "const:4:8"]]
- 00573f90 ["CALL", null, ["callee:00596cd0:8"]]
+ 00596e28 ["INT_ADD", "register:40f0:8", ["const:596e28:8", "const:4:8"]]
+ 00596e28 ["CALL", null, ["callee:00596cd0:8"]]
- 00573f90 bytes aaffff97
+ 00596e28 bytes aaffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6bf6d36aa1a89b833a6990699c0deb0"></a>

### [`00574358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574358.md) → [`005971f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971f0.md) FUN_005971f0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005732fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/005732fc.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004360f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004360f4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00596194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596194.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00458f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458f8c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574358.md#insn-00574398) · [`005743b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574358.md#insn-005743b8) · [`005743ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574358.md#insn-005743ec)
- 新版 [`00597230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971f0.md#insn-00597230) · [`00597250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971f0.md#insn-00597250) · [`00597284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971f0.md#insn-00597284)

~~~diff
- 00574398 ["INT_ADD", "register:40f0:8", ["const:574398:8", "const:4:8"]]
- 00574398 ["CALL", null, ["callee:00458f8c:8"]]
+ 00597230 ["INT_ADD", "register:40f0:8", ["const:597230:8", "const:4:8"]]
+ 00597230 ["CALL", null, ["callee:00458f8c:8"]]
- 00574398 bytes 5707fb97
+ 00597230 bytes 5707fb97
- 005743b8 ["INT_ADD", "register:40f0:8", ["const:5743b8:8", "const:4:8"]]
- 005743b8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00597250 ["INT_ADD", "register:40f0:8", ["const:597250:8", "const:4:8"]]
+ 00597250 ["CALL", null, ["callee:00c57a90:8"]]
- 005743b8 bytes 229b1994
+ 00597250 bytes 10021b94
- 005743ec ["INT_ADD", "register:40f0:8", ["const:5743ec:8", "const:4:8"]]
- 005743ec ["CALL", null, ["callee:0043bae0:8"]]
+ 00597284 ["INT_ADD", "register:40f0:8", ["const:597284:8", "const:4:8"]]
+ 00597284 ["CALL", null, ["callee:0043bae0:8"]]
- 005743ec bytes fd92fa97
+ 00597284 bytes 1792fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46c2645789605a4e9971b4265a72a476"></a>

### [`00574494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574494.md) → [`0059732c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059732c.md) FUN_0059732c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00573464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573464.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004360f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004360f4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005962fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/005962fc.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00458f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458f8c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005744d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574494.md#insn-005744d4) · [`005744f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574494.md#insn-005744f4) · [`00574528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574494.md#insn-00574528)
- 新版 [`0059736c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059732c.md#insn-0059736c) · [`0059738c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059732c.md#insn-0059738c) · [`005973c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059732c.md#insn-005973c0)

~~~diff
- 005744d4 ["INT_ADD", "register:40f0:8", ["const:5744d4:8", "const:4:8"]]
- 005744d4 ["CALL", null, ["callee:00458f8c:8"]]
+ 0059736c ["INT_ADD", "register:40f0:8", ["const:59736c:8", "const:4:8"]]
+ 0059736c ["CALL", null, ["callee:00458f8c:8"]]
- 005744d4 bytes 0807fb97
+ 0059736c bytes 0807fb97
- 005744f4 ["INT_ADD", "register:40f0:8", ["const:5744f4:8", "const:4:8"]]
- 005744f4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0059738c ["INT_ADD", "register:40f0:8", ["const:59738c:8", "const:4:8"]]
+ 0059738c ["CALL", null, ["callee:00c57a90:8"]]
- 005744f4 bytes d39a1994
+ 0059738c bytes c1011b94
- 00574528 ["INT_ADD", "register:40f0:8", ["const:574528:8", "const:4:8"]]
- 00574528 ["CALL", null, ["callee:0043bae0:8"]]
+ 005973c0 ["INT_ADD", "register:40f0:8", ["const:5973c0:8", "const:4:8"]]
+ 005973c0 ["CALL", null, ["callee:0043bae0:8"]]
- 00574528 bytes ae92fa97
+ 005973c0 bytes c891fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3052cc79ee862851ad8f68fb8afaac13"></a>

### [`0057462c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057462c.md) → [`005974c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md) FUN_005974c4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00575024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00575/00575024.md) [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) [`0076e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md) [`00aaebc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aae/00aaebc4.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00574344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574344.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 5件 [`005a1430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1430.md) [`0076621c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00766/0076621c.md) [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) [`00798e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00798/00798e60.md) [`00b0e654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0e/00b0e654.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005971dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005971dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005746ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057462c.md#insn-005746ac) · [`005746e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057462c.md#insn-005746e8) · [`005746fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057462c.md#insn-005746fc)
- 新版 [`00597544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md#insn-00597544) · [`00597580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md#insn-00597580) · [`00597594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005974c4.md#insn-00597594)

~~~diff
- 005746ac ["INT_ADD", "register:40f0:8", ["const:5746ac:8", "const:4:8"]]
- 005746ac ["CALL", null, ["callee:00c57a90:8"]]
+ 00597544 ["INT_ADD", "register:40f0:8", ["const:597544:8", "const:4:8"]]
+ 00597544 ["CALL", null, ["callee:00c57a90:8"]]
- 005746ac bytes 659a1994
+ 00597544 bytes 53011b94
- 005746e8 ["INT_ADD", "register:40f0:8", ["const:5746e8:8", "const:4:8"]]
- 005746e8 ["CALL", null, ["callee:00c57c00:8"]]
+ 00597580 ["INT_ADD", "register:40f0:8", ["const:597580:8", "const:4:8"]]
+ 00597580 ["CALL", null, ["callee:00c57c00:8"]]
- 005746e8 bytes b29a1994
+ 00597580 bytes a0011b94
- 005746fc ["INT_ADD", "register:40f0:8", ["const:5746fc:8", "const:4:8"]]
- 005746fc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00597594 ["INT_ADD", "register:40f0:8", ["const:597594:8", "const:4:8"]]
+ 00597594 ["CALL", null, ["callee:00c57ab0:8"]]
- 005746fc bytes 599a1994
+ 00597594 bytes 47011b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-709a8cc608952db70e6c9ec33a35a56c"></a>

### [`00574784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574784.md) → [`0059761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md) FUN_0059761c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 18件 [`0041cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cddc.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`0042f000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md) [`00456ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00456/00456ef0.md) [`00551ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551ccc.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1a0.md) [`00bdd4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4d0.md)
- 新版 呼出元 18件 [`0043f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f8dc.md) [`00450970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00450/00450970.md) [`00451e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) [`00479d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00479/00479d88.md) [`00574b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00574/00574b64.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bf0.md) [`00c59f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005747a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574784.md#insn-005747a8) · [`005747c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574784.md#insn-005747c8) · [`0057480c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574784.md#insn-0057480c)
- 新版 [`00597640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md#insn-00597640) · [`00597660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md#insn-00597660) · [`005976a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md#insn-005976a4)

~~~diff
- 005747a8 ["INT_ADD", "register:40f0:8", ["const:5747a8:8", "const:4:8"]]
- 005747a8 ["CALL", null, ["callee:00c57bf0:8"]]
+ 00597640 ["INT_ADD", "register:40f0:8", ["const:597640:8", "const:4:8"]]
+ 00597640 ["CALL", null, ["callee:00c57bf0:8"]]
- 005747a8 bytes 7e9a1994
+ 00597640 bytes 6c011b94
- 005747c8 ["INT_ADD", "register:40f0:8", ["const:5747c8:8", "const:4:8"]]
- 005747c8 ["CALL", null, ["callee:00c59f20:8"]]
+ 00597660 ["INT_ADD", "register:40f0:8", ["const:597660:8", "const:4:8"]]
+ 00597660 ["CALL", null, ["callee:00c59f20:8"]]
- 005747c8 bytes 42a31994
+ 00597660 bytes 300a1b94
- 0057480c ["INT_ADD", "register:40f0:8", ["const:57480c:8", "const:4:8"]]
- 0057480c ["CALL", null, ["callee:00c57ae0:8"]]
+ 005976a4 ["INT_ADD", "register:40f0:8", ["const:5976a4:8", "const:4:8"]]
+ 005976a4 ["CALL", null, ["callee:00c57ae0:8"]]
- 0057480c bytes 219a1994
+ 005976a4 bytes 0f011b94
~~~


<a id="compare-b11ff13c0b1aa67e5d851e174c57a281"></a>

### [`00574810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574810.md) → [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md) FUN_005976a8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 17件 [`0054e408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0054e/0054e408.md) [`0055664c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00556/0055664c.md) [`00606588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/00606588.md) [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb60.md) [`00bdd4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4d0.md)
- 新版 呼出元 17件 [`005712a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00571/005712a0.md) [`005794e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00579/005794e4.md) [`0062c080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062c/0062c080.md) [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c585b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c585b0.md) [`00c59f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574810.md#insn-00574850) · [`00574858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574810.md#insn-00574858) · [`0057489c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574810.md#insn-0057489c)
- 新版 [`005976e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md#insn-005976e8) · [`005976f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md#insn-005976f0) · [`00597734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md#insn-00597734)

~~~diff
- 00574850 ["INT_ADD", "register:40f0:8", ["const:574850:8", "const:4:8"]]
- 00574850 ["CALL", null, ["callee:00c585b0:8"]]
+ 005976e8 ["INT_ADD", "register:40f0:8", ["const:5976e8:8", "const:4:8"]]
+ 005976e8 ["CALL", null, ["callee:00c585b0:8"]]
- 00574850 bytes c49c1994
+ 005976e8 bytes b2031b94
- 00574858 ["INT_ADD", "register:40f0:8", ["const:574858:8", "const:4:8"]]
- 00574858 ["CALL", null, ["callee:00c59f20:8"]]
+ 005976f0 ["INT_ADD", "register:40f0:8", ["const:5976f0:8", "const:4:8"]]
+ 005976f0 ["CALL", null, ["callee:00c59f20:8"]]
- 00574858 bytes 1ea31994
+ 005976f0 bytes 0c0a1b94
- 0057489c ["INT_ADD", "register:40f0:8", ["const:57489c:8", "const:4:8"]]
- 0057489c ["CALL", null, ["callee:00c57ae0:8"]]
+ 00597734 ["INT_ADD", "register:40f0:8", ["const:597734:8", "const:4:8"]]
+ 00597734 ["CALL", null, ["callee:00c57ae0:8"]]
- 0057489c bytes fd991994
+ 00597734 bytes eb001b94
~~~


<a id="compare-4859b23621f6be5429a0ca15b0514979"></a>

### [`005748a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005748a0.md) → [`00597738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597738.md) FUN_00597738

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 20件 [`0045da24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045da24.md) [`00606588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/00606588.md) [`006118e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00611/006118e8.md) [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) · 呼出先 1件 [`00bdd4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4e0.md)
- 新版 呼出元 20件 [`004808bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004808bc.md) [`0062c080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062c/0062c080.md) [`006373e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00637/006373e0.md) [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 1件 [`00c59f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005748d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005748a0.md#insn-005748d0)
- 新版 [`00597768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597738.md#insn-00597768)

~~~diff
- 005748d0 ["INT_ADD", "register:40f0:8", ["const:5748d0:8", "const:4:8"]]
- 005748d0 ["CALL", null, ["callee:00c59f30:8"]]
+ 00597768 ["INT_ADD", "register:40f0:8", ["const:597768:8", "const:4:8"]]
+ 00597768 ["CALL", null, ["callee:00c59f30:8"]]
- 005748d0 bytes 04a31994
+ 00597768 bytes f2091b94
~~~


<a id="compare-3c83a67d271c91efdde86272e81c3beb"></a>

### [`00574f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f30.md) → [`00597dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597dc8.md) FUN_00597dc8

採用 · 移動量 `+0x22e98` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`004537f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md) [`00734374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/00734374.md) [`008a2cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a2cac.md) [`008b07b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b07b8.md) [`00acfb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acfb2c.md) · 呼出先 2件 [`00bdd4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4e0.md) [`00bdd4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4f0.md)
- 新版 呼出元 5件 [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`0075e548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075e548.md) [`008d6b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md) [`008e465c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e4/008e465c.md) [`00b2f5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2f/00b2f5e4.md) · 呼出先 2件 [`00c59f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f30.md) [`00c59f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f30.md#insn-00574f40) · [`00574f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f30.md#insn-00574f4c)
- 新版 [`00597dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597dc8.md#insn-00597dd8) · [`00597de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597dc8.md#insn-00597de4)

~~~diff
- 00574f40 ["INT_ADD", "register:40f0:8", ["const:574f40:8", "const:4:8"]]
- 00574f40 ["CALL", null, ["callee:00c59f30:8"]]
+ 00597dd8 ["INT_ADD", "register:40f0:8", ["const:597dd8:8", "const:4:8"]]
+ 00597dd8 ["CALL", null, ["callee:00c59f30:8"]]
- 00574f40 bytes 68a11994
+ 00597dd8 bytes 56081b94
- 00574f4c ["INT_ADD", "register:40f0:8", ["const:574f4c:8", "const:4:8"]]
- 00574f4c ["CALL", null, ["callee:00c59f40:8"]]
+ 00597de4 ["INT_ADD", "register:40f0:8", ["const:597de4:8", "const:4:8"]]
+ 00597de4 ["CALL", null, ["callee:00c59f40:8"]]
- 00574f4c bytes 69a11994
+ 00597de4 bytes 57081b94
~~~


<a id="compare-da50231ad5dc6bbc2b1be5b21741c3f1"></a>

### [`00574f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f70.md) → [`00597e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md) FUN_00597e08

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 14件 [`004537f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00453/004537f0.md) [`00776a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/00776a8c.md) [`00776bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00776/00776bfc.md) [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1a0.md) [`00bdd4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4d0.md)
- 新版 呼出元 16件 [`00476688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00476/00476688.md) [`007a0f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a0/007a0f60.md) [`007a10d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007a1/007a10d0.md) [`007abbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ab/007abbe4.md) [`007aca8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007ac/007aca8c.md) · 呼出先 3件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bf0.md) [`00c59f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00574f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f70.md#insn-00574f94) · [`00574fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f70.md#insn-00574fb4) · [`00574fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f70.md#insn-00574fe0)
- 新版 [`00597e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md#insn-00597e2c) · [`00597e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md#insn-00597e4c) · [`00597e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md#insn-00597e78)

~~~diff
- 00574f94 ["INT_ADD", "register:40f0:8", ["const:574f94:8", "const:4:8"]]
- 00574f94 ["CALL", null, ["callee:00c57bf0:8"]]
+ 00597e2c ["INT_ADD", "register:40f0:8", ["const:597e2c:8", "const:4:8"]]
+ 00597e2c ["CALL", null, ["callee:00c57bf0:8"]]
- 00574f94 bytes 83981994
+ 00597e2c bytes 71ff1a94
- 00574fb4 ["INT_ADD", "register:40f0:8", ["const:574fb4:8", "const:4:8"]]
- 00574fb4 ["CALL", null, ["callee:00c59f20:8"]]
+ 00597e4c ["INT_ADD", "register:40f0:8", ["const:597e4c:8", "const:4:8"]]
+ 00597e4c ["CALL", null, ["callee:00c59f20:8"]]
- 00574fb4 bytes 47a11994
+ 00597e4c bytes 35081b94
- 00574fe0 ["INT_ADD", "register:40f0:8", ["const:574fe0:8", "const:4:8"]]
- 00574fe0 ["CALL", null, ["callee:00c57ae0:8"]]
+ 00597e78 ["INT_ADD", "register:40f0:8", ["const:597e78:8", "const:4:8"]]
+ 00597e78 ["CALL", null, ["callee:00c57ae0:8"]]
- 00574fe0 bytes 2c981994
+ 00597e78 bytes 1aff1a94
~~~


<a id="compare-8555a24b338c0ed416b4174a39fc1436"></a>

### [`00576800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576800.md) → [`0059918c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059918c.md) FUN_0059918c

採用 · 移動量 `+0x2298c` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005891dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/005891dc.md) [`0058a2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a2e0.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576800.md#insn-0057681c) · [`0057683c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576800.md#insn-0057683c)
- 新版 [`005991a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059918c.md#insn-005991a8) · [`005991c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/0059918c.md#insn-005991c8)

~~~diff
- 0057681c ["INT_ADD", "register:40f0:8", ["const:57681c:8", "const:4:8"]]
- 0057681c ["CALL", null, ["callee:00c538e0:8"]]
+ 005991a8 ["INT_ADD", "register:40f0:8", ["const:5991a8:8", "const:4:8"]]
+ 005991a8 ["CALL", null, ["callee:00c538e0:8"]]
- 0057681c bytes 9d811994
+ 005991a8 bytes cee91a94
- 0057683c ["COPY", "register:0:8", ["register:4040:8"]]
- 0057683c ["INT_ADD", "register:40f0:8", ["const:57683c:8", "const:4:8"]]
- 0057683c ["CALLIND", null, ["register:0:8"]]
+ 005991c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005991c8 ["INT_ADD", "register:40f0:8", ["const:5991c8:8", "const:4:8"]]
+ 005991c8 ["CALLIND", null, ["register:0:8"]]
- 0057683c bytes 00013fd6
+ 005991c8 bytes 00013fd6
~~~


<a id="compare-0ef85d89ce4e432b03476bf5ad87c3a9"></a>

### [`00576d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d38.md) → [`00599610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599610.md) FUN_00599610

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00576d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d38.md#insn-00576d54) · [`00576d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d38.md#insn-00576d68) · [`00576d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576d38.md#insn-00576d88)
- 新版 [`0059962c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599610.md#insn-0059962c) · [`00599640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599610.md#insn-00599640) · [`00599660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599610.md#insn-00599660)

~~~diff
- 00576d54 ["INT_ADD", "register:40f0:8", ["const:576d54:8", "const:4:8"]]
- 00576d54 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0059962c ["INT_ADD", "register:40f0:8", ["const:59962c:8", "const:4:8"]]
+ 0059962c ["CALL", null, ["callee:00c57ab0:8"]]
- 00576d54 bytes c3901994
+ 0059962c bytes 21f91a94
- 00576d68 ["INT_ADD", "register:40f0:8", ["const:576d68:8", "const:4:8"]]
- 00576d68 ["CALL", null, ["callee:00c538e0:8"]]
+ 00599640 ["INT_ADD", "register:40f0:8", ["const:599640:8", "const:4:8"]]
+ 00599640 ["CALL", null, ["callee:00c538e0:8"]]
- 00576d68 bytes 4a801994
+ 00599640 bytes a8e81a94
- 00576d88 ["COPY", "register:0:8", ["register:4040:8"]]
- 00576d88 ["INT_ADD", "register:40f0:8", ["const:576d88:8", "const:4:8"]]
- 00576d88 ["CALLIND", null, ["register:0:8"]]
+ 00599660 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599660 ["INT_ADD", "register:40f0:8", ["const:599660:8", "const:4:8"]]
+ 00599660 ["CALLIND", null, ["register:0:8"]]
- 00576d88 bytes 00013fd6
+ 00599660 bytes 00013fd6
~~~


<a id="compare-d463c951e3612aa3bdad1742915f85e7"></a>

### [`0057749c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057749c.md) → [`00599d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599d74.md) FUN_00599d74

採用 · 移動量 `+0x228d8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005891dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/005891dc.md) [`0058a2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a2e0.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`005ad7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ad/005ad7a0.md) [`005ae8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae8a4.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005774b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057749c.md#insn-005774b8) · [`005774d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/0057749c.md#insn-005774d8)
- 新版 [`00599d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599d74.md#insn-00599d90) · [`00599db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00599/00599d74.md#insn-00599db0)

~~~diff
- 005774b8 ["INT_ADD", "register:40f0:8", ["const:5774b8:8", "const:4:8"]]
- 005774b8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00599d90 ["INT_ADD", "register:40f0:8", ["const:599d90:8", "const:4:8"]]
+ 00599d90 ["CALL", null, ["callee:00c538e0:8"]]
- 005774b8 bytes 767e1994
+ 00599d90 bytes d4e61a94
- 005774d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005774d8 ["INT_ADD", "register:40f0:8", ["const:5774d8:8", "const:4:8"]]
- 005774d8 ["CALLIND", null, ["register:0:8"]]
+ 00599db0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00599db0 ["INT_ADD", "register:40f0:8", ["const:599db0:8", "const:4:8"]]
+ 00599db0 ["CALLIND", null, ["register:0:8"]]
- 005774d8 bytes 00013fd6
+ 00599db0 bytes 00013fd6
~~~


<a id="compare-2ca90471bb209715d6f82bebdfc93c77"></a>

### [`00577868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577868.md) → [`0059a140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a140.md) FUN_0059a140

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00577884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577868.md#insn-00577884)
- 新版 [`0059a15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a140.md#insn-0059a15c)

~~~diff
- 00577884 ["INT_ADD", "register:40f0:8", ["const:577884:8", "const:4:8"]]
- 00577884 ["CALL", null, ["callee:00459d34:8"]]
+ 0059a15c ["INT_ADD", "register:40f0:8", ["const:59a15c:8", "const:4:8"]]
+ 0059a15c ["CALL", null, ["callee:00459d34:8"]]
- 00577884 bytes 86fdfa97
+ 0059a15c bytes f6fefa97
~~~


<a id="compare-6d941962d8d2f8ab4026af8b6248ced4"></a>

### [`00577d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577d74.md) → [`0059a64c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a64c.md) FUN_0059a64c

採用 · 移動量 `+0x228d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00577d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00577/00577d74.md#insn-00577d90)
- 新版 [`0059a668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0059a/0059a64c.md#insn-0059a668)

~~~diff
- 00577d90 ["INT_ADD", "register:40f0:8", ["const:577d90:8", "const:4:8"]]
- 00577d90 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0059a668 ["INT_ADD", "register:40f0:8", ["const:59a668:8", "const:4:8"]]
+ 0059a668 ["CALL", null, ["callee:00c57ab0:8"]]
- 00577d90 bytes b48c1994
+ 0059a668 bytes 12f51a94
~~~


<a id="compare-da14ce12bb2644278f25658f830a5090"></a>

### [`0057f054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f054.md) → [`005a1794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1794.md) FUN_005a1794

採用 · 移動量 `+0x22740` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0057efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057e/0057efa8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a16e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a16e8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0057f064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0057f/0057f054.md#insn-0057f064)
- 新版 [`005a17a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a1/005a1794.md#insn-005a17a4)

~~~diff
- 0057f064 ["INT_ADD", "register:40f0:8", ["const:57f064:8", "const:4:8"]]
- 0057f064 ["CALL", null, ["callee:005a16e8:8"]]
+ 005a17a4 ["INT_ADD", "register:40f0:8", ["const:5a17a4:8", "const:4:8"]]
+ 005a17a4 ["CALL", null, ["callee:005a16e8:8"]]
- 0057f064 bytes d1ffff97
+ 005a17a4 bytes d1ffff97
~~~


<a id="compare-3a2313988093cf73590df899b8350eae"></a>

### [`00581b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581b00.md) → [`005a4240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4240.md) FUN_005a4240

採用 · 移動量 `+0x22740` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`007726fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00772/007726fc.md) · 呼出先 1件 [`00581cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581cec.md)
- 新版 呼出元 1件 [`0079cbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0079c/0079cbd0.md) · 呼出先 1件 [`005a442c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a442c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00581b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00581/00581b00.md#insn-00581b10)
- 新版 [`005a4250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a4/005a4240.md#insn-005a4250)

~~~diff
- 00581b10 ["INT_ADD", "register:40f0:8", ["const:581b10:8", "const:4:8"]]
- 00581b10 ["CALL", null, ["callee:005a442c:8"]]
+ 005a4250 ["INT_ADD", "register:40f0:8", ["const:5a4250:8", "const:4:8"]]
+ 005a4250 ["CALL", null, ["callee:005a442c:8"]]
- 00581b10 bytes 77000094
+ 005a4250 bytes 77000094
~~~


<a id="compare-96e8159c11942e4b87cbbfff8503a8c4"></a>

### [`00583434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583434.md) → [`005a7c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7c0c.md) FUN_005a7c0c

採用 · 移動量 `+0x247d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00583484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00583/00583434.md#insn-00583484)
- 新版 [`005a7c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a7/005a7c0c.md#insn-005a7c5c)

~~~diff
- 00583484 ["INT_ADD", "register:40f0:8", ["const:583484:8", "const:4:8"]]
- 00583484 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005a7c5c ["INT_ADD", "register:40f0:8", ["const:5a7c5c:8", "const:4:8"]]
+ 005a7c5c ["CALL", null, ["callee:00c57ab0:8"]]
- 00583484 bytes f75e1994
+ 005a7c5c bytes 95bf1a94
~~~


<a id="compare-edb26656ea8fcf6f0cc73ea1f71864db"></a>

### [`005856cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005856cc.md) → [`005a9e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9e24.md) FUN_005a9e24

採用 · 移動量 `+0x24758` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0058558c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/0058558c.md) · 呼出先 2件 [`005859ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005859ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005a9ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9ce4.md) · 呼出先 2件 [`005aa144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005aa/005aa144.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00585720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005856cc.md#insn-00585720)
- 新版 [`005a9e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005a9/005a9e24.md#insn-005a9e78)

~~~diff
- 00585720 ["INT_ADD", "register:40f0:8", ["const:585720:8", "const:4:8"]]
- 00585720 ["CALL", null, ["callee:005aa144:8"]]
+ 005a9e78 ["INT_ADD", "register:40f0:8", ["const:5a9e78:8", "const:4:8"]]
+ 005a9e78 ["CALL", null, ["callee:005aa144:8"]]
- 00585720 bytes b3000094
+ 005a9e78 bytes b3000094
~~~


<a id="compare-f440aed011f7b12eb729cb549bac3c6e"></a>

### [`0058a21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a21c.md) → [`005ae7e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae7e0.md) FUN_005ae7e0

採用 · 移動量 `+0x245c4` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0058a238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a21c.md#insn-0058a238) · [`0058a24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a21c.md#insn-0058a24c) · [`0058a26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058a/0058a21c.md#insn-0058a26c)
- 新版 [`005ae7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae7e0.md#insn-005ae7fc) · [`005ae810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae7e0.md#insn-005ae810) · [`005ae830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae7e0.md#insn-005ae830)

~~~diff
- 0058a238 ["INT_ADD", "register:40f0:8", ["const:58a238:8", "const:4:8"]]
- 0058a238 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005ae7fc ["INT_ADD", "register:40f0:8", ["const:5ae7fc:8", "const:4:8"]]
+ 005ae7fc ["CALL", null, ["callee:00c57ab0:8"]]
- 0058a238 bytes 8a431994
+ 005ae7fc bytes ada41a94
- 0058a24c ["INT_ADD", "register:40f0:8", ["const:58a24c:8", "const:4:8"]]
- 0058a24c ["CALL", null, ["callee:00c538e0:8"]]
+ 005ae810 ["INT_ADD", "register:40f0:8", ["const:5ae810:8", "const:4:8"]]
+ 005ae810 ["CALL", null, ["callee:00c538e0:8"]]
- 0058a24c bytes 11331994
+ 005ae810 bytes 34941a94
- 0058a26c ["COPY", "register:0:8", ["register:4040:8"]]
- 0058a26c ["INT_ADD", "register:40f0:8", ["const:58a26c:8", "const:4:8"]]
- 0058a26c ["CALLIND", null, ["register:0:8"]]
+ 005ae830 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ae830 ["INT_ADD", "register:40f0:8", ["const:5ae830:8", "const:4:8"]]
+ 005ae830 ["CALLIND", null, ["register:0:8"]]
- 0058a26c bytes 00013fd6
+ 005ae830 bytes 00013fd6
~~~


<a id="compare-42a0b58fbdbd5aca6c75d95a989be24b"></a>

### [`00590bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590bb0.md) → [`005b51e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md) FUN_005b51e0

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0058cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cd38.md) [`0058cdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cdd0.md) [`00590bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590bb0.md) · 呼出先 2件 [`00590bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590bb0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`005b1368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1368.md) [`005b1400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1400.md) [`005b51e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md) · 呼出先 2件 [`005b51e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00590bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590bb0.md#insn-00590bcc) · [`00590bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590bb0.md#insn-00590bd8) · [`00590c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590bb0.md#insn-00590c0c)
- 新版 [`005b51fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md#insn-005b51fc) · [`005b5208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md#insn-005b5208) · [`005b523c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b51e0.md#insn-005b523c)

~~~diff
- 00590bcc ["INT_ADD", "register:40f0:8", ["const:590bcc:8", "const:4:8"]]
- 00590bcc ["CALL", null, ["local:b0:8"]]
+ 005b51fc ["INT_ADD", "register:40f0:8", ["const:5b51fc:8", "const:4:8"]]
+ 005b51fc ["CALL", null, ["local:b0:8"]]
- 00590bcc bytes f9ffff97
+ 005b51fc bytes f9ffff97
- 00590bd8 ["INT_ADD", "register:40f0:8", ["const:590bd8:8", "const:4:8"]]
- 00590bd8 ["CALL", null, ["local:b0:8"]]
+ 005b5208 ["INT_ADD", "register:40f0:8", ["const:5b5208:8", "const:4:8"]]
+ 005b5208 ["CALL", null, ["local:b0:8"]]
- 00590bd8 bytes f6ffff97
+ 005b5208 bytes f6ffff97
- 00590c0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00590c0c ["INT_ADD", "register:40f0:8", ["const:590c0c:8", "const:4:8"]]
- 00590c0c ["CALLIND", null, ["register:0:8"]]
+ 005b523c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b523c ["INT_ADD", "register:40f0:8", ["const:5b523c:8", "const:4:8"]]
+ 005b523c ["CALLIND", null, ["register:0:8"]]
- 00590c0c bytes 00013fd6
+ 005b523c bytes 00013fd6
~~~


<a id="compare-e2418d65c76e9db24b24d1c4cf5ecd5f"></a>

### [`00590c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590c20.md) → [`005b5250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md) FUN_005b5250

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0058cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cd38.md) [`0058cdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058cdd0.md) [`00590c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590c20.md) · 呼出先 2件 [`00590c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590c20.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`005b1368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1368.md) [`005b1400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b1400.md) [`005b5250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md) · 呼出先 2件 [`005b5250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00590c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590c20.md#insn-00590c3c) · [`00590c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590c20.md#insn-00590c48) · [`00590c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00590/00590c20.md#insn-00590c7c)
- 新版 [`005b526c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md#insn-005b526c) · [`005b5278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md#insn-005b5278) · [`005b52ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b5250.md#insn-005b52ac)

~~~diff
- 00590c3c ["INT_ADD", "register:40f0:8", ["const:590c3c:8", "const:4:8"]]
- 00590c3c ["CALL", null, ["local:b0:8"]]
+ 005b526c ["INT_ADD", "register:40f0:8", ["const:5b526c:8", "const:4:8"]]
+ 005b526c ["CALL", null, ["local:b0:8"]]
- 00590c3c bytes f9ffff97
+ 005b526c bytes f9ffff97
- 00590c48 ["INT_ADD", "register:40f0:8", ["const:590c48:8", "const:4:8"]]
- 00590c48 ["CALL", null, ["local:b0:8"]]
+ 005b5278 ["INT_ADD", "register:40f0:8", ["const:5b5278:8", "const:4:8"]]
+ 005b5278 ["CALL", null, ["local:b0:8"]]
- 00590c48 bytes f6ffff97
+ 005b5278 bytes f6ffff97
- 00590c7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00590c7c ["INT_ADD", "register:40f0:8", ["const:590c7c:8", "const:4:8"]]
- 00590c7c ["CALLIND", null, ["register:0:8"]]
+ 005b52ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b52ac ["INT_ADD", "register:40f0:8", ["const:5b52ac:8", "const:4:8"]]
+ 005b52ac ["CALLIND", null, ["register:0:8"]]
- 00590c7c bytes 00013fd6
+ 005b52ac bytes 00013fd6
~~~


<a id="compare-2432638082b4e61f98b147c1c08b56e6"></a>

### [`00591374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591374.md) → [`005b59a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b59a4.md) FUN_005b59a4

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00591390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591374.md#insn-00591390) · [`005913b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00591/00591374.md#insn-005913b0)
- 新版 [`005b59c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b59a4.md#insn-005b59c0) · [`005b59e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b5/005b59a4.md#insn-005b59e0)

~~~diff
- 00591390 ["INT_ADD", "register:40f0:8", ["const:591390:8", "const:4:8"]]
- 00591390 ["CALL", null, ["callee:00c538e0:8"]]
+ 005b59c0 ["INT_ADD", "register:40f0:8", ["const:5b59c0:8", "const:4:8"]]
+ 005b59c0 ["CALL", null, ["callee:00c538e0:8"]]
- 00591390 bytes c0161994
+ 005b59c0 bytes c8771a94
- 005913b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005913b0 ["INT_ADD", "register:40f0:8", ["const:5913b0:8", "const:4:8"]]
- 005913b0 ["CALLIND", null, ["register:0:8"]]
+ 005b59e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b59e0 ["INT_ADD", "register:40f0:8", ["const:5b59e0:8", "const:4:8"]]
+ 005b59e0 ["CALLIND", null, ["register:0:8"]]
- 005913b0 bytes 00013fd6
+ 005b59e0 bytes 00013fd6
~~~


<a id="compare-bf54629c9fd3275be89f0ec8dfed2d70"></a>

### [`00592eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592eb0.md) → [`005b74e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b74e0.md) FUN_005b74e0

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058f504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058f504.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005b3b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3b34.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00592eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592eb0.md#insn-00592eec)
- 新版 [`005b751c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b74e0.md#insn-005b751c)

~~~diff
- 00592eec ["COPY", "register:0:8", ["register:4040:8"]]
- 00592eec ["INT_ADD", "register:40f0:8", ["const:592eec:8", "const:4:8"]]
- 00592eec ["CALLIND", null, ["register:0:8"]]
+ 005b751c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b751c ["INT_ADD", "register:40f0:8", ["const:5b751c:8", "const:4:8"]]
+ 005b751c ["CALLIND", null, ["register:0:8"]]
- 00592eec bytes 00013fd6
+ 005b751c bytes 00013fd6
~~~


<a id="compare-bbe4de52c2a920f4bf2196bd5d01b00e"></a>

### [`00593638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593638.md) → [`005b7c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7c68.md) FUN_005b7c68

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00593654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593638.md#insn-00593654) · [`00593674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593638.md#insn-00593674)
- 新版 [`005b7c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7c68.md#insn-005b7c84) · [`005b7ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b7/005b7c68.md#insn-005b7ca4)

~~~diff
- 00593654 ["INT_ADD", "register:40f0:8", ["const:593654:8", "const:4:8"]]
- 00593654 ["CALL", null, ["callee:00c538e0:8"]]
+ 005b7c84 ["INT_ADD", "register:40f0:8", ["const:5b7c84:8", "const:4:8"]]
+ 005b7c84 ["CALL", null, ["callee:00c538e0:8"]]
- 00593654 bytes 0f0e1994
+ 005b7c84 bytes 176f1a94
- 00593674 ["COPY", "register:0:8", ["register:4040:8"]]
- 00593674 ["INT_ADD", "register:40f0:8", ["const:593674:8", "const:4:8"]]
- 00593674 ["CALLIND", null, ["register:0:8"]]
+ 005b7ca4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b7ca4 ["INT_ADD", "register:40f0:8", ["const:5b7ca4:8", "const:4:8"]]
+ 005b7ca4 ["CALLIND", null, ["register:0:8"]]
- 00593674 bytes 00013fd6
+ 005b7ca4 bytes 00013fd6
~~~


<a id="compare-341f981e68bee9c48ba4ef9e21bb49b3"></a>

### [`00593a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593a24.md) → [`005b8054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8054.md) FUN_005b8054

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00593a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00593/00593a24.md#insn-00593a40)
- 新版 [`005b8070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8054.md#insn-005b8070)

~~~diff
- 00593a40 ["INT_ADD", "register:40f0:8", ["const:593a40:8", "const:4:8"]]
- 00593a40 ["CALL", null, ["callee:00459d34:8"]]
+ 005b8070 ["INT_ADD", "register:40f0:8", ["const:5b8070:8", "const:4:8"]]
+ 005b8070 ["CALL", null, ["callee:00459d34:8"]]
- 00593a40 bytes 178dfa97
+ 005b8070 bytes 3187fa97
~~~


<a id="compare-2b88f1e579c26d414189959fc400417e"></a>

### [`0059419c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/0059419c.md) → [`005b87cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b87cc.md) FUN_005b87cc

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0058f9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058f/0058f9b0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005b3fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b3/005b3fe0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005941d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/0059419c.md#insn-005941d8)
- 新版 [`005b8808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b87cc.md#insn-005b8808)

~~~diff
- 005941d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 005941d8 ["INT_ADD", "register:40f0:8", ["const:5941d8:8", "const:4:8"]]
- 005941d8 ["CALLIND", null, ["register:0:8"]]
+ 005b8808 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8808 ["INT_ADD", "register:40f0:8", ["const:5b8808:8", "const:4:8"]]
+ 005b8808 ["CALLIND", null, ["register:0:8"]]
- 005941d8 bytes 00013fd6
+ 005b8808 bytes 00013fd6
~~~


<a id="compare-c1e03b68e1d2e375ca237f3949c17dc0"></a>

### [`005948f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005948f4.md) → [`005b8f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8f24.md) FUN_005b8f24

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00594910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005948f4.md#insn-00594910) · [`00594930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/005948f4.md#insn-00594930)
- 新版 [`005b8f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8f24.md#insn-005b8f40) · [`005b8f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b8/005b8f24.md#insn-005b8f60)

~~~diff
- 00594910 ["INT_ADD", "register:40f0:8", ["const:594910:8", "const:4:8"]]
- 00594910 ["CALL", null, ["callee:00c538e0:8"]]
+ 005b8f40 ["INT_ADD", "register:40f0:8", ["const:5b8f40:8", "const:4:8"]]
+ 005b8f40 ["CALL", null, ["callee:00c538e0:8"]]
- 00594910 bytes 60091994
+ 005b8f40 bytes 686a1a94
- 00594930 ["COPY", "register:0:8", ["register:4040:8"]]
- 00594930 ["INT_ADD", "register:40f0:8", ["const:594930:8", "const:4:8"]]
- 00594930 ["CALLIND", null, ["register:0:8"]]
+ 005b8f60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005b8f60 ["INT_ADD", "register:40f0:8", ["const:5b8f60:8", "const:4:8"]]
+ 005b8f60 ["CALLIND", null, ["register:0:8"]]
- 00594930 bytes 00013fd6
+ 005b8f60 bytes 00013fd6
~~~


<a id="compare-11501e0ffdb229f4901b1ade6ccb413a"></a>

### [`00594ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594ce0.md) → [`005b9310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9310.md) FUN_005b9310

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00594cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00594/00594ce0.md#insn-00594cfc)
- 新版 [`005b932c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b9310.md#insn-005b932c)

~~~diff
- 00594cfc ["INT_ADD", "register:40f0:8", ["const:594cfc:8", "const:4:8"]]
- 00594cfc ["CALL", null, ["callee:00459d34:8"]]
+ 005b932c ["INT_ADD", "register:40f0:8", ["const:5b932c:8", "const:4:8"]]
+ 005b932c ["CALL", null, ["callee:00459d34:8"]]
- 00594cfc bytes 6888fa97
+ 005b932c bytes 8282fa97
~~~


<a id="compare-6e736921d107c2ac257627c1c9ee743d"></a>

### [`0059539c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/0059539c.md) → [`005b99cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b99cc.md) FUN_005b99cc

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 3件 [`0045de70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045de70.md) [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md) [`0045e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045e1c0.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 3件 [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md) [`00481058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481058.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005953bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/0059539c.md#insn-005953bc) · [`005953c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00595/0059539c.md#insn-005953c8)
- 新版 [`005b99ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b99cc.md#insn-005b99ec) · [`005b99f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b9/005b99cc.md#insn-005b99f8)

~~~diff
- 005953bc ["INT_ADD", "register:40f0:8", ["const:5953bc:8", "const:4:8"]]
- 005953bc ["CALL", null, ["callee:00480d08:8"]]
+ 005b99ec ["INT_ADD", "register:40f0:8", ["const:5b99ec:8", "const:4:8"]]
+ 005b99ec ["CALL", null, ["callee:00480d08:8"]]
- 005953bc bytes ad22fb97
+ 005b99ec bytes c71cfb97
- 005953c8 ["INT_ADD", "register:40f0:8", ["const:5953c8:8", "const:4:8"]]
- 005953c8 ["CALL", null, ["callee:00480de8:8"]]
+ 005b99f8 ["INT_ADD", "register:40f0:8", ["const:5b99f8:8", "const:4:8"]]
+ 005b99f8 ["CALL", null, ["callee:00480de8:8"]]
- 005953c8 bytes e222fb97
+ 005b99f8 bytes fc1cfb97
~~~


<a id="compare-eab6503440db404e29c36bfc44e025f9"></a>

### [`00596098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596098.md) → [`005ba6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba6c8.md) FUN_005ba6c8

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005960b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596098.md#insn-005960b8) · [`005960d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596098.md#insn-005960d0) · [`005960f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596098.md#insn-005960f0)
- 新版 [`005ba6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba6c8.md#insn-005ba6e8) · [`005ba700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba6c8.md#insn-005ba700) · [`005ba720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba6c8.md#insn-005ba720)

~~~diff
- 005960b8 ["INT_ADD", "register:40f0:8", ["const:5960b8:8", "const:4:8"]]
- 005960b8 ["CALL", null, ["callee:00c538e0:8"]]
+ 005ba6e8 ["INT_ADD", "register:40f0:8", ["const:5ba6e8:8", "const:4:8"]]
+ 005ba6e8 ["CALL", null, ["callee:00c538e0:8"]]
- 005960b8 bytes 76031994
+ 005ba6e8 bytes 7e641a94
- 005960d0 ["INT_ADD", "register:40f0:8", ["const:5960d0:8", "const:4:8"]]
- 005960d0 ["CALL", null, ["callee:00c538e0:8"]]
+ 005ba700 ["INT_ADD", "register:40f0:8", ["const:5ba700:8", "const:4:8"]]
+ 005ba700 ["CALL", null, ["callee:00c538e0:8"]]
- 005960d0 bytes 70031994
+ 005ba700 bytes 78641a94
- 005960f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 005960f0 ["INT_ADD", "register:40f0:8", ["const:5960f0:8", "const:4:8"]]
- 005960f0 ["CALLIND", null, ["register:0:8"]]
+ 005ba720 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005ba720 ["INT_ADD", "register:40f0:8", ["const:5ba720:8", "const:4:8"]]
+ 005ba720 ["CALLIND", null, ["register:0:8"]]
- 005960f0 bytes 00013fd6
+ 005ba720 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d18123b4c1ae83b3021ba551fb971e3a"></a>

### [`0059d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d580.md) → [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) FUN_005c1bb0

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 19件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`0059d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d580.md) [`0064f828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064f828.md) [`0064f874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064f874.md) [`0070a160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070a/0070a160.md) · 呼出先 2件 [`0059d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 19件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) [`00675b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675b08.md) [`00675b54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00675/00675b54.md) [`00734260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00734/00734260.md) · 呼出先 2件 [`005c1bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059d5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d580.md#insn-0059d5a0) · [`0059d5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d580.md#insn-0059d5ac)
- 新版 [`005c1bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md#insn-005c1bd0) · [`005c1bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1bb0.md#insn-005c1bdc)

~~~diff
- 0059d5a0 ["INT_ADD", "register:40f0:8", ["const:59d5a0:8", "const:4:8"]]
- 0059d5a0 ["CALL", null, ["local:b0:8"]]
+ 005c1bd0 ["INT_ADD", "register:40f0:8", ["const:5c1bd0:8", "const:4:8"]]
+ 005c1bd0 ["CALL", null, ["local:b0:8"]]
- 0059d5a0 bytes f8ffff97
+ 005c1bd0 bytes f8ffff97
- 0059d5ac ["INT_ADD", "register:40f0:8", ["const:59d5ac:8", "const:4:8"]]
- 0059d5ac ["CALL", null, ["local:b0:8"]]
+ 005c1bdc ["INT_ADD", "register:40f0:8", ["const:5c1bdc:8", "const:4:8"]]
+ 005c1bdc ["CALL", null, ["local:b0:8"]]
- 0059d5ac bytes f5ffff97
+ 005c1bdc bytes f5ffff97
~~~


<a id="compare-62813e7e4c6946403c72d883bb3bfbfd"></a>

### [`0059d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d614.md) → [`005c1c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c44.md) FUN_005c1c44

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`0059d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d614.md) · 呼出先 2件 [`0059d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d614.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c1c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c44.md) · 呼出先 2件 [`005c1c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c44.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0059d634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d614.md#insn-0059d634) · [`0059d640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d614.md#insn-0059d640)
- 新版 [`005c1c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c44.md#insn-005c1c64) · [`005c1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c44.md#insn-005c1c70)

~~~diff
- 0059d634 ["INT_ADD", "register:40f0:8", ["const:59d634:8", "const:4:8"]]
- 0059d634 ["CALL", null, ["local:b0:8"]]
+ 005c1c64 ["INT_ADD", "register:40f0:8", ["const:5c1c64:8", "const:4:8"]]
+ 005c1c64 ["CALL", null, ["local:b0:8"]]
- 0059d634 bytes f8ffff97
+ 005c1c64 bytes f8ffff97
- 0059d640 ["INT_ADD", "register:40f0:8", ["const:59d640:8", "const:4:8"]]
- 0059d640 ["CALL", null, ["local:b0:8"]]
+ 005c1c70 ["INT_ADD", "register:40f0:8", ["const:5c1c70:8", "const:4:8"]]
+ 005c1c70 ["CALL", null, ["local:b0:8"]]
- 0059d640 bytes f5ffff97
+ 005c1c70 bytes f5ffff97
~~~


<a id="compare-d256bbc2d5a235f6d8dc9c0e244ca0a2"></a>

### [`005ab004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab004.md) → [`005cfcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcd0.md) FUN_005cfcd0

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ab020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab004.md#insn-005ab020)
- 新版 [`005cfcec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcd0.md#insn-005cfcec)

~~~diff
- 005ab020 ["INT_ADD", "register:40f0:8", ["const:5ab020:8", "const:4:8"]]
- 005ab020 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005cfcec ["INT_ADD", "register:40f0:8", ["const:5cfcec:8", "const:4:8"]]
+ 005cfcec ["CALL", null, ["callee:00c57ab0:8"]]
- 005ab020 bytes 10c01894
+ 005cfcec bytes 711f1a94
~~~


<a id="compare-29b9f98730bcf308a26acb802f6abe47"></a>

### [`005abca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abca8.md) → [`005d0974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md) FUN_005d0974

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) · 呼出先 3件 [`005aca98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005aca98.md) [`005acbf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acbf4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) · 呼出先 3件 [`005d1764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1764.md) [`005d18c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d18c0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005abcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abca8.md#insn-005abcf0) · [`005abd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abca8.md#insn-005abd14) · [`005abd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abca8.md#insn-005abd38)
- 新版 [`005d09bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md#insn-005d09bc) · [`005d09e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md#insn-005d09e0) · [`005d0a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0974.md#insn-005d0a04)

~~~diff
- 005abcf0 ["INT_ADD", "register:40f0:8", ["const:5abcf0:8", "const:4:8"]]
- 005abcf0 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d09bc ["INT_ADD", "register:40f0:8", ["const:5d09bc:8", "const:4:8"]]
+ 005d09bc ["CALL", null, ["callee:00c57a90:8"]]
- 005abcf0 bytes d4bc1894
+ 005d09bc bytes 351c1a94
- 005abd14 ["INT_ADD", "register:40f0:8", ["const:5abd14:8", "const:4:8"]]
- 005abd14 ["CALL", null, ["callee:005d18c0:8"]]
+ 005d09e0 ["INT_ADD", "register:40f0:8", ["const:5d09e0:8", "const:4:8"]]
+ 005d09e0 ["CALL", null, ["callee:005d18c0:8"]]
- 005abd14 bytes b8030094
+ 005d09e0 bytes b8030094
- 005abd38 ["INT_ADD", "register:40f0:8", ["const:5abd38:8", "const:4:8"]]
- 005abd38 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d0a04 ["INT_ADD", "register:40f0:8", ["const:5d0a04:8", "const:4:8"]]
+ 005d0a04 ["CALL", null, ["callee:00c57a90:8"]]
- 005abd38 bytes c2bc1894
+ 005d0a04 bytes 231c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82164a73c2fbd496b650639ccc27d814"></a>

### [`005ac4b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac4b4.md) → [`005d1180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1180.md) FUN_005d1180

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ac4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac4b4.md#insn-005ac4e4)
- 新版 [`005d11b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1180.md#insn-005d11b0)

~~~diff
- 005ac4e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005ac4e4 ["INT_ADD", "register:40f0:8", ["const:5ac4e4:8", "const:4:8"]]
- 005ac4e4 ["CALLIND", null, ["register:0:8"]]
+ 005d11b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d11b0 ["INT_ADD", "register:40f0:8", ["const:5d11b0:8", "const:4:8"]]
+ 005d11b0 ["CALLIND", null, ["register:0:8"]]
- 005ac4e4 bytes 20013fd6
+ 005d11b0 bytes 20013fd6
~~~


<a id="compare-61138fa986e26020e620813fb19f82c6"></a>

### [`005ad904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005ad904.md) → [`005d25d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d25d0.md) FUN_005d25d0

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005acfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acfa4.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`005d1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c70.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005ad988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005ad904.md#insn-005ad988) · [`005ad9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005ad904.md#insn-005ad9b0) · [`005ad9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005ad904.md#insn-005ad9ec)
- 新版 [`005d2654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d25d0.md#insn-005d2654) · [`005d267c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d25d0.md#insn-005d267c) · [`005d26b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d25d0.md#insn-005d26b8)

~~~diff
- 005ad988 ["INT_ADD", "register:40f0:8", ["const:5ad988:8", "const:4:8"]]
- 005ad988 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d2654 ["INT_ADD", "register:40f0:8", ["const:5d2654:8", "const:4:8"]]
+ 005d2654 ["CALL", null, ["callee:00c57a90:8"]]
- 005ad988 bytes aeb51894
+ 005d2654 bytes 0f151a94
- 005ad9b0 ["INT_ADD", "register:40f0:8", ["const:5ad9b0:8", "const:4:8"]]
- 005ad9b0 ["CALL", null, ["callee:00c57c00:8"]]
+ 005d267c ["INT_ADD", "register:40f0:8", ["const:5d267c:8", "const:4:8"]]
+ 005d267c ["CALL", null, ["callee:00c57c00:8"]]
- 005ad9b0 bytes 00b61894
+ 005d267c bytes 61151a94
- 005ad9ec ["COPY", "register:0:8", ["register:4048:8"]]
- 005ad9ec ["INT_ADD", "register:40f0:8", ["const:5ad9ec:8", "const:4:8"]]
- 005ad9ec ["CALLIND", null, ["register:0:8"]]
+ 005d26b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d26b8 ["INT_ADD", "register:40f0:8", ["const:5d26b8:8", "const:4:8"]]
+ 005d26b8 ["CALLIND", null, ["register:0:8"]]
- 005ad9ec bytes 20013fd6
+ 005d26b8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dac3277b76c4a6664f4a1119aa89f0df"></a>

### [`005ada74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005ada74.md) → [`005d2740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2740.md) FUN_005d2740

採用 · 移動量 `+0x24ccc` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005acfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acfa4.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`005d1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c70.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005adaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005ada74.md#insn-005adaf8) · [`005adb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005ada74.md#insn-005adb20) · [`005adb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005ada74.md#insn-005adb60)
- 新版 [`005d27c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2740.md#insn-005d27c4) · [`005d27ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2740.md#insn-005d27ec) · [`005d282c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2740.md#insn-005d282c)

~~~diff
- 005adaf8 ["INT_ADD", "register:40f0:8", ["const:5adaf8:8", "const:4:8"]]
- 005adaf8 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d27c4 ["INT_ADD", "register:40f0:8", ["const:5d27c4:8", "const:4:8"]]
+ 005d27c4 ["CALL", null, ["callee:00c57a90:8"]]
- 005adaf8 bytes 52b51894
+ 005d27c4 bytes b3141a94
- 005adb20 ["INT_ADD", "register:40f0:8", ["const:5adb20:8", "const:4:8"]]
- 005adb20 ["CALL", null, ["callee:00c57c00:8"]]
+ 005d27ec ["INT_ADD", "register:40f0:8", ["const:5d27ec:8", "const:4:8"]]
+ 005d27ec ["CALL", null, ["callee:00c57c00:8"]]
- 005adb20 bytes a4b51894
+ 005d27ec bytes 05151a94
- 005adb60 ["INT_ADD", "register:40f0:8", ["const:5adb60:8", "const:4:8"]]
- 005adb60 ["CALL", null, ["callee:00c5a400:8"]]
+ 005d282c ["INT_ADD", "register:40f0:8", ["const:5d282c:8", "const:4:8"]]
+ 005d282c ["CALL", null, ["callee:00c5a400:8"]]
- 005adb60 bytes 94bf1894
+ 005d282c bytes f51e1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f212ab0f94cb9f611207ae864771e1b"></a>

### [`005adcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adcd8.md) → [`005d29a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d29a4.md) FUN_005d29a4

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005acfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acfa4.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`005d1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c70.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005add5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adcd8.md#insn-005add5c) · [`005add84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adcd8.md#insn-005add84) · [`005addc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adcd8.md#insn-005addc0)
- 新版 [`005d2a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d29a4.md#insn-005d2a28) · [`005d2a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d29a4.md#insn-005d2a50) · [`005d2a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d29a4.md#insn-005d2a8c)

~~~diff
- 005add5c ["INT_ADD", "register:40f0:8", ["const:5add5c:8", "const:4:8"]]
- 005add5c ["CALL", null, ["callee:00c57a90:8"]]
+ 005d2a28 ["INT_ADD", "register:40f0:8", ["const:5d2a28:8", "const:4:8"]]
+ 005d2a28 ["CALL", null, ["callee:00c57a90:8"]]
- 005add5c bytes b9b41894
+ 005d2a28 bytes 1a141a94
- 005add84 ["INT_ADD", "register:40f0:8", ["const:5add84:8", "const:4:8"]]
- 005add84 ["CALL", null, ["callee:00c57c00:8"]]
+ 005d2a50 ["INT_ADD", "register:40f0:8", ["const:5d2a50:8", "const:4:8"]]
+ 005d2a50 ["CALL", null, ["callee:00c57c00:8"]]
- 005add84 bytes 0bb51894
+ 005d2a50 bytes 6c141a94
- 005addc0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005addc0 ["INT_ADD", "register:40f0:8", ["const:5addc0:8", "const:4:8"]]
- 005addc0 ["CALLIND", null, ["register:0:8"]]
+ 005d2a8c ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d2a8c ["INT_ADD", "register:40f0:8", ["const:5d2a8c:8", "const:4:8"]]
+ 005d2a8c ["CALLIND", null, ["register:0:8"]]
- 005addc0 bytes 20013fd6
+ 005d2a8c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d2bb067631c4a635fae7522958f1f0e"></a>

### [`005af1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af1a4.md) → [`005d3e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e70.md) FUN_005d3e70

採用 · 移動量 `+0x24ccc` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`005ae3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae3c8.md) [`005ae654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae654.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) [`005d3320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3320.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005af228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af1a4.md#insn-005af228) · [`005af250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af1a4.md#insn-005af250) · [`005af290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af1a4.md#insn-005af290)
- 新版 [`005d3ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e70.md#insn-005d3ef4) · [`005d3f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e70.md#insn-005d3f1c) · [`005d3f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3e70.md#insn-005d3f5c)

~~~diff
- 005af228 ["INT_ADD", "register:40f0:8", ["const:5af228:8", "const:4:8"]]
- 005af228 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d3ef4 ["INT_ADD", "register:40f0:8", ["const:5d3ef4:8", "const:4:8"]]
+ 005d3ef4 ["CALL", null, ["callee:00c57a90:8"]]
- 005af228 bytes 86af1894
+ 005d3ef4 bytes e70e1a94
- 005af250 ["INT_ADD", "register:40f0:8", ["const:5af250:8", "const:4:8"]]
- 005af250 ["CALL", null, ["callee:00c57c00:8"]]
+ 005d3f1c ["INT_ADD", "register:40f0:8", ["const:5d3f1c:8", "const:4:8"]]
+ 005d3f1c ["CALL", null, ["callee:00c57c00:8"]]
- 005af250 bytes d8af1894
+ 005d3f1c bytes 390f1a94
- 005af290 ["INT_ADD", "register:40f0:8", ["const:5af290:8", "const:4:8"]]
- 005af290 ["CALL", null, ["callee:00c5a400:8"]]
+ 005d3f5c ["INT_ADD", "register:40f0:8", ["const:5d3f5c:8", "const:4:8"]]
+ 005d3f5c ["CALL", null, ["callee:00c5a400:8"]]
- 005af290 bytes c8b91894
+ 005d3f5c bytes 29191a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e3ea0d581ac97a258bec5e79a87eb5b"></a>

### [`005af408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af408.md) → [`005d40d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d40d4.md) FUN_005d40d4

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005ae3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae3c8.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005d3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3094.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005af4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af408.md#insn-005af4d8) · [`005af544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af408.md#insn-005af544) · [`005af5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af408.md#insn-005af5a0)
- 新版 [`005d41a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d40d4.md#insn-005d41a4) · [`005d4210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d40d4.md#insn-005d4210) · [`005d426c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d40d4.md#insn-005d426c)

~~~diff
- 005af4d8 ["INT_ADD", "register:40f0:8", ["const:5af4d8:8", "const:4:8"]]
- 005af4d8 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d41a4 ["INT_ADD", "register:40f0:8", ["const:5d41a4:8", "const:4:8"]]
+ 005d41a4 ["CALL", null, ["callee:00c57a90:8"]]
- 005af4d8 bytes daae1894
+ 005d41a4 bytes 3b0e1a94
- 005af544 ["COPY", "register:0:8", ["register:4048:8"]]
- 005af544 ["INT_ADD", "register:40f0:8", ["const:5af544:8", "const:4:8"]]
- 005af544 ["CALLIND", null, ["register:0:8"]]
+ 005d4210 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005d4210 ["INT_ADD", "register:40f0:8", ["const:5d4210:8", "const:4:8"]]
+ 005d4210 ["CALLIND", null, ["register:0:8"]]
- 005af544 bytes 20013fd6
+ 005d4210 bytes 20013fd6
- 005af5a0 ["INT_ADD", "register:40f0:8", ["const:5af5a0:8", "const:4:8"]]
- 005af5a0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d426c ["INT_ADD", "register:40f0:8", ["const:5d426c:8", "const:4:8"]]
+ 005d426c ["CALL", null, ["callee:00c57ab0:8"]]
- 005af5a0 bytes b0ae1894
+ 005d426c bytes 110e1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e22be7cca392149db3e4c7731c424cb"></a>

### [`005af67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af67c.md) → [`005d4348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4348.md) FUN_005d4348

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005adef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adef8.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`005d2bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2bc4.md) · 呼出先 6件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005af700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af67c.md#insn-005af700) · [`005af728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af67c.md#insn-005af728) · [`005af760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af67c.md#insn-005af760)
- 新版 [`005d43cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4348.md#insn-005d43cc) · [`005d43f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4348.md#insn-005d43f4) · [`005d442c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4348.md#insn-005d442c)

~~~diff
- 005af700 ["INT_ADD", "register:40f0:8", ["const:5af700:8", "const:4:8"]]
- 005af700 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d43cc ["INT_ADD", "register:40f0:8", ["const:5d43cc:8", "const:4:8"]]
+ 005d43cc ["CALL", null, ["callee:00c57a90:8"]]
- 005af700 bytes 50ae1894
+ 005d43cc bytes b10d1a94
- 005af728 ["INT_ADD", "register:40f0:8", ["const:5af728:8", "const:4:8"]]
- 005af728 ["CALL", null, ["callee:00c57c00:8"]]
+ 005d43f4 ["INT_ADD", "register:40f0:8", ["const:5d43f4:8", "const:4:8"]]
+ 005d43f4 ["CALL", null, ["callee:00c57c00:8"]]
- 005af728 bytes a2ae1894
+ 005d43f4 bytes 030e1a94
- 005af760 ["COPY", "register:0:8", ["register:4040:8"]]
- 005af760 ["INT_ADD", "register:40f0:8", ["const:5af760:8", "const:4:8"]]
- 005af760 ["CALLIND", null, ["register:0:8"]]
+ 005d442c ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d442c ["INT_ADD", "register:40f0:8", ["const:5d442c:8", "const:4:8"]]
+ 005d442c ["CALLIND", null, ["register:0:8"]]
- 005af760 bytes 00013fd6
+ 005d442c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec6f0a988b12742ee86727bea2dd184f"></a>

### [`005af810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af810.md) → [`005d44dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md) FUN_005d44dc

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005ae770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae770.md) · 呼出先 4件 [`00426e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00426/00426e78.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`005d343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md) · 呼出先 4件 [`00449978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00449/00449978.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005af83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af810.md#insn-005af83c) · [`005af8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af810.md#insn-005af8a8) · [`005af8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af810.md#insn-005af8f4)
- 新版 [`005d4508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md#insn-005d4508) · [`005d4574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md#insn-005d4574) · [`005d45c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d44dc.md#insn-005d45c0)

~~~diff
- 005af83c ["COPY", "register:0:8", ["register:4040:8"]]
- 005af83c ["INT_ADD", "register:40f0:8", ["const:5af83c:8", "const:4:8"]]
- 005af83c ["CALLIND", null, ["register:0:8"]]
+ 005d4508 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005d4508 ["INT_ADD", "register:40f0:8", ["const:5d4508:8", "const:4:8"]]
+ 005d4508 ["CALLIND", null, ["register:0:8"]]
- 005af83c bytes 00013fd6
+ 005d4508 bytes 00013fd6
- 005af8a8 ["INT_ADD", "register:40f0:8", ["const:5af8a8:8", "const:4:8"]]
- 005af8a8 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d4574 ["INT_ADD", "register:40f0:8", ["const:5d4574:8", "const:4:8"]]
+ 005d4574 ["CALL", null, ["callee:00c57a90:8"]]
- 005af8a8 bytes e6ad1894
+ 005d4574 bytes 470d1a94
- 005af8f4 ["INT_ADD", "register:40f0:8", ["const:5af8f4:8", "const:4:8"]]
- 005af8f4 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d45c0 ["INT_ADD", "register:40f0:8", ["const:5d45c0:8", "const:4:8"]]
+ 005d45c0 ["CALL", null, ["callee:00c57a90:8"]]
- 005af8f4 bytes d3ad1894
+ 005d45c0 bytes 340d1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eadaac7683082962768fc8889141df50"></a>

### [`005af96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af96c.md) → [`005d4638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4638.md) FUN_005d4638

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005aea7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aea7c.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005d3748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005afa3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af96c.md#insn-005afa3c) · [`005afaa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af96c.md#insn-005afaa8) · [`005afab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005af96c.md#insn-005afab8)
- 新版 [`005d4708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4638.md#insn-005d4708) · [`005d4774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4638.md#insn-005d4774) · [`005d4784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4638.md#insn-005d4784)

~~~diff
- 005afa3c ["INT_ADD", "register:40f0:8", ["const:5afa3c:8", "const:4:8"]]
- 005afa3c ["CALL", null, ["callee:00c57a90:8"]]
+ 005d4708 ["INT_ADD", "register:40f0:8", ["const:5d4708:8", "const:4:8"]]
+ 005d4708 ["CALL", null, ["callee:00c57a90:8"]]
- 005afa3c bytes 81ad1894
+ 005d4708 bytes e20c1a94
- 005afaa8 ["COPY", "register:0:8", ["register:4050:8"]]
- 005afaa8 ["INT_ADD", "register:40f0:8", ["const:5afaa8:8", "const:4:8"]]
- 005afaa8 ["CALLIND", null, ["register:0:8"]]
+ 005d4774 ["COPY", "register:0:8", ["register:4050:8"]]
+ 005d4774 ["INT_ADD", "register:40f0:8", ["const:5d4774:8", "const:4:8"]]
+ 005d4774 ["CALLIND", null, ["register:0:8"]]
- 005afaa8 bytes 40013fd6
+ 005d4774 bytes 40013fd6
- 005afab8 ["INT_ADD", "register:40f0:8", ["const:5afab8:8", "const:4:8"]]
- 005afab8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d4784 ["INT_ADD", "register:40f0:8", ["const:5d4784:8", "const:4:8"]]
+ 005d4784 ["CALL", null, ["callee:00c57ab0:8"]]
- 005afab8 bytes 6aad1894
+ 005d4784 bytes cb0c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0bc4cfa3313bb8f3ec22c75cd40bb28"></a>

### [`005afb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afb7c.md) → [`005d4848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md) FUN_005d4848

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005aea7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005aea7c.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005afd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afd1c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005d3748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3748.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d49e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d49e8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005afc04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afb7c.md#insn-005afc04) · [`005afcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afb7c.md#insn-005afcc8) · [`005afcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afb7c.md#insn-005afcd8)
- 新版 [`005d48d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md#insn-005d48d0) · [`005d4994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md#insn-005d4994) · [`005d49a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4848.md#insn-005d49a4)

~~~diff
- 005afc04 ["INT_ADD", "register:40f0:8", ["const:5afc04:8", "const:4:8"]]
- 005afc04 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d48d0 ["INT_ADD", "register:40f0:8", ["const:5d48d0:8", "const:4:8"]]
+ 005d48d0 ["CALL", null, ["callee:00c57a90:8"]]
- 005afc04 bytes 0fad1894
+ 005d48d0 bytes 700c1a94
- 005afcc8 ["INT_ADD", "register:40f0:8", ["const:5afcc8:8", "const:4:8"]]
- 005afcc8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d4994 ["INT_ADD", "register:40f0:8", ["const:5d4994:8", "const:4:8"]]
+ 005d4994 ["CALL", null, ["callee:00c57ab0:8"]]
- 005afcc8 bytes e6ac1894
+ 005d4994 bytes 470c1a94
- 005afcd8 ["INT_ADD", "register:40f0:8", ["const:5afcd8:8", "const:4:8"]]
- 005afcd8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d49a4 ["INT_ADD", "register:40f0:8", ["const:5d49a4:8", "const:4:8"]]
+ 005d49a4 ["CALL", null, ["callee:00c57ab0:8"]]
- 005afcd8 bytes e2ac1894
+ 005d49a4 bytes 430c1a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bc64bdc1564f5c4b2b77e445ddf4249"></a>

### [`005b0e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0e84.md) → [`005d5b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5b50.md) FUN_005d5b50

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b0d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0d5c.md) · 呼出先 3件 [`005ac1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md) [`005ae894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae894.md) [`005b0b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b00.md)
- 新版 呼出元 1件 [`005d5a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5a28.md) · 呼出先 3件 [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md) [`005d3560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d3560.md) [`005d57cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d57cc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b0ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0e84.md#insn-005b0ef0) · [`005b0f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0e84.md#insn-005b0f38)
- 新版 [`005d5bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5b50.md#insn-005d5bbc) · [`005d5c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5b50.md#insn-005d5c04)

~~~diff
- 005b0ef0 ["INT_ADD", "register:40f0:8", ["const:5b0ef0:8", "const:4:8"]]
- 005b0ef0 ["CALL", null, ["callee:005d0e78:8"]]
+ 005d5bbc ["INT_ADD", "register:40f0:8", ["const:5d5bbc:8", "const:4:8"]]
+ 005d5bbc ["CALL", null, ["callee:005d0e78:8"]]
- 005b0ef0 bytes afecff97
+ 005d5bbc bytes afecff97
- 005b0f38 ["INT_ADD", "register:40f0:8", ["const:5b0f38:8", "const:4:8"]]
- 005b0f38 ["CALL", null, ["callee:005d57cc:8"]]
+ 005d5c04 ["INT_ADD", "register:40f0:8", ["const:5d5c04:8", "const:4:8"]]
+ 005d5c04 ["CALL", null, ["callee:005d57cc:8"]]
- 005b0f38 bytes f2feff97
+ 005d5c04 bytes f2feff97
~~~


<a id="compare-fabf329aaf0952eb7d678ff5766ad030"></a>

### [`005b0f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0f54.md) → [`005d5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md) FUN_005d5c20

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005a83e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a83e4.md) [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 4件 [`005aa9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md) [`005aae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aae28.md) [`005b1404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md) [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md)
- 新版 呼出元 2件 [`005cd0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd0b0.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 4件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005cfaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfaf4.md) [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b0fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0f54.md#insn-005b0fac) · [`005b1008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0f54.md#insn-005b1008) · [`005b1030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0f54.md#insn-005b1030)
- 新版 [`005d5c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md#insn-005d5c78) · [`005d5cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md#insn-005d5cd4) · [`005d5cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md#insn-005d5cfc)

~~~diff
- 005b0fac ["INT_ADD", "register:40f0:8", ["const:5b0fac:8", "const:4:8"]]
- 005b0fac ["CALL", null, ["callee:005cfaf4:8"]]
+ 005d5c78 ["INT_ADD", "register:40f0:8", ["const:5d5c78:8", "const:4:8"]]
+ 005d5c78 ["CALL", null, ["callee:005cfaf4:8"]]
- 005b0fac bytes 9fe7ff97
+ 005d5c78 bytes 9fe7ff97
- 005b1008 ["INT_ADD", "register:40f0:8", ["const:5b1008:8", "const:4:8"]]
- 005b1008 ["CALL", null, ["callee:005d69b0:8"]]
+ 005d5cd4 ["INT_ADD", "register:40f0:8", ["const:5d5cd4:8", "const:4:8"]]
+ 005d5cd4 ["CALL", null, ["callee:005d69b0:8"]]
- 005b1008 bytes 37030094
+ 005d5cd4 bytes 37030094
- 005b1030 ["INT_ADD", "register:40f0:8", ["const:5b1030:8", "const:4:8"]]
- 005b1030 ["CALL", null, ["callee:005cf680:8"]]
+ 005d5cfc ["INT_ADD", "register:40f0:8", ["const:5d5cfc:8", "const:4:8"]]
+ 005d5cfc ["CALL", null, ["callee:005cf680:8"]]
- 005b1030 bytes 61e6ff97
+ 005d5cfc bytes 61e6ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aeb1274b37cee8e04dae3d54840e05af"></a>

### [`005b1248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1248.md) → [`005d5f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5f14.md) FUN_005d5f14

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005a83e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a83e4.md) · 呼出先 1件 [`005b3850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3850.md)
- 新版 呼出元 1件 [`005cd0b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd0b0.md) · 呼出先 1件 [`005d851c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d851c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b12ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1248.md#insn-005b12ac)
- 新版 [`005d5f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5f14.md#insn-005d5f78)

~~~diff
- 005b12ac ["INT_ADD", "register:40f0:8", ["const:5b12ac:8", "const:4:8"]]
- 005b12ac ["CALL", null, ["callee:005d851c:8"]]
+ 005d5f78 ["INT_ADD", "register:40f0:8", ["const:5d5f78:8", "const:4:8"]]
+ 005d5f78 ["CALL", null, ["callee:005d851c:8"]]
- 005b12ac bytes 69090094
+ 005d5f78 bytes 69090094
~~~


<a id="compare-76e6d6dcec13826d83def2235b33a7db"></a>

### [`005b22e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b22e4.md) → [`005d6fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d6fb0.md) FUN_005d6fb0

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b2434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2434.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005d7100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7100.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b238c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b22e4.md#insn-005b238c) · [`005b239c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b22e4.md#insn-005b239c) · [`005b23e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b22e4.md#insn-005b23e0)
- 新版 [`005d7058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d6fb0.md#insn-005d7058) · [`005d7068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d6fb0.md#insn-005d7068) · [`005d70ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d6fb0.md#insn-005d70ac)

~~~diff
- 005b238c ["INT_ADD", "register:40f0:8", ["const:5b238c:8", "const:4:8"]]
- 005b238c ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d7058 ["INT_ADD", "register:40f0:8", ["const:5d7058:8", "const:4:8"]]
+ 005d7058 ["CALL", null, ["callee:00c57ab0:8"]]
- 005b238c bytes 35a31894
+ 005d7058 bytes 96021a94
- 005b239c ["INT_ADD", "register:40f0:8", ["const:5b239c:8", "const:4:8"]]
- 005b239c ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d7068 ["INT_ADD", "register:40f0:8", ["const:5d7068:8", "const:4:8"]]
+ 005d7068 ["CALL", null, ["callee:00c57ab0:8"]]
- 005b239c bytes 31a31894
+ 005d7068 bytes 92021a94
- 005b23e0 ["INT_ADD", "register:40f0:8", ["const:5b23e0:8", "const:4:8"]]
- 005b23e0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d70ac ["INT_ADD", "register:40f0:8", ["const:5d70ac:8", "const:4:8"]]
+ 005d70ac ["CALL", null, ["callee:00c57ab0:8"]]
- 005b23e0 bytes 20a31894
+ 005d70ac bytes 81021a94
~~~


<a id="compare-c8a85ee15603d244cbf49a1bf5623f01"></a>

### [`005b2434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2434.md) → [`005d7100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7100.md) FUN_005d7100

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b1404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md) · 呼出先 2件 [`005b22e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b22e4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) · 呼出先 2件 [`005d6fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d6fb0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b2448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2434.md#insn-005b2448) · [`005b245c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2434.md#insn-005b245c)
- 新版 [`005d7114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7100.md#insn-005d7114) · [`005d7128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7100.md#insn-005d7128)

~~~diff
- 005b2448 ["INT_ADD", "register:40f0:8", ["const:5b2448:8", "const:4:8"]]
- 005b2448 ["CALL", null, ["callee:005d6fb0:8"]]
+ 005d7114 ["INT_ADD", "register:40f0:8", ["const:5d7114:8", "const:4:8"]]
+ 005d7114 ["CALL", null, ["callee:005d6fb0:8"]]
- 005b2448 bytes a7ffff97
+ 005d7114 bytes a7ffff97
- 005b245c ["INT_ADD", "register:40f0:8", ["const:5b245c:8", "const:4:8"]]
- 005b245c ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d7128 ["INT_ADD", "register:40f0:8", ["const:5d7128:8", "const:4:8"]]
+ 005d7128 ["CALL", null, ["callee:00c57ab0:8"]]
- 005b245c bytes 01a31894
+ 005d7128 bytes 62021a94
~~~


<a id="compare-80eef29b877a685bd469df614d082e32"></a>

### [`005b24b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b24b0.md) → [`005d717c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md) FUN_005d717c

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b1404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005b2970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2970.md) [`005b2af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2af8.md) [`005b2c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2c84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md) [`005d77c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md) [`005d7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7950.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b2548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b24b0.md#insn-005b2548) · [`005b258c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b24b0.md#insn-005b258c) · [`005b259c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b24b0.md#insn-005b259c)
- 新版 [`005d7214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md#insn-005d7214) · [`005d7258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md#insn-005d7258) · [`005d7268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md#insn-005d7268)

~~~diff
- 005b2548 ["INT_ADD", "register:40f0:8", ["const:5b2548:8", "const:4:8"]]
- 005b2548 ["CALL", null, ["callee:00c57b40:8"]]
+ 005d7214 ["INT_ADD", "register:40f0:8", ["const:5d7214:8", "const:4:8"]]
+ 005d7214 ["CALL", null, ["callee:00c57b40:8"]]
- 005b2548 bytes eaa21894
+ 005d7214 bytes 4b021a94
- 005b258c ["INT_ADD", "register:40f0:8", ["const:5b258c:8", "const:4:8"]]
- 005b258c ["CALL", null, ["callee:00c57a90:8"]]
+ 005d7258 ["INT_ADD", "register:40f0:8", ["const:5d7258:8", "const:4:8"]]
+ 005d7258 ["CALL", null, ["callee:00c57a90:8"]]
- 005b258c bytes ada21894
+ 005d7258 bytes 0e021a94
- 005b259c ["INT_ADD", "register:40f0:8", ["const:5b259c:8", "const:4:8"]]
- 005b259c ["CALL", null, ["callee:005d763c:8"]]
+ 005d7268 ["INT_ADD", "register:40f0:8", ["const:5d7268:8", "const:4:8"]]
+ 005d7268 ["CALL", null, ["callee:005d763c:8"]]
- 005b259c bytes f5000094
+ 005d7268 bytes f5000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df79ab1acbb2ce1b5cdd7741a6bd08b9"></a>

### [`005b2970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2970.md) → [`005d763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md) FUN_005d763c

採用 · 移動量 `+0x24ccc` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005b24b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b24b0.md) [`005b2e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2e10.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 2件 [`005d717c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md) [`005d7adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b29d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2970.md#insn-005b29d8) · [`005b2a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2970.md#insn-005b2a10) · [`005b2ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2970.md#insn-005b2ac0)
- 新版 [`005d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md#insn-005d76a4) · [`005d76dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md#insn-005d76dc) · [`005d778c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md#insn-005d778c)

~~~diff
- 005b29d8 ["INT_ADD", "register:40f0:8", ["const:5b29d8:8", "const:4:8"]]
- 005b29d8 ["CALL", null, ["callee:00c57b40:8"]]
+ 005d76a4 ["INT_ADD", "register:40f0:8", ["const:5d76a4:8", "const:4:8"]]
+ 005d76a4 ["CALL", null, ["callee:00c57b40:8"]]
- 005b29d8 bytes c6a11894
+ 005d76a4 bytes 27011a94
- 005b2a10 ["INT_ADD", "register:40f0:8", ["const:5b2a10:8", "const:4:8"]]
- 005b2a10 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d76dc ["INT_ADD", "register:40f0:8", ["const:5d76dc:8", "const:4:8"]]
+ 005d76dc ["CALL", null, ["callee:00c57a90:8"]]
- 005b2a10 bytes 8ca11894
+ 005d76dc bytes ed001a94
- 005b2ac0 ["INT_ADD", "register:40f0:8", ["const:5b2ac0:8", "const:4:8"]]
- 005b2ac0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d778c ["INT_ADD", "register:40f0:8", ["const:5d778c:8", "const:4:8"]]
+ 005d778c ["CALL", null, ["callee:00c57ab0:8"]]
- 005b2ac0 bytes 68a11894
+ 005d778c bytes c9001a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7973dcc1dff35854bdb3d823e1e543cd"></a>

### [`005b2af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2af8.md) → [`005d77c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md) FUN_005d77c4

採用 · 移動量 `+0x24ccc` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005b24b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b24b0.md) [`005b2e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2e10.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 2件 [`005d717c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md) [`005d7adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b2b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2af8.md#insn-005b2b68) · [`005b2ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2af8.md#insn-005b2ba0) · [`005b2c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2af8.md#insn-005b2c50)
- 新版 [`005d7834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md#insn-005d7834) · [`005d786c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md#insn-005d786c) · [`005d791c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md#insn-005d791c)

~~~diff
- 005b2b68 ["INT_ADD", "register:40f0:8", ["const:5b2b68:8", "const:4:8"]]
- 005b2b68 ["CALL", null, ["callee:00c57b40:8"]]
+ 005d7834 ["INT_ADD", "register:40f0:8", ["const:5d7834:8", "const:4:8"]]
+ 005d7834 ["CALL", null, ["callee:00c57b40:8"]]
- 005b2b68 bytes 62a11894
+ 005d7834 bytes c3001a94
- 005b2ba0 ["INT_ADD", "register:40f0:8", ["const:5b2ba0:8", "const:4:8"]]
- 005b2ba0 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d786c ["INT_ADD", "register:40f0:8", ["const:5d786c:8", "const:4:8"]]
+ 005d786c ["CALL", null, ["callee:00c57a90:8"]]
- 005b2ba0 bytes 28a11894
+ 005d786c bytes 89001a94
- 005b2c50 ["INT_ADD", "register:40f0:8", ["const:5b2c50:8", "const:4:8"]]
- 005b2c50 ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d791c ["INT_ADD", "register:40f0:8", ["const:5d791c:8", "const:4:8"]]
+ 005d791c ["CALL", null, ["callee:00c57ab0:8"]]
- 005b2c50 bytes 04a11894
+ 005d791c bytes 65001a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f95b87808c5ef5c3ff06b7348d90a33c"></a>

### [`005b2c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2c84.md) → [`005d7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7950.md) FUN_005d7950

採用 · 移動量 `+0x24ccc` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b24b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b24b0.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`005d717c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d717c.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b2cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2c84.md#insn-005b2cf4) · [`005b2d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2c84.md#insn-005b2d2c) · [`005b2ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2c84.md#insn-005b2ddc)
- 新版 [`005d79c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7950.md#insn-005d79c0) · [`005d79f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7950.md#insn-005d79f8) · [`005d7aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7950.md#insn-005d7aa8)

~~~diff
- 005b2cf4 ["INT_ADD", "register:40f0:8", ["const:5b2cf4:8", "const:4:8"]]
- 005b2cf4 ["CALL", null, ["callee:00c57b40:8"]]
+ 005d79c0 ["INT_ADD", "register:40f0:8", ["const:5d79c0:8", "const:4:8"]]
+ 005d79c0 ["CALL", null, ["callee:00c57b40:8"]]
- 005b2cf4 bytes ffa01894
+ 005d79c0 bytes 60001a94
- 005b2d2c ["INT_ADD", "register:40f0:8", ["const:5b2d2c:8", "const:4:8"]]
- 005b2d2c ["CALL", null, ["callee:00c57a90:8"]]
+ 005d79f8 ["INT_ADD", "register:40f0:8", ["const:5d79f8:8", "const:4:8"]]
+ 005d79f8 ["CALL", null, ["callee:00c57a90:8"]]
- 005b2d2c bytes c5a01894
+ 005d79f8 bytes 26001a94
- 005b2ddc ["INT_ADD", "register:40f0:8", ["const:5b2ddc:8", "const:4:8"]]
- 005b2ddc ["CALL", null, ["callee:00c57ab0:8"]]
+ 005d7aa8 ["INT_ADD", "register:40f0:8", ["const:5d7aa8:8", "const:4:8"]]
+ 005d7aa8 ["CALL", null, ["callee:00c57ab0:8"]]
- 005b2ddc bytes a1a01894
+ 005d7aa8 bytes 02001a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45df97709724a2fa13647281443e4fa5"></a>

### [`005b2e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2e10.md) → [`005d7adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md) FUN_005d7adc

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b1404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1404.md) · 呼出先 8件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005b2970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2970.md) [`005b2af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2af8.md) [`005b31f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b31f4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005d60d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d60d0.md) · 呼出先 8件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d763c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d763c.md) [`005d77c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d77c4.md) [`005d7ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7ec0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b2e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2e10.md#insn-005b2e90) · [`005b2eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2e10.md#insn-005b2eb8) · [`005b2ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2e10.md#insn-005b2ec8)
- 新版 [`005d7b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md#insn-005d7b5c) · [`005d7b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md#insn-005d7b84) · [`005d7b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md#insn-005d7b94)

~~~diff
- 005b2e90 ["INT_ADD", "register:40f0:8", ["const:5b2e90:8", "const:4:8"]]
- 005b2e90 ["CALL", null, ["callee:005d7ec0:8"]]
+ 005d7b5c ["INT_ADD", "register:40f0:8", ["const:5d7b5c:8", "const:4:8"]]
+ 005d7b5c ["CALL", null, ["callee:005d7ec0:8"]]
- 005b2e90 bytes d9000094
+ 005d7b5c bytes d9000094
- 005b2eb8 ["INT_ADD", "register:40f0:8", ["const:5b2eb8:8", "const:4:8"]]
- 005b2eb8 ["CALL", null, ["callee:00c57a90:8"]]
+ 005d7b84 ["INT_ADD", "register:40f0:8", ["const:5d7b84:8", "const:4:8"]]
+ 005d7b84 ["CALL", null, ["callee:00c57a90:8"]]
- 005b2eb8 bytes 62a01894
+ 005d7b84 bytes c3ff1994
- 005b2ec8 ["INT_ADD", "register:40f0:8", ["const:5b2ec8:8", "const:4:8"]]
- 005b2ec8 ["CALL", null, ["callee:005d77c4:8"]]
+ 005d7b94 ["INT_ADD", "register:40f0:8", ["const:5d7b94:8", "const:4:8"]]
+ 005d7b94 ["CALL", null, ["callee:005d77c4:8"]]
- 005b2ec8 bytes 0cffff97
+ 005d7b94 bytes 0cffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb3739c800912a595e5efa20a8b7cc78"></a>

### [`005b4e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4e84.md) → [`005d9b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9b50.md) FUN_005d9b50

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`005b4278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4278.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005d8f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8f44.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b4eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4e84.md#insn-005b4eec) · [`005b4f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4e84.md#insn-005b4f20)
- 新版 [`005d9bb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9b50.md#insn-005d9bb8) · [`005d9bec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9b50.md#insn-005d9bec)

~~~diff
- 005b4eec ["INT_ADD", "register:40f0:8", ["const:5b4eec:8", "const:4:8"]]
- 005b4eec ["CALL", null, ["callee:00c57a90:8"]]
+ 005d9bb8 ["INT_ADD", "register:40f0:8", ["const:5d9bb8:8", "const:4:8"]]
+ 005d9bb8 ["CALL", null, ["callee:00c57a90:8"]]
- 005b4eec bytes 55981894
+ 005d9bb8 bytes b6f71994
- 005b4f20 ["INT_ADD", "register:40f0:8", ["const:5b4f20:8", "const:4:8"]]
- 005b4f20 ["CALL", null, ["callee:0043bb64:8"]]
+ 005d9bec ["INT_ADD", "register:40f0:8", ["const:5d9bec:8", "const:4:8"]]
+ 005d9bec ["CALL", null, ["callee:0043bb64:8"]]
- 005b4f20 bytes 5190f997
+ 005d9bec bytes de87f997
~~~


<a id="compare-17c18b1c441781751aeb1af9754febda"></a>

### [`005b51a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b51a0.md) → [`005d9e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9e6c.md) FUN_005d9e6c

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005b4278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4278.md) [`005b51a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b51a0.md) · 呼出先 2件 [`005b51a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b51a0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`005d8f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8f44.md) [`005d9e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9e6c.md) · 呼出先 2件 [`005d9e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9e6c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005b51c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b51a0.md#insn-005b51c0) · [`005b51cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b51a0.md#insn-005b51cc)
- 新版 [`005d9e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9e6c.md#insn-005d9e8c) · [`005d9e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9e6c.md#insn-005d9e98)

~~~diff
- 005b51c0 ["INT_ADD", "register:40f0:8", ["const:5b51c0:8", "const:4:8"]]
- 005b51c0 ["CALL", null, ["local:b0:8"]]
+ 005d9e8c ["INT_ADD", "register:40f0:8", ["const:5d9e8c:8", "const:4:8"]]
+ 005d9e8c ["CALL", null, ["local:b0:8"]]
- 005b51c0 bytes f8ffff97
+ 005d9e8c bytes f8ffff97
- 005b51cc ["INT_ADD", "register:40f0:8", ["const:5b51cc:8", "const:4:8"]]
- 005b51cc ["CALL", null, ["local:b0:8"]]
+ 005d9e98 ["INT_ADD", "register:40f0:8", ["const:5d9e98:8", "const:4:8"]]
+ 005d9e98 ["CALL", null, ["local:b0:8"]]
- 005b51cc bytes f5ffff97
+ 005d9e98 bytes f5ffff97
~~~


<a id="compare-cc21559073c1bbb5fd07111bc9358da0"></a>

### [`005baa68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005baa68.md) → [`005df738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df738.md) FUN_005df738

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005baa8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005baa68.md#insn-005baa8c) · [`005baa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005baa68.md#insn-005baa9c)
- 新版 [`005df75c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df738.md#insn-005df75c) · [`005df76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df738.md#insn-005df76c)

~~~diff
- 005baa8c ["INT_ADD", "register:40f0:8", ["const:5baa8c:8", "const:4:8"]]
- 005baa8c ["CALL", null, ["callee:0046e864:8"]]
+ 005df75c ["INT_ADD", "register:40f0:8", ["const:5df75c:8", "const:4:8"]]
+ 005df75c ["CALL", null, ["callee:0046e864:8"]]
- 005baa8c bytes d043fa97
+ 005df75c bytes 423cfa97
- 005baa9c ["INT_ADD", "register:40f0:8", ["const:5baa9c:8", "const:4:8"]]
- 005baa9c ["CALL", null, ["callee:00c57ab0:8"]]
+ 005df76c ["INT_ADD", "register:40f0:8", ["const:5df76c:8", "const:4:8"]]
+ 005df76c ["CALL", null, ["callee:00c57ab0:8"]]
- 005baa9c bytes 71811894
+ 005df76c bytes d1e01994
~~~


<a id="compare-7f1cfb3c272f6b160abe45783b37ee3f"></a>

### [`005c1cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c1/005c1cd4.md) → [`005e69a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e69a4.md) FUN_005e69a4

採用 · 移動量 `+0x24cd0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`005c0b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c0b0c.md) [`005c1cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c1/005c1cd4.md) [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) · 呼出先 2件 [`005c1cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c1/005c1cd4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`005e57dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e57dc.md) [`005e69a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e69a4.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) · 呼出先 2件 [`005e69a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e69a4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005c1cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c1/005c1cd4.md#insn-005c1cf4) · [`005c1d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c1/005c1cd4.md#insn-005c1d00)
- 新版 [`005e69c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e69a4.md#insn-005e69c4) · [`005e69d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e69a4.md#insn-005e69d0)

~~~diff
- 005c1cf4 ["INT_ADD", "register:40f0:8", ["const:5c1cf4:8", "const:4:8"]]
- 005c1cf4 ["CALL", null, ["local:b0:8"]]
+ 005e69c4 ["INT_ADD", "register:40f0:8", ["const:5e69c4:8", "const:4:8"]]
+ 005e69c4 ["CALL", null, ["local:b0:8"]]
- 005c1cf4 bytes f8ffff97
+ 005e69c4 bytes f8ffff97
- 005c1d00 ["INT_ADD", "register:40f0:8", ["const:5c1d00:8", "const:4:8"]]
- 005c1d00 ["CALL", null, ["local:b0:8"]]
+ 005e69d0 ["INT_ADD", "register:40f0:8", ["const:5e69d0:8", "const:4:8"]]
+ 005e69d0 ["CALL", null, ["local:b0:8"]]
- 005c1d00 bytes f5ffff97
+ 005e69d0 bytes f5ffff97
~~~


<a id="compare-317996674fa8aafc44a0ec42761ff6a7"></a>

### [`005d94f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d94f0.md) → [`005fe1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1b0.md) FUN_005fe1b0

採用 · 移動量 `+0x24cc0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`005d0a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0a68.md) [`005d94f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d94f0.md) · 呼出先 2件 [`005d94f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d94f0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`005fe1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1b0.md) · 呼出先 2件 [`005fe1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1b0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`005d9510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d94f0.md#insn-005d9510) · [`005d951c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d94f0.md#insn-005d951c)
- 新版 [`005fe1d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1b0.md#insn-005fe1d0) · [`005fe1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe1b0.md#insn-005fe1dc)

~~~diff
- 005d9510 ["INT_ADD", "register:40f0:8", ["const:5d9510:8", "const:4:8"]]
- 005d9510 ["CALL", null, ["local:b0:8"]]
+ 005fe1d0 ["INT_ADD", "register:40f0:8", ["const:5fe1d0:8", "const:4:8"]]
+ 005fe1d0 ["CALL", null, ["local:b0:8"]]
- 005d9510 bytes f8ffff97
+ 005fe1d0 bytes f8ffff97
- 005d951c ["INT_ADD", "register:40f0:8", ["const:5d951c:8", "const:4:8"]]
- 005d951c ["CALL", null, ["local:b0:8"]]
+ 005fe1dc ["INT_ADD", "register:40f0:8", ["const:5fe1dc:8", "const:4:8"]]
+ 005fe1dc ["CALL", null, ["local:b0:8"]]
- 005d951c bytes f5ffff97
+ 005fe1dc bytes f5ffff97
~~~


<a id="compare-9f047b434e5a79267c6ff88516ec8bf3"></a>

### [`00604928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604928.md) → [`0062a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a420.md) FUN_0062a420

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00604050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604050.md) [`00604928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604928.md) [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`00815d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00815/00815d0c.md) · 呼出先 2件 [`00604928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604928.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`00629b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629b48.md) [`0062a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a420.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`00847ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00847/00847ab8.md) · 呼出先 2件 [`0062a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a420.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00604948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604928.md#insn-00604948) · [`00604954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604928.md#insn-00604954)
- 新版 [`0062a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a420.md#insn-0062a440) · [`0062a44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a420.md#insn-0062a44c)

~~~diff
- 00604948 ["INT_ADD", "register:40f0:8", ["const:604948:8", "const:4:8"]]
- 00604948 ["CALL", null, ["local:b0:8"]]
+ 0062a440 ["INT_ADD", "register:40f0:8", ["const:62a440:8", "const:4:8"]]
+ 0062a440 ["CALL", null, ["local:b0:8"]]
- 00604948 bytes f8ffff97
+ 0062a440 bytes f8ffff97
- 00604954 ["INT_ADD", "register:40f0:8", ["const:604954:8", "const:4:8"]]
- 00604954 ["CALL", null, ["local:b0:8"]]
+ 0062a44c ["INT_ADD", "register:40f0:8", ["const:62a44c:8", "const:4:8"]]
+ 0062a44c ["CALL", null, ["local:b0:8"]]
- 00604954 bytes f5ffff97
+ 0062a44c bytes f5ffff97
~~~


<a id="compare-93f4bf9c68cf59c9b226da2a5bbf323f"></a>

### [`0060fd58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fd58.md) → [`00635850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635850.md) FUN_00635850

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0060fd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fd58.md#insn-0060fd80) · [`0060fd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fd58.md#insn-0060fd98) · [`0060fda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fd58.md#insn-0060fda8)
- 新版 [`00635878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635850.md#insn-00635878) · [`00635890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635850.md#insn-00635890) · [`006358a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635850.md#insn-006358a0)

~~~diff
- 0060fd80 ["INT_ADD", "register:40f0:8", ["const:60fd80:8", "const:4:8"]]
- 0060fd80 ["CALL", null, ["callee:00c57a80:8"]]
+ 00635878 ["INT_ADD", "register:40f0:8", ["const:635878:8", "const:4:8"]]
+ 00635878 ["CALL", null, ["callee:00c57a80:8"]]
- 0060fd80 bytes ac2c1794
+ 00635878 bytes 82881894
- 0060fd98 ["INT_ADD", "register:40f0:8", ["const:60fd98:8", "const:4:8"]]
- 0060fd98 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00635890 ["INT_ADD", "register:40f0:8", ["const:635890:8", "const:4:8"]]
+ 00635890 ["CALL", null, ["callee:00c57ab0:8"]]
- 0060fd98 bytes b22c1794
+ 00635890 bytes 88881894
- 0060fda8 ["INT_ADD", "register:40f0:8", ["const:60fda8:8", "const:4:8"]]
- 0060fda8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006358a0 ["INT_ADD", "register:40f0:8", ["const:6358a0:8", "const:4:8"]]
+ 006358a0 ["CALL", null, ["callee:00c57ab0:8"]]
- 0060fda8 bytes ae2c1794
+ 006358a0 bytes 84881894
~~~


<a id="compare-e0578b605969e765b863f462aa813bf5"></a>

### [`0060fde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fde8.md) → [`006358e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006358e0.md) FUN_006358e0

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0060fe38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fde8.md#insn-0060fe38) · [`0060fe64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fde8.md#insn-0060fe64)
- 新版 [`00635930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006358e0.md#insn-00635930) · [`0063595c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/006358e0.md#insn-0063595c)

~~~diff
- 0060fe38 ["INT_ADD", "register:40f0:8", ["const:60fe38:8", "const:4:8"]]
- 0060fe38 ["CALL", null, ["callee:0043bae0:8"]]
+ 00635930 ["INT_ADD", "register:40f0:8", ["const:635930:8", "const:4:8"]]
+ 00635930 ["CALL", null, ["callee:0043bae0:8"]]
- 0060fe38 bytes 6a24f897
+ 00635930 bytes 6c18f897
- 0060fe64 ["INT_ADD", "register:40f0:8", ["const:60fe64:8", "const:4:8"]]
- 0060fe64 ["CALL", null, ["callee:0043bae0:8"]]
+ 0063595c ["INT_ADD", "register:40f0:8", ["const:63595c:8", "const:4:8"]]
+ 0063595c ["CALL", null, ["callee:0043bae0:8"]]
- 0060fe64 bytes 5f24f897
+ 0063595c bytes 6118f897
~~~


<a id="compare-9c075741d1e910739a0eeb7f733618a7"></a>

### [`00613a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00613/00613a88.md) → [`00639580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639580.md) FUN_00639580

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00613ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00613/00613a88.md#insn-00613ac0)
- 新版 [`006395b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00639/00639580.md#insn-006395b8)

~~~diff
- 00613ac0 ["INT_ADD", "register:40f0:8", ["const:613ac0:8", "const:4:8"]]
- 00613ac0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006395b8 ["INT_ADD", "register:40f0:8", ["const:6395b8:8", "const:4:8"]]
+ 006395b8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00613ac0 bytes 681d1794
+ 006395b8 bytes 3e791894
~~~


<a id="compare-e01ffb257784e2e7412eca26e20f3049"></a>

### [`006145f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006145f0.md) → [`0063a0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a0e8.md) FUN_0063a0e8

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00614610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006145f0.md#insn-00614610) · [`00614638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006145f0.md#insn-00614638) · [`00614640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00614/006145f0.md#insn-00614640)
- 新版 [`0063a108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a0e8.md#insn-0063a108) · [`0063a130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a0e8.md#insn-0063a130) · [`0063a138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063a/0063a0e8.md#insn-0063a138)

~~~diff
- 00614610 ["INT_ADD", "register:40f0:8", ["const:614610:8", "const:4:8"]]
- 00614610 ["CALL", null, ["callee:00c538e0:8"]]
+ 0063a108 ["INT_ADD", "register:40f0:8", ["const:63a108:8", "const:4:8"]]
+ 0063a108 ["CALL", null, ["callee:00c538e0:8"]]
- 00614610 bytes 200a1794
+ 0063a108 bytes f6651894
- 00614638 ["COPY", "register:0:8", ["register:4040:8"]]
- 00614638 ["INT_ADD", "register:40f0:8", ["const:614638:8", "const:4:8"]]
- 00614638 ["CALLIND", null, ["register:0:8"]]
+ 0063a130 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0063a130 ["INT_ADD", "register:40f0:8", ["const:63a130:8", "const:4:8"]]
+ 0063a130 ["CALLIND", null, ["register:0:8"]]
- 00614638 bytes 00013fd6
+ 0063a130 bytes 00013fd6
- 00614640 ["INT_ADD", "register:40f0:8", ["const:614640:8", "const:4:8"]]
- 00614640 ["CALL", null, ["callee:00c57a80:8"]]
+ 0063a138 ["INT_ADD", "register:40f0:8", ["const:63a138:8", "const:4:8"]]
+ 0063a138 ["CALL", null, ["callee:00c57a80:8"]]
- 00614640 bytes 7c1a1794
+ 0063a138 bytes 52761894
~~~


<a id="compare-44cb6cc71e1db7aead0d386ee1ad20ee"></a>

### [`00624e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00624/00624e6c.md) → [`0064a950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a950.md) FUN_0064a950

採用 · 移動量 `+0x25ae4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) · 呼出先 3件 [`0069de1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069de1c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) · 呼出先 3件 [`006c4180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c4180.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00624e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00624/00624e6c.md#insn-00624e80) · [`00624e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00624/00624e6c.md#insn-00624e88) · [`00624e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00624/00624e6c.md#insn-00624e90)
- 新版 [`0064a964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a950.md#insn-0064a964) · [`0064a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a950.md#insn-0064a96c) · [`0064a974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064a/0064a950.md#insn-0064a974)

~~~diff
- 00624e80 ["INT_ADD", "register:40f0:8", ["const:624e80:8", "const:4:8"]]
- 00624e80 ["CALL", null, ["callee:006c4180:8"]]
+ 0064a964 ["INT_ADD", "register:40f0:8", ["const:64a964:8", "const:4:8"]]
+ 0064a964 ["CALL", null, ["callee:006c4180:8"]]
- 00624e80 bytes e7e30194
+ 0064a964 bytes 07e60194
- 00624e88 ["INT_ADD", "register:40f0:8", ["const:624e88:8", "const:4:8"]]
- 00624e88 ["CALL", null, ["callee:006c4180:8"]]
+ 0064a96c ["INT_ADD", "register:40f0:8", ["const:64a96c:8", "const:4:8"]]
+ 0064a96c ["CALL", null, ["callee:006c4180:8"]]
- 00624e88 bytes e5e30194
+ 0064a96c bytes 05e60194
- 00624e90 ["INT_ADD", "register:40f0:8", ["const:624e90:8", "const:4:8"]]
- 00624e90 ["CALL", null, ["callee:006c4180:8"]]
+ 0064a974 ["INT_ADD", "register:40f0:8", ["const:64a974:8", "const:4:8"]]
+ 0064a974 ["CALL", null, ["callee:006c4180:8"]]
- 00624e90 bytes e3e30194
+ 0064a974 bytes 03e60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f787356d52b19d84d1f2da0e280ee14"></a>

### [`0062ba54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062ba54.md) → [`00651538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651538.md) FUN_00651538

採用 · 移動量 `+0x25ae4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 2件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0062ba78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062ba54.md#insn-0062ba78) · [`0062bac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062ba54.md#insn-0062bac0) · [`0062bae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062ba54.md#insn-0062bae0)
- 新版 [`0065155c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651538.md#insn-0065155c) · [`006515a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651538.md#insn-006515a4) · [`006515c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651538.md#insn-006515c4)

~~~diff
- 0062ba78 ["INT_ADD", "register:40f0:8", ["const:62ba78:8", "const:4:8"]]
- 0062ba78 ["CALL", null, ["callee:00c57be0:8"]]
+ 0065155c ["INT_ADD", "register:40f0:8", ["const:65155c:8", "const:4:8"]]
+ 0065155c ["CALL", null, ["callee:00c57be0:8"]]
- 0062ba78 bytes c6bd1694
+ 0065155c bytes a1191894
- 0062bac0 ["INT_ADD", "register:40f0:8", ["const:62bac0:8", "const:4:8"]]
- 0062bac0 ["CALL", null, ["callee:00c57a90:8"]]
+ 006515a4 ["INT_ADD", "register:40f0:8", ["const:6515a4:8", "const:4:8"]]
+ 006515a4 ["CALL", null, ["callee:00c57a90:8"]]
- 0062bac0 bytes 60bd1694
+ 006515a4 bytes 3b191894
- 0062bae0 ["INT_ADD", "register:40f0:8", ["const:62bae0:8", "const:4:8"]]
- 0062bae0 ["CALL", null, ["callee:00c57b40:8"]]
+ 006515c4 ["INT_ADD", "register:40f0:8", ["const:6515c4:8", "const:4:8"]]
+ 006515c4 ["CALL", null, ["callee:00c57b40:8"]]
- 0062bae0 bytes 84bd1694
+ 006515c4 bytes 5f191894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54b5e2a81d3f0c6d8cd47e50607fa5be"></a>

### [`0062bb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bb1c.md) → [`00651600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651600.md) FUN_00651600

採用 · 移動量 `+0x25ae4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0062bb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bb1c.md#insn-0062bb84) · [`0062bbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bb1c.md#insn-0062bbc0)
- 新版 [`00651668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651600.md#insn-00651668) · [`006516a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/00651600.md#insn-006516a4)

~~~diff
- 0062bb84 ["INT_ADD", "register:40f0:8", ["const:62bb84:8", "const:4:8"]]
- 0062bb84 ["CALL", null, ["callee:00c57a90:8"]]
+ 00651668 ["INT_ADD", "register:40f0:8", ["const:651668:8", "const:4:8"]]
+ 00651668 ["CALL", null, ["callee:00c57a90:8"]]
- 0062bb84 bytes 2fbd1694
+ 00651668 bytes 0a191894
- 0062bbc0 ["INT_ADD", "register:40f0:8", ["const:62bbc0:8", "const:4:8"]]
- 0062bbc0 ["CALL", null, ["callee:0043bb64:8"]]
+ 006516a4 ["INT_ADD", "register:40f0:8", ["const:6516a4:8", "const:4:8"]]
+ 006516a4 ["CALL", null, ["callee:0043bb64:8"]]
- 0062bbc0 bytes 29b5f797
+ 006516a4 bytes 30a9f797
~~~


<a id="compare-30e1e83929fdbfdedaa431b99facb32c"></a>

### [`0062bbe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bbe8.md) → [`006516cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/006516cc.md) FUN_006516cc

採用 · 移動量 `+0x25ae4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) [`0062da7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062da7c.md) [`00687ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00687/00687ba8.md) [`007f24c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f2/007f24c4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`00653560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/00653560.md) [`006adef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ad/006adef0.md) [`008278d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00827/008278d8.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0062bc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bbe8.md#insn-0062bc20) · [`0062bc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bbe8.md#insn-0062bc30)
- 新版 [`00651704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/006516cc.md#insn-00651704) · [`00651714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00651/006516cc.md#insn-00651714)

~~~diff
- 0062bc20 ["INT_ADD", "register:40f0:8", ["const:62bc20:8", "const:4:8"]]
- 0062bc20 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00651704 ["INT_ADD", "register:40f0:8", ["const:651704:8", "const:4:8"]]
+ 00651704 ["CALL", null, ["callee:00c57ab0:8"]]
- 0062bc20 bytes 10bd1694
+ 00651704 bytes eb181894
- 0062bc30 ["INT_ADD", "register:40f0:8", ["const:62bc30:8", "const:4:8"]]
- 0062bc30 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00651714 ["INT_ADD", "register:40f0:8", ["const:651714:8", "const:4:8"]]
+ 00651714 ["CALL", null, ["callee:00c57ab0:8"]]
- 0062bc30 bytes 0cbd1694
+ 00651714 bytes e7181894
~~~


<a id="compare-797c076ec156f7a72ba00199ea0857b5"></a>

### [`0062d164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d164.md) → [`00652c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652c48.md) FUN_00652c48

採用 · 移動量 `+0x25ae4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006181e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00618/006181e8.md) [`0062d164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d164.md) [`00834d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00834/00834d90.md) · 呼出先 2件 [`0062d164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d164.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0063dcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dcd0.md) [`00652c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652c48.md) [`00866d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00866/00866d08.md) · 呼出先 2件 [`00652c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652c48.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0062d184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d164.md#insn-0062d184) · [`0062d190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d164.md#insn-0062d190)
- 新版 [`00652c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652c48.md#insn-00652c68) · [`00652c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652c48.md#insn-00652c74)

~~~diff
- 0062d184 ["INT_ADD", "register:40f0:8", ["const:62d184:8", "const:4:8"]]
- 0062d184 ["CALL", null, ["local:b0:8"]]
+ 00652c68 ["INT_ADD", "register:40f0:8", ["const:652c68:8", "const:4:8"]]
+ 00652c68 ["CALL", null, ["local:b0:8"]]
- 0062d184 bytes f8ffff97
+ 00652c68 bytes f8ffff97
- 0062d190 ["INT_ADD", "register:40f0:8", ["const:62d190:8", "const:4:8"]]
- 0062d190 ["CALL", null, ["local:b0:8"]]
+ 00652c74 ["INT_ADD", "register:40f0:8", ["const:652c74:8", "const:4:8"]]
+ 00652c74 ["CALL", null, ["local:b0:8"]]
- 0062d190 bytes f5ffff97
+ 00652c74 bytes f5ffff97
~~~


<a id="compare-e4fcfb6e93ef7807292be060a11d1d7f"></a>

### [`00638b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638b74.md) → [`0065ee44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ee44.md) FUN_0065ee44

採用 · 移動量 `+0x262d0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00634d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00634/00634d50.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0065ad00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065a/0065ad00.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00638bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638b74.md#insn-00638bb0)
- 新版 [`0065ee80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065e/0065ee44.md#insn-0065ee80)

~~~diff
- 00638bb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00638bb0 ["INT_ADD", "register:40f0:8", ["const:638bb0:8", "const:4:8"]]
- 00638bb0 ["CALLIND", null, ["register:0:8"]]
+ 0065ee80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0065ee80 ["INT_ADD", "register:40f0:8", ["const:65ee80:8", "const:4:8"]]
+ 0065ee80 ["CALLIND", null, ["register:0:8"]]
- 00638bb0 bytes 00013fd6
+ 0065ee80 bytes 00013fd6
~~~


<a id="compare-2ffcdd0f0bea5a2ae7d86ff2fe86e15a"></a>

### [`0063995c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/0063995c.md) → [`0065fc34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065fc34.md) FUN_0065fc34

採用 · 移動量 `+0x262d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00632964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/00632964.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00639a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639a84.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00658448`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00658/00658448.md) · 呼出先 5件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0054071c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/0054071c.md) [`0065fd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065fd5c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00639994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/0063995c.md#insn-00639994) · [`006399b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/0063995c.md#insn-006399b4) · [`006399ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/0063995c.md#insn-006399ec)
- 新版 [`0065fc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065fc34.md#insn-0065fc6c) · [`0065fc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065fc34.md#insn-0065fc8c) · [`0065fcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065f/0065fc34.md#insn-0065fcc4)

~~~diff
- 00639994 ["INT_ADD", "register:40f0:8", ["const:639994:8", "const:4:8"]]
- 00639994 ["CALL", null, ["callee:0065fd5c:8"]]
+ 0065fc6c ["INT_ADD", "register:40f0:8", ["const:65fc6c:8", "const:4:8"]]
+ 0065fc6c ["CALL", null, ["callee:0065fd5c:8"]]
- 00639994 bytes 3c000094
+ 0065fc6c bytes 3c000094
- 006399b4 ["INT_ADD", "register:40f0:8", ["const:6399b4:8", "const:4:8"]]
- 006399b4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0065fc8c ["INT_ADD", "register:40f0:8", ["const:65fc8c:8", "const:4:8"]]
+ 0065fc8c ["CALL", null, ["callee:00c57a90:8"]]
- 006399b4 bytes a3851694
+ 0065fc8c bytes 81df1794
- 006399ec ["INT_ADD", "register:40f0:8", ["const:6399ec:8", "const:4:8"]]
- 006399ec ["CALL", null, ["callee:0054071c:8"]]
+ 0065fcc4 ["INT_ADD", "register:40f0:8", ["const:65fcc4:8", "const:4:8"]]
+ 0065fcc4 ["CALL", null, ["callee:0054071c:8"]]
- 006399ec bytes a68ffb97
+ 0065fcc4 bytes 9682fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e7957f319598138d573221bd7ed082d"></a>

### [`006412c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/006412c4.md) → [`0066759c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/0066759c.md) FUN_0066759c

採用 · 移動量 `+0x262d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 6件 [`0063f0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063f0f4.md) [`006412c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/006412c4.md) [`00808774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00808/00808774.md) [`0094f7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094f/0094f7d0.md) [`00957f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00957/00957f9c.md) · 呼出先 2件 [`006412c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/006412c4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 6件 [`006653cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/006653cc.md) [`0066759c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/0066759c.md) [`0083a0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083a/0083a0e0.md) [`0098527c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00985/0098527c.md) [`0098da6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0098d/0098da6c.md) · 呼出先 2件 [`0066759c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/0066759c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006412e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/006412c4.md#insn-006412e4) · [`006412f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/006412c4.md#insn-006412f0)
- 新版 [`006675bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/0066759c.md#insn-006675bc) · [`006675c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00667/0066759c.md#insn-006675c8)

~~~diff
- 006412e4 ["INT_ADD", "register:40f0:8", ["const:6412e4:8", "const:4:8"]]
- 006412e4 ["CALL", null, ["local:b0:8"]]
+ 006675bc ["INT_ADD", "register:40f0:8", ["const:6675bc:8", "const:4:8"]]
+ 006675bc ["CALL", null, ["local:b0:8"]]
- 006412e4 bytes f8ffff97
+ 006675bc bytes f8ffff97
- 006412f0 ["INT_ADD", "register:40f0:8", ["const:6412f0:8", "const:4:8"]]
- 006412f0 ["CALL", null, ["local:b0:8"]]
+ 006675c8 ["INT_ADD", "register:40f0:8", ["const:6675c8:8", "const:4:8"]]
+ 006675c8 ["CALL", null, ["local:b0:8"]]
- 006412f0 bytes f5ffff97
+ 006675c8 bytes f5ffff97
~~~


<a id="compare-d314ba96a36b7050ef41b99d608013fc"></a>

### [`006425d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/006425d4.md) → [`006688ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/006688ac.md) FUN_006688ac

採用 · 移動量 `+0x262d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`0069a008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069a008.md) [`00797bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00797/00797bfc.md) [`007bfd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bf/007bfd30.md) [`007c0198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c0/007c0198.md) · 呼出先 3件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0064248c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/0064248c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 5件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) [`006c036c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c0/006c036c.md) [`007c8cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007c8/007c8cb0.md) [`007f1ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f1/007f1ecc.md) [`007f2334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f2/007f2334.md) · 呼出先 3件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00668764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/00668764.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006425f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/006425d4.md#insn-006425f4) · [`00642644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/006425d4.md#insn-00642644) · [`00642688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/006425d4.md#insn-00642688)
- 新版 [`006688cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/006688ac.md#insn-006688cc) · [`0066891c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/006688ac.md#insn-0066891c) · [`00668960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00668/006688ac.md#insn-00668960)

~~~diff
- 006425f4 ["INT_ADD", "register:40f0:8", ["const:6425f4:8", "const:4:8"]]
- 006425f4 ["CALL", null, ["callee:00668764:8"]]
+ 006688cc ["INT_ADD", "register:40f0:8", ["const:6688cc:8", "const:4:8"]]
+ 006688cc ["CALL", null, ["callee:00668764:8"]]
- 006425f4 bytes a6ffff97
+ 006688cc bytes a6ffff97
- 00642644 ["INT_ADD", "register:40f0:8", ["const:642644:8", "const:4:8"]]
- 00642644 ["CALL", null, ["callee:00c57a90:8"]]
+ 0066891c ["INT_ADD", "register:40f0:8", ["const:66891c:8", "const:4:8"]]
+ 0066891c ["CALL", null, ["callee:00c57a90:8"]]
- 00642644 bytes 7f621694
+ 0066891c bytes 5dbc1794
- 00642688 ["INT_ADD", "register:40f0:8", ["const:642688:8", "const:4:8"]]
- 00642688 ["CALL", null, ["callee:0043bb64:8"]]
+ 00668960 ["INT_ADD", "register:40f0:8", ["const:668960:8", "const:4:8"]]
+ 00668960 ["CALL", null, ["callee:0043bb64:8"]]
- 00642688 bytes 775af797
+ 00668960 bytes 814cf797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08f5cf426e77ca141f9b3e3f197fead6"></a>

### [`006451d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/006451d4.md) → [`0066b4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b4ac.md) FUN_0066b4ac

採用 · 移動量 `+0x262d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 3件 [`0045dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dc60.md) [`0045dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dd10.md) [`0045de70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045de70.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 3件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00645200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/006451d4.md#insn-00645200) · [`0064521c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/006451d4.md#insn-0064521c) · [`0064523c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/006451d4.md#insn-0064523c)
- 新版 [`0066b4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b4ac.md#insn-0066b4d8) · [`0066b4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b4ac.md#insn-0066b4f4) · [`0066b514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b4ac.md#insn-0066b514)

~~~diff
- 00645200 ["INT_ADD", "register:40f0:8", ["const:645200:8", "const:4:8"]]
- 00645200 ["CALL", null, ["callee:00480af8:8"]]
+ 0066b4d8 ["INT_ADD", "register:40f0:8", ["const:66b4d8:8", "const:4:8"]]
+ 0066b4d8 ["CALL", null, ["callee:00480af8:8"]]
- 00645200 bytes 9862f897
+ 0066b4d8 bytes 8855f897
- 0064521c ["INT_ADD", "register:40f0:8", ["const:64521c:8", "const:4:8"]]
- 0064521c ["CALL", null, ["callee:00480af8:8"]]
+ 0066b4f4 ["INT_ADD", "register:40f0:8", ["const:66b4f4:8", "const:4:8"]]
+ 0066b4f4 ["CALL", null, ["callee:00480af8:8"]]
- 0064521c bytes 9162f897
+ 0066b4f4 bytes 8155f897
- 0064523c ["INT_ADD", "register:40f0:8", ["const:64523c:8", "const:4:8"]]
- 0064523c ["CALL", null, ["callee:00480ba8:8"]]
+ 0066b514 ["INT_ADD", "register:40f0:8", ["const:66b514:8", "const:4:8"]]
+ 0066b514 ["CALL", null, ["callee:00480ba8:8"]]
- 0064523c bytes b562f897
+ 0066b514 bytes a555f897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c14076a713b0227e3b4c9d98226bf3c0"></a>

### [`00645504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/00645504.md) → [`0066b7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b7dc.md) FUN_0066b7dc

採用 · 移動量 `+0x262d8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 3件 [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`00644304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/00644304.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md)
- 新版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 3件 [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`0066a5dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066a/0066a5dc.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00645518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/00645504.md#insn-00645518) · [`00645528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/00645504.md#insn-00645528) · [`00645568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/00645504.md#insn-00645568)
- 新版 [`0066b7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b7dc.md#insn-0066b7f0) · [`0066b800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b7dc.md#insn-0066b800) · [`0066b840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b7dc.md#insn-0066b840)

~~~diff
- 00645518 ["INT_ADD", "register:40f0:8", ["const:645518:8", "const:4:8"]]
- 00645518 ["CALL", null, ["callee:00802b18:8"]]
+ 0066b7f0 ["INT_ADD", "register:40f0:8", ["const:66b7f0:8", "const:4:8"]]
+ 0066b7f0 ["CALL", null, ["callee:00802b18:8"]]
- 00645518 bytes 0e290694
+ 0066b7f0 bytes ca5c0694
- 00645528 ["INT_ADD", "register:40f0:8", ["const:645528:8", "const:4:8"]]
- 00645528 ["CALL", null, ["callee:0066a5dc:8"]]
+ 0066b800 ["INT_ADD", "register:40f0:8", ["const:66b800:8", "const:4:8"]]
+ 0066b800 ["CALL", null, ["callee:0066a5dc:8"]]
- 00645528 bytes 77fbff97
+ 0066b800 bytes 77fbff97
- 00645568 ["INT_ADD", "register:40f0:8", ["const:645568:8", "const:4:8"]]
- 00645568 ["CALL", null, ["callee:0049f3b0:8"]]
+ 0066b840 ["INT_ADD", "register:40f0:8", ["const:66b840:8", "const:4:8"]]
+ 0066b840 ["CALL", null, ["callee:0049f3b0:8"]]
- 00645568 bytes ecdbf897
+ 0066b840 bytes dccef897
~~~


<a id="compare-1d8f02aedd04aecc5a263c820f9d4283"></a>

### [`0064573c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/0064573c.md) → [`0066ba14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066ba14.md) FUN_0066ba14

採用 · 移動量 `+0x262d8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`006456c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/006456c4.md) [`0064573c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/0064573c.md) [`00645938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/00645938.md) · 呼出先 2件 [`0064573c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/0064573c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0066b99c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066b99c.md) [`0066ba14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066ba14.md) [`0066bc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066bc10.md) · 呼出先 2件 [`0066ba14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066ba14.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00645758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/0064573c.md#insn-00645758) · [`00645764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/0064573c.md#insn-00645764) · [`00645774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/0064573c.md#insn-00645774)
- 新版 [`0066ba30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066ba14.md#insn-0066ba30) · [`0066ba3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066ba14.md#insn-0066ba3c) · [`0066ba4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0066b/0066ba14.md#insn-0066ba4c)

~~~diff
- 00645758 ["INT_ADD", "register:40f0:8", ["const:645758:8", "const:4:8"]]
- 00645758 ["CALL", null, ["local:b0:8"]]
+ 0066ba30 ["INT_ADD", "register:40f0:8", ["const:66ba30:8", "const:4:8"]]
+ 0066ba30 ["CALL", null, ["local:b0:8"]]
- 00645758 bytes f9ffff97
+ 0066ba30 bytes f9ffff97
- 00645764 ["INT_ADD", "register:40f0:8", ["const:645764:8", "const:4:8"]]
- 00645764 ["CALL", null, ["local:b0:8"]]
+ 0066ba3c ["INT_ADD", "register:40f0:8", ["const:66ba3c:8", "const:4:8"]]
+ 0066ba3c ["CALL", null, ["local:b0:8"]]
- 00645764 bytes f6ffff97
+ 0066ba3c bytes f6ffff97
- 00645774 ["INT_ADD", "register:40f0:8", ["const:645774:8", "const:4:8"]]
- 00645774 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0066ba4c ["INT_ADD", "register:40f0:8", ["const:66ba4c:8", "const:4:8"]]
+ 0066ba4c ["CALL", null, ["callee:00c57ab0:8"]]
- 00645774 bytes 3b561694
+ 0066ba4c bytes 19b01794
~~~


<a id="compare-90d1b8de77bf93edba2a615ace096b2e"></a>

### [`0064c578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c578.md) → [`00672858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672858.md) FUN_00672858

採用 · 移動量 `+0x262e0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0064c5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c578.md#insn-0064c5b0) · [`0064c5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c578.md#insn-0064c5c4) · [`0064c5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c578.md#insn-0064c5cc)
- 新版 [`00672890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672858.md#insn-00672890) · [`006728a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672858.md#insn-006728a4) · [`006728ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672858.md#insn-006728ac)

~~~diff
- 0064c5b0 ["INT_ADD", "register:40f0:8", ["const:64c5b0:8", "const:4:8"]]
- 0064c5b0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00672890 ["INT_ADD", "register:40f0:8", ["const:672890:8", "const:4:8"]]
+ 00672890 ["CALL", null, ["callee:00c538e0:8"]]
- 0064c5b0 bytes 382a1694
+ 00672890 bytes 14841794
- 0064c5c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0064c5c4 ["INT_ADD", "register:40f0:8", ["const:64c5c4:8", "const:4:8"]]
- 0064c5c4 ["CALLIND", null, ["register:0:8"]]
+ 006728a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 006728a4 ["INT_ADD", "register:40f0:8", ["const:6728a4:8", "const:4:8"]]
+ 006728a4 ["CALLIND", null, ["register:0:8"]]
- 0064c5c4 bytes 00013fd6
+ 006728a4 bytes 00013fd6
- 0064c5cc ["INT_ADD", "register:40f0:8", ["const:64c5cc:8", "const:4:8"]]
- 0064c5cc ["CALL", null, ["callee:00c57a80:8"]]
+ 006728ac ["INT_ADD", "register:40f0:8", ["const:6728ac:8", "const:4:8"]]
+ 006728ac ["CALL", null, ["callee:00c57a80:8"]]
- 0064c5cc bytes 993a1694
+ 006728ac bytes 75941794
~~~


<a id="compare-ef7b06354b7af6a533e181ca7396d31c"></a>

### [`0064c804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c804.md) → [`00672ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672ae4.md) FUN_00672ae4

採用 · 移動量 `+0x262e0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0064c5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c5e4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006728c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/006728c4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0064c814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c804.md#insn-0064c814)
- 新版 [`00672af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672ae4.md#insn-00672af4)

~~~diff
- 0064c814 ["INT_ADD", "register:40f0:8", ["const:64c814:8", "const:4:8"]]
- 0064c814 ["CALL", null, ["callee:006728c4:8"]]
+ 00672af4 ["INT_ADD", "register:40f0:8", ["const:672af4:8", "const:4:8"]]
+ 00672af4 ["CALL", null, ["callee:006728c4:8"]]
- 0064c814 bytes 74ffff97
+ 00672af4 bytes 74ffff97
~~~


<a id="compare-c3d0d0eef48dc47cc4753d21ca91b384"></a>

### [`0064ca44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064ca44.md) → [`00672d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d24.md) FUN_00672d24

採用 · 移動量 `+0x262e0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0064c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c828.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00672b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672b08.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0064ca54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064ca44.md#insn-0064ca54)
- 新版 [`00672d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672d24.md#insn-00672d34)

~~~diff
- 0064ca54 ["INT_ADD", "register:40f0:8", ["const:64ca54:8", "const:4:8"]]
- 0064ca54 ["CALL", null, ["callee:00672b08:8"]]
+ 00672d34 ["INT_ADD", "register:40f0:8", ["const:672d34:8", "const:4:8"]]
+ 00672d34 ["CALL", null, ["callee:00672b08:8"]]
- 0064ca54 bytes 75ffff97
+ 00672d34 bytes 75ffff97
~~~


<a id="compare-4cff5a8da72a6ab9d4ebc4f976cf8cff"></a>

### [`00655468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/00655468.md) → [`0067b748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b748.md) FUN_0067b748

採用 · 移動量 `+0x262e0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006554a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/00655468.md#insn-006554a0) · [`006554b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/00655468.md#insn-006554b4) · [`006554bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/00655468.md#insn-006554bc)
- 新版 [`0067b780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b748.md#insn-0067b780) · [`0067b794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b748.md#insn-0067b794) · [`0067b79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067b/0067b748.md#insn-0067b79c)

~~~diff
- 006554a0 ["INT_ADD", "register:40f0:8", ["const:6554a0:8", "const:4:8"]]
- 006554a0 ["CALL", null, ["callee:00c538e0:8"]]
+ 0067b780 ["INT_ADD", "register:40f0:8", ["const:67b780:8", "const:4:8"]]
+ 0067b780 ["CALL", null, ["callee:00c538e0:8"]]
- 006554a0 bytes 7c061694
+ 0067b780 bytes 58601794
- 006554b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 006554b4 ["INT_ADD", "register:40f0:8", ["const:6554b4:8", "const:4:8"]]
- 006554b4 ["CALLIND", null, ["register:0:8"]]
+ 0067b794 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0067b794 ["INT_ADD", "register:40f0:8", ["const:67b794:8", "const:4:8"]]
+ 0067b794 ["CALLIND", null, ["register:0:8"]]
- 006554b4 bytes 00013fd6
+ 0067b794 bytes 00013fd6
- 006554bc ["INT_ADD", "register:40f0:8", ["const:6554bc:8", "const:4:8"]]
- 006554bc ["CALL", null, ["callee:00c57a80:8"]]
+ 0067b79c ["INT_ADD", "register:40f0:8", ["const:67b79c:8", "const:4:8"]]
+ 0067b79c ["CALL", null, ["callee:00c57a80:8"]]
- 006554bc bytes dd161694
+ 0067b79c bytes b9701794
~~~


<a id="compare-0244188998ebec4d3dbcadbcc1e156b4"></a>

### [`00656258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656258.md) → [`0067c538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c538.md) FUN_0067c538

採用 · 移動量 `+0x262e0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0065627c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656258.md#insn-0065627c) · [`0065628c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656258.md#insn-0065628c)
- 新版 [`0067c55c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c538.md#insn-0067c55c) · [`0067c56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067c/0067c538.md#insn-0067c56c)

~~~diff
- 0065627c ["INT_ADD", "register:40f0:8", ["const:65627c:8", "const:4:8"]]
- 0065627c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0067c55c ["INT_ADD", "register:40f0:8", ["const:67c55c:8", "const:4:8"]]
+ 0067c55c ["CALL", null, ["callee:00c57ab0:8"]]
- 0065627c bytes 79131694
+ 0067c55c bytes 556d1794
- 0065628c ["INT_ADD", "register:40f0:8", ["const:65628c:8", "const:4:8"]]
- 0065628c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0067c56c ["INT_ADD", "register:40f0:8", ["const:67c56c:8", "const:4:8"]]
+ 0067c56c ["CALL", null, ["callee:00c57ab0:8"]]
- 0065628c bytes 75131694
+ 0067c56c bytes 516d1794
~~~


<a id="compare-7cb3d0cc5cb2c2ebc10dc555954aef2e"></a>

### [`006581ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006581ec.md) → [`0067e4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e4cc.md) FUN_0067e4cc

採用 · 移動量 `+0x262e0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00658244",
      "incomplete_value": true,
      "site": "00658248",
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
            "const:a8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00658248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006581ec.md#insn-00658248) · [`00658200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006581ec.md#insn-00658200) · [`00658208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006581ec.md#insn-00658208)
- 新版 [`0067e528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e4cc.md#insn-0067e528) · [`0067e4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e4cc.md#insn-0067e4e0) · [`0067e4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e4cc.md#insn-0067e4e8)

~~~diff
- 00658248 ["INT_ADD", "register:40f0:8", ["const:658248:8", "const:4:8"]]
- 00658248 ["CALL", null, ["callee:0046ef9c:8"]]
+ 0067e528 ["INT_ADD", "register:40f0:8", ["const:67e528:8", "const:4:8"]]
+ 0067e528 ["CALL", null, ["callee:0046ef9c:8"]]
- 00658248 bytes afcff797
+ 0067e528 bytes 9dc2f797
- 00658200 ["INT_ADD", "register:40f0:8", ["const:658200:8", "const:4:8"]]
- 00658200 ["CALL", null, ["callee:0046ef9c:8"]]
+ 0067e4e0 ["INT_ADD", "register:40f0:8", ["const:67e4e0:8", "const:4:8"]]
+ 0067e4e0 ["CALL", null, ["callee:0046ef9c:8"]]
- 00658200 bytes c1cff797
+ 0067e4e0 bytes afc2f797
- 00658208 ["INT_ADD", "register:40f0:8", ["const:658208:8", "const:4:8"]]
- 00658208 ["CALL", null, ["callee:0046ef9c:8"]]
+ 0067e4e8 ["INT_ADD", "register:40f0:8", ["const:67e4e8:8", "const:4:8"]]
+ 0067e4e8 ["CALL", null, ["callee:0046ef9c:8"]]
- 00658208 bytes bfcff797
+ 0067e4e8 bytes adc2f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ef4e0d6e1c2ad3100a99124987e327e"></a>

### [`0065bec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bec4.md) → [`006821b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006821b4.md) FUN_006821b4

採用 · 移動量 `+0x262f0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0065bcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bcc8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00681fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00681/00681fb8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0065bed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bec4.md#insn-0065bed4)
- 新版 [`006821c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006821b4.md#insn-006821c4)

~~~diff
- 0065bed4 ["INT_ADD", "register:40f0:8", ["const:65bed4:8", "const:4:8"]]
- 0065bed4 ["CALL", null, ["callee:00681fb8:8"]]
+ 006821c4 ["INT_ADD", "register:40f0:8", ["const:6821c4:8", "const:4:8"]]
+ 006821c4 ["CALL", null, ["callee:00681fb8:8"]]
- 0065bed4 bytes 7dffff97
+ 006821c4 bytes 7dffff97
~~~


<a id="compare-12e63006c56f88302f7028a3e385055b"></a>

### [`00663624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663624.md) → [`00689914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/00689914.md) FUN_00689914

採用 · 移動量 `+0x262f0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`005b726c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b726c.md) [`006e34b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e3/006e34b0.md) [`009877e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00987/009877e0.md) [`00989a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989a48.md) · 呼出先 2件 [`00661f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/00661f64.md) [`0066341c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/0066341c.md)
- 新版 呼出元 4件 [`005dbf3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbf3c.md) [`0070d378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070d378.md) [`009bd2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bd/009bd2c0.md) [`009bf53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009bf/009bf53c.md) · 呼出先 2件 [`00688254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00688/00688254.md) [`0068970c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/0068970c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00663638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663624.md#insn-00663638)
- 新版 [`00689928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/00689914.md#insn-00689928)

~~~diff
- 00663638 ["INT_ADD", "register:40f0:8", ["const:663638:8", "const:4:8"]]
- 00663638 ["CALL", null, ["callee:00688254:8"]]
+ 00689928 ["INT_ADD", "register:40f0:8", ["const:689928:8", "const:4:8"]]
+ 00689928 ["CALL", null, ["callee:00688254:8"]]
- 00663638 bytes 4bfaff97
+ 00689928 bytes 4bfaff97
~~~


<a id="compare-9ed3807338246203fd1ac216bd37d4d1"></a>

### [`00663650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663650.md) → [`00689940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/00689940.md) FUN_00689940

採用 · 移動量 `+0x262f0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`009479b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00947/009479b4.md) · 呼出先 2件 [`00661f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/00661f64.md) [`0066341c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/0066341c.md)
- 新版 呼出元 1件 [`0097d45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097d/0097d45c.md) · 呼出先 2件 [`00688254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00688/00688254.md) [`0068970c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/0068970c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00663664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663650.md#insn-00663664)
- 新版 [`00689954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/00689940.md#insn-00689954)

~~~diff
- 00663664 ["INT_ADD", "register:40f0:8", ["const:663664:8", "const:4:8"]]
- 00663664 ["CALL", null, ["callee:00688254:8"]]
+ 00689954 ["INT_ADD", "register:40f0:8", ["const:689954:8", "const:4:8"]]
+ 00689954 ["CALL", null, ["callee:00688254:8"]]
- 00663664 bytes 40faff97
+ 00689954 bytes 40faff97
~~~


<a id="compare-a9710b2009df829fc31df52544a0e0f2"></a>

### [`0066c0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0a8.md) → [`006923f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923f0.md) FUN_006923f0

採用 · 移動量 `+0x26348` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00660ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660ab4.md) [`0066c0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0a8.md) [`0081715c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/0081715c.md) · 呼出先 2件 [`0066c0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0a8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`00686da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00686/00686da4.md) [`006923f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923f0.md) [`00848f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848f54.md) · 呼出先 2件 [`006923f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923f0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0066c0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0a8.md#insn-0066c0c4) · [`0066c0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0a8.md#insn-0066c0d0) · [`0066c0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0a8.md#insn-0066c0e0)
- 新版 [`0069240c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923f0.md#insn-0069240c) · [`00692418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923f0.md#insn-00692418) · [`00692428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923f0.md#insn-00692428)

~~~diff
- 0066c0c4 ["INT_ADD", "register:40f0:8", ["const:66c0c4:8", "const:4:8"]]
- 0066c0c4 ["CALL", null, ["local:b0:8"]]
+ 0069240c ["INT_ADD", "register:40f0:8", ["const:69240c:8", "const:4:8"]]
+ 0069240c ["CALL", null, ["local:b0:8"]]
- 0066c0c4 bytes f9ffff97
+ 0069240c bytes f9ffff97
- 0066c0d0 ["INT_ADD", "register:40f0:8", ["const:66c0d0:8", "const:4:8"]]
- 0066c0d0 ["CALL", null, ["local:b0:8"]]
+ 00692418 ["INT_ADD", "register:40f0:8", ["const:692418:8", "const:4:8"]]
+ 00692418 ["CALL", null, ["local:b0:8"]]
- 0066c0d0 bytes f6ffff97
+ 00692418 bytes f6ffff97
- 0066c0e0 ["INT_ADD", "register:40f0:8", ["const:66c0e0:8", "const:4:8"]]
- 0066c0e0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00692428 ["INT_ADD", "register:40f0:8", ["const:692428:8", "const:4:8"]]
+ 00692428 ["CALL", null, ["callee:00c57ab0:8"]]
- 0066c0e0 bytes e0bb1594
+ 00692428 bytes a2151794
~~~


