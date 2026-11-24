# v16.0.2 → v16.0.3 · 要調査の変更候補 (37)

[一覧の目次](README.md)

<a id="compare-864c5412ae9e534cc10169b5b6222b58"></a>

### [`00be2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2034.md) → [`00be3028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be3028.md) _ZN8firebase4auth4User18GetTokenThreadSafeEb

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0087b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b414.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab40.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0087c3c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087c/0087c3c0.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5baa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5baa0.md) [`00c5bab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bab0.md) [`00c5bb10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bb10.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be2064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2034.md#insn-00be2064) · [`00be206c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2034.md#insn-00be206c) · [`00be2088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2034.md#insn-00be2088)
- 新版 [`00be3058`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be3028.md#insn-00be3058) · [`00be3060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be3028.md#insn-00be3060) · [`00be307c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be3028.md#insn-00be307c)

~~~diff
- 00be2064 ["INT_ADD", "register:40f0:8", ["const:be2064:8", "const:4:8"]]
- 00be2064 ["CALL", null, ["callee:00c5bb10:8"]]
+ 00be3058 ["INT_ADD", "register:40f0:8", ["const:be3058:8", "const:4:8"]]
+ 00be3058 ["CALL", null, ["callee:00c5bb10:8"]]
- 00be2064 bytes b7e20194
+ 00be3058 bytes aee20194
- 00be206c ["INT_ADD", "register:40f0:8", ["const:be206c:8", "const:4:8"]]
- 00be206c ["CALL", null, ["callee:00c5baa0:8"]]
+ 00be3060 ["INT_ADD", "register:40f0:8", ["const:be3060:8", "const:4:8"]]
+ 00be3060 ["CALL", null, ["callee:00c5baa0:8"]]
- 00be206c bytes 99e20194
+ 00be3060 bytes 90e20194
- 00be2088 ["COPY", "register:0:8", ["register:4040:8"]]
- 00be2088 ["INT_ADD", "register:40f0:8", ["const:be2088:8", "const:4:8"]]
- 00be2088 ["CALLIND", null, ["register:0:8"]]
+ 00be307c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00be307c ["INT_ADD", "register:40f0:8", ["const:be307c:8", "const:4:8"]]
+ 00be307c ["CALLIND", null, ["register:0:8"]]
- 00be2088 bytes 00013fd6
+ 00be307c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d5282dbbaab8f437c5b3496ed19f438"></a>

### [`00be227c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be227c.md) → [`00be3270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be3270.md) _ZN8firebase4auth17UserInfoInterfaceD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5ec20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5ec20.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be228c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be227c.md#insn-00be228c)
- 新版 [`00be3280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be3/00be3270.md#insn-00be3280)

~~~diff
- 00be228c ["INT_ADD", "register:40f0:8", ["const:be228c:8", "const:4:8"]]
- 00be228c ["CALL", null, ["callee:00c5ec20:8"]]
+ 00be3280 ["INT_ADD", "register:40f0:8", ["const:be3280:8", "const:4:8"]]
+ 00be3280 ["CALL", null, ["callee:00c5ec20:8"]]
- 00be228c bytes 71ee0194
+ 00be3280 bytes 68ee0194
~~~


<a id="compare-b0348d9aa1d47f79d7c38e129c35755e"></a>

### [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) → [`00be96e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be9/00be96e8.md) FUN_00be96e8

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00be86d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86d4.md) [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) · 呼出先 5件 [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) [`00beefbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beefbc.md) [`00bef3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef3d8.md) [`00bef630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef630.md) [`00c53464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53464.md)
- 新版 呼出元 2件 [`00be96c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be9/00be96c8.md) [`00be96e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be9/00be96e8.md) · 呼出先 5件 [`00be96e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be9/00be96e8.md) [`00beffb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00beffb0.md) [`00bf03cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf03cc.md) [`00bf0624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0624.md) [`00c54458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54458.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be8798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md#insn-00be8798) · [`00be87a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md#insn-00be87a4) · [`00be87c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md#insn-00be87c8)
- 新版 [`00be978c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be9/00be96e8.md#insn-00be978c) · [`00be9798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be9/00be96e8.md#insn-00be9798) · [`00be97bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be9/00be96e8.md#insn-00be97bc)

~~~diff
- 00be8798 ["INT_ADD", "register:40f0:8", ["const:be8798:8", "const:4:8"]]
- 00be8798 ["CALL", null, ["callee:00c54458:8"]]
+ 00be978c ["INT_ADD", "register:40f0:8", ["const:be978c:8", "const:4:8"]]
+ 00be978c ["CALL", null, ["callee:00c54458:8"]]
- 00be8798 bytes 33ab0194
+ 00be978c bytes 33ab0194
- 00be87a4 ["INT_ADD", "register:40f0:8", ["const:be87a4:8", "const:4:8"]]
- 00be87a4 ["CALL", null, ["callee:00c54458:8"]]
+ 00be9798 ["INT_ADD", "register:40f0:8", ["const:be9798:8", "const:4:8"]]
+ 00be9798 ["CALL", null, ["callee:00c54458:8"]]
- 00be87a4 bytes 30ab0194
+ 00be9798 bytes 30ab0194
- 00be87c8 ["INT_ADD", "register:40f0:8", ["const:be87c8:8", "const:4:8"]]
- 00be87c8 ["CALL", null, ["callee:00c54458:8"]]
+ 00be97bc ["INT_ADD", "register:40f0:8", ["const:be97bc:8", "const:4:8"]]
+ 00be97bc ["CALL", null, ["callee:00c54458:8"]]
- 00be87c8 bytes 27ab0194
+ 00be97bc bytes 27ab0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c0d6da22fed632bc8792a5d87d095a5"></a>

### [`00beefbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beefbc.md) → [`00beffb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00beffb0.md) FUN_00beffb0

採用 · 移動量 `+0xff4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) · 呼出先 2件 [`00bef3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef3d8.md) [`00c53464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53464.md)
- 新版 呼出元 1件 [`00be96e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be9/00be96e8.md) · 呼出先 2件 [`00bf03cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf03cc.md) [`00c54458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54458.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef00c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beefbc.md#insn-00bef00c) · [`00bef058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beefbc.md#insn-00bef058) · [`00bef074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beefbc.md#insn-00bef074)
- 新版 [`00bf0000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00beffb0.md#insn-00bf0000) · [`00bf004c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00beffb0.md#insn-00bf004c) · [`00bf0068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00beffb0.md#insn-00bf0068)

~~~diff
- 00bef00c ["INT_ADD", "register:40f0:8", ["const:bef00c:8", "const:4:8"]]
- 00bef00c ["CALL", null, ["callee:00c54458:8"]]
+ 00bf0000 ["INT_ADD", "register:40f0:8", ["const:bf0000:8", "const:4:8"]]
+ 00bf0000 ["CALL", null, ["callee:00c54458:8"]]
- 00bef00c bytes 16910194
+ 00bf0000 bytes 16910194
- 00bef058 ["INT_ADD", "register:40f0:8", ["const:bef058:8", "const:4:8"]]
- 00bef058 ["CALL", null, ["callee:00bf03cc:8"]]
+ 00bf004c ["INT_ADD", "register:40f0:8", ["const:bf004c:8", "const:4:8"]]
+ 00bf004c ["CALL", null, ["callee:00bf03cc:8"]]
- 00bef058 bytes e0000094
+ 00bf004c bytes e0000094
- 00bef074 ["INT_ADD", "register:40f0:8", ["const:bef074:8", "const:4:8"]]
- 00bef074 ["CALL", null, ["callee:00c54458:8"]]
+ 00bf0068 ["INT_ADD", "register:40f0:8", ["const:bf0068:8", "const:4:8"]]
+ 00bf0068 ["CALL", null, ["callee:00c54458:8"]]
- 00bef074 bytes fc900194
+ 00bf0068 bytes fc900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58e858c834c335e76ab8fc69afb4a14e"></a>

### [`00bef3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef3d8.md) → [`00bf03cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf03cc.md) FUN_00bf03cc

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) [`00beefbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beefbc.md) · 呼出先 1件 [`00c53464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53464.md)
- 新版 呼出元 2件 [`00be96e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be9/00be96e8.md) [`00beffb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bef/00beffb0.md) · 呼出先 1件 [`00c54458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54458.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef420`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef3d8.md#insn-00bef420) · [`00bef430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef3d8.md#insn-00bef430) · [`00bef450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef3d8.md#insn-00bef450)
- 新版 [`00bf0414`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf03cc.md#insn-00bf0414) · [`00bf0424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf03cc.md#insn-00bf0424) · [`00bf0444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf03cc.md#insn-00bf0444)

~~~diff
- 00bef420 ["INT_ADD", "register:40f0:8", ["const:bef420:8", "const:4:8"]]
- 00bef420 ["CALL", null, ["callee:00c54458:8"]]
+ 00bf0414 ["INT_ADD", "register:40f0:8", ["const:bf0414:8", "const:4:8"]]
+ 00bf0414 ["CALL", null, ["callee:00c54458:8"]]
- 00bef420 bytes 11900194
+ 00bf0414 bytes 11900194
- 00bef430 ["INT_ADD", "register:40f0:8", ["const:bef430:8", "const:4:8"]]
- 00bef430 ["CALL", null, ["callee:00c54458:8"]]
+ 00bf0424 ["INT_ADD", "register:40f0:8", ["const:bf0424:8", "const:4:8"]]
+ 00bf0424 ["CALL", null, ["callee:00c54458:8"]]
- 00bef430 bytes 0d900194
+ 00bf0424 bytes 0d900194
- 00bef450 ["INT_ADD", "register:40f0:8", ["const:bef450:8", "const:4:8"]]
- 00bef450 ["CALL", null, ["callee:00c54458:8"]]
+ 00bf0444 ["INT_ADD", "register:40f0:8", ["const:bf0444:8", "const:4:8"]]
+ 00bf0444 ["CALL", null, ["callee:00c54458:8"]]
- 00bef450 bytes 05900194
+ 00bf0444 bytes 05900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02c542f2a987843832bb5c30397f0667"></a>

### [`00bef630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef630.md) → [`00bf0624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0624.md) FUN_00bf0624

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) · 呼出先 1件 [`00c53464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53464.md)
- 新版 呼出元 1件 [`00be96e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00be9/00be96e8.md) · 呼出先 1件 [`00c54458`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54458.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef630.md#insn-00bef6d0) · [`00bef6f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef630.md#insn-00bef6f4) · [`00bef710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef630.md#insn-00bef710)
- 新版 [`00bf06c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0624.md#insn-00bf06c4) · [`00bf06e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0624.md#insn-00bf06e8) · [`00bf0704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0624.md#insn-00bf0704)

~~~diff
- 00bef6d0 ["INT_ADD", "register:40f0:8", ["const:bef6d0:8", "const:4:8"]]
- 00bef6d0 ["CALL", null, ["callee:00c54458:8"]]
+ 00bf06c4 ["INT_ADD", "register:40f0:8", ["const:bf06c4:8", "const:4:8"]]
+ 00bf06c4 ["CALL", null, ["callee:00c54458:8"]]
- 00bef6d0 bytes 658f0194
+ 00bf06c4 bytes 658f0194
- 00bef6f4 ["INT_ADD", "register:40f0:8", ["const:bef6f4:8", "const:4:8"]]
- 00bef6f4 ["CALL", null, ["callee:00c54458:8"]]
+ 00bf06e8 ["INT_ADD", "register:40f0:8", ["const:bf06e8:8", "const:4:8"]]
+ 00bf06e8 ["CALL", null, ["callee:00c54458:8"]]
- 00bef6f4 bytes 5c8f0194
+ 00bf06e8 bytes 5c8f0194
- 00bef710 ["INT_ADD", "register:40f0:8", ["const:bef710:8", "const:4:8"]]
- 00bef710 ["CALL", null, ["callee:00c54458:8"]]
+ 00bf0704 ["INT_ADD", "register:40f0:8", ["const:bf0704:8", "const:4:8"]]
+ 00bf0704 ["CALL", null, ["callee:00c54458:8"]]
- 00bef710 bytes 558f0194
+ 00bf0704 bytes 558f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf6cb1f34b0b7acafbbbf9f5ffccbd36"></a>

### [`00befafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befafc.md) → [`00bf0af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0af0.md) _ZSt18uncaught_exceptionv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1c0.md) · 呼出先 1件 [`00c5dfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfd0.md)
- 新版 呼出元 1件 [`00c5e190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5e190.md) · 呼出先 1件 [`00c5efa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5efa0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befb08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befafc.md#insn-00befb08)
- 新版 [`00bf0afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0af0.md#insn-00bf0afc)

~~~diff
- 00befb08 ["INT_ADD", "register:40f0:8", ["const:befb08:8", "const:4:8"]]
- 00befb08 ["CALL", null, ["callee:00c5efa0:8"]]
+ 00bf0afc ["INT_ADD", "register:40f0:8", ["const:bf0afc:8", "const:4:8"]]
+ 00bf0afc ["CALL", null, ["callee:00c5efa0:8"]]
- 00befb08 bytes 32b90194
+ 00bf0afc bytes 29b90194
~~~


<a id="compare-cded7bc4ba445495a8246fdad5e60c45"></a>

### [`00befb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befb4c.md) → [`00bf0b40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0b40.md) _ZNSt13exception_ptraSERKS_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e000.md) · 呼出先 2件 [`00c5dfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfe0.md) [`00c5dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dff0.md)
- 新版 呼出元 1件 [`00c5efd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5efd0.md) · 呼出先 2件 [`00c5efb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5efb0.md) [`00c5efc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5efc0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befb74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befb4c.md#insn-00befb74) · [`00befb7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befb4c.md#insn-00befb7c)
- 新版 [`00bf0b68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0b40.md#insn-00bf0b68) · [`00bf0b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0b40.md#insn-00bf0b70)

~~~diff
- 00befb74 ["INT_ADD", "register:40f0:8", ["const:befb74:8", "const:4:8"]]
- 00befb74 ["CALL", null, ["callee:00c5efc0:8"]]
+ 00bf0b68 ["INT_ADD", "register:40f0:8", ["const:bf0b68:8", "const:4:8"]]
+ 00bf0b68 ["CALL", null, ["callee:00c5efc0:8"]]
- 00befb74 bytes 1fb90194
+ 00bf0b68 bytes 16b90194
- 00befb7c ["INT_ADD", "register:40f0:8", ["const:befb7c:8", "const:4:8"]]
- 00befb7c ["CALL", null, ["callee:00c5efb0:8"]]
+ 00bf0b70 ["INT_ADD", "register:40f0:8", ["const:bf0b70:8", "const:4:8"]]
+ 00bf0b70 ["CALL", null, ["callee:00c5efb0:8"]]
- 00befb7c bytes 19b90194
+ 00bf0b70 bytes 10b90194
~~~


<a id="compare-2e8e47427953bcdcc9daa19b90610ad5"></a>

### [`00befbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befbe4.md) → [`00bf0bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0bd8.md) _ZSt17current_exceptionv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58630.md) · 呼出先 1件 [`00c5e010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e010.md)
- 新版 呼出元 1件 [`00c59600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59600.md) · 呼出先 1件 [`00c5efe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5efe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befbf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befbe4.md#insn-00befbf8)
- 新版 [`00bf0bec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0bd8.md#insn-00bf0bec)

~~~diff
- 00befbf8 ["INT_ADD", "register:40f0:8", ["const:befbf8:8", "const:4:8"]]
- 00befbf8 ["CALL", null, ["callee:00c5efe0:8"]]
+ 00bf0bec ["INT_ADD", "register:40f0:8", ["const:bf0bec:8", "const:4:8"]]
+ 00bf0bec ["CALL", null, ["callee:00c5efe0:8"]]
- 00befbf8 bytes 06b90194
+ 00bf0bec bytes fdb80194
~~~


<a id="compare-9b311461d933756d8eaa74e218b89119"></a>

### [`00befc28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befc28.md) → [`00bf0c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0c1c.md) _ZNSt16nested_exceptionD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5eff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5e/00c5eff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befc28.md#insn-00befc3c)
- 新版 [`00bf0c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0c1c.md#insn-00bf0c30)

~~~diff
- 00befc3c ["INT_ADD", "register:40f0:8", ["const:befc3c:8", "const:4:8"]]
- 00befc3c ["CALL", null, ["callee:00c5eff0:8"]]
+ 00bf0c30 ["INT_ADD", "register:40f0:8", ["const:bf0c30:8", "const:4:8"]]
+ 00bf0c30 ["CALL", null, ["callee:00c5eff0:8"]]
- 00befc3c bytes f9b80194
+ 00bf0c30 bytes f0b80194
~~~


<a id="compare-11909c49f3d2ed48af01eedf1c49d139"></a>

### [`00befc54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befc54.md) → [`00bf0c48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0c48.md) _ZNKSt16nested_exception14rethrow_nestedEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58580.md) [`00c58590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58590.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c59390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59390.md) [`00c59550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59550.md) [`00c59560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59560.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befc78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befc54.md#insn-00befc78) · [`00befc80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befc54.md#insn-00befc80) · [`00befc8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befc54.md#insn-00befc8c)
- 新版 [`00bf0c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0c48.md#insn-00bf0c6c) · [`00bf0c74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0c48.md#insn-00bf0c74) · [`00bf0c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0c48.md#insn-00bf0c80)

~~~diff
- 00befc78 ["INT_ADD", "register:40f0:8", ["const:befc78:8", "const:4:8"]]
- 00befc78 ["CALL", null, ["callee:00c59390:8"]]
+ 00bf0c6c ["INT_ADD", "register:40f0:8", ["const:bf0c6c:8", "const:4:8"]]
+ 00bf0c6c ["CALL", null, ["callee:00c59390:8"]]
- 00befc78 bytes d2a10194
+ 00bf0c6c bytes c9a10194
- 00befc80 ["INT_ADD", "register:40f0:8", ["const:befc80:8", "const:4:8"]]
- 00befc80 ["CALL", null, ["callee:00c590c0:8"]]
+ 00bf0c74 ["INT_ADD", "register:40f0:8", ["const:bf0c74:8", "const:4:8"]]
+ 00bf0c74 ["CALL", null, ["callee:00c590c0:8"]]
- 00befc80 bytes 1ca10194
+ 00bf0c74 bytes 13a10194
- 00befc8c ["INT_ADD", "register:40f0:8", ["const:befc8c:8", "const:4:8"]]
- 00befc8c ["CALL", null, ["callee:00c59550:8"]]
+ 00bf0c80 ["INT_ADD", "register:40f0:8", ["const:bf0c80:8", "const:4:8"]]
+ 00bf0c80 ["CALL", null, ["callee:00c59550:8"]]
- 00befc8c bytes 3da20194
+ 00bf0c80 bytes 34a20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7e2e334ef28575430a17719dd92a284"></a>

### [`00befcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcac.md) → [`00bf0ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0ca0.md) _ZSt17rethrow_exceptionSt13exception_ptr

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58590.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5e030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e030.md)
- 新版 呼出元 1件 [`00c59560`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59560.md) · 呼出先 2件 [`00c590c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590c0.md) [`00c5f000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f000.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befcbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcac.md#insn-00befcbc) · [`00befcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcac.md#insn-00befcc0)
- 新版 [`00bf0cb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0ca0.md#insn-00bf0cb0) · [`00bf0cb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf0/00bf0ca0.md#insn-00bf0cb4)

~~~diff
- 00befcbc ["INT_ADD", "register:40f0:8", ["const:befcbc:8", "const:4:8"]]
- 00befcbc ["CALL", null, ["callee:00c5f000:8"]]
+ 00bf0cb0 ["INT_ADD", "register:40f0:8", ["const:bf0cb0:8", "const:4:8"]]
+ 00bf0cb0 ["CALL", null, ["callee:00c5f000:8"]]
- 00befcbc bytes ddb80194
+ 00bf0cb0 bytes d4b80194
- 00befcc0 ["INT_ADD", "register:40f0:8", ["const:befcc0:8", "const:4:8"]]
- 00befcc0 ["CALL", null, ["callee:00c590c0:8"]]
+ 00bf0cb4 ["INT_ADD", "register:40f0:8", ["const:bf0cb4:8", "const:4:8"]]
+ 00bf0cb4 ["CALL", null, ["callee:00c590c0:8"]]
- 00befcc0 bytes 0ca10194
+ 00bf0cb4 bytes 03a10194
~~~


<a id="compare-92ac3709d4f431f9ab4838bbb95dc9ee"></a>

### [`00bf0478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0478.md) → [`00bf146c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf146c.md) _ZNSt6__ndk112bad_weak_ptrD0Ev

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a860.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c5b830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b830.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf048c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0478.md#insn-00bf048c)
- 新版 [`00bf1480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf146c.md#insn-00bf1480)

~~~diff
- 00bf048c ["INT_ADD", "register:40f0:8", ["const:bf048c:8", "const:4:8"]]
- 00bf048c ["CALL", null, ["callee:00c5b830:8"]]
+ 00bf1480 ["INT_ADD", "register:40f0:8", ["const:bf1480:8", "const:4:8"]]
+ 00bf1480 ["CALL", null, ["callee:00c5b830:8"]]
- 00bf048c bytes f5a80194
+ 00bf1480 bytes eca80194
~~~


<a id="compare-438e037619e7b9f580a88e8f762fb773"></a>

### [`00bf04cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf04cc.md) → [`00bf14c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf14c0.md) _ZNSt6__ndk114__shared_count12__add_sharedEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf04e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf04cc.md#insn-00bf04e0)
- 新版 [`00bf14d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf14c0.md#insn-00bf14d4)

~~~diff
- 00bf04e0 ["INT_ADD", "register:40f0:8", ["const:bf04e0:8", "const:4:8"]]
- 00bf04e0 ["CALL", null, ["callee:00c54d60:8"]]
+ 00bf14d4 ["INT_ADD", "register:40f0:8", ["const:bf14d4:8", "const:4:8"]]
+ 00bf14d4 ["CALL", null, ["callee:00c54d60:8"]]
- 00bf04e0 bytes 248e0194
+ 00bf14d4 bytes 238e0194
~~~


<a id="compare-ae8569c1f6509f8a0698638ee4eb724d"></a>

### [`00bf04f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf04f0.md) → [`00bf14e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf14e4.md) _ZNSt6__ndk114__shared_count16__release_sharedEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf050c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf04f0.md#insn-00bf050c) · [`00bf0524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf04f0.md#insn-00bf0524)
- 新版 [`00bf1500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf14e4.md#insn-00bf1500) · [`00bf1518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf14e4.md#insn-00bf1518)

~~~diff
- 00bf050c ["INT_ADD", "register:40f0:8", ["const:bf050c:8", "const:4:8"]]
- 00bf050c ["CALL", null, ["callee:00c54d90:8"]]
+ 00bf1500 ["INT_ADD", "register:40f0:8", ["const:bf1500:8", "const:4:8"]]
+ 00bf1500 ["CALL", null, ["callee:00c54d90:8"]]
- 00bf050c bytes 258e0194
+ 00bf1500 bytes 248e0194
- 00bf0524 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bf0524 ["INT_ADD", "register:40f0:8", ["const:bf0524:8", "const:4:8"]]
- 00bf0524 ["CALLIND", null, ["register:0:8"]]
+ 00bf1518 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bf1518 ["INT_ADD", "register:40f0:8", ["const:bf1518:8", "const:4:8"]]
+ 00bf1518 ["CALLIND", null, ["register:0:8"]]
- 00bf0524 bytes 00013fd6
+ 00bf1518 bytes 00013fd6
~~~


<a id="compare-ec501963de9fe4fdebefecc111fdc5d2"></a>

### [`00bf0540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0540.md) → [`00bf1534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1534.md) _ZNSt6__ndk119__shared_weak_count12__add_sharedEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0540.md#insn-00bf0554)
- 新版 [`00bf1548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1534.md#insn-00bf1548)

~~~diff
- 00bf0554 ["INT_ADD", "register:40f0:8", ["const:bf0554:8", "const:4:8"]]
- 00bf0554 ["CALL", null, ["callee:00c54d60:8"]]
+ 00bf1548 ["INT_ADD", "register:40f0:8", ["const:bf1548:8", "const:4:8"]]
+ 00bf1548 ["CALL", null, ["callee:00c54d60:8"]]
- 00bf0554 bytes 078e0194
+ 00bf1548 bytes 068e0194
~~~


<a id="compare-1ee199511e3676f94ada67df9be1d759"></a>

### [`00bf0564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0564.md) → [`00bf1558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1558.md) _ZNSt6__ndk119__shared_weak_count10__add_weakEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0564.md#insn-00bf0578)
- 新版 [`00bf156c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1558.md#insn-00bf156c)

~~~diff
- 00bf0578 ["INT_ADD", "register:40f0:8", ["const:bf0578:8", "const:4:8"]]
- 00bf0578 ["CALL", null, ["callee:00c54d60:8"]]
+ 00bf156c ["INT_ADD", "register:40f0:8", ["const:bf156c:8", "const:4:8"]]
+ 00bf156c ["CALL", null, ["callee:00c54d60:8"]]
- 00bf0578 bytes fe8d0194
+ 00bf156c bytes fd8d0194
~~~


<a id="compare-061bf50951cef9affeb28700fbfb4273"></a>

### [`00bf0588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0588.md) → [`00bf157c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf157c.md) _ZNSt6__ndk119__shared_weak_count16__release_sharedEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf05a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0588.md#insn-00bf05a4) · [`00bf05cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0588.md#insn-00bf05cc) · [`00bf05e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0588.md#insn-00bf05e0)
- 新版 [`00bf1598`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf157c.md#insn-00bf1598) · [`00bf15c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf157c.md#insn-00bf15c0) · [`00bf15d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf157c.md#insn-00bf15d4)

~~~diff
- 00bf05a4 ["INT_ADD", "register:40f0:8", ["const:bf05a4:8", "const:4:8"]]
- 00bf05a4 ["CALL", null, ["callee:00c54d90:8"]]
+ 00bf1598 ["INT_ADD", "register:40f0:8", ["const:bf1598:8", "const:4:8"]]
+ 00bf1598 ["CALL", null, ["callee:00c54d90:8"]]
- 00bf05a4 bytes ff8d0194
+ 00bf1598 bytes fe8d0194
- 00bf05cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bf05cc ["INT_ADD", "register:40f0:8", ["const:bf05cc:8", "const:4:8"]]
- 00bf05cc ["CALLIND", null, ["register:0:8"]]
+ 00bf15c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bf15c0 ["INT_ADD", "register:40f0:8", ["const:bf15c0:8", "const:4:8"]]
+ 00bf15c0 ["CALLIND", null, ["register:0:8"]]
- 00bf05cc bytes 00013fd6
+ 00bf15c0 bytes 00013fd6
- 00bf05e0 ["INT_ADD", "register:40f0:8", ["const:bf05e0:8", "const:4:8"]]
- 00bf05e0 ["CALL", null, ["callee:00c54d90:8"]]
+ 00bf15d4 ["INT_ADD", "register:40f0:8", ["const:bf15d4:8", "const:4:8"]]
+ 00bf15d4 ["CALL", null, ["callee:00c54d90:8"]]
- 00bf05e0 bytes f08d0194
+ 00bf15d4 bytes ef8d0194
~~~


<a id="compare-7098ffcd8f8f720a0150c40795d3ff26"></a>

### [`00bf0604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0604.md) → [`00bf15f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf15f8.md) _ZNSt6__ndk119__shared_weak_count14__release_weakEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) · 呼出先 1件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0604.md#insn-00bf0628)
- 新版 [`00bf161c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf15f8.md#insn-00bf161c)

~~~diff
- 00bf0628 ["INT_ADD", "register:40f0:8", ["const:bf0628:8", "const:4:8"]]
- 00bf0628 ["CALL", null, ["callee:00c54d90:8"]]
+ 00bf161c ["INT_ADD", "register:40f0:8", ["const:bf161c:8", "const:4:8"]]
+ 00bf161c ["CALL", null, ["callee:00c54d90:8"]]
- 00bf0628 bytes de8d0194
+ 00bf161c bytes dd8d0194
~~~


<a id="compare-a5065050cb3ac33fd44e74afe5847874"></a>

### [`00bf065c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf065c.md) → [`00bf1650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1650.md) _ZNSt6__ndk119__shared_weak_count4lockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c585c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585c0.md) · 呼出先 1件 [`00c53ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ca0.md)
- 新版 呼出元 1件 [`00c59590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59590.md) · 呼出先 1件 [`00c54c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54c90.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf068c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf065c.md#insn-00bf068c)
- 新版 [`00bf1680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1650.md#insn-00bf1680)

~~~diff
- 00bf068c ["INT_ADD", "register:40f0:8", ["const:bf068c:8", "const:4:8"]]
- 00bf068c ["CALL", null, ["callee:00c54c90:8"]]
+ 00bf1680 ["INT_ADD", "register:40f0:8", ["const:bf1680:8", "const:4:8"]]
+ 00bf1680 ["CALL", null, ["callee:00c54c90:8"]]
- 00bf068c bytes 858d0194
+ 00bf1680 bytes 848d0194
~~~


<a id="compare-963ec5dddd13162970b67bbe804190ae"></a>

### [`00bf06c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf06c8.md) → [`00bf16bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf16bc.md) _ZNSt6__ndk18__sp_mut4lockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c740.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf06d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf06c8.md#insn-00bf06d8)
- 新版 [`00bf16cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf16bc.md#insn-00bf16cc)

~~~diff
- 00bf06d8 ["INT_ADD", "register:40f0:8", ["const:bf06d8:8", "const:4:8"]]
- 00bf06d8 ["CALL", null, ["callee:00c5c740:8"]]
+ 00bf16cc ["INT_ADD", "register:40f0:8", ["const:bf16cc:8", "const:4:8"]]
+ 00bf16cc ["CALL", null, ["callee:00c5c740:8"]]
- 00bf06d8 bytes 26ac0194
+ 00bf16cc bytes 1dac0194
~~~


<a id="compare-40d60c7728f02728915aa39a0e6fc127"></a>

### [`00bf06ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf06ec.md) → [`00bf16e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf16e0.md) _ZNSt6__ndk18__sp_mut6unlockEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c750.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf06fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf06ec.md#insn-00bf06fc)
- 新版 [`00bf16f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf16e0.md#insn-00bf16f0)

~~~diff
- 00bf06fc ["INT_ADD", "register:40f0:8", ["const:bf06fc:8", "const:4:8"]]
- 00bf06fc ["CALL", null, ["callee:00c5c750:8"]]
+ 00bf16f0 ["INT_ADD", "register:40f0:8", ["const:bf16f0:8", "const:4:8"]]
+ 00bf16f0 ["CALL", null, ["callee:00c5c750:8"]]
- 00bf06fc bytes 21ac0194
+ 00bf16f0 bytes 18ac0194
~~~


<a id="compare-f19bc52e5d6f74268964174c1880c27d"></a>

### [`00bf0710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0710.md) → [`00bf1704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1704.md) _ZNSt6__ndk112__get_sp_mutEPKv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf1750",
      "incomplete_value": true,
      "site": "00bf1754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca5788:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_AND",
              [
                "leaf",
                "const:3:4"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bf075c",
      "incomplete_value": true,
      "site": "00bf0760",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca47b8:8"
          ],
          [
            "INT_LEFT",
            "8",
            [
              "INT_AND",
              [
                "leaf",
                "const:3:4"
              ]
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


#### 変更候補の命令位置

- 旧版 [`00bf0750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0710.md#insn-00bf0750)
- 新版 [`00bf1744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1704.md#insn-00bf1744)

~~~diff
- 00bf0750 ["COPY", "register:4048:8", ["const:ca47b8:8"]]
+ 00bf1744 ["COPY", "register:4048:8", ["const:ca5788:8"]]
- 00bf0750 bytes 49035a10
+ 00bf1744 bytes 29025a10
~~~


<a id="compare-8648b885c53fb4841470ce4bfb81d113"></a>

### [`00bf0940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0940.md) → [`00bf1934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1934.md) _ZNSt11logic_erroraSERKS_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0940.md#insn-00bf0968) · [`00bf0974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0940.md#insn-00bf0974) · [`00bf0984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0940.md#insn-00bf0984)
- 新版 [`00bf195c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1934.md#insn-00bf195c) · [`00bf1968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1934.md#insn-00bf1968) · [`00bf1978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1934.md#insn-00bf1978)

~~~diff
- 00bf0968 ["INT_ADD", "register:40f0:8", ["const:bf0968:8", "const:4:8"]]
- 00bf0968 ["CALL", null, ["callee:00c54d30:8"]]
+ 00bf195c ["INT_ADD", "register:40f0:8", ["const:bf195c:8", "const:4:8"]]
+ 00bf195c ["CALL", null, ["callee:00c54d30:8"]]
- 00bf0968 bytes f68c0194
+ 00bf195c bytes f58c0194
- 00bf0974 ["INT_ADD", "register:40f0:8", ["const:bf0974:8", "const:4:8"]]
- 00bf0974 ["CALL", null, ["callee:00c54d30:8"]]
+ 00bf1968 ["INT_ADD", "register:40f0:8", ["const:bf1968:8", "const:4:8"]]
+ 00bf1968 ["CALL", null, ["callee:00c54d30:8"]]
- 00bf0974 bytes f38c0194
+ 00bf1968 bytes f28c0194
- 00bf0984 ["INT_ADD", "register:40f0:8", ["const:bf0984:8", "const:4:8"]]
- 00bf0984 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bf1978 ["INT_ADD", "register:40f0:8", ["const:bf1978:8", "const:4:8"]]
+ 00bf1978 ["CALL", null, ["callee:00c58f50:8"]]
- 00bf0984 bytes 7f9d0194
+ 00bf1978 bytes 769d0194
~~~


<a id="compare-49a0ba938519176f095a4ee194ebda37"></a>

### [`00bf0af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0af0.md) → [`00bf1ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1ae4.md) _ZNSt13runtime_erroraSERKS_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0af0.md#insn-00bf0b18) · [`00bf0b24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0af0.md#insn-00bf0b24) · [`00bf0b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0af0.md#insn-00bf0b34)
- 新版 [`00bf1b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1ae4.md#insn-00bf1b0c) · [`00bf1b18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1ae4.md#insn-00bf1b18) · [`00bf1b28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1ae4.md#insn-00bf1b28)

~~~diff
- 00bf0b18 ["INT_ADD", "register:40f0:8", ["const:bf0b18:8", "const:4:8"]]
- 00bf0b18 ["CALL", null, ["callee:00c54d30:8"]]
+ 00bf1b0c ["INT_ADD", "register:40f0:8", ["const:bf1b0c:8", "const:4:8"]]
+ 00bf1b0c ["CALL", null, ["callee:00c54d30:8"]]
- 00bf0b18 bytes 8a8c0194
+ 00bf1b0c bytes 898c0194
- 00bf0b24 ["INT_ADD", "register:40f0:8", ["const:bf0b24:8", "const:4:8"]]
- 00bf0b24 ["CALL", null, ["callee:00c54d30:8"]]
+ 00bf1b18 ["INT_ADD", "register:40f0:8", ["const:bf1b18:8", "const:4:8"]]
+ 00bf1b18 ["CALL", null, ["callee:00c54d30:8"]]
- 00bf0b24 bytes 878c0194
+ 00bf1b18 bytes 868c0194
- 00bf0b34 ["INT_ADD", "register:40f0:8", ["const:bf0b34:8", "const:4:8"]]
- 00bf0b34 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bf1b28 ["INT_ADD", "register:40f0:8", ["const:bf1b28:8", "const:4:8"]]
+ 00bf1b28 ["CALL", null, ["callee:00c58f50:8"]]
- 00bf0b34 bytes 139d0194
+ 00bf1b28 bytes 0a9d0194
~~~


<a id="compare-9fc69e90964c03ba29e865d6dafdcc13"></a>

### [`00bf0ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0ba0.md) → [`00bf1b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1b94.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58140.md) · 呼出先 3件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md)
- 新版 呼出元 1件 [`00c59110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59110.md) · 呼出先 3件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5c140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0ba0.md#insn-00bf0c40) · [`00bf0c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0ba0.md#insn-00bf0c8c) · [`00bf0c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0ba0.md#insn-00bf0c9c)
- 新版 [`00bf1c34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1b94.md#insn-00bf1c34) · [`00bf1c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1b94.md#insn-00bf1c80) · [`00bf1c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1b94.md#insn-00bf1c90)

~~~diff
- 00bf0c40 ["INT_ADD", "register:40f0:8", ["const:bf0c40:8", "const:4:8"]]
- 00bf0c40 ["CALL", null, ["callee:00c5c140:8"]]
+ 00bf1c34 ["INT_ADD", "register:40f0:8", ["const:bf1c34:8", "const:4:8"]]
+ 00bf1c34 ["CALL", null, ["callee:00c5c140:8"]]
- 00bf0c40 bytes 4ca90194
+ 00bf1c34 bytes 43a90194
- 00bf0c8c ["INT_ADD", "register:40f0:8", ["const:bf0c8c:8", "const:4:8"]]
- 00bf0c8c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf1c80 ["INT_ADD", "register:40f0:8", ["const:bf1c80:8", "const:4:8"]]
+ 00bf1c80 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf0c8c bytes e19c0194
+ 00bf1c80 bytes d89c0194
- 00bf0c9c ["INT_ADD", "register:40f0:8", ["const:bf0c9c:8", "const:4:8"]]
- 00bf0c9c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf1c90 ["INT_ADD", "register:40f0:8", ["const:bf1c90:8", "const:4:8"]]
+ 00bf1c90 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf0c9c bytes dd9c0194
+ 00bf1c90 bytes d49c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-446d3a4d07459897fc2d2c4e6f1b9d3a"></a>

### [`00bf0e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0e2c.md) → [`00bf1e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1e20.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0e2c.md#insn-00bf0e88) · [`00bf0eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0e2c.md#insn-00bf0eac) · [`00bf0ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0e2c.md#insn-00bf0ecc)
- 新版 [`00bf1e7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1e20.md#insn-00bf1e7c) · [`00bf1ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1e20.md#insn-00bf1ea0) · [`00bf1ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1e20.md#insn-00bf1ec0)

~~~diff
- 00bf0e88 ["INT_ADD", "register:40f0:8", ["const:bf0e88:8", "const:4:8"]]
- 00bf0e88 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf1e7c ["INT_ADD", "register:40f0:8", ["const:bf1e7c:8", "const:4:8"]]
+ 00bf1e7c ["CALL", null, ["callee:00c58f30:8"]]
- 00bf0e88 bytes 369c0194
+ 00bf1e7c bytes 2d9c0194
- 00bf0eac ["INT_ADD", "register:40f0:8", ["const:bf0eac:8", "const:4:8"]]
- 00bf0eac ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf1ea0 ["INT_ADD", "register:40f0:8", ["const:bf1ea0:8", "const:4:8"]]
+ 00bf1ea0 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf0eac bytes 599c0194
+ 00bf1ea0 bytes 509c0194
- 00bf0ecc ["INT_ADD", "register:40f0:8", ["const:bf0ecc:8", "const:4:8"]]
- 00bf0ecc ["CALL", null, ["callee:0043bac4:8"]]
+ 00bf1ec0 ["INT_ADD", "register:40f0:8", ["const:bf1ec0:8", "const:4:8"]]
+ 00bf1ec0 ["CALL", null, ["callee:0043bac4:8"]]
- 00bf0ecc bytes 362ae197
+ 00bf1ec0 bytes 0127e197
~~~


<a id="compare-b7c607aeae73245a385bef0048bb970e"></a>

### [`00bf0efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0efc.md) → [`00bf1ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1ef0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58150.md) · 呼出先 2件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58140.md)
- 新版 呼出元 1件 [`00c59120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59120.md) · 呼出先 2件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c59110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0efc.md#insn-00bf0f24)
- 新版 [`00bf1f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1ef0.md#insn-00bf1f18)

~~~diff
- 00bf0f24 ["INT_ADD", "register:40f0:8", ["const:bf0f24:8", "const:4:8"]]
- 00bf0f24 ["CALL", null, ["callee:00c59080:8"]]
+ 00bf1f18 ["INT_ADD", "register:40f0:8", ["const:bf1f18:8", "const:4:8"]]
+ 00bf1f18 ["CALL", null, ["callee:00c59080:8"]]
- 00bf0f24 bytes 639c0194
+ 00bf1f18 bytes 5a9c0194
~~~


<a id="compare-4fa8abe2ee1f35d40e228f80df8a6571"></a>

### [`00bf0f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0f7c.md) → [`00bf1f70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1f70.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16find_last_not_ofEPKcmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0fd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0f7c.md#insn-00bf0fd8)
- 新版 [`00bf1fcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf1/00bf1f70.md#insn-00bf1fcc)

~~~diff
- 00bf0fd8 ["INT_ADD", "register:40f0:8", ["const:bf0fd8:8", "const:4:8"]]
- 00bf0fd8 ["CALL", null, ["callee:00c59070:8"]]
+ 00bf1fcc ["INT_ADD", "register:40f0:8", ["const:bf1fcc:8", "const:4:8"]]
+ 00bf1fcc ["CALL", null, ["callee:00c59070:8"]]
- 00bf0fd8 bytes 329c0194
+ 00bf1fcc bytes 299c0194
~~~


<a id="compare-50ea269ea701eb1271eaf9982773423a"></a>

### [`00bf1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1014.md) → [`00bf2008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2008.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17find_first_not_ofEPKcmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1014.md#insn-00bf1068)
- 新版 [`00bf205c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2008.md#insn-00bf205c)

~~~diff
- 00bf1068 ["INT_ADD", "register:40f0:8", ["const:bf1068:8", "const:4:8"]]
- 00bf1068 ["CALL", null, ["callee:00c59070:8"]]
+ 00bf205c ["INT_ADD", "register:40f0:8", ["const:bf205c:8", "const:4:8"]]
+ 00bf205c ["CALL", null, ["callee:00c59070:8"]]
- 00bf1068 bytes 0e9c0194
+ 00bf205c bytes 059c0194
~~~


<a id="compare-34afef08a127788e5787f11bd8ef6e94"></a>

### [`00bf10a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf10a0.md) → [`00bf2094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2094.md) FUN_00bf2094

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf1368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1368.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00bf235c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf235c.md) · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf114c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf10a0.md#insn-00bf114c) · [`00bf1164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf10a0.md#insn-00bf1164) · [`00bf1184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf10a0.md#insn-00bf1184)
- 新版 [`00bf2140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2094.md#insn-00bf2140) · [`00bf2158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2094.md#insn-00bf2158) · [`00bf2178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2094.md#insn-00bf2178)

~~~diff
- 00bf114c ["INT_ADD", "register:40f0:8", ["const:bf114c:8", "const:4:8"]]
- 00bf114c ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf2140 ["INT_ADD", "register:40f0:8", ["const:bf2140:8", "const:4:8"]]
+ 00bf2140 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf114c bytes 859b0194
+ 00bf2140 bytes 7c9b0194
- 00bf1164 ["INT_ADD", "register:40f0:8", ["const:bf1164:8", "const:4:8"]]
- 00bf1164 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf2158 ["INT_ADD", "register:40f0:8", ["const:bf2158:8", "const:4:8"]]
+ 00bf2158 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf1164 bytes ab9b0194
+ 00bf2158 bytes a29b0194
- 00bf1184 ["INT_ADD", "register:40f0:8", ["const:bf1184:8", "const:4:8"]]
- 00bf1184 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf2178 ["INT_ADD", "register:40f0:8", ["const:bf2178:8", "const:4:8"]]
+ 00bf2178 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf1184 bytes a39b0194
+ 00bf2178 bytes 9a9b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ba30393ce296e0852b671491d416216"></a>

### [`00bf1208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1208.md) → [`00bf21fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf21fc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1208.md#insn-00bf1264) · [`00bf1284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1208.md#insn-00bf1284) · [`00bf12a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1208.md#insn-00bf12a4)
- 新版 [`00bf2258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf21fc.md#insn-00bf2258) · [`00bf2278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf21fc.md#insn-00bf2278) · [`00bf2298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf21fc.md#insn-00bf2298)

~~~diff
- 00bf1264 ["INT_ADD", "register:40f0:8", ["const:bf1264:8", "const:4:8"]]
- 00bf1264 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf2258 ["INT_ADD", "register:40f0:8", ["const:bf2258:8", "const:4:8"]]
+ 00bf2258 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf1264 bytes 3f9b0194
+ 00bf2258 bytes 369b0194
- 00bf1284 ["INT_ADD", "register:40f0:8", ["const:bf1284:8", "const:4:8"]]
- 00bf1284 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf2278 ["INT_ADD", "register:40f0:8", ["const:bf2278:8", "const:4:8"]]
+ 00bf2278 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf1284 bytes 639b0194
+ 00bf2278 bytes 5a9b0194
- 00bf12a4 ["INT_ADD", "register:40f0:8", ["const:bf12a4:8", "const:4:8"]]
- 00bf12a4 ["CALL", null, ["callee:0043bac4:8"]]
+ 00bf2298 ["INT_ADD", "register:40f0:8", ["const:bf2298:8", "const:4:8"]]
+ 00bf2298 ["CALL", null, ["callee:0043bac4:8"]]
- 00bf12a4 bytes 4029e197
+ 00bf2298 bytes 0b26e197
~~~


<a id="compare-d1fb126f4f3f6be2084f4778cf8508c2"></a>

### [`00bf12a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf12a8.md) → [`00bf229c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf229c.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf12e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf12a8.md#insn-00bf12e8)
- 新版 [`00bf22dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf229c.md#insn-00bf22dc)

~~~diff
- 00bf12e8 ["INT_ADD", "register:40f0:8", ["const:bf12e8:8", "const:4:8"]]
- 00bf12e8 ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf22dc ["INT_ADD", "register:40f0:8", ["const:bf22dc:8", "const:4:8"]]
+ 00bf22dc ["CALL", null, ["callee:00442c7c:8"]]
- 00bf12e8 bytes 9d45e197
+ 00bf22dc bytes 6842e197
~~~


<a id="compare-3df4206014d677e97f6c7ca6195714e6"></a>

### [`00bf1368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1368.md) → [`00bf235c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf235c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmmc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00bf10a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf10a0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00bf2094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2094.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1368.md#insn-00bf1400) · [`00bf1438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1368.md#insn-00bf1438) · [`00bf144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1368.md#insn-00bf144c)
- 新版 [`00bf23f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf235c.md#insn-00bf23f4) · [`00bf242c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf235c.md#insn-00bf242c) · [`00bf2440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf235c.md#insn-00bf2440)

~~~diff
- 00bf1400 ["INT_ADD", "register:40f0:8", ["const:bf1400:8", "const:4:8"]]
- 00bf1400 ["CALL", null, ["callee:00bf2094:8"]]
+ 00bf23f4 ["INT_ADD", "register:40f0:8", ["const:bf23f4:8", "const:4:8"]]
+ 00bf23f4 ["CALL", null, ["callee:00bf2094:8"]]
- 00bf1400 bytes 28ffff97
+ 00bf23f4 bytes 28ffff97
- 00bf1438 ["INT_ADD", "register:40f0:8", ["const:bf1438:8", "const:4:8"]]
- 00bf1438 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf242c ["INT_ADD", "register:40f0:8", ["const:bf242c:8", "const:4:8"]]
+ 00bf242c ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf1438 bytes f69a0194
+ 00bf242c bytes ed9a0194
- 00bf144c ["INT_ADD", "register:40f0:8", ["const:bf144c:8", "const:4:8"]]
- 00bf144c ["CALL", null, ["callee:00c59130:8"]]
+ 00bf2440 ["INT_ADD", "register:40f0:8", ["const:bf2440:8", "const:4:8"]]
+ 00bf2440 ["CALL", null, ["callee:00c59130:8"]]
- 00bf144c bytes 459b0194
+ 00bf2440 bytes 3c9b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6de23b40708b7210893a6272aefdbfe"></a>

### [`00bf149c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf149c.md) → [`00bf2490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2490.md) FUN_00bf2490

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf15e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf15e8.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 2件 [`00bf25dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf25dc.md) [`00bf3028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3028.md) · 呼出先 5件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf154c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf149c.md#insn-00bf154c) · [`00bf158c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf149c.md#insn-00bf158c) · [`00bf159c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf149c.md#insn-00bf159c)
- 新版 [`00bf2540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2490.md#insn-00bf2540) · [`00bf2580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2490.md#insn-00bf2580) · [`00bf2590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2490.md#insn-00bf2590)

~~~diff
- 00bf154c ["INT_ADD", "register:40f0:8", ["const:bf154c:8", "const:4:8"]]
- 00bf154c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf2540 ["INT_ADD", "register:40f0:8", ["const:bf2540:8", "const:4:8"]]
+ 00bf2540 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf154c bytes b19a0194
+ 00bf2540 bytes a89a0194
- 00bf158c ["INT_ADD", "register:40f0:8", ["const:bf158c:8", "const:4:8"]]
- 00bf158c ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf2580 ["INT_ADD", "register:40f0:8", ["const:bf2580:8", "const:4:8"]]
+ 00bf2580 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf158c bytes 759a0194
+ 00bf2580 bytes 6c9a0194
- 00bf159c ["INT_ADD", "register:40f0:8", ["const:bf159c:8", "const:4:8"]]
- 00bf159c ["CALL", null, ["callee:00c590a0:8"]]
+ 00bf2590 ["INT_ADD", "register:40f0:8", ["const:bf2590:8", "const:4:8"]]
+ 00bf2590 ["CALL", null, ["callee:00c590a0:8"]]
- 00bf159c bytes cd9a0194
+ 00bf2590 bytes c49a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8285f011e110a8e00f8e4ffb465d147"></a>

### [`00bf15e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf15e8.md) → [`00bf25dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf25dc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignERKS5_mm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00bf149c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf149c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00bf2490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2490.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf15e8.md#insn-00bf1634)
- 新版 [`00bf2628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf25dc.md#insn-00bf2628)

~~~diff
- 00bf1634 ["INT_ADD", "register:40f0:8", ["const:bf1634:8", "const:4:8"]]
- 00bf1634 ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf2628 ["INT_ADD", "register:40f0:8", ["const:bf2628:8", "const:4:8"]]
+ 00bf2628 ["CALL", null, ["callee:00442c7c:8"]]
- 00bf1634 bytes ca44e197
+ 00bf2628 bytes 9541e197
~~~


<a id="compare-92197c01c4299e0b2f6f374d0f537fb8"></a>

### [`00bf1638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1638.md) → [`00bf262c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf262c.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4copyEPcmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf168c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1638.md#insn-00bf168c) · [`00bf16a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1638.md#insn-00bf16a4)
- 新版 [`00bf2680`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf262c.md#insn-00bf2680) · [`00bf2698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf262c.md#insn-00bf2698)

~~~diff
- 00bf168c ["INT_ADD", "register:40f0:8", ["const:bf168c:8", "const:4:8"]]
- 00bf168c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf2680 ["INT_ADD", "register:40f0:8", ["const:bf2680:8", "const:4:8"]]
+ 00bf2680 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf168c bytes 619a0194
+ 00bf2680 bytes 589a0194
- 00bf16a4 ["INT_ADD", "register:40f0:8", ["const:bf16a4:8", "const:4:8"]]
- 00bf16a4 ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf2698 ["INT_ADD", "register:40f0:8", ["const:bf2698:8", "const:4:8"]]
+ 00bf2698 ["CALL", null, ["callee:00442c7c:8"]]
- 00bf16a4 bytes ae44e197
+ 00bf2698 bytes 7941e197
~~~


<a id="compare-804a980e960d6c223bee7b44405878d5"></a>

### [`00bf16a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf16a8.md) → [`00bf269c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf269c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf16a8.md#insn-00bf1734) · [`00bf1754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf16a8.md#insn-00bf1754) · [`00bf1778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf16a8.md#insn-00bf1778)
- 新版 [`00bf2728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf269c.md#insn-00bf2728) · [`00bf2748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf269c.md#insn-00bf2748) · [`00bf276c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf269c.md#insn-00bf276c)

~~~diff
- 00bf1734 ["INT_ADD", "register:40f0:8", ["const:bf1734:8", "const:4:8"]]
- 00bf1734 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf2728 ["INT_ADD", "register:40f0:8", ["const:bf2728:8", "const:4:8"]]
+ 00bf2728 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf1734 bytes 0b9a0194
+ 00bf2728 bytes 029a0194
- 00bf1754 ["INT_ADD", "register:40f0:8", ["const:bf1754:8", "const:4:8"]]
- 00bf1754 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf2748 ["INT_ADD", "register:40f0:8", ["const:bf2748:8", "const:4:8"]]
+ 00bf2748 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf1754 bytes 2f9a0194
+ 00bf2748 bytes 269a0194
- 00bf1778 ["INT_ADD", "register:40f0:8", ["const:bf1778:8", "const:4:8"]]
- 00bf1778 ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf276c ["INT_ADD", "register:40f0:8", ["const:bf276c:8", "const:4:8"]]
+ 00bf276c ["CALL", null, ["callee:00442c7c:8"]]
- 00bf1778 bytes 7944e197
+ 00bf276c bytes 4441e197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8270486bc959cb7beb85eb0ddab4d1d"></a>

### [`00bf1784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1784.md) → [`00bf2778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2778.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c586a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586a0.md) · 呼出先 1件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)
- 新版 呼出元 1件 [`00c59670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59670.md) · 呼出先 1件 [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf17cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1784.md#insn-00bf17cc)
- 新版 [`00bf27c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2778.md#insn-00bf27c0)

~~~diff
- 00bf17cc ["INT_ADD", "register:40f0:8", ["const:bf17cc:8", "const:4:8"]]
- 00bf17cc ["CALL", null, ["callee:00c59070:8"]]
+ 00bf27c0 ["INT_ADD", "register:40f0:8", ["const:bf27c0:8", "const:4:8"]]
+ 00bf27c0 ["CALL", null, ["callee:00c59070:8"]]
- 00bf17cc bytes 359a0194
+ 00bf27c0 bytes 2c9a0194
~~~


<a id="compare-37c10347aa5a771b48c8d5070bf4a43e"></a>

### [`00bf17f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf17f4.md) → [`00bf27e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf27e8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEmc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf17f4.md#insn-00bf1850) · [`00bf1870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf17f4.md#insn-00bf1870) · [`00bf1890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf17f4.md#insn-00bf1890)
- 新版 [`00bf2844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf27e8.md#insn-00bf2844) · [`00bf2864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf27e8.md#insn-00bf2864) · [`00bf2884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf27e8.md#insn-00bf2884)

~~~diff
- 00bf1850 ["INT_ADD", "register:40f0:8", ["const:bf1850:8", "const:4:8"]]
- 00bf1850 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf2844 ["INT_ADD", "register:40f0:8", ["const:bf2844:8", "const:4:8"]]
+ 00bf2844 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf1850 bytes c4990194
+ 00bf2844 bytes bb990194
- 00bf1870 ["INT_ADD", "register:40f0:8", ["const:bf1870:8", "const:4:8"]]
- 00bf1870 ["CALL", null, ["callee:00c59130:8"]]
+ 00bf2864 ["INT_ADD", "register:40f0:8", ["const:bf2864:8", "const:4:8"]]
+ 00bf2864 ["CALL", null, ["callee:00c59130:8"]]
- 00bf1870 bytes 3c9a0194
+ 00bf2864 bytes 339a0194
- 00bf1890 ["INT_ADD", "register:40f0:8", ["const:bf1890:8", "const:4:8"]]
- 00bf1890 ["CALL", null, ["callee:0043bac4:8"]]
+ 00bf2884 ["INT_ADD", "register:40f0:8", ["const:bf2884:8", "const:4:8"]]
+ 00bf2884 ["CALL", null, ["callee:0043bac4:8"]]
- 00bf1890 bytes c527e197
+ 00bf2884 bytes 9024e197
~~~


<a id="compare-a9843ffb12df9da783571cf56477fa5c"></a>

### [`00bf1894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1894.md) → [`00bf2888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2888.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) · 呼出先 2件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md)
- 新版 呼出元 1件 [`00c59000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59000.md) · 呼出先 2件 [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf18b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1894.md#insn-00bf18b8)
- 新版 [`00bf28ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2888.md#insn-00bf28ac)

~~~diff
- 00bf18b8 ["INT_ADD", "register:40f0:8", ["const:bf18b8:8", "const:4:8"]]
- 00bf18b8 ["CALL", null, ["callee:00c59080:8"]]
+ 00bf28ac ["INT_ADD", "register:40f0:8", ["const:bf28ac:8", "const:4:8"]]
+ 00bf28ac ["CALL", null, ["callee:00c59080:8"]]
- 00bf18b8 bytes fe990194
+ 00bf28ac bytes f5990194
~~~


<a id="compare-5db13771ce52e0b98b06690873d7c900"></a>

### [`00bf18e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf18e0.md) → [`00bf28d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf28d4.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE12find_last_ofEPKcmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf193c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf18e0.md#insn-00bf193c)
- 新版 [`00bf2930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf28d4.md#insn-00bf2930)

~~~diff
- 00bf193c ["INT_ADD", "register:40f0:8", ["const:bf193c:8", "const:4:8"]]
- 00bf193c ["CALL", null, ["callee:00c59070:8"]]
+ 00bf2930 ["INT_ADD", "register:40f0:8", ["const:bf2930:8", "const:4:8"]]
+ 00bf2930 ["CALL", null, ["callee:00c59070:8"]]
- 00bf193c bytes d9990194
+ 00bf2930 bytes d0990194
~~~


<a id="compare-629caff57bcafd2e7515bf84e41a28dc"></a>

### [`00bf1968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1968.md) → [`00bf295c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf295c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c586d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586d0.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c596a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596a0.md) · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1a34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1968.md#insn-00bf1a34) · [`00bf1a44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1968.md#insn-00bf1a44) · [`00bf1a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1968.md#insn-00bf1a54)
- 新版 [`00bf2a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf295c.md#insn-00bf2a28) · [`00bf2a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf295c.md#insn-00bf2a38) · [`00bf2a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf295c.md#insn-00bf2a48)

~~~diff
- 00bf1a34 ["INT_ADD", "register:40f0:8", ["const:bf1a34:8", "const:4:8"]]
- 00bf1a34 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf2a28 ["INT_ADD", "register:40f0:8", ["const:bf2a28:8", "const:4:8"]]
+ 00bf2a28 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf1a34 bytes 4b990194
+ 00bf2a28 bytes 42990194
- 00bf1a44 ["INT_ADD", "register:40f0:8", ["const:bf1a44:8", "const:4:8"]]
- 00bf1a44 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf2a38 ["INT_ADD", "register:40f0:8", ["const:bf2a38:8", "const:4:8"]]
+ 00bf2a38 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf1a44 bytes 73990194
+ 00bf2a38 bytes 6a990194
- 00bf1a54 ["INT_ADD", "register:40f0:8", ["const:bf1a54:8", "const:4:8"]]
- 00bf1a54 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bf2a48 ["INT_ADD", "register:40f0:8", ["const:bf2a48:8", "const:4:8"]]
+ 00bf2a48 ["CALL", null, ["callee:00c58f50:8"]]
- 00bf1a54 bytes 4b990194
+ 00bf2a48 bytes 42990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ec908784888bdf777793ec6479c7ff7"></a>

### [`00bf1aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1aec.md) → [`00bf2ae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2ae0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEmc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a7b0.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`00c5b780`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b780.md) · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c59130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59130.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1aec.md#insn-00bf1bc8) · [`00bf1bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1aec.md#insn-00bf1bd8) · [`00bf1bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1aec.md#insn-00bf1bf4)
- 新版 [`00bf2bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2ae0.md#insn-00bf2bbc) · [`00bf2bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2ae0.md#insn-00bf2bcc) · [`00bf2be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2ae0.md#insn-00bf2be8)

~~~diff
- 00bf1bc8 ["INT_ADD", "register:40f0:8", ["const:bf1bc8:8", "const:4:8"]]
- 00bf1bc8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf2bbc ["INT_ADD", "register:40f0:8", ["const:bf2bbc:8", "const:4:8"]]
+ 00bf2bbc ["CALL", null, ["callee:00c58f30:8"]]
- 00bf1bc8 bytes e6980194
+ 00bf2bbc bytes dd980194
- 00bf1bd8 ["INT_ADD", "register:40f0:8", ["const:bf1bd8:8", "const:4:8"]]
- 00bf1bd8 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bf2bcc ["INT_ADD", "register:40f0:8", ["const:bf2bcc:8", "const:4:8"]]
+ 00bf2bcc ["CALL", null, ["callee:00c58f50:8"]]
- 00bf1bd8 bytes ea980194
+ 00bf2bcc bytes e1980194
- 00bf1bf4 ["INT_ADD", "register:40f0:8", ["const:bf1bf4:8", "const:4:8"]]
- 00bf1bf4 ["CALL", null, ["callee:00c59130:8"]]
+ 00bf2be8 ["INT_ADD", "register:40f0:8", ["const:bf2be8:8", "const:4:8"]]
+ 00bf2be8 ["CALL", null, ["callee:00c59130:8"]]
- 00bf1bf4 bytes 5b990194
+ 00bf2be8 bytes 52990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51802c0fe6dfe25e6bd30fa8838546ee"></a>

### [`00bf1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1c30.md) → [`00bf2c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2c24.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a00.md) · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00bf1ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1ca8.md)
- 新版 呼出元 1件 [`00c5a9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a9d0.md) · 呼出先 2件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00bf2c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2c9c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1c30.md#insn-00bf1c68) · [`00bf1ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1c30.md#insn-00bf1ca4)
- 新版 [`00bf2c5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2c24.md#insn-00bf2c5c) · [`00bf2c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2c24.md#insn-00bf2c98)

~~~diff
- 00bf1c68 ["INT_ADD", "register:40f0:8", ["const:bf1c68:8", "const:4:8"]]
- 00bf1c68 ["CALL", null, ["callee:00bf2c9c:8"]]
+ 00bf2c5c ["INT_ADD", "register:40f0:8", ["const:bf2c5c:8", "const:4:8"]]
+ 00bf2c5c ["CALL", null, ["callee:00bf2c9c:8"]]
- 00bf1c68 bytes 10000094
+ 00bf2c5c bytes 10000094
- 00bf1ca4 ["INT_ADD", "register:40f0:8", ["const:bf1ca4:8", "const:4:8"]]
- 00bf1ca4 ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf2c98 ["INT_ADD", "register:40f0:8", ["const:bf2c98:8", "const:4:8"]]
+ 00bf2c98 ["CALL", null, ["callee:00442c7c:8"]]
- 00bf1ca4 bytes 2e43e197
+ 00bf2c98 bytes f93fe197
~~~


<a id="compare-7a7460b55d94c0026a481f2c26555ea5"></a>

### [`00bf1ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1ca8.md) → [`00bf2c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2c9c.md) FUN_00bf2c9c

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1c30.md) [`00c36154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36154.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 2件 [`00bf2c24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2c24.md) [`00c37148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c37148.md) · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1ca8.md#insn-00bf1d00)
- 新版 [`00bf2cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2c9c.md#insn-00bf2cf4)

~~~diff
- 00bf1d00 ["INT_ADD", "register:40f0:8", ["const:bf1d00:8", "const:4:8"]]
- 00bf1d00 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf2cf4 ["INT_ADD", "register:40f0:8", ["const:bf2cf4:8", "const:4:8"]]
+ 00bf2cf4 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf1d00 bytes c4980194
+ 00bf2cf4 bytes bb980194
~~~


<a id="compare-d6976149438835d5277e99818ee3a0eb"></a>

### [`00bf1d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1d3c.md) → [`00bf2d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2d30.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendERKS5_mm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5c140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1dd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1d3c.md#insn-00bf1dd8) · [`00bf1e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1d3c.md#insn-00bf1e00) · [`00bf1e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1d3c.md#insn-00bf1e40)
- 新版 [`00bf2dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2d30.md#insn-00bf2dcc) · [`00bf2df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2d30.md#insn-00bf2df4) · [`00bf2e34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2d30.md#insn-00bf2e34)

~~~diff
- 00bf1dd8 ["INT_ADD", "register:40f0:8", ["const:bf1dd8:8", "const:4:8"]]
- 00bf1dd8 ["CALL", null, ["callee:00c5c140:8"]]
+ 00bf2dcc ["INT_ADD", "register:40f0:8", ["const:bf2dcc:8", "const:4:8"]]
+ 00bf2dcc ["CALL", null, ["callee:00c5c140:8"]]
- 00bf1dd8 bytes e6a40194
+ 00bf2dcc bytes dda40194
- 00bf1e00 ["INT_ADD", "register:40f0:8", ["const:bf1e00:8", "const:4:8"]]
- 00bf1e00 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf2df4 ["INT_ADD", "register:40f0:8", ["const:bf2df4:8", "const:4:8"]]
+ 00bf2df4 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf1e00 bytes 84980194
+ 00bf2df4 bytes 7b980194
- 00bf1e40 ["INT_ADD", "register:40f0:8", ["const:bf1e40:8", "const:4:8"]]
- 00bf1e40 ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf2e34 ["INT_ADD", "register:40f0:8", ["const:bf2e34:8", "const:4:8"]]
+ 00bf2e34 ["CALL", null, ["callee:00442c7c:8"]]
- 00bf1e40 bytes c742e197
+ 00bf2e34 bytes 923fe197
~~~


<a id="compare-4d7fc577ab79b80d3d5c4d928409026c"></a>

### [`00bf1e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1e44.md) → [`00bf2e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2e38.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1e44.md#insn-00bf1e60) · [`00bf1e9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1e44.md#insn-00bf1e9c) · [`00bf1ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1e44.md#insn-00bf1ebc)
- 新版 [`00bf2e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2e38.md#insn-00bf2e54) · [`00bf2e90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2e38.md#insn-00bf2e90) · [`00bf2eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2e38.md#insn-00bf2eb0)

~~~diff
- 00bf1e60 ["INT_ADD", "register:40f0:8", ["const:bf1e60:8", "const:4:8"]]
- 00bf1e60 ["CALL", null, ["callee:00c59080:8"]]
+ 00bf2e54 ["INT_ADD", "register:40f0:8", ["const:bf2e54:8", "const:4:8"]]
+ 00bf2e54 ["CALL", null, ["callee:00c59080:8"]]
- 00bf1e60 bytes 94980194
+ 00bf2e54 bytes 8b980194
- 00bf1e9c ["INT_ADD", "register:40f0:8", ["const:bf1e9c:8", "const:4:8"]]
- 00bf1e9c ["CALL", null, ["callee:00c590f0:8"]]
+ 00bf2e90 ["INT_ADD", "register:40f0:8", ["const:bf2e90:8", "const:4:8"]]
+ 00bf2e90 ["CALL", null, ["callee:00c590f0:8"]]
- 00bf1e9c bytes a1980194
+ 00bf2e90 bytes 98980194
- 00bf1ebc ["INT_ADD", "register:40f0:8", ["const:bf1ebc:8", "const:4:8"]]
- 00bf1ebc ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf2eb0 ["INT_ADD", "register:40f0:8", ["const:bf2eb0:8", "const:4:8"]]
+ 00bf2eb0 ["CALL", null, ["callee:00442c7c:8"]]
- 00bf1ebc bytes a842e197
+ 00bf2eb0 bytes 733fe197
~~~


<a id="compare-ee0eddcd9311761ea784d57eb05c7f86"></a>

### [`00bf1ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1ec4.md) → [`00bf2eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2eb8.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKcm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1ec4.md#insn-00bf1f24) · [`00bf1f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1ec4.md#insn-00bf1f40)
- 新版 [`00bf2f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2eb8.md#insn-00bf2f18) · [`00bf2f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2eb8.md#insn-00bf2f34)

~~~diff
- 00bf1f24 ["INT_ADD", "register:40f0:8", ["const:bf1f24:8", "const:4:8"]]
- 00bf1f24 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bf2f18 ["INT_ADD", "register:40f0:8", ["const:bf2f18:8", "const:4:8"]]
+ 00bf2f18 ["CALL", null, ["callee:00c590f0:8"]]
- 00bf1f24 bytes 7f980194
+ 00bf2f18 bytes 76980194
- 00bf1f40 ["INT_ADD", "register:40f0:8", ["const:bf1f40:8", "const:4:8"]]
- 00bf1f40 ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf2f34 ["INT_ADD", "register:40f0:8", ["const:bf2f34:8", "const:4:8"]]
+ 00bf2f34 ["CALL", null, ["callee:00442c7c:8"]]
- 00bf1f40 bytes 8742e197
+ 00bf2f34 bytes 523fe197
~~~


<a id="compare-3f220492a95b447e18510e09f6b1064c"></a>

### [`00bf1f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1f44.md) → [`00bf2f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2f38.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1f44.md#insn-00bf1f6c) · [`00bf1fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1f44.md#insn-00bf1fc0) · [`00bf1fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1f44.md#insn-00bf1fe4)
- 新版 [`00bf2f60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2f38.md#insn-00bf2f60) · [`00bf2fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2f38.md#insn-00bf2fb4) · [`00bf2fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2f38.md#insn-00bf2fd8)

~~~diff
- 00bf1f6c ["INT_ADD", "register:40f0:8", ["const:bf1f6c:8", "const:4:8"]]
- 00bf1f6c ["CALL", null, ["callee:00c59080:8"]]
+ 00bf2f60 ["INT_ADD", "register:40f0:8", ["const:bf2f60:8", "const:4:8"]]
+ 00bf2f60 ["CALL", null, ["callee:00c59080:8"]]
- 00bf1f6c bytes 51980194
+ 00bf2f60 bytes 48980194
- 00bf1fc0 ["INT_ADD", "register:40f0:8", ["const:bf1fc0:8", "const:4:8"]]
- 00bf1fc0 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bf2fb4 ["INT_ADD", "register:40f0:8", ["const:bf2fb4:8", "const:4:8"]]
+ 00bf2fb4 ["CALL", null, ["callee:00c590f0:8"]]
- 00bf1fc0 bytes 58980194
+ 00bf2fb4 bytes 4f980194
- 00bf1fe4 ["INT_ADD", "register:40f0:8", ["const:bf1fe4:8", "const:4:8"]]
- 00bf1fe4 ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf2fd8 ["INT_ADD", "register:40f0:8", ["const:bf2fd8:8", "const:4:8"]]
+ 00bf2fd8 ["CALL", null, ["callee:00442c7c:8"]]
- 00bf1fe4 bytes 5e42e197
+ 00bf2fd8 bytes 293fe197
~~~


<a id="compare-c0e3a5bc9d5d5a6bb863ec1c638b116c"></a>

### [`00bf1fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1fe8.md) → [`00bf2fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2fdc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1fe8.md#insn-00bf2028)
- 新版 [`00bf301c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2fdc.md#insn-00bf301c)

~~~diff
- 00bf2028 ["INT_ADD", "register:40f0:8", ["const:bf2028:8", "const:4:8"]]
- 00bf2028 ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf301c ["INT_ADD", "register:40f0:8", ["const:bf301c:8", "const:4:8"]]
+ 00bf301c ["CALL", null, ["callee:00442c7c:8"]]
- 00bf2028 bytes 4d42e197
+ 00bf301c bytes 183fe197
~~~


<a id="compare-bfad01a9ea09cef37307417eb1e591e0"></a>

### [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) → [`00bf3028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3028.md) FUN_00bf3028

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00bf202c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf202c.md) [`00c2c2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c2c4.md) [`00c2c6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c6c0.md) [`00c30b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30b0c.md) [`00c32b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32b20.md) · 呼出先 2件 [`00bf149c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf149c.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)
- 新版 呼出元 8件 [`00bf3020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3020.md) [`00c2d2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d2b8.md) [`00c2d6b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2d/00c2d6b4.md) [`00c31b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c31/00c31b00.md) [`00c33b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c33/00c33b14.md) · 呼出先 2件 [`00bf2490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2490.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md#insn-00bf2050)
- 新版 [`00bf3044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3028.md#insn-00bf3044)

~~~diff
- 00bf2050 ["INT_ADD", "register:40f0:8", ["const:bf2050:8", "const:4:8"]]
- 00bf2050 ["CALL", null, ["callee:00c59080:8"]]
+ 00bf3044 ["INT_ADD", "register:40f0:8", ["const:bf3044:8", "const:4:8"]]
+ 00bf3044 ["CALL", null, ["callee:00c59080:8"]]
- 00bf2050 bytes 18980194
+ 00bf3044 bytes 0f980194
~~~


<a id="compare-29ba4360fa1e400a512dbfd7b600cf0c"></a>

### [`00bf2070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2070.md) → [`00bf3064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3064.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEPKcmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59070.md) [`00c590f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2070.md#insn-00bf2110) · [`00bf2124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2070.md#insn-00bf2124)
- 新版 [`00bf3104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3064.md#insn-00bf3104) · [`00bf3118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3064.md#insn-00bf3118)

~~~diff
- 00bf2110 ["INT_ADD", "register:40f0:8", ["const:bf2110:8", "const:4:8"]]
- 00bf2110 ["CALL", null, ["callee:00c59070:8"]]
+ 00bf3104 ["INT_ADD", "register:40f0:8", ["const:bf3104:8", "const:4:8"]]
+ 00bf3104 ["CALL", null, ["callee:00c59070:8"]]
- 00bf2110 bytes e4970194
+ 00bf3104 bytes db970194
- 00bf2124 ["INT_ADD", "register:40f0:8", ["const:bf2124:8", "const:4:8"]]
- 00bf2124 ["CALL", null, ["callee:00c590f0:8"]]
+ 00bf3118 ["INT_ADD", "register:40f0:8", ["const:bf3118:8", "const:4:8"]]
+ 00bf3118 ["CALL", null, ["callee:00c590f0:8"]]
- 00bf2124 bytes ff970194
+ 00bf3118 bytes f6970194
~~~


<a id="compare-f136fae65089ec3ab190ef3998230ca0"></a>

### [`00bf2244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2244.md) → [`00bf3238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3238.md) FUN_00bf3238

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf21f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf21f0.md) [`00c0521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0521c.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 2件 [`00bf31e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf31e4.md) [`00c06210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06210.md) · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2244.md#insn-00bf2284) · [`00bf22b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2244.md#insn-00bf22b0) · [`00bf22c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2244.md#insn-00bf22c0)
- 新版 [`00bf3278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3238.md#insn-00bf3278) · [`00bf32a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3238.md#insn-00bf32a4) · [`00bf32b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3238.md#insn-00bf32b4)

~~~diff
- 00bf2284 ["INT_ADD", "register:40f0:8", ["const:bf2284:8", "const:4:8"]]
- 00bf2284 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf3278 ["INT_ADD", "register:40f0:8", ["const:bf3278:8", "const:4:8"]]
+ 00bf3278 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf2284 bytes 63970194
+ 00bf3278 bytes 5a970194
- 00bf22b0 ["INT_ADD", "register:40f0:8", ["const:bf22b0:8", "const:4:8"]]
- 00bf22b0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf32a4 ["INT_ADD", "register:40f0:8", ["const:bf32a4:8", "const:4:8"]]
+ 00bf32a4 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf22b0 bytes 2c970194
+ 00bf32a4 bytes 23970194
- 00bf22c0 ["INT_ADD", "register:40f0:8", ["const:bf22c0:8", "const:4:8"]]
- 00bf22c0 ["CALL", null, ["callee:00c590a0:8"]]
+ 00bf32b4 ["INT_ADD", "register:40f0:8", ["const:bf32b4:8", "const:4:8"]]
+ 00bf32b4 ["CALL", null, ["callee:00c590a0:8"]]
- 00bf22c0 bytes 84970194
+ 00bf32b4 bytes 7b970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6590e1ff75d9c0548888f9e0534c88e"></a>

### [`00bf22f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf22f8.md) → [`00bf32ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf32ec.md) FUN_00bf32ec

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf21f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf21f0.md) [`00c0521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0521c.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 2件 [`00bf31e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf31e4.md) [`00c06210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c06/00c06210.md) · 呼出先 5件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf233c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf22f8.md#insn-00bf233c) · [`00bf23c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf22f8.md#insn-00bf23c4) · [`00bf23dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf22f8.md#insn-00bf23dc)
- 新版 [`00bf3330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf32ec.md#insn-00bf3330) · [`00bf33b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf32ec.md#insn-00bf33b8) · [`00bf33d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf32ec.md#insn-00bf33d0)

~~~diff
- 00bf233c ["INT_ADD", "register:40f0:8", ["const:bf233c:8", "const:4:8"]]
- 00bf233c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf3330 ["INT_ADD", "register:40f0:8", ["const:bf3330:8", "const:4:8"]]
+ 00bf3330 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf233c bytes 35970194
+ 00bf3330 bytes 2c970194
- 00bf23c4 ["INT_ADD", "register:40f0:8", ["const:bf23c4:8", "const:4:8"]]
- 00bf23c4 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf33b8 ["INT_ADD", "register:40f0:8", ["const:bf33b8:8", "const:4:8"]]
+ 00bf33b8 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf23c4 bytes e7960194
+ 00bf33b8 bytes de960194
- 00bf23dc ["INT_ADD", "register:40f0:8", ["const:bf23dc:8", "const:4:8"]]
- 00bf23dc ["CALL", null, ["callee:00c590a0:8"]]
+ 00bf33d0 ["INT_ADD", "register:40f0:8", ["const:bf33d0:8", "const:4:8"]]
+ 00bf33d0 ["CALL", null, ["callee:00c590a0:8"]]
- 00bf23dc bytes 3d970194
+ 00bf33d0 bytes 34970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa4a2deadeae5a4999d728d0b19dbe9e"></a>

### [`00bf241c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf241c.md) → [`00bf3410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3410.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) · 呼出先 3件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md)
- 新版 呼出元 1件 [`00c59010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59010.md) · 呼出先 3件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c59080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59080.md) [`00c5c140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf241c.md#insn-00bf2440) · [`00bf249c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf241c.md#insn-00bf249c) · [`00bf24c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf241c.md#insn-00bf24c0)
- 新版 [`00bf3434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3410.md#insn-00bf3434) · [`00bf3490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3410.md#insn-00bf3490) · [`00bf34b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3410.md#insn-00bf34b4)

~~~diff
- 00bf2440 ["INT_ADD", "register:40f0:8", ["const:bf2440:8", "const:4:8"]]
- 00bf2440 ["CALL", null, ["callee:00c59080:8"]]
+ 00bf3434 ["INT_ADD", "register:40f0:8", ["const:bf3434:8", "const:4:8"]]
+ 00bf3434 ["CALL", null, ["callee:00c59080:8"]]
- 00bf2440 bytes 1c970194
+ 00bf3434 bytes 13970194
- 00bf249c ["INT_ADD", "register:40f0:8", ["const:bf249c:8", "const:4:8"]]
- 00bf249c ["CALL", null, ["callee:00c5c140:8"]]
+ 00bf3490 ["INT_ADD", "register:40f0:8", ["const:bf3490:8", "const:4:8"]]
+ 00bf3490 ["CALL", null, ["callee:00c5c140:8"]]
- 00bf249c bytes 35a30194
+ 00bf3490 bytes 2ca30194
- 00bf24c0 ["INT_ADD", "register:40f0:8", ["const:bf24c0:8", "const:4:8"]]
- 00bf24c0 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf34b4 ["INT_ADD", "register:40f0:8", ["const:bf34b4:8", "const:4:8"]]
+ 00bf34b4 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf24c0 bytes d4960194
+ 00bf34b4 bytes cb960194
~~~


<a id="compare-970b4846e2de57cee07565a482b960c2"></a>

### [`00bf2500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2500.md) → [`00bf34f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf34f4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c58140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c59110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf254c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2500.md#insn-00bf254c)
- 新版 [`00bf3540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf34f4.md#insn-00bf3540)

~~~diff
- 00bf254c ["INT_ADD", "register:40f0:8", ["const:bf254c:8", "const:4:8"]]
- 00bf254c ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf3540 ["INT_ADD", "register:40f0:8", ["const:bf3540:8", "const:4:8"]]
+ 00bf3540 ["CALL", null, ["callee:00442c7c:8"]]
- 00bf254c bytes 0441e197
+ 00bf3540 bytes cf3de197
~~~


<a id="compare-49181bfed1b5f7d2796e52c559f8ee89"></a>

### [`00bf2550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2550.md) → [`00bf3544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3544.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertENS_11__wrap_iterIPKcEEc

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2550.md#insn-00bf2614) · [`00bf2640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2550.md#insn-00bf2640) · [`00bf2660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2550.md#insn-00bf2660)
- 新版 [`00bf3608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3544.md#insn-00bf3608) · [`00bf3634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3544.md#insn-00bf3634) · [`00bf3654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3544.md#insn-00bf3654)

~~~diff
- 00bf2614 ["INT_ADD", "register:40f0:8", ["const:bf2614:8", "const:4:8"]]
- 00bf2614 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf3608 ["INT_ADD", "register:40f0:8", ["const:bf3608:8", "const:4:8"]]
+ 00bf3608 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf2614 bytes 7f960194
+ 00bf3608 bytes 76960194
- 00bf2640 ["INT_ADD", "register:40f0:8", ["const:bf2640:8", "const:4:8"]]
- 00bf2640 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf3634 ["INT_ADD", "register:40f0:8", ["const:bf3634:8", "const:4:8"]]
+ 00bf3634 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf2640 bytes 48960194
+ 00bf3634 bytes 3f960194
- 00bf2660 ["INT_ADD", "register:40f0:8", ["const:bf2660:8", "const:4:8"]]
- 00bf2660 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bf3654 ["INT_ADD", "register:40f0:8", ["const:bf3654:8", "const:4:8"]]
+ 00bf3654 ["CALL", null, ["callee:00c58f50:8"]]
- 00bf2660 bytes 48960194
+ 00bf3654 bytes 3f960194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-232bd5c5fe036fd75897dc4eaba810f6"></a>

### [`00bf274c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf274c.md) → [`00bf3740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3740.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmRKS5_mm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c5a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a070.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf274c.md#insn-00bf2798)
- 新版 [`00bf378c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3740.md#insn-00bf378c)

~~~diff
- 00bf2798 ["INT_ADD", "register:40f0:8", ["const:bf2798:8", "const:4:8"]]
- 00bf2798 ["CALL", null, ["callee:00442c7c:8"]]
+ 00bf378c ["INT_ADD", "register:40f0:8", ["const:bf378c:8", "const:4:8"]]
+ 00bf378c ["CALL", null, ["callee:00442c7c:8"]]
- 00bf2798 bytes 7140e197
+ 00bf378c bytes 3c3de197
~~~


<a id="compare-0983dc3334ecb02fc73990cc23e08094"></a>

### [`00bf279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf279c.md) → [`00bf3790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3790.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmPKwm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0b0.md) · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)
- 新版 呼出元 1件 [`00c5f080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f080.md) · 呼出先 3件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5f090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf283c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf279c.md#insn-00bf283c) · [`00bf288c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf279c.md#insn-00bf288c) · [`00bf289c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf279c.md#insn-00bf289c)
- 新版 [`00bf3830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3790.md#insn-00bf3830) · [`00bf3880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3790.md#insn-00bf3880) · [`00bf3890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3790.md#insn-00bf3890)

~~~diff
- 00bf283c ["INT_ADD", "register:40f0:8", ["const:bf283c:8", "const:4:8"]]
- 00bf283c ["CALL", null, ["callee:00c5f090:8"]]
+ 00bf3830 ["INT_ADD", "register:40f0:8", ["const:bf3830:8", "const:4:8"]]
+ 00bf3830 ["CALL", null, ["callee:00c5f090:8"]]
- 00bf283c bytes 21ae0194
+ 00bf3830 bytes 18ae0194
- 00bf288c ["INT_ADD", "register:40f0:8", ["const:bf288c:8", "const:4:8"]]
- 00bf288c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf3880 ["INT_ADD", "register:40f0:8", ["const:bf3880:8", "const:4:8"]]
+ 00bf3880 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf288c bytes e1950194
+ 00bf3880 bytes d8950194
- 00bf289c ["INT_ADD", "register:40f0:8", ["const:bf289c:8", "const:4:8"]]
- 00bf289c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf3890 ["INT_ADD", "register:40f0:8", ["const:bf3890:8", "const:4:8"]]
+ 00bf3890 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf289c bytes dd950194
+ 00bf3890 bytes d4950194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dede6faf794d8953dbb659cdefda44ca"></a>

### [`00bf298c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf298c.md) → [`00bf3980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3980.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE21__grow_by_and_replaceEmmmmmmPKw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c5f090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f090.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf298c.md#insn-00bf2a58) · [`00bf2a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf298c.md#insn-00bf2a74) · [`00bf2a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf298c.md#insn-00bf2a88)
- 新版 [`00bf3a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3980.md#insn-00bf3a4c) · [`00bf3a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3980.md#insn-00bf3a68) · [`00bf3a7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3980.md#insn-00bf3a7c)

~~~diff
- 00bf2a58 ["INT_ADD", "register:40f0:8", ["const:bf2a58:8", "const:4:8"]]
- 00bf2a58 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf3a4c ["INT_ADD", "register:40f0:8", ["const:bf3a4c:8", "const:4:8"]]
+ 00bf3a4c ["CALL", null, ["callee:00c58f30:8"]]
- 00bf2a58 bytes 42950194
+ 00bf3a4c bytes 39950194
- 00bf2a74 ["INT_ADD", "register:40f0:8", ["const:bf2a74:8", "const:4:8"]]
- 00bf2a74 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf3a68 ["INT_ADD", "register:40f0:8", ["const:bf3a68:8", "const:4:8"]]
+ 00bf3a68 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf2a74 bytes 67950194
+ 00bf3a68 bytes 5e950194
- 00bf2a88 ["INT_ADD", "register:40f0:8", ["const:bf2a88:8", "const:4:8"]]
- 00bf2a88 ["CALL", null, ["callee:00c590a0:8"]]
+ 00bf3a7c ["INT_ADD", "register:40f0:8", ["const:bf3a7c:8", "const:4:8"]]
+ 00bf3a7c ["CALL", null, ["callee:00c590a0:8"]]
- 00bf2a88 bytes 92950194
+ 00bf3a7c bytes 89950194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3626314392159419993663516fe29acc"></a>

### [`00bf2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2bd0.md) → [`00bf3bc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3bc4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEPKwmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2bd0.md#insn-00bf2c14) · [`00bf2c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2bd0.md#insn-00bf2c5c) · [`00bf2c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2bd0.md#insn-00bf2c80)
- 新版 [`00bf3c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3bc4.md#insn-00bf3c08) · [`00bf3c50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3bc4.md#insn-00bf3c50) · [`00bf3c74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3bc4.md#insn-00bf3c74)

~~~diff
- 00bf2c14 ["INT_ADD", "register:40f0:8", ["const:bf2c14:8", "const:4:8"]]
- 00bf2c14 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf3c08 ["INT_ADD", "register:40f0:8", ["const:bf3c08:8", "const:4:8"]]
+ 00bf3c08 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf2c14 bytes ff940194
+ 00bf3c08 bytes f6940194
- 00bf2c5c ["INT_ADD", "register:40f0:8", ["const:bf2c5c:8", "const:4:8"]]
- 00bf2c5c ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf3c50 ["INT_ADD", "register:40f0:8", ["const:bf3c50:8", "const:4:8"]]
+ 00bf3c50 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf2c5c bytes c1940194
+ 00bf3c50 bytes b8940194
- 00bf2c80 ["INT_ADD", "register:40f0:8", ["const:bf2c80:8", "const:4:8"]]
- 00bf2c80 ["CALL", null, ["callee:006d7aa8:8"]]
+ 00bf3c74 ["INT_ADD", "register:40f0:8", ["const:bf3c74:8", "const:4:8"]]
+ 00bf3c74 ["CALL", null, ["callee:006d7aa8:8"]]
- 00bf2c80 bytes 9e92eb97
+ 00bf3c74 bytes 8d8feb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c76d1a4c033cf55b744c008b482dd9d"></a>

### [`00bf2cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2cb4.md) → [`00bf3ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3ca8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmPKw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0b0.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5f080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f080.md) [`00c5f0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2cb4.md#insn-00bf2cdc)
- 新版 [`00bf3cd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3ca8.md#insn-00bf3cd0)

~~~diff
- 00bf2cdc ["INT_ADD", "register:40f0:8", ["const:bf2cdc:8", "const:4:8"]]
- 00bf2cdc ["CALL", null, ["callee:00c5f0a0:8"]]
+ 00bf3cd0 ["INT_ADD", "register:40f0:8", ["const:bf3cd0:8", "const:4:8"]]
+ 00bf3cd0 ["CALL", null, ["callee:00c5f0a0:8"]]
- 00bf2cdc bytes fdac0194
+ 00bf3cd0 bytes f4ac0194
~~~


<a id="compare-f2f967fcb0cf606064fc989afa60c34f"></a>

### [`00bf2d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2d34.md) → [`00bf3d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3d28.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE16find_last_not_ofEPKwmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c594f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2d34.md#insn-00bf2d98)
- 新版 [`00bf3d8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3d28.md#insn-00bf3d8c)

~~~diff
- 00bf2d98 ["INT_ADD", "register:40f0:8", ["const:bf2d98:8", "const:4:8"]]
- 00bf2d98 ["CALL", null, ["callee:00c594f0:8"]]
+ 00bf3d8c ["INT_ADD", "register:40f0:8", ["const:bf3d8c:8", "const:4:8"]]
+ 00bf3d8c ["CALL", null, ["callee:00c594f0:8"]]
- 00bf2d98 bytes e2950194
+ 00bf3d8c bytes d9950194
~~~


<a id="compare-b29dbbc3048d2eaf98169fc1179adb5e"></a>

### [`00bf2ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2ddc.md) → [`00bf3dd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3dd0.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c594f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2e3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2ddc.md#insn-00bf2e3c)
- 新版 [`00bf3e30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3dd0.md#insn-00bf3e30)

~~~diff
- 00bf2e3c ["INT_ADD", "register:40f0:8", ["const:bf2e3c:8", "const:4:8"]]
- 00bf2e3c ["CALL", null, ["callee:00c594f0:8"]]
+ 00bf3e30 ["INT_ADD", "register:40f0:8", ["const:bf3e30:8", "const:4:8"]]
+ 00bf3e30 ["CALL", null, ["callee:00c594f0:8"]]
- 00bf2e3c bytes b9950194
+ 00bf3e30 bytes b0950194
~~~


<a id="compare-f32a8c3806eb3dc5f5e46e900318f438"></a>

### [`00bf2e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2e78.md) → [`00bf3e6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3e6c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmmw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0e0.md) · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)
- 新版 呼出元 1件 [`00c5f0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0b0.md) · 呼出先 3件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5b940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2e78.md#insn-00bf2efc) · [`00bf2f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2e78.md#insn-00bf2f3c) · [`00bf2fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2e78.md#insn-00bf2fcc)
- 新版 [`00bf3ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3e6c.md#insn-00bf3ef0) · [`00bf3f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3e6c.md#insn-00bf3f30) · [`00bf3fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3e6c.md#insn-00bf3fc0)

~~~diff
- 00bf2efc ["INT_ADD", "register:40f0:8", ["const:bf2efc:8", "const:4:8"]]
- 00bf2efc ["CALL", null, ["callee:00c5b940:8"]]
+ 00bf3ef0 ["INT_ADD", "register:40f0:8", ["const:bf3ef0:8", "const:4:8"]]
+ 00bf3ef0 ["CALL", null, ["callee:00c5b940:8"]]
- 00bf2efc bytes 9d9e0194
+ 00bf3ef0 bytes 949e0194
- 00bf2f3c ["INT_ADD", "register:40f0:8", ["const:bf2f3c:8", "const:4:8"]]
- 00bf2f3c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf3f30 ["INT_ADD", "register:40f0:8", ["const:bf3f30:8", "const:4:8"]]
+ 00bf3f30 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf2f3c bytes 35940194
+ 00bf3f30 bytes 2c940194
- 00bf2fcc ["INT_ADD", "register:40f0:8", ["const:bf2fcc:8", "const:4:8"]]
- 00bf2fcc ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf3fc0 ["INT_ADD", "register:40f0:8", ["const:bf3fc0:8", "const:4:8"]]
+ 00bf3fc0 ["CALL", null, ["callee:00bf3968:8"]]
- 00bf2fcc bytes 6afeff97
+ 00bf3fc0 bytes 6afeff97
~~~


<a id="compare-b676ac2fee83d803d43b174b6a2d9668"></a>

### [`00bf3004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3004.md) → [`00bf3ff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3ff8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEPKwm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3004.md#insn-00bf3070) · [`00bf3090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3004.md#insn-00bf3090) · [`00bf30b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3004.md#insn-00bf30b0)
- 新版 [`00bf4064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3ff8.md#insn-00bf4064) · [`00bf4084`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3ff8.md#insn-00bf4084) · [`00bf40a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3ff8.md#insn-00bf40a4)

~~~diff
- 00bf3070 ["INT_ADD", "register:40f0:8", ["const:bf3070:8", "const:4:8"]]
- 00bf3070 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf4064 ["INT_ADD", "register:40f0:8", ["const:bf4064:8", "const:4:8"]]
+ 00bf4064 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf3070 bytes bc930194
+ 00bf4064 bytes b3930194
- 00bf3090 ["INT_ADD", "register:40f0:8", ["const:bf3090:8", "const:4:8"]]
- 00bf3090 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf4084 ["INT_ADD", "register:40f0:8", ["const:bf4084:8", "const:4:8"]]
+ 00bf4084 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf3090 bytes e0930194
+ 00bf4084 bytes d7930194
- 00bf30b0 ["INT_ADD", "register:40f0:8", ["const:bf30b0:8", "const:4:8"]]
- 00bf30b0 ["CALL", null, ["callee:006d7aa8:8"]]
+ 00bf40a4 ["INT_ADD", "register:40f0:8", ["const:bf40a4:8", "const:4:8"]]
+ 00bf40a4 ["CALL", null, ["callee:006d7aa8:8"]]
- 00bf30b0 bytes 9291eb97
+ 00bf40a4 bytes 818eeb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63f68b80f19a6595dca5335aef370d31"></a>

### [`00bf30b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf30b8.md) → [`00bf40ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf40ac.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf30fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf30b8.md#insn-00bf30fc)
- 新版 [`00bf40f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf40ac.md#insn-00bf40f0)

~~~diff
- 00bf30fc ["INT_ADD", "register:40f0:8", ["const:bf30fc:8", "const:4:8"]]
- 00bf30fc ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf40f0 ["INT_ADD", "register:40f0:8", ["const:bf40f0:8", "const:4:8"]]
+ 00bf40f0 ["CALL", null, ["callee:00bf3968:8"]]
- 00bf30fc bytes 1efeff97
+ 00bf40f0 bytes 1efeff97
~~~


<a id="compare-a90fcda3c10914bd6435c277071af142"></a>

### [`00bf3100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3100.md) → [`00bf40f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf40f4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKwm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0f0.md) · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)
- 新版 呼出元 1件 [`00c5f0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0c0.md) · 呼出先 3件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5f090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3184`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3100.md#insn-00bf3184) · [`00bf31cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3100.md#insn-00bf31cc) · [`00bf31dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3100.md#insn-00bf31dc)
- 新版 [`00bf4178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf40f4.md#insn-00bf4178) · [`00bf41c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf40f4.md#insn-00bf41c0) · [`00bf41d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf40f4.md#insn-00bf41d0)

~~~diff
- 00bf3184 ["INT_ADD", "register:40f0:8", ["const:bf3184:8", "const:4:8"]]
- 00bf3184 ["CALL", null, ["callee:00c5f090:8"]]
+ 00bf4178 ["INT_ADD", "register:40f0:8", ["const:bf4178:8", "const:4:8"]]
+ 00bf4178 ["CALL", null, ["callee:00c5f090:8"]]
- 00bf3184 bytes cfab0194
+ 00bf4178 bytes c6ab0194
- 00bf31cc ["INT_ADD", "register:40f0:8", ["const:bf31cc:8", "const:4:8"]]
- 00bf31cc ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf41c0 ["INT_ADD", "register:40f0:8", ["const:bf41c0:8", "const:4:8"]]
+ 00bf41c0 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf31cc bytes 91930194
+ 00bf41c0 bytes 88930194
- 00bf31dc ["INT_ADD", "register:40f0:8", ["const:bf31dc:8", "const:4:8"]]
- 00bf31dc ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf41d0 ["INT_ADD", "register:40f0:8", ["const:bf41d0:8", "const:4:8"]]
+ 00bf41d0 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf31dc bytes 8d930194
+ 00bf41d0 bytes 84930194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c83c85c02f019379fd2ef1fa1cd883f"></a>

### [`00bf32ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf32ac.md) → [`00bf42a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf42a0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmmw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5b940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf32ac.md#insn-00bf3340) · [`00bf3394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf32ac.md#insn-00bf3394) · [`00bf3430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf32ac.md#insn-00bf3430)
- 新版 [`00bf4334`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf42a0.md#insn-00bf4334) · [`00bf4388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf42a0.md#insn-00bf4388) · [`00bf4424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf42a0.md#insn-00bf4424)

~~~diff
- 00bf3340 ["INT_ADD", "register:40f0:8", ["const:bf3340:8", "const:4:8"]]
- 00bf3340 ["CALL", null, ["callee:00c5b940:8"]]
+ 00bf4334 ["INT_ADD", "register:40f0:8", ["const:bf4334:8", "const:4:8"]]
+ 00bf4334 ["CALL", null, ["callee:00c5b940:8"]]
- 00bf3340 bytes 8c9d0194
+ 00bf4334 bytes 839d0194
- 00bf3394 ["INT_ADD", "register:40f0:8", ["const:bf3394:8", "const:4:8"]]
- 00bf3394 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf4388 ["INT_ADD", "register:40f0:8", ["const:bf4388:8", "const:4:8"]]
+ 00bf4388 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf3394 bytes 1f930194
+ 00bf4388 bytes 16930194
- 00bf3430 ["INT_ADD", "register:40f0:8", ["const:bf3430:8", "const:4:8"]]
- 00bf3430 ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf4424 ["INT_ADD", "register:40f0:8", ["const:bf4424:8", "const:4:8"]]
+ 00bf4424 ["CALL", null, ["callee:00bf3968:8"]]
- 00bf3430 bytes 51fdff97
+ 00bf4424 bytes 51fdff97
~~~


<a id="compare-742544e7325762beacdf5eccd3e636df"></a>

### [`00bf343c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf343c.md) → [`00bf4430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4430.md) FUN_00bf4430

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00bf3434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3434.md) [`00bf37bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf37bc.md) [`00bf4490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4490.md) [`00c2d030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d030.md) [`00c2dac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dac4.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)
- 新版 呼出元 5件 [`00bf4428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4428.md) [`00bf47b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf47b0.md) [`00bf5484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5484.md) [`00c2e024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2e024.md) [`00c2eab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c2e/00c2eab8.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5f090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf34a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf343c.md#insn-00bf34a4) · [`00bf34cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf343c.md#insn-00bf34cc)
- 新版 [`00bf4498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4430.md#insn-00bf4498) · [`00bf44c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4430.md#insn-00bf44c0)

~~~diff
- 00bf34a4 ["INT_ADD", "register:40f0:8", ["const:bf34a4:8", "const:4:8"]]
- 00bf34a4 ["CALL", null, ["callee:00c5f090:8"]]
+ 00bf4498 ["INT_ADD", "register:40f0:8", ["const:bf4498:8", "const:4:8"]]
+ 00bf4498 ["CALL", null, ["callee:00c5f090:8"]]
- 00bf34a4 bytes 07ab0194
+ 00bf4498 bytes feaa0194
- 00bf34cc ["INT_ADD", "register:40f0:8", ["const:bf34cc:8", "const:4:8"]]
- 00bf34cc ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf44c0 ["INT_ADD", "register:40f0:8", ["const:bf44c0:8", "const:4:8"]]
+ 00bf44c0 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf34cc bytes d1920194
+ 00bf44c0 bytes c8920194
~~~


<a id="compare-2a5498554abbd0354d8189a75da049ef"></a>

### [`00bf3504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3504.md) → [`00bf44f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf44f8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7reserveEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00bf35a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf35a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00bf4594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4594.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf359c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3504.md#insn-00bf359c)
- 新版 [`00bf4590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf44f8.md#insn-00bf4590)

~~~diff
- 00bf359c ["INT_ADD", "register:40f0:8", ["const:bf359c:8", "const:4:8"]]
- 00bf359c ["CALL", null, ["callee:006d7aa8:8"]]
+ 00bf4590 ["INT_ADD", "register:40f0:8", ["const:bf4590:8", "const:4:8"]]
+ 00bf4590 ["CALL", null, ["callee:006d7aa8:8"]]
- 00bf359c bytes 5790eb97
+ 00bf4590 bytes 468deb97
~~~


<a id="compare-1c668797390911a464a27a68493eabf0"></a>

### [`00bf35a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf35a0.md) → [`00bf4594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4594.md) FUN_00bf4594

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf3504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3504.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00bf44f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf44f8.md) · 呼出先 4件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf35a0.md#insn-00bf3610) · [`00bf363c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf35a0.md#insn-00bf363c) · [`00bf3660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf35a0.md#insn-00bf3660)
- 新版 [`00bf4604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4594.md#insn-00bf4604) · [`00bf4630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4594.md#insn-00bf4630) · [`00bf4654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4594.md#insn-00bf4654)

~~~diff
- 00bf3610 ["INT_ADD", "register:40f0:8", ["const:bf3610:8", "const:4:8"]]
- 00bf3610 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf4604 ["INT_ADD", "register:40f0:8", ["const:bf4604:8", "const:4:8"]]
+ 00bf4604 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf3610 bytes 54920194
+ 00bf4604 bytes 4b920194
- 00bf363c ["INT_ADD", "register:40f0:8", ["const:bf363c:8", "const:4:8"]]
- 00bf363c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf4630 ["INT_ADD", "register:40f0:8", ["const:bf4630:8", "const:4:8"]]
+ 00bf4630 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf363c bytes 75920194
+ 00bf4630 bytes 6c920194
- 00bf3660 ["INT_ADD", "register:40f0:8", ["const:bf3660:8", "const:4:8"]]
- 00bf3660 ["CALL", null, ["callee:00c58f50:8"]]
+ 00bf4654 ["INT_ADD", "register:40f0:8", ["const:bf4654:8", "const:4:8"]]
+ 00bf4654 ["CALL", null, ["callee:00c58f50:8"]]
- 00bf3660 bytes 48920194
+ 00bf4654 bytes 3f920194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1976fb6d578216d5f88f7cefb3a5457"></a>

### [`00bf36e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf36e4.md) → [`00bf46d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf46d8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEPKwm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a980.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)
- 新版 呼出元 1件 [`00c5b950`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b950.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5f090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf36e4.md#insn-00bf3758) · [`00bf3780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf36e4.md#insn-00bf3780)
- 新版 [`00bf474c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf46d8.md#insn-00bf474c) · [`00bf4774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf46d8.md#insn-00bf4774)

~~~diff
- 00bf3758 ["INT_ADD", "register:40f0:8", ["const:bf3758:8", "const:4:8"]]
- 00bf3758 ["CALL", null, ["callee:00c5f090:8"]]
+ 00bf474c ["INT_ADD", "register:40f0:8", ["const:bf474c:8", "const:4:8"]]
+ 00bf474c ["CALL", null, ["callee:00c5f090:8"]]
- 00bf3758 bytes 5aaa0194
+ 00bf474c bytes 51aa0194
- 00bf3780 ["INT_ADD", "register:40f0:8", ["const:bf3780:8", "const:4:8"]]
- 00bf3780 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf4774 ["INT_ADD", "register:40f0:8", ["const:bf4774:8", "const:4:8"]]
+ 00bf4774 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf3780 bytes 24920194
+ 00bf4774 bytes 1b920194
~~~


<a id="compare-aa4b9dcb9bd38c8a63fce7eced2dab5b"></a>

### [`00bf37bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf37bc.md) → [`00bf47b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf47b0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6assignERKS5_mm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00bf343c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf343c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00bf4430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4430.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf380c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf37bc.md#insn-00bf380c)
- 新版 [`00bf4800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf47b0.md#insn-00bf4800)

~~~diff
- 00bf380c ["INT_ADD", "register:40f0:8", ["const:bf380c:8", "const:4:8"]]
- 00bf380c ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf4800 ["INT_ADD", "register:40f0:8", ["const:bf4800:8", "const:4:8"]]
+ 00bf4800 ["CALL", null, ["callee:00bf3968:8"]]
- 00bf380c bytes 5afcff97
+ 00bf4800 bytes 5afcff97
~~~


<a id="compare-dcdc968cbc0b47610d2bd3ac478f2437"></a>

### [`00bf3810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3810.md) → [`00bf4804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4804.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4copyEPwmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3810.md#insn-00bf3868) · [`00bf3880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3810.md#insn-00bf3880)
- 新版 [`00bf485c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4804.md#insn-00bf485c) · [`00bf4874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4804.md#insn-00bf4874)

~~~diff
- 00bf3868 ["INT_ADD", "register:40f0:8", ["const:bf3868:8", "const:4:8"]]
- 00bf3868 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf485c ["INT_ADD", "register:40f0:8", ["const:bf485c:8", "const:4:8"]]
+ 00bf485c ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf3868 bytes ea910194
+ 00bf485c bytes e1910194
- 00bf3880 ["INT_ADD", "register:40f0:8", ["const:bf3880:8", "const:4:8"]]
- 00bf3880 ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf4874 ["INT_ADD", "register:40f0:8", ["const:bf4874:8", "const:4:8"]]
+ 00bf4874 ["CALL", null, ["callee:00bf3968:8"]]
- 00bf3880 bytes 3dfcff97
+ 00bf4874 bytes 3dfcff97
~~~


<a id="compare-e496eff8052191a8223a9a290089b177"></a>

### [`00bf3884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3884.md) → [`00bf4878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4878.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9e0.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c5b9b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b9b0.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3884.md#insn-00bf3924) · [`00bf3944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3884.md#insn-00bf3944) · [`00bf3968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3884.md#insn-00bf3968)
- 新版 [`00bf4918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4878.md#insn-00bf4918) · [`00bf4938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4878.md#insn-00bf4938) · [`00bf495c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4878.md#insn-00bf495c)

~~~diff
- 00bf3924 ["INT_ADD", "register:40f0:8", ["const:bf3924:8", "const:4:8"]]
- 00bf3924 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf4918 ["INT_ADD", "register:40f0:8", ["const:bf4918:8", "const:4:8"]]
+ 00bf4918 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf3924 bytes 8f910194
+ 00bf4918 bytes 86910194
- 00bf3944 ["INT_ADD", "register:40f0:8", ["const:bf3944:8", "const:4:8"]]
- 00bf3944 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf4938 ["INT_ADD", "register:40f0:8", ["const:bf4938:8", "const:4:8"]]
+ 00bf4938 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf3944 bytes b3910194
+ 00bf4938 bytes aa910194
- 00bf3968 ["INT_ADD", "register:40f0:8", ["const:bf3968:8", "const:4:8"]]
- 00bf3968 ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf495c ["INT_ADD", "register:40f0:8", ["const:bf495c:8", "const:4:8"]]
+ 00bf495c ["CALL", null, ["callee:00bf3968:8"]]
- 00bf3968 bytes 03fcff97
+ 00bf495c bytes 03fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2b9903f92933cf8599e4873376a8e8a"></a>

### [`00bf3978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3978.md) → [`00bf496c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf496c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4findEwm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c594f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf39c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3978.md#insn-00bf39c0)
- 新版 [`00bf49b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf496c.md#insn-00bf49b4)

~~~diff
- 00bf39c0 ["INT_ADD", "register:40f0:8", ["const:bf39c0:8", "const:4:8"]]
- 00bf39c0 ["CALL", null, ["callee:00c594f0:8"]]
+ 00bf49b4 ["INT_ADD", "register:40f0:8", ["const:bf49b4:8", "const:4:8"]]
+ 00bf49b4 ["CALL", null, ["callee:00c594f0:8"]]
- 00bf39c0 bytes d8920194
+ 00bf49b4 bytes cf920194
~~~


<a id="compare-85b421028e1db5b71de23fa3a4fcb37b"></a>

### [`00bf39ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf39ec.md) → [`00bf49e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf49e0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEmw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf39ec.md#insn-00bf3a58) · [`00bf3ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf39ec.md#insn-00bf3ad4) · [`00bf3ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf39ec.md#insn-00bf3ad8)
- 新版 [`00bf4a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf49e0.md#insn-00bf4a4c) · [`00bf4ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf49e0.md#insn-00bf4ac8) · [`00bf4acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf49e0.md#insn-00bf4acc)

~~~diff
- 00bf3a58 ["INT_ADD", "register:40f0:8", ["const:bf3a58:8", "const:4:8"]]
- 00bf3a58 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf4a4c ["INT_ADD", "register:40f0:8", ["const:bf4a4c:8", "const:4:8"]]
+ 00bf4a4c ["CALL", null, ["callee:00c58f30:8"]]
- 00bf3a58 bytes 42910194
+ 00bf4a4c bytes 39910194
- 00bf3ad4 ["INT_ADD", "register:40f0:8", ["const:bf3ad4:8", "const:4:8"]]
- 00bf3ad4 ["CALL", null, ["callee:006d7aa8:8"]]
+ 00bf4ac8 ["INT_ADD", "register:40f0:8", ["const:bf4ac8:8", "const:4:8"]]
+ 00bf4ac8 ["CALL", null, ["callee:006d7aa8:8"]]
- 00bf3ad4 bytes 098feb97
+ 00bf4ac8 bytes f88beb97
- 00bf3ad8 ["INT_ADD", "register:40f0:8", ["const:bf3ad8:8", "const:4:8"]]
- 00bf3ad8 ["CALL", null, ["callee:00441220:8"]]
+ 00bf4acc ["INT_ADD", "register:40f0:8", ["const:bf4acc:8", "const:4:8"]]
+ 00bf4acc ["CALL", null, ["callee:00441220:8"]]
- 00bf3ad8 bytes 0a35e197
+ 00bf4acc bytes d531e197
~~~


<a id="compare-d65c488b5bb2255de96b95407c251c02"></a>

### [`00bf3adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3adc.md) → [`00bf4ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4ad0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md) [`00c5e0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5f0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0a0.md) [`00c5f0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3b00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3adc.md#insn-00bf3b00)
- 新版 [`00bf4af4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4ad0.md#insn-00bf4af4)

~~~diff
- 00bf3b00 ["INT_ADD", "register:40f0:8", ["const:bf3b00:8", "const:4:8"]]
- 00bf3b00 ["CALL", null, ["callee:00c5f0a0:8"]]
+ 00bf4af4 ["INT_ADD", "register:40f0:8", ["const:bf4af4:8", "const:4:8"]]
+ 00bf4af4 ["CALL", null, ["callee:00c5f0a0:8"]]
- 00bf3b00 bytes 74a90194
+ 00bf4af4 bytes 6ba90194
~~~


<a id="compare-775168c268db9e1622fe3a1dc496ec84"></a>

### [`00bf3b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3b28.md) → [`00bf4b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4b1c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE12find_last_ofEPKwmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c594f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3b28.md#insn-00bf3b90)
- 新版 [`00bf4b84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4b1c.md#insn-00bf4b84)

~~~diff
- 00bf3b90 ["INT_ADD", "register:40f0:8", ["const:bf3b90:8", "const:4:8"]]
- 00bf3b90 ["CALL", null, ["callee:00c594f0:8"]]
+ 00bf4b84 ["INT_ADD", "register:40f0:8", ["const:bf4b84:8", "const:4:8"]]
+ 00bf4b84 ["CALL", null, ["callee:00c594f0:8"]]
- 00bf3b90 bytes 64920194
+ 00bf4b84 bytes 5b920194
~~~


<a id="compare-3d860223bbab05e7a0a8a23c848db02c"></a>

### [`00bf3bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3bc4.md) → [`00bf4bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4bb8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9__grow_byEmmmmmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c5b940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b940.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3c78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3bc4.md#insn-00bf3c78) · [`00bf3c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3bc4.md#insn-00bf3c94) · [`00bf3cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3bc4.md#insn-00bf3cb8)
- 新版 [`00bf4c6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4bb8.md#insn-00bf4c6c) · [`00bf4c88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4bb8.md#insn-00bf4c88) · [`00bf4cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4bb8.md#insn-00bf4cac)

~~~diff
- 00bf3c78 ["INT_ADD", "register:40f0:8", ["const:bf3c78:8", "const:4:8"]]
- 00bf3c78 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf4c6c ["INT_ADD", "register:40f0:8", ["const:bf4c6c:8", "const:4:8"]]
+ 00bf4c6c ["CALL", null, ["callee:00c58f30:8"]]
- 00bf3c78 bytes ba900194
+ 00bf4c6c bytes b1900194
- 00bf3c94 ["INT_ADD", "register:40f0:8", ["const:bf3c94:8", "const:4:8"]]
- 00bf3c94 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf4c88 ["INT_ADD", "register:40f0:8", ["const:bf4c88:8", "const:4:8"]]
+ 00bf4c88 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf3c94 bytes df900194
+ 00bf4c88 bytes d6900194
- 00bf3cb8 ["INT_ADD", "register:40f0:8", ["const:bf3cb8:8", "const:4:8"]]
- 00bf3cb8 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf4cac ["INT_ADD", "register:40f0:8", ["const:bf4cac:8", "const:4:8"]]
+ 00bf4cac ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf3cb8 bytes d6900194
+ 00bf4cac bytes cd900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01bfa88fce8492d72e4217075c6be5ba"></a>

### [`00bf3d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3d04.md) → [`00bf4cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4cf8.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9push_backEw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e100.md) · 呼出先 1件 [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)
- 新版 呼出元 1件 [`00c5f0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0d0.md) · 呼出先 1件 [`00c5b940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3d04.md#insn-00bf3d68)
- 新版 [`00bf4d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4cf8.md#insn-00bf4d5c)

~~~diff
- 00bf3d68 ["INT_ADD", "register:40f0:8", ["const:bf3d68:8", "const:4:8"]]
- 00bf3d68 ["CALL", null, ["callee:00c5b940:8"]]
+ 00bf4d5c ["INT_ADD", "register:40f0:8", ["const:bf4d5c:8", "const:4:8"]]
+ 00bf4d5c ["CALL", null, ["callee:00c5b940:8"]]
- 00bf3d68 bytes 029b0194
+ 00bf4d5c bytes f99a0194
~~~


<a id="compare-0eb224c774bbc9175ab57c7c06355e18"></a>

### [`00bf3dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3dac.md) → [`00bf4da0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4da0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEmw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3dac.md#insn-00bf3e24)
- 新版 [`00bf4e18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4da0.md#insn-00bf4e18)

~~~diff
- 00bf3e24 ["INT_ADD", "register:40f0:8", ["const:bf3e24:8", "const:4:8"]]
- 00bf3e24 ["CALL", null, ["callee:00c5b940:8"]]
+ 00bf4e18 ["INT_ADD", "register:40f0:8", ["const:bf4e18:8", "const:4:8"]]
+ 00bf4e18 ["CALL", null, ["callee:00c5b940:8"]]
- 00bf3e24 bytes d39a0194
+ 00bf4e18 bytes ca9a0194
~~~


<a id="compare-b2361f5ffc68f9a83dd7403df01a2ea4"></a>

### [`00bf3f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3f2c.md) → [`00bf4f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4f20.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6assignEmw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3f2c.md#insn-00bf3f90)
- 新版 [`00bf4f84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4f20.md#insn-00bf4f84)

~~~diff
- 00bf3f90 ["INT_ADD", "register:40f0:8", ["const:bf3f90:8", "const:4:8"]]
- 00bf3f90 ["CALL", null, ["callee:00c5b940:8"]]
+ 00bf4f84 ["INT_ADD", "register:40f0:8", ["const:bf4f84:8", "const:4:8"]]
+ 00bf4f84 ["CALL", null, ["callee:00c5b940:8"]]
- 00bf3f90 bytes 789a0194
+ 00bf4f84 bytes 6f9a0194
~~~


<a id="compare-e36d43507ff48a8c88626ad4455d0344"></a>

### [`00bf4044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4044.md) → [`00bf5038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5038.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE5eraseEmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00bf40bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf40bc.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00bf50b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf50b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf407c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4044.md#insn-00bf407c) · [`00bf40b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4044.md#insn-00bf40b8)
- 新版 [`00bf5070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5038.md#insn-00bf5070) · [`00bf50ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5038.md#insn-00bf50ac)

~~~diff
- 00bf407c ["INT_ADD", "register:40f0:8", ["const:bf407c:8", "const:4:8"]]
- 00bf407c ["CALL", null, ["callee:00bf50b0:8"]]
+ 00bf5070 ["INT_ADD", "register:40f0:8", ["const:bf5070:8", "const:4:8"]]
+ 00bf5070 ["CALL", null, ["callee:00bf50b0:8"]]
- 00bf407c bytes 10000094
+ 00bf5070 bytes 10000094
- 00bf40b8 ["INT_ADD", "register:40f0:8", ["const:bf40b8:8", "const:4:8"]]
- 00bf40b8 ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf50ac ["INT_ADD", "register:40f0:8", ["const:bf50ac:8", "const:4:8"]]
+ 00bf50ac ["CALL", null, ["callee:00bf3968:8"]]
- 00bf40b8 bytes 2ffaff97
+ 00bf50ac bytes 2ffaff97
~~~


<a id="compare-9685a4d5b1a700333170776874293f22"></a>

### [`00bf40bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf40bc.md) → [`00bf50b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf50b0.md) FUN_00bf50b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf4044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4044.md) [`00c361ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c361ac.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 2件 [`00bf5038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5038.md) [`00c371a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c37/00c371a0.md) · 呼出先 1件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf411c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf40bc.md#insn-00bf411c)
- 新版 [`00bf5110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf50b0.md#insn-00bf5110)

~~~diff
- 00bf411c ["INT_ADD", "register:40f0:8", ["const:bf411c:8", "const:4:8"]]
- 00bf411c ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf5110 ["INT_ADD", "register:40f0:8", ["const:bf5110:8", "const:4:8"]]
+ 00bf5110 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf411c bytes bd8f0194
+ 00bf5110 bytes b48f0194
~~~


<a id="compare-df752b1f6977fcc8a74dbe88e45c5120"></a>

### [`00bf4158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4158.md) → [`00bf514c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf514c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendERKS5_mm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5f090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf41f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4158.md#insn-00bf41f4) · [`00bf4220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4158.md#insn-00bf4220) · [`00bf4260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4158.md#insn-00bf4260)
- 新版 [`00bf51e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf514c.md#insn-00bf51e8) · [`00bf5214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf514c.md#insn-00bf5214) · [`00bf5254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf514c.md#insn-00bf5254)

~~~diff
- 00bf41f4 ["INT_ADD", "register:40f0:8", ["const:bf41f4:8", "const:4:8"]]
- 00bf41f4 ["CALL", null, ["callee:00c5f090:8"]]
+ 00bf51e8 ["INT_ADD", "register:40f0:8", ["const:bf51e8:8", "const:4:8"]]
+ 00bf51e8 ["CALL", null, ["callee:00c5f090:8"]]
- 00bf41f4 bytes b3a70194
+ 00bf51e8 bytes aaa70194
- 00bf4220 ["INT_ADD", "register:40f0:8", ["const:bf4220:8", "const:4:8"]]
- 00bf4220 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf5214 ["INT_ADD", "register:40f0:8", ["const:bf5214:8", "const:4:8"]]
+ 00bf5214 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf4220 bytes 7c8f0194
+ 00bf5214 bytes 738f0194
- 00bf4260 ["INT_ADD", "register:40f0:8", ["const:bf4260:8", "const:4:8"]]
- 00bf4260 ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf5254 ["INT_ADD", "register:40f0:8", ["const:bf5254:8", "const:4:8"]]
+ 00bf5254 ["CALL", null, ["callee:00bf3968:8"]]
- 00bf4260 bytes c5f9ff97
+ 00bf5254 bytes c5f9ff97
~~~


<a id="compare-308fd45fbec32c6677dac32a74902997"></a>

### [`00bf4264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4264.md) → [`00bf5258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5258.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEPKw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md) [`00c5e110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e110.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c5f0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0a0.md) [`00c5f0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4264.md#insn-00bf4284) · [`00bf42c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4264.md#insn-00bf42c8) · [`00bf42f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4264.md#insn-00bf42f4)
- 新版 [`00bf5278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5258.md#insn-00bf5278) · [`00bf52bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5258.md#insn-00bf52bc) · [`00bf52e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5258.md#insn-00bf52e8)

~~~diff
- 00bf4284 ["INT_ADD", "register:40f0:8", ["const:bf4284:8", "const:4:8"]]
- 00bf4284 ["CALL", null, ["callee:00c5f0a0:8"]]
+ 00bf5278 ["INT_ADD", "register:40f0:8", ["const:bf5278:8", "const:4:8"]]
+ 00bf5278 ["CALL", null, ["callee:00c5f0a0:8"]]
- 00bf4284 bytes 93a70194
+ 00bf5278 bytes 8aa70194
- 00bf42c8 ["INT_ADD", "register:40f0:8", ["const:bf42c8:8", "const:4:8"]]
- 00bf42c8 ["CALL", null, ["callee:00c5f0e0:8"]]
+ 00bf52bc ["INT_ADD", "register:40f0:8", ["const:bf52bc:8", "const:4:8"]]
+ 00bf52bc ["CALL", null, ["callee:00c5f0e0:8"]]
- 00bf42c8 bytes 92a70194
+ 00bf52bc bytes 89a70194
- 00bf42f4 ["INT_ADD", "register:40f0:8", ["const:bf42f4:8", "const:4:8"]]
- 00bf42f4 ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf52e8 ["INT_ADD", "register:40f0:8", ["const:bf52e8:8", "const:4:8"]]
+ 00bf52e8 ["CALL", null, ["callee:00bf3968:8"]]
- 00bf42f4 bytes a0f9ff97
+ 00bf52e8 bytes a0f9ff97
~~~


<a id="compare-2412ba02f3a68d615a513d6a7d190b41"></a>

### [`00bf42fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf42fc.md) → [`00bf52f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf52f0.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKwm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c5e110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e110.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c5f0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf42fc.md#insn-00bf4360) · [`00bf4384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf42fc.md#insn-00bf4384)
- 新版 [`00bf5354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf52f0.md#insn-00bf5354) · [`00bf5378`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf52f0.md#insn-00bf5378)

~~~diff
- 00bf4360 ["INT_ADD", "register:40f0:8", ["const:bf4360:8", "const:4:8"]]
- 00bf4360 ["CALL", null, ["callee:00c5f0e0:8"]]
+ 00bf5354 ["INT_ADD", "register:40f0:8", ["const:bf5354:8", "const:4:8"]]
+ 00bf5354 ["CALL", null, ["callee:00c5f0e0:8"]]
- 00bf4360 bytes 6ca70194
+ 00bf5354 bytes 63a70194
- 00bf4384 ["INT_ADD", "register:40f0:8", ["const:bf4384:8", "const:4:8"]]
- 00bf4384 ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf5378 ["INT_ADD", "register:40f0:8", ["const:bf5378:8", "const:4:8"]]
+ 00bf5378 ["CALL", null, ["callee:00bf3968:8"]]
- 00bf4384 bytes 7cf9ff97
+ 00bf5378 bytes 7cf9ff97
~~~


<a id="compare-5f0419b7cdf1db37b06302c57166f2fd"></a>

### [`00bf4388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4388.md) → [`00bf537c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf537c.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md) [`00c5e110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e110.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c5f0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0a0.md) [`00c5f0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf43b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4388.md#insn-00bf43b4) · [`00bf440c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4388.md#insn-00bf440c) · [`00bf443c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4388.md#insn-00bf443c)
- 新版 [`00bf53a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf537c.md#insn-00bf53a8) · [`00bf5400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf537c.md#insn-00bf5400) · [`00bf5430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf537c.md#insn-00bf5430)

~~~diff
- 00bf43b4 ["INT_ADD", "register:40f0:8", ["const:bf43b4:8", "const:4:8"]]
- 00bf43b4 ["CALL", null, ["callee:00c5f0a0:8"]]
+ 00bf53a8 ["INT_ADD", "register:40f0:8", ["const:bf53a8:8", "const:4:8"]]
+ 00bf53a8 ["CALL", null, ["callee:00c5f0a0:8"]]
- 00bf43b4 bytes 47a70194
+ 00bf53a8 bytes 3ea70194
- 00bf440c ["INT_ADD", "register:40f0:8", ["const:bf440c:8", "const:4:8"]]
- 00bf440c ["CALL", null, ["callee:00c5f0e0:8"]]
+ 00bf5400 ["INT_ADD", "register:40f0:8", ["const:bf5400:8", "const:4:8"]]
+ 00bf5400 ["CALL", null, ["callee:00c5f0e0:8"]]
- 00bf440c bytes 41a70194
+ 00bf5400 bytes 38a70194
- 00bf443c ["INT_ADD", "register:40f0:8", ["const:bf443c:8", "const:4:8"]]
- 00bf443c ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf5430 ["INT_ADD", "register:40f0:8", ["const:bf5430:8", "const:4:8"]]
+ 00bf5430 ["CALL", null, ["callee:00bf3968:8"]]
- 00bf443c bytes 4ef9ff97
+ 00bf5430 bytes 4ef9ff97
~~~


<a id="compare-23733def064ce0382770962796e71029"></a>

### [`00bf4440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4440.md) → [`00bf5434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5434.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4440.md#insn-00bf4484)
- 新版 [`00bf5478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5434.md#insn-00bf5478)

~~~diff
- 00bf4484 ["INT_ADD", "register:40f0:8", ["const:bf4484:8", "const:4:8"]]
- 00bf4484 ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf5478 ["INT_ADD", "register:40f0:8", ["const:bf5478:8", "const:4:8"]]
+ 00bf5478 ["CALL", null, ["callee:00bf3968:8"]]
- 00bf4484 bytes 3cf9ff97
+ 00bf5478 bytes 3cf9ff97
~~~


<a id="compare-afb896861341d2c864f10672a3f34f45"></a>

### [`00bf4490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4490.md) → [`00bf5484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5484.md) FUN_00bf5484

採用 · 移動量 `+0xff4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf4488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4488.md) · 呼出先 2件 [`00bf343c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf343c.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md)
- 新版 呼出元 1件 [`00bf547c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf547c.md) · 呼出先 2件 [`00bf4430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf4/00bf4430.md) [`00c5f0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf44ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4490.md#insn-00bf44ac)
- 新版 [`00bf54a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5484.md#insn-00bf54a0)

~~~diff
- 00bf44ac ["INT_ADD", "register:40f0:8", ["const:bf44ac:8", "const:4:8"]]
- 00bf44ac ["CALL", null, ["callee:00c5f0a0:8"]]
+ 00bf54a0 ["INT_ADD", "register:40f0:8", ["const:bf54a0:8", "const:4:8"]]
+ 00bf54a0 ["CALL", null, ["callee:00c5f0a0:8"]]
- 00bf44ac bytes 09a70194
+ 00bf54a0 bytes 00a70194
~~~


<a id="compare-a70483241d79022d9ac03c21d545e19c"></a>

### [`00bf44cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf44cc.md) → [`00bf54c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf54c0.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4findEPKwmm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md) [`00c5e110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e110.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c594f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594f0.md) [`00c5f0e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0e0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf44cc.md#insn-00bf4578) · [`00bf458c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf44cc.md#insn-00bf458c)
- 新版 [`00bf556c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf54c0.md#insn-00bf556c) · [`00bf5580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf54c0.md#insn-00bf5580)

~~~diff
- 00bf4578 ["INT_ADD", "register:40f0:8", ["const:bf4578:8", "const:4:8"]]
- 00bf4578 ["CALL", null, ["callee:00c594f0:8"]]
+ 00bf556c ["INT_ADD", "register:40f0:8", ["const:bf556c:8", "const:4:8"]]
+ 00bf556c ["CALL", null, ["callee:00c594f0:8"]]
- 00bf4578 bytes ea8f0194
+ 00bf556c bytes e18f0194
- 00bf458c ["INT_ADD", "register:40f0:8", ["const:bf458c:8", "const:4:8"]]
- 00bf458c ["CALL", null, ["callee:00c5f0e0:8"]]
+ 00bf5580 ["INT_ADD", "register:40f0:8", ["const:bf5580:8", "const:4:8"]]
+ 00bf5580 ["CALL", null, ["callee:00c5f0e0:8"]]
- 00bf458c bytes e1a60194
+ 00bf5580 bytes d8a60194
~~~


<a id="compare-a6236be77e8a5bf58dc1ce935d775a8f"></a>

### [`00bf46bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf46bc.md) → [`00bf56b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf56b0.md) FUN_00bf56b0

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf4664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4664.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00bf5658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5658.md) · 呼出先 5件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`006d7aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/006d7/006d7aa8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf46fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf46bc.md#insn-00bf46fc) · [`00bf4744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf46bc.md#insn-00bf4744) · [`00bf4754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf46bc.md#insn-00bf4754)
- 新版 [`00bf56f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf56b0.md#insn-00bf56f0) · [`00bf5738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf56b0.md#insn-00bf5738) · [`00bf5748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf56b0.md#insn-00bf5748)

~~~diff
- 00bf46fc ["INT_ADD", "register:40f0:8", ["const:bf46fc:8", "const:4:8"]]
- 00bf46fc ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf56f0 ["INT_ADD", "register:40f0:8", ["const:bf56f0:8", "const:4:8"]]
+ 00bf56f0 ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf46fc bytes 458e0194
+ 00bf56f0 bytes 3c8e0194
- 00bf4744 ["INT_ADD", "register:40f0:8", ["const:bf4744:8", "const:4:8"]]
- 00bf4744 ["CALL", null, ["callee:00c58f30:8"]]
+ 00bf5738 ["INT_ADD", "register:40f0:8", ["const:bf5738:8", "const:4:8"]]
+ 00bf5738 ["CALL", null, ["callee:00c58f30:8"]]
- 00bf4744 bytes 078e0194
+ 00bf5738 bytes fe8d0194
- 00bf4754 ["INT_ADD", "register:40f0:8", ["const:bf4754:8", "const:4:8"]]
- 00bf4754 ["CALL", null, ["callee:00c590a0:8"]]
+ 00bf5748 ["INT_ADD", "register:40f0:8", ["const:bf5748:8", "const:4:8"]]
+ 00bf5748 ["CALL", null, ["callee:00c590a0:8"]]
- 00bf4754 bytes 5f8e0194
+ 00bf5748 bytes 568e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b740dbc9df4574ea13e0d05ce106bf2"></a>

### [`00bf4790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4790.md) → [`00bf5784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5784.md) FUN_00bf5784

採用 · 移動量 `+0xff4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf4664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4664.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)
- 新版 呼出元 1件 [`00bf5658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5658.md) · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5f090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f090.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf47d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4790.md#insn-00bf47d8) · [`00bf4804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4790.md#insn-00bf4804)
- 新版 [`00bf57cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5784.md#insn-00bf57cc) · [`00bf57f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5784.md#insn-00bf57f8)

~~~diff
- 00bf47d8 ["INT_ADD", "register:40f0:8", ["const:bf47d8:8", "const:4:8"]]
- 00bf47d8 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf57cc ["INT_ADD", "register:40f0:8", ["const:bf57cc:8", "const:4:8"]]
+ 00bf57cc ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf47d8 bytes 0e8e0194
+ 00bf57cc bytes 058e0194
- 00bf4804 ["INT_ADD", "register:40f0:8", ["const:bf4804:8", "const:4:8"]]
- 00bf4804 ["CALL", null, ["callee:00c5f090:8"]]
+ 00bf57f8 ["INT_ADD", "register:40f0:8", ["const:bf57f8:8", "const:4:8"]]
+ 00bf57f8 ["CALL", null, ["callee:00c5f090:8"]]
- 00bf4804 bytes 2fa60194
+ 00bf57f8 bytes 26a60194
~~~


<a id="compare-f57b43674bbd83fb7766e124884c2ded"></a>

### [`00bf4820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4820.md) → [`00bf5814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5814.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEPKw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5f090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f090.md) [`00c5f0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f0a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4820.md#insn-00bf4844) · [`00bf48a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4820.md#insn-00bf48a0) · [`00bf48c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4820.md#insn-00bf48c8)
- 新版 [`00bf5838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5814.md#insn-00bf5838) · [`00bf5894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5814.md#insn-00bf5894) · [`00bf58bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5814.md#insn-00bf58bc)

~~~diff
- 00bf4844 ["INT_ADD", "register:40f0:8", ["const:bf4844:8", "const:4:8"]]
- 00bf4844 ["CALL", null, ["callee:00c5f0a0:8"]]
+ 00bf5838 ["INT_ADD", "register:40f0:8", ["const:bf5838:8", "const:4:8"]]
+ 00bf5838 ["CALL", null, ["callee:00c5f0a0:8"]]
- 00bf4844 bytes 23a60194
+ 00bf5838 bytes 1aa60194
- 00bf48a0 ["INT_ADD", "register:40f0:8", ["const:bf48a0:8", "const:4:8"]]
- 00bf48a0 ["CALL", null, ["callee:00c5f090:8"]]
+ 00bf5894 ["INT_ADD", "register:40f0:8", ["const:bf5894:8", "const:4:8"]]
+ 00bf5894 ["CALL", null, ["callee:00c5f090:8"]]
- 00bf48a0 bytes 08a60194
+ 00bf5894 bytes ffa50194
- 00bf48c8 ["INT_ADD", "register:40f0:8", ["const:bf48c8:8", "const:4:8"]]
- 00bf48c8 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf58bc ["INT_ADD", "register:40f0:8", ["const:bf58bc:8", "const:4:8"]]
+ 00bf58bc ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf48c8 bytes d28d0194
+ 00bf58bc bytes c98d0194
~~~


<a id="compare-6e3a43e8f020a7a117478ac8c1f36090"></a>

### [`00bf4908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4908.md) → [`00bf58fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf58fc.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c5e0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf3968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf3/00bf3968.md) [`00c5f080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5f/00c5f080.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4908.md#insn-00bf4954)
- 新版 [`00bf5948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf58fc.md#insn-00bf5948)

~~~diff
- 00bf4954 ["INT_ADD", "register:40f0:8", ["const:bf4954:8", "const:4:8"]]
- 00bf4954 ["CALL", null, ["callee:00bf3968:8"]]
+ 00bf5948 ["INT_ADD", "register:40f0:8", ["const:bf5948:8", "const:4:8"]]
+ 00bf5948 ["CALL", null, ["callee:00bf3968:8"]]
- 00bf4954 bytes 08f8ff97
+ 00bf5948 bytes 08f8ff97
~~~


<a id="compare-502cfad98905f4a2ab8e5e5a8d895428"></a>

### [`00bf4958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4958.md) → [`00bf594c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf594c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertENS_11__wrap_iterIPKwEEw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md) [`00c5b940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf49d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4958.md#insn-00bf49d8) · [`00bf4a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4958.md#insn-00bf4a08)
- 新版 [`00bf59cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf594c.md#insn-00bf59cc) · [`00bf59fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf594c.md#insn-00bf59fc)

~~~diff
- 00bf49d8 ["INT_ADD", "register:40f0:8", ["const:bf49d8:8", "const:4:8"]]
- 00bf49d8 ["CALL", null, ["callee:00c5b940:8"]]
+ 00bf59cc ["INT_ADD", "register:40f0:8", ["const:bf59cc:8", "const:4:8"]]
+ 00bf59cc ["CALL", null, ["callee:00c5b940:8"]]
- 00bf49d8 bytes e6970194
+ 00bf59cc bytes dd970194
- 00bf4a08 ["INT_ADD", "register:40f0:8", ["const:bf4a08:8", "const:4:8"]]
- 00bf4a08 ["CALL", null, ["callee:00c58fe0:8"]]
+ 00bf59fc ["INT_ADD", "register:40f0:8", ["const:bf59fc:8", "const:4:8"]]
+ 00bf59fc ["CALL", null, ["callee:00c58fe0:8"]]
- 00bf4a08 bytes 828d0194
+ 00bf59fc bytes 798d0194
~~~


<a id="compare-d3909f11bb1a9776126128021f1025f4"></a>

### [`00bf4a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4a5c.md) → [`00bf5a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5a50.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6resizeEmw

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a960.md) · 呼出先 1件 [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)
- 新版 呼出元 1件 [`00c5b930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b930.md) · 呼出先 1件 [`00c5b940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b940.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4ae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4a5c.md#insn-00bf4ae0)
- 新版 [`00bf5ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf5/00bf5a50.md#insn-00bf5ad4)

~~~diff
- 00bf4ae0 ["INT_ADD", "register:40f0:8", ["const:bf4ae0:8", "const:4:8"]]
- 00bf4ae0 ["CALL", null, ["callee:00c5b940:8"]]
+ 00bf5ad4 ["INT_ADD", "register:40f0:8", ["const:bf5ad4:8", "const:4:8"]]
+ 00bf5ad4 ["CALL", null, ["callee:00c5b940:8"]]
- 00bf4ae0 bytes a4970194
+ 00bf5ad4 bytes 9b970194
~~~


