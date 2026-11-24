# v15.7.4 → v16.0.0 · 要調査の変更候補 (21)

[一覧の目次](README.md)

<a id="compare-2b98037b4ee5ab33ee0d78498e00066a"></a>

### [`00b977a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b977a0.md) → [`00c141e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c141e8.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE13__get_weekdayERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b977cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b977a0.md#insn-00b977cc)
- 新版 [`00c14214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c141e8.md#insn-00c14214)

~~~diff
- 00b977cc ["INT_ADD", "register:40f0:8", ["const:b977cc:8", "const:4:8"]]
- 00b977cc ["CALL", null, ["callee:00c14484:8"]]
+ 00c14214 ["INT_ADD", "register:40f0:8", ["const:c14214:8", "const:4:8"]]
+ 00c14214 ["CALL", null, ["callee:00c14484:8"]]
- 00b977cc bytes 9c000094
+ 00c14214 bytes 9c000094
~~~


<a id="compare-ea261ec1d4554d23ce9bc2c7f247330e"></a>

### [`00b97800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97800.md) → [`00c14248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14248.md) _ZNKSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE11__get_year4ERiRS4_S4_RjRKNS_5ctypeIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b97a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97a3c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c14484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14484.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9782c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b97/00b97800.md#insn-00b9782c)
- 新版 [`00c14274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14248.md#insn-00c14274)

~~~diff
- 00b9782c ["INT_ADD", "register:40f0:8", ["const:b9782c:8", "const:4:8"]]
- 00b9782c ["CALL", null, ["callee:00c14484:8"]]
+ 00c14274 ["INT_ADD", "register:40f0:8", ["const:c14274:8", "const:4:8"]]
+ 00c14274 ["CALL", null, ["callee:00c14484:8"]]
- 00b9782c bytes 84000094
+ 00c14274 bytes 84000094
~~~


<a id="compare-98b9ecbd8d3dc79d487dacd45b90b19c"></a>

### [`00b982c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b982c0.md) → [`00c14d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14d08.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11do_get_dateES4_S4_RNS_8ios_baseERjP2tm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1640.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e230.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b982f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b982c0.md#insn-00b982f8)
- 新版 [`00c14d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c14/00c14d08.md#insn-00c14d40)

~~~diff
- 00b982f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b982f8 ["INT_ADD", "register:40f0:8", ["const:b982f8:8", "const:4:8"]]
- 00b982f8 ["CALLIND", null, ["register:0:8"]]
+ 00c14d40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c14d40 ["INT_ADD", "register:40f0:8", ["const:c14d40:8", "const:4:8"]]
+ 00c14d40 ["CALLIND", null, ["register:0:8"]]
- 00b982f8 bytes 00013fd6
+ 00c14d40 bytes 00013fd6
~~~


<a id="compare-430aef8bdf31bfa75468d9dfd46b7522"></a>

### [`00b98884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98884.md) → [`00c152cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c152cc.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE10__get_yearERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b988b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98884.md#insn-00b988b0)
- 新版 [`00c152f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c152cc.md#insn-00c152f8)

~~~diff
- 00b988b0 ["INT_ADD", "register:40f0:8", ["const:b988b0:8", "const:4:8"]]
- 00b988b0 ["CALL", null, ["callee:00c161c8:8"]]
+ 00c152f8 ["INT_ADD", "register:40f0:8", ["const:c152f8:8", "const:4:8"]]
+ 00c152f8 ["CALL", null, ["callee:00c161c8:8"]]
- 00b988b0 bytes b4030094
+ 00c152f8 bytes b4030094
~~~


<a id="compare-669f89b0be88dc6e30dcd9dfd3eda014"></a>

### [`00b98f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98f5c.md) → [`00c159a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c159a4.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE9__get_dayERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b98f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b98/00b98f5c.md#insn-00b98f88)
- 新版 [`00c159d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c159a4.md#insn-00c159d0)

~~~diff
- 00b98f88 ["INT_ADD", "register:40f0:8", ["const:b98f88:8", "const:4:8"]]
- 00b98f88 ["CALL", null, ["callee:00c161c8:8"]]
+ 00c159d0 ["INT_ADD", "register:40f0:8", ["const:c159d0:8", "const:4:8"]]
+ 00c159d0 ["CALL", null, ["callee:00c161c8:8"]]
- 00b98f88 bytes fe010094
+ 00c159d0 bytes fe010094
~~~


<a id="compare-7e1d2b6695f4480e574c69736b01401b"></a>

### [`00b99020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99020.md) → [`00c15a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15a68.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_12_hourERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b9904c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99020.md#insn-00b9904c)
- 新版 [`00c15a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15a68.md#insn-00c15a94)

~~~diff
- 00b9904c ["INT_ADD", "register:40f0:8", ["const:b9904c:8", "const:4:8"]]
- 00b9904c ["CALL", null, ["callee:00c161c8:8"]]
+ 00c15a94 ["INT_ADD", "register:40f0:8", ["const:c15a94:8", "const:4:8"]]
+ 00c15a94 ["CALL", null, ["callee:00c161c8:8"]]
- 00b9904c bytes cd010094
+ 00c15a94 bytes cd010094
~~~


<a id="compare-0cf757ab8d65f7078f2711b4ed5a01db"></a>

### [`00b990e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b990e4.md) → [`00c15b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15b2c.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE11__get_monthERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b99110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b990e4.md#insn-00b99110)
- 新版 [`00c15b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15b2c.md#insn-00c15b58)

~~~diff
- 00b99110 ["INT_ADD", "register:40f0:8", ["const:b99110:8", "const:4:8"]]
- 00b99110 ["CALL", null, ["callee:00c161c8:8"]]
+ 00c15b58 ["INT_ADD", "register:40f0:8", ["const:c15b58:8", "const:4:8"]]
+ 00c15b58 ["CALL", null, ["callee:00c161c8:8"]]
- 00b99110 bytes 9c010094
+ 00c15b58 bytes 9c010094
~~~


<a id="compare-e5b6b20448df24e5fcee1024e5dd5c90"></a>

### [`00b99480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99480.md) → [`00c15ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15ec8.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE12__get_secondERiRS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b99780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c161c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c161c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b994ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99480.md#insn-00b994ac)
- 新版 [`00c15ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15ec8.md#insn-00c15ef4)

~~~diff
- 00b994ac ["INT_ADD", "register:40f0:8", ["const:b994ac:8", "const:4:8"]]
- 00b994ac ["CALL", null, ["callee:00c161c8:8"]]
+ 00c15ef4 ["INT_ADD", "register:40f0:8", ["const:c15ef4:8", "const:4:8"]]
+ 00c15ef4 ["CALL", null, ["callee:00c161c8:8"]]
- 00b994ac bytes b5000094
+ 00c15ef4 bytes b5000094
~~~


<a id="compare-937e929498a294857646c9652b705135"></a>

### [`00ba05c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba05c0.md) → [`00c1d008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d008.md) _ZNSt6__ndk114codecvt_bynameIcc9mbstate_tED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1750.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e340.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba05d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba05c0.md#insn-00ba05d4)
- 新版 [`00c1d01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d008.md#insn-00c1d01c)

~~~diff
- 00ba05d4 ["INT_ADD", "register:40f0:8", ["const:ba05d4:8", "const:4:8"]]
- 00ba05d4 ["CALL", null, ["callee:00c5e340:8"]]
+ 00c1d01c ["INT_ADD", "register:40f0:8", ["const:c1d01c:8", "const:4:8"]]
+ 00c1d01c ["CALL", null, ["callee:00c5e340:8"]]
- 00ba05d4 bytes 5f040194
+ 00c1d01c bytes c9040194
~~~


<a id="compare-c23b085bfbf22be0f98a027082410697"></a>

### [`00ba0690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0690.md) → [`00c1d0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d0d8.md) _ZNSt6__ndk114codecvt_bynameIDsDu9mbstate_tED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be17c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be17c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e3b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba06a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0690.md#insn-00ba06a4)
- 新版 [`00c1d0ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d0d8.md#insn-00c1d0ec)

~~~diff
- 00ba06a4 ["INT_ADD", "register:40f0:8", ["const:ba06a4:8", "const:4:8"]]
- 00ba06a4 ["CALL", null, ["callee:00c5e3b0:8"]]
+ 00c1d0ec ["INT_ADD", "register:40f0:8", ["const:c1d0ec:8", "const:4:8"]]
+ 00c1d0ec ["CALL", null, ["callee:00c5e3b0:8"]]
- 00ba06a4 bytes 47040194
+ 00c1d0ec bytes b1040194
~~~


<a id="compare-04aa9216b484b2653d4bd65560b2f8ec"></a>

### [`00ba06c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06c4.md) → [`00c1d10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d10c.md) _ZNSt6__ndk114codecvt_bynameIDiDu9mbstate_tED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be17e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be17e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e3d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ba06d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06c4.md#insn-00ba06d8)
- 新版 [`00c1d120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d10c.md#insn-00c1d120)

~~~diff
- 00ba06d8 ["INT_ADD", "register:40f0:8", ["const:ba06d8:8", "const:4:8"]]
- 00ba06d8 ["CALL", null, ["callee:00c5e3d0:8"]]
+ 00c1d120 ["INT_ADD", "register:40f0:8", ["const:c1d120:8", "const:4:8"]]
+ 00c1d120 ["CALL", null, ["callee:00c5e3d0:8"]]
- 00ba06d8 bytes 42040194
+ 00c1d120 bytes ac040194
~~~


<a id="compare-e654ddc5e1d6f5e7be73efa4bfdb3df6"></a>

### [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) → [`00c2550c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md) FUN_00c2550c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 13件 [`00ba89ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba89ec.md) [`00ba9030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9030.md) [`00baa328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa328.md) [`00baa8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa8a0.md) [`00bab43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab43c.md) · 呼出先 2件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)
- 新版 呼出元 13件 [`00c25434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25434.md) [`00c25a78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25a78.md) [`00c26d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26d70.md) [`00c272e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c272e8.md) [`00c27e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27e84.md) · 呼出先 2件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c58bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58bd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c25534",
      "incomplete_value": true,
      "site": "00c25540",
      "value": [
        "live",
        "register:4098:8"
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
      "definition_site": "00c25530",
      "incomplete_value": true,
      "site": "00c25540",
      "value": [
        "live",
        "register:4000:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 4
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md#insn-00ba8af8) · [`00ba8ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md#insn-00ba8ae4)
- 新版 [`00c25540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md#insn-00c25540) · [`00c2552c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c2550c.md#insn-00c2552c)

~~~diff
- 00ba8af8 ["INT_ADD", "register:40f0:8", ["const:ba8af8:8", "const:4:8"]]
- 00ba8af8 ["CALL", null, ["callee:00c58bd0:8"]]
+ 00c25540 ["INT_ADD", "register:40f0:8", ["const:c25540:8", "const:4:8"]]
+ 00c25540 ["CALL", null, ["callee:00c58bd0:8"]]
- 00ba8af8 bytes a2cd0094
+ 00c25540 bytes a4cd0094
- 00ba8ae4 ["INT_ADD", "register:40f0:8", ["const:ba8ae4:8", "const:4:8"]]
- 00ba8ae4 ["CALL", null, ["callee:00c57be0:8"]]
+ 00c2552c ["INT_ADD", "register:40f0:8", ["const:c2552c:8", "const:4:8"]]
+ 00c2552c ["CALL", null, ["callee:00c57be0:8"]]
- 00ba8ae4 bytes abc90094
+ 00c2552c bytes adc90094
~~~


<a id="compare-eb404d129201e328b6b6ae81353d0e65"></a>

### [`00baaa3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa3c.md) → [`00c27484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27484.md) _ZNSt6__ndk112ctype_bynameIwED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e620.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00baaa50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa3c.md#insn-00baaa50)
- 新版 [`00c27498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27484.md#insn-00c27498)

~~~diff
- 00baaa50 ["INT_ADD", "register:40f0:8", ["const:baaa50:8", "const:4:8"]]
- 00baaa50 ["CALL", null, ["callee:00c5e620:8"]]
+ 00c27498 ["INT_ADD", "register:40f0:8", ["const:c27498:8", "const:4:8"]]
+ 00c27498 ["CALL", null, ["callee:00c5e620:8"]]
- 00baaa50 bytes fcdb0094
+ 00c27498 bytes 62dc0094
~~~


<a id="compare-36067512d608d1af420f8547d37b61de"></a>

### [`00bad128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad128.md) → [`00c29b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29b70.md) _ZNKSt6__ndk114__codecvt_utf8IwE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac8b4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c292fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c292fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad128.md#insn-00bad174)
- 新版 [`00c29bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29b70.md#insn-00c29bbc)

~~~diff
- 00bad174 ["INT_ADD", "register:40f0:8", ["const:bad174:8", "const:4:8"]]
- 00bad174 ["CALL", null, ["callee:00c292fc:8"]]
+ 00c29bbc ["INT_ADD", "register:40f0:8", ["const:c29bbc:8", "const:4:8"]]
+ 00c29bbc ["CALL", null, ["callee:00c292fc:8"]]
- 00bad174 bytes d0fdff97
+ 00c29bbc bytes d0fdff97
~~~


<a id="compare-9805a4222a3680d7db2a950e607c382a"></a>

### [`00bad198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad198.md) → [`00c29be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29be0.md) _ZNKSt6__ndk114__codecvt_utf8IwE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bacaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacaa4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c294ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c294ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad198.md#insn-00bad1e4)
- 新版 [`00c29c2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29be0.md#insn-00c29c2c)

~~~diff
- 00bad1e4 ["INT_ADD", "register:40f0:8", ["const:bad1e4:8", "const:4:8"]]
- 00bad1e4 ["CALL", null, ["callee:00c294ec:8"]]
+ 00c29c2c ["INT_ADD", "register:40f0:8", ["const:c29c2c:8", "const:4:8"]]
+ 00c29c2c ["CALL", null, ["callee:00c294ec:8"]]
- 00bad1e4 bytes 30feff97
+ 00c29c2c bytes 30feff97
~~~


<a id="compare-bb89f59b79e6b44250328d370759bbb0"></a>

### [`00bad6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad6b8.md) → [`00c2a100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a100.md) _ZNKSt6__ndk114__codecvt_utf8IDiE6do_outER9mbstate_tPKDiS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bac8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bac8b4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c292fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c292fc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad6b8.md#insn-00bad704)
- 新版 [`00c2a14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a100.md#insn-00c2a14c)

~~~diff
- 00bad704 ["INT_ADD", "register:40f0:8", ["const:bad704:8", "const:4:8"]]
- 00bad704 ["CALL", null, ["callee:00c292fc:8"]]
+ 00c2a14c ["INT_ADD", "register:40f0:8", ["const:c2a14c:8", "const:4:8"]]
+ 00c2a14c ["CALL", null, ["callee:00c292fc:8"]]
- 00bad704 bytes 6cfcff97
+ 00c2a14c bytes 6cfcff97
~~~


<a id="compare-490828824ea939c5d32e26383dc0e444"></a>

### [`00bad728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad728.md) → [`00c2a170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a170.md) _ZNKSt6__ndk114__codecvt_utf8IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bacaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacaa4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c294ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c294ec.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bad774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad728.md#insn-00bad774)
- 新版 [`00c2a1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a170.md#insn-00c2a1bc)

~~~diff
- 00bad774 ["INT_ADD", "register:40f0:8", ["const:bad774:8", "const:4:8"]]
- 00bad774 ["CALL", null, ["callee:00c294ec:8"]]
+ 00c2a1bc ["INT_ADD", "register:40f0:8", ["const:c2a1bc:8", "const:4:8"]]
+ 00c2a1bc ["CALL", null, ["callee:00c294ec:8"]]
- 00bad774 bytes ccfcff97
+ 00c2a1bc bytes ccfcff97
~~~


<a id="compare-d23ec895c7827a642ab8727ab5601cd4"></a>

### [`00bb7e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e44.md) → [`00c3488c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c3488c.md) FUN_00c3488c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e44.md#insn-00bb7e58)
- 新版 [`00c348a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c3488c.md#insn-00c348a0)

~~~diff
- 00bb7e58 ["INT_ADD", "register:40f0:8", ["const:bb7e58:8", "const:4:8"]]
- 00bb7e58 ["CALL", null, ["callee:00c5a480:8"]]
+ 00c348a0 ["INT_ADD", "register:40f0:8", ["const:c348a0:8", "const:4:8"]]
+ 00c348a0 ["CALL", null, ["callee:00c5a480:8"]]
- 00bb7e58 bytes f6960094
+ 00c348a0 bytes f8960094
~~~


<a id="compare-a0bae75c1642d131e1e10e9bdc3708f4"></a>

### [`00bb7e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e70.md) → [`00c348b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c348b8.md) FUN_00c348b8

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb7e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7e70.md#insn-00bb7e84)
- 新版 [`00c348cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c348b8.md#insn-00c348cc)

~~~diff
- 00bb7e84 ["INT_ADD", "register:40f0:8", ["const:bb7e84:8", "const:4:8"]]
- 00bb7e84 ["CALL", null, ["callee:00c5a480:8"]]
+ 00c348cc ["INT_ADD", "register:40f0:8", ["const:c348cc:8", "const:4:8"]]
+ 00c348cc ["CALL", null, ["callee:00c5a480:8"]]
- 00bb7e84 bytes eb960094
+ 00c348cc bytes ed960094
~~~


<a id="compare-ab54f665da444ec6088c0d125874556a"></a>

### [`00bb800c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb800c.md) → [`00c34a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34a54.md) FUN_00c34a54

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb8020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb800c.md#insn-00bb8020)
- 新版 [`00c34a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34a54.md#insn-00c34a68)

~~~diff
- 00bb8020 ["INT_ADD", "register:40f0:8", ["const:bb8020:8", "const:4:8"]]
- 00bb8020 ["CALL", null, ["callee:00c5a480:8"]]
+ 00c34a68 ["INT_ADD", "register:40f0:8", ["const:c34a68:8", "const:4:8"]]
+ 00c34a68 ["CALL", null, ["callee:00c5a480:8"]]
- 00bb8020 bytes 84960094
+ 00c34a68 bytes 86960094
~~~


<a id="compare-8ccdf47b9c39c60d94a6cd4510d0197d"></a>

### [`00bb9248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9248.md) → [`00c35c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c90.md) FUN_00c35c90

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bb5ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5ffc.md) · 呼出先 2件 [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`00b74d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74d9c.md)
- 新版 呼出元 1件 [`00c32a44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c32a44.md) · 呼出先 2件 [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`00bf17e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf1/00bf17e4.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bb9284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9248.md#insn-00bb9284) · [`00bb929c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9248.md#insn-00bb929c)
- 新版 [`00c35ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c90.md#insn-00c35ccc) · [`00c35ce4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35c90.md#insn-00c35ce4)

~~~diff
- 00bb9284 ["INT_ADD", "register:40f0:8", ["const:bb9284:8", "const:4:8"]]
- 00bb9284 ["CALL", null, ["callee:00bf17e4:8"]]
+ 00c35ccc ["INT_ADD", "register:40f0:8", ["const:c35ccc:8", "const:4:8"]]
+ 00c35ccc ["CALL", null, ["callee:00bf17e4:8"]]
- 00bb9284 bytes c6eefe97
+ 00c35ccc bytes c6eefe97
- 00bb929c ["INT_ADD", "register:40f0:8", ["const:bb929c:8", "const:4:8"]]
- 00bb929c ["CALL", null, ["callee:004428dc:8"]]
+ 00c35ce4 ["INT_ADD", "register:40f0:8", ["const:c35ce4:8", "const:4:8"]]
+ 00c35ce4 ["CALL", null, ["callee:004428dc:8"]]
- 00bb929c bytes d09ae197
+ 00c35ce4 bytes fe32e097
~~~


<a id="compare-4b71cbc781f1dd1b3b341565f78e7025"></a>

### [`00bbb318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb318.md) → [`00c37d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d60.md) FUN_00c37d60

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bbb32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb318.md#insn-00bbb32c)
- 新版 [`00c37d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37d60.md#insn-00c37d74)

~~~diff
- 00bbb32c ["INT_ADD", "register:40f0:8", ["const:bbb32c:8", "const:4:8"]]
- 00bbb32c ["CALL", null, ["callee:00c5ea50:8"]]
+ 00c37d74 ["INT_ADD", "register:40f0:8", ["const:c37d74:8", "const:4:8"]]
+ 00c37d74 ["CALL", null, ["callee:00c5ea50:8"]]
- 00bbb32c bytes d99a0094
+ 00c37d74 bytes 379b0094
~~~


<a id="compare-3a2dd1654d1b2144f1c0255cd21d425d"></a>

### [`00bc140c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc140c.md) → [`00c3de54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3de54.md) FUN_00c3de54

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc145c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc140c.md#insn-00bc145c) · [`00bc1478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc140c.md#insn-00bc1478) · [`00bc149c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc140c.md#insn-00bc149c)
- 新版 [`00c3dea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3de54.md#insn-00c3dea4) · [`00c3dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3de54.md#insn-00c3dec0) · [`00c3dee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3de54.md#insn-00c3dee4)

~~~diff
- 00bc145c ["INT_ADD", "register:40f0:8", ["const:bc145c:8", "const:4:8"]]
- 00bc145c ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c3dea4 ["INT_ADD", "register:40f0:8", ["const:c3dea4:8", "const:4:8"]]
+ 00c3dea4 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bc145c bytes 7d6f0094
+ 00c3dea4 bytes 7f6f0094
- 00bc1478 ["INT_ADD", "register:40f0:8", ["const:bc1478:8", "const:4:8"]]
- 00bc1478 ["CALL", null, ["callee:00c57c00:8"]]
+ 00c3dec0 ["INT_ADD", "register:40f0:8", ["const:c3dec0:8", "const:4:8"]]
+ 00c3dec0 ["CALL", null, ["callee:00c57c00:8"]]
- 00bc1478 bytes 4e670094
+ 00c3dec0 bytes 50670094
- 00bc149c ["INT_ADD", "register:40f0:8", ["const:bc149c:8", "const:4:8"]]
- 00bc149c ["CALL", null, ["callee:00c5ad40:8"]]
+ 00c3dee4 ["INT_ADD", "register:40f0:8", ["const:c3dee4:8", "const:4:8"]]
+ 00c3dee4 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bc149c bytes 89730094
+ 00c3dee4 bytes 97730094
~~~


<a id="compare-c9c20995592ffb58d5aec4589ac91259"></a>

### [`00bc14b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc14b8.md) → [`00c3df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3df00.md) FUN_00c3df00

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc14ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc14b8.md#insn-00bc14ec) · [`00bc1510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc14b8.md#insn-00bc1510) · [`00bc155c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc14b8.md#insn-00bc155c)
- 新版 [`00c3df34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3df00.md#insn-00c3df34) · [`00c3df58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3df00.md#insn-00c3df58) · [`00c3dfa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3df00.md#insn-00c3dfa4)

~~~diff
- 00bc14ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc14ec ["INT_ADD", "register:40f0:8", ["const:bc14ec:8", "const:4:8"]]
- 00bc14ec ["CALLIND", null, ["register:0:8"]]
+ 00c3df34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3df34 ["INT_ADD", "register:40f0:8", ["const:c3df34:8", "const:4:8"]]
+ 00c3df34 ["CALLIND", null, ["register:0:8"]]
- 00bc14ec bytes 00013fd6
+ 00c3df34 bytes 00013fd6
- 00bc1510 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc1510 ["INT_ADD", "register:40f0:8", ["const:bc1510:8", "const:4:8"]]
- 00bc1510 ["CALLIND", null, ["register:0:8"]]
+ 00c3df58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3df58 ["INT_ADD", "register:40f0:8", ["const:c3df58:8", "const:4:8"]]
+ 00c3df58 ["CALLIND", null, ["register:0:8"]]
- 00bc1510 bytes 00013fd6
+ 00c3df58 bytes 00013fd6
- 00bc155c ["INT_ADD", "register:40f0:8", ["const:bc155c:8", "const:4:8"]]
- 00bc155c ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c3dfa4 ["INT_ADD", "register:40f0:8", ["const:c3dfa4:8", "const:4:8"]]
+ 00c3dfa4 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bc155c bytes 3d6f0094
+ 00c3dfa4 bytes 3f6f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf496c37a5fce11fc0f9113656c3765e"></a>

### [`00bc2c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2c84.md) → [`00c3f6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f6cc.md) FUN_00c3f6cc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2c84.md#insn-00bc2cd0)
- 新版 [`00c3f718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f6cc.md#insn-00c3f718)

~~~diff
- 00bc2cd0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bc2cd0 ["INT_ADD", "register:40f0:8", ["const:bc2cd0:8", "const:4:8"]]
- 00bc2cd0 ["CALLIND", null, ["register:0:8"]]
+ 00c3f718 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3f718 ["INT_ADD", "register:40f0:8", ["const:c3f718:8", "const:4:8"]]
+ 00c3f718 ["CALLIND", null, ["register:0:8"]]
- 00bc2cd0 bytes 20013fd6
+ 00c3f718 bytes 20013fd6
~~~


<a id="compare-f3943a2730d58eeaf8bb5a67a5553a18"></a>

### [`00bc2e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2e10.md) → [`00c3f858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f858.md) FUN_00c3f858

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2e10.md#insn-00bc2e44)
- 新版 [`00c3f88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f858.md#insn-00c3f88c)

~~~diff
- 00bc2e44 ["COPY", "register:0:8", ["register:4048:8"]]
- 00bc2e44 ["INT_ADD", "register:40f0:8", ["const:bc2e44:8", "const:4:8"]]
- 00bc2e44 ["CALLIND", null, ["register:0:8"]]
+ 00c3f88c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00c3f88c ["INT_ADD", "register:40f0:8", ["const:c3f88c:8", "const:4:8"]]
+ 00c3f88c ["CALLIND", null, ["register:0:8"]]
- 00bc2e44 bytes 20013fd6
+ 00c3f88c bytes 20013fd6
~~~


<a id="compare-3c637f2a01a7c2684a3ea1e6754f0f61"></a>

### [`00bc2e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2e64.md) → [`00c3f8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f8ac.md) FUN_00c3f8ac

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc2e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2e64.md#insn-00bc2e94)
- 新版 [`00c3f8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f8ac.md#insn-00c3f8dc)

~~~diff
- 00bc2e94 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bc2e94 ["INT_ADD", "register:40f0:8", ["const:bc2e94:8", "const:4:8"]]
- 00bc2e94 ["CALLIND", null, ["register:0:8"]]
+ 00c3f8dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c3f8dc ["INT_ADD", "register:40f0:8", ["const:c3f8dc:8", "const:4:8"]]
+ 00c3f8dc ["CALLIND", null, ["register:0:8"]]
- 00bc2e94 bytes 00013fd6
+ 00c3f8dc bytes 00013fd6
~~~


<a id="compare-a0b440b6fc2a36b45fcb29333c3613a7"></a>

### [`00bc91d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc91d8.md) → [`00c45c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45c20.md) FUN_00c45c20

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc922c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc91d8.md#insn-00bc922c) · [`00bc9248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc91d8.md#insn-00bc9248) · [`00bc928c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc91d8.md#insn-00bc928c)
- 新版 [`00c45c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45c20.md#insn-00c45c74) · [`00c45c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45c20.md#insn-00c45c90) · [`00c45cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45c20.md#insn-00c45cd4)

~~~diff
- 00bc922c ["INT_ADD", "register:40f0:8", ["const:bc922c:8", "const:4:8"]]
- 00bc922c ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c45c74 ["INT_ADD", "register:40f0:8", ["const:c45c74:8", "const:4:8"]]
+ 00c45c74 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bc922c bytes 09500094
+ 00c45c74 bytes 0b500094
- 00bc9248 ["INT_ADD", "register:40f0:8", ["const:bc9248:8", "const:4:8"]]
- 00bc9248 ["CALL", null, ["callee:00c57c00:8"]]
+ 00c45c90 ["INT_ADD", "register:40f0:8", ["const:c45c90:8", "const:4:8"]]
+ 00c45c90 ["CALL", null, ["callee:00c57c00:8"]]
- 00bc9248 bytes da470094
+ 00c45c90 bytes dc470094
- 00bc928c ["INT_ADD", "register:40f0:8", ["const:bc928c:8", "const:4:8"]]
- 00bc928c ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c45cd4 ["INT_ADD", "register:40f0:8", ["const:c45cd4:8", "const:4:8"]]
+ 00c45cd4 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bc928c bytes f14f0094
+ 00c45cd4 bytes f34f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e2ef191fed481378c81b1795a52c35c"></a>

### [`00bc9f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9f7c.md) → [`00c469c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c469c4.md) FUN_00c469c4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bc9fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9f7c.md#insn-00bc9fdc) · [`00bca034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9f7c.md#insn-00bca034) · [`00bca050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9f7c.md#insn-00bca050)
- 新版 [`00c46a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c469c4.md#insn-00c46a24) · [`00c46a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c469c4.md#insn-00c46a7c) · [`00c46a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c469c4.md#insn-00c46a98)

~~~diff
- 00bc9fdc ["INT_ADD", "register:40f0:8", ["const:bc9fdc:8", "const:4:8"]]
- 00bc9fdc ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c46a24 ["INT_ADD", "register:40f0:8", ["const:c46a24:8", "const:4:8"]]
+ 00c46a24 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bc9fdc bytes 9d4c0094
+ 00c46a24 bytes 9f4c0094
- 00bca034 ["INT_ADD", "register:40f0:8", ["const:bca034:8", "const:4:8"]]
- 00bca034 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c46a7c ["INT_ADD", "register:40f0:8", ["const:c46a7c:8", "const:4:8"]]
+ 00c46a7c ["CALL", null, ["callee:00c59ca0:8"]]
- 00bca034 bytes 874c0094
+ 00c46a7c bytes 894c0094
- 00bca050 ["INT_ADD", "register:40f0:8", ["const:bca050:8", "const:4:8"]]
- 00bca050 ["CALL", null, ["callee:00c57c00:8"]]
+ 00c46a98 ["INT_ADD", "register:40f0:8", ["const:c46a98:8", "const:4:8"]]
+ 00c46a98 ["CALL", null, ["callee:00c57c00:8"]]
- 00bca050 bytes 58440094
+ 00c46a98 bytes 5a440094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83b9a437f6a6e7486166a85781afa93b"></a>

### [`00bcb48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb48c.md) → [`00c47ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47ed4.md) FUN_00c47ed4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb48c.md#insn-00bcb4d4) · [`00bcb53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb48c.md#insn-00bcb53c) · [`00bcb558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb48c.md#insn-00bcb558)
- 新版 [`00c47f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47ed4.md#insn-00c47f1c) · [`00c47f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47ed4.md#insn-00c47f84) · [`00c47fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47ed4.md#insn-00c47fa0)

~~~diff
- 00bcb4d4 ["INT_ADD", "register:40f0:8", ["const:bcb4d4:8", "const:4:8"]]
- 00bcb4d4 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c47f1c ["INT_ADD", "register:40f0:8", ["const:c47f1c:8", "const:4:8"]]
+ 00c47f1c ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcb4d4 bytes 5f470094
+ 00c47f1c bytes 61470094
- 00bcb53c ["INT_ADD", "register:40f0:8", ["const:bcb53c:8", "const:4:8"]]
- 00bcb53c ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c47f84 ["INT_ADD", "register:40f0:8", ["const:c47f84:8", "const:4:8"]]
+ 00c47f84 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcb53c bytes 45470094
+ 00c47f84 bytes 47470094
- 00bcb558 ["INT_ADD", "register:40f0:8", ["const:bcb558:8", "const:4:8"]]
- 00bcb558 ["CALL", null, ["callee:00c57c00:8"]]
+ 00c47fa0 ["INT_ADD", "register:40f0:8", ["const:c47fa0:8", "const:4:8"]]
+ 00c47fa0 ["CALL", null, ["callee:00c57c00:8"]]
- 00bcb558 bytes 163f0094
+ 00c47fa0 bytes 183f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6521e501e8c6c08ba1f56ebbb929285d"></a>

### [`00bcbac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbac4.md) → [`00c4850c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md) FUN_00c4850c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbac4.md#insn-00bcbae8) · [`00bcbb0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbac4.md#insn-00bcbb0c) · [`00bcbb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbac4.md#insn-00bcbb48)
- 新版 [`00c48530`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md#insn-00c48530) · [`00c48554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md#insn-00c48554) · [`00c48590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4850c.md#insn-00c48590)

~~~diff
- 00bcbae8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbae8 ["INT_ADD", "register:40f0:8", ["const:bcbae8:8", "const:4:8"]]
- 00bcbae8 ["CALLIND", null, ["register:0:8"]]
+ 00c48530 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48530 ["INT_ADD", "register:40f0:8", ["const:c48530:8", "const:4:8"]]
+ 00c48530 ["CALLIND", null, ["register:0:8"]]
- 00bcbae8 bytes 00013fd6
+ 00c48530 bytes 00013fd6
- 00bcbb0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbb0c ["INT_ADD", "register:40f0:8", ["const:bcbb0c:8", "const:4:8"]]
- 00bcbb0c ["CALLIND", null, ["register:0:8"]]
+ 00c48554 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48554 ["INT_ADD", "register:40f0:8", ["const:c48554:8", "const:4:8"]]
+ 00c48554 ["CALLIND", null, ["register:0:8"]]
- 00bcbb0c bytes 00013fd6
+ 00c48554 bytes 00013fd6
- 00bcbb48 ["INT_ADD", "register:40f0:8", ["const:bcbb48:8", "const:4:8"]]
- 00bcbb48 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c48590 ["INT_ADD", "register:40f0:8", ["const:c48590:8", "const:4:8"]]
+ 00c48590 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcbb48 bytes c2450094
+ 00c48590 bytes c4450094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f5ecd0dd966f3b4f449bd1b7e94da81"></a>

### [`00bcbb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbb80.md) → [`00c485c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c485c8.md) FUN_00c485c8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbbac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbb80.md#insn-00bcbbac) · [`00bcbbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbb80.md#insn-00bcbbd0)
- 新版 [`00c485f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c485c8.md#insn-00c485f4) · [`00c48618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c485c8.md#insn-00c48618)

~~~diff
- 00bcbbac ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbbac ["INT_ADD", "register:40f0:8", ["const:bcbbac:8", "const:4:8"]]
- 00bcbbac ["CALLIND", null, ["register:0:8"]]
+ 00c485f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c485f4 ["INT_ADD", "register:40f0:8", ["const:c485f4:8", "const:4:8"]]
+ 00c485f4 ["CALLIND", null, ["register:0:8"]]
- 00bcbbac bytes 00013fd6
+ 00c485f4 bytes 00013fd6
- 00bcbbd0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbbd0 ["INT_ADD", "register:40f0:8", ["const:bcbbd0:8", "const:4:8"]]
- 00bcbbd0 ["CALLIND", null, ["register:0:8"]]
+ 00c48618 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48618 ["INT_ADD", "register:40f0:8", ["const:c48618:8", "const:4:8"]]
+ 00c48618 ["CALLIND", null, ["register:0:8"]]
- 00bcbbd0 bytes 00013fd6
+ 00c48618 bytes 00013fd6
~~~


<a id="compare-e51802357d99924b612ad0ee2d26b6f7"></a>

### [`00bcbe44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbe44.md) → [`00c4888c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4888c.md) FUN_00c4888c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcbe64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbe44.md#insn-00bcbe64) · [`00bcbe90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbe44.md#insn-00bcbe90) · [`00bcbed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbe44.md#insn-00bcbed0)
- 新版 [`00c488ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4888c.md#insn-00c488ac) · [`00c488d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4888c.md#insn-00c488d8) · [`00c48918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c4888c.md#insn-00c48918)

~~~diff
- 00bcbe64 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbe64 ["INT_ADD", "register:40f0:8", ["const:bcbe64:8", "const:4:8"]]
- 00bcbe64 ["CALLIND", null, ["register:0:8"]]
+ 00c488ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c488ac ["INT_ADD", "register:40f0:8", ["const:c488ac:8", "const:4:8"]]
+ 00c488ac ["CALLIND", null, ["register:0:8"]]
- 00bcbe64 bytes 00013fd6
+ 00c488ac bytes 00013fd6
- 00bcbe90 ["INT_ADD", "register:40f0:8", ["const:bcbe90:8", "const:4:8"]]
- 00bcbe90 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c488d8 ["INT_ADD", "register:40f0:8", ["const:c488d8:8", "const:4:8"]]
+ 00c488d8 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcbe90 bytes f0440094
+ 00c488d8 bytes f2440094
- 00bcbed0 ["INT_ADD", "register:40f0:8", ["const:bcbed0:8", "const:4:8"]]
- 00bcbed0 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00c48918 ["INT_ADD", "register:40f0:8", ["const:c48918:8", "const:4:8"]]
+ 00c48918 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bcbed0 bytes fc480094
+ 00c48918 bytes 0a490094
~~~


<a id="compare-20bf602c7217fe67d1a57253db640410"></a>

### [`00bcebcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcebcc.md) → [`00c4b614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b614.md) FUN_00c4b614

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcebf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcebcc.md#insn-00bcebf8) · [`00bcec1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcebcc.md#insn-00bcec1c) · [`00bcec48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcebcc.md#insn-00bcec48)
- 新版 [`00c4b640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b614.md#insn-00c4b640) · [`00c4b664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b614.md#insn-00c4b664) · [`00c4b690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b614.md#insn-00c4b690)

~~~diff
- 00bcebf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcebf8 ["INT_ADD", "register:40f0:8", ["const:bcebf8:8", "const:4:8"]]
- 00bcebf8 ["CALLIND", null, ["register:0:8"]]
+ 00c4b640 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b640 ["INT_ADD", "register:40f0:8", ["const:c4b640:8", "const:4:8"]]
+ 00c4b640 ["CALLIND", null, ["register:0:8"]]
- 00bcebf8 bytes 00013fd6
+ 00c4b640 bytes 00013fd6
- 00bcec1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcec1c ["INT_ADD", "register:40f0:8", ["const:bcec1c:8", "const:4:8"]]
- 00bcec1c ["CALLIND", null, ["register:0:8"]]
+ 00c4b664 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4b664 ["INT_ADD", "register:40f0:8", ["const:c4b664:8", "const:4:8"]]
+ 00c4b664 ["CALLIND", null, ["register:0:8"]]
- 00bcec1c bytes 00013fd6
+ 00c4b664 bytes 00013fd6
- 00bcec48 ["INT_ADD", "register:40f0:8", ["const:bcec48:8", "const:4:8"]]
- 00bcec48 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c4b690 ["INT_ADD", "register:40f0:8", ["const:c4b690:8", "const:4:8"]]
+ 00c4b690 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcec48 bytes 82390094
+ 00c4b690 bytes 84390094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62af02b0ccffb7e045e47c9aa1dbe042"></a>

### [`00bcf06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf06c.md) → [`00c4bab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bab4.md) FUN_00c4bab4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf06c.md#insn-00bcf0b4) · [`00bcf0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf06c.md#insn-00bcf0fc)
- 新版 [`00c4bafc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bab4.md#insn-00c4bafc) · [`00c4bb44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bab4.md#insn-00c4bb44)

~~~diff
- 00bcf0b4 ["INT_ADD", "register:40f0:8", ["const:bcf0b4:8", "const:4:8"]]
- 00bcf0b4 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c4bafc ["INT_ADD", "register:40f0:8", ["const:c4bafc:8", "const:4:8"]]
+ 00c4bafc ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcf0b4 bytes 67380094
+ 00c4bafc bytes 69380094
- 00bcf0fc ["INT_ADD", "register:40f0:8", ["const:bcf0fc:8", "const:4:8"]]
- 00bcf0fc ["CALL", null, ["callee:00c5ad40:8"]]
+ 00c4bb44 ["INT_ADD", "register:40f0:8", ["const:c4bb44:8", "const:4:8"]]
+ 00c4bb44 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bcf0fc bytes 713c0094
+ 00c4bb44 bytes 7f3c0094
~~~


<a id="compare-b11a2757597b2c7fef2923414b270d1c"></a>

### [`00bcf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf9d0.md) → [`00c4c418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c418.md) FUN_00c4c418

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bcf3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf3b8.md) · 呼出先 1件 [`00bc12ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc12ec.md)
- 新版 呼出元 1件 [`00c4be00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4be00.md) · 呼出先 1件 [`00c3dd34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3dd34.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcf9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf9d0.md#insn-00bcf9ec)
- 新版 [`00c4c434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c418.md#insn-00c4c434)

~~~diff
- 00bcf9ec ["INT_ADD", "register:40f0:8", ["const:bcf9ec:8", "const:4:8"]]
- 00bcf9ec ["CALL", null, ["callee:00c3dd34:8"]]
+ 00c4c434 ["INT_ADD", "register:40f0:8", ["const:c4c434:8", "const:4:8"]]
+ 00c4c434 ["CALL", null, ["callee:00c3dd34:8"]]
- 00bcf9ec bytes 40c6ff97
+ 00c4c434 bytes 40c6ff97
~~~


<a id="compare-fec9d738e30216072e0804420dc77c9c"></a>

### [`00bd0a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0a54.md) → [`00c4d49c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d49c.md) FUN_00c4d49c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0a54.md#insn-00bd0a98) · [`00bd0ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0a54.md#insn-00bd0ae4) · [`00bd0b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0a54.md#insn-00bd0b28)
- 新版 [`00c4d4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d49c.md#insn-00c4d4e0) · [`00c4d52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d49c.md#insn-00c4d52c) · [`00c4d570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d49c.md#insn-00c4d570)

~~~diff
- 00bd0a98 ["INT_ADD", "register:40f0:8", ["const:bd0a98:8", "const:4:8"]]
- 00bd0a98 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c4d4e0 ["INT_ADD", "register:40f0:8", ["const:c4d4e0:8", "const:4:8"]]
+ 00c4d4e0 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bd0a98 bytes ee310094
+ 00c4d4e0 bytes f0310094
- 00bd0ae4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0ae4 ["INT_ADD", "register:40f0:8", ["const:bd0ae4:8", "const:4:8"]]
- 00bd0ae4 ["CALLIND", null, ["register:0:8"]]
+ 00c4d52c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d52c ["INT_ADD", "register:40f0:8", ["const:c4d52c:8", "const:4:8"]]
+ 00c4d52c ["CALLIND", null, ["register:0:8"]]
- 00bd0ae4 bytes 00013fd6
+ 00c4d52c bytes 00013fd6
- 00bd0b28 ["INT_ADD", "register:40f0:8", ["const:bd0b28:8", "const:4:8"]]
- 00bd0b28 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00c4d570 ["INT_ADD", "register:40f0:8", ["const:c4d570:8", "const:4:8"]]
+ 00c4d570 ["CALL", null, ["callee:00c5ad40:8"]]
- 00bd0b28 bytes e6350094
+ 00c4d570 bytes f4350094
~~~


<a id="compare-45eee46a9a6f737b2f9ad484b8b88743"></a>

### [`00bd0b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0b4c.md) → [`00c4d594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d594.md) FUN_00c4d594

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd0b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0b4c.md#insn-00bd0b78) · [`00bd0b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0b4c.md#insn-00bd0b9c) · [`00bd0bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0b4c.md#insn-00bd0bd8)
- 新版 [`00c4d5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d594.md#insn-00c4d5c0) · [`00c4d5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d594.md#insn-00c4d5e4) · [`00c4d620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d594.md#insn-00c4d620)

~~~diff
- 00bd0b78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0b78 ["INT_ADD", "register:40f0:8", ["const:bd0b78:8", "const:4:8"]]
- 00bd0b78 ["CALLIND", null, ["register:0:8"]]
+ 00c4d5c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d5c0 ["INT_ADD", "register:40f0:8", ["const:c4d5c0:8", "const:4:8"]]
+ 00c4d5c0 ["CALLIND", null, ["register:0:8"]]
- 00bd0b78 bytes 00013fd6
+ 00c4d5c0 bytes 00013fd6
- 00bd0b9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd0b9c ["INT_ADD", "register:40f0:8", ["const:bd0b9c:8", "const:4:8"]]
- 00bd0b9c ["CALLIND", null, ["register:0:8"]]
+ 00c4d5e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4d5e4 ["INT_ADD", "register:40f0:8", ["const:c4d5e4:8", "const:4:8"]]
+ 00c4d5e4 ["CALLIND", null, ["register:0:8"]]
- 00bd0b9c bytes 00013fd6
+ 00c4d5e4 bytes 00013fd6
- 00bd0bd8 ["INT_ADD", "register:40f0:8", ["const:bd0bd8:8", "const:4:8"]]
- 00bd0bd8 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c4d620 ["INT_ADD", "register:40f0:8", ["const:c4d620:8", "const:4:8"]]
+ 00c4d620 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bd0bd8 bytes 9e310094
+ 00c4d620 bytes a0310094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13c23c9c8b0ee115d9654313975657ea"></a>

### [`00bd42ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd42ac.md) → [`00c50cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50cf4.md) FUN_00c50cf4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd42e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd42ac.md#insn-00bd42e8) · [`00bd4318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd42ac.md#insn-00bd4318) · [`00bd4348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd42ac.md#insn-00bd4348)
- 新版 [`00c50d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50cf4.md#insn-00c50d30) · [`00c50d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50cf4.md#insn-00c50d60) · [`00c50d90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50cf4.md#insn-00c50d90)

~~~diff
- 00bd42e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd42e8 ["INT_ADD", "register:40f0:8", ["const:bd42e8:8", "const:4:8"]]
- 00bd42e8 ["CALLIND", null, ["register:0:8"]]
+ 00c50d30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50d30 ["INT_ADD", "register:40f0:8", ["const:c50d30:8", "const:4:8"]]
+ 00c50d30 ["CALLIND", null, ["register:0:8"]]
- 00bd42e8 bytes 00013fd6
+ 00c50d30 bytes 00013fd6
- 00bd4318 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd4318 ["INT_ADD", "register:40f0:8", ["const:bd4318:8", "const:4:8"]]
- 00bd4318 ["CALLIND", null, ["register:0:8"]]
+ 00c50d60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50d60 ["INT_ADD", "register:40f0:8", ["const:c50d60:8", "const:4:8"]]
+ 00c50d60 ["CALLIND", null, ["register:0:8"]]
- 00bd4318 bytes 00013fd6
+ 00c50d60 bytes 00013fd6
- 00bd4348 ["INT_ADD", "register:40f0:8", ["const:bd4348:8", "const:4:8"]]
- 00bd4348 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c50d90 ["INT_ADD", "register:40f0:8", ["const:c50d90:8", "const:4:8"]]
+ 00c50d90 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bd4348 bytes c2230094
+ 00c50d90 bytes c4230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da6faabc4095a449b276b78d9988f6ef"></a>

### [`00bd4398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4398.md) → [`00c50de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50de0.md) FUN_00c50de0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd43ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4398.md#insn-00bd43ec) · [`00bd4408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4398.md#insn-00bd4408) · [`00bd4440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4398.md#insn-00bd4440)
- 新版 [`00c50e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50de0.md#insn-00c50e34) · [`00c50e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50de0.md#insn-00c50e50) · [`00c50e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50de0.md#insn-00c50e88)

~~~diff
- 00bd43ec ["INT_ADD", "register:40f0:8", ["const:bd43ec:8", "const:4:8"]]
- 00bd43ec ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c50e34 ["INT_ADD", "register:40f0:8", ["const:c50e34:8", "const:4:8"]]
+ 00c50e34 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bd43ec bytes 99230094
+ 00c50e34 bytes 9b230094
- 00bd4408 ["INT_ADD", "register:40f0:8", ["const:bd4408:8", "const:4:8"]]
- 00bd4408 ["CALL", null, ["callee:00c57c00:8"]]
+ 00c50e50 ["INT_ADD", "register:40f0:8", ["const:c50e50:8", "const:4:8"]]
+ 00c50e50 ["CALL", null, ["callee:00c57c00:8"]]
- 00bd4408 bytes 6a1b0094
+ 00c50e50 bytes 6c1b0094
- 00bd4440 ["INT_ADD", "register:40f0:8", ["const:bd4440:8", "const:4:8"]]
- 00bd4440 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c50e88 ["INT_ADD", "register:40f0:8", ["const:c50e88:8", "const:4:8"]]
+ 00c50e88 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bd4440 bytes 84230094
+ 00c50e88 bytes 86230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-369754b92ead7d9f93f4c24821b05629"></a>

### [`00bd4eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4eb0.md) → [`00c518f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c518f8.md) _ZnwmRKSt9nothrow_t

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdda00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda00.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00c5a450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a450.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4eb0.md#insn-00bd4ebc)
- 新版 [`00c51904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c518f8.md#insn-00c51904)

~~~diff
- 00bd4ebc ["INT_ADD", "register:40f0:8", ["const:bd4ebc:8", "const:4:8"]]
- 00bd4ebc ["CALL", null, ["callee:00c57a90:8"]]
+ 00c51904 ["INT_ADD", "register:40f0:8", ["const:c51904:8", "const:4:8"]]
+ 00c51904 ["CALL", null, ["callee:00c57a90:8"]]
- 00bd4ebc bytes 61180094
+ 00c51904 bytes 63180094
~~~


<a id="compare-d672606518de3e802e70fd59bc352b6d"></a>

### [`00bd4f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4f40.md) → [`00c51988`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51988.md) _ZnwmSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eac0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4f40.md#insn-00bd4f4c)
- 新版 [`00c51994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51988.md#insn-00c51994)

~~~diff
- 00bd4f4c ["INT_ADD", "register:40f0:8", ["const:bd4f4c:8", "const:4:8"]]
- 00bd4f4c ["CALL", null, ["callee:00c5eac0:8"]]
+ 00c51994 ["INT_ADD", "register:40f0:8", ["const:c51994:8", "const:4:8"]]
+ 00c51994 ["CALL", null, ["callee:00c5eac0:8"]]
- 00bd4f4c bytes ed330094
+ 00c51994 bytes 4b340094
~~~


<a id="compare-e3ffa604dd8c285bd60cea8008f2f4c1"></a>

### [`00bd4f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4f70.md) → [`00c519b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c519b8.md) _ZnamSt11align_val_tRKSt9nothrow_t

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4f70.md#insn-00bd4f7c)
- 新版 [`00c519c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c519b8.md#insn-00c519c4)

~~~diff
- 00bd4f7c ["INT_ADD", "register:40f0:8", ["const:bd4f7c:8", "const:4:8"]]
- 00bd4f7c ["CALL", null, ["callee:00c5eae0:8"]]
+ 00c519c4 ["INT_ADD", "register:40f0:8", ["const:c519c4:8", "const:4:8"]]
+ 00c519c4 ["CALL", null, ["callee:00c5eae0:8"]]
- 00bd4f7c bytes e9330094
+ 00c519c4 bytes 47340094
~~~


<a id="compare-84a352748e2a83288c351f947a89ca5a"></a>

### [`00bd577c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd577c.md) → [`00c521c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c521c4.md) __cxa_uncaught_exception

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd577c.md#insn-00bd5788)
- 新版 [`00c521d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c521c4.md#insn-00c521d0)

~~~diff
- 00bd5788 ["INT_ADD", "register:40f0:8", ["const:bd5788:8", "const:4:8"]]
- 00bd5788 ["CALL", null, ["callee:00c5e9a0:8"]]
+ 00c521d0 ["INT_ADD", "register:40f0:8", ["const:c521d0:8", "const:4:8"]]
+ 00c521d0 ["CALL", null, ["callee:00c5e9a0:8"]]
- 00bd5788 bytes 96310094
+ 00c521d0 bytes f4310094
~~~


<a id="compare-31fc52a66c1b7efd1e2bbfcbcaea2384"></a>

### [`00bd57ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57ac.md) → [`00c521f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c521f4.md) __cxa_uncaught_exceptions

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be0f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f00.md) · 呼出先 1件 [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)
- 新版 呼出元 1件 [`00c5db00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db00.md) · 呼出先 1件 [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd57b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57ac.md#insn-00bd57b8)
- 新版 [`00c52200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c521f4.md#insn-00c52200)

~~~diff
- 00bd57b8 ["INT_ADD", "register:40f0:8", ["const:bd57b8:8", "const:4:8"]]
- 00bd57b8 ["CALL", null, ["callee:00c5e9a0:8"]]
+ 00c52200 ["INT_ADD", "register:40f0:8", ["const:c52200:8", "const:4:8"]]
+ 00c52200 ["CALL", null, ["callee:00c5e9a0:8"]]
- 00bd57b8 bytes 8a310094
+ 00c52200 bytes e8310094
~~~


<a id="compare-902d008a885af03c008467819bd03142"></a>

### [`00bd57d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md) → [`00c5221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md) FUN_00c5221c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`00bd5008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5008.md) [`00bd51f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd51f0.md) [`00bd55e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd55e8.md) · 呼出先 2件 [`00bd5820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5820.md) [`00be1f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f10.md)
- 新版 呼出元 3件 [`00c51a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a50.md) [`00c51c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c38.md) [`00c52030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52030.md) · 呼出先 2件 [`00c52268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52268.md) [`00c5ead0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ead0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd57fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md#insn-00bd57fc) · [`00bd580c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md#insn-00bd580c)
- 新版 [`00c52244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md#insn-00c52244) · [`00c52254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md#insn-00c52254)

~~~diff
- 00bd57fc ["INT_ADD", "register:40f0:8", ["const:bd57fc:8", "const:4:8"]]
- 00bd57fc ["CALL", null, ["callee:00c5ead0:8"]]
+ 00c52244 ["INT_ADD", "register:40f0:8", ["const:c52244:8", "const:4:8"]]
+ 00c52244 ["CALL", null, ["callee:00c5ead0:8"]]
- 00bd57fc bytes c5310094
+ 00c52244 bytes 23320094
- 00bd580c ["INT_ADD", "register:40f0:8", ["const:bd580c:8", "const:4:8"]]
- 00bd580c ["CALL", null, ["callee:00c52268:8"]]
+ 00c52254 ["INT_ADD", "register:40f0:8", ["const:c52254:8", "const:4:8"]]
+ 00c52254 ["CALL", null, ["callee:00c52268:8"]]
- 00bd580c bytes 05000094
+ 00c52254 bytes 05000094
~~~


<a id="compare-64cb8955182c894c42ff3c1612831aed"></a>

### [`00bd7264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7264.md) → [`00c53cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53cb4.md) FUN_00c53cb4

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) · 呼出先 1件 [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md)
- 新版 呼出元 1件 [`00c52520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md) · 呼出先 1件 [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7264.md#insn-00bd7278)
- 新版 [`00c53cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53cb4.md#insn-00c53cc8)

~~~diff
- 00bd7278 ["INT_ADD", "register:40f0:8", ["const:bd7278:8", "const:4:8"]]
- 00bd7278 ["CALL", null, ["callee:00c53fb8:8"]]
+ 00c53cc8 ["INT_ADD", "register:40f0:8", ["const:c53cc8:8", "const:4:8"]]
+ 00c53cc8 ["CALL", null, ["callee:00c53fb8:8"]]
- 00bd7278 bytes bc000094
+ 00c53cc8 bytes bc000094
~~~


<a id="compare-a7be7afab29db27d20487d8b0a05c3c1"></a>

### [`00bd7298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7298.md) → [`00c53ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ce8.md) FUN_00c53ce8

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) · 呼出先 1件 [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md)
- 新版 呼出元 1件 [`00c52520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md) · 呼出先 1件 [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd72ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7298.md#insn-00bd72ac)
- 新版 [`00c53cfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ce8.md#insn-00c53cfc)

~~~diff
- 00bd72ac ["INT_ADD", "register:40f0:8", ["const:bd72ac:8", "const:4:8"]]
- 00bd72ac ["CALL", null, ["callee:00c53fb8:8"]]
+ 00c53cfc ["INT_ADD", "register:40f0:8", ["const:c53cfc:8", "const:4:8"]]
+ 00c53cfc ["CALL", null, ["callee:00c53fb8:8"]]
- 00bd72ac bytes af000094
+ 00c53cfc bytes af000094
~~~


<a id="compare-5bb052f0a030426b7011b10a49e2843c"></a>

### [`00bd72f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd72f0.md) → [`00c53d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d40.md) FUN_00c53d40

採用 · 移動量 `+0x7ca50` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) · 呼出先 1件 [`00bd73d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md)
- 新版 呼出元 1件 [`00c52520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md) · 呼出先 1件 [`00c53e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd72f0.md#insn-00bd7308)
- 新版 [`00c53d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d40.md#insn-00c53d58)

~~~diff
- 00bd7308 ["INT_ADD", "register:40f0:8", ["const:bd7308:8", "const:4:8"]]
- 00bd7308 ["CALL", null, ["callee:00c53e28:8"]]
+ 00c53d58 ["INT_ADD", "register:40f0:8", ["const:c53d58:8", "const:4:8"]]
+ 00c53d58 ["CALL", null, ["callee:00c53e28:8"]]
- 00bd7308 bytes 34000094
+ 00c53d58 bytes 34000094
~~~


<a id="compare-8db14e5728ba2d2cb6adf9d1c80ca069"></a>

### [`00bd73d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md) → [`00c53e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md) FUN_00c53e28

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd72f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd72f0.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d40.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md#insn-00bd7400) · [`00bd7418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md#insn-00bd7418)
- 新版 [`00c53e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md#insn-00c53e50) · [`00c53e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md#insn-00c53e68)

~~~diff
- 00bd7400 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7400 ["INT_ADD", "register:40f0:8", ["const:bd7400:8", "const:4:8"]]
- 00bd7400 ["CALLIND", null, ["register:0:8"]]
+ 00c53e50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c53e50 ["INT_ADD", "register:40f0:8", ["const:c53e50:8", "const:4:8"]]
+ 00c53e50 ["CALLIND", null, ["register:0:8"]]
- 00bd7400 bytes 00013fd6
+ 00c53e50 bytes 00013fd6
- 00bd7418 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7418 ["INT_ADD", "register:40f0:8", ["const:bd7418:8", "const:4:8"]]
- 00bd7418 ["CALLIND", null, ["register:0:8"]]
+ 00c53e68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c53e68 ["INT_ADD", "register:40f0:8", ["const:c53e68:8", "const:4:8"]]
+ 00c53e68 ["CALLIND", null, ["register:0:8"]]
- 00bd7418 bytes 00013fd6
+ 00c53e68 bytes 00013fd6
~~~


<a id="compare-c5c0d0bc4896cbad7c992f416c81c831"></a>

### [`00bd7454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7454.md) → [`00c53ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ea4.md) FUN_00c53ea4

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bd72e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd72e8.md) [`00bd7320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7320.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00c53d38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d38.md) [`00c53d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d70.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7454.md#insn-00bd7480) · [`00bd749c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7454.md#insn-00bd749c) · [`00bd74b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7454.md#insn-00bd74b8)
- 新版 [`00c53ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ea4.md#insn-00c53ed0) · [`00c53eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ea4.md#insn-00c53eec) · [`00c53f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ea4.md#insn-00c53f08)

~~~diff
- 00bd7480 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7480 ["INT_ADD", "register:40f0:8", ["const:bd7480:8", "const:4:8"]]
- 00bd7480 ["CALLIND", null, ["register:0:8"]]
+ 00c53ed0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c53ed0 ["INT_ADD", "register:40f0:8", ["const:c53ed0:8", "const:4:8"]]
+ 00c53ed0 ["CALLIND", null, ["register:0:8"]]
- 00bd7480 bytes 00013fd6
+ 00c53ed0 bytes 00013fd6
- 00bd749c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd749c ["INT_ADD", "register:40f0:8", ["const:bd749c:8", "const:4:8"]]
- 00bd749c ["CALLIND", null, ["register:0:8"]]
+ 00c53eec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c53eec ["INT_ADD", "register:40f0:8", ["const:c53eec:8", "const:4:8"]]
+ 00c53eec ["CALLIND", null, ["register:0:8"]]
- 00bd749c bytes 00013fd6
+ 00c53eec bytes 00013fd6
- 00bd74b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd74b8 ["INT_ADD", "register:40f0:8", ["const:bd74b8:8", "const:4:8"]]
- 00bd74b8 ["CALLIND", null, ["register:0:8"]]
+ 00c53f08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c53f08 ["INT_ADD", "register:40f0:8", ["const:c53f08:8", "const:4:8"]]
+ 00c53f08 ["CALLIND", null, ["register:0:8"]]
- 00bd74b8 bytes 00013fd6
+ 00c53f08 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1207d8a8a2aa3fda6871f9883fe7bea8"></a>

### [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md) → [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md) FUN_00c53fb8

採用 · 移動量 `+0x7ca50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md) [`00bd7264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7264.md) [`00bd7298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7298.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md) [`00c53cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53cb4.md) [`00c53ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ce8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md#insn-00bd7584)
- 新版 [`00c53fd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md#insn-00c53fd4)

~~~diff
- 00bd7584 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7584 ["INT_ADD", "register:40f0:8", ["const:bd7584:8", "const:4:8"]]
- 00bd7584 ["CALLIND", null, ["register:0:8"]]
+ 00c53fd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c53fd4 ["INT_ADD", "register:40f0:8", ["const:c53fd4:8", "const:4:8"]]
+ 00c53fd4 ["CALLIND", null, ["register:0:8"]]
- 00bd7584 bytes 00013fd6
+ 00c53fd4 bytes 00013fd6
~~~


<a id="compare-de04190d9610f1876c787b2e4d2eaeee"></a>

### [`00bd75a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75a8.md) → [`00c53ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ff8.md) FUN_00c53ff8

採用 · 移動量 `+0x7ca50` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd75bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75a8.md#insn-00bd75bc)
- 新版 [`00c5400c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ff8.md#insn-00c5400c)

~~~diff
- 00bd75bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd75bc ["INT_ADD", "register:40f0:8", ["const:bd75bc:8", "const:4:8"]]
- 00bd75bc ["CALLIND", null, ["register:0:8"]]
+ 00c5400c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c5400c ["INT_ADD", "register:40f0:8", ["const:c5400c:8", "const:4:8"]]
+ 00c5400c ["CALLIND", null, ["register:0:8"]]
- 00bd75bc bytes 00013fd6
+ 00c5400c bytes 00013fd6
~~~


