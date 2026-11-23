# v15.7.4 → v16.0.0 · 要調査の変更候補 (6)

[一覧の目次](README.md)

<a id="compare-4018ff6253f5baf3f39e8d297573dacd"></a>

### [`00492380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492380.md) → [`004b5218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5218.md) _ZN5Botan11OctetStringeOERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00492434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492380.md#insn-00492434)
- 新版 `004b52cc`（命令位置の公開資料なし）

~~~diff
- 00492434 ["INT_ADD", "register:40f0:8", ["const:492434:8", "const:4:8"]]
- 00492434 ["CALL", null, ["callee:00c57c90:8"]]
+ 004b52cc ["INT_ADD", "register:40f0:8", ["const:4b52cc:8", "const:4:8"]]
+ 004b52cc ["CALL", null, ["callee:00c57c90:8"]]
- 00492434 bytes 83231d94
+ 004b52cc bytes 718a1e94
~~~


<a id="compare-e581b09b32ec10ee2807b17b5cbfe188"></a>

### [`004925cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/004925cc.md) → [`004b5464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b5/004b5464.md) _ZN5BotanneERKNS_11OctetStringES2_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdbd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c587b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004925d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/004925cc.md#insn-004925d4)
- 新版 `004b546c`（命令位置の公開資料なし）

~~~diff
- 004925d4 ["INT_ADD", "register:40f0:8", ["const:4925d4:8", "const:4:8"]]
- 004925d4 ["CALL", null, ["callee:00c587b0:8"]]
+ 004b546c ["INT_ADD", "register:40f0:8", ["const:4b546c:8", "const:4:8"]]
+ 004b546c ["CALL", null, ["callee:00c587b0:8"]]
- 004925d4 bytes e3251d94
+ 004b546c bytes d18c1e94
~~~


<a id="compare-caebb604f399c67c64b72a0f033b00ef"></a>

### [`00493288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493288.md) → [`004b6120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b6120.md) _ZN5Botan13base64_decodeEPKcmb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdbda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbda0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c587f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004932cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493288.md#insn-004932cc) · [`004932e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493288.md#insn-004932e0) · [`004932f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493288.md#insn-004932f8)
- 新版 `004b6164`（命令位置の公開資料なし） · `004b6178`（命令位置の公開資料なし） · `004b6190`（命令位置の公開資料なし）

~~~diff
- 004932cc ["INT_ADD", "register:40f0:8", ["const:4932cc:8", "const:4:8"]]
- 004932cc ["CALL", null, ["callee:004b34c8:8"]]
+ 004b6164 ["INT_ADD", "register:40f0:8", ["const:4b6164:8", "const:4:8"]]
+ 004b6164 ["CALL", null, ["callee:004b34c8:8"]]
- 004932cc bytes d9f4ff97
+ 004b6164 bytes d9f4ff97
- 004932e0 ["INT_ADD", "register:40f0:8", ["const:4932e0:8", "const:4:8"]]
- 004932e0 ["CALL", null, ["callee:00c587f0:8"]]
+ 004b6178 ["INT_ADD", "register:40f0:8", ["const:4b6178:8", "const:4:8"]]
+ 004b6178 ["CALL", null, ["callee:00c587f0:8"]]
- 004932e0 bytes b0221d94
+ 004b6178 bytes 9e891e94
- 004932f8 ["INT_ADD", "register:40f0:8", ["const:4932f8:8", "const:4:8"]]
- 004932f8 ["CALL", null, ["callee:005404ac:8"]]
+ 004b6190 ["INT_ADD", "register:40f0:8", ["const:4b6190:8", "const:4:8"]]
+ 004b6190 ["CALL", null, ["callee:005404ac:8"]]
- 004932f8 bytes c7280294
+ 004b6190 bytes c7280294
~~~


<a id="compare-ac7216cd24a611b68fdbe19ea7d42ff1"></a>

### [`00493354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493354.md) → [`004b61ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b6/004b61ec.md) _ZN5Botan13base64_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdb0.md) · 呼出先 3件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdbda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbda0.md)
- 新版 呼出元 1件 [`00c58800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58800.md) · 呼出先 3件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c587f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c587f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004933a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493354.md#insn-004933a8) · [`004933bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493354.md#insn-004933bc) · [`004933d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493354.md#insn-004933d4)
- 新版 `004b6240`（命令位置の公開資料なし） · `004b6254`（命令位置の公開資料なし） · `004b626c`（命令位置の公開資料なし）

~~~diff
- 004933a8 ["INT_ADD", "register:40f0:8", ["const:4933a8:8", "const:4:8"]]
- 004933a8 ["CALL", null, ["callee:004b34c8:8"]]
+ 004b6240 ["INT_ADD", "register:40f0:8", ["const:4b6240:8", "const:4:8"]]
+ 004b6240 ["CALL", null, ["callee:004b34c8:8"]]
- 004933a8 bytes a2f4ff97
+ 004b6240 bytes a2f4ff97
- 004933bc ["INT_ADD", "register:40f0:8", ["const:4933bc:8", "const:4:8"]]
- 004933bc ["CALL", null, ["callee:00c587f0:8"]]
+ 004b6254 ["INT_ADD", "register:40f0:8", ["const:4b6254:8", "const:4:8"]]
+ 004b6254 ["CALL", null, ["callee:00c587f0:8"]]
- 004933bc bytes 79221d94
+ 004b6254 bytes 67891e94
- 004933d4 ["INT_ADD", "register:40f0:8", ["const:4933d4:8", "const:4:8"]]
- 004933d4 ["CALL", null, ["callee:005404ac:8"]]
+ 004b626c ["INT_ADD", "register:40f0:8", ["const:4b626c:8", "const:4:8"]]
+ 004b626c ["CALL", null, ["callee:005404ac:8"]]
- 004933d4 bytes 90280294
+ 004b626c bytes 90280294
~~~


<a id="compare-3f3e9683264c40e24314c0a00319807d"></a>

### [`00494544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494544.md) → [`004b73dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b73dc.md) _ZN5Botan6BigInt13encode_lockedERKS0_NS0_4BaseE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdbaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbaf0.md) [`00bdbb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb00.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c58540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58540.md) [`00c58550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58550.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494544.md#insn-00494560) · [`0049456c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494544.md#insn-0049456c) · [`0049457c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494544.md#insn-0049457c)
- 新版 `004b73f8`（命令位置の公開資料なし） · `004b7404`（命令位置の公開資料なし） · `004b7414`（命令位置の公開資料なし）

~~~diff
- 00494560 ["INT_ADD", "register:40f0:8", ["const:494560:8", "const:4:8"]]
- 00494560 ["CALL", null, ["callee:00c58540:8"]]
+ 004b73f8 ["INT_ADD", "register:40f0:8", ["const:4b73f8:8", "const:4:8"]]
+ 004b73f8 ["CALL", null, ["callee:00c58540:8"]]
- 00494560 bytes 641d1d94
+ 004b73f8 bytes 52841e94
- 0049456c ["INT_ADD", "register:40f0:8", ["const:49456c:8", "const:4:8"]]
- 0049456c ["CALL", null, ["callee:004b34c8:8"]]
+ 004b7404 ["INT_ADD", "register:40f0:8", ["const:4b7404:8", "const:4:8"]]
+ 004b7404 ["CALL", null, ["callee:004b34c8:8"]]
- 0049456c bytes 31f0ff97
+ 004b7404 bytes 31f0ff97
- 0049457c ["INT_ADD", "register:40f0:8", ["const:49457c:8", "const:4:8"]]
- 0049457c ["CALL", null, ["callee:00c58550:8"]]
+ 004b7414 ["INT_ADD", "register:40f0:8", ["const:4b7414:8", "const:4:8"]]
+ 004b7414 ["CALL", null, ["callee:00c58550:8"]]
- 0049457c bytes 611d1d94
+ 004b7414 bytes 4f841e94
~~~


<a id="compare-7aeab6691e38cfbbb9e0f0f6ea295fda"></a>

### [`004945e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/004945e8.md) → [`004b7480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7480.md) _ZN5Botan6BigInt11encode_1363ERKS0_m

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdbe10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c58860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/004945e8.md#insn-00494600) · [`00494610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/004945e8.md#insn-00494610)
- 新版 `004b7498`（命令位置の公開資料なし） · `004b74a8`（命令位置の公開資料なし）

~~~diff
- 00494600 ["INT_ADD", "register:40f0:8", ["const:494600:8", "const:4:8"]]
- 00494600 ["CALL", null, ["callee:004b34c8:8"]]
+ 004b7498 ["INT_ADD", "register:40f0:8", ["const:4b7498:8", "const:4:8"]]
+ 004b7498 ["CALL", null, ["callee:004b34c8:8"]]
- 00494600 bytes 0cf0ff97
+ 004b7498 bytes 0cf0ff97
- 00494610 ["INT_ADD", "register:40f0:8", ["const:494610:8", "const:4:8"]]
- 00494610 ["CALL", null, ["callee:00c58860:8"]]
+ 004b74a8 ["INT_ADD", "register:40f0:8", ["const:4b74a8:8", "const:4:8"]]
+ 004b74a8 ["CALL", null, ["callee:00c58860:8"]]
- 00494610 bytes 001e1d94
+ 004b74a8 bytes ee841e94
~~~


<a id="compare-4db8b9f9328d40f809356b342e8e67c0"></a>

### [`004947cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/004947cc.md) → [`004b7664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7664.md) _ZN5Botan6BigInt28encode_fixed_length_int_pairERKS0_S2_m

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdbe10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`00c58860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004947f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/004947cc.md#insn-004947f4) · [`00494804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/004947cc.md#insn-00494804) · [`00494818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/004947cc.md#insn-00494818)
- 新版 `004b768c`（命令位置の公開資料なし） · `004b769c`（命令位置の公開資料なし） · `004b76b0`（命令位置の公開資料なし）

~~~diff
- 004947f4 ["INT_ADD", "register:40f0:8", ["const:4947f4:8", "const:4:8"]]
- 004947f4 ["CALL", null, ["callee:004b34c8:8"]]
+ 004b768c ["INT_ADD", "register:40f0:8", ["const:4b768c:8", "const:4:8"]]
+ 004b768c ["CALL", null, ["callee:004b34c8:8"]]
- 004947f4 bytes 8fefff97
+ 004b768c bytes 8fefff97
- 00494804 ["INT_ADD", "register:40f0:8", ["const:494804:8", "const:4:8"]]
- 00494804 ["CALL", null, ["callee:00c58860:8"]]
+ 004b769c ["INT_ADD", "register:40f0:8", ["const:4b769c:8", "const:4:8"]]
+ 004b769c ["CALL", null, ["callee:00c58860:8"]]
- 00494804 bytes 831d1d94
+ 004b769c bytes 71841e94
- 00494818 ["INT_ADD", "register:40f0:8", ["const:494818:8", "const:4:8"]]
- 00494818 ["CALL", null, ["callee:00c58860:8"]]
+ 004b76b0 ["INT_ADD", "register:40f0:8", ["const:4b76b0:8", "const:4:8"]]
+ 004b76b0 ["CALL", null, ["callee:00c58860:8"]]
- 00494818 bytes 7e1d1d94
+ 004b76b0 bytes 6c841e94
~~~


<a id="compare-ce76d3ef32e87891607fda3496a86c41"></a>

### [`00494b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494b6c.md) → [`004b7a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7a04.md) _ZN5Botan17hex_decode_lockedEPKcmb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdbc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c586e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00494b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494b6c.md#insn-00494b98) · [`00494bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494b6c.md#insn-00494bac) · [`00494bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494b6c.md#insn-00494bc4)
- 新版 `004b7a30`（命令位置の公開資料なし） · `004b7a44`（命令位置の公開資料なし） · `004b7a5c`（命令位置の公開資料なし）

~~~diff
- 00494b98 ["INT_ADD", "register:40f0:8", ["const:494b98:8", "const:4:8"]]
- 00494b98 ["CALL", null, ["callee:004b34c8:8"]]
+ 004b7a30 ["INT_ADD", "register:40f0:8", ["const:4b7a30:8", "const:4:8"]]
+ 004b7a30 ["CALL", null, ["callee:004b34c8:8"]]
- 00494b98 bytes a6eeff97
+ 004b7a30 bytes a6eeff97
- 00494bac ["INT_ADD", "register:40f0:8", ["const:494bac:8", "const:4:8"]]
- 00494bac ["CALL", null, ["callee:00c586e0:8"]]
+ 004b7a44 ["INT_ADD", "register:40f0:8", ["const:4b7a44:8", "const:4:8"]]
+ 004b7a44 ["CALL", null, ["callee:00c586e0:8"]]
- 00494bac bytes 391c1d94
+ 004b7a44 bytes 27831e94
- 00494bc4 ["INT_ADD", "register:40f0:8", ["const:494bc4:8", "const:4:8"]]
- 00494bc4 ["CALL", null, ["callee:005404ac:8"]]
+ 004b7a5c ["INT_ADD", "register:40f0:8", ["const:4b7a5c:8", "const:4:8"]]
+ 004b7a5c ["CALL", null, ["callee:005404ac:8"]]
- 00494bc4 bytes 94220294
+ 004b7a5c bytes 94220294
~~~


<a id="compare-922a7a9a8144e8a43e620f67e46f88f0"></a>

### [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) → [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) FUN_004b8774

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 9件 [`004950f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00495e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495e3c.md) [`00496ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496ee0.md) [`00497068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497068.md) · 呼出先 1件 [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md)
- 新版 呼出元 9件 [`004b7f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7f88.md) [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b8cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8cd4.md) [`004b9d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9d78.md) [`004b9f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9f00.md) · 呼出先 1件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00495904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md#insn-00495904)
- 新版 `004b879c`（命令位置の公開資料なし）

~~~diff
- 00495904 ["INT_ADD", "register:40f0:8", ["const:495904:8", "const:4:8"]]
- 00495904 ["CALL", null, ["local:b0:8"]]
+ 004b879c ["INT_ADD", "register:40f0:8", ["const:4b879c:8", "const:4:8"]]
+ 004b879c ["CALL", null, ["local:b0:8"]]
- 00495904 bytes f6ffff97
+ 004b879c bytes f6ffff97
~~~


<a id="compare-7069e4c41ee9cb01a114d9cc19a6f696"></a>

### [`00496564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496564.md) → [`004b93fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b93fc.md) _ZN5Botan6BigIntrSEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbde0.md) · 呼出先 1件 [`00496d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md)
- 新版 呼出元 1件 [`00c58830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58830.md) · 呼出先 1件 [`004b9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004965ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496564.md#insn-004965ac)
- 新版 `004b9444`（命令位置の公開資料なし）

~~~diff
- 004965ac ["INT_ADD", "register:40f0:8", ["const:4965ac:8", "const:4:8"]]
- 004965ac ["CALL", null, ["callee:004b9bf8:8"]]
+ 004b9444 ["INT_ADD", "register:40f0:8", ["const:4b9444:8", "const:4:8"]]
+ 004b9444 ["CALL", null, ["callee:004b9bf8:8"]]
- 004965ac bytes ed010094
+ 004b9444 bytes ed010094
~~~


<a id="compare-7dce484acd14aa0aa5b1d9b9ece8b564"></a>

### [`00496c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496c30.md) → [`004b9ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9ac8.md) _ZN5Botan6BigIntlSEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbdc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdc0.md) · 呼出先 3件 [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c58810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58810.md) · 呼出先 3件 [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496c30.md#insn-00496cc0) · [`00496cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496c30.md#insn-00496cfc) · [`00496d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496c30.md#insn-00496d0c)
- 新版 `004b9b58`（命令位置の公開資料なし） · `004b9b94`（命令位置の公開資料なし） · `004b9ba4`（命令位置の公開資料なし）

~~~diff
- 00496cc0 ["INT_ADD", "register:40f0:8", ["const:496cc0:8", "const:4:8"]]
- 00496cc0 ["CALL", null, ["callee:005408e0:8"]]
+ 004b9b58 ["INT_ADD", "register:40f0:8", ["const:4b9b58:8", "const:4:8"]]
+ 004b9b58 ["CALL", null, ["callee:005408e0:8"]]
- 00496cc0 bytes 621b0294
+ 004b9b58 bytes 621b0294
- 00496cfc ["INT_ADD", "register:40f0:8", ["const:496cfc:8", "const:4:8"]]
- 00496cfc ["CALL", null, ["callee:00c57b40:8"]]
+ 004b9b94 ["INT_ADD", "register:40f0:8", ["const:4b9b94:8", "const:4:8"]]
+ 004b9b94 ["CALL", null, ["callee:00c57b40:8"]]
- 00496cfc bytes fd101d94
+ 004b9b94 bytes eb771e94
- 00496d0c ["INT_ADD", "register:40f0:8", ["const:496d0c:8", "const:4:8"]]
- 00496d0c ["CALL", null, ["callee:00c57c90:8"]]
+ 004b9ba4 ["INT_ADD", "register:40f0:8", ["const:4b9ba4:8", "const:4:8"]]
+ 004b9ba4 ["CALL", null, ["callee:00c57c90:8"]]
- 00496d0c bytes 4d111d94
+ 004b9ba4 bytes 3b781e94
~~~


<a id="compare-d736ce8befd1fe9486bb80213c49f281"></a>

### [`00496d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md) → [`004b9bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b9bf8.md) FUN_004b9bf8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00496564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496564.md) [`004b6640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b6/004b6640.md) [`004b77d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b7/004b77d0.md) [`004ba430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ba/004ba430.md) [`004bcf24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bcf24.md) · 呼出先 2件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 5件 [`004b93fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b93fc.md) [`004d94d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d9/004d94d8.md) [`004da668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004da/004da668.md) [`004dd2c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004dd/004dd2c8.md) [`004dfdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004dfdbc.md) · 呼出先 2件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00496dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md#insn-00496dc8) · [`00496e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496d60.md#insn-00496e08)
- 新版 `004b9c60`（命令位置の公開資料なし） · `004b9ca0`（命令位置の公開資料なし）

~~~diff
- 00496dc8 ["INT_ADD", "register:40f0:8", ["const:496dc8:8", "const:4:8"]]
- 00496dc8 ["CALL", null, ["callee:00c57b40:8"]]
+ 004b9c60 ["INT_ADD", "register:40f0:8", ["const:4b9c60:8", "const:4:8"]]
+ 004b9c60 ["CALL", null, ["callee:00c57b40:8"]]
- 00496dc8 bytes ca101d94
+ 004b9c60 bytes b8771e94
- 00496e08 ["INT_ADD", "register:40f0:8", ["const:496e08:8", "const:4:8"]]
- 00496e08 ["CALL", null, ["callee:00c57c90:8"]]
+ 004b9ca0 ["INT_ADD", "register:40f0:8", ["const:4b9ca0:8", "const:4:8"]]
+ 004b9ca0 ["CALL", null, ["callee:00c57c90:8"]]
- 00496e08 bytes 0e111d94
+ 004b9ca0 bytes fc771e94
~~~


<a id="compare-3da6793b4d543e01a5dc85228216eecc"></a>

### [`00497bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497bf4.md) → [`004baa8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004baa8c.md) _ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbeb0.md) · 呼出先 2件 [`00bdbcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md) [`00bdbea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbea0.md)
- 新版 呼出元 1件 [`00c58900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58900.md) · 呼出先 2件 [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md) [`00c588f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497bf4.md#insn-00497cb0) · [`00497cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497bf4.md#insn-00497cc0) · [`00497cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497bf4.md#insn-00497cd4)
- 新版 `004bab48`（命令位置の公開資料なし） · `004bab58`（命令位置の公開資料なし） · `004bab6c`（命令位置の公開資料なし）

~~~diff
- 00497cb0 ["INT_ADD", "register:40f0:8", ["const:497cb0:8", "const:4:8"]]
- 00497cb0 ["CALL", null, ["callee:00c588f0:8"]]
+ 004bab48 ["INT_ADD", "register:40f0:8", ["const:4bab48:8", "const:4:8"]]
+ 004bab48 ["CALL", null, ["callee:00c588f0:8"]]
- 00497cb0 bytes 7c101d94
+ 004bab48 bytes 6a771e94
- 00497cc0 ["INT_ADD", "register:40f0:8", ["const:497cc0:8", "const:4:8"]]
- 00497cc0 ["CALL", null, ["callee:00c58720:8"]]
+ 004bab58 ["INT_ADD", "register:40f0:8", ["const:4bab58:8", "const:4:8"]]
+ 004bab58 ["CALL", null, ["callee:00c58720:8"]]
- 00497cc0 bytes 04101d94
+ 004bab58 bytes f2761e94
- 00497cd4 ["INT_ADD", "register:40f0:8", ["const:497cd4:8", "const:4:8"]]
- 00497cd4 ["CALL", null, ["callee:00c58720:8"]]
+ 004bab6c ["INT_ADD", "register:40f0:8", ["const:4bab6c:8", "const:4:8"]]
+ 004bab6c ["CALL", null, ["callee:00c58720:8"]]
- 00497cd4 bytes ff0f1d94
+ 004bab6c bytes ed761e94
~~~


<a id="compare-fcea8f2bc51009ebc0a35f322e7573d9"></a>

### [`00497d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497d04.md) → [`004bab9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004bab9c.md) _ZN5Botan6BigIntC1Em

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) · 呼出先 1件 [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 1件 [`00c58520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58520.md) · 呼出先 1件 [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497d04.md#insn-00497d30)
- 新版 `004babc8`（命令位置の公開資料なし）

~~~diff
- 00497d30 ["INT_ADD", "register:40f0:8", ["const:497d30:8", "const:4:8"]]
- 00497d30 ["CALL", null, ["callee:005408e0:8"]]
+ 004babc8 ["INT_ADD", "register:40f0:8", ["const:4babc8:8", "const:4:8"]]
+ 004babc8 ["CALL", null, ["callee:005408e0:8"]]
- 00497d30 bytes 46170294
+ 004babc8 bytes 46170294
~~~


<a id="compare-df1ffc0b2bb3c4d3938b4c769ad30969"></a>

### [`00497d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497d5c.md) → [`004babf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004babf4.md) _ZN5Botan6BigIntC1ENS0_4SignEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbdd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdd0.md) · 呼出先 1件 [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 1件 [`00c58820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58820.md) · 呼出先 1件 [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497da0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497d5c.md#insn-00497da0)
- 新版 `004bac38`（命令位置の公開資料なし）

~~~diff
- 00497da0 ["INT_ADD", "register:40f0:8", ["const:497da0:8", "const:4:8"]]
- 00497da0 ["CALL", null, ["callee:005408e0:8"]]
+ 004bac38 ["INT_ADD", "register:40f0:8", ["const:4bac38:8", "const:4:8"]]
+ 004bac38 ["CALL", null, ["callee:005408e0:8"]]
- 00497da0 bytes 2a170294
+ 004bac38 bytes 2a170294
~~~


<a id="compare-58e2d0fc4c12dd16d465ae9e77eebabf"></a>

### [`00497dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497dc8.md) → [`004bac60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004bac60.md) _ZN5Botan6BigIntC2ERKS0_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md) · 呼出先 1件 [`00520804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520804.md)
- 新版 呼出元 1件 [`00c58740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58740.md) · 呼出先 1件 [`0054369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/0054369c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00497e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497dc8.md#insn-00497e04)
- 新版 `004bac9c`（命令位置の公開資料なし）

~~~diff
- 00497e04 ["INT_ADD", "register:40f0:8", ["const:497e04:8", "const:4:8"]]
- 00497e04 ["CALL", null, ["callee:0054369c:8"]]
+ 004bac9c ["INT_ADD", "register:40f0:8", ["const:4bac9c:8", "const:4:8"]]
+ 004bac9c ["CALL", null, ["callee:0054369c:8"]]
- 00497e04 bytes 80220294
+ 004bac9c bytes 80220294
~~~


<a id="compare-12a8cef97bd93e84e968af9f4fcad101"></a>

### [`0049811c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/0049811c.md) → [`004bafb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004bafb4.md) _ZN5Botan6BigIntC2ERNS_21RandomNumberGeneratorEmb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc500.md) · 呼出先 1件 [`00bdbea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbea0.md)
- 新版 呼出元 1件 [`00c58f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58f50.md) · 呼出先 1件 [`00c588f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c588f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049813c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/0049811c.md#insn-0049813c)
- 新版 `004bafd4`（命令位置の公開資料なし）

~~~diff
- 0049813c ["INT_ADD", "register:40f0:8", ["const:49813c:8", "const:4:8"]]
- 0049813c ["CALL", null, ["callee:00c588f0:8"]]
+ 004bafd4 ["INT_ADD", "register:40f0:8", ["const:4bafd4:8", "const:4:8"]]
+ 004bafd4 ["CALL", null, ["callee:00c588f0:8"]]
- 0049813c bytes 590f1d94
+ 004bafd4 bytes 47761e94
~~~


<a id="compare-01b6ff7e2d078dd13885f83e00d47036"></a>

### [`00498160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498160.md) → [`004baff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004baff8.md) _ZNK5Botan6BigInt3cmpERKS0_b

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbcd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcd0.md) · 呼出先 1件 [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md)
- 新版 呼出元 1件 [`00c58720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58720.md) · 呼出先 1件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004981f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498160.md#insn-004981f0)
- 新版 `004bb088`（命令位置の公開資料なし）

~~~diff
- 004981f0 ["INT_ADD", "register:40f0:8", ["const:4981f0:8", "const:4:8"]]
- 004981f0 ["CALL", null, ["callee:004b8774:8"]]
+ 004bb088 ["INT_ADD", "register:40f0:8", ["const:4bb088:8", "const:4:8"]]
+ 004bb088 ["CALL", null, ["callee:004b8774:8"]]
- 004981f0 bytes bbf5ff97
+ 004bb088 bytes bbf5ff97
~~~


<a id="compare-cb987b743d4f48fca69b759cb8c6f2b1"></a>

### [`004986a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004986a4.md) → [`004bb53c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bb53c.md) _ZN5Botan6BigInt7set_bitEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)
- 新版 呼出元 0件  · 呼出先 1件 [`005408e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005408e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004986f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004986a4.md#insn-004986f4)
- 新版 `004bb58c`（命令位置の公開資料なし）

~~~diff
- 004986f4 ["INT_ADD", "register:40f0:8", ["const:4986f4:8", "const:4:8"]]
- 004986f4 ["CALL", null, ["callee:005408e0:8"]]
+ 004bb58c ["INT_ADD", "register:40f0:8", ["const:4bb58c:8", "const:4:8"]]
+ 004bb58c ["CALL", null, ["callee:005408e0:8"]]
- 004986f4 bytes d5140294
+ 004bb58c bytes d5140294
~~~


<a id="compare-8219111ebb20a01652d63250c0d41651"></a>

### [`00499040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499040.md) → [`004bbed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bb/004bbed8.md) FUN_004bbed8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049e3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e3f4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004c128c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c128c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049908c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499040.md#insn-0049908c) · [`0049909c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499040.md#insn-0049909c) · [`004990d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499040.md#insn-004990d8)
- 新版 `004bbf24`（命令位置の公開資料なし） · `004bbf34`（命令位置の公開資料なし） · `004bbf70`（命令位置の公開資料なし）

~~~diff
- 0049908c ["INT_ADD", "register:40f0:8", ["const:49908c:8", "const:4:8"]]
- 0049908c ["CALL", null, ["callee:00c57ab0:8"]]
+ 004bbf24 ["INT_ADD", "register:40f0:8", ["const:4bbf24:8", "const:4:8"]]
+ 004bbf24 ["CALL", null, ["callee:00c57ab0:8"]]
- 0049908c bytes f5071d94
+ 004bbf24 bytes e36e1e94
- 0049909c ["INT_ADD", "register:40f0:8", ["const:49909c:8", "const:4:8"]]
- 0049909c ["CALL", null, ["callee:00c57ab0:8"]]
+ 004bbf34 ["INT_ADD", "register:40f0:8", ["const:4bbf34:8", "const:4:8"]]
+ 004bbf34 ["CALL", null, ["callee:00c57ab0:8"]]
- 0049909c bytes f1071d94
+ 004bbf34 bytes df6e1e94
- 004990d8 ["INT_ADD", "register:40f0:8", ["const:4990d8:8", "const:4:8"]]
- 004990d8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004bbf70 ["INT_ADD", "register:40f0:8", ["const:4bbf70:8", "const:4:8"]]
+ 004bbf70 ["CALL", null, ["callee:00c57ab0:8"]]
- 004990d8 bytes e2071d94
+ 004bbf70 bytes d06e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-629099600fc3b3ee74de6ebebd1a6bc1"></a>

### [`0049923c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/0049923c.md) → [`004bc0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc0d4.md) _ZN5Botan11BlockCipher9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004993a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004993a0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004bc238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc238.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004992ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/0049923c.md#insn-004992ac) · [`004992bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/0049923c.md#insn-004992bc) · [`004992f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/0049923c.md#insn-004992f8)
- 新版 `004bc144`（命令位置の公開資料なし） · `004bc154`（命令位置の公開資料なし） · `004bc190`（命令位置の公開資料なし）

~~~diff
- 004992ac ["INT_ADD", "register:40f0:8", ["const:4992ac:8", "const:4:8"]]
- 004992ac ["CALL", null, ["callee:00473500:8"]]
+ 004bc144 ["INT_ADD", "register:40f0:8", ["const:4bc144:8", "const:4:8"]]
+ 004bc144 ["CALL", null, ["callee:00473500:8"]]
- 004992ac bytes efdcfe97
+ 004bc144 bytes efdcfe97
- 004992bc ["INT_ADD", "register:40f0:8", ["const:4992bc:8", "const:4:8"]]
- 004992bc ["CALL", null, ["callee:004bc238:8"]]
+ 004bc154 ["INT_ADD", "register:40f0:8", ["const:4bc154:8", "const:4:8"]]
+ 004bc154 ["CALL", null, ["callee:004bc238:8"]]
- 004992bc bytes 39000094
+ 004bc154 bytes 39000094
- 004992f8 ["INT_ADD", "register:40f0:8", ["const:4992f8:8", "const:4:8"]]
- 004992f8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004bc190 ["INT_ADD", "register:40f0:8", ["const:4bc190:8", "const:4:8"]]
+ 004bc190 ["CALL", null, ["callee:00c57ab0:8"]]
- 004992f8 bytes 5a071d94
+ 004bc190 bytes 486e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94c22958bfce92fcf2f73643a446791e"></a>

### [`004993a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004993a0.md) → [`004bc238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc238.md) FUN_004bc238

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049923c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/0049923c.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbee0.md)
- 新版 呼出元 1件 [`004bc0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc0d4.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58930.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004993f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004993a0.md#insn-004993f0) · [`00499404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004993a0.md#insn-00499404) · [`00499420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004993a0.md#insn-00499420)
- 新版 `004bc288`（命令位置の公開資料なし） · `004bc29c`（命令位置の公開資料なし） · `004bc2b8`（命令位置の公開資料なし）

~~~diff
- 004993f0 ["INT_ADD", "register:40f0:8", ["const:4993f0:8", "const:4:8"]]
- 004993f0 ["CALL", null, ["callee:00540d3c:8"]]
+ 004bc288 ["INT_ADD", "register:40f0:8", ["const:4bc288:8", "const:4:8"]]
+ 004bc288 ["CALL", null, ["callee:00540d3c:8"]]
- 004993f0 bytes ad120294
+ 004bc288 bytes ad120294
- 00499404 ["COPY", "register:0:8", ["register:4040:8"]]
- 00499404 ["INT_ADD", "register:40f0:8", ["const:499404:8", "const:4:8"]]
- 00499404 ["CALLIND", null, ["register:0:8"]]
+ 004bc29c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bc29c ["INT_ADD", "register:40f0:8", ["const:4bc29c:8", "const:4:8"]]
+ 004bc29c ["CALLIND", null, ["register:0:8"]]
- 00499404 bytes 00013fd6
+ 004bc29c bytes 00013fd6
- 00499420 ["INT_ADD", "register:40f0:8", ["const:499420:8", "const:4:8"]]
- 00499420 ["CALL", null, ["callee:00c58930:8"]]
+ 004bc2b8 ["INT_ADD", "register:40f0:8", ["const:4bc2b8:8", "const:4:8"]]
+ 004bc2b8 ["CALL", null, ["callee:00c58930:8"]]
- 00499420 bytes b00a1d94
+ 004bc2b8 bytes 9e711e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf7579f5be399f4a755e154d11b22154"></a>

### [`00499808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499808.md) → [`004bc6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc6a0.md) _ZN5Botan8CBC_Mode5clearEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499808.md#insn-00499824)
- 新版 `004bc6bc`（命令位置の公開資料なし）

~~~diff
- 00499824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00499824 ["INT_ADD", "register:40f0:8", ["const:499824:8", "const:4:8"]]
- 00499824 ["CALLIND", null, ["register:0:8"]]
+ 004bc6bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bc6bc ["INT_ADD", "register:40f0:8", ["const:4bc6bc:8", "const:4:8"]]
+ 004bc6bc ["CALLIND", null, ["register:0:8"]]
- 00499824 bytes 00013fd6
+ 004bc6bc bytes 00013fd6
~~~


<a id="compare-f8d4f8f15a8dcea80d5618a87fa9d667"></a>

### [`00499aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499aa4.md) → [`004bc93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bc/004bc93c.md) _ZNK5Botan8CBC_Mode18update_granularityEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00499ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499aa4.md#insn-00499ac0) · [`00499ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499aa4.md#insn-00499ad4)
- 新版 `004bc958`（命令位置の公開資料なし） · `004bc96c`（命令位置の公開資料なし）

~~~diff
- 00499ac0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00499ac0 ["INT_ADD", "register:40f0:8", ["const:499ac0:8", "const:4:8"]]
- 00499ac0 ["CALLIND", null, ["register:0:8"]]
+ 004bc958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bc958 ["INT_ADD", "register:40f0:8", ["const:4bc958:8", "const:4:8"]]
+ 004bc958 ["CALLIND", null, ["register:0:8"]]
- 00499ac0 bytes 00013fd6
+ 004bc958 bytes 00013fd6
- 00499ad4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00499ad4 ["INT_ADD", "register:40f0:8", ["const:499ad4:8", "const:4:8"]]
- 00499ad4 ["CALLIND", null, ["register:0:8"]]
+ 004bc96c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bc96c ["INT_ADD", "register:40f0:8", ["const:4bc96c:8", "const:4:8"]]
+ 004bc96c ["CALLIND", null, ["register:0:8"]]
- 00499ad4 bytes 00013fd6
+ 004bc96c bytes 00013fd6
~~~


<a id="compare-4588ab60abc73896b4dc42af0d6fc52c"></a>

### [`0049ae90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049ae90.md) → [`004bdd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bd/004bdd28.md) _ZN5Botan14CBC_Decryption5resetEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049aeb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049a/0049ae90.md#insn-0049aeb4)
- 新版 `004bdd4c`（命令位置の公開資料なし）

~~~diff
- 0049aeb4 ["INT_ADD", "register:40f0:8", ["const:49aeb4:8", "const:4:8"]]
- 0049aeb4 ["CALL", null, ["callee:00c57c90:8"]]
+ 004bdd4c ["INT_ADD", "register:40f0:8", ["const:4bdd4c:8", "const:4:8"]]
+ 004bdd4c ["CALL", null, ["callee:00c57c90:8"]]
- 0049aeb4 bytes e3001d94
+ 004bdd4c bytes d1671e94
~~~


<a id="compare-e5d57ef7baa6f4a6223ea9b93403bf95"></a>

### [`0049bbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bbfc.md) → [`004bea94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bea94.md) _ZN5Botan11string_joinERKNSt6__ndk16vectorINS0_12basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS5_IS7_EEEEc

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md) [`00c58200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58200.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049bc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bbfc.md#insn-0049bc48) · [`0049bc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bbfc.md#insn-0049bc70)
- 新版 `004beae0`（命令位置の公開資料なし） · `004beb08`（命令位置の公開資料なし）

~~~diff
- 0049bc48 ["INT_ADD", "register:40f0:8", ["const:49bc48:8", "const:4:8"]]
- 0049bc48 ["CALL", null, ["callee:00c58200:8"]]
+ 004beae0 ["INT_ADD", "register:40f0:8", ["const:4beae0:8", "const:4:8"]]
+ 004beae0 ["CALL", null, ["callee:00c58200:8"]]
- 0049bc48 bytes dafe1c94
+ 004beae0 bytes c8651e94
- 0049bc70 ["INT_ADD", "register:40f0:8", ["const:49bc70:8", "const:4:8"]]
- 0049bc70 ["CALL", null, ["callee:00c57b80:8"]]
+ 004beb08 ["INT_ADD", "register:40f0:8", ["const:4beb08:8", "const:4:8"]]
+ 004beb08 ["CALL", null, ["callee:00c57b80:8"]]
- 0049bc70 bytes 30fd1c94
+ 004beb08 bytes 1e641e94
~~~


<a id="compare-a7ded79f03cd5ce9ab51ac4747e93e78"></a>

### [`0049bdc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bdc0.md) → [`004bec58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bec58.md) _ZN5Botan5CPUID15bit_from_stringERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0049bfc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bfc8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004bee60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bee60.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049be40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bdc0.md#insn-0049be40) · [`0049bea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bdc0.md#insn-0049bea4) · [`0049bef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bdc0.md#insn-0049bef0)
- 新版 `004becd8`（命令位置の公開資料なし） · `004bed3c`（命令位置の公開資料なし） · `004bed88`（命令位置の公開資料なし）

~~~diff
- 0049be40 ["INT_ADD", "register:40f0:8", ["const:49be40:8", "const:4:8"]]
- 0049be40 ["CALL", null, ["callee:00c57a90:8"]]
+ 004becd8 ["INT_ADD", "register:40f0:8", ["const:4becd8:8", "const:4:8"]]
+ 004becd8 ["CALL", null, ["callee:00c57a90:8"]]
- 0049be40 bytes 80fc1c94
+ 004becd8 bytes 6e631e94
- 0049bea4 ["INT_ADD", "register:40f0:8", ["const:49bea4:8", "const:4:8"]]
- 0049bea4 ["CALL", null, ["callee:004bee60:8"]]
+ 004bed3c ["INT_ADD", "register:40f0:8", ["const:4bed3c:8", "const:4:8"]]
+ 004bed3c ["CALL", null, ["callee:004bee60:8"]]
- 0049bea4 bytes 49000094
+ 004bed3c bytes 49000094
- 0049bef0 ["INT_ADD", "register:40f0:8", ["const:49bef0:8", "const:4:8"]]
- 0049bef0 ["CALL", null, ["callee:00c57a90:8"]]
+ 004bed88 ["INT_ADD", "register:40f0:8", ["const:4bed88:8", "const:4:8"]]
+ 004bed88 ["CALL", null, ["callee:00c57a90:8"]]
- 0049bef0 bytes 54fc1c94
+ 004bed88 bytes 42631e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f2b8374104df4c7f7f8b0c10515f4df"></a>

### [`0049bfc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bfc8.md) → [`004bee60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bee60.md) FUN_004bee60

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049bdc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bdc0.md) · 呼出先 5件 [`00520ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520ae8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`004bec58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004be/004bec58.md) · 呼出先 5件 [`00543980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543980.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049bffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bfc8.md#insn-0049bffc) · [`0049c014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bfc8.md#insn-0049c014) · [`0049c030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049b/0049bfc8.md#insn-0049c030)
- 新版 `004bee94`（命令位置の公開資料なし） · `004beeac`（命令位置の公開資料なし） · `004beec8`（命令位置の公開資料なし）

~~~diff
- 0049bffc ["INT_ADD", "register:40f0:8", ["const:49bffc:8", "const:4:8"]]
- 0049bffc ["CALL", null, ["callee:00c57a90:8"]]
+ 004bee94 ["INT_ADD", "register:40f0:8", ["const:4bee94:8", "const:4:8"]]
+ 004bee94 ["CALL", null, ["callee:00c57a90:8"]]
- 0049bffc bytes 11fc1c94
+ 004bee94 bytes ff621e94
- 0049c014 ["INT_ADD", "register:40f0:8", ["const:49c014:8", "const:4:8"]]
- 0049c014 ["CALL", null, ["callee:00c57b40:8"]]
+ 004beeac ["INT_ADD", "register:40f0:8", ["const:4beeac:8", "const:4:8"]]
+ 004beeac ["CALL", null, ["callee:00c57b40:8"]]
- 0049c014 bytes 37fc1c94
+ 004beeac bytes 25631e94
- 0049c030 ["INT_ADD", "register:40f0:8", ["const:49c030:8", "const:4:8"]]
- 0049c030 ["CALL", null, ["callee:00543980:8"]]
+ 004beec8 ["INT_ADD", "register:40f0:8", ["const:4beec8:8", "const:4:8"]]
+ 004beec8 ["CALL", null, ["callee:00543980:8"]]
- 0049c030 bytes ae120294
+ 004beec8 bytes ae120294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0bb6935da0e543d293508138722b6df"></a>

### [`0049c500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c500.md) → [`004bf398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bf398.md) _ZNK5Botan8ECB_Mode18update_granularityEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049c51c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c500.md#insn-0049c51c) · [`0049c530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c500.md#insn-0049c530)
- 新版 `004bf3b4`（命令位置の公開資料なし） · `004bf3c8`（命令位置の公開資料なし）

~~~diff
- 0049c51c ["COPY", "register:0:8", ["register:4040:8"]]
- 0049c51c ["INT_ADD", "register:40f0:8", ["const:49c51c:8", "const:4:8"]]
- 0049c51c ["CALLIND", null, ["register:0:8"]]
+ 004bf3b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf3b4 ["INT_ADD", "register:40f0:8", ["const:4bf3b4:8", "const:4:8"]]
+ 004bf3b4 ["CALLIND", null, ["register:0:8"]]
- 0049c51c bytes 00013fd6
+ 004bf3b4 bytes 00013fd6
- 0049c530 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049c530 ["INT_ADD", "register:40f0:8", ["const:49c530:8", "const:4:8"]]
- 0049c530 ["CALLIND", null, ["register:0:8"]]
+ 004bf3c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bf3c8 ["INT_ADD", "register:40f0:8", ["const:4bf3c8:8", "const:4:8"]]
+ 004bf3c8 ["CALLIND", null, ["register:0:8"]]
- 0049c530 bytes 00013fd6
+ 004bf3c8 bytes 00013fd6
~~~


<a id="compare-8ba5ed589eabc24484f1defcadd3809e"></a>

### [`0049cd68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cd68.md) → [`004bfc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfc00.md) _ZN5Botan13EMSA_PKCS1v158raw_dataEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049cd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cd68.md#insn-0049cd88) · [`0049cd94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cd68.md#insn-0049cd94) · [`0049cda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cd68.md#insn-0049cda8)
- 新版 `004bfc20`（命令位置の公開資料なし） · `004bfc2c`（命令位置の公開資料なし） · `004bfc40`（命令位置の公開資料なし）

~~~diff
- 0049cd88 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049cd88 ["INT_ADD", "register:40f0:8", ["const:49cd88:8", "const:4:8"]]
- 0049cd88 ["CALLIND", null, ["register:0:8"]]
+ 004bfc20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bfc20 ["INT_ADD", "register:40f0:8", ["const:4bfc20:8", "const:4:8"]]
+ 004bfc20 ["CALLIND", null, ["register:0:8"]]
- 0049cd88 bytes 20013fd6
+ 004bfc20 bytes 20013fd6
- 0049cd94 ["INT_ADD", "register:40f0:8", ["const:49cd94:8", "const:4:8"]]
- 0049cd94 ["CALL", null, ["callee:004b34c8:8"]]
+ 004bfc2c ["INT_ADD", "register:40f0:8", ["const:4bfc2c:8", "const:4:8"]]
+ 004bfc2c ["CALL", null, ["callee:004b34c8:8"]]
- 0049cd94 bytes 27ceff97
+ 004bfc2c bytes 27ceff97
- 0049cda8 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049cda8 ["INT_ADD", "register:40f0:8", ["const:49cda8:8", "const:4:8"]]
- 0049cda8 ["CALLIND", null, ["register:0:8"]]
+ 004bfc40 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bfc40 ["INT_ADD", "register:40f0:8", ["const:4bfc40:8", "const:4:8"]]
+ 004bfc40 ["CALLIND", null, ["register:0:8"]]
- 0049cda8 bytes 00013fd6
+ 004bfc40 bytes 00013fd6
~~~


<a id="compare-a460034e75f00e1b1d24fbb0bcdfe3c3"></a>

### [`0049cdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cdcc.md) → [`004bfc64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004bf/004bfc64.md) FUN_004bfc64

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0049ef6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049ef6c.md) · 呼出先 1件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md)
- 新版 呼出元 1件 [`004c1e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1e04.md) · 呼出先 1件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049cde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cdcc.md#insn-0049cde8) · [`0049cdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cdcc.md#insn-0049cdf4) · [`0049ce08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049cdcc.md#insn-0049ce08)
- 新版 `004bfc80`（命令位置の公開資料なし） · `004bfc8c`（命令位置の公開資料なし） · `004bfca0`（命令位置の公開資料なし）

~~~diff
- 0049cde8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049cde8 ["INT_ADD", "register:40f0:8", ["const:49cde8:8", "const:4:8"]]
- 0049cde8 ["CALLIND", null, ["register:0:8"]]
+ 004bfc80 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004bfc80 ["INT_ADD", "register:40f0:8", ["const:4bfc80:8", "const:4:8"]]
+ 004bfc80 ["CALLIND", null, ["register:0:8"]]
- 0049cde8 bytes 20013fd6
+ 004bfc80 bytes 20013fd6
- 0049cdf4 ["INT_ADD", "register:40f0:8", ["const:49cdf4:8", "const:4:8"]]
- 0049cdf4 ["CALL", null, ["callee:004b34c8:8"]]
+ 004bfc8c ["INT_ADD", "register:40f0:8", ["const:4bfc8c:8", "const:4:8"]]
+ 004bfc8c ["CALL", null, ["callee:004b34c8:8"]]
- 0049cdf4 bytes 0fceff97
+ 004bfc8c bytes 0fceff97
- 0049ce08 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049ce08 ["INT_ADD", "register:40f0:8", ["const:49ce08:8", "const:4:8"]]
- 0049ce08 ["CALLIND", null, ["register:0:8"]]
+ 004bfca0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004bfca0 ["INT_ADD", "register:40f0:8", ["const:4bfca0:8", "const:4:8"]]
+ 004bfca0 ["CALLIND", null, ["register:0:8"]]
- 0049ce08 bytes 00013fd6
+ 004bfca0 bytes 00013fd6
~~~


<a id="compare-652f90337f01c51f6a0108f77d970230"></a>

### [`0049d82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d82c.md) → [`004c06c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c06c4.md) FUN_004c06c4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004daaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004daaa4.md) [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`004fd93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md) [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d82c.md#insn-0049d898)
- 新版 `004c0730`（命令位置の公開資料なし）

~~~diff
- 0049d898 ["INT_ADD", "register:40f0:8", ["const:49d898:8", "const:4:8"]]
- 0049d898 ["CALL", null, ["callee:00c57c50:8"]]
+ 004c0730 ["INT_ADD", "register:40f0:8", ["const:4c0730:8", "const:4:8"]]
+ 004c0730 ["CALL", null, ["callee:00c57c50:8"]]
- 0049d898 bytes 5af61c94
+ 004c0730 bytes 485d1e94
~~~


<a id="compare-304dc51eddf1f10100be85dedb05d767"></a>

### [`0049d8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d8dc.md) → [`004c0774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0774.md) FUN_004c0774

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0049d2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d2b0.md) [`0049f624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049f/0049f624.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdbf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf80.md)
- 新版 呼出元 2件 [`004c0148`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0148.md) [`004c24bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c2/004c24bc.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md) [`00c589d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049d928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d8dc.md#insn-0049d928) · [`0049d934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d8dc.md#insn-0049d934) · [`0049d944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049d8dc.md#insn-0049d944)
- 新版 `004c07c0`（命令位置の公開資料なし） · `004c07cc`（命令位置の公開資料なし） · `004c07dc`（命令位置の公開資料なし）

~~~diff
- 0049d928 ["INT_ADD", "register:40f0:8", ["const:49d928:8", "const:4:8"]]
- 0049d928 ["CALL", null, ["callee:0043bae0:8"]]
+ 004c07c0 ["INT_ADD", "register:40f0:8", ["const:4c07c0:8", "const:4:8"]]
+ 004c07c0 ["CALL", null, ["callee:0043bae0:8"]]
- 0049d928 bytes aeedfd97
+ 004c07c0 bytes c8ecfd97
- 0049d934 ["INT_ADD", "register:40f0:8", ["const:49d934:8", "const:4:8"]]
- 0049d934 ["CALL", null, ["callee:00c589d0:8"]]
+ 004c07cc ["INT_ADD", "register:40f0:8", ["const:4c07cc:8", "const:4:8"]]
+ 004c07cc ["CALL", null, ["callee:00c589d0:8"]]
- 0049d934 bytes 93f91c94
+ 004c07cc bytes 81601e94
- 0049d944 ["INT_ADD", "register:40f0:8", ["const:49d944:8", "const:4:8"]]
- 0049d944 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004c07dc ["INT_ADD", "register:40f0:8", ["const:4c07dc:8", "const:4:8"]]
+ 004c07dc ["CALL", null, ["callee:00c57ab0:8"]]
- 0049d944 bytes c7f51c94
+ 004c07dc bytes b55c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4faea32ad5b359b954b974b2dd26cfbf"></a>

### [`0049dba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dba0.md) → [`004c0a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0a38.md) FUN_004c0a38

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`0050a638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050a638.md) [`0050b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050b/0050b45c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0052d4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052d4d0.md) [`0052e2f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052e/0052e2f4.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049dbbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dba0.md#insn-0049dbbc)
- 新版 `004c0a54`（命令位置の公開資料なし）

~~~diff
- 0049dbbc ["INT_ADD", "register:40f0:8", ["const:49dbbc:8", "const:4:8"]]
- 0049dbbc ["CALL", null, ["callee:00c57ab0:8"]]
+ 004c0a54 ["INT_ADD", "register:40f0:8", ["const:4c0a54:8", "const:4:8"]]
+ 004c0a54 ["CALL", null, ["callee:00c57ab0:8"]]
- 0049dbbc bytes 29f51c94
+ 004c0a54 bytes 175c1e94
~~~


<a id="compare-96e86585aade44c73a5dbd4ed1bdf55f"></a>

### [`0049e688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e688.md) → [`004c1520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1520.md) _ZN5Botan17EMSA_PKCS1v15_Raw6updateEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049e6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e688.md#insn-0049e6c0)
- 新版 `004c1558`（命令位置の公開資料なし）

~~~diff
- 0049e6c0 ["INT_ADD", "register:40f0:8", ["const:49e6c0:8", "const:4:8"]]
- 0049e6c0 ["CALL", null, ["callee:005404ac:8"]]
+ 004c1558 ["INT_ADD", "register:40f0:8", ["const:4c1558:8", "const:4:8"]]
+ 004c1558 ["CALL", null, ["callee:005404ac:8"]]
- 0049e6c0 bytes d5fb0194
+ 004c1558 bytes d5fb0194
~~~


<a id="compare-4ab7f8412fdf24a9413131e03b4c2d14"></a>

### [`0049e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e9d8.md) → [`004c1870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c1/004c1870.md) _ZN5Botan4PSSR8raw_dataEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md)
- 新版 呼出元 0件  · 呼出先 1件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0049e9f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e9d8.md#insn-0049e9f8) · [`0049ea04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e9d8.md#insn-0049ea04) · [`0049ea18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049e/0049e9d8.md#insn-0049ea18)
- 新版 `004c1890`（命令位置の公開資料なし） · `004c189c`（命令位置の公開資料なし） · `004c18b0`（命令位置の公開資料なし）

~~~diff
- 0049e9f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0049e9f8 ["INT_ADD", "register:40f0:8", ["const:49e9f8:8", "const:4:8"]]
- 0049e9f8 ["CALLIND", null, ["register:0:8"]]
+ 004c1890 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c1890 ["INT_ADD", "register:40f0:8", ["const:4c1890:8", "const:4:8"]]
+ 004c1890 ["CALLIND", null, ["register:0:8"]]
- 0049e9f8 bytes 20013fd6
+ 004c1890 bytes 20013fd6
- 0049ea04 ["INT_ADD", "register:40f0:8", ["const:49ea04:8", "const:4:8"]]
- 0049ea04 ["CALL", null, ["callee:004b34c8:8"]]
+ 004c189c ["INT_ADD", "register:40f0:8", ["const:4c189c:8", "const:4:8"]]
+ 004c189c ["CALL", null, ["callee:004b34c8:8"]]
- 0049ea04 bytes 0bc7ff97
+ 004c189c bytes 0bc7ff97
- 0049ea18 ["COPY", "register:0:8", ["register:4040:8"]]
- 0049ea18 ["INT_ADD", "register:40f0:8", ["const:49ea18:8", "const:4:8"]]
- 0049ea18 ["CALLIND", null, ["register:0:8"]]
+ 004c18b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c18b0 ["INT_ADD", "register:40f0:8", ["const:4c18b0:8", "const:4:8"]]
+ 004c18b0 ["CALLIND", null, ["register:0:8"]]
- 0049ea18 bytes 00013fd6
+ 004c18b0 bytes 00013fd6
~~~


<a id="compare-4b15572f9a10f308b9b1465c4aad7e87"></a>

### [`004a0414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0414.md) → [`004c32ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c32ac.md) _ZN5Botan15Entropy_Sources10add_sourceENSt6__ndk110unique_ptrINS_14Entropy_SourceENS1_14default_deleteIS3_EEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdbfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfe0.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00520d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520d70.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00c58a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a30.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00543c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543c08.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a0498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0414.md#insn-004a0498) · [`004a04d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0414.md#insn-004a04d0) · [`004a04e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0414.md#insn-004a04e4)
- 新版 `004c3330`（命令位置の公開資料なし） · `004c3368`（命令位置の公開資料なし） · `004c337c`（命令位置の公開資料なし）

~~~diff
- 004a0498 ["INT_ADD", "register:40f0:8", ["const:4a0498:8", "const:4:8"]]
- 004a0498 ["CALL", null, ["callee:00c57a90:8"]]
+ 004c3330 ["INT_ADD", "register:40f0:8", ["const:4c3330:8", "const:4:8"]]
+ 004c3330 ["CALL", null, ["callee:00c57a90:8"]]
- 004a0498 bytes eaea1c94
+ 004c3330 bytes d8511e94
- 004a04d0 ["INT_ADD", "register:40f0:8", ["const:4a04d0:8", "const:4:8"]]
- 004a04d0 ["CALL", null, ["callee:00c57c00:8"]]
+ 004c3368 ["INT_ADD", "register:40f0:8", ["const:4c3368:8", "const:4:8"]]
+ 004c3368 ["CALL", null, ["callee:00c57c00:8"]]
- 004a04d0 bytes 38eb1c94
+ 004c3368 bytes 26521e94
- 004a04e4 ["INT_ADD", "register:40f0:8", ["const:4a04e4:8", "const:4:8"]]
- 004a04e4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004c337c ["INT_ADD", "register:40f0:8", ["const:4c337c:8", "const:4:8"]]
+ 004c337c ["CALL", null, ["callee:00c57ab0:8"]]
- 004a04e4 bytes dfea1c94
+ 004c337c bytes cd511e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e4bef00c055c89bfc167a1cb7a357c7"></a>

### [`004a050c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a050c.md) → [`004c33a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c33a4.md) _ZNK5Botan15Entropy_Sources15enabled_sourcesEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00440f1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f1c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a05b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a050c.md#insn-004a05b0) · [`004a0618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a050c.md#insn-004a0618) · [`004a065c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a050c.md#insn-004a065c)
- 新版 `004c3448`（命令位置の公開資料なし） · `004c34b0`（命令位置の公開資料なし） · `004c34f4`（命令位置の公開資料なし）

~~~diff
- 004a05b0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a05b0 ["INT_ADD", "register:40f0:8", ["const:4a05b0:8", "const:4:8"]]
- 004a05b0 ["CALLIND", null, ["register:0:8"]]
+ 004c3448 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c3448 ["INT_ADD", "register:40f0:8", ["const:4c3448:8", "const:4:8"]]
+ 004c3448 ["CALLIND", null, ["register:0:8"]]
- 004a05b0 bytes 20013fd6
+ 004c3448 bytes 20013fd6
- 004a0618 ["INT_ADD", "register:40f0:8", ["const:4a0618:8", "const:4:8"]]
- 004a0618 ["CALL", null, ["callee:00c57a90:8"]]
+ 004c34b0 ["INT_ADD", "register:40f0:8", ["const:4c34b0:8", "const:4:8"]]
+ 004c34b0 ["CALL", null, ["callee:00c57a90:8"]]
- 004a0618 bytes 8aea1c94
+ 004c34b0 bytes 78511e94
- 004a065c ["INT_ADD", "register:40f0:8", ["const:4a065c:8", "const:4:8"]]
- 004a065c ["CALL", null, ["callee:00c57c00:8"]]
+ 004c34f4 ["INT_ADD", "register:40f0:8", ["const:4c34f4:8", "const:4:8"]]
+ 004c34f4 ["CALL", null, ["callee:00c57c00:8"]]
- 004a065c bytes d5ea1c94
+ 004c34f4 bytes c3511e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-121133fd8e962d5e12ca5c87dbb77b77"></a>

### [`004a0754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0754.md) → [`004c35ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c35ec.md) _ZN5Botan15Entropy_Sources4pollERNS_21RandomNumberGeneratorEmNSt6__ndk16chrono8durationIxNS3_5ratioILl1ELl1000EEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb730.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58180.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a0778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0754.md#insn-004a0778) · [`004a07a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0754.md#insn-004a07a8) · [`004a07b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0754.md#insn-004a07b8)
- 新版 `004c3610`（命令位置の公開資料なし） · `004c3640`（命令位置の公開資料なし） · `004c3650`（命令位置の公開資料なし）

~~~diff
- 004a0778 ["INT_ADD", "register:40f0:8", ["const:4a0778:8", "const:4:8"]]
- 004a0778 ["CALL", null, ["callee:00c58180:8"]]
+ 004c3610 ["INT_ADD", "register:40f0:8", ["const:4c3610:8", "const:4:8"]]
+ 004c3610 ["CALL", null, ["callee:00c58180:8"]]
- 004a0778 bytes eeeb1c94
+ 004c3610 bytes dc521e94
- 004a07a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a07a8 ["INT_ADD", "register:40f0:8", ["const:4a07a8:8", "const:4:8"]]
- 004a07a8 ["CALLIND", null, ["register:0:8"]]
+ 004c3640 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c3640 ["INT_ADD", "register:40f0:8", ["const:4c3640:8", "const:4:8"]]
+ 004c3640 ["CALLIND", null, ["register:0:8"]]
- 004a07a8 bytes 00013fd6
+ 004c3640 bytes 00013fd6
- 004a07b8 ["INT_ADD", "register:40f0:8", ["const:4a07b8:8", "const:4:8"]]
- 004a07b8 ["CALL", null, ["callee:00c58180:8"]]
+ 004c3650 ["INT_ADD", "register:40f0:8", ["const:4c3650:8", "const:4:8"]]
+ 004c3650 ["CALL", null, ["callee:00c58180:8"]]
- 004a07b8 bytes deeb1c94
+ 004c3650 bytes cc521e94
~~~


<a id="compare-f42e2883631766656770b04c0336e0a2"></a>

### [`004a07f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a07f8.md) → [`004c3690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3690.md) _ZN5Botan15Entropy_Sources9poll_justERNS_21RandomNumberGeneratorERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a0854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a07f8.md#insn-004a0854) · [`004a0860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a07f8.md#insn-004a0860) · [`004a088c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a07f8.md#insn-004a088c)
- 新版 `004c36ec`（命令位置の公開資料なし） · `004c36f8`（命令位置の公開資料なし） · `004c3724`（命令位置の公開資料なし）

~~~diff
- 004a0854 ["INT_ADD", "register:40f0:8", ["const:4a0854:8", "const:4:8"]]
- 004a0854 ["CALL", null, ["callee:00c57c50:8"]]
+ 004c36ec ["INT_ADD", "register:40f0:8", ["const:4c36ec:8", "const:4:8"]]
+ 004c36ec ["CALL", null, ["callee:00c57c50:8"]]
- 004a0854 bytes 6bea1c94
+ 004c36ec bytes 59511e94
- 004a0860 ["INT_ADD", "register:40f0:8", ["const:4a0860:8", "const:4:8"]]
- 004a0860 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004c36f8 ["INT_ADD", "register:40f0:8", ["const:4c36f8:8", "const:4:8"]]
+ 004c36f8 ["CALL", null, ["callee:00c57ab0:8"]]
- 004a0860 bytes 00ea1c94
+ 004c36f8 bytes ee501e94
- 004a088c ["COPY", "register:0:8", ["register:4048:8"]]
- 004a088c ["INT_ADD", "register:40f0:8", ["const:4a088c:8", "const:4:8"]]
- 004a088c ["CALLIND", null, ["register:0:8"]]
+ 004c3724 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c3724 ["INT_ADD", "register:40f0:8", ["const:4c3724:8", "const:4:8"]]
+ 004c3724 ["CALLIND", null, ["register:0:8"]]
- 004a088c bytes 20013fd6
+ 004c3724 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24e18303e11988bbcae6fc0c80d76064"></a>

### [`004a0978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0978.md) → [`004c3810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3810.md) FUN_004c3810

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 3件 [`004daaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004da/004daaa4.md) [`0086a350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086a/0086a350.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 3件 [`004fd93c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fd/004fd93c.md) [`0089d484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089d/0089d484.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a09e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0978.md#insn-004a09e4)
- 新版 `004c387c`（命令位置の公開資料なし）

~~~diff
- 004a09e4 ["INT_ADD", "register:40f0:8", ["const:4a09e4:8", "const:4:8"]]
- 004a09e4 ["CALL", null, ["callee:00c57c50:8"]]
+ 004c387c ["INT_ADD", "register:40f0:8", ["const:4c387c:8", "const:4:8"]]
+ 004c387c ["CALL", null, ["callee:00c57c50:8"]]
- 004a09e4 bytes 07ea1c94
+ 004c387c bytes f5501e94
~~~


<a id="compare-d7adb1b949760dcf0d3f640949be417c"></a>

### [`004a0be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0be8.md) → [`004c3a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3a80.md) FUN_004c3a80

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a0c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0be8.md#insn-004a0c34)
- 新版 `004c3acc`（命令位置の公開資料なし）

~~~diff
- 004a0c34 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a0c34 ["INT_ADD", "register:40f0:8", ["const:4a0c34:8", "const:4:8"]]
- 004a0c34 ["CALLIND", null, ["register:0:8"]]
+ 004c3acc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c3acc ["INT_ADD", "register:40f0:8", ["const:4c3acc:8", "const:4:8"]]
+ 004c3acc ["CALLIND", null, ["register:0:8"]]
- 004a0c34 bytes 00013fd6
+ 004c3acc bytes 00013fd6
~~~


<a id="compare-51a3aba7fe84d9e68480bfd9b878a6c5"></a>

### [`004a0fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0fc4.md) → [`004c3e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3e5c.md) FUN_004c3e5c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004a0c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0c64.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004c3afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c3/004c3afc.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a0/004a0fc4.md#insn-004a1010)
- 新版 `004c3ea8`（命令位置の公開資料なし）

~~~diff
- 004a1010 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a1010 ["INT_ADD", "register:40f0:8", ["const:4a1010:8", "const:4:8"]]
- 004a1010 ["CALLIND", null, ["register:0:8"]]
+ 004c3ea8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c3ea8 ["INT_ADD", "register:40f0:8", ["const:4c3ea8:8", "const:4:8"]]
+ 004c3ea8 ["CALLIND", null, ["register:0:8"]]
- 004a1010 bytes 00013fd6
+ 004c3ea8 bytes 00013fd6
~~~


<a id="compare-bfcb4a1b07e3e61123d6857521f82df8"></a>

### [`004a17a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a17a0.md) → [`004c4638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c4/004c4638.md) _ZN5Botan19StreamCipher_Filter5writeEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a17e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a17a0.md#insn-004a17e4) · [`004a17fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a1/004a17a0.md#insn-004a17fc)
- 新版 `004c467c`（命令位置の公開資料なし） · `004c4694`（命令位置の公開資料なし）

~~~diff
- 004a17e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a17e4 ["INT_ADD", "register:40f0:8", ["const:4a17e4:8", "const:4:8"]]
- 004a17e4 ["CALLIND", null, ["register:0:8"]]
+ 004c467c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004c467c ["INT_ADD", "register:40f0:8", ["const:4c467c:8", "const:4:8"]]
+ 004c467c ["CALLIND", null, ["register:0:8"]]
- 004a17e4 bytes 20013fd6
+ 004c467c bytes 20013fd6
- 004a17fc ["COPY", "register:0:8", ["register:4040:8"]]
- 004a17fc ["INT_ADD", "register:40f0:8", ["const:4a17fc:8", "const:4:8"]]
- 004a17fc ["CALLIND", null, ["register:0:8"]]
+ 004c4694 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c4694 ["INT_ADD", "register:40f0:8", ["const:4c4694:8", "const:4:8"]]
+ 004c4694 ["CALLIND", null, ["register:0:8"]]
- 004a17fc bytes 00013fd6
+ 004c4694 bytes 00013fd6
~~~


<a id="compare-f9534842d0fd707a26e905004c09f757"></a>

### [`004a28b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a28b8.md) → [`004c5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5750.md) _ZN5Botan15Buffered_Filter5writeEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc060.md) · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c58ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ab0.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a2918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a28b8.md#insn-004a2918) · [`004a2964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a28b8.md#insn-004a2964) · [`004a2980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a2/004a28b8.md#insn-004a2980)
- 新版 `004c57b0`（命令位置の公開資料なし） · `004c57fc`（命令位置の公開資料なし） · `004c5818`（命令位置の公開資料なし）

~~~diff
- 004a2918 ["INT_ADD", "register:40f0:8", ["const:4a2918:8", "const:4:8"]]
- 004a2918 ["CALL", null, ["callee:00c57b40:8"]]
+ 004c57b0 ["INT_ADD", "register:40f0:8", ["const:4c57b0:8", "const:4:8"]]
+ 004c57b0 ["CALL", null, ["callee:00c57b40:8"]]
- 004a2918 bytes f6e11c94
+ 004c57b0 bytes e4481e94
- 004a2964 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a2964 ["INT_ADD", "register:40f0:8", ["const:4a2964:8", "const:4:8"]]
- 004a2964 ["CALLIND", null, ["register:0:8"]]
+ 004c57fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c57fc ["INT_ADD", "register:40f0:8", ["const:4c57fc:8", "const:4:8"]]
+ 004c57fc ["CALLIND", null, ["register:0:8"]]
- 004a2964 bytes 00013fd6
+ 004c57fc bytes 00013fd6
- 004a2980 ["INT_ADD", "register:40f0:8", ["const:4a2980:8", "const:4:8"]]
- 004a2980 ["CALL", null, ["callee:00c57b40:8"]]
+ 004c5818 ["INT_ADD", "register:40f0:8", ["const:4c5818:8", "const:4:8"]]
+ 004c5818 ["CALL", null, ["callee:00c57b40:8"]]
- 004a2980 bytes dce11c94
+ 004c5818 bytes ca481e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f49211b557995081638e03b05abfc4e"></a>

### [`004a3114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3114.md) → [`004c5fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c5/004c5fac.md) _ZN5Botan18Cipher_Mode_Filter14buffered_blockEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc080.md) · 呼出先 2件 [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`005204e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005204e8.md)
- 新版 呼出元 1件 [`00c58ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ad0.md) · 呼出先 2件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00543380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00543/00543380.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a3144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3114.md#insn-004a3144) · [`004a315c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3114.md#insn-004a315c) · [`004a3178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3114.md#insn-004a3178)
- 新版 `004c5fdc`（命令位置の公開資料なし） · `004c5ff4`（命令位置の公開資料なし） · `004c6010`（命令位置の公開資料なし）

~~~diff
- 004a3144 ["INT_ADD", "register:40f0:8", ["const:4a3144:8", "const:4:8"]]
- 004a3144 ["CALL", null, ["callee:005404ac:8"]]
+ 004c5fdc ["INT_ADD", "register:40f0:8", ["const:4c5fdc:8", "const:4:8"]]
+ 004c5fdc ["CALL", null, ["callee:005404ac:8"]]
- 004a3144 bytes 34e90194
+ 004c5fdc bytes 34e90194
- 004a315c ["COPY", "register:0:8", ["register:4040:8"]]
- 004a315c ["INT_ADD", "register:40f0:8", ["const:4a315c:8", "const:4:8"]]
- 004a315c ["CALLIND", null, ["register:0:8"]]
+ 004c5ff4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c5ff4 ["INT_ADD", "register:40f0:8", ["const:4c5ff4:8", "const:4:8"]]
+ 004c5ff4 ["CALLIND", null, ["register:0:8"]]
- 004a315c bytes 00013fd6
+ 004c5ff4 bytes 00013fd6
- 004a3178 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a3178 ["INT_ADD", "register:40f0:8", ["const:4a3178:8", "const:4:8"]]
- 004a3178 ["CALLIND", null, ["register:0:8"]]
+ 004c6010 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c6010 ["INT_ADD", "register:40f0:8", ["const:4c6010:8", "const:4:8"]]
+ 004c6010 ["CALLIND", null, ["register:0:8"]]
- 004a3178 bytes 00013fd6
+ 004c6010 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c80a46c0ffbfc523bdd28bf2b80a9f92"></a>

### [`004a38b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a38b0.md) → [`004c6748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6748.md) _ZN5Botan15DataSink_StreamD0Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a38c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a38b0.md#insn-004a38c0)
- 新版 `004c6758`（命令位置の公開資料なし）

~~~diff
- 004a38c0 ["INT_ADD", "register:40f0:8", ["const:4a38c0:8", "const:4:8"]]
- 004a38c0 ["CALL", null, ["callee:00c58b30:8"]]
+ 004c6758 ["INT_ADD", "register:40f0:8", ["const:4c6758:8", "const:4:8"]]
+ 004c6758 ["CALL", null, ["callee:00c58b30:8"]]
- 004a38c0 bytes 08e21c94
+ 004c6758 bytes f6481e94
~~~


<a id="compare-5bdc23867d61e1dbbe790d157c8cd828"></a>

### [`004a38d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a38d4.md) → [`004c676c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c676c.md) _ZN5Botan6Filter4sendEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc0f0.md) · 呼出先 2件 [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c58b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b40.md) · 呼出先 2件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a3940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a38d4.md#insn-004a3940) · [`004a395c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a38d4.md#insn-004a395c) · [`004a39a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a38d4.md#insn-004a39a8)
- 新版 `004c67d8`（命令位置の公開資料なし） · `004c67f4`（命令位置の公開資料なし） · `004c6840`（命令位置の公開資料なし）

~~~diff
- 004a3940 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a3940 ["INT_ADD", "register:40f0:8", ["const:4a3940:8", "const:4:8"]]
- 004a3940 ["CALLIND", null, ["register:0:8"]]
+ 004c67d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c67d8 ["INT_ADD", "register:40f0:8", ["const:4c67d8:8", "const:4:8"]]
+ 004c67d8 ["CALLIND", null, ["register:0:8"]]
- 004a3940 bytes 00013fd6
+ 004c67d8 bytes 00013fd6
- 004a395c ["COPY", "register:0:8", ["register:4040:8"]]
- 004a395c ["INT_ADD", "register:40f0:8", ["const:4a395c:8", "const:4:8"]]
- 004a395c ["CALLIND", null, ["register:0:8"]]
+ 004c67f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c67f4 ["INT_ADD", "register:40f0:8", ["const:4c67f4:8", "const:4:8"]]
+ 004c67f4 ["CALLIND", null, ["register:0:8"]]
- 004a395c bytes 00013fd6
+ 004c67f4 bytes 00013fd6
- 004a39a8 ["INT_ADD", "register:40f0:8", ["const:4a39a8:8", "const:4:8"]]
- 004a39a8 ["CALL", null, ["callee:005404ac:8"]]
+ 004c6840 ["INT_ADD", "register:40f0:8", ["const:4c6840:8", "const:4:8"]]
+ 004c6840 ["CALL", null, ["callee:005404ac:8"]]
- 004a39a8 bytes 1be70194
+ 004c6840 bytes 1be70194
~~~


<a id="compare-31b40534bd8ec8e33a235079f80a35e6"></a>

### [`004a3a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3a0c.md) → [`004c68a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c68a4.md) _ZN5Botan6Filter7new_msgEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc100.md) · 呼出先 1件 [`00bdc100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc100.md)
- 新版 呼出元 1件 [`00c58b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b50.md) · 呼出先 1件 [`00c58b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a3a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3a0c.md#insn-004a3a24) · [`004a3a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3a0c.md#insn-004a3a54)
- 新版 `004c68bc`（命令位置の公開資料なし） · `004c68ec`（命令位置の公開資料なし）

~~~diff
- 004a3a24 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a3a24 ["INT_ADD", "register:40f0:8", ["const:4a3a24:8", "const:4:8"]]
- 004a3a24 ["CALLIND", null, ["register:0:8"]]
+ 004c68bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c68bc ["INT_ADD", "register:40f0:8", ["const:4c68bc:8", "const:4:8"]]
+ 004c68bc ["CALLIND", null, ["register:0:8"]]
- 004a3a24 bytes 00013fd6
+ 004c68bc bytes 00013fd6
- 004a3a54 ["INT_ADD", "register:40f0:8", ["const:4a3a54:8", "const:4:8"]]
- 004a3a54 ["CALL", null, ["callee:00c58b50:8"]]
+ 004c68ec ["INT_ADD", "register:40f0:8", ["const:4c68ec:8", "const:4:8"]]
+ 004c68ec ["CALL", null, ["callee:00c58b50:8"]]
- 004a3a54 bytes abe11c94
+ 004c68ec bytes 99481e94
~~~


<a id="compare-fe7e970e137d7607c325d8ee2fa7e527"></a>

### [`004a3a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3a6c.md) → [`004c6904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c6/004c6904.md) _ZN5Botan6Filter10finish_msgEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc110.md) · 呼出先 1件 [`00bdc110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc110.md)
- 新版 呼出元 1件 [`00c58b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b60.md) · 呼出先 1件 [`00c58b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a3a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3a6c.md#insn-004a3a84) · [`004a3ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a3/004a3a6c.md#insn-004a3ab4)
- 新版 `004c691c`（命令位置の公開資料なし） · `004c694c`（命令位置の公開資料なし）

~~~diff
- 004a3a84 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a3a84 ["INT_ADD", "register:40f0:8", ["const:4a3a84:8", "const:4:8"]]
- 004a3a84 ["CALLIND", null, ["register:0:8"]]
+ 004c691c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c691c ["INT_ADD", "register:40f0:8", ["const:4c691c:8", "const:4:8"]]
+ 004c691c ["CALLIND", null, ["register:0:8"]]
- 004a3a84 bytes 00013fd6
+ 004c691c bytes 00013fd6
- 004a3ab4 ["INT_ADD", "register:40f0:8", ["const:4a3ab4:8", "const:4:8"]]
- 004a3ab4 ["CALL", null, ["callee:00c58b60:8"]]
+ 004c694c ["INT_ADD", "register:40f0:8", ["const:4c694c:8", "const:4:8"]]
+ 004c694c ["CALL", null, ["callee:00c58b60:8"]]
- 004a3ab4 bytes 97e11c94
+ 004c694c bytes 85481e94
~~~


<a id="compare-eb923b676942262cb1a654b1fb4cb3bb"></a>

### [`004a48d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a48d0.md) → [`004c7768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7768.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS_11OctetStringESB_NS_10Cipher_DirE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc120.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a48ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a48d0.md#insn-004a48ec) · [`004a4900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a48d0.md#insn-004a4900) · [`004a4920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a48d0.md#insn-004a4920)
- 新版 `004c7784`（命令位置の公開資料なし） · `004c7798`（命令位置の公開資料なし） · `004c77b8`（命令位置の公開資料なし）

~~~diff
- 004a48ec ["INT_ADD", "register:40f0:8", ["const:4a48ec:8", "const:4:8"]]
- 004a48ec ["CALL", null, ["callee:00c58b70:8"]]
+ 004c7784 ["INT_ADD", "register:40f0:8", ["const:4c7784:8", "const:4:8"]]
+ 004c7784 ["CALL", null, ["callee:00c58b70:8"]]
- 004a48ec bytes 0dde1c94
+ 004c7784 bytes fb441e94
- 004a4900 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a4900 ["INT_ADD", "register:40f0:8", ["const:4a4900:8", "const:4:8"]]
- 004a4900 ["CALLIND", null, ["register:0:8"]]
+ 004c7798 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c7798 ["INT_ADD", "register:40f0:8", ["const:4c7798:8", "const:4:8"]]
+ 004c7798 ["CALLIND", null, ["register:0:8"]]
- 004a4900 bytes 00013fd6
+ 004c7798 bytes 00013fd6
- 004a4920 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a4920 ["INT_ADD", "register:40f0:8", ["const:4a4920:8", "const:4:8"]]
- 004a4920 ["CALLIND", null, ["register:0:8"]]
+ 004c77b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c77b8 ["INT_ADD", "register:40f0:8", ["const:4c77b8:8", "const:4:8"]]
+ 004c77b8 ["CALLIND", null, ["register:0:8"]]
- 004a4920 bytes 00013fd6
+ 004c77b8 bytes 00013fd6
~~~


<a id="compare-df7750703b4a852e5cadcbd0786931c9"></a>

### [`004a4938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4938.md) → [`004c77d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c77d0.md) _ZN5Botan10get_cipherERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEERKNS_11OctetStringENS_10Cipher_DirE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc120.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58b70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a494c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4938.md#insn-004a494c) · [`004a4960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4938.md#insn-004a4960)
- 新版 `004c77e4`（命令位置の公開資料なし） · `004c77f8`（命令位置の公開資料なし）

~~~diff
- 004a494c ["INT_ADD", "register:40f0:8", ["const:4a494c:8", "const:4:8"]]
- 004a494c ["CALL", null, ["callee:00c58b70:8"]]
+ 004c77e4 ["INT_ADD", "register:40f0:8", ["const:4c77e4:8", "const:4:8"]]
+ 004c77e4 ["CALL", null, ["callee:00c58b70:8"]]
- 004a494c bytes f5dd1c94
+ 004c77e4 bytes e3441e94
- 004a4960 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a4960 ["INT_ADD", "register:40f0:8", ["const:4a4960:8", "const:4:8"]]
- 004a4960 ["CALLIND", null, ["register:0:8"]]
+ 004c77f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004c77f8 ["INT_ADD", "register:40f0:8", ["const:4c77f8:8", "const:4:8"]]
+ 004c77f8 ["CALLIND", null, ["register:0:8"]]
- 004a4960 bytes 00013fd6
+ 004c77f8 bytes 00013fd6
~~~


<a id="compare-d69bb3b21f5444eb13d460f5701789d9"></a>

### [`004a4a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4a98.md) → [`004c7930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7930.md) _ZNK5Botan11SecureQueue4peekEPhmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1b0.md) · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c58c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c00.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a4b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4a98.md#insn-004a4b30) · [`004a4b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4a98.md#insn-004a4b88)
- 新版 `004c79c8`（命令位置の公開資料なし） · `004c7a20`（命令位置の公開資料なし）

~~~diff
- 004a4b30 ["INT_ADD", "register:40f0:8", ["const:4a4b30:8", "const:4:8"]]
- 004a4b30 ["CALL", null, ["callee:00c57b40:8"]]
+ 004c79c8 ["INT_ADD", "register:40f0:8", ["const:4c79c8:8", "const:4:8"]]
+ 004c79c8 ["CALL", null, ["callee:00c57b40:8"]]
- 004a4b30 bytes 70d91c94
+ 004c79c8 bytes 5e401e94
- 004a4b88 ["INT_ADD", "register:40f0:8", ["const:4a4b88:8", "const:4:8"]]
- 004a4b88 ["CALL", null, ["callee:00c57b40:8"]]
+ 004c7a20 ["INT_ADD", "register:40f0:8", ["const:4c7a20:8", "const:4:8"]]
+ 004c7a20 ["CALL", null, ["callee:00c57b40:8"]]
- 004a4b88 bytes 5ad91c94
+ 004c7a20 bytes 48401e94
~~~


<a id="compare-fff3f889013bda57c4a311e049dca803"></a>

### [`004a4d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d4c.md) → [`004c7be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7be4.md) FUN_004c7be4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0050d8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0053078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a4d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d4c.md#insn-004a4d68)
- 新版 `004c7c00`（命令位置の公開資料なし）

~~~diff
- 004a4d68 ["INT_ADD", "register:40f0:8", ["const:4a4d68:8", "const:4:8"]]
- 004a4d68 ["CALL", null, ["callee:0053078c:8"]]
+ 004c7c00 ["INT_ADD", "register:40f0:8", ["const:4c7c00:8", "const:4:8"]]
+ 004c7c00 ["CALL", null, ["callee:0053078c:8"]]
- 004a4d68 bytes e3a20194
+ 004c7c00 bytes e3a20194
~~~


<a id="compare-3e2a1e648c47be211683ae1d878c9054"></a>

### [`004a4d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d88.md) → [`004c7c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c7/004c7c20.md) FUN_004c7c20

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`004a5940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5940.md) · 呼出先 2件 [`0050d8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050d/0050d8f4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004c87d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c87d8.md) · 呼出先 2件 [`0053078c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00530/0053078c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a4db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d88.md#insn-004a4db4) · [`004a4dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d88.md#insn-004a4dbc) · [`004a4e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a4/004a4d88.md#insn-004a4e70)
- 新版 `004c7c4c`（命令位置の公開資料なし） · `004c7c54`（命令位置の公開資料なし） · `004c7d08`（命令位置の公開資料なし）

~~~diff
- 004a4db4 ["INT_ADD", "register:40f0:8", ["const:4a4db4:8", "const:4:8"]]
- 004a4db4 ["CALL", null, ["callee:0053078c:8"]]
+ 004c7c4c ["INT_ADD", "register:40f0:8", ["const:4c7c4c:8", "const:4:8"]]
+ 004c7c4c ["CALL", null, ["callee:0053078c:8"]]
- 004a4db4 bytes d0a20194
+ 004c7c4c bytes d0a20194
- 004a4dbc ["INT_ADD", "register:40f0:8", ["const:4a4dbc:8", "const:4:8"]]
- 004a4dbc ["CALL", null, ["callee:00c57ab0:8"]]
+ 004c7c54 ["INT_ADD", "register:40f0:8", ["const:4c7c54:8", "const:4:8"]]
+ 004c7c54 ["CALL", null, ["callee:00c57ab0:8"]]
- 004a4dbc bytes a9d81c94
+ 004c7c54 bytes 973f1e94
- 004a4e70 ["INT_ADD", "register:40f0:8", ["const:4a4e70:8", "const:4:8"]]
- 004a4e70 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004c7d08 ["INT_ADD", "register:40f0:8", ["const:4c7d08:8", "const:4:8"]]
+ 004c7d08 ["CALL", null, ["callee:00c57ab0:8"]]
- 004a4e70 bytes 7cd81c94
+ 004c7d08 bytes 6a3f1e94
~~~


<a id="compare-01c0ea4ce07e740fa836c16df78e87a9"></a>

### [`004a5238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5238.md) → [`004c80d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c80d0.md) FUN_004c80d0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00521954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521954.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005447ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005447ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5238.md#insn-004a5254)
- 新版 `004c80ec`（命令位置の公開資料なし）

~~~diff
- 004a5254 ["INT_ADD", "register:40f0:8", ["const:4a5254:8", "const:4:8"]]
- 004a5254 ["CALL", null, ["callee:005447ec:8"]]
+ 004c80ec ["INT_ADD", "register:40f0:8", ["const:4c80ec:8", "const:4:8"]]
+ 004c80ec ["CALL", null, ["callee:005447ec:8"]]
- 004a5254 bytes c0f10194
+ 004c80ec bytes c0f10194
~~~


<a id="compare-4f1c1a3598178d721a89d987a8e66fdf"></a>

### [`004a5274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5274.md) → [`004c810c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c810c.md) _ZN5Botan4PipeD2Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1e0.md) · 呼出先 3件 [`00521954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521954.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1d0.md)
- 新版 呼出元 1件 [`00c58c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c30.md) · 呼出先 3件 [`005447ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/005447ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5274.md#insn-004a5288) · [`004a529c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5274.md#insn-004a529c)
- 新版 `004c8120`（命令位置の公開資料なし） · `004c8134`（命令位置の公開資料なし）

~~~diff
- 004a5288 ["INT_ADD", "register:40f0:8", ["const:4a5288:8", "const:4:8"]]
- 004a5288 ["CALL", null, ["callee:00c58c20:8"]]
+ 004c8120 ["INT_ADD", "register:40f0:8", ["const:4c8120:8", "const:4:8"]]
+ 004c8120 ["CALL", null, ["callee:00c58c20:8"]]
- 004a5288 bytes d2db1c94
+ 004c8120 bytes c0421e94
- 004a529c ["INT_ADD", "register:40f0:8", ["const:4a529c:8", "const:4:8"]]
- 004a529c ["CALL", null, ["callee:005447ec:8"]]
+ 004c8134 ["INT_ADD", "register:40f0:8", ["const:4c8134:8", "const:4:8"]]
+ 004c8134 ["CALL", null, ["callee:005447ec:8"]]
- 004a529c bytes aef10194
+ 004c8134 bytes aef10194
~~~


<a id="compare-cc9e11785dbc347189e52ff345e16931"></a>

### [`004a5374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5374.md) → [`004c820c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c820c.md) _ZN5Botan4Pipe5resetEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5374.md#insn-004a5388)
- 新版 `004c8220`（命令位置の公開資料なし）

~~~diff
- 004a5388 ["INT_ADD", "register:40f0:8", ["const:4a5388:8", "const:4:8"]]
- 004a5388 ["CALL", null, ["callee:00c58c20:8"]]
+ 004c8220 ["INT_ADD", "register:40f0:8", ["const:4c8220:8", "const:4:8"]]
+ 004c8220 ["CALL", null, ["callee:00c58c20:8"]]
- 004a5388 bytes 92db1c94
+ 004c8220 bytes 80421e94
~~~


<a id="compare-d5b69bfdcb15c378d65ce5c4a3d89c27"></a>

### [`004a53a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a53a0.md) → [`004c8238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8238.md) _ZNK5Botan4Pipe11end_of_dataEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a53ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a53a0.md#insn-004a53ac)
- 新版 `004c8244`（命令位置の公開資料なし）

~~~diff
- 004a53ac ["INT_ADD", "register:40f0:8", ["const:4a53ac:8", "const:4:8"]]
- 004a53ac ["CALL", null, ["callee:00c58c40:8"]]
+ 004c8244 ["INT_ADD", "register:40f0:8", ["const:4c8244:8", "const:4:8"]]
+ 004c8244 ["CALL", null, ["callee:00c58c40:8"]]
- 004a53ac bytes 91db1c94
+ 004c8244 bytes 7f421e94
~~~


<a id="compare-2f60447278de576195efd92abdd084fd"></a>

### [`004a5654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5654.md) → [`004c84ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c84ec.md) _ZN5Botan4Pipe11process_msgEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) [`00bdc210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md) [`00bdc220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) [`00c58c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md) [`00c58c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5654.md#insn-004a5670) · [`004a5680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5654.md#insn-004a5680)
- 新版 `004c8508`（命令位置の公開資料なし） · `004c8518`（命令位置の公開資料なし）

~~~diff
- 004a5670 ["INT_ADD", "register:40f0:8", ["const:4a5670:8", "const:4:8"]]
- 004a5670 ["CALL", null, ["callee:00c58c50:8"]]
+ 004c8508 ["INT_ADD", "register:40f0:8", ["const:4c8508:8", "const:4:8"]]
+ 004c8508 ["CALL", null, ["callee:00c58c50:8"]]
- 004a5670 bytes e4da1c94
+ 004c8508 bytes d2411e94
- 004a5680 ["INT_ADD", "register:40f0:8", ["const:4a5680:8", "const:4:8"]]
- 004a5680 ["CALL", null, ["callee:00c58c60:8"]]
+ 004c8518 ["INT_ADD", "register:40f0:8", ["const:4c8518:8", "const:4:8"]]
+ 004c8518 ["CALL", null, ["callee:00c58c60:8"]]
- 004a5680 bytes e4da1c94
+ 004c8518 bytes d2411e94
~~~


<a id="compare-4cc63a8ef9dc292f08c1d23aa6d83341"></a>

### [`004a5acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5acc.md) → [`004c8964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8964.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) [`00bdc210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md) [`00bdc220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) [`00c58c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md) [`00c58c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5acc.md#insn-004a5ae8) · [`004a5af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5acc.md#insn-004a5af8)
- 新版 `004c8980`（命令位置の公開資料なし） · `004c8990`（命令位置の公開資料なし）

~~~diff
- 004a5ae8 ["INT_ADD", "register:40f0:8", ["const:4a5ae8:8", "const:4:8"]]
- 004a5ae8 ["CALL", null, ["callee:00c58c50:8"]]
+ 004c8980 ["INT_ADD", "register:40f0:8", ["const:4c8980:8", "const:4:8"]]
+ 004c8980 ["CALL", null, ["callee:00c58c50:8"]]
- 004a5ae8 bytes c6d91c94
+ 004c8980 bytes b4401e94
- 004a5af8 ["INT_ADD", "register:40f0:8", ["const:4a5af8:8", "const:4:8"]]
- 004a5af8 ["CALL", null, ["callee:00c58c60:8"]]
+ 004c8990 ["INT_ADD", "register:40f0:8", ["const:4c8990:8", "const:4:8"]]
+ 004c8990 ["CALL", null, ["callee:00c58c60:8"]]
- 004a5af8 bytes c6d91c94
+ 004c8990 bytes b4401e94
~~~


<a id="compare-640ec199e8fbe5e5e5fecf02f1a6a5eb"></a>

### [`004a5b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5b10.md) → [`004c89a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c89a8.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) [`00bdc210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md) [`00bdc220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) [`00c58c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md) [`00c58c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5b10.md#insn-004a5b2c) · [`004a5b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5b10.md#insn-004a5b3c)
- 新版 `004c89c4`（命令位置の公開資料なし） · `004c89d4`（命令位置の公開資料なし）

~~~diff
- 004a5b2c ["INT_ADD", "register:40f0:8", ["const:4a5b2c:8", "const:4:8"]]
- 004a5b2c ["CALL", null, ["callee:00c58c50:8"]]
+ 004c89c4 ["INT_ADD", "register:40f0:8", ["const:4c89c4:8", "const:4:8"]]
+ 004c89c4 ["CALL", null, ["callee:00c58c50:8"]]
- 004a5b2c bytes b5d91c94
+ 004c89c4 bytes a3401e94
- 004a5b3c ["INT_ADD", "register:40f0:8", ["const:4a5b3c:8", "const:4:8"]]
- 004a5b3c ["CALL", null, ["callee:00c58c60:8"]]
+ 004c89d4 ["INT_ADD", "register:40f0:8", ["const:4c89d4:8", "const:4:8"]]
+ 004c89d4 ["CALL", null, ["callee:00c58c60:8"]]
- 004a5b3c bytes b5d91c94
+ 004c89d4 bytes a3401e94
~~~


<a id="compare-9e44d9d5334bde60b1b3018416475738"></a>

### [`004a5b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5b54.md) → [`004c89ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c89ec.md) _ZN5Botan4Pipe11process_msgERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) [`00bdc210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md) [`00bdc220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) [`00c58c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md) [`00c58c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5b54.md#insn-004a5b80) · [`004a5b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5b54.md#insn-004a5b90)
- 新版 `004c8a18`（命令位置の公開資料なし） · `004c8a28`（命令位置の公開資料なし）

~~~diff
- 004a5b80 ["INT_ADD", "register:40f0:8", ["const:4a5b80:8", "const:4:8"]]
- 004a5b80 ["CALL", null, ["callee:00c58c50:8"]]
+ 004c8a18 ["INT_ADD", "register:40f0:8", ["const:4c8a18:8", "const:4:8"]]
+ 004c8a18 ["CALL", null, ["callee:00c58c50:8"]]
- 004a5b80 bytes a0d91c94
+ 004c8a18 bytes 8e401e94
- 004a5b90 ["INT_ADD", "register:40f0:8", ["const:4a5b90:8", "const:4:8"]]
- 004a5b90 ["CALL", null, ["callee:00c58c60:8"]]
+ 004c8a28 ["INT_ADD", "register:40f0:8", ["const:4c8a28:8", "const:4:8"]]
+ 004c8a28 ["CALL", null, ["callee:00c58c60:8"]]
- 004a5b90 bytes a0d91c94
+ 004c8a28 bytes 8e401e94
~~~


<a id="compare-deed15e817f24a4f1209959e38d4a46f"></a>

### [`004a5ba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5ba8.md) → [`004c8a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c8/004c8a40.md) _ZN5Botan4Pipe11process_msgERNS_10DataSourceE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdc200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc200.md) [`00bdc220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc220.md) [`00bdc250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc250.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c50.md) [`00c58c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c70.md) [`00c58ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58ca0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a5bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5ba8.md#insn-004a5bbc) · [`004a5bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a5/004a5ba8.md#insn-004a5bc8)
- 新版 `004c8a54`（命令位置の公開資料なし） · `004c8a60`（命令位置の公開資料なし）

~~~diff
- 004a5bbc ["INT_ADD", "register:40f0:8", ["const:4a5bbc:8", "const:4:8"]]
- 004a5bbc ["CALL", null, ["callee:00c58c50:8"]]
+ 004c8a54 ["INT_ADD", "register:40f0:8", ["const:4c8a54:8", "const:4:8"]]
+ 004c8a54 ["CALL", null, ["callee:00c58c50:8"]]
- 004a5bbc bytes 91d91c94
+ 004c8a54 bytes 7f401e94
- 004a5bc8 ["INT_ADD", "register:40f0:8", ["const:4a5bc8:8", "const:4:8"]]
- 004a5bc8 ["CALL", null, ["callee:00c58ca0:8"]]
+ 004c8a60 ["INT_ADD", "register:40f0:8", ["const:4c8a60:8", "const:4:8"]]
+ 004c8a60 ["CALL", null, ["callee:00c58ca0:8"]]
- 004a5bc8 bytes a2d91c94
+ 004c8a60 bytes 90401e94
~~~


<a id="compare-e1553f1764faaed4ed2af23ac8a5366a"></a>

### [`004a6a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6a58.md) → [`004c98f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c98f0.md) _ZN5Botan4Pipe5writeEh

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc210.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a6a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6a58.md#insn-004a6a80) · [`004a6aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6a58.md#insn-004a6aa4)
- 新版 `004c9918`（命令位置の公開資料なし） · `004c993c`（命令位置の公開資料なし）

~~~diff
- 004a6a80 ["INT_ADD", "register:40f0:8", ["const:4a6a80:8", "const:4:8"]]
- 004a6a80 ["CALL", null, ["callee:00c58c60:8"]]
+ 004c9918 ["INT_ADD", "register:40f0:8", ["const:4c9918:8", "const:4:8"]]
+ 004c9918 ["CALL", null, ["callee:00c58c60:8"]]
- 004a6a80 bytes e4d51c94
+ 004c9918 bytes d23c1e94
- 004a6aa4 ["INT_ADD", "register:40f0:8", ["const:4a6aa4:8", "const:4:8"]]
- 004a6aa4 ["CALL", null, ["callee:00c57ae0:8"]]
+ 004c993c ["INT_ADD", "register:40f0:8", ["const:4c993c:8", "const:4:8"]]
+ 004c993c ["CALL", null, ["callee:00c57ae0:8"]]
- 004a6aa4 bytes 7bd11c94
+ 004c993c bytes 69381e94
~~~


<a id="compare-bee90a3833a9135408b6198e6b774c81"></a>

### [`004a6c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6c04.md) → [`004c9a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9a9c.md) _ZN5Botan4Pipe8read_allEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdc1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1f0.md) [`00bdc270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc270.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c58c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c40.md) [`00c58cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58cc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a6c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6c04.md#insn-004a6c2c) · [`004a6c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6c04.md#insn-004a6c38) · [`004a6c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a6/004a6c04.md#insn-004a6c4c)
- 新版 `004c9ac4`（命令位置の公開資料なし） · `004c9ad0`（命令位置の公開資料なし） · `004c9ae4`（命令位置の公開資料なし）

~~~diff
- 004a6c2c ["INT_ADD", "register:40f0:8", ["const:4a6c2c:8", "const:4:8"]]
- 004a6c2c ["CALL", null, ["callee:00c58c40:8"]]
+ 004c9ac4 ["INT_ADD", "register:40f0:8", ["const:4c9ac4:8", "const:4:8"]]
+ 004c9ac4 ["CALL", null, ["callee:00c58c40:8"]]
- 004a6c2c bytes 71d51c94
+ 004c9ac4 bytes 5f3c1e94
- 004a6c38 ["INT_ADD", "register:40f0:8", ["const:4a6c38:8", "const:4:8"]]
- 004a6c38 ["CALL", null, ["callee:004b34c8:8"]]
+ 004c9ad0 ["INT_ADD", "register:40f0:8", ["const:4c9ad0:8", "const:4:8"]]
+ 004c9ad0 ["CALL", null, ["callee:004b34c8:8"]]
- 004a6c38 bytes 7ea6ff97
+ 004c9ad0 bytes 7ea6ff97
- 004a6c4c ["INT_ADD", "register:40f0:8", ["const:4a6c4c:8", "const:4:8"]]
- 004a6c4c ["CALL", null, ["callee:00c58cc0:8"]]
+ 004c9ae4 ["INT_ADD", "register:40f0:8", ["const:4c9ae4:8", "const:4:8"]]
+ 004c9ae4 ["CALL", null, ["callee:00c58cc0:8"]]
- 004a6c4c bytes 89d51c94
+ 004c9ae4 bytes 773c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c8be5d1f743fc7a42833d906b601c79"></a>

### [`004a70b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a70b0.md) → [`004c9f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9f48.md) _ZN5Botan4Pipe15check_availableEm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a70c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a70b0.md#insn-004a70c8)
- 新版 `004c9f60`（命令位置の公開資料なし）

~~~diff
- 004a70c8 ["INT_ADD", "register:40f0:8", ["const:4a70c8:8", "const:4:8"]]
- 004a70c8 ["CALL", null, ["callee:00c58c40:8"]]
+ 004c9f60 ["INT_ADD", "register:40f0:8", ["const:4c9f60:8", "const:4:8"]]
+ 004c9f60 ["CALL", null, ["callee:00c58c40:8"]]
- 004a70c8 bytes 4ad41c94
+ 004c9f60 bytes 383b1e94
~~~


<a id="compare-29fc240d7605a3d748a3ef6136d3da35"></a>

### [`004a70e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a70e0.md) → [`004c9f78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c9/004c9f78.md) _ZN5Botan4Pipe19check_available_msgEmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdc1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc1f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58c40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a70f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a70e0.md#insn-004a70f4)
- 新版 `004c9f8c`（命令位置の公開資料なし）

~~~diff
- 004a70f4 ["INT_ADD", "register:40f0:8", ["const:4a70f4:8", "const:4:8"]]
- 004a70f4 ["CALL", null, ["callee:00c58c40:8"]]
+ 004c9f8c ["INT_ADD", "register:40f0:8", ["const:4c9f8c:8", "const:4:8"]]
+ 004c9f8c ["CALL", null, ["callee:00c58c40:8"]]
- 004a70f4 bytes 3fd41c94
+ 004c9f8c bytes 2d3b1e94
~~~


<a id="compare-866b3bea04a81ffa7b93acdb36ef8d54"></a>

### [`004a7d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7d10.md) → [`004caba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004caba8.md) FUN_004caba8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a7d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7d10.md#insn-004a7d5c) · [`004a7d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7d10.md#insn-004a7d70) · [`004a7d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7d10.md#insn-004a7d78)
- 新版 `004cabf4`（命令位置の公開資料なし） · `004cac08`（命令位置の公開資料なし） · `004cac10`（命令位置の公開資料なし）

~~~diff
- 004a7d5c ["INT_ADD", "register:40f0:8", ["const:4a7d5c:8", "const:4:8"]]
- 004a7d5c ["CALL", null, ["callee:00c538e0:8"]]
+ 004cabf4 ["INT_ADD", "register:40f0:8", ["const:4cabf4:8", "const:4:8"]]
+ 004cabf4 ["CALL", null, ["callee:00c538e0:8"]]
- 004a7d5c bytes 4dbc1c94
+ 004cabf4 bytes 3b231e94
- 004a7d70 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a7d70 ["INT_ADD", "register:40f0:8", ["const:4a7d70:8", "const:4:8"]]
- 004a7d70 ["CALLIND", null, ["register:0:8"]]
+ 004cac08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cac08 ["INT_ADD", "register:40f0:8", ["const:4cac08:8", "const:4:8"]]
+ 004cac08 ["CALLIND", null, ["register:0:8"]]
- 004a7d70 bytes 00013fd6
+ 004cac08 bytes 00013fd6
- 004a7d78 ["INT_ADD", "register:40f0:8", ["const:4a7d78:8", "const:4:8"]]
- 004a7d78 ["CALL", null, ["callee:00c57a80:8"]]
+ 004cac10 ["INT_ADD", "register:40f0:8", ["const:4cac10:8", "const:4:8"]]
+ 004cac10 ["CALL", null, ["callee:00c57a80:8"]]
- 004a7d78 bytes aecc1c94
+ 004cac10 bytes 9c331e94
~~~


<a id="compare-35f22007dd985b7c2ecc5689cb05563f"></a>

### [`004a807c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a807c.md) → [`004caf14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004caf14.md) _ZN5Botan13Threaded_ForkD0Ev

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a808c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a807c.md#insn-004a808c)
- 新版 `004caf24`（命令位置の公開資料なし）

~~~diff
- 004a808c ["INT_ADD", "register:40f0:8", ["const:4a808c:8", "const:4:8"]]
- 004a808c ["CALL", null, ["callee:00c58d20:8"]]
+ 004caf24 ["INT_ADD", "register:40f0:8", ["const:4caf24:8", "const:4:8"]]
+ 004caf24 ["CALL", null, ["callee:00c58d20:8"]]
- 004a808c bytes 91d01c94
+ 004caf24 bytes 7f371e94
~~~


<a id="compare-72e412191b721c4d3461484d663657b8"></a>

### [`004a80c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a80c8.md) → [`004caf60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004caf60.md) FUN_004caf60

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004a7a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7a98.md) · 呼出先 5件 [`00521ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521ad8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`004ca930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca930.md) · 呼出先 5件 [`00544970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544970.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a810c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a80c8.md#insn-004a810c) · [`004a8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a80c8.md#insn-004a8160) · [`004a8174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a80c8.md#insn-004a8174)
- 新版 `004cafa4`（命令位置の公開資料なし） · `004caff8`（命令位置の公開資料なし） · `004cb00c`（命令位置の公開資料なし）

~~~diff
- 004a810c ["INT_ADD", "register:40f0:8", ["const:4a810c:8", "const:4:8"]]
- 004a810c ["CALL", null, ["callee:00c57a90:8"]]
+ 004cafa4 ["INT_ADD", "register:40f0:8", ["const:4cafa4:8", "const:4:8"]]
+ 004cafa4 ["CALL", null, ["callee:00c57a90:8"]]
- 004a810c bytes cdcb1c94
+ 004cafa4 bytes bb321e94
- 004a8160 ["INT_ADD", "register:40f0:8", ["const:4a8160:8", "const:4:8"]]
- 004a8160 ["CALL", null, ["callee:00c538e0:8"]]
+ 004caff8 ["INT_ADD", "register:40f0:8", ["const:4caff8:8", "const:4:8"]]
+ 004caff8 ["CALL", null, ["callee:00c538e0:8"]]
- 004a8160 bytes 4cbb1c94
+ 004caff8 bytes 3a221e94
- 004a8174 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a8174 ["INT_ADD", "register:40f0:8", ["const:4a8174:8", "const:4:8"]]
- 004a8174 ["CALLIND", null, ["register:0:8"]]
+ 004cb00c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cb00c ["INT_ADD", "register:40f0:8", ["const:4cb00c:8", "const:4:8"]]
+ 004cb00c ["CALLIND", null, ["register:0:8"]]
- 004a8174 bytes 00013fd6
+ 004cb00c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e29908f6c5fc4136ec1b5810bd135cf"></a>

### [`004a81d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a81d0.md) → [`004cb068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb068.md) _ZN5Botan13Threaded_Fork12thread_entryEPNS_6FilterE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004a7a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a7/004a7a98.md) · 呼出先 5件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md)
- 新版 呼出元 1件 [`004ca930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ca/004ca930.md) · 呼出先 5件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a8218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a81d0.md#insn-004a8218) · [`004a8220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a81d0.md#insn-004a8220) · [`004a8234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a81d0.md#insn-004a8234)
- 新版 `004cb0b0`（命令位置の公開資料なし） · `004cb0b8`（命令位置の公開資料なし） · `004cb0cc`（命令位置の公開資料なし）

~~~diff
- 004a8218 ["INT_ADD", "register:40f0:8", ["const:4a8218:8", "const:4:8"]]
- 004a8218 ["CALL", null, ["callee:00c57f80:8"]]
+ 004cb0b0 ["INT_ADD", "register:40f0:8", ["const:4cb0b0:8", "const:4:8"]]
+ 004cb0b0 ["CALL", null, ["callee:00c57f80:8"]]
- 004a8218 bytes c6cc1c94
+ 004cb0b0 bytes b4331e94
- 004a8220 ["INT_ADD", "register:40f0:8", ["const:4a8220:8", "const:4:8"]]
- 004a8220 ["CALL", null, ["callee:00c57cf0:8"]]
+ 004cb0b8 ["INT_ADD", "register:40f0:8", ["const:4cb0b8:8", "const:4:8"]]
+ 004cb0b8 ["CALL", null, ["callee:00c57cf0:8"]]
- 004a8220 bytes 20cc1c94
+ 004cb0b8 bytes 0e331e94
- 004a8234 ["INT_ADD", "register:40f0:8", ["const:4a8234:8", "const:4:8"]]
- 004a8234 ["CALL", null, ["callee:00c57ce0:8"]]
+ 004cb0cc ["INT_ADD", "register:40f0:8", ["const:4cb0cc:8", "const:4:8"]]
+ 004cb0cc ["CALL", null, ["callee:00c57ce0:8"]]
- 004a8234 bytes 17cc1c94
+ 004cb0cc bytes 05331e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-243124139aa506042e9e71f605b394c3"></a>

### [`004a8428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8428.md) → [`004cb2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb2c0.md) FUN_004cb2c0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a8444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8428.md#insn-004a8444) · [`004a8464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8428.md#insn-004a8464)
- 新版 `004cb2dc`（命令位置の公開資料なし） · `004cb2fc`（命令位置の公開資料なし）

~~~diff
- 004a8444 ["INT_ADD", "register:40f0:8", ["const:4a8444:8", "const:4:8"]]
- 004a8444 ["CALL", null, ["callee:00c538e0:8"]]
+ 004cb2dc ["INT_ADD", "register:40f0:8", ["const:4cb2dc:8", "const:4:8"]]
+ 004cb2dc ["CALL", null, ["callee:00c538e0:8"]]
- 004a8444 bytes 93ba1c94
+ 004cb2dc bytes 81211e94
- 004a8464 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a8464 ["INT_ADD", "register:40f0:8", ["const:4a8464:8", "const:4:8"]]
- 004a8464 ["CALLIND", null, ["register:0:8"]]
+ 004cb2fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cb2fc ["INT_ADD", "register:40f0:8", ["const:4cb2fc:8", "const:4:8"]]
+ 004cb2fc ["CALLIND", null, ["register:0:8"]]
- 004a8464 bytes 00013fd6
+ 004cb2fc bytes 00013fd6
~~~


<a id="compare-4920a7701b000535a99148497ac671c6"></a>

### [`004a8478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8478.md) → [`004cb310`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb310.md) _ZN5Botan13Threaded_Fork4sendEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdc2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c58d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a84b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8478.md#insn-004a84b0) · [`004a84c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8478.md#insn-004a84c0) · [`004a8690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8478.md#insn-004a8690)
- 新版 `004cb348`（命令位置の公開資料なし） · `004cb358`（命令位置の公開資料なし） · `004cb528`（命令位置の公開資料なし）

~~~diff
- 004a84b0 ["INT_ADD", "register:40f0:8", ["const:4a84b0:8", "const:4:8"]]
- 004a84b0 ["CALL", null, ["callee:00c58d30:8"]]
+ 004cb348 ["INT_ADD", "register:40f0:8", ["const:4cb348:8", "const:4:8"]]
+ 004cb348 ["CALL", null, ["callee:00c58d30:8"]]
- 004a84b0 bytes 8ccf1c94
+ 004cb348 bytes 7a361e94
- 004a84c0 ["INT_ADD", "register:40f0:8", ["const:4a84c0:8", "const:4:8"]]
- 004a84c0 ["CALL", null, ["callee:00c58d30:8"]]
+ 004cb358 ["INT_ADD", "register:40f0:8", ["const:4cb358:8", "const:4:8"]]
+ 004cb358 ["CALL", null, ["callee:00c58d30:8"]]
- 004a84c0 bytes 88cf1c94
+ 004cb358 bytes 76361e94
- 004a8690 ["INT_ADD", "register:40f0:8", ["const:4a8690:8", "const:4:8"]]
- 004a8690 ["CALL", null, ["callee:005404ac:8"]]
+ 004cb528 ["INT_ADD", "register:40f0:8", ["const:4cb528:8", "const:4:8"]]
+ 004cb528 ["CALL", null, ["callee:005404ac:8"]]
- 004a8690 bytes e1d30194
+ 004cb528 bytes e1d30194
~~~


<a id="compare-c0382d6e1fd936b8ef668a7cb963f40c"></a>

### [`004a86e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a86e8.md) → [`004cb580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cb580.md) _ZN5Botan13Threaded_Fork20thread_delegate_workEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2e0.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md)
- 新版 呼出元 1件 [`00c58d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d30.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a872c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a86e8.md#insn-004a872c) · [`004a8744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a86e8.md#insn-004a8744) · [`004a8764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a86e8.md#insn-004a8764)
- 新版 `004cb5c4`（命令位置の公開資料なし） · `004cb5dc`（命令位置の公開資料なし） · `004cb5fc`（命令位置の公開資料なし）

~~~diff
- 004a872c ["INT_ADD", "register:40f0:8", ["const:4a872c:8", "const:4:8"]]
- 004a872c ["CALL", null, ["callee:00c57ce0:8"]]
+ 004cb5c4 ["INT_ADD", "register:40f0:8", ["const:4cb5c4:8", "const:4:8"]]
+ 004cb5c4 ["CALL", null, ["callee:00c57ce0:8"]]
- 004a872c bytes d9ca1c94
+ 004cb5c4 bytes c7311e94
- 004a8744 ["INT_ADD", "register:40f0:8", ["const:4a8744:8", "const:4:8"]]
- 004a8744 ["CALL", null, ["callee:00c57cf0:8"]]
+ 004cb5dc ["INT_ADD", "register:40f0:8", ["const:4cb5dc:8", "const:4:8"]]
+ 004cb5dc ["CALL", null, ["callee:00c57cf0:8"]]
- 004a8744 bytes d7ca1c94
+ 004cb5dc bytes c5311e94
- 004a8764 ["INT_ADD", "register:40f0:8", ["const:4a8764:8", "const:4:8"]]
- 004a8764 ["CALL", null, ["callee:00c57cf0:8"]]
+ 004cb5fc ["INT_ADD", "register:40f0:8", ["const:4cb5fc:8", "const:4:8"]]
+ 004cb5fc ["CALL", null, ["callee:00c57cf0:8"]]
- 004a8764 bytes cfca1c94
+ 004cb5fc bytes bd311e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d464f1a7db0f6962d1f2c686d47f1781"></a>

### [`004a8fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8fa8.md) → [`004cbe40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbe40.md) _ZN5Botan12HashFunction9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004a9174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9174.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004cc00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc00c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a9038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8fa8.md#insn-004a9038) · [`004a9048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8fa8.md#insn-004a9048) · [`004a9084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8fa8.md#insn-004a9084)
- 新版 `004cbed0`（命令位置の公開資料なし） · `004cbee0`（命令位置の公開資料なし） · `004cbf1c`（命令位置の公開資料なし）

~~~diff
- 004a9038 ["INT_ADD", "register:40f0:8", ["const:4a9038:8", "const:4:8"]]
- 004a9038 ["CALL", null, ["callee:00473500:8"]]
+ 004cbed0 ["INT_ADD", "register:40f0:8", ["const:4cbed0:8", "const:4:8"]]
+ 004cbed0 ["CALL", null, ["callee:00473500:8"]]
- 004a9038 bytes 8c9dfe97
+ 004cbed0 bytes 8c9dfe97
- 004a9048 ["INT_ADD", "register:40f0:8", ["const:4a9048:8", "const:4:8"]]
- 004a9048 ["CALL", null, ["callee:004cc00c:8"]]
+ 004cbee0 ["INT_ADD", "register:40f0:8", ["const:4cbee0:8", "const:4:8"]]
+ 004cbee0 ["CALL", null, ["callee:004cc00c:8"]]
- 004a9048 bytes 4b000094
+ 004cbee0 bytes 4b000094
- 004a9084 ["INT_ADD", "register:40f0:8", ["const:4a9084:8", "const:4:8"]]
- 004a9084 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004cbf1c ["INT_ADD", "register:40f0:8", ["const:4cbf1c:8", "const:4:8"]]
+ 004cbf1c ["CALL", null, ["callee:00c57ab0:8"]]
- 004a9084 bytes f7c71c94
+ 004cbf1c bytes e52e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4763b745a21ffbcaa4cf8ef9e1255875"></a>

### [`004a9174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9174.md) → [`004cc00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc00c.md) FUN_004cc00c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004a8fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a8/004a8fa8.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbfa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfa0.md)
- 新版 呼出元 1件 [`004cbe40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cb/004cbe40.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c589f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c589f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a91c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9174.md#insn-004a91c4) · [`004a91d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9174.md#insn-004a91d8) · [`004a91f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9174.md#insn-004a91f4)
- 新版 `004cc05c`（命令位置の公開資料なし） · `004cc070`（命令位置の公開資料なし） · `004cc08c`（命令位置の公開資料なし）

~~~diff
- 004a91c4 ["INT_ADD", "register:40f0:8", ["const:4a91c4:8", "const:4:8"]]
- 004a91c4 ["CALL", null, ["callee:00540d3c:8"]]
+ 004cc05c ["INT_ADD", "register:40f0:8", ["const:4cc05c:8", "const:4:8"]]
+ 004cc05c ["CALL", null, ["callee:00540d3c:8"]]
- 004a91c4 bytes 38d30194
+ 004cc05c bytes 38d30194
- 004a91d8 ["COPY", "register:0:8", ["register:4040:8"]]
- 004a91d8 ["INT_ADD", "register:40f0:8", ["const:4a91d8:8", "const:4:8"]]
- 004a91d8 ["CALLIND", null, ["register:0:8"]]
+ 004cc070 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cc070 ["INT_ADD", "register:40f0:8", ["const:4cc070:8", "const:4:8"]]
+ 004cc070 ["CALLIND", null, ["register:0:8"]]
- 004a91d8 bytes 00013fd6
+ 004cc070 bytes 00013fd6
- 004a91f4 ["INT_ADD", "register:40f0:8", ["const:4a91f4:8", "const:4:8"]]
- 004a91f4 ["CALL", null, ["callee:00c589f0:8"]]
+ 004cc08c ["INT_ADD", "register:40f0:8", ["const:4cc08c:8", "const:4:8"]]
+ 004cc08c ["CALL", null, ["callee:00c589f0:8"]]
- 004a91f4 bytes 6bcb1c94
+ 004cc08c bytes 59321e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1914bbeb70afae02de2df2b9a5fd47a"></a>

### [`004a92b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a92b4.md) → [`004cc14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc14c.md) FUN_004cc14c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`0049dd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049d/0049dd0c.md) · 呼出先 3件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`004c0ba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004c0/004c0ba4.md) · 呼出先 3件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a92e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a92b4.md#insn-004a92e4) · [`004a92fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a92b4.md#insn-004a92fc) · [`004a9318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a92b4.md#insn-004a9318)
- 新版 `004cc17c`（命令位置の公開資料なし） · `004cc194`（命令位置の公開資料なし） · `004cc1b0`（命令位置の公開資料なし）

~~~diff
- 004a92e4 ["INT_ADD", "register:40f0:8", ["const:4a92e4:8", "const:4:8"]]
- 004a92e4 ["CALL", null, ["callee:00c57a90:8"]]
+ 004cc17c ["INT_ADD", "register:40f0:8", ["const:4cc17c:8", "const:4:8"]]
+ 004cc17c ["CALL", null, ["callee:00c57a90:8"]]
- 004a92e4 bytes 57c71c94
+ 004cc17c bytes 452e1e94
- 004a92fc ["INT_ADD", "register:40f0:8", ["const:4a92fc:8", "const:4:8"]]
- 004a92fc ["CALL", null, ["callee:00c57c00:8"]]
+ 004cc194 ["INT_ADD", "register:40f0:8", ["const:4cc194:8", "const:4:8"]]
+ 004cc194 ["CALL", null, ["callee:00c57c00:8"]]
- 004a92fc bytes adc71c94
+ 004cc194 bytes 9b2e1e94
- 004a9318 ["INT_ADD", "register:40f0:8", ["const:4a9318:8", "const:4:8"]]
- 004a9318 ["CALL", null, ["callee:0049f3ec:8"]]
+ 004cc1b0 ["INT_ADD", "register:40f0:8", ["const:4cc1b0:8", "const:4:8"]]
+ 004cc1b0 ["CALL", null, ["callee:0049f3ec:8"]]
- 004a9318 bytes 8f4cff97
+ 004cc1b0 bytes 8f4cff97
~~~


<a id="compare-93990cd7c0559a3eca8f87e9f13559ca"></a>

### [`004a9884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9884.md) → [`004cc71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc71c.md) _ZN5Botan17hex_decode_lockedERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdbc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`004b34c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b3/004b34c8.md) [`005404ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/005404ac.md) [`00c586e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c586e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a98c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9884.md#insn-004a98c0) · [`004a98d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9884.md#insn-004a98d4) · [`004a98ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9884.md#insn-004a98ec)
- 新版 `004cc758`（命令位置の公開資料なし） · `004cc76c`（命令位置の公開資料なし） · `004cc784`（命令位置の公開資料なし）

~~~diff
- 004a98c0 ["INT_ADD", "register:40f0:8", ["const:4a98c0:8", "const:4:8"]]
- 004a98c0 ["CALL", null, ["callee:004b34c8:8"]]
+ 004cc758 ["INT_ADD", "register:40f0:8", ["const:4cc758:8", "const:4:8"]]
+ 004cc758 ["CALL", null, ["callee:004b34c8:8"]]
- 004a98c0 bytes 5c9bff97
+ 004cc758 bytes 5c9bff97
- 004a98d4 ["INT_ADD", "register:40f0:8", ["const:4a98d4:8", "const:4:8"]]
- 004a98d4 ["CALL", null, ["callee:00c586e0:8"]]
+ 004cc76c ["INT_ADD", "register:40f0:8", ["const:4cc76c:8", "const:4:8"]]
+ 004cc76c ["CALL", null, ["callee:00c586e0:8"]]
- 004a98d4 bytes efc81c94
+ 004cc76c bytes dd2f1e94
- 004a98ec ["INT_ADD", "register:40f0:8", ["const:4a98ec:8", "const:4:8"]]
- 004a98ec ["CALL", null, ["callee:005404ac:8"]]
+ 004cc784 ["INT_ADD", "register:40f0:8", ["const:4cc784:8", "const:4:8"]]
+ 004cc784 ["CALL", null, ["callee:005404ac:8"]]
- 004a98ec bytes 4acf0194
+ 004cc784 bytes 4acf0194
~~~


<a id="compare-82ec40950915b87c192872fe0bd6a705"></a>

### [`004a9924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9924.md) → [`004cc7bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cc/004cc7bc.md) _ZN5Botan10hex_decodeEPKcmb

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc300.md) · 呼出先 6件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c58d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d50.md) · 呼出先 6件 [`0049f3ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004a9964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9924.md#insn-004a9964) · [`004a9980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9924.md#insn-004a9980) · [`004a9998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004a9/004a9924.md#insn-004a9998)
- 新版 `004cc7fc`（命令位置の公開資料なし） · `004cc818`（命令位置の公開資料なし） · `004cc830`（命令位置の公開資料なし）

~~~diff
- 004a9964 ["INT_ADD", "register:40f0:8", ["const:4a9964:8", "const:4:8"]]
- 004a9964 ["CALL", null, ["callee:00c57a90:8"]]
+ 004cc7fc ["INT_ADD", "register:40f0:8", ["const:4cc7fc:8", "const:4:8"]]
+ 004cc7fc ["CALL", null, ["callee:00c57a90:8"]]
- 004a9964 bytes b7c51c94
+ 004cc7fc bytes a52c1e94
- 004a9980 ["INT_ADD", "register:40f0:8", ["const:4a9980:8", "const:4:8"]]
- 004a9980 ["CALL", null, ["callee:00c57c90:8"]]
+ 004cc818 ["INT_ADD", "register:40f0:8", ["const:4cc818:8", "const:4:8"]]
+ 004cc818 ["CALL", null, ["callee:00c57c90:8"]]
- 004a9980 bytes 30c61c94
+ 004cc818 bytes 1e2d1e94
- 004a9998 ["INT_ADD", "register:40f0:8", ["const:4a9998:8", "const:4:8"]]
- 004a9998 ["CALL", null, ["callee:00c586e0:8"]]
+ 004cc830 ["INT_ADD", "register:40f0:8", ["const:4cc830:8", "const:4:8"]]
+ 004cc830 ["CALL", null, ["callee:00c586e0:8"]]
- 004a9998 bytes bec81c94
+ 004cc830 bytes ac2f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31550c7dcdac742ff48a95ba5b0bd5f6"></a>

### [`004aa268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa268.md) → [`004cd100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd100.md) _ZN5Botan4HMAC5clearEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdc330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc330.md) · 呼出先 2件 [`0051dca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dca0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c58d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d80.md) · 呼出先 2件 [`00540b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540b38.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004aa284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa268.md#insn-004aa284) · [`004aa29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa268.md#insn-004aa29c) · [`004aa2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa268.md#insn-004aa2ac)
- 新版 `004cd11c`（命令位置の公開資料なし） · `004cd134`（命令位置の公開資料なし） · `004cd144`（命令位置の公開資料なし）

~~~diff
- 004aa284 ["COPY", "register:0:8", ["register:4040:8"]]
- 004aa284 ["INT_ADD", "register:40f0:8", ["const:4aa284:8", "const:4:8"]]
- 004aa284 ["CALLIND", null, ["register:0:8"]]
+ 004cd11c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cd11c ["INT_ADD", "register:40f0:8", ["const:4cd11c:8", "const:4:8"]]
+ 004cd11c ["CALLIND", null, ["register:0:8"]]
- 004aa284 bytes 00013fd6
+ 004cd11c bytes 00013fd6
- 004aa29c ["INT_ADD", "register:40f0:8", ["const:4aa29c:8", "const:4:8"]]
- 004aa29c ["CALL", null, ["callee:00c57c90:8"]]
+ 004cd134 ["INT_ADD", "register:40f0:8", ["const:4cd134:8", "const:4:8"]]
+ 004cd134 ["CALL", null, ["callee:00c57c90:8"]]
- 004aa29c bytes e9c31c94
+ 004cd134 bytes d72a1e94
- 004aa2ac ["INT_ADD", "register:40f0:8", ["const:4aa2ac:8", "const:4:8"]]
- 004aa2ac ["CALL", null, ["callee:00540b38:8"]]
+ 004cd144 ["INT_ADD", "register:40f0:8", ["const:4cd144:8", "const:4:8"]]
+ 004cd144 ["CALL", null, ["callee:00540b38:8"]]
- 004aa2ac bytes 7dce0194
+ 004cd144 bytes 7dce0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-032d0ad11522f9b0ffcfaa04d8f85d95"></a>

### [`004aa624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa624.md) → [`004cd4bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd4bc.md) _ZN5Botan3KDF6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc360.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbef0.md)
- 新版 呼出元 1件 [`00c58db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58db0.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004aa66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa624.md#insn-004aa66c) · [`004aa678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa624.md#insn-004aa678) · [`004aa688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa624.md#insn-004aa688)
- 新版 `004cd504`（命令位置の公開資料なし） · `004cd510`（命令位置の公開資料なし） · `004cd520`（命令位置の公開資料なし）

~~~diff
- 004aa66c ["INT_ADD", "register:40f0:8", ["const:4aa66c:8", "const:4:8"]]
- 004aa66c ["CALL", null, ["callee:0043bae0:8"]]
+ 004cd504 ["INT_ADD", "register:40f0:8", ["const:4cd504:8", "const:4:8"]]
+ 004cd504 ["CALL", null, ["callee:0043bae0:8"]]
- 004aa66c bytes 5dbafd97
+ 004cd504 bytes 77b9fd97
- 004aa678 ["INT_ADD", "register:40f0:8", ["const:4aa678:8", "const:4:8"]]
- 004aa678 ["CALL", null, ["callee:00c58940:8"]]
+ 004cd510 ["INT_ADD", "register:40f0:8", ["const:4cd510:8", "const:4:8"]]
+ 004cd510 ["CALL", null, ["callee:00c58940:8"]]
- 004aa678 bytes 1ec61c94
+ 004cd510 bytes 0c2d1e94
- 004aa688 ["INT_ADD", "register:40f0:8", ["const:4aa688:8", "const:4:8"]]
- 004aa688 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004cd520 ["INT_ADD", "register:40f0:8", ["const:4cd520:8", "const:4:8"]]
+ 004cd520 ["CALL", null, ["callee:00c57ab0:8"]]
- 004aa688 bytes 76c21c94
+ 004cd520 bytes 64291e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-777534e2e71e28d64693c2263e99e594"></a>

### [`004aa8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa8b0.md) → [`004cd748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd748.md) _ZN5Botan3KDF9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004aa9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa9d0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004cd868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd868.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004aa8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa8b0.md#insn-004aa8fc) · [`004aa90c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa8b0.md#insn-004aa90c) · [`004aa948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa8b0.md#insn-004aa948)
- 新版 `004cd794`（命令位置の公開資料なし） · `004cd7a4`（命令位置の公開資料なし） · `004cd7e0`（命令位置の公開資料なし）

~~~diff
- 004aa8fc ["INT_ADD", "register:40f0:8", ["const:4aa8fc:8", "const:4:8"]]
- 004aa8fc ["CALL", null, ["callee:00473500:8"]]
+ 004cd794 ["INT_ADD", "register:40f0:8", ["const:4cd794:8", "const:4:8"]]
+ 004cd794 ["CALL", null, ["callee:00473500:8"]]
- 004aa8fc bytes 5b97fe97
+ 004cd794 bytes 5b97fe97
- 004aa90c ["INT_ADD", "register:40f0:8", ["const:4aa90c:8", "const:4:8"]]
- 004aa90c ["CALL", null, ["callee:004cd868:8"]]
+ 004cd7a4 ["INT_ADD", "register:40f0:8", ["const:4cd7a4:8", "const:4:8"]]
+ 004cd7a4 ["CALL", null, ["callee:004cd868:8"]]
- 004aa90c bytes 31000094
+ 004cd7a4 bytes 31000094
- 004aa948 ["INT_ADD", "register:40f0:8", ["const:4aa948:8", "const:4:8"]]
- 004aa948 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004cd7e0 ["INT_ADD", "register:40f0:8", ["const:4cd7e0:8", "const:4:8"]]
+ 004cd7e0 ["CALL", null, ["callee:00c57ab0:8"]]
- 004aa948 bytes c6c11c94
+ 004cd7e0 bytes b4281e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7864922d10e89fd3912faeb8bc57d15d"></a>

### [`004aa9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa9d0.md) → [`004cd868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd868.md) FUN_004cd868

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004aa8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa8b0.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc360.md)
- 新版 呼出元 1件 [`004cd748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cd/004cd748.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58db0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004aaa20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa9d0.md#insn-004aaa20) · [`004aaa34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa9d0.md#insn-004aaa34) · [`004aaa4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004aa/004aa9d0.md#insn-004aaa4c)
- 新版 `004cd8b8`（命令位置の公開資料なし） · `004cd8cc`（命令位置の公開資料なし） · `004cd8e4`（命令位置の公開資料なし）

~~~diff
- 004aaa20 ["INT_ADD", "register:40f0:8", ["const:4aaa20:8", "const:4:8"]]
- 004aaa20 ["CALL", null, ["callee:00540d3c:8"]]
+ 004cd8b8 ["INT_ADD", "register:40f0:8", ["const:4cd8b8:8", "const:4:8"]]
+ 004cd8b8 ["CALL", null, ["callee:00540d3c:8"]]
- 004aaa20 bytes 21cd0194
+ 004cd8b8 bytes 21cd0194
- 004aaa34 ["COPY", "register:0:8", ["register:4040:8"]]
- 004aaa34 ["INT_ADD", "register:40f0:8", ["const:4aaa34:8", "const:4:8"]]
- 004aaa34 ["CALLIND", null, ["register:0:8"]]
+ 004cd8cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cd8cc ["INT_ADD", "register:40f0:8", ["const:4cd8cc:8", "const:4:8"]]
+ 004cd8cc ["CALLIND", null, ["register:0:8"]]
- 004aaa34 bytes 00013fd6
+ 004cd8cc bytes 00013fd6
- 004aaa4c ["INT_ADD", "register:40f0:8", ["const:4aaa4c:8", "const:4:8"]]
- 004aaa4c ["CALL", null, ["callee:00c58db0:8"]]
+ 004cd8e4 ["INT_ADD", "register:40f0:8", ["const:4cd8e4:8", "const:4:8"]]
+ 004cd8e4 ["CALL", null, ["callee:00c58db0:8"]]
- 004aaa4c bytes 45c61c94
+ 004cd8e4 bytes 332d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5b7631145b2f4fc9b65f0db2c452e85"></a>

### [`004ab178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab178.md) → [`004ce010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce010.md) _ZNK5Botan16PK_Encryptor_EME18maximum_input_sizeEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ab18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab178.md#insn-004ab18c)
- 新版 `004ce024`（命令位置の公開資料なし）

~~~diff
- 004ab18c ["COPY", "register:0:8", ["register:4040:8"]]
- 004ab18c ["INT_ADD", "register:40f0:8", ["const:4ab18c:8", "const:4:8"]]
- 004ab18c ["CALLIND", null, ["register:0:8"]]
+ 004ce024 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ce024 ["INT_ADD", "register:40f0:8", ["const:4ce024:8", "const:4:8"]]
+ 004ce024 ["CALLIND", null, ["register:0:8"]]
- 004ab18c bytes 00013fd6
+ 004ce024 bytes 00013fd6
~~~


<a id="compare-e67be17b815aa5d517a7ad9f52210aec"></a>

### [`004ab6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab6ac.md) → [`004ce544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce544.md) _ZN5Botan25MessageAuthenticationCode9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004ab810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab810.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004ce6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce6a8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ab71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab6ac.md#insn-004ab71c) · [`004ab72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab6ac.md#insn-004ab72c) · [`004ab768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab6ac.md#insn-004ab768)
- 新版 `004ce5b4`（命令位置の公開資料なし） · `004ce5c4`（命令位置の公開資料なし） · `004ce600`（命令位置の公開資料なし）

~~~diff
- 004ab71c ["INT_ADD", "register:40f0:8", ["const:4ab71c:8", "const:4:8"]]
- 004ab71c ["CALL", null, ["callee:00473500:8"]]
+ 004ce5b4 ["INT_ADD", "register:40f0:8", ["const:4ce5b4:8", "const:4:8"]]
+ 004ce5b4 ["CALL", null, ["callee:00473500:8"]]
- 004ab71c bytes d393fe97
+ 004ce5b4 bytes d393fe97
- 004ab72c ["INT_ADD", "register:40f0:8", ["const:4ab72c:8", "const:4:8"]]
- 004ab72c ["CALL", null, ["callee:004ce6a8:8"]]
+ 004ce5c4 ["INT_ADD", "register:40f0:8", ["const:4ce5c4:8", "const:4:8"]]
+ 004ce5c4 ["CALL", null, ["callee:004ce6a8:8"]]
- 004ab72c bytes 39000094
+ 004ce5c4 bytes 39000094
- 004ab768 ["INT_ADD", "register:40f0:8", ["const:4ab768:8", "const:4:8"]]
- 004ab768 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004ce600 ["INT_ADD", "register:40f0:8", ["const:4ce600:8", "const:4:8"]]
+ 004ce600 ["CALL", null, ["callee:00c57ab0:8"]]
- 004ab768 bytes 3ebe1c94
+ 004ce600 bytes 2c251e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d14bc0ea8a7370fd9ec14ea0dbc40795"></a>

### [`004ab810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab810.md) → [`004ce6a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce6a8.md) FUN_004ce6a8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004ab6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab6ac.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdc040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc040.md)
- 新版 呼出元 1件 [`004ce544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004ce544.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ab860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab810.md#insn-004ab860) · [`004ab874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab810.md#insn-004ab874) · [`004ab890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004ab810.md#insn-004ab890)
- 新版 `004ce6f8`（命令位置の公開資料なし） · `004ce70c`（命令位置の公開資料なし） · `004ce728`（命令位置の公開資料なし）

~~~diff
- 004ab860 ["INT_ADD", "register:40f0:8", ["const:4ab860:8", "const:4:8"]]
- 004ab860 ["CALL", null, ["callee:00540d3c:8"]]
+ 004ce6f8 ["INT_ADD", "register:40f0:8", ["const:4ce6f8:8", "const:4:8"]]
+ 004ce6f8 ["CALL", null, ["callee:00540d3c:8"]]
- 004ab860 bytes 91c90194
+ 004ce6f8 bytes 91c90194
- 004ab874 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ab874 ["INT_ADD", "register:40f0:8", ["const:4ab874:8", "const:4:8"]]
- 004ab874 ["CALLIND", null, ["register:0:8"]]
+ 004ce70c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ce70c ["INT_ADD", "register:40f0:8", ["const:4ce70c:8", "const:4:8"]]
+ 004ce70c ["CALLIND", null, ["register:0:8"]]
- 004ab874 bytes 00013fd6
+ 004ce70c bytes 00013fd6
- 004ab890 ["INT_ADD", "register:40f0:8", ["const:4ab890:8", "const:4:8"]]
- 004ab890 ["CALL", null, ["callee:00c58a90:8"]]
+ 004ce728 ["INT_ADD", "register:40f0:8", ["const:4ce728:8", "const:4:8"]]
+ 004ce728 ["CALL", null, ["callee:00c58a90:8"]]
- 004ab890 bytes ecc11c94
+ 004ce728 bytes da281e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ea37b128ac8593fb2faf48b576c957e"></a>

### [`004abba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004abba0.md) → [`004cea38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ce/004cea38.md) _ZN5Botan3MD510compress_nEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ac5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ab/004abba0.md#insn-004ac5b8)
- 新版 `004cf450`（命令位置の公開資料なし）

~~~diff
- 004ac5b8 ["INT_ADD", "register:40f0:8", ["const:4ac5b8:8", "const:4:8"]]
- 004ac5b8 ["CALL", null, ["callee:00c57c00:8"]]
+ 004cf450 ["INT_ADD", "register:40f0:8", ["const:4cf450:8", "const:4:8"]]
+ 004cf450 ["CALL", null, ["callee:00c57c00:8"]]
- 004ac5b8 bytes feba1c94
+ 004cf450 bytes ec211e94
~~~


<a id="compare-3e67a07c730a74f5492fff456551a1af"></a>

### [`004ac678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac678.md) → [`004cf510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf510.md) _ZN5Botan16MDx_HashFunction5clearEv

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ac69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac678.md#insn-004ac69c)
- 新版 `004cf534`（命令位置の公開資料なし）

~~~diff
- 004ac69c ["INT_ADD", "register:40f0:8", ["const:4ac69c:8", "const:4:8"]]
- 004ac69c ["CALL", null, ["callee:00c57c90:8"]]
+ 004cf534 ["INT_ADD", "register:40f0:8", ["const:4cf534:8", "const:4:8"]]
+ 004cf534 ["CALL", null, ["callee:00c57c90:8"]]
- 004ac69c bytes e9ba1c94
+ 004cf534 bytes d7211e94
~~~


<a id="compare-dd7230d22f473f686ad11e7e64f889e4"></a>

### [`004ac704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac704.md) → [`004cf59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf59c.md) _ZN5Botan16MDx_HashFunction8add_dataEPKhm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ac754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac704.md#insn-004ac754) · [`004ac780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac704.md#insn-004ac780) · [`004ac7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac704.md#insn-004ac7d4)
- 新版 `004cf5ec`（命令位置の公開資料なし） · `004cf618`（命令位置の公開資料なし） · `004cf66c`（命令位置の公開資料なし）

~~~diff
- 004ac754 ["INT_ADD", "register:40f0:8", ["const:4ac754:8", "const:4:8"]]
- 004ac754 ["CALL", null, ["callee:00c57b40:8"]]
+ 004cf5ec ["INT_ADD", "register:40f0:8", ["const:4cf5ec:8", "const:4:8"]]
+ 004cf5ec ["CALL", null, ["callee:00c57b40:8"]]
- 004ac754 bytes 67ba1c94
+ 004cf5ec bytes 55211e94
- 004ac780 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ac780 ["INT_ADD", "register:40f0:8", ["const:4ac780:8", "const:4:8"]]
- 004ac780 ["CALLIND", null, ["register:0:8"]]
+ 004cf618 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cf618 ["INT_ADD", "register:40f0:8", ["const:4cf618:8", "const:4:8"]]
+ 004cf618 ["CALLIND", null, ["register:0:8"]]
- 004ac780 bytes 00013fd6
+ 004cf618 bytes 00013fd6
- 004ac7d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ac7d4 ["INT_ADD", "register:40f0:8", ["const:4ac7d4:8", "const:4:8"]]
- 004ac7d4 ["CALLIND", null, ["register:0:8"]]
+ 004cf66c ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cf66c ["INT_ADD", "register:40f0:8", ["const:4cf66c:8", "const:4:8"]]
+ 004cf66c ["CALLIND", null, ["register:0:8"]]
- 004ac7d4 bytes 00013fd6
+ 004cf66c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11d27fa1c6c4be004cd277a463242878"></a>

### [`004ac830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac830.md) → [`004cf6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cf6c8.md) _ZN5Botan16MDx_HashFunction12final_resultEPh

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ac8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac830.md#insn-004ac8bc) · [`004ac8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac830.md#insn-004ac8d0) · [`004ac8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004ac830.md#insn-004ac8ec)
- 新版 `004cf754`（命令位置の公開資料なし） · `004cf768`（命令位置の公開資料なし） · `004cf784`（命令位置の公開資料なし）

~~~diff
- 004ac8bc ["COPY", "register:0:8", ["register:4048:8"]]
- 004ac8bc ["INT_ADD", "register:40f0:8", ["const:4ac8bc:8", "const:4:8"]]
- 004ac8bc ["CALLIND", null, ["register:0:8"]]
+ 004cf754 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004cf754 ["INT_ADD", "register:40f0:8", ["const:4cf754:8", "const:4:8"]]
+ 004cf754 ["CALLIND", null, ["register:0:8"]]
- 004ac8bc bytes 20013fd6
+ 004cf754 bytes 20013fd6
- 004ac8d0 ["INT_ADD", "register:40f0:8", ["const:4ac8d0:8", "const:4:8"]]
- 004ac8d0 ["CALL", null, ["callee:00c57c90:8"]]
+ 004cf768 ["INT_ADD", "register:40f0:8", ["const:4cf768:8", "const:4:8"]]
+ 004cf768 ["CALL", null, ["callee:00c57c90:8"]]
- 004ac8d0 bytes 5cba1c94
+ 004cf768 bytes 4a211e94
- 004ac8ec ["COPY", "register:0:8", ["register:4040:8"]]
- 004ac8ec ["INT_ADD", "register:40f0:8", ["const:4ac8ec:8", "const:4:8"]]
- 004ac8ec ["CALLIND", null, ["register:0:8"]]
+ 004cf784 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004cf784 ["INT_ADD", "register:40f0:8", ["const:4cf784:8", "const:4:8"]]
+ 004cf784 ["CALLIND", null, ["register:0:8"]]
- 004ac8ec bytes 00013fd6
+ 004cf784 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-615a0e1145e2b0f240e712c66b0fe069"></a>

### [`004acef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acef0.md) → [`004cfd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004cf/004cfd88.md) _ZNK5Botan13PKCS7_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00521e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521e04.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00544c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544c9c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004acf5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acef0.md#insn-004acf5c) · [`004acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ac/004acef0.md#insn-004acf88)
- 新版 `004cfdf4`（命令位置の公開資料なし） · `004cfe20`（命令位置の公開資料なし）

~~~diff
- 004acf5c ["INT_ADD", "register:40f0:8", ["const:4acf5c:8", "const:4:8"]]
- 004acf5c ["CALL", null, ["callee:00544c9c:8"]]
+ 004cfdf4 ["INT_ADD", "register:40f0:8", ["const:4cfdf4:8", "const:4:8"]]
+ 004cfdf4 ["CALL", null, ["callee:00544c9c:8"]]
- 004acf5c bytes aad30194
+ 004cfdf4 bytes aad30194
- 004acf88 ["INT_ADD", "register:40f0:8", ["const:4acf88:8", "const:4:8"]]
- 004acf88 ["CALL", null, ["callee:00c57ae0:8"]]
+ 004cfe20 ["INT_ADD", "register:40f0:8", ["const:4cfe20:8", "const:4:8"]]
+ 004cfe20 ["CALL", null, ["callee:00c57ae0:8"]]
- 004acf88 bytes 42b81c94
+ 004cfe20 bytes 301f1e94
~~~


<a id="compare-8b8eb7bd8c601774db13581858646d99"></a>

### [`004ad3b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad3b4.md) → [`004d024c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d024c.md) _ZNK5Botan17ANSI_X923_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0051e2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e2cc.md) [`00521e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00521/00521e04.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00541164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00544c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00544/00544c9c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ad404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad3b4.md#insn-004ad404) · [`004ad450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad3b4.md#insn-004ad450) · [`004ad47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad3b4.md#insn-004ad47c)
- 新版 `004d029c`（命令位置の公開資料なし） · `004d02e8`（命令位置の公開資料なし） · `004d0314`（命令位置の公開資料なし）

~~~diff
- 004ad404 ["INT_ADD", "register:40f0:8", ["const:4ad404:8", "const:4:8"]]
- 004ad404 ["CALL", null, ["callee:00541164:8"]]
+ 004d029c ["INT_ADD", "register:40f0:8", ["const:4d029c:8", "const:4:8"]]
+ 004d029c ["CALL", null, ["callee:00541164:8"]]
- 004ad404 bytes b2c30194
+ 004d029c bytes b2c30194
- 004ad450 ["INT_ADD", "register:40f0:8", ["const:4ad450:8", "const:4:8"]]
- 004ad450 ["CALL", null, ["callee:00544c9c:8"]]
+ 004d02e8 ["INT_ADD", "register:40f0:8", ["const:4d02e8:8", "const:4:8"]]
+ 004d02e8 ["CALL", null, ["callee:00544c9c:8"]]
- 004ad450 bytes 6dd20194
+ 004d02e8 bytes 6dd20194
- 004ad47c ["INT_ADD", "register:40f0:8", ["const:4ad47c:8", "const:4:8"]]
- 004ad47c ["CALL", null, ["callee:00c57ae0:8"]]
+ 004d0314 ["INT_ADD", "register:40f0:8", ["const:4d0314:8", "const:4:8"]]
+ 004d0314 ["CALL", null, ["callee:00c57ae0:8"]]
- 004ad47c bytes 05b71c94
+ 004d0314 bytes f31d1e94
~~~


<a id="compare-c06b37edc7cbf5e2f64c5fedda9d3abb"></a>

### [`004ad87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad87c.md) → [`004d0714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0714.md) _ZNK5Botan19OneAndZeros_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051e2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e2cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00541164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ad8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad87c.md#insn-004ad8cc) · [`004ad920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad87c.md#insn-004ad920) · [`004ad94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad87c.md#insn-004ad94c)
- 新版 `004d0764`（命令位置の公開資料なし） · `004d07b8`（命令位置の公開資料なし） · `004d07e4`（命令位置の公開資料なし）

~~~diff
- 004ad8cc ["INT_ADD", "register:40f0:8", ["const:4ad8cc:8", "const:4:8"]]
- 004ad8cc ["CALL", null, ["callee:00541164:8"]]
+ 004d0764 ["INT_ADD", "register:40f0:8", ["const:4d0764:8", "const:4:8"]]
+ 004d0764 ["CALL", null, ["callee:00541164:8"]]
- 004ad8cc bytes 80c20194
+ 004d0764 bytes 80c20194
- 004ad920 ["INT_ADD", "register:40f0:8", ["const:4ad920:8", "const:4:8"]]
- 004ad920 ["CALL", null, ["callee:00541164:8"]]
+ 004d07b8 ["INT_ADD", "register:40f0:8", ["const:4d07b8:8", "const:4:8"]]
+ 004d07b8 ["CALL", null, ["callee:00541164:8"]]
- 004ad920 bytes 6bc20194
+ 004d07b8 bytes 6bc20194
- 004ad94c ["INT_ADD", "register:40f0:8", ["const:4ad94c:8", "const:4:8"]]
- 004ad94c ["CALL", null, ["callee:00c57ae0:8"]]
+ 004d07e4 ["INT_ADD", "register:40f0:8", ["const:4d07e4:8", "const:4:8"]]
+ 004d07e4 ["CALL", null, ["callee:00c57ae0:8"]]
- 004ad94c bytes d1b51c94
+ 004d07e4 bytes bf1c1e94
~~~


<a id="compare-8b6aefaf5a334305662b9b4bd064585c"></a>

### [`004ad9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad9f4.md) → [`004d088c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d088c.md) _ZNK5Botan11ESP_Padding11add_paddingERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEmm

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0051e2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e2cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00541164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00541/00541164.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004ada34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad9f4.md#insn-004ada34) · [`004ada84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ad9f4.md#insn-004ada84)
- 新版 `004d08cc`（命令位置の公開資料なし） · `004d091c`（命令位置の公開資料なし）

~~~diff
- 004ada34 ["INT_ADD", "register:40f0:8", ["const:4ada34:8", "const:4:8"]]
- 004ada34 ["CALL", null, ["callee:00541164:8"]]
+ 004d08cc ["INT_ADD", "register:40f0:8", ["const:4d08cc:8", "const:4:8"]]
+ 004d08cc ["CALL", null, ["callee:00541164:8"]]
- 004ada34 bytes 26c20194
+ 004d08cc bytes 26c20194
- 004ada84 ["INT_ADD", "register:40f0:8", ["const:4ada84:8", "const:4:8"]]
- 004ada84 ["CALL", null, ["callee:00c57ae0:8"]]
+ 004d091c ["INT_ADD", "register:40f0:8", ["const:4d091c:8", "const:4:8"]]
+ 004d091c ["CALL", null, ["callee:00c57ae0:8"]]
- 004ada84 bytes 83b51c94
+ 004d091c bytes 711c1e94
~~~


<a id="compare-6a174f06bfc720e4263da5af1de7faf0"></a>

### [`004ade98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ade98.md) → [`004d0d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d0/004d0d30.md) _ZN5Botan12StreamCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdc010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc010.md) · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbef0.md)
- 新版 呼出元 1件 [`00c58a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58a60.md) · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c58940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004adee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ade98.md#insn-004adee0) · [`004adeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ade98.md#insn-004adeec) · [`004adefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ad/004ade98.md#insn-004adefc)
- 新版 `004d0d78`（命令位置の公開資料なし） · `004d0d84`（命令位置の公開資料なし） · `004d0d94`（命令位置の公開資料なし）

~~~diff
- 004adee0 ["INT_ADD", "register:40f0:8", ["const:4adee0:8", "const:4:8"]]
- 004adee0 ["CALL", null, ["callee:0043bae0:8"]]
+ 004d0d78 ["INT_ADD", "register:40f0:8", ["const:4d0d78:8", "const:4:8"]]
+ 004d0d78 ["CALL", null, ["callee:0043bae0:8"]]
- 004adee0 bytes 40acfd97
+ 004d0d78 bytes 5aabfd97
- 004adeec ["INT_ADD", "register:40f0:8", ["const:4adeec:8", "const:4:8"]]
- 004adeec ["CALL", null, ["callee:00c58940:8"]]
+ 004d0d84 ["INT_ADD", "register:40f0:8", ["const:4d0d84:8", "const:4:8"]]
+ 004d0d84 ["CALL", null, ["callee:00c58940:8"]]
- 004adeec bytes 01b81c94
+ 004d0d84 bytes ef1e1e94
- 004adefc ["INT_ADD", "register:40f0:8", ["const:4adefc:8", "const:4:8"]]
- 004adefc ["CALL", null, ["callee:00c57ab0:8"]]
+ 004d0d94 ["INT_ADD", "register:40f0:8", ["const:4d0d94:8", "const:4:8"]]
+ 004d0d94 ["CALL", null, ["callee:00c57ab0:8"]]
- 004adefc bytes 59b41c94
+ 004d0d94 bytes 471b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed7fe520b3af5899ef17263cec58536c"></a>

### [`004aed68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004aed68.md) → [`004d1c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1c00.md) _ZN5Botan11Cipher_Mode9providersERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x22e98` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00540d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00540/00540d3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004aede0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004aed68.md#insn-004aede0) · [`004aedf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004aed68.md#insn-004aedf0) · [`004aee00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ae/004aed68.md#insn-004aee00)
- 新版 `004d1c78`（命令位置の公開資料なし） · `004d1c88`（命令位置の公開資料なし） · `004d1c98`（命令位置の公開資料なし）

~~~diff
- 004aede0 ["INT_ADD", "register:40f0:8", ["const:4aede0:8", "const:4:8"]]
- 004aede0 ["CALL", null, ["callee:00473500:8"]]
+ 004d1c78 ["INT_ADD", "register:40f0:8", ["const:4d1c78:8", "const:4:8"]]
+ 004d1c78 ["CALL", null, ["callee:00473500:8"]]
- 004aede0 bytes 2286fe97
+ 004d1c78 bytes 2286fe97
- 004aedf0 ["INT_ADD", "register:40f0:8", ["const:4aedf0:8", "const:4:8"]]
- 004aedf0 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004d1c88 ["INT_ADD", "register:40f0:8", ["const:4d1c88:8", "const:4:8"]]
+ 004d1c88 ["CALL", null, ["callee:00c57ab0:8"]]
- 004aedf0 bytes 9cb01c94
+ 004d1c88 bytes 8a171e94
- 004aee00 ["INT_ADD", "register:40f0:8", ["const:4aee00:8", "const:4:8"]]
- 004aee00 ["CALL", null, ["callee:00c57ab0:8"]]
+ 004d1c98 ["INT_ADD", "register:40f0:8", ["const:4d1c98:8", "const:4:8"]]
+ 004d1c98 ["CALL", null, ["callee:00c57ab0:8"]]
- 004aee00 bytes 98b01c94
+ 004d1c98 bytes 86171e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f01564794bd8f5d2f020ebeceeeb6530"></a>

### [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) → [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) FUN_004d6e28

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00494d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494d38.md) [`0049731c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/0049731c.md) [`004b87c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b87c8.md) [`004bc804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bc/004bc804.md) [`004bd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bd/004bd550.md) · 呼出先 10件 [`00496208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496208.md) [`004af0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af0b8.md) [`004af4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af4c4.md) [`004afcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004afcb8.md) [`004b088c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b0/004b088c.md)
- 新版 呼出元 5件 [`004b7bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b7/004b7bd0.md) [`004ba1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004ba1b4.md) [`004db660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004db/004db660.md) [`004df69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004df/004df69c.md) [`004e03e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e0/004e03e8.md) · 呼出先 10件 [`004b90a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b9/004b90a0.md) [`004d1f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d1/004d1f50.md) [`004d235c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d235c.md) [`004d2b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d2b50.md) [`004d3724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d3/004d3724.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b3fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md#insn-004b3fdc) · [`004b41d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md#insn-004b41d4)
- 新版 `004d6e74`（命令位置の公開資料なし） · `004d706c`（命令位置の公開資料なし）

~~~diff
- 004b3fdc ["INT_ADD", "register:40f0:8", ["const:4b3fdc:8", "const:4:8"]]
- 004b3fdc ["CALL", null, ["callee:00c57c90:8"]]
+ 004d6e74 ["INT_ADD", "register:40f0:8", ["const:4d6e74:8", "const:4:8"]]
+ 004d6e74 ["CALL", null, ["callee:00c57c90:8"]]
- 004b3fdc bytes 999c1c94
+ 004d6e74 bytes 87031e94
- 004b41d4 ["INT_ADD", "register:40f0:8", ["const:4b41d4:8", "const:4:8"]]
- 004b41d4 ["CALL", null, ["callee:004d727c:8"]]
+ 004d706c ["INT_ADD", "register:40f0:8", ["const:4d706c:8", "const:4:8"]]
+ 004d706c ["CALL", null, ["callee:004d727c:8"]]
- 004b41d4 bytes 84000094
+ 004d706c bytes 84000094
~~~


<a id="compare-b3cc5eb1e733bf205105797816a0f899"></a>

### [`004b423c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b423c.md) → [`004d70d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d70d4.md) FUN_004d70d4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 4件 [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`004b44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) [`004b47ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b47ec.md) [`004b4a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md) · 呼出先 1件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 4件 [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) [`004d7684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7684.md) [`004d78c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d78c8.md) · 呼出先 1件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b4278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b423c.md#insn-004b4278)
- 新版 `004d7110`（命令位置の公開資料なし）

~~~diff
- 004b4278 ["INT_ADD", "register:40f0:8", ["const:4b4278:8", "const:4:8"]]
- 004b4278 ["CALL", null, ["callee:00c57c90:8"]]
+ 004d7110 ["INT_ADD", "register:40f0:8", ["const:4d7110:8", "const:4:8"]]
+ 004d7110 ["CALL", null, ["callee:00c57c90:8"]]
- 004b4278 bytes f29b1c94
+ 004d7110 bytes e0021e94
~~~


<a id="compare-567a1d3b4f5c0f4d41f1c1f3adb81698"></a>

### [`004b44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) → [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) FUN_004d7350

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`004b44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) · 呼出先 11件 [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00495a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md) [`00495c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495c94.md) [`004af4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004af4c4.md) [`004afcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004af/004afcb8.md)
- 新版 呼出元 2件 [`004d6e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d6/004d6e28.md) [`004d7350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d7/004d7350.md) · 呼出先 11件 [`004b8774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8774.md) [`004b890c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b890c.md) [`004b8b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004b8/004b8b2c.md) [`004d235c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d235c.md) [`004d2b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004d2/004d2b50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`004b4510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md#insn-004b4510) · [`004b4528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md#insn-004b4528) · [`004b4540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md#insn-004b4540)
- 新版 `004d73a8`（命令位置の公開資料なし） · `004d73c0`（命令位置の公開資料なし） · `004d73d8`（命令位置の公開資料なし）

~~~diff
- 004b4510 ["INT_ADD", "register:40f0:8", ["const:4b4510:8", "const:4:8"]]
- 004b4510 ["CALL", null, ["callee:004b8774:8"]]
+ 004d73a8 ["INT_ADD", "register:40f0:8", ["const:4d73a8:8", "const:4:8"]]
+ 004d73a8 ["CALL", null, ["callee:004b8774:8"]]
- 004b4510 bytes f384ff97
+ 004d73a8 bytes f384ff97
- 004b4528 ["INT_ADD", "register:40f0:8", ["const:4b4528:8", "const:4:8"]]
- 004b4528 ["CALL", null, ["callee:004b8774:8"]]
+ 004d73c0 ["INT_ADD", "register:40f0:8", ["const:4d73c0:8", "const:4:8"]]
+ 004d73c0 ["CALL", null, ["callee:004b8774:8"]]
- 004b4528 bytes ed84ff97
+ 004d73c0 bytes ed84ff97
- 004b4540 ["INT_ADD", "register:40f0:8", ["const:4b4540:8", "const:4:8"]]
- 004b4540 ["CALL", null, ["callee:00c57c90:8"]]
+ 004d73d8 ["INT_ADD", "register:40f0:8", ["const:4d73d8:8", "const:4:8"]]
+ 004d73d8 ["CALL", null, ["callee:00c57c90:8"]]
- 004b4540 bytes 409b1c94
+ 004d73d8 bytes 2e021e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

