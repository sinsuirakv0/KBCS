# v16.0.1 → v16.0.2 · 要調査の変更候補 (40)

[一覧の目次](README.md)

<a id="compare-5d773bd35be4abbc640f01bb8a0e9cb3"></a>

### [`00be1f08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f08.md) → [`00be1fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be1/00be1fa4.md) _ZNK8firebase4auth4User37UpdatePhoneNumberCredentialLastResultEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5ac70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ac70.md) [`00c5ad50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ad50.md) [`00c5ae10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5ae10.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ad40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ad40.md) [`00c5ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ae20.md) [`00c5aee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aee0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f08.md#insn-00be1f28) · [`00be1f34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f08.md#insn-00be1f34) · [`00be1f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f08.md#insn-00be1f40)
- 新版 `00be1fc4`（命令位置の公開資料なし） · `00be1fd0`（命令位置の公開資料なし） · `00be1fdc`（命令位置の公開資料なし）

~~~diff
- 00be1f28 ["INT_ADD", "register:40f0:8", ["const:be1f28:8", "const:4:8"]]
- 00be1f28 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be1fc4 ["INT_ADD", "register:40f0:8", ["const:be1fc4:8", "const:4:8"]]
+ 00be1fc4 ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1f28 bytes b6e20194
+ 00be1fc4 bytes c3e20194
- 00be1f34 ["INT_ADD", "register:40f0:8", ["const:be1f34:8", "const:4:8"]]
- 00be1f34 ["CALL", null, ["callee:00c5aae0:8"]]
+ 00be1fd0 ["INT_ADD", "register:40f0:8", ["const:be1fd0:8", "const:4:8"]]
+ 00be1fd0 ["CALL", null, ["callee:00c5aae0:8"]]
- 00be1f34 bytes b7e20194
+ 00be1fd0 bytes c4e20194
- 00be1f40 ["INT_ADD", "register:40f0:8", ["const:be1f40:8", "const:4:8"]]
- 00be1f40 ["CALL", null, ["callee:00c5ad40:8"]]
+ 00be1fdc ["INT_ADD", "register:40f0:8", ["const:be1fdc:8", "const:4:8"]]
+ 00be1fdc ["CALL", null, ["callee:00c5ad40:8"]]
- 00be1f40 bytes 4ce30194
+ 00be1fdc bytes 59e30194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92cb954d85466b6e191caf30d359ae89"></a>

### [`00be1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f98.md) → [`00be2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be2034.md) _ZN8firebase4auth4User18GetTokenThreadSafeEb

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0087b3bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0087b/0087b3bc.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c5aa00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa00.md) [`00c5aa10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa10.md) [`00c5aa70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5aa70.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0087b414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0087b/0087b414.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5aad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aad0.md) [`00c5aae0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5aae0.md) [`00c5ab40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5ab40.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be1fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f98.md#insn-00be1fc8) · [`00be1fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f98.md#insn-00be1fd0) · [`00be1fec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be1/00be1f98.md#insn-00be1fec)
- 新版 `00be2064`（命令位置の公開資料なし） · `00be206c`（命令位置の公開資料なし） · `00be2088`（命令位置の公開資料なし）

~~~diff
- 00be1fc8 ["INT_ADD", "register:40f0:8", ["const:be1fc8:8", "const:4:8"]]
- 00be1fc8 ["CALL", null, ["callee:00c5ab40:8"]]
+ 00be2064 ["INT_ADD", "register:40f0:8", ["const:be2064:8", "const:4:8"]]
+ 00be2064 ["CALL", null, ["callee:00c5ab40:8"]]
- 00be1fc8 bytes aae20194
+ 00be2064 bytes b7e20194
- 00be1fd0 ["INT_ADD", "register:40f0:8", ["const:be1fd0:8", "const:4:8"]]
- 00be1fd0 ["CALL", null, ["callee:00c5aad0:8"]]
+ 00be206c ["INT_ADD", "register:40f0:8", ["const:be206c:8", "const:4:8"]]
+ 00be206c ["CALL", null, ["callee:00c5aad0:8"]]
- 00be1fd0 bytes 8ce20194
+ 00be206c bytes 99e20194
- 00be1fec ["COPY", "register:0:8", ["register:4040:8"]]
- 00be1fec ["INT_ADD", "register:40f0:8", ["const:be1fec:8", "const:4:8"]]
- 00be1fec ["CALLIND", null, ["register:0:8"]]
+ 00be2088 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00be2088 ["INT_ADD", "register:40f0:8", ["const:be2088:8", "const:4:8"]]
+ 00be2088 ["CALLIND", null, ["register:0:8"]]
- 00be1fec bytes 00013fd6
+ 00be2088 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96f8774668116ebd1c133b009aecda4f"></a>

### [`00be21e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be21e0.md) → [`00be227c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be2/00be227c.md) _ZN8firebase4auth17UserInfoInterfaceD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5db80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5db80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5dc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dc50.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be21f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be2/00be21e0.md#insn-00be21f0)
- 新版 `00be228c`（命令位置の公開資料なし）

~~~diff
- 00be21f0 ["INT_ADD", "register:40f0:8", ["const:be21f0:8", "const:4:8"]]
- 00be21f0 ["CALL", null, ["callee:00c5dc50:8"]]
+ 00be228c ["INT_ADD", "register:40f0:8", ["const:be228c:8", "const:4:8"]]
+ 00be228c ["CALL", null, ["callee:00c5dc50:8"]]
- 00be21f0 bytes 64ee0194
+ 00be228c bytes 71ee0194
~~~


<a id="compare-1437bc7a81584ca8a5b0cc86d0ef1f42"></a>

### [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) → [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) FUN_00be86f4

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00be8638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8638.md) [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) · 呼出先 5件 [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) [`00beef20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md) [`00bef33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md) [`00bef594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef594.md) [`00c533c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c533c8.md)
- 新版 呼出元 2件 [`00be86d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86d4.md) [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) · 呼出先 5件 [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) [`00beefbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beefbc.md) [`00bef3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef3d8.md) [`00bef630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef630.md) [`00c53464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53464.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00be86fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md#insn-00be86fc) · [`00be8708`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md#insn-00be8708) · [`00be872c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md#insn-00be872c)
- 新版 `00be8798`（命令位置の公開資料なし） · `00be87a4`（命令位置の公開資料なし） · `00be87c8`（命令位置の公開資料なし）

~~~diff
- 00be86fc ["INT_ADD", "register:40f0:8", ["const:be86fc:8", "const:4:8"]]
- 00be86fc ["CALL", null, ["callee:00c53464:8"]]
+ 00be8798 ["INT_ADD", "register:40f0:8", ["const:be8798:8", "const:4:8"]]
+ 00be8798 ["CALL", null, ["callee:00c53464:8"]]
- 00be86fc bytes 33ab0194
+ 00be8798 bytes 33ab0194
- 00be8708 ["INT_ADD", "register:40f0:8", ["const:be8708:8", "const:4:8"]]
- 00be8708 ["CALL", null, ["callee:00c53464:8"]]
+ 00be87a4 ["INT_ADD", "register:40f0:8", ["const:be87a4:8", "const:4:8"]]
+ 00be87a4 ["CALL", null, ["callee:00c53464:8"]]
- 00be8708 bytes 30ab0194
+ 00be87a4 bytes 30ab0194
- 00be872c ["INT_ADD", "register:40f0:8", ["const:be872c:8", "const:4:8"]]
- 00be872c ["CALL", null, ["callee:00c53464:8"]]
+ 00be87c8 ["INT_ADD", "register:40f0:8", ["const:be87c8:8", "const:4:8"]]
+ 00be87c8 ["CALL", null, ["callee:00c53464:8"]]
- 00be872c bytes 27ab0194
+ 00be87c8 bytes 27ab0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90d3fd7760b63ddb696647b22258fc13"></a>

### [`00beef20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md) → [`00beefbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beefbc.md) FUN_00beefbc

採用 · 移動量 `+0x9c` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) · 呼出先 2件 [`00bef33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md) [`00c533c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c533c8.md)
- 新版 呼出元 1件 [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) · 呼出先 2件 [`00bef3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef3d8.md) [`00c53464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53464.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00beef70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md#insn-00beef70) · [`00beefbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md#insn-00beefbc) · [`00beefd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md#insn-00beefd8)
- 新版 `00bef00c`（命令位置の公開資料なし） · `00bef058`（命令位置の公開資料なし） · `00bef074`（命令位置の公開資料なし）

~~~diff
- 00beef70 ["INT_ADD", "register:40f0:8", ["const:beef70:8", "const:4:8"]]
- 00beef70 ["CALL", null, ["callee:00c53464:8"]]
+ 00bef00c ["INT_ADD", "register:40f0:8", ["const:bef00c:8", "const:4:8"]]
+ 00bef00c ["CALL", null, ["callee:00c53464:8"]]
- 00beef70 bytes 16910194
+ 00bef00c bytes 16910194
- 00beefbc ["INT_ADD", "register:40f0:8", ["const:beefbc:8", "const:4:8"]]
- 00beefbc ["CALL", null, ["callee:00bef3d8:8"]]
+ 00bef058 ["INT_ADD", "register:40f0:8", ["const:bef058:8", "const:4:8"]]
+ 00bef058 ["CALL", null, ["callee:00bef3d8:8"]]
- 00beefbc bytes e0000094
+ 00bef058 bytes e0000094
- 00beefd8 ["INT_ADD", "register:40f0:8", ["const:beefd8:8", "const:4:8"]]
- 00beefd8 ["CALL", null, ["callee:00c53464:8"]]
+ 00bef074 ["INT_ADD", "register:40f0:8", ["const:bef074:8", "const:4:8"]]
+ 00bef074 ["CALL", null, ["callee:00c53464:8"]]
- 00beefd8 bytes fc900194
+ 00bef074 bytes fc900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1ffe3b54a0e8761e837327833cf49fc"></a>

### [`00bef33c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md) → [`00bef3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef3d8.md) FUN_00bef3d8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) [`00beef20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bee/00beef20.md) · 呼出先 1件 [`00c533c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c533c8.md)
- 新版 呼出元 2件 [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) [`00beefbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bee/00beefbc.md) · 呼出先 1件 [`00c53464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53464.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef384`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md#insn-00bef384) · [`00bef394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md#insn-00bef394) · [`00bef3b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef33c.md#insn-00bef3b4)
- 新版 `00bef420`（命令位置の公開資料なし） · `00bef430`（命令位置の公開資料なし） · `00bef450`（命令位置の公開資料なし）

~~~diff
- 00bef384 ["INT_ADD", "register:40f0:8", ["const:bef384:8", "const:4:8"]]
- 00bef384 ["CALL", null, ["callee:00c53464:8"]]
+ 00bef420 ["INT_ADD", "register:40f0:8", ["const:bef420:8", "const:4:8"]]
+ 00bef420 ["CALL", null, ["callee:00c53464:8"]]
- 00bef384 bytes 11900194
+ 00bef420 bytes 11900194
- 00bef394 ["INT_ADD", "register:40f0:8", ["const:bef394:8", "const:4:8"]]
- 00bef394 ["CALL", null, ["callee:00c53464:8"]]
+ 00bef430 ["INT_ADD", "register:40f0:8", ["const:bef430:8", "const:4:8"]]
+ 00bef430 ["CALL", null, ["callee:00c53464:8"]]
- 00bef394 bytes 0d900194
+ 00bef430 bytes 0d900194
- 00bef3b4 ["INT_ADD", "register:40f0:8", ["const:bef3b4:8", "const:4:8"]]
- 00bef3b4 ["CALL", null, ["callee:00c53464:8"]]
+ 00bef450 ["INT_ADD", "register:40f0:8", ["const:bef450:8", "const:4:8"]]
+ 00bef450 ["CALL", null, ["callee:00c53464:8"]]
- 00bef3b4 bytes 05900194
+ 00bef450 bytes 05900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28e58a19f428d8aedfd20821330ddf7b"></a>

### [`00bef594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef594.md) → [`00bef630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00bef630.md) FUN_00bef630

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00be8658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00be8/00be8658.md) · 呼出先 1件 [`00c533c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c533c8.md)
- 新版 呼出元 1件 [`00be86f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00be8/00be86f4.md) · 呼出先 1件 [`00c53464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53464.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bef634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef594.md#insn-00bef634) · [`00bef658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef594.md#insn-00bef658) · [`00bef674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00bef594.md#insn-00bef674)
- 新版 `00bef6d0`（命令位置の公開資料なし） · `00bef6f4`（命令位置の公開資料なし） · `00bef710`（命令位置の公開資料なし）

~~~diff
- 00bef634 ["INT_ADD", "register:40f0:8", ["const:bef634:8", "const:4:8"]]
- 00bef634 ["CALL", null, ["callee:00c53464:8"]]
+ 00bef6d0 ["INT_ADD", "register:40f0:8", ["const:bef6d0:8", "const:4:8"]]
+ 00bef6d0 ["CALL", null, ["callee:00c53464:8"]]
- 00bef634 bytes 658f0194
+ 00bef6d0 bytes 658f0194
- 00bef658 ["INT_ADD", "register:40f0:8", ["const:bef658:8", "const:4:8"]]
- 00bef658 ["CALL", null, ["callee:00c53464:8"]]
+ 00bef6f4 ["INT_ADD", "register:40f0:8", ["const:bef6f4:8", "const:4:8"]]
+ 00bef6f4 ["CALL", null, ["callee:00c53464:8"]]
- 00bef658 bytes 5c8f0194
+ 00bef6f4 bytes 5c8f0194
- 00bef674 ["INT_ADD", "register:40f0:8", ["const:bef674:8", "const:4:8"]]
- 00bef674 ["CALL", null, ["callee:00c53464:8"]]
+ 00bef710 ["INT_ADD", "register:40f0:8", ["const:bef710:8", "const:4:8"]]
+ 00bef710 ["CALL", null, ["callee:00c53464:8"]]
- 00bef674 bytes 558f0194
+ 00bef710 bytes 558f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce92a923dbf54a3923ef26c7e1f04239"></a>

### [`00befa60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa60.md) → [`00befafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befafc.md) _ZSt18uncaught_exceptionv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5d0f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5d0f0.md) · 呼出先 1件 [`00c5df00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df00.md)
- 新版 呼出元 1件 [`00c5d1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5d1c0.md) · 呼出先 1件 [`00c5dfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfd0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befa6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befa60.md#insn-00befa6c)
- 新版 `00befb08`（命令位置の公開資料なし）

~~~diff
- 00befa6c ["INT_ADD", "register:40f0:8", ["const:befa6c:8", "const:4:8"]]
- 00befa6c ["CALL", null, ["callee:00c5dfd0:8"]]
+ 00befb08 ["INT_ADD", "register:40f0:8", ["const:befb08:8", "const:4:8"]]
+ 00befb08 ["CALL", null, ["callee:00c5dfd0:8"]]
- 00befa6c bytes 25b90194
+ 00befb08 bytes 32b90194
~~~


<a id="compare-263d816a7f0177b15b6e1057f9e24e27"></a>

### [`00befab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befab0.md) → [`00befb4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befb4c.md) _ZNSt13exception_ptraSERKS_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5df30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df30.md) · 呼出先 2件 [`00c5df10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df10.md) [`00c5df20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df20.md)
- 新版 呼出元 1件 [`00c5e000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e000.md) · 呼出先 2件 [`00c5dfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dfe0.md) [`00c5dff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5d/00c5dff0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befab0.md#insn-00befad8) · [`00befae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befab0.md#insn-00befae0)
- 新版 `00befb74`（命令位置の公開資料なし） · `00befb7c`（命令位置の公開資料なし）

~~~diff
- 00befad8 ["INT_ADD", "register:40f0:8", ["const:befad8:8", "const:4:8"]]
- 00befad8 ["CALL", null, ["callee:00c5dff0:8"]]
+ 00befb74 ["INT_ADD", "register:40f0:8", ["const:befb74:8", "const:4:8"]]
+ 00befb74 ["CALL", null, ["callee:00c5dff0:8"]]
- 00befad8 bytes 12b90194
+ 00befb74 bytes 1fb90194
- 00befae0 ["INT_ADD", "register:40f0:8", ["const:befae0:8", "const:4:8"]]
- 00befae0 ["CALL", null, ["callee:00c5dfe0:8"]]
+ 00befb7c ["INT_ADD", "register:40f0:8", ["const:befb7c:8", "const:4:8"]]
+ 00befb7c ["CALL", null, ["callee:00c5dfe0:8"]]
- 00befae0 bytes 0cb90194
+ 00befb7c bytes 19b90194
~~~


<a id="compare-fc5f5b7da94b026f94334df4c324ffc8"></a>

### [`00befb48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb48.md) → [`00befbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befbe4.md) _ZSt17current_exceptionv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58560`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58560.md) · 呼出先 1件 [`00c5df40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df40.md)
- 新版 呼出元 1件 [`00c58630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58630.md) · 呼出先 1件 [`00c5e010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb48.md#insn-00befb5c)
- 新版 `00befbf8`（命令位置の公開資料なし）

~~~diff
- 00befb5c ["INT_ADD", "register:40f0:8", ["const:befb5c:8", "const:4:8"]]
- 00befb5c ["CALL", null, ["callee:00c5e010:8"]]
+ 00befbf8 ["INT_ADD", "register:40f0:8", ["const:befbf8:8", "const:4:8"]]
+ 00befbf8 ["CALL", null, ["callee:00c5e010:8"]]
- 00befb5c bytes f9b80194
+ 00befbf8 bytes 06b90194
~~~


<a id="compare-18a9c3fdfdf55644b0aeb380da6ea642"></a>

### [`00befb8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb8c.md) → [`00befc28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befc28.md) _ZNSt16nested_exceptionD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5df50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5e020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e020.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befba0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befb8c.md#insn-00befba0)
- 新版 `00befc3c`（命令位置の公開資料なし）

~~~diff
- 00befba0 ["INT_ADD", "register:40f0:8", ["const:befba0:8", "const:4:8"]]
- 00befba0 ["CALL", null, ["callee:00c5e020:8"]]
+ 00befc3c ["INT_ADD", "register:40f0:8", ["const:befc3c:8", "const:4:8"]]
+ 00befc3c ["CALL", null, ["callee:00c5e020:8"]]
- 00befba0 bytes ecb80194
+ 00befc3c bytes f9b80194
~~~


<a id="compare-2f8cc74a56811c539f79cf0da0a33b18"></a>

### [`00befbb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befbb8.md) → [`00befc54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befc54.md) _ZNKSt16nested_exception14rethrow_nestedEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c582f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c582f0.md) [`00c584b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584b0.md) [`00c584c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c583c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c583c0.md) [`00c58580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58580.md) [`00c58590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58590.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befbdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befbb8.md#insn-00befbdc) · [`00befbe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befbb8.md#insn-00befbe4) · [`00befbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befbb8.md#insn-00befbf0)
- 新版 `00befc78`（命令位置の公開資料なし） · `00befc80`（命令位置の公開資料なし） · `00befc8c`（命令位置の公開資料なし）

~~~diff
- 00befbdc ["INT_ADD", "register:40f0:8", ["const:befbdc:8", "const:4:8"]]
- 00befbdc ["CALL", null, ["callee:00c583c0:8"]]
+ 00befc78 ["INT_ADD", "register:40f0:8", ["const:befc78:8", "const:4:8"]]
+ 00befc78 ["CALL", null, ["callee:00c583c0:8"]]
- 00befbdc bytes c5a10194
+ 00befc78 bytes d2a10194
- 00befbe4 ["INT_ADD", "register:40f0:8", ["const:befbe4:8", "const:4:8"]]
- 00befbe4 ["CALL", null, ["callee:00c580f0:8"]]
+ 00befc80 ["INT_ADD", "register:40f0:8", ["const:befc80:8", "const:4:8"]]
+ 00befc80 ["CALL", null, ["callee:00c580f0:8"]]
- 00befbe4 bytes 0fa10194
+ 00befc80 bytes 1ca10194
- 00befbf0 ["INT_ADD", "register:40f0:8", ["const:befbf0:8", "const:4:8"]]
- 00befbf0 ["CALL", null, ["callee:00c58580:8"]]
+ 00befc8c ["INT_ADD", "register:40f0:8", ["const:befc8c:8", "const:4:8"]]
+ 00befc8c ["CALL", null, ["callee:00c58580:8"]]
- 00befbf0 bytes 30a20194
+ 00befc8c bytes 3da20194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3320b15c656edb1728bb7306dab10a74"></a>

### [`00befc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc10.md) → [`00befcac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befcac.md) _ZSt17rethrow_exceptionSt13exception_ptr

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c584c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584c0.md) · 呼出先 2件 [`00c58020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5df60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5df60.md)
- 新版 呼出元 1件 [`00c58590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58590.md) · 呼出先 2件 [`00c580f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5e030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e030.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00befc20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc10.md#insn-00befc20) · [`00befc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bef/00befc10.md#insn-00befc24)
- 新版 `00befcbc`（命令位置の公開資料なし） · `00befcc0`（命令位置の公開資料なし）

~~~diff
- 00befc20 ["INT_ADD", "register:40f0:8", ["const:befc20:8", "const:4:8"]]
- 00befc20 ["CALL", null, ["callee:00c5e030:8"]]
+ 00befcbc ["INT_ADD", "register:40f0:8", ["const:befcbc:8", "const:4:8"]]
+ 00befcbc ["CALL", null, ["callee:00c5e030:8"]]
- 00befc20 bytes d0b80194
+ 00befcbc bytes ddb80194
- 00befc24 ["INT_ADD", "register:40f0:8", ["const:befc24:8", "const:4:8"]]
- 00befc24 ["CALL", null, ["callee:00c580f0:8"]]
+ 00befcc0 ["INT_ADD", "register:40f0:8", ["const:befcc0:8", "const:4:8"]]
+ 00befcc0 ["CALL", null, ["callee:00c580f0:8"]]
- 00befc24 bytes ffa00194
+ 00befcc0 bytes 0ca10194
~~~


<a id="compare-2c5ac091289483768fd9bb80ad2b5db7"></a>

### [`00bf03dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf03dc.md) → [`00bf0478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0478.md) _ZNSt6__ndk112bad_weak_ptrD0Ev

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c5a790`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a790.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c5a860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a860.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf03f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf03dc.md#insn-00bf03f0)
- 新版 `00bf048c`（命令位置の公開資料なし）

~~~diff
- 00bf03f0 ["INT_ADD", "register:40f0:8", ["const:bf03f0:8", "const:4:8"]]
- 00bf03f0 ["CALL", null, ["callee:00c5a860:8"]]
+ 00bf048c ["INT_ADD", "register:40f0:8", ["const:bf048c:8", "const:4:8"]]
+ 00bf048c ["CALL", null, ["callee:00c5a860:8"]]
- 00bf03f0 bytes e8a80194
+ 00bf048c bytes f5a80194
~~~


<a id="compare-285cfca73d34816ce78aeb5ac7c14f6d"></a>

### [`00bf0430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0430.md) → [`00bf04cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf04cc.md) _ZNSt6__ndk114__shared_count12__add_sharedEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0444`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0430.md#insn-00bf0444)
- 新版 `00bf04e0`（命令位置の公開資料なし）

~~~diff
- 00bf0444 ["INT_ADD", "register:40f0:8", ["const:bf0444:8", "const:4:8"]]
- 00bf0444 ["CALL", null, ["callee:00c53d70:8"]]
+ 00bf04e0 ["INT_ADD", "register:40f0:8", ["const:bf04e0:8", "const:4:8"]]
+ 00bf04e0 ["CALL", null, ["callee:00c53d70:8"]]
- 00bf0444 bytes 238e0194
+ 00bf04e0 bytes 248e0194
~~~


<a id="compare-c886ad05ed28d64d4999a0601463050a"></a>

### [`00bf0454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0454.md) → [`00bf04f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf04f0.md) _ZNSt6__ndk114__shared_count16__release_sharedEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0470`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0454.md#insn-00bf0470) · [`00bf0488`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0454.md#insn-00bf0488)
- 新版 `00bf050c`（命令位置の公開資料なし） · `00bf0524`（命令位置の公開資料なし）

~~~diff
- 00bf0470 ["INT_ADD", "register:40f0:8", ["const:bf0470:8", "const:4:8"]]
- 00bf0470 ["CALL", null, ["callee:00c53da0:8"]]
+ 00bf050c ["INT_ADD", "register:40f0:8", ["const:bf050c:8", "const:4:8"]]
+ 00bf050c ["CALL", null, ["callee:00c53da0:8"]]
- 00bf0470 bytes 248e0194
+ 00bf050c bytes 258e0194
- 00bf0488 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bf0488 ["INT_ADD", "register:40f0:8", ["const:bf0488:8", "const:4:8"]]
- 00bf0488 ["CALLIND", null, ["register:0:8"]]
+ 00bf0524 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bf0524 ["INT_ADD", "register:40f0:8", ["const:bf0524:8", "const:4:8"]]
+ 00bf0524 ["CALLIND", null, ["register:0:8"]]
- 00bf0488 bytes 00013fd6
+ 00bf0524 bytes 00013fd6
~~~


<a id="compare-d6ce76980ce9eb7b4b52904cade3b2be"></a>

### [`00bf04a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04a4.md) → [`00bf0540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0540.md) _ZNSt6__ndk119__shared_weak_count12__add_sharedEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf04b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04a4.md#insn-00bf04b8)
- 新版 `00bf0554`（命令位置の公開資料なし）

~~~diff
- 00bf04b8 ["INT_ADD", "register:40f0:8", ["const:bf04b8:8", "const:4:8"]]
- 00bf04b8 ["CALL", null, ["callee:00c53d70:8"]]
+ 00bf0554 ["INT_ADD", "register:40f0:8", ["const:bf0554:8", "const:4:8"]]
+ 00bf0554 ["CALL", null, ["callee:00c53d70:8"]]
- 00bf04b8 bytes 068e0194
+ 00bf0554 bytes 078e0194
~~~


<a id="compare-97b0c3625a7bb9ecfc5875d6a01e491a"></a>

### [`00bf04c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04c8.md) → [`00bf0564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0564.md) _ZNSt6__ndk119__shared_weak_count10__add_weakEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf04dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04c8.md#insn-00bf04dc)
- 新版 `00bf0578`（命令位置の公開資料なし）

~~~diff
- 00bf04dc ["INT_ADD", "register:40f0:8", ["const:bf04dc:8", "const:4:8"]]
- 00bf04dc ["CALL", null, ["callee:00c53d70:8"]]
+ 00bf0578 ["INT_ADD", "register:40f0:8", ["const:bf0578:8", "const:4:8"]]
+ 00bf0578 ["CALL", null, ["callee:00c53d70:8"]]
- 00bf04dc bytes fd8d0194
+ 00bf0578 bytes fe8d0194
~~~


<a id="compare-2c7ff1380e92dd8429c07b5ab420eb50"></a>

### [`00bf04ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04ec.md) → [`00bf0588`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0588.md) _ZNSt6__ndk119__shared_weak_count16__release_sharedEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04ec.md#insn-00bf0508) · [`00bf0530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04ec.md#insn-00bf0530) · [`00bf0544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf04ec.md#insn-00bf0544)
- 新版 `00bf05a4`（命令位置の公開資料なし） · `00bf05cc`（命令位置の公開資料なし） · `00bf05e0`（命令位置の公開資料なし）

~~~diff
- 00bf0508 ["INT_ADD", "register:40f0:8", ["const:bf0508:8", "const:4:8"]]
- 00bf0508 ["CALL", null, ["callee:00c53da0:8"]]
+ 00bf05a4 ["INT_ADD", "register:40f0:8", ["const:bf05a4:8", "const:4:8"]]
+ 00bf05a4 ["CALL", null, ["callee:00c53da0:8"]]
- 00bf0508 bytes fe8d0194
+ 00bf05a4 bytes ff8d0194
- 00bf0530 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bf0530 ["INT_ADD", "register:40f0:8", ["const:bf0530:8", "const:4:8"]]
- 00bf0530 ["CALLIND", null, ["register:0:8"]]
+ 00bf05cc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bf05cc ["INT_ADD", "register:40f0:8", ["const:bf05cc:8", "const:4:8"]]
+ 00bf05cc ["CALLIND", null, ["register:0:8"]]
- 00bf0530 bytes 00013fd6
+ 00bf05cc bytes 00013fd6
- 00bf0544 ["INT_ADD", "register:40f0:8", ["const:bf0544:8", "const:4:8"]]
- 00bf0544 ["CALL", null, ["callee:00c53da0:8"]]
+ 00bf05e0 ["INT_ADD", "register:40f0:8", ["const:bf05e0:8", "const:4:8"]]
+ 00bf05e0 ["CALL", null, ["callee:00c53da0:8"]]
- 00bf0544 bytes ef8d0194
+ 00bf05e0 bytes f08d0194
~~~


<a id="compare-c51761d8d268d52d383e7d8b2c7eb3a8"></a>

### [`00bf0568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0568.md) → [`00bf0604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0604.md) _ZNSt6__ndk119__shared_weak_count14__release_weakEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) · 呼出先 1件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)
- 新版 呼出元 1件 [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) · 呼出先 1件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf058c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0568.md#insn-00bf058c)
- 新版 `00bf0628`（命令位置の公開資料なし）

~~~diff
- 00bf058c ["INT_ADD", "register:40f0:8", ["const:bf058c:8", "const:4:8"]]
- 00bf058c ["CALL", null, ["callee:00c53da0:8"]]
+ 00bf0628 ["INT_ADD", "register:40f0:8", ["const:bf0628:8", "const:4:8"]]
+ 00bf0628 ["CALL", null, ["callee:00c53da0:8"]]
- 00bf058c bytes dd8d0194
+ 00bf0628 bytes de8d0194
~~~


<a id="compare-23835a5b990ebf4c99ee008a836b298a"></a>

### [`00bf05c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf05c0.md) → [`00bf065c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf065c.md) _ZNSt6__ndk119__shared_weak_count4lockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c584f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c584f0.md) · 呼出先 1件 [`00c53c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53c00.md)
- 新版 呼出元 1件 [`00c585c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c585c0.md) · 呼出先 1件 [`00c53ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ca0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf05f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf05c0.md#insn-00bf05f0)
- 新版 `00bf068c`（命令位置の公開資料なし）

~~~diff
- 00bf05f0 ["INT_ADD", "register:40f0:8", ["const:bf05f0:8", "const:4:8"]]
- 00bf05f0 ["CALL", null, ["callee:00c53ca0:8"]]
+ 00bf068c ["INT_ADD", "register:40f0:8", ["const:bf068c:8", "const:4:8"]]
+ 00bf068c ["CALL", null, ["callee:00c53ca0:8"]]
- 00bf05f0 bytes 848d0194
+ 00bf068c bytes 858d0194
~~~


<a id="compare-9e4d0d6f76614c9a6da95841662fea3b"></a>

### [`00bf062c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf062c.md) → [`00bf06c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf06c8.md) _ZNSt6__ndk18__sp_mut4lockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b6a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b770.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf063c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf062c.md#insn-00bf063c)
- 新版 `00bf06d8`（命令位置の公開資料なし）

~~~diff
- 00bf063c ["INT_ADD", "register:40f0:8", ["const:bf063c:8", "const:4:8"]]
- 00bf063c ["CALL", null, ["callee:00c5b770:8"]]
+ 00bf06d8 ["INT_ADD", "register:40f0:8", ["const:bf06d8:8", "const:4:8"]]
+ 00bf06d8 ["CALL", null, ["callee:00c5b770:8"]]
- 00bf063c bytes 19ac0194
+ 00bf06d8 bytes 26ac0194
~~~


<a id="compare-8733a4b0204fd2a041826354712b1f4c"></a>

### [`00bf0650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0650.md) → [`00bf06ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf06ec.md) _ZNSt6__ndk18__sp_mut6unlockEv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b6b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b6b0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5b780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b780.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0650.md#insn-00bf0660)
- 新版 `00bf06fc`（命令位置の公開資料なし）

~~~diff
- 00bf0660 ["INT_ADD", "register:40f0:8", ["const:bf0660:8", "const:4:8"]]
- 00bf0660 ["CALL", null, ["callee:00c5b780:8"]]
+ 00bf06fc ["INT_ADD", "register:40f0:8", ["const:bf06fc:8", "const:4:8"]]
+ 00bf06fc ["CALL", null, ["callee:00c5b780:8"]]
- 00bf0660 bytes 14ac0194
+ 00bf06fc bytes 21ac0194
~~~


<a id="compare-d6d85f4671475f8002045bbbacc7a18d"></a>

### [`00bf0674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0674.md) → [`00bf0710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0710.md) _ZNSt6__ndk112__get_sp_mutEPKv

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

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
    "old": {
      "definition_site": "00bf06c0",
      "incomplete_value": true,
      "site": "00bf06c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:ca46e8:8"
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

- 旧版 [`00bf06b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0674.md#insn-00bf06b4)
- 新版 `00bf0750`（命令位置の公開資料なし）

~~~diff
- 00bf06b4 ["COPY", "register:4048:8", ["const:ca46e8:8"]]
+ 00bf0750 ["COPY", "register:4048:8", ["const:ca47b8:8"]]
- 00bf06b4 bytes a9015a10
+ 00bf0750 bytes 49035a10
~~~


<a id="compare-266f5776b776ec7aedca1dd4103000eb"></a>

### [`00bf08a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf08a4.md) → [`00bf0940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0940.md) _ZNSt11logic_erroraSERKS_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf08cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf08a4.md#insn-00bf08cc) · [`00bf08d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf08a4.md#insn-00bf08d8) · [`00bf08e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf08a4.md#insn-00bf08e8)
- 新版 `00bf0968`（命令位置の公開資料なし） · `00bf0974`（命令位置の公開資料なし） · `00bf0984`（命令位置の公開資料なし）

~~~diff
- 00bf08cc ["INT_ADD", "register:40f0:8", ["const:bf08cc:8", "const:4:8"]]
- 00bf08cc ["CALL", null, ["callee:00c53d40:8"]]
+ 00bf0968 ["INT_ADD", "register:40f0:8", ["const:bf0968:8", "const:4:8"]]
+ 00bf0968 ["CALL", null, ["callee:00c53d40:8"]]
- 00bf08cc bytes f58c0194
+ 00bf0968 bytes f68c0194
- 00bf08d8 ["INT_ADD", "register:40f0:8", ["const:bf08d8:8", "const:4:8"]]
- 00bf08d8 ["CALL", null, ["callee:00c53d40:8"]]
+ 00bf0974 ["INT_ADD", "register:40f0:8", ["const:bf0974:8", "const:4:8"]]
+ 00bf0974 ["CALL", null, ["callee:00c53d40:8"]]
- 00bf08d8 bytes f28c0194
+ 00bf0974 bytes f38c0194
- 00bf08e8 ["INT_ADD", "register:40f0:8", ["const:bf08e8:8", "const:4:8"]]
- 00bf08e8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bf0984 ["INT_ADD", "register:40f0:8", ["const:bf0984:8", "const:4:8"]]
+ 00bf0984 ["CALL", null, ["callee:00c57f80:8"]]
- 00bf08e8 bytes 729d0194
+ 00bf0984 bytes 7f9d0194
~~~


<a id="compare-25f697dac761b20e4db86740537fdbb6"></a>

### [`00bf0a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0a54.md) → [`00bf0af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0af0.md) _ZNSt13runtime_erroraSERKS_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53ca0.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c53d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d40.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0a54.md#insn-00bf0a7c) · [`00bf0a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0a54.md#insn-00bf0a88) · [`00bf0a98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0a54.md#insn-00bf0a98)
- 新版 `00bf0b18`（命令位置の公開資料なし） · `00bf0b24`（命令位置の公開資料なし） · `00bf0b34`（命令位置の公開資料なし）

~~~diff
- 00bf0a7c ["INT_ADD", "register:40f0:8", ["const:bf0a7c:8", "const:4:8"]]
- 00bf0a7c ["CALL", null, ["callee:00c53d40:8"]]
+ 00bf0b18 ["INT_ADD", "register:40f0:8", ["const:bf0b18:8", "const:4:8"]]
+ 00bf0b18 ["CALL", null, ["callee:00c53d40:8"]]
- 00bf0a7c bytes 898c0194
+ 00bf0b18 bytes 8a8c0194
- 00bf0a88 ["INT_ADD", "register:40f0:8", ["const:bf0a88:8", "const:4:8"]]
- 00bf0a88 ["CALL", null, ["callee:00c53d40:8"]]
+ 00bf0b24 ["INT_ADD", "register:40f0:8", ["const:bf0b24:8", "const:4:8"]]
+ 00bf0b24 ["CALL", null, ["callee:00c53d40:8"]]
- 00bf0a88 bytes 868c0194
+ 00bf0b24 bytes 878c0194
- 00bf0a98 ["INT_ADD", "register:40f0:8", ["const:bf0a98:8", "const:4:8"]]
- 00bf0a98 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bf0b34 ["INT_ADD", "register:40f0:8", ["const:bf0b34:8", "const:4:8"]]
+ 00bf0b34 ["CALL", null, ["callee:00c57f80:8"]]
- 00bf0a98 bytes 069d0194
+ 00bf0b34 bytes 139d0194
~~~


<a id="compare-a1608185b8ff18668e38525212b6ed1e"></a>

### [`00bf0b04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0b04.md) → [`00bf0ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0ba0.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58070.md) · 呼出先 3件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5b0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0a0.md)
- 新版 呼出元 1件 [`00c58140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58140.md) · 呼出先 3件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0b04.md#insn-00bf0ba4) · [`00bf0bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0b04.md#insn-00bf0bf0) · [`00bf0c00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0b04.md#insn-00bf0c00)
- 新版 `00bf0c40`（命令位置の公開資料なし） · `00bf0c8c`（命令位置の公開資料なし） · `00bf0c9c`（命令位置の公開資料なし）

~~~diff
- 00bf0ba4 ["INT_ADD", "register:40f0:8", ["const:bf0ba4:8", "const:4:8"]]
- 00bf0ba4 ["CALL", null, ["callee:00c5b170:8"]]
+ 00bf0c40 ["INT_ADD", "register:40f0:8", ["const:bf0c40:8", "const:4:8"]]
+ 00bf0c40 ["CALL", null, ["callee:00c5b170:8"]]
- 00bf0ba4 bytes 3fa90194
+ 00bf0c40 bytes 4ca90194
- 00bf0bf0 ["INT_ADD", "register:40f0:8", ["const:bf0bf0:8", "const:4:8"]]
- 00bf0bf0 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf0c8c ["INT_ADD", "register:40f0:8", ["const:bf0c8c:8", "const:4:8"]]
+ 00bf0c8c ["CALL", null, ["callee:00c58010:8"]]
- 00bf0bf0 bytes d49c0194
+ 00bf0c8c bytes e19c0194
- 00bf0c00 ["INT_ADD", "register:40f0:8", ["const:bf0c00:8", "const:4:8"]]
- 00bf0c00 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf0c9c ["INT_ADD", "register:40f0:8", ["const:bf0c9c:8", "const:4:8"]]
+ 00bf0c9c ["CALL", null, ["callee:00c58010:8"]]
- 00bf0c00 bytes d09c0194
+ 00bf0c9c bytes dd9c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-615de497661b3e17e89a3f834aac183c"></a>

### [`00bf0d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0d90.md) → [`00bf0e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0e2c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0dec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0d90.md#insn-00bf0dec) · [`00bf0e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0d90.md#insn-00bf0e10) · [`00bf0e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0d90.md#insn-00bf0e30)
- 新版 `00bf0e88`（命令位置の公開資料なし） · `00bf0eac`（命令位置の公開資料なし） · `00bf0ecc`（命令位置の公開資料なし）

~~~diff
- 00bf0dec ["INT_ADD", "register:40f0:8", ["const:bf0dec:8", "const:4:8"]]
- 00bf0dec ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf0e88 ["INT_ADD", "register:40f0:8", ["const:bf0e88:8", "const:4:8"]]
+ 00bf0e88 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf0dec bytes 299c0194
+ 00bf0e88 bytes 369c0194
- 00bf0e10 ["INT_ADD", "register:40f0:8", ["const:bf0e10:8", "const:4:8"]]
- 00bf0e10 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf0eac ["INT_ADD", "register:40f0:8", ["const:bf0eac:8", "const:4:8"]]
+ 00bf0eac ["CALL", null, ["callee:00c58010:8"]]
- 00bf0e10 bytes 4c9c0194
+ 00bf0eac bytes 599c0194
- 00bf0e30 ["INT_ADD", "register:40f0:8", ["const:bf0e30:8", "const:4:8"]]
- 00bf0e30 ["CALL", null, ["callee:0043b7a4:8"]]
+ 00bf0ecc ["INT_ADD", "register:40f0:8", ["const:bf0ecc:8", "const:4:8"]]
+ 00bf0ecc ["CALL", null, ["callee:0043b7a4:8"]]
- 00bf0e30 bytes 4d2ae197
+ 00bf0ecc bytes 362ae197
~~~


<a id="compare-40e5195eb95cb345c388eb7e2754b475"></a>

### [`00bf0e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0e60.md) → [`00bf0efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0efc.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58080.md) · 呼出先 2件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58070.md)
- 新版 呼出元 1件 [`00c58150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58150.md) · 呼出先 2件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0e60.md#insn-00bf0e88)
- 新版 `00bf0f24`（命令位置の公開資料なし）

~~~diff
- 00bf0e88 ["INT_ADD", "register:40f0:8", ["const:bf0e88:8", "const:4:8"]]
- 00bf0e88 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bf0f24 ["INT_ADD", "register:40f0:8", ["const:bf0f24:8", "const:4:8"]]
+ 00bf0f24 ["CALL", null, ["callee:00c580b0:8"]]
- 00bf0e88 bytes 569c0194
+ 00bf0f24 bytes 639c0194
~~~


<a id="compare-8f651f0baa61547a8c989bd07f7cf951"></a>

### [`00bf0ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0ee0.md) → [`00bf0f7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf0/00bf0f7c.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16find_last_not_ofEPKcmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0f3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0ee0.md#insn-00bf0f3c)
- 新版 `00bf0fd8`（命令位置の公開資料なし）

~~~diff
- 00bf0f3c ["INT_ADD", "register:40f0:8", ["const:bf0f3c:8", "const:4:8"]]
- 00bf0f3c ["CALL", null, ["callee:00c580a0:8"]]
+ 00bf0fd8 ["INT_ADD", "register:40f0:8", ["const:bf0fd8:8", "const:4:8"]]
+ 00bf0fd8 ["CALL", null, ["callee:00c580a0:8"]]
- 00bf0f3c bytes 259c0194
+ 00bf0fd8 bytes 329c0194
~~~


<a id="compare-d61e006204a6720ef74760f099f7eb6c"></a>

### [`00bf0f78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0f78.md) → [`00bf1014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1014.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17find_first_not_ofEPKcmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf0fcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf0/00bf0f78.md#insn-00bf0fcc)
- 新版 `00bf1068`（命令位置の公開資料なし）

~~~diff
- 00bf0fcc ["INT_ADD", "register:40f0:8", ["const:bf0fcc:8", "const:4:8"]]
- 00bf0fcc ["CALL", null, ["callee:00c580a0:8"]]
+ 00bf1068 ["INT_ADD", "register:40f0:8", ["const:bf1068:8", "const:4:8"]]
+ 00bf1068 ["CALL", null, ["callee:00c580a0:8"]]
- 00bf0fcc bytes 019c0194
+ 00bf1068 bytes 0e9c0194
~~~


<a id="compare-654b3b88cdbf4ff8eec093e3def4e2db"></a>

### [`00bf1004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1004.md) → [`00bf10a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf10a0.md) FUN_00bf10a0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf12cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf12cc.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00bf1368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1368.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf10b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1004.md#insn-00bf10b0) · [`00bf10c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1004.md#insn-00bf10c8) · [`00bf10e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1004.md#insn-00bf10e8)
- 新版 `00bf114c`（命令位置の公開資料なし） · `00bf1164`（命令位置の公開資料なし） · `00bf1184`（命令位置の公開資料なし）

~~~diff
- 00bf10b0 ["INT_ADD", "register:40f0:8", ["const:bf10b0:8", "const:4:8"]]
- 00bf10b0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf114c ["INT_ADD", "register:40f0:8", ["const:bf114c:8", "const:4:8"]]
+ 00bf114c ["CALL", null, ["callee:00c57f60:8"]]
- 00bf10b0 bytes 789b0194
+ 00bf114c bytes 859b0194
- 00bf10c8 ["INT_ADD", "register:40f0:8", ["const:bf10c8:8", "const:4:8"]]
- 00bf10c8 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf1164 ["INT_ADD", "register:40f0:8", ["const:bf1164:8", "const:4:8"]]
+ 00bf1164 ["CALL", null, ["callee:00c58010:8"]]
- 00bf10c8 bytes 9e9b0194
+ 00bf1164 bytes ab9b0194
- 00bf10e8 ["INT_ADD", "register:40f0:8", ["const:bf10e8:8", "const:4:8"]]
- 00bf10e8 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf1184 ["INT_ADD", "register:40f0:8", ["const:bf1184:8", "const:4:8"]]
+ 00bf1184 ["CALL", null, ["callee:00c58010:8"]]
- 00bf10e8 bytes 969b0194
+ 00bf1184 bytes a39b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d4c7bf8cb4972f365bf953a0a91a55e"></a>

### [`00bf116c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf116c.md) → [`00bf1208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1208.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEPKcm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf11c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf116c.md#insn-00bf11c8) · [`00bf11e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf116c.md#insn-00bf11e8) · [`00bf1208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf116c.md#insn-00bf1208)
- 新版 `00bf1264`（命令位置の公開資料なし） · `00bf1284`（命令位置の公開資料なし） · `00bf12a4`（命令位置の公開資料なし）

~~~diff
- 00bf11c8 ["INT_ADD", "register:40f0:8", ["const:bf11c8:8", "const:4:8"]]
- 00bf11c8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf1264 ["INT_ADD", "register:40f0:8", ["const:bf1264:8", "const:4:8"]]
+ 00bf1264 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf11c8 bytes 329b0194
+ 00bf1264 bytes 3f9b0194
- 00bf11e8 ["INT_ADD", "register:40f0:8", ["const:bf11e8:8", "const:4:8"]]
- 00bf11e8 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf1284 ["INT_ADD", "register:40f0:8", ["const:bf1284:8", "const:4:8"]]
+ 00bf1284 ["CALL", null, ["callee:00c58010:8"]]
- 00bf11e8 bytes 569b0194
+ 00bf1284 bytes 639b0194
- 00bf1208 ["INT_ADD", "register:40f0:8", ["const:bf1208:8", "const:4:8"]]
- 00bf1208 ["CALL", null, ["callee:0043b7a4:8"]]
+ 00bf12a4 ["INT_ADD", "register:40f0:8", ["const:bf12a4:8", "const:4:8"]]
+ 00bf12a4 ["CALL", null, ["callee:0043b7a4:8"]]
- 00bf1208 bytes 5729e197
+ 00bf12a4 bytes 4029e197
~~~


<a id="compare-8dd88311b87dd9b95d9b57944dd4dd5a"></a>

### [`00bf120c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf120c.md) → [`00bf12a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf12a8.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf124c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf120c.md#insn-00bf124c)
- 新版 `00bf12e8`（命令位置の公開資料なし）

~~~diff
- 00bf124c ["INT_ADD", "register:40f0:8", ["const:bf124c:8", "const:4:8"]]
- 00bf124c ["CALL", null, ["callee:0044295c:8"]]
+ 00bf12e8 ["INT_ADD", "register:40f0:8", ["const:bf12e8:8", "const:4:8"]]
+ 00bf12e8 ["CALL", null, ["callee:0044295c:8"]]
- 00bf124c bytes b445e197
+ 00bf12e8 bytes 9d45e197
~~~


<a id="compare-7e40bb4c9192ad0d048b3e98772e6664"></a>

### [`00bf12cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf12cc.md) → [`00bf1368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1368.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmmc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00bf1004`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1004.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00bf10a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf10a0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1364`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf12cc.md#insn-00bf1364) · [`00bf139c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf12cc.md#insn-00bf139c) · [`00bf13b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf12cc.md#insn-00bf13b0)
- 新版 `00bf1400`（命令位置の公開資料なし） · `00bf1438`（命令位置の公開資料なし） · `00bf144c`（命令位置の公開資料なし）

~~~diff
- 00bf1364 ["INT_ADD", "register:40f0:8", ["const:bf1364:8", "const:4:8"]]
- 00bf1364 ["CALL", null, ["callee:00bf10a0:8"]]
+ 00bf1400 ["INT_ADD", "register:40f0:8", ["const:bf1400:8", "const:4:8"]]
+ 00bf1400 ["CALL", null, ["callee:00bf10a0:8"]]
- 00bf1364 bytes 28ffff97
+ 00bf1400 bytes 28ffff97
- 00bf139c ["INT_ADD", "register:40f0:8", ["const:bf139c:8", "const:4:8"]]
- 00bf139c ["CALL", null, ["callee:00c58010:8"]]
+ 00bf1438 ["INT_ADD", "register:40f0:8", ["const:bf1438:8", "const:4:8"]]
+ 00bf1438 ["CALL", null, ["callee:00c58010:8"]]
- 00bf139c bytes e99a0194
+ 00bf1438 bytes f69a0194
- 00bf13b0 ["INT_ADD", "register:40f0:8", ["const:bf13b0:8", "const:4:8"]]
- 00bf13b0 ["CALL", null, ["callee:00c58160:8"]]
+ 00bf144c ["INT_ADD", "register:40f0:8", ["const:bf144c:8", "const:4:8"]]
+ 00bf144c ["CALL", null, ["callee:00c58160:8"]]
- 00bf13b0 bytes 389b0194
+ 00bf144c bytes 459b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3236c1b881ddc3c5b16448b54747ea87"></a>

### [`00bf1400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md) → [`00bf149c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf149c.md) FUN_00bf149c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf154c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf154c.md) [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 2件 [`00bf15e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf15e8.md) [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf14b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md#insn-00bf14b0) · [`00bf14f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md#insn-00bf14f0) · [`00bf1500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md#insn-00bf1500)
- 新版 `00bf154c`（命令位置の公開資料なし） · `00bf158c`（命令位置の公開資料なし） · `00bf159c`（命令位置の公開資料なし）

~~~diff
- 00bf14b0 ["INT_ADD", "register:40f0:8", ["const:bf14b0:8", "const:4:8"]]
- 00bf14b0 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf154c ["INT_ADD", "register:40f0:8", ["const:bf154c:8", "const:4:8"]]
+ 00bf154c ["CALL", null, ["callee:00c58010:8"]]
- 00bf14b0 bytes a49a0194
+ 00bf154c bytes b19a0194
- 00bf14f0 ["INT_ADD", "register:40f0:8", ["const:bf14f0:8", "const:4:8"]]
- 00bf14f0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf158c ["INT_ADD", "register:40f0:8", ["const:bf158c:8", "const:4:8"]]
+ 00bf158c ["CALL", null, ["callee:00c57f60:8"]]
- 00bf14f0 bytes 689a0194
+ 00bf158c bytes 759a0194
- 00bf1500 ["INT_ADD", "register:40f0:8", ["const:bf1500:8", "const:4:8"]]
- 00bf1500 ["CALL", null, ["callee:00c580d0:8"]]
+ 00bf159c ["INT_ADD", "register:40f0:8", ["const:bf159c:8", "const:4:8"]]
+ 00bf159c ["CALL", null, ["callee:00c580d0:8"]]
- 00bf1500 bytes c09a0194
+ 00bf159c bytes cd9a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48539a05615ce32379aefdd57f22456e"></a>

### [`00bf154c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf154c.md) → [`00bf15e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf15e8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignERKS5_mm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00bf1400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00bf149c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf149c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf154c.md#insn-00bf1598)
- 新版 `00bf1634`（命令位置の公開資料なし）

~~~diff
- 00bf1598 ["INT_ADD", "register:40f0:8", ["const:bf1598:8", "const:4:8"]]
- 00bf1598 ["CALL", null, ["callee:0044295c:8"]]
+ 00bf1634 ["INT_ADD", "register:40f0:8", ["const:bf1634:8", "const:4:8"]]
+ 00bf1634 ["CALL", null, ["callee:0044295c:8"]]
- 00bf1598 bytes e144e197
+ 00bf1634 bytes ca44e197
~~~


<a id="compare-fc7f0322c4097b2878ee7d18e6c9bf45"></a>

### [`00bf159c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf159c.md) → [`00bf1638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1638.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4copyEPcmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf15f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf159c.md#insn-00bf15f0) · [`00bf1608`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf159c.md#insn-00bf1608)
- 新版 `00bf168c`（命令位置の公開資料なし） · `00bf16a4`（命令位置の公開資料なし）

~~~diff
- 00bf15f0 ["INT_ADD", "register:40f0:8", ["const:bf15f0:8", "const:4:8"]]
- 00bf15f0 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf168c ["INT_ADD", "register:40f0:8", ["const:bf168c:8", "const:4:8"]]
+ 00bf168c ["CALL", null, ["callee:00c58010:8"]]
- 00bf15f0 bytes 549a0194
+ 00bf168c bytes 619a0194
- 00bf1608 ["INT_ADD", "register:40f0:8", ["const:bf1608:8", "const:4:8"]]
- 00bf1608 ["CALL", null, ["callee:0044295c:8"]]
+ 00bf16a4 ["INT_ADD", "register:40f0:8", ["const:bf16a4:8", "const:4:8"]]
+ 00bf16a4 ["CALL", null, ["callee:0044295c:8"]]
- 00bf1608 bytes c544e197
+ 00bf16a4 bytes ae44e197
~~~


<a id="compare-42aea976f34e50e427cc2ce2b49e8b2b"></a>

### [`00bf160c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf160c.md) → [`00bf16a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf16a8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1ERKS5_mmRKS4_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1698`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf160c.md#insn-00bf1698) · [`00bf16b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf160c.md#insn-00bf16b8) · [`00bf16dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf160c.md#insn-00bf16dc)
- 新版 `00bf1734`（命令位置の公開資料なし） · `00bf1754`（命令位置の公開資料なし） · `00bf1778`（命令位置の公開資料なし）

~~~diff
- 00bf1698 ["INT_ADD", "register:40f0:8", ["const:bf1698:8", "const:4:8"]]
- 00bf1698 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf1734 ["INT_ADD", "register:40f0:8", ["const:bf1734:8", "const:4:8"]]
+ 00bf1734 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf1698 bytes fe990194
+ 00bf1734 bytes 0b9a0194
- 00bf16b8 ["INT_ADD", "register:40f0:8", ["const:bf16b8:8", "const:4:8"]]
- 00bf16b8 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf1754 ["INT_ADD", "register:40f0:8", ["const:bf1754:8", "const:4:8"]]
+ 00bf1754 ["CALL", null, ["callee:00c58010:8"]]
- 00bf16b8 bytes 229a0194
+ 00bf1754 bytes 2f9a0194
- 00bf16dc ["INT_ADD", "register:40f0:8", ["const:bf16dc:8", "const:4:8"]]
- 00bf16dc ["CALL", null, ["callee:0044295c:8"]]
+ 00bf1778 ["INT_ADD", "register:40f0:8", ["const:bf1778:8", "const:4:8"]]
+ 00bf1778 ["CALL", null, ["callee:0044295c:8"]]
- 00bf16dc bytes 9044e197
+ 00bf1778 bytes 7944e197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c1bfb0e8d1a910a12a5b623f098d3a2"></a>

### [`00bf16e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf16e8.md) → [`00bf1784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1784.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEcm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c585d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c585d0.md) · 呼出先 1件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)
- 新版 呼出元 1件 [`00c586a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586a0.md) · 呼出先 1件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf16e8.md#insn-00bf1730)
- 新版 `00bf17cc`（命令位置の公開資料なし）

~~~diff
- 00bf1730 ["INT_ADD", "register:40f0:8", ["const:bf1730:8", "const:4:8"]]
- 00bf1730 ["CALL", null, ["callee:00c580a0:8"]]
+ 00bf17cc ["INT_ADD", "register:40f0:8", ["const:bf17cc:8", "const:4:8"]]
+ 00bf17cc ["CALL", null, ["callee:00c580a0:8"]]
- 00bf1730 bytes 289a0194
+ 00bf17cc bytes 359a0194
~~~


<a id="compare-87c783bc690e09fe08e98d74147f963f"></a>

### [`00bf1758`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1758.md) → [`00bf17f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf17f4.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6__initEmc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf17b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1758.md#insn-00bf17b4) · [`00bf17d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1758.md#insn-00bf17d4) · [`00bf17f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1758.md#insn-00bf17f4)
- 新版 `00bf1850`（命令位置の公開資料なし） · `00bf1870`（命令位置の公開資料なし） · `00bf1890`（命令位置の公開資料なし）

~~~diff
- 00bf17b4 ["INT_ADD", "register:40f0:8", ["const:bf17b4:8", "const:4:8"]]
- 00bf17b4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf1850 ["INT_ADD", "register:40f0:8", ["const:bf1850:8", "const:4:8"]]
+ 00bf1850 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf17b4 bytes b7990194
+ 00bf1850 bytes c4990194
- 00bf17d4 ["INT_ADD", "register:40f0:8", ["const:bf17d4:8", "const:4:8"]]
- 00bf17d4 ["CALL", null, ["callee:00c58160:8"]]
+ 00bf1870 ["INT_ADD", "register:40f0:8", ["const:bf1870:8", "const:4:8"]]
+ 00bf1870 ["CALL", null, ["callee:00c58160:8"]]
- 00bf17d4 bytes 2f9a0194
+ 00bf1870 bytes 3c9a0194
- 00bf17f4 ["INT_ADD", "register:40f0:8", ["const:bf17f4:8", "const:4:8"]]
- 00bf17f4 ["CALL", null, ["callee:0043b7a4:8"]]
+ 00bf1890 ["INT_ADD", "register:40f0:8", ["const:bf1890:8", "const:4:8"]]
+ 00bf1890 ["CALL", null, ["callee:0043b7a4:8"]]
- 00bf17f4 bytes dc27e197
+ 00bf1890 bytes c527e197
~~~


<a id="compare-04adcda01f832cd33077e11223eee657"></a>

### [`00bf17f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf17f8.md) → [`00bf1894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1894.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) · 呼出先 2件 [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md)
- 新版 呼出元 1件 [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) · 呼出先 2件 [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf181c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf17f8.md#insn-00bf181c)
- 新版 `00bf18b8`（命令位置の公開資料なし）

~~~diff
- 00bf181c ["INT_ADD", "register:40f0:8", ["const:bf181c:8", "const:4:8"]]
- 00bf181c ["CALL", null, ["callee:00c580b0:8"]]
+ 00bf18b8 ["INT_ADD", "register:40f0:8", ["const:bf18b8:8", "const:4:8"]]
+ 00bf18b8 ["CALL", null, ["callee:00c580b0:8"]]
- 00bf181c bytes f1990194
+ 00bf18b8 bytes fe990194
~~~


<a id="compare-7064c80a9d0d9b78501732c851c07a60"></a>

### [`00bf1844`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1844.md) → [`00bf18e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf18e0.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE12find_last_ofEPKcmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf18a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1844.md#insn-00bf18a0)
- 新版 `00bf193c`（命令位置の公開資料なし）

~~~diff
- 00bf18a0 ["INT_ADD", "register:40f0:8", ["const:bf18a0:8", "const:4:8"]]
- 00bf18a0 ["CALL", null, ["callee:00c580a0:8"]]
+ 00bf193c ["INT_ADD", "register:40f0:8", ["const:bf193c:8", "const:4:8"]]
+ 00bf193c ["CALL", null, ["callee:00c580a0:8"]]
- 00bf18a0 bytes cc990194
+ 00bf193c bytes d9990194
~~~


<a id="compare-a6dbebdfd2538fe2a745d4f45eb2d3b6"></a>

### [`00bf18cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf18cc.md) → [`00bf1968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1968.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c58600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58600.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c586d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c586d0.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1998`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf18cc.md#insn-00bf1998) · [`00bf19a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf18cc.md#insn-00bf19a8) · [`00bf19b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf18cc.md#insn-00bf19b8)
- 新版 `00bf1a34`（命令位置の公開資料なし） · `00bf1a44`（命令位置の公開資料なし） · `00bf1a54`（命令位置の公開資料なし）

~~~diff
- 00bf1998 ["INT_ADD", "register:40f0:8", ["const:bf1998:8", "const:4:8"]]
- 00bf1998 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf1a34 ["INT_ADD", "register:40f0:8", ["const:bf1a34:8", "const:4:8"]]
+ 00bf1a34 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf1998 bytes 3e990194
+ 00bf1a34 bytes 4b990194
- 00bf19a8 ["INT_ADD", "register:40f0:8", ["const:bf19a8:8", "const:4:8"]]
- 00bf19a8 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf1a44 ["INT_ADD", "register:40f0:8", ["const:bf1a44:8", "const:4:8"]]
+ 00bf1a44 ["CALL", null, ["callee:00c58010:8"]]
- 00bf19a8 bytes 66990194
+ 00bf1a44 bytes 73990194
- 00bf19b8 ["INT_ADD", "register:40f0:8", ["const:bf19b8:8", "const:4:8"]]
- 00bf19b8 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bf1a54 ["INT_ADD", "register:40f0:8", ["const:bf1a54:8", "const:4:8"]]
+ 00bf1a54 ["CALL", null, ["callee:00c57f80:8"]]
- 00bf19b8 bytes 3e990194
+ 00bf1a54 bytes 4b990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fae1b943a125ccd22ba65d2e074b8ec"></a>

### [`00bf1a50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1a50.md) → [`00bf1aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1aec.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEmc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a6e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a6e0.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md)
- 新版 呼出元 1件 [`00c5a7b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a7b0.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1a50.md#insn-00bf1b2c) · [`00bf1b3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1a50.md#insn-00bf1b3c) · [`00bf1b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1a50.md#insn-00bf1b58)
- 新版 `00bf1bc8`（命令位置の公開資料なし） · `00bf1bd8`（命令位置の公開資料なし） · `00bf1bf4`（命令位置の公開資料なし）

~~~diff
- 00bf1b2c ["INT_ADD", "register:40f0:8", ["const:bf1b2c:8", "const:4:8"]]
- 00bf1b2c ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf1bc8 ["INT_ADD", "register:40f0:8", ["const:bf1bc8:8", "const:4:8"]]
+ 00bf1bc8 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf1b2c bytes d9980194
+ 00bf1bc8 bytes e6980194
- 00bf1b3c ["INT_ADD", "register:40f0:8", ["const:bf1b3c:8", "const:4:8"]]
- 00bf1b3c ["CALL", null, ["callee:00c57f80:8"]]
+ 00bf1bd8 ["INT_ADD", "register:40f0:8", ["const:bf1bd8:8", "const:4:8"]]
+ 00bf1bd8 ["CALL", null, ["callee:00c57f80:8"]]
- 00bf1b3c bytes dd980194
+ 00bf1bd8 bytes ea980194
- 00bf1b58 ["INT_ADD", "register:40f0:8", ["const:bf1b58:8", "const:4:8"]]
- 00bf1b58 ["CALL", null, ["callee:00c58160:8"]]
+ 00bf1bf4 ["INT_ADD", "register:40f0:8", ["const:bf1bf4:8", "const:4:8"]]
+ 00bf1bf4 ["CALL", null, ["callee:00c58160:8"]]
- 00bf1b58 bytes 4e990194
+ 00bf1bf4 bytes 5b990194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b3a287a02e1251e84373d95cab6aa0e"></a>

### [`00bf1b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1b94.md) → [`00bf1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1c30.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c59930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59930.md) · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00bf1c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1c0c.md)
- 新版 呼出元 1件 [`00c59a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a00.md) · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00bf1ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1ca8.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1bcc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1b94.md#insn-00bf1bcc) · [`00bf1c08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1b94.md#insn-00bf1c08)
- 新版 `00bf1c68`（命令位置の公開資料なし） · `00bf1ca4`（命令位置の公開資料なし）

~~~diff
- 00bf1bcc ["INT_ADD", "register:40f0:8", ["const:bf1bcc:8", "const:4:8"]]
- 00bf1bcc ["CALL", null, ["callee:00bf1ca8:8"]]
+ 00bf1c68 ["INT_ADD", "register:40f0:8", ["const:bf1c68:8", "const:4:8"]]
+ 00bf1c68 ["CALL", null, ["callee:00bf1ca8:8"]]
- 00bf1bcc bytes 10000094
+ 00bf1c68 bytes 10000094
- 00bf1c08 ["INT_ADD", "register:40f0:8", ["const:bf1c08:8", "const:4:8"]]
- 00bf1c08 ["CALL", null, ["callee:0044295c:8"]]
+ 00bf1ca4 ["INT_ADD", "register:40f0:8", ["const:bf1ca4:8", "const:4:8"]]
+ 00bf1ca4 ["CALL", null, ["callee:0044295c:8"]]
- 00bf1c08 bytes 4543e197
+ 00bf1ca4 bytes 2e43e197
~~~


<a id="compare-8411672660ba77a8f9daef948da2052b"></a>

### [`00bf1c0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1c0c.md) → [`00bf1ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1ca8.md) FUN_00bf1ca8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf1b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1b94.md) [`00c360b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c360b8.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 2件 [`00bf1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1c30.md) [`00c36154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c36154.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1c0c.md#insn-00bf1c64)
- 新版 `00bf1d00`（命令位置の公開資料なし）

~~~diff
- 00bf1c64 ["INT_ADD", "register:40f0:8", ["const:bf1c64:8", "const:4:8"]]
- 00bf1c64 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf1d00 ["INT_ADD", "register:40f0:8", ["const:bf1d00:8", "const:4:8"]]
+ 00bf1d00 ["CALL", null, ["callee:00c58010:8"]]
- 00bf1c64 bytes b7980194
+ 00bf1d00 bytes c4980194
~~~


<a id="compare-b56a44f452a4b8819932ea49e33ec305"></a>

### [`00bf1ca0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ca0.md) → [`00bf1d3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1d3c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendERKS5_mm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5b0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1d3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ca0.md#insn-00bf1d3c) · [`00bf1d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ca0.md#insn-00bf1d64) · [`00bf1da4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ca0.md#insn-00bf1da4)
- 新版 `00bf1dd8`（命令位置の公開資料なし） · `00bf1e00`（命令位置の公開資料なし） · `00bf1e40`（命令位置の公開資料なし）

~~~diff
- 00bf1d3c ["INT_ADD", "register:40f0:8", ["const:bf1d3c:8", "const:4:8"]]
- 00bf1d3c ["CALL", null, ["callee:00c5b170:8"]]
+ 00bf1dd8 ["INT_ADD", "register:40f0:8", ["const:bf1dd8:8", "const:4:8"]]
+ 00bf1dd8 ["CALL", null, ["callee:00c5b170:8"]]
- 00bf1d3c bytes d9a40194
+ 00bf1dd8 bytes e6a40194
- 00bf1d64 ["INT_ADD", "register:40f0:8", ["const:bf1d64:8", "const:4:8"]]
- 00bf1d64 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf1e00 ["INT_ADD", "register:40f0:8", ["const:bf1e00:8", "const:4:8"]]
+ 00bf1e00 ["CALL", null, ["callee:00c58010:8"]]
- 00bf1d64 bytes 77980194
+ 00bf1e00 bytes 84980194
- 00bf1da4 ["INT_ADD", "register:40f0:8", ["const:bf1da4:8", "const:4:8"]]
- 00bf1da4 ["CALL", null, ["callee:0044295c:8"]]
+ 00bf1e40 ["INT_ADD", "register:40f0:8", ["const:bf1e40:8", "const:4:8"]]
+ 00bf1e40 ["CALL", null, ["callee:0044295c:8"]]
- 00bf1da4 bytes de42e197
+ 00bf1e40 bytes c742e197
~~~


<a id="compare-c41b47cacff941f19de8a0f107405e01"></a>

### [`00bf1da8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1da8.md) → [`00bf1e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1e44.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1dc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1da8.md#insn-00bf1dc4) · [`00bf1e00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1da8.md#insn-00bf1e00) · [`00bf1e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1da8.md#insn-00bf1e20)
- 新版 `00bf1e60`（命令位置の公開資料なし） · `00bf1e9c`（命令位置の公開資料なし） · `00bf1ebc`（命令位置の公開資料なし）

~~~diff
- 00bf1dc4 ["INT_ADD", "register:40f0:8", ["const:bf1dc4:8", "const:4:8"]]
- 00bf1dc4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bf1e60 ["INT_ADD", "register:40f0:8", ["const:bf1e60:8", "const:4:8"]]
+ 00bf1e60 ["CALL", null, ["callee:00c580b0:8"]]
- 00bf1dc4 bytes 87980194
+ 00bf1e60 bytes 94980194
- 00bf1e00 ["INT_ADD", "register:40f0:8", ["const:bf1e00:8", "const:4:8"]]
- 00bf1e00 ["CALL", null, ["callee:00c58120:8"]]
+ 00bf1e9c ["INT_ADD", "register:40f0:8", ["const:bf1e9c:8", "const:4:8"]]
+ 00bf1e9c ["CALL", null, ["callee:00c58120:8"]]
- 00bf1e00 bytes 94980194
+ 00bf1e9c bytes a1980194
- 00bf1e20 ["INT_ADD", "register:40f0:8", ["const:bf1e20:8", "const:4:8"]]
- 00bf1e20 ["CALL", null, ["callee:0044295c:8"]]
+ 00bf1ebc ["INT_ADD", "register:40f0:8", ["const:bf1ebc:8", "const:4:8"]]
+ 00bf1ebc ["CALL", null, ["callee:0044295c:8"]]
- 00bf1e20 bytes bf42e197
+ 00bf1ebc bytes a842e197
~~~


<a id="compare-2a1a3d4183d7b18d95711174a424294d"></a>

### [`00bf1e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1e28.md) → [`00bf1ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1ec4.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKcm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1e28.md#insn-00bf1e88) · [`00bf1ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1e28.md#insn-00bf1ea4)
- 新版 `00bf1f24`（命令位置の公開資料なし） · `00bf1f40`（命令位置の公開資料なし）

~~~diff
- 00bf1e88 ["INT_ADD", "register:40f0:8", ["const:bf1e88:8", "const:4:8"]]
- 00bf1e88 ["CALL", null, ["callee:00c58120:8"]]
+ 00bf1f24 ["INT_ADD", "register:40f0:8", ["const:bf1f24:8", "const:4:8"]]
+ 00bf1f24 ["CALL", null, ["callee:00c58120:8"]]
- 00bf1e88 bytes 72980194
+ 00bf1f24 bytes 7f980194
- 00bf1ea4 ["INT_ADD", "register:40f0:8", ["const:bf1ea4:8", "const:4:8"]]
- 00bf1ea4 ["CALL", null, ["callee:0044295c:8"]]
+ 00bf1f40 ["INT_ADD", "register:40f0:8", ["const:bf1f40:8", "const:4:8"]]
+ 00bf1f40 ["CALL", null, ["callee:0044295c:8"]]
- 00bf1ea4 bytes 9e42e197
+ 00bf1f40 bytes 8742e197
~~~


<a id="compare-a4bd0af4954880b67ae53d0d3a7d0bc3"></a>

### [`00bf1ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ea8.md) → [`00bf1f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1f44.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7compareEmmPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1ed0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ea8.md#insn-00bf1ed0) · [`00bf1f24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ea8.md#insn-00bf1f24) · [`00bf1f48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1ea8.md#insn-00bf1f48)
- 新版 `00bf1f6c`（命令位置の公開資料なし） · `00bf1fc0`（命令位置の公開資料なし） · `00bf1fe4`（命令位置の公開資料なし）

~~~diff
- 00bf1ed0 ["INT_ADD", "register:40f0:8", ["const:bf1ed0:8", "const:4:8"]]
- 00bf1ed0 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bf1f6c ["INT_ADD", "register:40f0:8", ["const:bf1f6c:8", "const:4:8"]]
+ 00bf1f6c ["CALL", null, ["callee:00c580b0:8"]]
- 00bf1ed0 bytes 44980194
+ 00bf1f6c bytes 51980194
- 00bf1f24 ["INT_ADD", "register:40f0:8", ["const:bf1f24:8", "const:4:8"]]
- 00bf1f24 ["CALL", null, ["callee:00c58120:8"]]
+ 00bf1fc0 ["INT_ADD", "register:40f0:8", ["const:bf1fc0:8", "const:4:8"]]
+ 00bf1fc0 ["CALL", null, ["callee:00c58120:8"]]
- 00bf1f24 bytes 4b980194
+ 00bf1fc0 bytes 58980194
- 00bf1f48 ["INT_ADD", "register:40f0:8", ["const:bf1f48:8", "const:4:8"]]
- 00bf1f48 ["CALL", null, ["callee:0044295c:8"]]
+ 00bf1fe4 ["INT_ADD", "register:40f0:8", ["const:bf1fe4:8", "const:4:8"]]
+ 00bf1fe4 ["CALL", null, ["callee:0044295c:8"]]
- 00bf1f48 bytes 7542e197
+ 00bf1fe4 bytes 5e42e197
~~~


<a id="compare-24e035bcdd2d341add7afbc35579aaa7"></a>

### [`00bf1f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f4c.md) → [`00bf1fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf1fe8.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f4c.md#insn-00bf1f8c)
- 新版 `00bf2028`（命令位置の公開資料なし）

~~~diff
- 00bf1f8c ["INT_ADD", "register:40f0:8", ["const:bf1f8c:8", "const:4:8"]]
- 00bf1f8c ["CALL", null, ["callee:0044295c:8"]]
+ 00bf2028 ["INT_ADD", "register:40f0:8", ["const:bf2028:8", "const:4:8"]]
+ 00bf2028 ["CALL", null, ["callee:0044295c:8"]]
- 00bf1f8c bytes 6442e197
+ 00bf2028 bytes 4d42e197
~~~


<a id="compare-46f0eb568b56f4c4e8860399fb46c144"></a>

### [`00bf1f98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md) → [`00bf2034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2034.md) FUN_00bf2034

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 8件 [`00bf1f90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f90.md) [`00c2c228`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c228.md) [`00c2c624`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2c624.md) [`00c30a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c30/00c30a70.md) [`00c32a84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c32/00c32a84.md) · 呼出先 2件 [`00bf1400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1400.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md)
- 新版 呼出元 8件 [`00bf202c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf202c.md) [`00c2c2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c2c4.md) [`00c2c6c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2c/00c2c6c0.md) [`00c30b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c30/00c30b0c.md) [`00c32b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c32/00c32b20.md) · 呼出先 2件 [`00bf149c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf1/00bf149c.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf1fb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1f98.md#insn-00bf1fb4)
- 新版 `00bf2050`（命令位置の公開資料なし）

~~~diff
- 00bf1fb4 ["INT_ADD", "register:40f0:8", ["const:bf1fb4:8", "const:4:8"]]
- 00bf1fb4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bf2050 ["INT_ADD", "register:40f0:8", ["const:bf2050:8", "const:4:8"]]
+ 00bf2050 ["CALL", null, ["callee:00c580b0:8"]]
- 00bf1fb4 bytes 0b980194
+ 00bf2050 bytes 18980194
~~~


<a id="compare-320ba61c1b3485a3f2b07ac33c673583"></a>

### [`00bf1fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1fd4.md) → [`00bf2070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2070.md) _ZNKSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findEPKcmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fd0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c580a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580a0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2074`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1fd4.md#insn-00bf2074) · [`00bf2088`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1fd4.md#insn-00bf2088)
- 新版 `00bf2110`（命令位置の公開資料なし） · `00bf2124`（命令位置の公開資料なし）

~~~diff
- 00bf2074 ["INT_ADD", "register:40f0:8", ["const:bf2074:8", "const:4:8"]]
- 00bf2074 ["CALL", null, ["callee:00c580a0:8"]]
+ 00bf2110 ["INT_ADD", "register:40f0:8", ["const:bf2110:8", "const:4:8"]]
+ 00bf2110 ["CALL", null, ["callee:00c580a0:8"]]
- 00bf2074 bytes d7970194
+ 00bf2110 bytes e4970194
- 00bf2088 ["INT_ADD", "register:40f0:8", ["const:bf2088:8", "const:4:8"]]
- 00bf2088 ["CALL", null, ["callee:00c58120:8"]]
+ 00bf2124 ["INT_ADD", "register:40f0:8", ["const:bf2124:8", "const:4:8"]]
+ 00bf2124 ["CALL", null, ["callee:00c58120:8"]]
- 00bf2088 bytes f2970194
+ 00bf2124 bytes ff970194
~~~


<a id="compare-62726ee039e49168f41c16277be65ef2"></a>

### [`00bf21a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf21a8.md) → [`00bf2244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2244.md) FUN_00bf2244

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf2154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2154.md) [`00c05180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05180.md) · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 2件 [`00bf21f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf21f0.md) [`00c0521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0521c.md) · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf21e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf21a8.md#insn-00bf21e8) · [`00bf2214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf21a8.md#insn-00bf2214) · [`00bf2224`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf21a8.md#insn-00bf2224)
- 新版 `00bf2284`（命令位置の公開資料なし） · `00bf22b0`（命令位置の公開資料なし） · `00bf22c0`（命令位置の公開資料なし）

~~~diff
- 00bf21e8 ["INT_ADD", "register:40f0:8", ["const:bf21e8:8", "const:4:8"]]
- 00bf21e8 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf2284 ["INT_ADD", "register:40f0:8", ["const:bf2284:8", "const:4:8"]]
+ 00bf2284 ["CALL", null, ["callee:00c58010:8"]]
- 00bf21e8 bytes 56970194
+ 00bf2284 bytes 63970194
- 00bf2214 ["INT_ADD", "register:40f0:8", ["const:bf2214:8", "const:4:8"]]
- 00bf2214 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf22b0 ["INT_ADD", "register:40f0:8", ["const:bf22b0:8", "const:4:8"]]
+ 00bf22b0 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf2214 bytes 1f970194
+ 00bf22b0 bytes 2c970194
- 00bf2224 ["INT_ADD", "register:40f0:8", ["const:bf2224:8", "const:4:8"]]
- 00bf2224 ["CALL", null, ["callee:00c580d0:8"]]
+ 00bf22c0 ["INT_ADD", "register:40f0:8", ["const:bf22c0:8", "const:4:8"]]
+ 00bf22c0 ["CALL", null, ["callee:00c580d0:8"]]
- 00bf2224 bytes 77970194
+ 00bf22c0 bytes 84970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05b21a2904b1bf6392b8ae17f660aac6"></a>

### [`00bf225c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf225c.md) → [`00bf22f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf22f8.md) FUN_00bf22f8

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf2154`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2154.md) [`00c05180`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c05/00c05180.md) · 呼出先 5件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 2件 [`00bf21f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf21f0.md) [`00c0521c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c05/00c0521c.md) · 呼出先 5件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf22a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf225c.md#insn-00bf22a0) · [`00bf2328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf225c.md#insn-00bf2328) · [`00bf2340`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf225c.md#insn-00bf2340)
- 新版 `00bf233c`（命令位置の公開資料なし） · `00bf23c4`（命令位置の公開資料なし） · `00bf23dc`（命令位置の公開資料なし）

~~~diff
- 00bf22a0 ["INT_ADD", "register:40f0:8", ["const:bf22a0:8", "const:4:8"]]
- 00bf22a0 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf233c ["INT_ADD", "register:40f0:8", ["const:bf233c:8", "const:4:8"]]
+ 00bf233c ["CALL", null, ["callee:00c58010:8"]]
- 00bf22a0 bytes 28970194
+ 00bf233c bytes 35970194
- 00bf2328 ["INT_ADD", "register:40f0:8", ["const:bf2328:8", "const:4:8"]]
- 00bf2328 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf23c4 ["INT_ADD", "register:40f0:8", ["const:bf23c4:8", "const:4:8"]]
+ 00bf23c4 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf2328 bytes da960194
+ 00bf23c4 bytes e7960194
- 00bf2340 ["INT_ADD", "register:40f0:8", ["const:bf2340:8", "const:4:8"]]
- 00bf2340 ["CALL", null, ["callee:00c580d0:8"]]
+ 00bf23dc ["INT_ADD", "register:40f0:8", ["const:bf23dc:8", "const:4:8"]]
+ 00bf23dc ["CALL", null, ["callee:00c580d0:8"]]
- 00bf2340 bytes 30970194
+ 00bf23dc bytes 3d970194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1da9c0f462e8a47ad6357773fb2533e"></a>

### [`00bf2380`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2380.md) → [`00bf241c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf241c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) · 呼出先 3件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c57fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c5b0a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b0a0.md)
- 新版 呼出元 1件 [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) · 呼出先 3件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c5b170`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b170.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf23a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2380.md#insn-00bf23a4) · [`00bf2400`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2380.md#insn-00bf2400) · [`00bf2424`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2380.md#insn-00bf2424)
- 新版 `00bf2440`（命令位置の公開資料なし） · `00bf249c`（命令位置の公開資料なし） · `00bf24c0`（命令位置の公開資料なし）

~~~diff
- 00bf23a4 ["INT_ADD", "register:40f0:8", ["const:bf23a4:8", "const:4:8"]]
- 00bf23a4 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bf2440 ["INT_ADD", "register:40f0:8", ["const:bf2440:8", "const:4:8"]]
+ 00bf2440 ["CALL", null, ["callee:00c580b0:8"]]
- 00bf23a4 bytes 0f970194
+ 00bf2440 bytes 1c970194
- 00bf2400 ["INT_ADD", "register:40f0:8", ["const:bf2400:8", "const:4:8"]]
- 00bf2400 ["CALL", null, ["callee:00c5b170:8"]]
+ 00bf249c ["INT_ADD", "register:40f0:8", ["const:bf249c:8", "const:4:8"]]
+ 00bf249c ["CALL", null, ["callee:00c5b170:8"]]
- 00bf2400 bytes 28a30194
+ 00bf249c bytes 35a30194
- 00bf2424 ["INT_ADD", "register:40f0:8", ["const:bf2424:8", "const:4:8"]]
- 00bf2424 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf24c0 ["INT_ADD", "register:40f0:8", ["const:bf24c0:8", "const:4:8"]]
+ 00bf24c0 ["CALL", null, ["callee:00c58010:8"]]
- 00bf2424 bytes c7960194
+ 00bf24c0 bytes d4960194
~~~


<a id="compare-16cf1b53406559b3fcff11a51ed4ce7b"></a>

### [`00bf2464`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2464.md) → [`00bf2500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2500.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c58070`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58070.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c58140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58140.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf24b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2464.md#insn-00bf24b0)
- 新版 `00bf254c`（命令位置の公開資料なし）

~~~diff
- 00bf24b0 ["INT_ADD", "register:40f0:8", ["const:bf24b0:8", "const:4:8"]]
- 00bf24b0 ["CALL", null, ["callee:0044295c:8"]]
+ 00bf254c ["INT_ADD", "register:40f0:8", ["const:bf254c:8", "const:4:8"]]
+ 00bf254c ["CALL", null, ["callee:0044295c:8"]]
- 00bf24b0 bytes 1b41e197
+ 00bf254c bytes 0441e197
~~~


<a id="compare-ccc91963e755205b84b87cbcf656add3"></a>

### [`00bf24b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf24b4.md) → [`00bf2550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2550.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertENS_11__wrap_iterIPKcEEc

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2578`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf24b4.md#insn-00bf2578) · [`00bf25a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf24b4.md#insn-00bf25a4) · [`00bf25c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf24b4.md#insn-00bf25c4)
- 新版 `00bf2614`（命令位置の公開資料なし） · `00bf2640`（命令位置の公開資料なし） · `00bf2660`（命令位置の公開資料なし）

~~~diff
- 00bf2578 ["INT_ADD", "register:40f0:8", ["const:bf2578:8", "const:4:8"]]
- 00bf2578 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf2614 ["INT_ADD", "register:40f0:8", ["const:bf2614:8", "const:4:8"]]
+ 00bf2614 ["CALL", null, ["callee:00c58010:8"]]
- 00bf2578 bytes 72960194
+ 00bf2614 bytes 7f960194
- 00bf25a4 ["INT_ADD", "register:40f0:8", ["const:bf25a4:8", "const:4:8"]]
- 00bf25a4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf2640 ["INT_ADD", "register:40f0:8", ["const:bf2640:8", "const:4:8"]]
+ 00bf2640 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf25a4 bytes 3b960194
+ 00bf2640 bytes 48960194
- 00bf25c4 ["INT_ADD", "register:40f0:8", ["const:bf25c4:8", "const:4:8"]]
- 00bf25c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bf2660 ["INT_ADD", "register:40f0:8", ["const:bf2660:8", "const:4:8"]]
+ 00bf2660 ["CALL", null, ["callee:00c57f80:8"]]
- 00bf25c4 bytes 3b960194
+ 00bf2660 bytes 48960194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6267abf572d2a3ad0754017e0703ab9"></a>

### [`00bf26b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf26b0.md) → [`00bf274c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf274c.md) _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmRKS5_mm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044291c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/0044291c.md) [`00c58fd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58fd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c590a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf26fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf26b0.md#insn-00bf26fc)
- 新版 `00bf2798`（命令位置の公開資料なし）

~~~diff
- 00bf26fc ["INT_ADD", "register:40f0:8", ["const:bf26fc:8", "const:4:8"]]
- 00bf26fc ["CALL", null, ["callee:0044295c:8"]]
+ 00bf2798 ["INT_ADD", "register:40f0:8", ["const:bf2798:8", "const:4:8"]]
+ 00bf2798 ["CALL", null, ["callee:0044295c:8"]]
- 00bf26fc bytes 8840e197
+ 00bf2798 bytes 7140e197
~~~


<a id="compare-66a299b8ce3978fb370389d5c0c42968"></a>

### [`00bf2700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2700.md) → [`00bf279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf279c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmPKwm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfe0.md) · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)
- 新版 呼出元 1件 [`00c5e0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0b0.md) · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf27a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2700.md#insn-00bf27a0) · [`00bf27f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2700.md#insn-00bf27f0) · [`00bf2800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2700.md#insn-00bf2800)
- 新版 `00bf283c`（命令位置の公開資料なし） · `00bf288c`（命令位置の公開資料なし） · `00bf289c`（命令位置の公開資料なし）

~~~diff
- 00bf27a0 ["INT_ADD", "register:40f0:8", ["const:bf27a0:8", "const:4:8"]]
- 00bf27a0 ["CALL", null, ["callee:00c5e0c0:8"]]
+ 00bf283c ["INT_ADD", "register:40f0:8", ["const:bf283c:8", "const:4:8"]]
+ 00bf283c ["CALL", null, ["callee:00c5e0c0:8"]]
- 00bf27a0 bytes 14ae0194
+ 00bf283c bytes 21ae0194
- 00bf27f0 ["INT_ADD", "register:40f0:8", ["const:bf27f0:8", "const:4:8"]]
- 00bf27f0 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf288c ["INT_ADD", "register:40f0:8", ["const:bf288c:8", "const:4:8"]]
+ 00bf288c ["CALL", null, ["callee:00c58010:8"]]
- 00bf27f0 bytes d4950194
+ 00bf288c bytes e1950194
- 00bf2800 ["INT_ADD", "register:40f0:8", ["const:bf2800:8", "const:4:8"]]
- 00bf2800 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf289c ["INT_ADD", "register:40f0:8", ["const:bf289c:8", "const:4:8"]]
+ 00bf289c ["CALL", null, ["callee:00c58010:8"]]
- 00bf2800 bytes d0950194
+ 00bf289c bytes dd950194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6934cc32550e589b08dad2a944b034b"></a>

### [`00bf28f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28f0.md) → [`00bf298c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf298c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE21__grow_by_and_replaceEmmmmmmPKw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md) · 呼出先 6件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf29bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28f0.md#insn-00bf29bc) · [`00bf29d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28f0.md#insn-00bf29d8) · [`00bf29ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28f0.md#insn-00bf29ec)
- 新版 `00bf2a58`（命令位置の公開資料なし） · `00bf2a74`（命令位置の公開資料なし） · `00bf2a88`（命令位置の公開資料なし）

~~~diff
- 00bf29bc ["INT_ADD", "register:40f0:8", ["const:bf29bc:8", "const:4:8"]]
- 00bf29bc ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf2a58 ["INT_ADD", "register:40f0:8", ["const:bf2a58:8", "const:4:8"]]
+ 00bf2a58 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf29bc bytes 35950194
+ 00bf2a58 bytes 42950194
- 00bf29d8 ["INT_ADD", "register:40f0:8", ["const:bf29d8:8", "const:4:8"]]
- 00bf29d8 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf2a74 ["INT_ADD", "register:40f0:8", ["const:bf2a74:8", "const:4:8"]]
+ 00bf2a74 ["CALL", null, ["callee:00c58010:8"]]
- 00bf29d8 bytes 5a950194
+ 00bf2a74 bytes 67950194
- 00bf29ec ["INT_ADD", "register:40f0:8", ["const:bf29ec:8", "const:4:8"]]
- 00bf29ec ["CALL", null, ["callee:00c580d0:8"]]
+ 00bf2a88 ["INT_ADD", "register:40f0:8", ["const:bf2a88:8", "const:4:8"]]
+ 00bf2a88 ["CALL", null, ["callee:00c580d0:8"]]
- 00bf29ec bytes 85950194
+ 00bf2a88 bytes 92950194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4619ce2cb4e8193db9232a8ee3ce144f"></a>

### [`00bf2b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2b34.md) → [`00bf2bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2bd0.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEPKwmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2b78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2b34.md#insn-00bf2b78) · [`00bf2bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2b34.md#insn-00bf2bc0) · [`00bf2be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2b34.md#insn-00bf2be4)
- 新版 `00bf2c14`（命令位置の公開資料なし） · `00bf2c5c`（命令位置の公開資料なし） · `00bf2c80`（命令位置の公開資料なし）

~~~diff
- 00bf2b78 ["INT_ADD", "register:40f0:8", ["const:bf2b78:8", "const:4:8"]]
- 00bf2b78 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf2c14 ["INT_ADD", "register:40f0:8", ["const:bf2c14:8", "const:4:8"]]
+ 00bf2c14 ["CALL", null, ["callee:00c58010:8"]]
- 00bf2b78 bytes f2940194
+ 00bf2c14 bytes ff940194
- 00bf2bc0 ["INT_ADD", "register:40f0:8", ["const:bf2bc0:8", "const:4:8"]]
- 00bf2bc0 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf2c5c ["INT_ADD", "register:40f0:8", ["const:bf2c5c:8", "const:4:8"]]
+ 00bf2c5c ["CALL", null, ["callee:00c57f60:8"]]
- 00bf2bc0 bytes b4940194
+ 00bf2c5c bytes c1940194
- 00bf2be4 ["INT_ADD", "register:40f0:8", ["const:bf2be4:8", "const:4:8"]]
- 00bf2be4 ["CALL", null, ["callee:006d76f8:8"]]
+ 00bf2c80 ["INT_ADD", "register:40f0:8", ["const:bf2c80:8", "const:4:8"]]
+ 00bf2c80 ["CALL", null, ["callee:006d76f8:8"]]
- 00bf2be4 bytes af92eb97
+ 00bf2c80 bytes 9e92eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ea47cd52362d05b6995ceff184c008e"></a>

### [`00bf2c18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2c18.md) → [`00bf2cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2cb4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmPKw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5dfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfe0.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0b0.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2c18.md#insn-00bf2c40)
- 新版 `00bf2cdc`（命令位置の公開資料なし）

~~~diff
- 00bf2c40 ["INT_ADD", "register:40f0:8", ["const:bf2c40:8", "const:4:8"]]
- 00bf2c40 ["CALL", null, ["callee:00c5e0d0:8"]]
+ 00bf2cdc ["INT_ADD", "register:40f0:8", ["const:bf2cdc:8", "const:4:8"]]
+ 00bf2cdc ["CALL", null, ["callee:00c5e0d0:8"]]
- 00bf2c40 bytes f0ac0194
+ 00bf2cdc bytes fdac0194
~~~


<a id="compare-0bb04daa9878c1d14f35e96d1243257b"></a>

### [`00bf2c98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2c98.md) → [`00bf2d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2d34.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE16find_last_not_ofEPKwmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2c98.md#insn-00bf2cfc)
- 新版 `00bf2d98`（命令位置の公開資料なし）

~~~diff
- 00bf2cfc ["INT_ADD", "register:40f0:8", ["const:bf2cfc:8", "const:4:8"]]
- 00bf2cfc ["CALL", null, ["callee:00c58520:8"]]
+ 00bf2d98 ["INT_ADD", "register:40f0:8", ["const:bf2d98:8", "const:4:8"]]
+ 00bf2d98 ["CALL", null, ["callee:00c58520:8"]]
- 00bf2cfc bytes d5950194
+ 00bf2d98 bytes e2950194
~~~


<a id="compare-75e17246050cbef281a222ecca341f0f"></a>

### [`00bf2d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d40.md) → [`00bf2ddc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2ddc.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2da0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d40.md#insn-00bf2da0)
- 新版 `00bf2e3c`（命令位置の公開資料なし）

~~~diff
- 00bf2da0 ["INT_ADD", "register:40f0:8", ["const:bf2da0:8", "const:4:8"]]
- 00bf2da0 ["CALL", null, ["callee:00c58520:8"]]
+ 00bf2e3c ["INT_ADD", "register:40f0:8", ["const:bf2e3c:8", "const:4:8"]]
+ 00bf2e3c ["CALL", null, ["callee:00c58520:8"]]
- 00bf2da0 bytes ac950194
+ 00bf2e3c bytes b9950194
~~~


<a id="compare-edfd897adbfc7e188d4c1f1c3c55819c"></a>

### [`00bf2ddc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2ddc.md) → [`00bf2e78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2e78.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmmw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e010.md) · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 1件 [`00c5e0e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0e0.md) · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2e60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2ddc.md#insn-00bf2e60) · [`00bf2ea0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2ddc.md#insn-00bf2ea0) · [`00bf2f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2ddc.md#insn-00bf2f30)
- 新版 `00bf2efc`（命令位置の公開資料なし） · `00bf2f3c`（命令位置の公開資料なし） · `00bf2fcc`（命令位置の公開資料なし）

~~~diff
- 00bf2e60 ["INT_ADD", "register:40f0:8", ["const:bf2e60:8", "const:4:8"]]
- 00bf2e60 ["CALL", null, ["callee:00c5a970:8"]]
+ 00bf2efc ["INT_ADD", "register:40f0:8", ["const:bf2efc:8", "const:4:8"]]
+ 00bf2efc ["CALL", null, ["callee:00c5a970:8"]]
- 00bf2e60 bytes 909e0194
+ 00bf2efc bytes 9d9e0194
- 00bf2ea0 ["INT_ADD", "register:40f0:8", ["const:bf2ea0:8", "const:4:8"]]
- 00bf2ea0 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf2f3c ["INT_ADD", "register:40f0:8", ["const:bf2f3c:8", "const:4:8"]]
+ 00bf2f3c ["CALL", null, ["callee:00c58010:8"]]
- 00bf2ea0 bytes 28940194
+ 00bf2f3c bytes 35940194
- 00bf2f30 ["INT_ADD", "register:40f0:8", ["const:bf2f30:8", "const:4:8"]]
- 00bf2f30 ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf2fcc ["INT_ADD", "register:40f0:8", ["const:bf2fcc:8", "const:4:8"]]
+ 00bf2fcc ["CALL", null, ["callee:00bf2974:8"]]
- 00bf2f30 bytes 6afeff97
+ 00bf2fcc bytes 6afeff97
~~~


<a id="compare-3f19e349dfeaa8b6f68f5ab7abddf633"></a>

### [`00bf2f68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2f68.md) → [`00bf3004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3004.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEPKwm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf2fd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2f68.md#insn-00bf2fd4) · [`00bf2ff4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2f68.md#insn-00bf2ff4) · [`00bf3014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2f68.md#insn-00bf3014)
- 新版 `00bf3070`（命令位置の公開資料なし） · `00bf3090`（命令位置の公開資料なし） · `00bf30b0`（命令位置の公開資料なし）

~~~diff
- 00bf2fd4 ["INT_ADD", "register:40f0:8", ["const:bf2fd4:8", "const:4:8"]]
- 00bf2fd4 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf3070 ["INT_ADD", "register:40f0:8", ["const:bf3070:8", "const:4:8"]]
+ 00bf3070 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf2fd4 bytes af930194
+ 00bf3070 bytes bc930194
- 00bf2ff4 ["INT_ADD", "register:40f0:8", ["const:bf2ff4:8", "const:4:8"]]
- 00bf2ff4 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf3090 ["INT_ADD", "register:40f0:8", ["const:bf3090:8", "const:4:8"]]
+ 00bf3090 ["CALL", null, ["callee:00c58010:8"]]
- 00bf2ff4 bytes d3930194
+ 00bf3090 bytes e0930194
- 00bf3014 ["INT_ADD", "register:40f0:8", ["const:bf3014:8", "const:4:8"]]
- 00bf3014 ["CALL", null, ["callee:006d76f8:8"]]
+ 00bf30b0 ["INT_ADD", "register:40f0:8", ["const:bf30b0:8", "const:4:8"]]
+ 00bf30b0 ["CALL", null, ["callee:006d76f8:8"]]
- 00bf3014 bytes a391eb97
+ 00bf30b0 bytes 9291eb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85024da8d79d93a39289e7fd76c133e9"></a>

### [`00bf301c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf301c.md) → [`00bf30b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf30b8.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf301c.md#insn-00bf3060)
- 新版 `00bf30fc`（命令位置の公開資料なし）

~~~diff
- 00bf3060 ["INT_ADD", "register:40f0:8", ["const:bf3060:8", "const:4:8"]]
- 00bf3060 ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf30fc ["INT_ADD", "register:40f0:8", ["const:bf30fc:8", "const:4:8"]]
+ 00bf30fc ["CALL", null, ["callee:00bf2974:8"]]
- 00bf3060 bytes 1efeff97
+ 00bf30fc bytes 1efeff97
~~~


<a id="compare-2be47a5f69a0598de3d20b14032f6dbf"></a>

### [`00bf3064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3064.md) → [`00bf3100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3100.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKwm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e020.md) · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)
- 新版 呼出元 1件 [`00c5e0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0f0.md) · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf30e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3064.md#insn-00bf30e8) · [`00bf3130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3064.md#insn-00bf3130) · [`00bf3140`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3064.md#insn-00bf3140)
- 新版 `00bf3184`（命令位置の公開資料なし） · `00bf31cc`（命令位置の公開資料なし） · `00bf31dc`（命令位置の公開資料なし）

~~~diff
- 00bf30e8 ["INT_ADD", "register:40f0:8", ["const:bf30e8:8", "const:4:8"]]
- 00bf30e8 ["CALL", null, ["callee:00c5e0c0:8"]]
+ 00bf3184 ["INT_ADD", "register:40f0:8", ["const:bf3184:8", "const:4:8"]]
+ 00bf3184 ["CALL", null, ["callee:00c5e0c0:8"]]
- 00bf30e8 bytes c2ab0194
+ 00bf3184 bytes cfab0194
- 00bf3130 ["INT_ADD", "register:40f0:8", ["const:bf3130:8", "const:4:8"]]
- 00bf3130 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf31cc ["INT_ADD", "register:40f0:8", ["const:bf31cc:8", "const:4:8"]]
+ 00bf31cc ["CALL", null, ["callee:00c58010:8"]]
- 00bf3130 bytes 84930194
+ 00bf31cc bytes 91930194
- 00bf3140 ["INT_ADD", "register:40f0:8", ["const:bf3140:8", "const:4:8"]]
- 00bf3140 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf31dc ["INT_ADD", "register:40f0:8", ["const:bf31dc:8", "const:4:8"]]
+ 00bf31dc ["CALL", null, ["callee:00c58010:8"]]
- 00bf3140 bytes 80930194
+ 00bf31dc bytes 8d930194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c2a9f58ebf9080bf46c45a31567e39d"></a>

### [`00bf3210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3210.md) → [`00bf32ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf32ac.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmmw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf32a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3210.md#insn-00bf32a4) · [`00bf32f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3210.md#insn-00bf32f8) · [`00bf3394`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3210.md#insn-00bf3394)
- 新版 `00bf3340`（命令位置の公開資料なし） · `00bf3394`（命令位置の公開資料なし） · `00bf3430`（命令位置の公開資料なし）

~~~diff
- 00bf32a4 ["INT_ADD", "register:40f0:8", ["const:bf32a4:8", "const:4:8"]]
- 00bf32a4 ["CALL", null, ["callee:00c5a970:8"]]
+ 00bf3340 ["INT_ADD", "register:40f0:8", ["const:bf3340:8", "const:4:8"]]
+ 00bf3340 ["CALL", null, ["callee:00c5a970:8"]]
- 00bf32a4 bytes 7f9d0194
+ 00bf3340 bytes 8c9d0194
- 00bf32f8 ["INT_ADD", "register:40f0:8", ["const:bf32f8:8", "const:4:8"]]
- 00bf32f8 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf3394 ["INT_ADD", "register:40f0:8", ["const:bf3394:8", "const:4:8"]]
+ 00bf3394 ["CALL", null, ["callee:00c58010:8"]]
- 00bf32f8 bytes 12930194
+ 00bf3394 bytes 1f930194
- 00bf3394 ["INT_ADD", "register:40f0:8", ["const:bf3394:8", "const:4:8"]]
- 00bf3394 ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf3430 ["INT_ADD", "register:40f0:8", ["const:bf3430:8", "const:4:8"]]
+ 00bf3430 ["CALL", null, ["callee:00bf2974:8"]]
- 00bf3394 bytes 51fdff97
+ 00bf3430 bytes 51fdff97
~~~


<a id="compare-6d3f78dfac105bbb1cdf8787b447d138"></a>

### [`00bf33a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md) → [`00bf343c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf343c.md) FUN_00bf343c

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 5件 [`00bf3398`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3398.md) [`00bf3720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3720.md) [`00bf43f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43f4.md) [`00c2cf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2c/00c2cf94.md) [`00c2da28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c2d/00c2da28.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)
- 新版 呼出元 5件 [`00bf3434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3434.md) [`00bf37bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf37bc.md) [`00bf4490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4490.md) [`00c2d030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2d030.md) [`00c2dac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c2d/00c2dac4.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3408`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md#insn-00bf3408) · [`00bf3430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md#insn-00bf3430)
- 新版 `00bf34a4`（命令位置の公開資料なし） · `00bf34cc`（命令位置の公開資料なし）

~~~diff
- 00bf3408 ["INT_ADD", "register:40f0:8", ["const:bf3408:8", "const:4:8"]]
- 00bf3408 ["CALL", null, ["callee:00c5e0c0:8"]]
+ 00bf34a4 ["INT_ADD", "register:40f0:8", ["const:bf34a4:8", "const:4:8"]]
+ 00bf34a4 ["CALL", null, ["callee:00c5e0c0:8"]]
- 00bf3408 bytes faaa0194
+ 00bf34a4 bytes 07ab0194
- 00bf3430 ["INT_ADD", "register:40f0:8", ["const:bf3430:8", "const:4:8"]]
- 00bf3430 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf34cc ["INT_ADD", "register:40f0:8", ["const:bf34cc:8", "const:4:8"]]
+ 00bf34cc ["CALL", null, ["callee:00c58010:8"]]
- 00bf3430 bytes c4920194
+ 00bf34cc bytes d1920194
~~~


<a id="compare-892dfb7c77ad45fbf04c68b3b274d194"></a>

### [`00bf3468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3468.md) → [`00bf3504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3504.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7reserveEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00bf3504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3504.md)
- 新版 呼出元 0件  · 呼出先 2件 [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00bf35a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf35a0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3468.md#insn-00bf3500)
- 新版 `00bf359c`（命令位置の公開資料なし）

~~~diff
- 00bf3500 ["INT_ADD", "register:40f0:8", ["const:bf3500:8", "const:4:8"]]
- 00bf3500 ["CALL", null, ["callee:006d76f8:8"]]
+ 00bf359c ["INT_ADD", "register:40f0:8", ["const:bf359c:8", "const:4:8"]]
+ 00bf359c ["CALL", null, ["callee:006d76f8:8"]]
- 00bf3500 bytes 6890eb97
+ 00bf359c bytes 5790eb97
~~~


<a id="compare-96f0ac7c3b53557326dcb576262f3473"></a>

### [`00bf3504`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3504.md) → [`00bf35a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf35a0.md) FUN_00bf35a0

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf3468`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3468.md) · 呼出先 4件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00bf3504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3504.md) · 呼出先 4件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3574`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3504.md#insn-00bf3574) · [`00bf35a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3504.md#insn-00bf35a0) · [`00bf35c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3504.md#insn-00bf35c4)
- 新版 `00bf3610`（命令位置の公開資料なし） · `00bf363c`（命令位置の公開資料なし） · `00bf3660`（命令位置の公開資料なし）

~~~diff
- 00bf3574 ["INT_ADD", "register:40f0:8", ["const:bf3574:8", "const:4:8"]]
- 00bf3574 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf3610 ["INT_ADD", "register:40f0:8", ["const:bf3610:8", "const:4:8"]]
+ 00bf3610 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf3574 bytes 47920194
+ 00bf3610 bytes 54920194
- 00bf35a0 ["INT_ADD", "register:40f0:8", ["const:bf35a0:8", "const:4:8"]]
- 00bf35a0 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf363c ["INT_ADD", "register:40f0:8", ["const:bf363c:8", "const:4:8"]]
+ 00bf363c ["CALL", null, ["callee:00c58010:8"]]
- 00bf35a0 bytes 68920194
+ 00bf363c bytes 75920194
- 00bf35c4 ["INT_ADD", "register:40f0:8", ["const:bf35c4:8", "const:4:8"]]
- 00bf35c4 ["CALL", null, ["callee:00c57f80:8"]]
+ 00bf3660 ["INT_ADD", "register:40f0:8", ["const:bf3660:8", "const:4:8"]]
+ 00bf3660 ["CALL", null, ["callee:00c57f80:8"]]
- 00bf35c4 bytes 3b920194
+ 00bf3660 bytes 48920194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-636888f0ed12aa95789c8d55f004c3ed"></a>

### [`00bf3648`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3648.md) → [`00bf36e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf36e4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEPKwm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a8b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8b0.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)
- 新版 呼出元 1件 [`00c5a980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a980.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf36bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3648.md#insn-00bf36bc) · [`00bf36e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3648.md#insn-00bf36e4)
- 新版 `00bf3758`（命令位置の公開資料なし） · `00bf3780`（命令位置の公開資料なし）

~~~diff
- 00bf36bc ["INT_ADD", "register:40f0:8", ["const:bf36bc:8", "const:4:8"]]
- 00bf36bc ["CALL", null, ["callee:00c5e0c0:8"]]
+ 00bf3758 ["INT_ADD", "register:40f0:8", ["const:bf3758:8", "const:4:8"]]
+ 00bf3758 ["CALL", null, ["callee:00c5e0c0:8"]]
- 00bf36bc bytes 4daa0194
+ 00bf3758 bytes 5aaa0194
- 00bf36e4 ["INT_ADD", "register:40f0:8", ["const:bf36e4:8", "const:4:8"]]
- 00bf36e4 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf3780 ["INT_ADD", "register:40f0:8", ["const:bf3780:8", "const:4:8"]]
+ 00bf3780 ["CALL", null, ["callee:00c58010:8"]]
- 00bf36e4 bytes 17920194
+ 00bf3780 bytes 24920194
~~~


<a id="compare-455e6babb208e4d1f54603769e12901e"></a>

### [`00bf3720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3720.md) → [`00bf37bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf37bc.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6assignERKS5_mm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00bf33a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00bf343c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf343c.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3720.md#insn-00bf3770)
- 新版 `00bf380c`（命令位置の公開資料なし）

~~~diff
- 00bf3770 ["INT_ADD", "register:40f0:8", ["const:bf3770:8", "const:4:8"]]
- 00bf3770 ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf380c ["INT_ADD", "register:40f0:8", ["const:bf380c:8", "const:4:8"]]
+ 00bf380c ["CALL", null, ["callee:00bf2974:8"]]
- 00bf3770 bytes 5afcff97
+ 00bf380c bytes 5afcff97
~~~


<a id="compare-991b3359de96003759ce081c27b0ee75"></a>

### [`00bf3774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3774.md) → [`00bf3810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3810.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4copyEPwmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf37cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3774.md#insn-00bf37cc) · [`00bf37e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3774.md#insn-00bf37e4)
- 新版 `00bf3868`（命令位置の公開資料なし） · `00bf3880`（命令位置の公開資料なし）

~~~diff
- 00bf37cc ["INT_ADD", "register:40f0:8", ["const:bf37cc:8", "const:4:8"]]
- 00bf37cc ["CALL", null, ["callee:00c58010:8"]]
+ 00bf3868 ["INT_ADD", "register:40f0:8", ["const:bf3868:8", "const:4:8"]]
+ 00bf3868 ["CALL", null, ["callee:00c58010:8"]]
- 00bf37cc bytes dd910194
+ 00bf3868 bytes ea910194
- 00bf37e4 ["INT_ADD", "register:40f0:8", ["const:bf37e4:8", "const:4:8"]]
- 00bf37e4 ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf3880 ["INT_ADD", "register:40f0:8", ["const:bf3880:8", "const:4:8"]]
+ 00bf3880 ["CALL", null, ["callee:00bf2974:8"]]
- 00bf37e4 bytes 3dfcff97
+ 00bf3880 bytes 3dfcff97
~~~


<a id="compare-7557e8e867691d0c3498eb7782f83bdd"></a>

### [`00bf37e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf37e8.md) → [`00bf3884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3884.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEC2ERKS5_mmRKS4_

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a910.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c5a9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a9e0.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3888`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf37e8.md#insn-00bf3888) · [`00bf38a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf37e8.md#insn-00bf38a8) · [`00bf38cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf37e8.md#insn-00bf38cc)
- 新版 `00bf3924`（命令位置の公開資料なし） · `00bf3944`（命令位置の公開資料なし） · `00bf3968`（命令位置の公開資料なし）

~~~diff
- 00bf3888 ["INT_ADD", "register:40f0:8", ["const:bf3888:8", "const:4:8"]]
- 00bf3888 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf3924 ["INT_ADD", "register:40f0:8", ["const:bf3924:8", "const:4:8"]]
+ 00bf3924 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf3888 bytes 82910194
+ 00bf3924 bytes 8f910194
- 00bf38a8 ["INT_ADD", "register:40f0:8", ["const:bf38a8:8", "const:4:8"]]
- 00bf38a8 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf3944 ["INT_ADD", "register:40f0:8", ["const:bf3944:8", "const:4:8"]]
+ 00bf3944 ["CALL", null, ["callee:00c58010:8"]]
- 00bf38a8 bytes a6910194
+ 00bf3944 bytes b3910194
- 00bf38cc ["INT_ADD", "register:40f0:8", ["const:bf38cc:8", "const:4:8"]]
- 00bf38cc ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf3968 ["INT_ADD", "register:40f0:8", ["const:bf3968:8", "const:4:8"]]
+ 00bf3968 ["CALL", null, ["callee:00bf2974:8"]]
- 00bf38cc bytes 03fcff97
+ 00bf3968 bytes 03fcff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-589e43a1e4f39c900ae221fb4c05fe3d"></a>

### [`00bf38dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf38dc.md) → [`00bf3978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3978.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4findEwm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf38dc.md#insn-00bf3924)
- 新版 `00bf39c0`（命令位置の公開資料なし）

~~~diff
- 00bf3924 ["INT_ADD", "register:40f0:8", ["const:bf3924:8", "const:4:8"]]
- 00bf3924 ["CALL", null, ["callee:00c58520:8"]]
+ 00bf39c0 ["INT_ADD", "register:40f0:8", ["const:bf39c0:8", "const:4:8"]]
+ 00bf39c0 ["CALL", null, ["callee:00c58520:8"]]
- 00bf3924 bytes cb920194
+ 00bf39c0 bytes d8920194
~~~


<a id="compare-4c9921a083b34114fde1be692f69219d"></a>

### [`00bf3950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3950.md) → [`00bf39ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf39ec.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6__initEmw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf39bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3950.md#insn-00bf39bc) · [`00bf3a38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3950.md#insn-00bf3a38) · [`00bf3a3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3950.md#insn-00bf3a3c)
- 新版 `00bf3a58`（命令位置の公開資料なし） · `00bf3ad4`（命令位置の公開資料なし） · `00bf3ad8`（命令位置の公開資料なし）

~~~diff
- 00bf39bc ["INT_ADD", "register:40f0:8", ["const:bf39bc:8", "const:4:8"]]
- 00bf39bc ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf3a58 ["INT_ADD", "register:40f0:8", ["const:bf3a58:8", "const:4:8"]]
+ 00bf3a58 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf39bc bytes 35910194
+ 00bf3a58 bytes 42910194
- 00bf3a38 ["INT_ADD", "register:40f0:8", ["const:bf3a38:8", "const:4:8"]]
- 00bf3a38 ["CALL", null, ["callee:006d76f8:8"]]
+ 00bf3ad4 ["INT_ADD", "register:40f0:8", ["const:bf3ad4:8", "const:4:8"]]
+ 00bf3ad4 ["CALL", null, ["callee:006d76f8:8"]]
- 00bf3a38 bytes 1a8feb97
+ 00bf3ad4 bytes 098feb97
- 00bf3a3c ["INT_ADD", "register:40f0:8", ["const:bf3a3c:8", "const:4:8"]]
- 00bf3a3c ["CALL", null, ["callee:00440f00:8"]]
+ 00bf3ad8 ["INT_ADD", "register:40f0:8", ["const:bf3ad8:8", "const:4:8"]]
+ 00bf3ad8 ["CALL", null, ["callee:00440f00:8"]]
- 00bf3a3c bytes 2135e197
+ 00bf3ad8 bytes 0a35e197
~~~


<a id="compare-87936134184b2efe6a81a8b03c91fa47"></a>

### [`00bf3a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3a40.md) → [`00bf3adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3adc.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertEmPKw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md) [`00c5e020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md) [`00c5e0f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0f0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3a40.md#insn-00bf3a64)
- 新版 `00bf3b00`（命令位置の公開資料なし）

~~~diff
- 00bf3a64 ["INT_ADD", "register:40f0:8", ["const:bf3a64:8", "const:4:8"]]
- 00bf3a64 ["CALL", null, ["callee:00c5e0d0:8"]]
+ 00bf3b00 ["INT_ADD", "register:40f0:8", ["const:bf3b00:8", "const:4:8"]]
+ 00bf3b00 ["CALL", null, ["callee:00c5e0d0:8"]]
- 00bf3a64 bytes 67a90194
+ 00bf3b00 bytes 74a90194
~~~


<a id="compare-ff4fdec3be8d0c2cad1afda359c8c90d"></a>

### [`00bf3a8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3a8c.md) → [`00bf3b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3b28.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE12find_last_ofEPKwmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3af4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3a8c.md#insn-00bf3af4)
- 新版 `00bf3b90`（命令位置の公開資料なし）

~~~diff
- 00bf3af4 ["INT_ADD", "register:40f0:8", ["const:bf3af4:8", "const:4:8"]]
- 00bf3af4 ["CALL", null, ["callee:00c58520:8"]]
+ 00bf3b90 ["INT_ADD", "register:40f0:8", ["const:bf3b90:8", "const:4:8"]]
+ 00bf3b90 ["CALL", null, ["callee:00c58520:8"]]
- 00bf3af4 bytes 57920194
+ 00bf3b90 bytes 64920194
~~~


<a id="compare-2e027aa5db3f7d20063b742616f79233"></a>

### [`00bf3b28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3b28.md) → [`00bf3bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3bc4.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9__grow_byEmmmmmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3b28.md#insn-00bf3bdc) · [`00bf3bf8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3b28.md#insn-00bf3bf8) · [`00bf3c1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3b28.md#insn-00bf3c1c)
- 新版 `00bf3c78`（命令位置の公開資料なし） · `00bf3c94`（命令位置の公開資料なし） · `00bf3cb8`（命令位置の公開資料なし）

~~~diff
- 00bf3bdc ["INT_ADD", "register:40f0:8", ["const:bf3bdc:8", "const:4:8"]]
- 00bf3bdc ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf3c78 ["INT_ADD", "register:40f0:8", ["const:bf3c78:8", "const:4:8"]]
+ 00bf3c78 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf3bdc bytes ad900194
+ 00bf3c78 bytes ba900194
- 00bf3bf8 ["INT_ADD", "register:40f0:8", ["const:bf3bf8:8", "const:4:8"]]
- 00bf3bf8 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf3c94 ["INT_ADD", "register:40f0:8", ["const:bf3c94:8", "const:4:8"]]
+ 00bf3c94 ["CALL", null, ["callee:00c58010:8"]]
- 00bf3bf8 bytes d2900194
+ 00bf3c94 bytes df900194
- 00bf3c1c ["INT_ADD", "register:40f0:8", ["const:bf3c1c:8", "const:4:8"]]
- 00bf3c1c ["CALL", null, ["callee:00c58010:8"]]
+ 00bf3cb8 ["INT_ADD", "register:40f0:8", ["const:bf3cb8:8", "const:4:8"]]
+ 00bf3cb8 ["CALL", null, ["callee:00c58010:8"]]
- 00bf3c1c bytes c9900194
+ 00bf3cb8 bytes d6900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7456d9a59f6e74f3f3f3fca459d0ed58"></a>

### [`00bf3c68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3c68.md) → [`00bf3d04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3d04.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE9push_backEw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00c5e030`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e030.md) · 呼出先 1件 [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 1件 [`00c5e100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e100.md) · 呼出先 1件 [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3c68.md#insn-00bf3ccc)
- 新版 `00bf3d68`（命令位置の公開資料なし）

~~~diff
- 00bf3ccc ["INT_ADD", "register:40f0:8", ["const:bf3ccc:8", "const:4:8"]]
- 00bf3ccc ["CALL", null, ["callee:00c5a970:8"]]
+ 00bf3d68 ["INT_ADD", "register:40f0:8", ["const:bf3d68:8", "const:4:8"]]
+ 00bf3d68 ["CALL", null, ["callee:00c5a970:8"]]
- 00bf3ccc bytes f59a0194
+ 00bf3d68 bytes 029b0194
~~~


<a id="compare-2b677be4b990d765d7980068f5cbe919"></a>

### [`00bf3d10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3d10.md) → [`00bf3dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3dac.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEmw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3d10.md#insn-00bf3d88)
- 新版 `00bf3e24`（命令位置の公開資料なし）

~~~diff
- 00bf3d88 ["INT_ADD", "register:40f0:8", ["const:bf3d88:8", "const:4:8"]]
- 00bf3d88 ["CALL", null, ["callee:00c5a970:8"]]
+ 00bf3e24 ["INT_ADD", "register:40f0:8", ["const:bf3e24:8", "const:4:8"]]
+ 00bf3e24 ["CALL", null, ["callee:00c5a970:8"]]
- 00bf3d88 bytes c69a0194
+ 00bf3e24 bytes d39a0194
~~~


<a id="compare-834af41170384b486ee88a2f20b0c0fd"></a>

### [`00bf3e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3e90.md) → [`00bf3f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf3f2c.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6assignEmw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3e90.md#insn-00bf3ef4)
- 新版 `00bf3f90`（命令位置の公開資料なし）

~~~diff
- 00bf3ef4 ["INT_ADD", "register:40f0:8", ["const:bf3ef4:8", "const:4:8"]]
- 00bf3ef4 ["CALL", null, ["callee:00c5a970:8"]]
+ 00bf3f90 ["INT_ADD", "register:40f0:8", ["const:bf3f90:8", "const:4:8"]]
+ 00bf3f90 ["CALL", null, ["callee:00c5a970:8"]]
- 00bf3ef4 bytes 6b9a0194
+ 00bf3f90 bytes 789a0194
~~~


<a id="compare-823cb64e639a8d2dc1947713c522e644"></a>

### [`00bf3fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3fa8.md) → [`00bf4044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4044.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE5eraseEmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00bf4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4020.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00bf40bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf40bc.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf3fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3fa8.md#insn-00bf3fe0) · [`00bf401c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3fa8.md#insn-00bf401c)
- 新版 `00bf407c`（命令位置の公開資料なし） · `00bf40b8`（命令位置の公開資料なし）

~~~diff
- 00bf3fe0 ["INT_ADD", "register:40f0:8", ["const:bf3fe0:8", "const:4:8"]]
- 00bf3fe0 ["CALL", null, ["callee:00bf40bc:8"]]
+ 00bf407c ["INT_ADD", "register:40f0:8", ["const:bf407c:8", "const:4:8"]]
+ 00bf407c ["CALL", null, ["callee:00bf40bc:8"]]
- 00bf3fe0 bytes 10000094
+ 00bf407c bytes 10000094
- 00bf401c ["INT_ADD", "register:40f0:8", ["const:bf401c:8", "const:4:8"]]
- 00bf401c ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf40b8 ["INT_ADD", "register:40f0:8", ["const:bf40b8:8", "const:4:8"]]
+ 00bf40b8 ["CALL", null, ["callee:00bf2974:8"]]
- 00bf401c bytes 2ffaff97
+ 00bf40b8 bytes 2ffaff97
~~~


<a id="compare-f9810fd0ab012d7e4753d0b97fb3495f"></a>

### [`00bf4020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4020.md) → [`00bf40bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf40bc.md) FUN_00bf40bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 2件 [`00bf3fa8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf3fa8.md) [`00c36110`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c36/00c36110.md) · 呼出先 1件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 2件 [`00bf4044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4044.md) [`00c361ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c36/00c361ac.md) · 呼出先 1件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4020.md#insn-00bf4080)
- 新版 `00bf411c`（命令位置の公開資料なし）

~~~diff
- 00bf4080 ["INT_ADD", "register:40f0:8", ["const:bf4080:8", "const:4:8"]]
- 00bf4080 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf411c ["INT_ADD", "register:40f0:8", ["const:bf411c:8", "const:4:8"]]
+ 00bf411c ["CALL", null, ["callee:00c58010:8"]]
- 00bf4080 bytes b08f0194
+ 00bf411c bytes bd8f0194
~~~


<a id="compare-7c08dfc0d9f58631edb2d1c1472cadcf"></a>

### [`00bf40bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf40bc.md) → [`00bf4158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4158.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendERKS5_mm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf40bc.md#insn-00bf4158) · [`00bf4184`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf40bc.md#insn-00bf4184) · [`00bf41c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf40bc.md#insn-00bf41c4)
- 新版 `00bf41f4`（命令位置の公開資料なし） · `00bf4220`（命令位置の公開資料なし） · `00bf4260`（命令位置の公開資料なし）

~~~diff
- 00bf4158 ["INT_ADD", "register:40f0:8", ["const:bf4158:8", "const:4:8"]]
- 00bf4158 ["CALL", null, ["callee:00c5e0c0:8"]]
+ 00bf41f4 ["INT_ADD", "register:40f0:8", ["const:bf41f4:8", "const:4:8"]]
+ 00bf41f4 ["CALL", null, ["callee:00c5e0c0:8"]]
- 00bf4158 bytes a6a70194
+ 00bf41f4 bytes b3a70194
- 00bf4184 ["INT_ADD", "register:40f0:8", ["const:bf4184:8", "const:4:8"]]
- 00bf4184 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf4220 ["INT_ADD", "register:40f0:8", ["const:bf4220:8", "const:4:8"]]
+ 00bf4220 ["CALL", null, ["callee:00c58010:8"]]
- 00bf4184 bytes 6f8f0194
+ 00bf4220 bytes 7c8f0194
- 00bf41c4 ["INT_ADD", "register:40f0:8", ["const:bf41c4:8", "const:4:8"]]
- 00bf41c4 ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf4260 ["INT_ADD", "register:40f0:8", ["const:bf4260:8", "const:4:8"]]
+ 00bf4260 ["CALL", null, ["callee:00bf2974:8"]]
- 00bf41c4 bytes c5f9ff97
+ 00bf4260 bytes c5f9ff97
~~~


<a id="compare-cf3d6ad6fe2bf2ef3b7e8646de285413"></a>

### [`00bf41c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf41c8.md) → [`00bf4264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4264.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEPKw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md) [`00c5e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md) [`00c5e110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf41e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf41c8.md#insn-00bf41e8) · [`00bf422c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf41c8.md#insn-00bf422c) · [`00bf4258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf41c8.md#insn-00bf4258)
- 新版 `00bf4284`（命令位置の公開資料なし） · `00bf42c8`（命令位置の公開資料なし） · `00bf42f4`（命令位置の公開資料なし）

~~~diff
- 00bf41e8 ["INT_ADD", "register:40f0:8", ["const:bf41e8:8", "const:4:8"]]
- 00bf41e8 ["CALL", null, ["callee:00c5e0d0:8"]]
+ 00bf4284 ["INT_ADD", "register:40f0:8", ["const:bf4284:8", "const:4:8"]]
+ 00bf4284 ["CALL", null, ["callee:00c5e0d0:8"]]
- 00bf41e8 bytes 86a70194
+ 00bf4284 bytes 93a70194
- 00bf422c ["INT_ADD", "register:40f0:8", ["const:bf422c:8", "const:4:8"]]
- 00bf422c ["CALL", null, ["callee:00c5e110:8"]]
+ 00bf42c8 ["INT_ADD", "register:40f0:8", ["const:bf42c8:8", "const:4:8"]]
+ 00bf42c8 ["CALL", null, ["callee:00c5e110:8"]]
- 00bf422c bytes 85a70194
+ 00bf42c8 bytes 92a70194
- 00bf4258 ["INT_ADD", "register:40f0:8", ["const:bf4258:8", "const:4:8"]]
- 00bf4258 ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf42f4 ["INT_ADD", "register:40f0:8", ["const:bf42f4:8", "const:4:8"]]
+ 00bf42f4 ["CALL", null, ["callee:00bf2974:8"]]
- 00bf4258 bytes a0f9ff97
+ 00bf42f4 bytes a0f9ff97
~~~


<a id="compare-f9315264a5bbe3be50b84d784ec4d488"></a>

### [`00bf4260`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4260.md) → [`00bf42fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf42fc.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKwm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c5e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c5e110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf42c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4260.md#insn-00bf42c4) · [`00bf42e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4260.md#insn-00bf42e8)
- 新版 `00bf4360`（命令位置の公開資料なし） · `00bf4384`（命令位置の公開資料なし）

~~~diff
- 00bf42c4 ["INT_ADD", "register:40f0:8", ["const:bf42c4:8", "const:4:8"]]
- 00bf42c4 ["CALL", null, ["callee:00c5e110:8"]]
+ 00bf4360 ["INT_ADD", "register:40f0:8", ["const:bf4360:8", "const:4:8"]]
+ 00bf4360 ["CALL", null, ["callee:00c5e110:8"]]
- 00bf42c4 bytes 5fa70194
+ 00bf4360 bytes 6ca70194
- 00bf42e8 ["INT_ADD", "register:40f0:8", ["const:bf42e8:8", "const:4:8"]]
- 00bf42e8 ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf4384 ["INT_ADD", "register:40f0:8", ["const:bf4384:8", "const:4:8"]]
+ 00bf4384 ["CALL", null, ["callee:00bf2974:8"]]
- 00bf42e8 bytes 7cf9ff97
+ 00bf4384 bytes 7cf9ff97
~~~


<a id="compare-05ab799e043ed576c38e1ba3aca94ac9"></a>

### [`00bf42ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf42ec.md) → [`00bf4388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4388.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7compareEmmPKw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md) [`00c5e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md) [`00c5e110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf42ec.md#insn-00bf4318) · [`00bf4370`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf42ec.md#insn-00bf4370) · [`00bf43a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf42ec.md#insn-00bf43a0)
- 新版 `00bf43b4`（命令位置の公開資料なし） · `00bf440c`（命令位置の公開資料なし） · `00bf443c`（命令位置の公開資料なし）

~~~diff
- 00bf4318 ["INT_ADD", "register:40f0:8", ["const:bf4318:8", "const:4:8"]]
- 00bf4318 ["CALL", null, ["callee:00c5e0d0:8"]]
+ 00bf43b4 ["INT_ADD", "register:40f0:8", ["const:bf43b4:8", "const:4:8"]]
+ 00bf43b4 ["CALL", null, ["callee:00c5e0d0:8"]]
- 00bf4318 bytes 3aa70194
+ 00bf43b4 bytes 47a70194
- 00bf4370 ["INT_ADD", "register:40f0:8", ["const:bf4370:8", "const:4:8"]]
- 00bf4370 ["CALL", null, ["callee:00c5e110:8"]]
+ 00bf440c ["INT_ADD", "register:40f0:8", ["const:bf440c:8", "const:4:8"]]
+ 00bf440c ["CALL", null, ["callee:00c5e110:8"]]
- 00bf4370 bytes 34a70194
+ 00bf440c bytes 41a70194
- 00bf43a0 ["INT_ADD", "register:40f0:8", ["const:bf43a0:8", "const:4:8"]]
- 00bf43a0 ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf443c ["INT_ADD", "register:40f0:8", ["const:bf443c:8", "const:4:8"]]
+ 00bf443c ["CALL", null, ["callee:00bf2974:8"]]
- 00bf43a0 bytes 4ef9ff97
+ 00bf443c bytes 4ef9ff97
~~~


<a id="compare-ac71d0e82aab0b261cb74d95014d78e6"></a>

### [`00bf43a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43a4.md) → [`00bf4440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4440.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE2atEm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf43e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43a4.md#insn-00bf43e8)
- 新版 `00bf4484`（命令位置の公開資料なし）

~~~diff
- 00bf43e8 ["INT_ADD", "register:40f0:8", ["const:bf43e8:8", "const:4:8"]]
- 00bf43e8 ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf4484 ["INT_ADD", "register:40f0:8", ["const:bf4484:8", "const:4:8"]]
+ 00bf4484 ["CALL", null, ["callee:00bf2974:8"]]
- 00bf43e8 bytes 3cf9ff97
+ 00bf4484 bytes 3cf9ff97
~~~


<a id="compare-264a5c266c79eb338eb954484f56deab"></a>

### [`00bf43f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43f4.md) → [`00bf4490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4490.md) FUN_00bf4490

採用 · 移動量 `+0x9c` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf43ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43ec.md) · 呼出先 2件 [`00bf33a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf3/00bf33a0.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md)
- 新版 呼出元 1件 [`00bf4488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4488.md) · 呼出先 2件 [`00bf343c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf3/00bf343c.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf43f4.md#insn-00bf4410)
- 新版 `00bf44ac`（命令位置の公開資料なし）

~~~diff
- 00bf4410 ["INT_ADD", "register:40f0:8", ["const:bf4410:8", "const:4:8"]]
- 00bf4410 ["CALL", null, ["callee:00c5e0d0:8"]]
+ 00bf44ac ["INT_ADD", "register:40f0:8", ["const:bf44ac:8", "const:4:8"]]
+ 00bf44ac ["CALL", null, ["callee:00c5e0d0:8"]]
- 00bf4410 bytes fca60194
+ 00bf44ac bytes 09a70194
~~~


<a id="compare-473d612f815f44239de3b5fe12e52172"></a>

### [`00bf4430`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4430.md) → [`00bf44cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf44cc.md) _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE4findEPKwmm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c58450`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58450.md) [`00c5e040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58520.md) [`00c5e110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e110.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf44dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4430.md#insn-00bf44dc) · [`00bf44f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4430.md#insn-00bf44f0)
- 新版 `00bf4578`（命令位置の公開資料なし） · `00bf458c`（命令位置の公開資料なし）

~~~diff
- 00bf44dc ["INT_ADD", "register:40f0:8", ["const:bf44dc:8", "const:4:8"]]
- 00bf44dc ["CALL", null, ["callee:00c58520:8"]]
+ 00bf4578 ["INT_ADD", "register:40f0:8", ["const:bf4578:8", "const:4:8"]]
+ 00bf4578 ["CALL", null, ["callee:00c58520:8"]]
- 00bf44dc bytes dd8f0194
+ 00bf4578 bytes ea8f0194
- 00bf44f0 ["INT_ADD", "register:40f0:8", ["const:bf44f0:8", "const:4:8"]]
- 00bf44f0 ["CALL", null, ["callee:00c5e110:8"]]
+ 00bf458c ["INT_ADD", "register:40f0:8", ["const:bf458c:8", "const:4:8"]]
+ 00bf458c ["CALL", null, ["callee:00c5e110:8"]]
- 00bf44f0 bytes d4a60194
+ 00bf458c bytes e1a60194
~~~


<a id="compare-40ee624b121cfef6069a19cdfda35c27"></a>

### [`00bf4620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4620.md) → [`00bf46bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf46bc.md) FUN_00bf46bc

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf45c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf45c8.md) · 呼出先 5件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`006d76a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d7/006d76a0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00bf4664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4664.md) · 呼出先 5件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`006d76f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006d7/006d76f8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf4660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4620.md#insn-00bf4660) · [`00bf46a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4620.md#insn-00bf46a8) · [`00bf46b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4620.md#insn-00bf46b8)
- 新版 `00bf46fc`（命令位置の公開資料なし） · `00bf4744`（命令位置の公開資料なし） · `00bf4754`（命令位置の公開資料なし）

~~~diff
- 00bf4660 ["INT_ADD", "register:40f0:8", ["const:bf4660:8", "const:4:8"]]
- 00bf4660 ["CALL", null, ["callee:00c58010:8"]]
+ 00bf46fc ["INT_ADD", "register:40f0:8", ["const:bf46fc:8", "const:4:8"]]
+ 00bf46fc ["CALL", null, ["callee:00c58010:8"]]
- 00bf4660 bytes 388e0194
+ 00bf46fc bytes 458e0194
- 00bf46a8 ["INT_ADD", "register:40f0:8", ["const:bf46a8:8", "const:4:8"]]
- 00bf46a8 ["CALL", null, ["callee:00c57f60:8"]]
+ 00bf4744 ["INT_ADD", "register:40f0:8", ["const:bf4744:8", "const:4:8"]]
+ 00bf4744 ["CALL", null, ["callee:00c57f60:8"]]
- 00bf46a8 bytes fa8d0194
+ 00bf4744 bytes 078e0194
- 00bf46b8 ["INT_ADD", "register:40f0:8", ["const:bf46b8:8", "const:4:8"]]
- 00bf46b8 ["CALL", null, ["callee:00c580d0:8"]]
+ 00bf4754 ["INT_ADD", "register:40f0:8", ["const:bf4754:8", "const:4:8"]]
+ 00bf4754 ["CALL", null, ["callee:00c580d0:8"]]
- 00bf46b8 bytes 528e0194
+ 00bf4754 bytes 5f8e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7731514f9f052687d3f210388427ee5"></a>

### [`00bf46f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf46f4.md) → [`00bf4790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4790.md) FUN_00bf4790

採用 · 移動量 `+0x9c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 1件 [`00bf45c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf45c8.md) · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md)
- 新版 呼出元 1件 [`00bf4664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4664.md) · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf473c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf46f4.md#insn-00bf473c) · [`00bf4768`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf46f4.md#insn-00bf4768)
- 新版 `00bf47d8`（命令位置の公開資料なし） · `00bf4804`（命令位置の公開資料なし）

~~~diff
- 00bf473c ["INT_ADD", "register:40f0:8", ["const:bf473c:8", "const:4:8"]]
- 00bf473c ["CALL", null, ["callee:00c58010:8"]]
+ 00bf47d8 ["INT_ADD", "register:40f0:8", ["const:bf47d8:8", "const:4:8"]]
+ 00bf47d8 ["CALL", null, ["callee:00c58010:8"]]
- 00bf473c bytes 018e0194
+ 00bf47d8 bytes 0e8e0194
- 00bf4768 ["INT_ADD", "register:40f0:8", ["const:bf4768:8", "const:4:8"]]
- 00bf4768 ["CALL", null, ["callee:00c5e0c0:8"]]
+ 00bf4804 ["INT_ADD", "register:40f0:8", ["const:bf4804:8", "const:4:8"]]
+ 00bf4804 ["CALL", null, ["callee:00c5e0c0:8"]]
- 00bf4768 bytes 22a60194
+ 00bf4804 bytes 2fa60194
~~~


<a id="compare-3b941a46efd43c50a303c4c5886b8ec0"></a>

### [`00bf4784`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4784.md) → [`00bf4820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4820.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6appendEPKw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5dff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dff0.md) [`00c5e000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e000.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5e0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0c0.md) [`00c5e0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0d0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf47a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4784.md#insn-00bf47a8) · [`00bf4804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4784.md#insn-00bf4804) · [`00bf482c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf4784.md#insn-00bf482c)
- 新版 `00bf4844`（命令位置の公開資料なし） · `00bf48a0`（命令位置の公開資料なし） · `00bf48c8`（命令位置の公開資料なし）

~~~diff
- 00bf47a8 ["INT_ADD", "register:40f0:8", ["const:bf47a8:8", "const:4:8"]]
- 00bf47a8 ["CALL", null, ["callee:00c5e0d0:8"]]
+ 00bf4844 ["INT_ADD", "register:40f0:8", ["const:bf4844:8", "const:4:8"]]
+ 00bf4844 ["CALL", null, ["callee:00c5e0d0:8"]]
- 00bf47a8 bytes 16a60194
+ 00bf4844 bytes 23a60194
- 00bf4804 ["INT_ADD", "register:40f0:8", ["const:bf4804:8", "const:4:8"]]
- 00bf4804 ["CALL", null, ["callee:00c5e0c0:8"]]
+ 00bf48a0 ["INT_ADD", "register:40f0:8", ["const:bf48a0:8", "const:4:8"]]
+ 00bf48a0 ["CALL", null, ["callee:00c5e0c0:8"]]
- 00bf4804 bytes fba50194
+ 00bf48a0 bytes 08a60194
- 00bf482c ["INT_ADD", "register:40f0:8", ["const:bf482c:8", "const:4:8"]]
- 00bf482c ["CALL", null, ["callee:00c58010:8"]]
+ 00bf48c8 ["INT_ADD", "register:40f0:8", ["const:bf48c8:8", "const:4:8"]]
+ 00bf48c8 ["CALL", null, ["callee:00c58010:8"]]
- 00bf482c bytes c58d0194
+ 00bf48c8 bytes d28d0194
~~~


<a id="compare-ab80fb8f3826df8d2b27f1f27ca76781"></a>

### [`00bf486c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf486c.md) → [`00bf4908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4908.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE7replaceEmmRKS5_mm

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bf28d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf28d8.md) [`00c5dfe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5d/00c5dfe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bf2974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf2/00bf2974.md) [`00c5e0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e0b0.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf48b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf486c.md#insn-00bf48b8)
- 新版 `00bf4954`（命令位置の公開資料なし）

~~~diff
- 00bf48b8 ["INT_ADD", "register:40f0:8", ["const:bf48b8:8", "const:4:8"]]
- 00bf48b8 ["CALL", null, ["callee:00bf2974:8"]]
+ 00bf4954 ["INT_ADD", "register:40f0:8", ["const:bf4954:8", "const:4:8"]]
+ 00bf4954 ["CALL", null, ["callee:00bf2974:8"]]
- 00bf48b8 bytes 08f8ff97
+ 00bf4954 bytes 08f8ff97
~~~


<a id="compare-c117367fd99fd25d6a454324d987e5d7"></a>

### [`00bf48bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf48bc.md) → [`00bf4958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4958.md) _ZNSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE6insertENS_11__wrap_iterIPKwEEw

採用 · 移動量 `+0x9c` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c5a8a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a8a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c5a970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a970.md)

変更の種類 constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bf493c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf48bc.md#insn-00bf493c) · [`00bf496c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf4/00bf48bc.md#insn-00bf496c)
- 新版 `00bf49d8`（命令位置の公開資料なし） · `00bf4a08`（命令位置の公開資料なし）

~~~diff
- 00bf493c ["INT_ADD", "register:40f0:8", ["const:bf493c:8", "const:4:8"]]
- 00bf493c ["CALL", null, ["callee:00c5a970:8"]]
+ 00bf49d8 ["INT_ADD", "register:40f0:8", ["const:bf49d8:8", "const:4:8"]]
+ 00bf49d8 ["CALL", null, ["callee:00c5a970:8"]]
- 00bf493c bytes d9970194
+ 00bf49d8 bytes e6970194
- 00bf496c ["INT_ADD", "register:40f0:8", ["const:bf496c:8", "const:4:8"]]
- 00bf496c ["CALL", null, ["callee:00c58010:8"]]
+ 00bf4a08 ["INT_ADD", "register:40f0:8", ["const:bf4a08:8", "const:4:8"]]
+ 00bf4a08 ["CALL", null, ["callee:00c58010:8"]]
- 00bf496c bytes 758d0194
+ 00bf4a08 bytes 828d0194
~~~


